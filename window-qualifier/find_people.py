#!/usr/bin/env python3
"""Find decision-maker names, roles and emails published on company websites.

Crawls each company's own site — contact, about, team, leadership and staff pages —
and extracts email addresses together with whatever name and job title the page
attaches to them. Only addresses actually present on a page are reported; nothing is
guessed from a pattern, because an invented address bounces and bounces damage the
sending domain's reputation.

Usage
-----
    python3 find_people.py --input WINDOW_LEADS_final.csv --out people.csv
    python3 find_people.py --input WINDOW_LEADS_final.csv --out people.csv --workers 16

Pages are cached under ./people_cache, so re-runs and rule changes cost no bandwidth.
"""
from __future__ import annotations

import argparse
import concurrent.futures as cf
import csv
import hashlib
import html
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
HEADERS = {"User-Agent": UA,
           "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
           "Accept-Language": "en-US,en;q=0.9"}
TIMEOUT = 15
MAX_PAGES = 8
CACHE_DIR = "people_cache"

# Pages where a business publishes its people.
PEOPLE_LINK = re.compile(
    r'(contact|about|team|our-?team|meet|staff|people|leadership|management|'
    r'who-?we-?are|our-?story|owner|founder|executive|careers?/?$|company)', re.I)
SKIP_LINK = re.compile(r'(\.pdf|\.jpg|\.png|\.zip|/tag/|/category/|/product/|/cart|'
                       r'/privacy|/terms|/blog|/news|/press|/article|/post/|/\d{4}/\d{2}/|'
                       r'facebook\.com|instagram\.com|twitter\.com)', re.I)

EMAIL_RE = re.compile(r'[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}')
# "name (at) domain (dot) com" and similar light obfuscation
OBFUSCATED = re.compile(
    r'([A-Za-z0-9._%+\-]+)\s*(?:\(at\)|\[at\]|\s+at\s+)\s*([A-Za-z0-9.\-]+)\s*'
    r'(?:\(dot\)|\[dot\]|\s+dot\s+)\s*([A-Za-z]{2,})', re.I)

# Addresses that are never a person.
JUNK_EMAIL = re.compile(
    r'(^|@)(example|test|domain|yourname|email|sentry|wix|squarespace|godaddy|'
    r'godaddysites|jquery|wordpress|sentry\.io)', re.I)
IMAGE_EXT = re.compile(r'\.(png|jpe?g|gif|svg|webp|ico|css|js)$', re.I)

# Decision-maker roles the client asked for, highest authority first.
ROLE_PATTERNS = [
    (re.compile(r'\b(chief executive officer|ceo)\b', re.I), 'CEO', 1),
    (re.compile(r'\b(co[- ]?founder|founder)\b', re.I), 'Founder', 1),
    (re.compile(r'\b(co[- ]?owner|owner|proprietor)\b', re.I), 'Owner', 1),
    (re.compile(r'\b(president)\b', re.I), 'President', 1),
    (re.compile(r'\b(managing (director|partner|member))\b', re.I), 'Managing Director', 1),
    (re.compile(r'\b(chief operating officer|coo)\b', re.I), 'COO', 2),
    (re.compile(r'\b(chief financial officer|cfo)\b', re.I), 'CFO', 2),
    (re.compile(r'\b(chief (marketing|revenue|sales) officer|cmo|cro)\b', re.I), 'C-suite', 2),
    (re.compile(r'\b(vice president|vp)\b.{0,24}\b(sales|revenue|business)\b', re.I), 'VP Sales', 2),
    (re.compile(r'\b(vice president|vp)\b.{0,24}\b(marketing)\b', re.I), 'VP Marketing', 2),
    (re.compile(r'\b(vice president|vp)\b', re.I), 'VP', 3),
    (re.compile(r'\b(regional sales (director|manager))\b', re.I), 'Regional Sales Director', 2),
    (re.compile(r'\b((director of |)sales director|director of sales|head of sales)\b', re.I),
     'Sales Director', 2),
    (re.compile(r'\b(marketing director|director of marketing|head of marketing)\b', re.I),
     'Marketing Director', 2),
    (re.compile(r'\b(general manager|gm)\b', re.I), 'General Manager', 3),
    (re.compile(r'\b(partner|principal)\b', re.I), 'Partner', 3),
    (re.compile(r'\b(sales manager|business development)\b', re.I), 'Sales Manager', 3),
    (re.compile(r'\b(operations manager|office manager)\b', re.I), 'Manager', 4),
]

