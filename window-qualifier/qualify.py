#!/usr/bin/env python3
"""Qualify companies by scraping their own websites.

Answers one question per company: does this business install or replace windows in
homes and buildings? Vehicles, window cleaning, blinds and window film do not count.

Scraping the site directly rather than asking a language model per company is what
makes this cheap: a full 1,700-company run costs a few minutes of bandwidth and no
model tokens at all. Evidence is the company's own page text, quoted verbatim, so
every verdict can be checked by hand.

Usage
-----
    python3 qualify.py --input companies.csv --out qualified.csv
    python3 qualify.py --input companies.csv --out qualified.csv --workers 16
    python3 qualify.py --input companies.csv --out qualified.csv --only-ambiguous

Results are cached per domain under ./cache, so a re-run costs nothing for sites
already fetched and an interrupted run resumes where it stopped.
"""
from __future__ import annotations

import argparse
import concurrent.futures as cf
import csv
import hashlib
import json
import os
import re
import sys
import threading
import time
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")
TIMEOUT = 15
MAX_PAGES = 4          # homepage + up to 3 promising internal pages
CACHE_DIR = "cache"

# Internal links worth following, most promising first.
LINK_HINTS = re.compile(
    r'(window|glass|glazing|service|product|residential|commercial|replace|install)', re.I)
SKIP_LINKS = re.compile(
    r'(blog|news|career|privacy|terms|login|cart|account|financing|review|gallery/\d)', re.I)

# ---------------------------------------------------------------- verdict rules

# Building-window work. These are what earns a YES.
POSITIVE = [
    # allow a qualifier between the noun and the verb: "window glass replacement",
    # "window and door installation" are both extremely common phrasings
    (r'windows?\s+(\w+\s+){0,2}(replacement|installation|install\b|repair|replac\w+)',
     'window replacement/installation'),
    (r'replacement windows?', 'replacement windows'),
    (r're-?glaz\w+', 'reglazing'),
    (r'(residential|commercial|home|house|building)\s+glass\s+(replacement|repair|service)',
     'building glass replacement'),
    (r'(new|energy[- ]efficient|vinyl|fiberglass|aluminum|wood|impact) windows?', 'window product line'),
    (r'windows? (and|&) doors?', 'windows & doors'),
    (r'(install|replace|replacing)\w* (new )?windows?', 'installs/replaces windows'),
    (r'(double|triple|single)[- ]pane', 'pane glazing work'),
    (r'(insulated glass|igu|thermal pane|foggy window|failed seal)', 'insulated glass unit work'),
    (r'(storefront|curtain wall|commercial glazing|glazier)', 'commercial storefront glazing'),
    (r'broken window (glass|repair|replacement)', 'broken window glass'),
    (r'(casement|double[- ]hung|single[- ]hung|awning|bay window|bow window|picture window|slider window)',
     'named window styles'),
]

# Vehicle work. Presence alone is not disqualifying — many shops do both — but it
# is recorded so the client can filter, and it decides otherwise-empty sites.
VEHICLE = re.compile(
    r'(windshield|auto glass|automotive glass|vehicle glass|car window|'
    r'side mirror|rock chip|adas calibration)', re.I)

# Services that look window-ish but are not installation or repair.
NEGATIVE_ONLY = [
    (r'window clean|window wash|squeegee|pressure wash|power wash', 'window cleaning'),
    (r'window (tint|film)|solar screen', 'window tint/film'),
    (r'\b(blinds|shades|shutters|drapery|draperies|window treatment|window covering)\b',
     'window treatments'),
]

SENTENCE = re.compile(r'[^.!?\n]{0,180}[.!?]')


def cache_path(domain: str) -> str:
    h = hashlib.sha1(domain.encode()).hexdigest()[:16]
    return os.path.join(CACHE_DIR, f"{h}.json")


