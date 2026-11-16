# Verification - "Utah Window Companies, Google Maps Scrape (update 2, 47 zips)"

Sheet `1ADq4kMo0aiYNghDX5lmLS82Yc6pT9uNC6rgXBGI01yc`, checked 16 Nov 2026.
**667 rows.** No business data is committed here, counts only.

## Geography: all 667 are Utah

| | Rows |
|---|---|
| UT street address in the Address column | 436 |
| No street address, but Utah (84xxx) zips in "Found in zips" | 231 |
| Any other state | **0** |

The 231 without an address are Google Maps service-area businesses, which
do not publish a street address. They were found in the 47 Utah zips the
scrape ran, so they operate in Utah, but their base is inferred from where
they appear rather than read off a verified address.

Spread is wider than "Salt Lake": Layton, Farmington, Ogden, Eagle
Mountain, Tooele, Park City and Logan all appear. Logan is about 80 miles
north of Salt Lake. Still Utah, but not all Salt Lake metro.

## Classification: the sheet's own column is close, with 61 rows wrong

Sheet: 256 Yes / 72 Maybe / 339 No. Mine: **251 Yes / 65 needs-check / 351 No.**

| Disagreement | Rows |
|---|---|
| Sheet Yes, should be No | 28 |
| Sheet Maybe, is a Yes | 26 |
| Sheet Maybe, is a No | 7 |
| Sheet No, is a Yes | 6 |

### What the sheet wrongly marked Yes

- **8x "Home Services at The Home Depot"** -- a national big-box install
  desk, eight duplicate rows, no local owner to reach
- **6 door-only businesses** -- GS Iron Doors, High Country Iron Doors,
  C & M Doors, Steve's Discount Doors, Visionmakers, BJ's lock & door
- **4 window-well companies** -- Savage Window Wells, Windowell
  Expressions, Accent Window Well Covers, Window Well Covers By John
  Henry. Egress wells are concrete and steel, a different trade entirely
- **2 window cleaners** that read as installers by name -- Keep Em Clear
  Window, Windows & Wishes
- **2 Google Maps category stubs** -- rows literally named "Doors and
  Windows" and "Doors & Windows", not businesses
- **Window Covering Store** -- blinds
- **Ideal Siding SLC** and **Capitol Exteriors** -- checked both websites:
  siding only, and the sole window page on each is window *cleaning*

### What the sheet got right, and is worth keeping

Every "Window cleaning service" (97), "Window tinting service" (32),
"Window treatment store" (32) and auto-glass row was already correctly
marked No. The auto-glass catch is the impressive one: Google files
Safelite, Auto Glass Now and eight others under "Window installation
service" or "Glass repair service", and the sheet still excluded them.

## The 65 needs-check rows

Siding, roofing and general exterior contractors. Some replace windows,
some do not, and the Google category cannot tell them apart. Five were
checked by website this session:

| Company | Verdict |
|---|---|
| Novus Roofing and Exteriors | YES, sells Andersen, Pella, ProVia replacements |
| Paramount Peaks Builders | YES, "expertly installed windows and doors" |
| JadeView Windows & Doors | YES, custom aluminium windows, measured and installed |
| Precision Window Services | YES, window repair, glass and hardware |
| Ideal Siding SLC | NO, siding only |
| Capitol Exteriors | NO, window *cleaning* only |

Roughly half pass, so the remaining 60 are worth about an hour of website
checks rather than being accepted or binned wholesale.

## The blocker for outreach

| Column | Filled |
|---|---|
| Phone | 661 / 667 (99%) |
| Website | 373 / 667 (55%) |
| **Email** | **0 / 667** |
| **Owner / decision maker** | **0 / 667** |
| **LinkedIn** | **0 / 667** |
| Facebook | 27 / 667 (4%) |

The Email, Owner and LinkedIn columns exist in the sheet but are empty on
every single row. **This list cannot feed an Instantly campaign as it
stands** -- it is a phone and website list. Getting from here to a sending
list means an enrichment pass: Apollo or Hunter against the 182 verified
YES rows that have a website, or hand-research for the 69 that do not.

## Duplicates

The 251 YES rows are 237 distinct names and fewer distinct companies:
Valley Glass appears 3x, Marvin Design Gallery, Westlake, Revival,
Window World Utah, Accent Windows, Mountain States and Epic Windows + Doors
twice each. Genuine separate branches, but one company for outreach.

## Output

`utah_window_VERIFIED.csv` in the session scratchpad, not committed. All
667 rows with my Verdict, the reason, the geography basis and what the
sheet said, sorted YES first.