# Role-shaped mailbox names, used when a page gives no person.
ROLE_MAILBOX = re.compile(r'^(info|contact|hello|sales|admin|office|service|support|'
                          r'estimates?|quotes?|help|team|inquiries|customerservice)@', re.I)

NAME_RE = re.compile(r'\b([A-Z][a-z]{1,15})\s+([A-Z][a-z\'\-]{1,20})\b')


def cache_path(domain: str) -> str:
    return os.path.join(CACHE_DIR, hashlib.sha1(domain.encode()).hexdigest()[:16] + ".json")


def classify_role(text: str):
    """Return (label, tier) for the highest-authority role named in text."""
    best = None
    for pat, label, tier in ROLE_PATTERNS:
        if pat.search(text or ""):
            if best is None or tier < best[1]:
                best = (label, tier)
    return best or (None, 9)


def emails_from(soup: BeautifulSoup, raw: str, domain: str) -> dict:
    """Map each address found on the page to the text surrounding it."""
    found = {}

    def add(addr, ctx):
        addr = addr.strip().strip('.').lower()
        if not addr or IMAGE_EXT.search(addr) or JUNK_EMAIL.search(addr):
            return
        if len(addr) > 80:
            return
        found.setdefault(addr, "")
        if ctx and len(found[addr]) < 400:
            found[addr] = (found[addr] + " " + ctx).strip()

    for a in soup.find_all("a", href=True):
        if a["href"].lower().startswith("mailto:"):
            addr = a["href"][7:].split("?")[0]
            # the link's own text and its surrounding block both carry the person
            ctx = " ".join(filter(None, [
                a.get_text(" ", strip=True),
                a.find_parent(["li", "div", "td", "p", "article", "section"]).get_text(
                    " ", strip=True)[:300] if a.find_parent(
                    ["li", "div", "td", "p", "article", "section"]) else ""]))
            add(addr, ctx)

    text = soup.get_text(" ")
    for m in EMAIL_RE.finditer(text):
        add(m.group(0), text[max(0, m.start() - 200): m.end() + 200])
    for m in EMAIL_RE.finditer(raw):           # addresses only present in markup
        add(m.group(0), "")
    for m in OBFUSCATED.finditer(text):
        add(f"{m.group(1)}@{m.group(2)}.{m.group(3)}",
            text[max(0, m.start() - 200): m.end() + 200])
    return found


def person_near(ctx: str, addr: str):
    """Best guess at the person's name and role from text around the address."""
    ctx = html.unescape(re.sub(r'\s+', ' ', ctx or ''))
    role, tier = classify_role(ctx)

    name = None
    # a name immediately before the role word reads as "Jane Smith, Owner"
    if role:
        for pat, label, _ in ROLE_PATTERNS:
            m = pat.search(ctx)
            if m and label == role:
                before = ctx[max(0, m.start() - 60): m.start()]
                names = NAME_RE.findall(before)
                if names:
                    name = " ".join(names[-1])
                else:
                    after = ctx[m.end(): m.end() + 60]
                    names = NAME_RE.findall(after)
                    if names:
                        name = " ".join(names[0])
                break
    if not name:
        local = addr.split("@")[0]
        if not ROLE_MAILBOX.match(addr) and re.fullmatch(r'[a-z]+[._-][a-z]+', local):
            name = " ".join(p.capitalize() for p in re.split(r'[._-]', local))
    return name, role, tier


# "Jane Smith, Owner"  /  "Owner: Jane Smith"  /  "Jane Smith – Founder & CEO"
PERSON_ROLE = re.compile(
    r'\b([A-Z][a-z\'\-]{1,15}(?:\s+[A-Z]\.)?\s+[A-Z][a-z\'\-]{1,20})\s*'
    r'(?:,|\s+[-–—|]\s*|\s+is\s+(?:the\s+|our\s+)?|\s+)\s*'
    r'((?:co[- ]?)?(?:founder|owner|president|ceo|chief executive|coo|cfo|'
    r'vice president|vp[^a-z]|general manager|managing (?:director|partner)|'
    r'(?:regional\s+)?sales director|director of sales|marketing director|'
    r'director of marketing|head of sales|partner|principal)[a-z ]{0,24})', re.I)
