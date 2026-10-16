# Roofing qualification — batch 2

1,061 companies from the second Apollo export, each read individually and given
a verdict on one question: **does this company install, repair or replace
roofs?**

| verdict | rows | meaning |
|---|---|---|
| YES | 911 | performs roof work (installs, repairs, replaces, re-roofs, coats) |
| MAYBE | 39 | roofing-adjacent, but the export never shows it doing roof work |
| NO | 107 | not a roofing services provider |
| UNCLEAR | 4 | the source row contradicts itself; name says roofing, everything else does not |

## Files

| file | rows | what it is |
|---|---|---|
| `roofing_batch2_verdicts.csv` | 1,061 | every company with verdict, confidence, category and note |
| `roofing_batch2_qualified.csv` | 848 | YES rows with no data-quality flag — the list to work |
| `roofing_batch2_review.csv` | 106 | MAYBE + UNCLEAR + the 63 flagged YES rows |
| `roofing_batch2_excluded.csv` | 107 | the NO rows, with the reason in `note` |
| `companies.jsonl` | 1,061 | the parsed export, one JSON object per company |
| `source_paste.tsv` | — | the paste as received, tab delimiters intact |
| `verdict-notes/c001.tsv` … `c009.tsv` | 471 | the per-row verdicts that deviate from the YES default |

Columns: `n, company_name, verdict, confidence, category, category_group, note,
city, state, employees, industry, website, phone, sic_naics_codes, keywords,
short_description, apollo_record_id, linkedin_url`.

## Confidence

`confidence` rates the **evidence**, not the company:

- `high` (628) — description or keywords name a roofing service and the
  description is substantial
- `medium` (79) — roofing name plus a roofing SIC/NAICS code, but thin text
- `low` (354) — name and domain only, or a note flags thin data

313 of the 911 YES rows are low confidence. Nearly all of them are small
contractors whose Apollo record carries a roofing name, 1761/238160, and
nothing else; the verdict rests on the name and the code. They are on the
qualified list, but the column marks them.

## Why rows were excluded

| reason | rows |
|---|---|
| manufacturers (membranes, metal panels, coatings, trusses, slate, underlayment, fasteners, skylights, solar mounts) | 37 |
| suppliers and distributors (supply houses, lumberyards, metal sales, tool dealers, online stores) | 26 |
| consultants, manufacturers' reps and engineers | 12 |
| marketing, lead-gen, media and directories | 12 |
| inspectors, testers and insurance adjusters | 9 |
| exterior and roof cleaning only | 3 |
| everything else: a Turkish-Mediterranean restaurant, a general home-repair service, a wall-coating franchise, a contractor-financing platform, an outdoor lighting company, an event-staging firm, a dumpster-rental company, a sports-canopy designer and a roofing licence-exam school | 8 |

## The two genuinely ambiguous groups

**Solar.** Seven rows sit on the line. Where the company's own described
services include roof work, it is YES with a note that it is solar-led
(Harness Building Solutions, NXT Level Homes, Brightshield, Kairos, Bluebonnet,
AX CO, Bright Home Solutions). Where roofing exists only as a keyword, a
partner arrangement or a word in the company name, it is MAYBE — proSOLAR, Bay
Area Energy Solutions, RiverTowne Solar, Ready Roofing & Solar, Lela Homelife,
Empower Solar and Roofing, Volta Solar.

**Builders, remodelers and restoration GCs.** The rule used throughout: if the
description names roofing among the services the company itself performs, YES
(with a note saying it is remodel- or GC-led); if roofing appears only in the
keyword list, MAYBE. That puts Parker Construction, JLJ Construction, Chase
Remodeling, Jayron, RenovateRite and Upstate Professional Contractors on the
YES side, and CAS Building & Remodeling, My Home Renovations, B3 Contracting,
APM Group, Royce Home Improvement, Ameri Restoration and Eagle Air Conditioning
on the MAYBE side.

## Source-data defects found

These are defects in the export, not verdicts. The flagged rows are in
`roofing_batch2_review.csv`.

- **Foreign companies carrying US addresses.** Thirteen rows: UK, Scottish, New
  Zealand and Ghanaian firms mapped onto look-alike US towns — `krb-group.co.uk`
  as "Ayrshire, Iowa", `swinglerroofing.co.uk` as "Northampton, Massachusetts",
  `balmoralflatroofing.co.uk` as "Mansfield, Ohio", `rjroofing.org.uk` as
  "Bedford, Texas", `waikatoroofing.co.nz` as "Hamilton, Ohio",
  `roofingtasman.co.nz` as "Richmond, Virginia", `perfectroofingandfascia.co.uk`
  as "Gloucester Point, Virginia", plus Cotswold Metal Roofing, Roofing
  Revolution, S. Hedges, Target Roofing and Skydome (an Australian skylight
  manufacturer listed in Johnson City, New York). JLB Property Maintenance is a
  fourteenth: an English firm listed as Northampton, Massachusetts.
