#!/usr/bin/env python3
"""Join the per-row verdicts onto the parsed batch and write the deliverable.

Every row was read individually. Rows absent from the verdict files are plain
roofing contractors (YES); the files carry only the rows that deviate from that
or that need a data-quality flag. Confidence is derived from how much evidence
the export actually carries for the row, so a one-line listing never reads as
confidently as a full description.
"""
import csv
import glob
import json
import os
import re
import sys

SERVICE = re.compile(
    r'roof(ing|s|er|ers)?\b.{0,40}(repair|replace|replacement|install|'
    r'maintenance|restoration|contractor|service|inspection|coating|re-?roof)|'
    r'(repair|replace|replacement|install|maintenance|contractor|service)'
    r'.{0,40}\broof|re-?roof|commercial roofing|residential roofing|'
    r'roofing contractor|roof replacement|roof repair', re.I | re.S)
ROOF_CODE = re.compile(r'\b(1761|2381[0-9]?|23816|238160|17)\b')
THIN = re.compile(r'thin data|no keywords|no other data|no industry, keywords', re.I)

# Coarse buckets over the free-text categories, so the list can be filtered
# without reading every one of the ~140 distinct category strings.
GROUPS = [
    # a roofing contractor that also does an adjacent trade is still a roofing
    # contractor; the solar-led and coatings-led ones are kept separate below
    # because that is the distinction worth filtering on
    ("roofing contractor", r'^roofing[/ ](contractor|sheet metal|gutter)|'
                            r'^(commercial )?roofing platform|'
                            r'^exteriors/storm restoration platform'),
    ("supplier/manufacturer", r'manufactur|supplier|supply|distribut|wholesal|'
                              r'materials|metal suppl|fabricat|recycler|product '
                              r'\(|truss|prefab|decking subcontractor|'
                              r'green roof systems|hardware|footwear|asphalt plant'),
    ("software/marketing/lead-gen", r'software|lead gen|marketing|analytics|'
                                    r'media|directory|platform|marketplace|'
                                    r'visualization|photography|IT/'),
    ("consultant/inspector/estimator", r'consultant|consulting|estimat|inspect|'
                                        r'expert report|testing|certification|'
                                        r'engineering|asset management|'
                                        r'program management'),
    ("association", r'association'),
    ("solar", r'solar'),
    ("cleaning/rejuvenation", r'cleaning|rejuvenation|moisture remediation|roof prep'),
    ("builder/remodeler/GC", r'remodel|builder|general contractor|GC|renovat|'
                              r'restoration|construction management|'
                              r'design-build|reconstruction|abatement|board-up|'
                              r'facilities|handyman|home improvement|'
                              r'multi-trade subcontractor|civil engineering'),
    ("other trade", r'railing|stucco|painting|concrete|masonry|siding|gutter|'
                    r'waterproofing|sheet metal|HVAC|mechanical|steel erection|'
                    r'patio|outdoor living|fabric architecture|awnings|'
                    r'equipment|trucking|home energy|home inspection|'
                    r'metal building contractor|franchisor'),
]


def group(category):
    for name, pat in GROUPS:
        if re.search(pat, category, re.I):
            return name
    return "roofing contractor" if "roof" in category.lower() else "other"


def confidence(row, note):
    text = f"{row['description']} {row['keywords']}"
    strong = bool(SERVICE.search(text))
    if THIN.search(note or ""):
        return "low"
    if strong and len(row['description']) > 80:
        return "high"
    if strong or (re.search(r'roof', row['name'], re.I)
                  and ROOF_CODE.search(row['codes'])):
        return "medium"
    return "low"


def main(parsed, verdict_dir, out_csv):
    rows = [json.loads(l) for l in open(parsed)]
    verdicts = {}
    for path in sorted(glob.glob(os.path.join(verdict_dir, "*.tsv"))):
        for line in open(path):
            if not line.strip():
                continue
            n, verdict, category, note = line.rstrip("\n").split("\t")
            n = int(n)
            if n in verdicts:
                sys.exit(f"duplicate verdict for row {n}")
            verdicts[n] = (verdict, category, note)

    with open(out_csv, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["n", "company_name", "verdict", "confidence", "category",
                    "category_group", "note", "city", "state", "employees",
                    "industry", "website",
                    "phone", "sic_naics_codes", "keywords", "short_description",
                    "apollo_record_id", "linkedin_url"])
        counts = {}
        for r in rows:
            v, cat, note = verdicts.get(
                r['n'], ("YES", "roofing contractor", ""))
            conf = confidence(r, note)
            counts[v] = counts.get(v, 0) + 1
            w.writerow([r['n'], r['name'], v, conf, cat, group(cat), note,
                        r['city'],
                        r['state'], r['employees'], r['industry'], r['website'],
                        r['phone'], r['codes'], r['keywords'], r['description'],
                        r['apollo'], r['linkedin']])
    unknown = [n for n in verdicts if n < 1 or n > len(rows)]
    if unknown:
        sys.exit(f"verdicts for rows outside the batch: {unknown}")
    print(f"{len(rows)} rows, verdicts given explicitly for {len(verdicts)}")
    for k in sorted(counts):
        print(f"  {k}: {counts[k]}")


if __name__ == "__main__":
    main(*sys.argv[1:])