ROLE_PERSON = re.compile(
    r'\b((?:co[- ]?)?(?:founder|owner|president|ceo|coo|cfo|general manager|'
    r'(?:regional\s+)?sales director|marketing director|vice president)[a-z ]{0,20})'
    r'\s*(?::|,|\s+[-–—|]\s*)\s*([A-Z][a-z\'\-]{1,15}\s+[A-Z][a-z\'\-]{1,20})', re.I)

NOT_NAME_WORD = {
    'press', 'release', 'announces', 'announced', 'named', 'names', 'retire', 'retires',
    'retirement', 'continue', 'continues', 'join', 'joins', 'joined', 'welcome', 'welcomes',
    'as', 'and', 'or', 'of', 'the', 'to', 'new', 'executive', 'executives', 'operations',
    'supply', 'company', 'group', 'inc', 'llc', 'corp', 'services', 'service', 'solutions',
    'windows', 'window', 'doors', 'door', 'glass', 'roofing', 'construction', 'remodeling',
    'appoints', 'appointed', 'promotes', 'promoted', 'hires', 'hired', 'leadership',
    'chief', 'vice', 'senior', 'junior', 'team', 'staff', 'board', 'director', 'manager',
    'president', 'owner', 'founder', 'partner', 'sales', 'marketing', 'customer', 'client',
    'our', 'your', 'his', 'her', 'their', 'meet', 'about', 'contact', 'read', 'more',
    'learn', 'view', 'call', 'today', 'free', 'quote', 'estimate', 'home', 'homes',
}


BRANDS = {
    'james hardie', 'andersen windows', 'pella windows', 'marvin windows', 'milgard',
    'simonton', 'alside', 'velux', 'jeld wen', 'jeldwen', 'ply gem', 'plygem', 'anlin',
    'atrium windows', 'cardinal glass', 'guardian glass', 'therma tru', 'thermatru',
    'provia', 'okna', 'soft lite', 'softlite', 'harvey windows', 'sunrise windows',
    'renewal andersen', 'window world', 'champion windows', 'owens corning', 'certainteed',
    'gaf roofing', 'hardie board', 'low e', 'energy star', 'better business',
}


def is_brand(name: str) -> bool:
    n = re.sub(r'[^a-z ]', '', name.lower()).strip()
    return n in BRANDS or any(b in n or n in b for b in BRANDS)


def looks_like_name(name: str) -> bool:
    """Two or three capitalised word-tokens, none of which is page furniture."""
    parts = name.split()
    if not 2 <= len(parts) <= 3:
        return False
    for p in parts:
        if re.fullmatch(r'[A-Z]\.', p):       # middle initial
            continue
        if not re.fullmatch(r"[A-Z][a-z'\-]{1,20}", p):
            return False                      # rejects ALL-CAPS and lowercase tokens
        if p.lower() in NOT_NAME_WORD:
            return False
    return not is_brand(name)


BAD_NAME = re.compile(r'\b(our|the|we|us|your|free|call|get|home|window|door|glass|'
                      r'service|quote|team|company|contact|about|read|more|view|'
                      r'privacy|terms|copyright|all rights)\b', re.I)


def people_in_prose(text: str) -> list:
    """Named decision-makers mentioned anywhere in the page text."""
    out = []
    t = re.sub(r'\s+', ' ', html.unescape(text or ''))
    for pat, name_first in ((PERSON_ROLE, True), (ROLE_PERSON, False)):
        for m in pat.finditer(t):
            name = (m.group(1) if name_first else m.group(2)).strip()
            title = (m.group(2) if name_first else m.group(1)).strip()
            if BAD_NAME.search(name) or not looks_like_name(name):
                continue
            role, tier = classify_role(title)
            if role:
                out.append({"name": name, "role": role, "tier": tier,
                            "title_text": title[:60]})
    # de-duplicate on name, keeping the most senior role
    best = {}
    for p in out:
        k = p["name"].lower()
        if k not in best or p["tier"] < best[k]["tier"]:
            best[k] = p
    return list(best.values())


