# roofing-qualifier

Decides, for a list of companies exported from Apollo, which ones are **roofing
companies that actually offer roofing services** — a contractor who installs,
repairs or replaces roofs — and which ones only sit near the trade: material
manufacturers and distributors, equipment vendors, consultants, estimators,
software and lead-gen firms, trade associations, roof cleaners, solar installers.

Two batches so far: **batch 1, 1,158 companies** and **batch 2, 1,061
companies** (2,219 in total; the Apollo record ids confirm no overlap). Each
batch has its own folder and its own README — `batch2/README.md` covers batch 2
and the figures below are batch 1's.

Every row was read individually against its
own keywords, short description, SIC/NAICS codes, name and website. No per-company
web search was run — the export already carries that text, which is what you asked
for. Where the export is thin or self-contradictory, the row says so rather than
guessing.

## The verdict

| verdict | count | meaning |
|---|---|---|
| `YES` | 932 | installs, repairs or replaces roofs — the target |
| `MAYBE` | 73 | roofing-adjacent, but the export does not show them performing roof work |
| `NO` | 143 | not a roofing services provider |
| `UNCLEAR` | 10 | the source data contradicts itself; neither verdict is honest |

`confidence` is about the evidence, not the company:

- `high` — the description or keywords name a roofing service in so many words
- `medium` — a roofing name and a roofing SIC/NAICS code (1761 / 238160), but thin text
- `low` — name and domain only; nothing in the export confirms it

749 of the 932 `YES` rows are `high`. The 102 `low`-confidence `YES` rows are
companies called "<something> Roofing" with a matching domain and no other data in
the export; they are very probably roofing contractors, but that is an inference
from the name, so it is labelled as one.

## Files

| file | rows | what it is |
|---|---|---|
| `roofing_batch1_verdicts.csv` | 1,158 | every company, with verdict, confidence, category and note |
| `roofing_batch1_qualified.csv` | 870 | `YES` with no data-quality flag — the clean outreach list |
| `roofing_batch1_review.csv` | 145 | `MAYBE`, `UNCLEAR`, and the 62 flagged `YES` rows |
| `roofing_batch1_excluded.csv` | 143 | `NO`, with the reason in `note` |
| `companies.jsonl` | 1,158 | the export parsed back into fields |
| `source_paste.txt` | — | the paste as received, so the parse can be re-run |
| `verdict-notes/*.tsv` | 288 | the hand-written verdicts, as `n / verdict / category / note` |