def visible_text(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup(["script", "style", "noscript", "svg"]):
        tag.decompose()
    return re.sub(r'\s+', ' ', soup.get_text(" "))


def pick_links(html: str, base: str, limit: int) -> list[str]:
    """Internal links most likely to describe services, best first."""
    soup = BeautifulSoup(html, "html.parser")
    host = urlparse(base).netloc
    scored: list[tuple[int, str]] = []
    seen = set()
    for a in soup.find_all("a", href=True):
        url = urljoin(base, a["href"]).split("#")[0]
        if urlparse(url).netloc != host or url in seen:
            continue
        blob = (a.get_text(" ") or "") + " " + url
        if SKIP_LINKS.search(blob):
            continue
        score = len(LINK_HINTS.findall(blob))
        if "window" in blob.lower():
            score += 5           # a page named for windows answers the question outright
        if score:
            seen.add(url)
            scored.append((score, url))
    scored.sort(key=lambda t: -t[0])
    return [u for _, u in scored[:limit]]


def fetch_site(domain: str, session: requests.Session) -> dict:
    """Fetch a site's homepage plus a few service pages. Returns a cacheable dict."""
    out = {"domain": domain, "ok": False, "status": None, "pages": [], "text": "", "error": ""}
    base = None
    for scheme in ("https://", "http://"):
        try:
            r = session.get(scheme + domain, timeout=TIMEOUT,
                            headers={"User-Agent": UA}, allow_redirects=True)
            out["status"] = r.status_code
            if r.status_code < 400 and r.text:
                base, home = r.url, r.text
                break
        except requests.RequestException as e:
            out["error"] = f"{type(e).__name__}: {str(e)[:120]}"
    if base is None:
        return out

    texts = [visible_text(home)]
    out["pages"].append(base)
    for url in pick_links(home, base, MAX_PAGES - 1):
        try:
            r = session.get(url, timeout=TIMEOUT, headers={"User-Agent": UA})
            if r.status_code < 400 and r.text:
                texts.append(visible_text(r.text))
                out["pages"].append(url)
        except requests.RequestException:
            continue
        time.sleep(0.2)          # be polite to one host

    out["ok"] = True
    out["text"] = " ".join(texts)[:400_000]
    return out


def quote_for(text: str, pattern: str) -> str:
    """A short verbatim sentence containing the match, for the evidence column."""
    m = re.search(pattern, text, re.I)
    if not m:
        return ""
    start = max(0, m.start() - 90)
    snippet = text[start:m.end() + 90]
    matched = m.group(0).lower()
    # The quote must contain the phrase that triggered the verdict, or it cannot be
    # audited. Fall back to a window around the match rather than any long sentence.
    for s in SENTENCE.findall(snippet):
        if matched in s.lower():
            return re.sub(r'\s+', ' ', s).strip()[:220]
    return re.sub(r'\s+', ' ', snippet).strip()[:220]


def judge(text: str) -> dict:
    """Decide from site text alone. Returns verdict, evidence and matched signals."""
    hits = [(label, pat) for pat, label in POSITIVE if re.search(pat, text, re.I)]
    negs = [label for pat, label in NEGATIVE_ONLY if re.search(pat, text, re.I)]
    vehicle = bool(VEHICLE.search(text))

    # Thin text is only inconclusive when it also says nothing useful. A short
    # one-page site that states the service outright still gets a verdict.
    if not (hits or negs or vehicle) and len(text or "") < 200:
        return {"verdict": "UNKNOWN", "evidence": "", "signals": "", "vehicle": False,
                "note": "site returned little or no readable text"}

    if hits:
        # Distinguish real window work from a passing mention on an unrelated site.
        strong = [l for l, p in hits if l in (
            'window replacement/installation', 'replacement windows', 'windows & doors',
            'installs/replaces windows', 'insulated glass unit work',
            'commercial storefront glazing', 'broken window glass')]
        verdict = "YES" if strong or len(hits) >= 2 else "LIKELY"
        label, pat = hits[0]
        return {"verdict": verdict, "evidence": quote_for(text, pat),
                "signals": "; ".join(sorted({l for l, _ in hits})),
                "vehicle": vehicle,
                "note": ("also does vehicle glass" if vehicle else "")
                        + ((" | also: " + ", ".join(negs)) if negs else "")}

    if vehicle:
        return {"verdict": "NO", "evidence": quote_for(text, VEHICLE.pattern),
                "signals": "vehicle glass only", "vehicle": True,
                "note": "vehicle glass, no building-window work found"}
    if negs:
        return {"verdict": "NO", "evidence": quote_for(text, NEGATIVE_ONLY[0][0]),
                "signals": "; ".join(negs), "vehicle": False,
                "note": "window-adjacent service that is not installation or repair"}
    return {"verdict": "NO", "evidence": "", "signals": "", "vehicle": False,
            "note": "no window installation or repair signal on site"}


def load_companies(path: str) -> list[dict]:
    """Read the export. Company names contain commas and spill across columns, and
    there is no header row, so fields are located by shape rather than position."""
    phone = re.compile(r'^\+?1[\s\-]?\d{3}')
    addr = re.compile(r',\s*[A-Z]{2}\s*\d{5}')
    out = []
    with open(path, encoding="utf-8", errors="replace") as fh:
        for row in csv.reader(fh):
            if not any(c.strip() for c in row):
                continue
            iu = next((i for i, c in enumerate(row)
                       if c.startswith("http") and "googleusercontent" not in c), None)
            ip = next((i for i, c in enumerate(row) if phone.match(c or "")), None)
            ia = next((i for i, c in enumerate(row) if addr.search(c or "")), None)
            end = min([x for x in (ip, ia, iu) if x is not None], default=1)
            name = " ".join(c.strip() for c in row[:end] if c.strip()) or (row[0] or "").strip()
            if name.lower() in ("", "company name"):
                continue
            url = row[iu] if iu is not None else ""
            m = re.match(r'https?://(?:www\.)?([^/?#]+)', url or "")
            nums = [c for c in row[(iu + 1) if iu is not None else 0:]
                    if re.fullmatch(r'\d+(\.\d+)?', (c or "").strip())]
            out.append({
                "name": name,
                "website": url,
                "domain": m.group(1).lower() if m else "",
                "phone": row[ip] if ip is not None else "",
                "address": row[ia] if ia is not None else "",
                "rating": nums[0] if nums else "",
                "review_count": nums[1] if len(nums) > 1 else "",
            })
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--input", required=True, help="companies CSV export")
    ap.add_argument("--out", required=True, help="output CSV path")
    ap.add_argument("--workers", type=int, default=12)
    ap.add_argument("--limit", type=int, default=0, help="stop after N companies (for testing)")
    ap.add_argument("--cache", default=CACHE_DIR)
    args = ap.parse_args()

    os.makedirs(args.cache, exist_ok=True)
    globals()["CACHE_DIR"] = args.cache

    companies = load_companies(args.input)
    if args.limit:
        companies = companies[:args.limit]
    with_site = [c for c in companies if c["domain"]]
    print(f"{len(companies)} companies | {len(with_site)} with a website "
          f"| {len(companies) - len(with_site)} without", file=sys.stderr)

    lock = threading.Lock()
    done = [0]
    session_local = threading.local()

    def get_session() -> requests.Session:
        if not hasattr(session_local, "s"):
            session_local.s = requests.Session()
        return session_local.s

    def work(c: dict) -> dict:
        path = cache_path(c["domain"])
        if os.path.exists(path):
            with open(path) as fh:
                site = json.load(fh)
        else:
            site = fetch_site(c["domain"], get_session())
            with open(path, "w") as fh:
                json.dump(site, fh)
        v = judge(site.get("text", ""))
        if not site.get("ok"):
            v = {"verdict": "UNREACHABLE", "evidence": "", "signals": "", "vehicle": False,
                 "note": site.get("error") or f"HTTP {site.get('status')}"}
        with lock:
            done[0] += 1
            if done[0] % 25 == 0:
                print(f"  {done[0]}/{len(with_site)}", file=sys.stderr)
        return {**c, "verdict": v["verdict"], "window_services": v["signals"],
                "also_vehicle_glass": v["vehicle"], "evidence": v["evidence"],
                "note": v["note"], "pages_checked": " | ".join(site.get("pages", [])[:4])}

    results = []
    with cf.ThreadPoolExecutor(max_workers=args.workers) as pool:
        for r in pool.map(work, with_site):
            results.append(r)
    for c in companies:
        if not c["domain"]:
            results.append({**c, "verdict": "NO_WEBSITE", "window_services": "",
                            "also_vehicle_glass": False, "evidence": "",
                            "note": "no website in source data", "pages_checked": ""})

    cols = ["name", "website", "domain", "phone", "address", "rating", "review_count",
            "verdict", "window_services", "also_vehicle_glass", "evidence", "note",
            "pages_checked"]
    with open(args.out, "w", newline="") as fh:
        w = csv.DictWriter(fh, cols)
        w.writeheader()
        w.writerows(results)

    tally: dict[str, int] = {}
    for r in results:
        tally[r["verdict"]] = tally.get(r["verdict"], 0) + 1
    print(f"\nwrote {args.out}", file=sys.stderr)
    for k in sorted(tally, key=lambda k: -tally[k]):
        print(f"  {tally[k]:5d}  {k}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