def corroborates(name: str, email: str) -> bool:
    """True when the address itself supports the name attached to it.

    Team pages list several people close together, so a text window around one
    address easily catches a neighbour's name. Unless the mailbox echoes the name,
    the pairing is a guess and is not reported as that person's address.
    """
    if not name or not email:
        return False
    parts = [p for p in re.split(r'\s+', name.lower()) if len(p) > 1 and '.' not in p]
    if not parts:
        return False
    first, last = parts[0], parts[-1]
    lp = re.sub(r'[^a-z]', '', email.split("@")[0].lower())
    return lp in {first, last, first + last, last + first,
                  first[0] + last, first + last[0], last + first[0]} or (
        len(lp) > 4 and (lp.startswith(first) or lp.startswith(last)))


def crawl(domain: str, session: requests.Session) -> dict:
    out = {"domain": domain, "ok": False, "pages": [], "people": [], "error": ""}
    bare = domain[4:] if domain.startswith("www.") else domain
    base = home = None
    for url in (f"https://{bare}", f"https://www.{bare}", f"http://{bare}"):
        try:
            r = session.get(url, timeout=TIMEOUT, headers=HEADERS, allow_redirects=True)
            if r.status_code < 400 and r.text:
                base, home = r.url, r.text
                break
            out["error"] = f"HTTP {r.status_code}"
        except requests.RequestException as e:
            out["error"] = f"{type(e).__name__}"
    if not base:
        return out

    host = urlparse(base).netloc
    targets, seen = [(base, home)], {base.rstrip("/")}
    soup = BeautifulSoup(home, "html.parser")
    links = []
    for a in soup.find_all("a", href=True):
        u = urljoin(base, a["href"]).split("#")[0]
        if urlparse(u).netloc != host or u.rstrip("/") in seen or SKIP_LINK.search(u):
            continue
        blob = (a.get_text(" ") or "") + " " + u
        if PEOPLE_LINK.search(blob):
            seen.add(u.rstrip("/"))
            # team and leadership pages carry people; contact pages carry addresses
            pri = 0 if re.search(r'(team|leader|staff|management|people|owner|founder)', blob, re.I) else 1
            links.append((pri, u))
    # Small-business sites often have these pages without linking them in the nav.
    for guess in ("about", "about-us", "our-team", "team", "meet-the-team", "staff",
                  "leadership", "our-story", "contact", "contact-us"):
        u = urljoin(base, "/" + guess)
        if u.rstrip("/") not in seen:
            seen.add(u.rstrip("/"))
            links.append((2, u))
    links.sort()
    for _, u in links[:MAX_PAGES - 1]:
        try:
            r = session.get(u, timeout=TIMEOUT, headers=HEADERS)
            if r.status_code < 400 and r.text:
                targets.append((r.url, r.text))
        except requests.RequestException:
            continue
        time.sleep(0.15)

    people, prose = {}, {}
    for url, raw in targets:
        s = BeautifulSoup(raw, "html.parser")
        for p in people_in_prose(s.get_text(" ")):
            k = p["name"].lower()
            if k not in prose or p["tier"] < prose[k]["tier"]:
                prose[k] = {**p, "source": url}
        for addr, ctx in emails_from(s, raw, domain).items():
            name, role, tier = person_near(ctx, addr)
            prev = people.get(addr)
            cand = {"email": addr, "name": name, "role": role, "tier": tier,
                    "source": url,
                    "context": re.sub(r'\s+', ' ', (ctx or ''))[:200]}
            if prev is None or cand["tier"] < prev["tier"] or (
                    cand["tier"] == prev["tier"] and cand["name"] and not prev["name"]):
                people[addr] = cand
        out["pages"].append(url)
    out["people"] = list(people.values())
    out["named"] = sorted(prose.values(), key=lambda p: p["tier"])
    out["ok"] = True
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--workers", type=int, default=14)
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--cache", default=CACHE_DIR)
    args = ap.parse_args()
    os.makedirs(args.cache, exist_ok=True)
    globals()["CACHE_DIR"] = args.cache

    companies = list(csv.DictReader(open(args.input)))
    if args.limit:
        companies = companies[:args.limit]
    print(f"{len(companies)} companies", file=sys.stderr)

    lock, done = threading.Lock(), [0]
    tl = threading.local()

    def sess():
        if not hasattr(tl, "s"):
            tl.s = requests.Session()
        return tl.s

    def work(c):
        d = c["domain"].strip().lower()
        p = cache_path(d)
        if os.path.exists(p):
            res = json.load(open(p))
        else:
            res = crawl(d, sess())
            json.dump(res, open(p, "w"))
        with lock:
            done[0] += 1
            if done[0] % 25 == 0:
                print(f"  {done[0]}/{len(companies)}", file=sys.stderr)
        return c, res

    rows = []
    with cf.ThreadPoolExecutor(max_workers=args.workers) as pool:
        for c, res in pool.map(work, companies):
            found = sorted(res.get("people", []), key=lambda p: p["tier"])
            named = res.get("named", [])
            # a person named on the site but with no address of their own
            attributed = {(p.get("name") or "").lower() for p in found if p.get("name")}
            best_email = None
            for p in sorted(found, key=lambda p: (ROLE_MAILBOX.match(p["email"]) is not None,
                                                  p["tier"])):
                best_email = p
                break
            for np in named:
                if np["name"].lower() in attributed or is_brand(np["name"]):
                    continue
                # Pair only with an address that plausibly belongs to this person;
                # attaching their name to info@ would imply a link that is not there.
                own = ""
                first = np["name"].split()[0].lower()
                last = np["name"].split()[-1].lower()
                for p in found:
                    lp = p["email"].split("@")[0].lower()
                    if lp in (first, last, f"{first}.{last}", f"{first}{last}",
                              f"{first[0]}{last}", f"{first}_{last}", f"{first}{last[0]}"):
                        own = p["email"]
                        break
                found.append({"email": own, "name": np["name"], "role": np["role"],
                              "tier": np["tier"], "source": np["source"],
                              "context": f'named on site as "{np["title_text"]}"'})
            found = sorted(found, key=lambda p: p["tier"])
            if not found:
                rows.append({**{k: c.get(k, "") for k in
                                ("company_name", "website", "domain", "phone", "address")},
                             "person_name": "", "role": "", "role_tier": "",
                             "email": "", "email_type": "", "company_mailbox": "",
                             "source_page": "",
                             "context": "", "status": "no email published"})
                continue
            company_mailbox = best_email["email"] if best_email else ""
            for p in found:
                if (p.get("name") and p.get("email")
                        and not p.get("context", "").startswith("named on site")
                        and not corroborates(p["name"], p["email"])):
                    p = {**p, "name": "", "role": p.get("role"),
                         "context": (p.get("context") or "")}
                if p.get("name") and not looks_like_name(p["name"]):
                    p = {**p, "name": ""}
                generic = bool(ROLE_MAILBOX.match(p["email"])) if p["email"] else False
                rows.append({**{k: c.get(k, "") for k in
                                ("company_name", "website", "domain", "phone", "address")},
                             "person_name": p["name"] or "", "role": p["role"] or "",
                             "role_tier": p["tier"] if p["role"] else "",
                             "email": p["email"],
                             "email_type": ("" if not p["email"] else
                                            "generic mailbox" if generic else
                                            "personal mailbox" if p["name"] else "unattributed"),
                             "company_mailbox": company_mailbox,
                             "source_page": p["source"], "context": p["context"],
                             "status": "found"})

    cols = ["company_name", "website", "domain", "phone", "address", "person_name", "role",
            "role_tier", "email", "email_type", "company_mailbox", "source_page",
            "context", "status"]
    with open(args.out, "w", newline="") as f:
        w = csv.DictWriter(f, cols)
        w.writeheader()
        w.writerows(rows)

    cos = {r["domain"] for r in rows}
    with_any = {r["domain"] for r in rows if r["email"]}
    with_person = {r["domain"] for r in rows if r["role"]}
    print(f"\nwrote {args.out}", file=sys.stderr)
    print(f"  companies: {len(cos)}", file=sys.stderr)
    print(f"  with any email: {len(with_any)}", file=sys.stderr)
    print(f"  with a named decision-maker role: {len(with_person)}", file=sys.stderr)
    print(f"  total email rows: {sum(1 for r in rows if r['email'])}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