- **Descriptions belonging to another company or market.** Fletcher Roofing
  (Georgia address, New Jersey description), Reyes Roofing (Texas address,
  Virginia description), Brand Roofing (Duran's Roofing copy), Suntek Roofing,
  Aabic Roofing (Revere Roofing copy), Award Roofing (Pittsburgh address,
  Georgia phone), Rick's Roofing (North Dakota address, Ontario description),
  Erickson Roofing (Wisconsin address, British Columbia description), Advance
  Roofing (Arkansas address, Florida description), Shamrock Roofing, Sealtight
  Roofing, Designer Roofing, Morales Roofing, Luxury Roofing, Ramirez Roofing,
  Maranatha Roofing, Next Generation Roofing, SR Roofing Solutions, Howard Home
  Improvements, Naples Roofing.
- **Shared call-centre description.** Ten rows carry the identical line
  "Professional roofing services for repairs, replacements, and new roof
  installations. Same-day appointments available. Call (877) 259-1106" —
  Leatherwood, Cockney, AA Roofing, Samuel, Dependable, American One, Coleman,
  Bellaire, Galaxy (Freeport) and Pearce Blackburn.
- **Spam-injected descriptions.** Ivey Roofing (Chinese lottery text),
  Sacramento Roofing (Polish footwear marketing), Precision Roofing And
  Exteriors (Turkish casino copy, with gambling SIC/NAICS codes and industry to
  match).
- **Parked domains.** Clutch Roofing and Lay Comercial Roofing both return
  "This domain may be for sale" — marked UNCLEAR, since there is no evidence
  either is trading.
- **Apollo industry mislabels.** 33 rows. Roofing companies tagged *telecommu-
  nications*, *hospitality*, *human resources*, *graphic design*, *oil & energy*,
  *real estate*, *marketing & advertising*, *management consulting*, *machinery*,
  *mining & metals*, *accounting*, *law practice*, *higher education*,
  *mental health care*, *entertainment*, *executive office*, *professional
  training & coaching*, *architecture & planning* and *health, wellness &
  fitness*. Filtering this export on `industry` would drop real roofers.
- **Mismatched websites.** New Tech Roofing (`prosteelcustomsutah.com`), Cap
  Roofing (`natarelliandsonroofing.com`), Precision Gutters (`baxtopia.com`),
  Briggs Roofing (`idahofallsdirect.us`), Pro Brush (`futurerockdoc.com`), CBS
  Roofing (`cbsmechanical.com`), Bjs Roofing (`myhomeprojectcenter.com`),
  C-West Roofing (`socalsolarroofing.com`), Mountain View Roofing
  (`mountainviewroofingnj.com` against an Idaho address).
- **Missing address fields.** Eight rows have no city or no state: South Star
  Roofing, Action Renovations, Nicotera Roofing, Green Technologies, Harrison
  Roofing, Archway Roofing, Dezign Roofing and Stanley And Sons Roofing.
- **One row is not a roofing company at all.** Row 44, Oxus7, is a
  Turkish-Mediterranean restaurant (SIC 5812).

## How the batch was parsed

Unlike batch 1, this paste kept its tab delimiters (25,496 of them) but arrived
with no header row, so it parses as plain TSV against batch 1's column order,
with the standard CSV reader handling the newlines embedded in quoted
description fields. All 1,061 rows produced 23 columns and a valid 24-hex
Apollo record id; all 1,061 ids are unique, and none of them appears in batch 1,
so the two batches do not overlap.

## Re-running

```sh
python3 -I build_verdicts.py batch2/companies.jsonl batch2/verdict-notes \
    batch2/roofing_batch2_verdicts.csv
python3 -I split_batch2.py batch2/roofing_batch2_verdicts.csv \
    batch2/roofing_batch2_qualified.csv batch2/roofing_batch2_review.csv \
    batch2/roofing_batch2_excluded.csv
```

`build_verdicts.py` exits non-zero on a duplicate or out-of-range row number in
the verdict files, so an edit to `verdict-notes/` cannot silently mis-join.