`category` is free text ("manufacturer rep", "solar-led", "roof asset
management"); `category_group` buckets it so you can filter without reading all
~140 distinct values.

## Why things were excluded

Among the 143 `NO` rows: 60 suppliers and manufacturers, 20 software / marketing /
lead-gen firms, 17 builders and remodelers with no roofing line, 16 consultants,
estimators and inspectors, 13 other trades, 12 solar-only installers, 3 roof
cleaners, 2 IIBEC chapters.

Two kinds of near-miss are worth knowing about, because reasonable people would
decide them differently:

- **Solar.** A solar installer whose own description or trading name includes
  roofing (Saguaro Solar, Roofing & Electric; ESD Roofing + Solar; ReNu Solar &
  Roofing) is `YES`, flagged `solar-led`. A solar installer carrying only a 238160
  NAICS code or the word "roofing" in a keyword list, with nothing in the
  description, is `MAYBE` or `NO`. If you want solar-first firms out entirely,
  filter `category_group = solar`.
- **Builders, remodelers and restoration GCs.** Where roofing is a named service
  ("licensed Illinois Roofing Contractor", "roofing, siding, gutters, windows")
  the row is `YES`. Where roofing is one word in a long keyword list for a kitchen
  remodeler, it is `MAYBE`. That is the single biggest `MAYBE` bucket (41 rows).

## Data quality in the source

The export has real defects, and each one is flagged in `note` on its row:

- **Row 1, Allphase Construction & Roofing** — the keyword field is saturated with
  Indonesian gambling spam (*taruhan online 24 jam*, *deposit 5rb menang besar*).
  That is what a compromised or expired-and-reused domain looks like. Still a
  roofing contractor on its description, but check the site before any outreach.
- **Foreign websites against US addresses** — `maxroofing.co.uk` in Spring TX,
  `a1roofing.com.au` in Richburg SC, `laytonroofing.co.uk` in Worcester MA,
  `americanshingles.com.au` in Atlanta, a `+44` phone in Truro MA. Several are
  plainly the UK or Australian company, with a same-named US town attached.
- **Descriptions describing a different company or state** — Yoder Roofing (Ohio
  address, Sarasota FL description), AAA Roofing Contractors (Delray Beach FL
  address, Fresno CA description), Twin Peaks Roofing (Washington address,
  Ontario description), Northside Roofing (Iowa address, a Texas keyword, a New
  York description).
- **A shared call-centre description** — rows 411, 421 and 425 carry the identical
  "Same-day appointments available. Call (877) 259-1106" text.
- **Apollo industry mislabels** — Maine Roofing tagged *music* with the keyword
  "musicians", Noahs Roofing tagged *pharmaceuticals*, Mikes Roofing tagged
  *financial services*, Rex Roofing tagged *media production*, Boone Roofing tagged
  *warehousing*. The codes and descriptions are right; the industry field is not.
- **Non-US contractors** — Weber Bedachungen (Maxsain, Germany) and Olympia
  Construction (Ontario, Canada) are genuine roofers with bad US addresses;
  ALBERT & FILS is a French building firm. Flagged, not silently dropped.

## Re-running it

```bash
python3 parse_batch.py batch1/source_paste.txt batch1/companies.jsonl
python3 build_verdicts.py batch1/companies.jsonl batch1/verdict-notes \
        batch1/roofing_batch1_verdicts.csv
```

## About the parse

The paste arrived with every tab collapsed to a space, so the 23 columns had to be
recovered from the shape of their values. Four anchors survived and carry the
parse: the `Lists` field (a closed vocabulary, so it marks where each record
starts), the comma-joined `Company Address` (its country token is the one place
`", United States"` appears, which is where the keywords begin), the 24-hex Apollo
record id, and the s3 `Logo Url` that ends each record. All 1,158 records came out
with a unique Apollo id and no duplicates; the 84 rows where the company name and
domain share no token are abbreviations (`Commercial Roofers, Inc.` /
`commroof.com`), not misalignments.

One side effect of the lost tabs remains visible in the output: a handful of
`city` / `state` values absorbed part of the un-joined address block. No company
name came out doubled, and nothing here affects a verdict.

## Batch 2

`batch2/` holds the second export: 1,061 companies, 911 YES, 39 MAYBE, 107 NO,
4 UNCLEAR. Same verdict taxonomy, same confidence rules, same four CSVs. See
`batch2/README.md` for its counts, its exclusion breakdown and the source
defects it turned up (thirteen foreign companies carrying US addresses, ten rows
sharing one call-centre description, three spam-injected descriptions, 33 Apollo
industry mislabels).

That paste kept its tab delimiters, so it needed no shape recovery: it parses as
plain TSV against batch 1's column order, with no header row.

## Next batches

If the paste arrives **with tabs intact**, parse it as TSV (23 columns in the
order of batch 1's header) — that is what batch 2 needed, and it is the easy
case. If the tabs are **stripped**, `parse_batch.py` recovers the columns from
the shape of their values; it handles the `Lists` values seen so far (`Roofing
List (x-Tobi)`, `Master List - Roofing - Tobi`, `All Window Installation List`,
`Window Installation List for TX,Phoenix,FL`), and a new list name needs adding
to `_LIST_NAMES` or the parser will merge two records into one — the record count
and the Apollo-id uniqueness check catch it.
