#!/usr/bin/env python3
import html, os, re, sys, json
raw = sys.argv[1]
UT_CITY = (r'Salt Lake City|West Valley City|West Jordan|South Jordan|Sandy|Draper|Provo|Orem|Lehi|'
           r'Ogden|Layton|Murray|Taylorsville|Riverton|Herriman|Bountiful|Clearfield|Logan|'
           r'American Fork|Pleasant Grove|Spanish Fork|Springville|Lindon|Midvale|Holladay|'
           r'Kaysville|Farmington|Centerville|Syracuse|Roy|Tooele|Park City|St\. George|'
           r'Saratoga Springs|Eagle Mountain|Cottonwood Heights|Millcreek|Magna|Kearns|'
           r'Payson|Nephi|Heber|Vernal|Cedar City|Brigham City|Hurricane|Washington Terrace|'
           r'North Salt Lake|Woods Cross|Pleasant View|Wasatch|Utah County|Salt Lake County')
PATS = {
 'ut_state': r'\b(Utah|UT)\b',
 'ut_zip': r'\b84[0-7]\d\d\b',
 'ut_phone': r'\(?\b(801|385|435)\)?[\s.-]?\d{3}[\s.-]?\d{4}',
 'ut_city': UT_CITY,
 'win_install': r'window (replacement|installation|install|repair)|replacement window|'
                r'new windows|window company|window contractor|windows and doors|'
                r'window & door|replace your windows',
 'win_glass': r'glass repair|glass replacement|auto glass|windshield|insulated glass|'
              r'glass shop|window glass',
 'win_clean': r'window cleaning|window washing|clean your windows',
 'win_tint': r'window tint|window film|solar screen|window screen',
 'roof': r'\broof(ing|s)?\b',
 'other_state': r'\b(Arizona|Nevada|Idaho|Colorado|Texas|California|Ohio|Michigan|Florida|'
                r'Washington|Oregon|Wyoming|Montana|New Mexico|AZ|NV|ID|CO)\b',
}
def text_of(p):
    s = open(p, encoding='utf-8', errors='replace').read()
    s = re.sub(r'(?is)<(script|style|noscript|svg)[^>]*>.*?</\1>', ' ', s)
    title = re.search(r'(?is)<title[^>]*>(.*?)</title>', s)
    desc = re.search(r'(?is)<meta[^>]+name=["\']description["\'][^>]+content=["\'](.*?)["\']', s)
    if not desc:
        desc = re.search(r'(?is)<meta[^>]+content=["\'](.*?)["\'][^>]+name=["\']description["\']', s)
    body = html.unescape(re.sub(r'(?s)<[^>]+>', ' ', s))
    body = re.sub(r'\s+', ' ', body)
    return (html.unescape(title.group(1)).strip() if title else ''), \
           (html.unescape(desc.group(1)).strip() if desc else ''), body, s
out = []
for f in sorted(os.listdir(raw)):
    if not f.endswith('.html'):
        continue
    p = os.path.join(raw, f)
    if os.path.getsize(p) < 200:
        out.append({'file': f, 'empty': os.path.getsize(p)}); continue
    title, desc, body, s = text_of(p)
    hits = {}
    for k, pat in PATS.items():
        m = re.findall(pat, body, re.I)
        if m:
            vals = [x if isinstance(x, str) else x[0] for x in m]
            uniq = sorted(set(v.strip() for v in vals if v.strip()))[:6]
            hits[k] = f"{len(m)}x {uniq}"
    addr = re.findall(r'[0-9]{2,6}[^,<>\n]{3,40},?\s*[A-Z][a-zA-Z .]{2,22},?\s*(?:UT|Utah)[, ]*\s*\b84\d\d\d\b', body)
    addr2 = re.findall(r'\b[A-Z][a-zA-Z .]{2,22},\s*(?:UT|Utah)\s+84\d\d\d\b', body)
    out.append({'file': f, 'bytes': os.path.getsize(p), 'title': title[:140],
                'desc': desc[:220], 'addr': sorted(set(addr))[:3] or sorted(set(addr2))[:3],
                'hits': hits, 'len': len(body)})
json.dump(out, open('profiles.json', 'w'), indent=1)
print("profiled", len(out))
