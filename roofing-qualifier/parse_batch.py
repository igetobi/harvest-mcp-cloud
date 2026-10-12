#!/usr/bin/env python3
"""Reconstruct Apollo export rows from a paste whose tab delimiters were lost.

Every tab collapsed to a space, so columns can only be recovered from the shape
of their values. Four anchors survive intact and carry the parse:

  Lists            a closed vocabulary, so it marks where each record starts
  Company Address  repeats street/city/state/country/postal comma-joined, and
                   its country token is the one place ", United States" appears
  Apollo Record Id 24 hex characters, splitting the row into before/after
  Logo Url         an s3 URL, the last field of the record
"""
import json
import re
import sys

_LIST_NAMES = (r'Roofing List \(x-Tobi\)|Master List - Roofing - Tobi|'
               r'All Window Installation List|'
               r'Window Installation List for TX,Phoenix,FL')
LISTS = re.compile(r'(?:%s)(?:, (?:%s))*' % (_LIST_NAMES, _LIST_NAMES))
APOLLO = re.compile(r'(?<![0-9a-f/])[0-9a-f]{24}(?![0-9a-f])')
URL = re.compile(r'https?://\S+')
COUNTRY = re.compile(r', (United States|Canada|United Kingdom|Australia|Ireland|'
                     r'India|Mexico|Germany|Netherlands|South Africa|New Zealand|'
                     r'Philippines|Singapore|Spain|France|Italy|Poland|Brazil)'
                     r'(?:, (?P<postal>[A-Z0-9][A-Z0-9 -]{1,9}?))?(?=\s|$)')
PHONE = re.compile(r'(?:\+\d{1,3}[\s-]?)?(?:\(\d{3}\)|\d{3})[\s.-]?\d{3}[\s.-]?\d{4}'
                   r'(?:\s*(?:ext|x)\.?\s*\d+)?\s*$')
CODES = re.compile(r'^\s*(\d{2,6}(?:\s*,\s*\d{2,6})*)(?=\s|$)')
YEAR = re.compile(r'\b(1[6-9]\d\d|20[0-2]\d)\b')


def split_name_pair(blob):
    """'Acme Roofing Acme Roofing' -> 'Acme Roofing'.

    The export repeats the name in Company Name for Emails, usually verbatim
    but sometimes shortened ('Acme Roofing LLC' / 'Acme Roofing'). Prefer the
    longest exact doubling; fall back to the whole blob.
    """
    t = " ".join(blob.split())
    t = re.sub(r'^[^0-9A-Za-z&]+', '', t).strip()
    if not t:
        return "", ""
    # Company Name for Emails drops punctuation, so compare without it
    norm = lambda x: re.sub(r'\s+', ' ', re.sub(r"[,.()'\u2019]", '', x)).strip().lower()
    for cut in range(len(t) - 1, 0, -1):
        a, b = t[:cut].strip(), t[cut:].strip()
        if a and b and norm(a) == norm(b):
            return a, b
    for cut in range(len(t) - 1, 0, -1):
        a, b = t[:cut].strip(), t[cut:].strip()
        if a and len(b) > 2 and (norm(b).startswith(norm(a))
                                 or norm(a).startswith(norm(b))):
            return a, b
    return t, ""


def parse(raw):
    body = raw[raw.index("Logo Url") + len("Logo Url"):]
    marks = [(m.start(), m.end()) for m in LISTS.finditer(body)]
    out = []
    for i, (s, e) in enumerate(marks):
        name_blob = body[marks[i - 1][1]:s] if i else body[:s]
        chunk = body[e:marks[i + 1][0] if i + 1 < len(marks) else len(body)]

        # The name blob trails the previous record, which normally ended at its
        # Logo Url. When that field was empty the trail runs on through the
        # address, phone and description, so cut at whichever record-tail
        # anchor sits furthest right.
        cut = 0
        for pat in (URL, COUNTRY, APOLLO, re.compile(PHONE.pattern[:-2])):
            for m in pat.finditer(name_blob):
                cut = max(cut, m.end())
        name, name_email = split_name_pair(name_blob[cut:])

        am = APOLLO.search(chunk)
        pre, post = (chunk[:am.start()], chunk[am.end():]) if am else (chunk, "")
        apollo = am.group(0) if am else ""

        m = re.match(r'\s*(\d+)\s*', pre)
        employees, rest = (m.group(1), pre[m.end():]) if m else ("", pre.lstrip())

        pu = list(URL.finditer(rest))
        industry = " ".join(rest[:pu[0].start()].split()) if pu else ""
        urls_found = [u.group(0) for u in pu]
        after = rest[pu[-1].end():] if pu else rest

        website = next((u for u in urls_found if not re.search(
            r'linkedin\.com|facebook\.com|twitter\.com|//x\.com', u, re.I)), "")
        linkedin = next((u for u in urls_found if 'linkedin.com' in u.lower()), "")

        cm = COUNTRY.search(after)
        if cm:
            head = " ".join(after[:cm.start()].split())
            bits = [b.strip() for b in head.split(',')]
            city = bits[-2] if len(bits) >= 2 else ""
            state = bits[-1] if bits else ""
            address = f"{head}, {cm.group(1)}" + (
                f", {cm.group('postal')}" if cm.group('postal') else "")
            kw_phone = after[cm.end():]
        else:
            city = state = address = ""
            kw_phone = after

        kw_phone = " ".join(kw_phone.split())
        pm = PHONE.search(kw_phone)
        phone, keywords = ((pm.group(0).strip(), kw_phone[:pm.start()].strip())
                           if pm else ("", kw_phone))

        codes, desc = "", post
        for _ in range(2):            # SIC Codes then NAICS Codes
            c = CODES.match(desc)
            if not c:
                break
            codes = (codes + ", " + c.group(1)).strip(", ")
            desc = desc[c.end():]
        desc = " ".join(desc.split()).strip().strip('"').strip()

        logo = ""
        lm = list(URL.finditer(desc))
        if lm:
            logo, desc = lm[-1].group(0), desc[:lm[-1].start()].strip()
        founded = ""
        ym = list(YEAR.finditer(desc[-10:]))
        if ym and desc[-10:][ym[-1].end():].strip() == "":
            cutpoint = len(desc) - 10 + ym[-1].start()
            founded, desc = ym[-1].group(0), desc[:cutpoint].rstrip().rstrip(',')

        out.append(dict(n=i + 1, name=name, name_email=name_email,
                        lists=" ".join(LISTS.pattern and body[s:e].split()),
                        employees=employees, industry=industry, website=website,
                        linkedin=linkedin, address=address, city=city, state=state,
                        keywords=keywords, phone=phone, apollo=apollo, codes=codes,
                        description=desc.strip('"'), founded=founded, logo=logo))
    return out


if __name__ == "__main__":
    rows = parse(open(sys.argv[1]).read())
    with open(sys.argv[2], "w") as f:
        for r in rows:
            f.write(json.dumps(r) + "\n")
    print(f"{len(rows)} records")
