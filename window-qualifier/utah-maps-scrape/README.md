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

Sheet: 256 Yes / 72 Maybe / 339 No. Mine, after the website checks:
**256 Yes / 383 No / 16 unresolved / 11 unreachable / 1 flagged.**

| Disagreement | Rows |
|---|---|
| Sheet Yes, should be No | 29 |
| Sheet Maybe, is a No | 29 |
| Sheet Maybe, is a Yes | 28 |
| Sheet No, is a Yes | 7 |

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

## The 65 needs-check rows: resolved

All 49 with a website were checked, 16 Nov. Results:

| Outcome | Rows |
|---|---|
| Confirmed they fit windows | 5 |
| Confirmed they do not | 27 |
| Website unreachable or dead | 11 |
| No website at all, cannot check this way | 16 |
| Listing looks mis-located | 1 |

### Confirmed window work (moved to YES)

| Company | Evidence on their own site |
|---|---|
| BH Exterior and Design | "energy-efficient window replacements" |
| Classic Roofing and Exteriors | "Windows and Door" service, consultation to installation |
| Love Builds Construction | "Windows & Doors" service; a review mentions windows replaced |
| Rock Top Construction | Windows listed as a service, FAQ confirms window replacements |
| Wanner & Sons Construction | "window tear-out and installation" |

Together with Novus Roofing, Paramount Peaks, JadeView and Precision
Window Services from the earlier pass, nine exterior contractors turned
out to be genuine.

### Confirmed no window work (moved to NO)

Eleven are plainly another trade: Ace Gutter (two branches, gutters),
Cottonwood Custom (decks), Cook Builders (commercial ground-up),
Utah Pro Xteriors and R&R Stucco (stucco), Preferred Roofing, VIP Roofing
and Maldonado Roof (roofing), Deck Kings (decks), Salt Lake City
Contractors (interiors), TJ Construction (stucco -- its site even explains
why windows must be fitted correctly, without offering to fit them).

Sixteen more have a live site that never mentions window work at all:
A D Johnson, Barlow, CCR Roofing, Copperhead, Cransten (handyman, lists
"Doors and Windows" generically), Creative Construction Solutions (egress
windows only inside a basement job), Elite Custom Exteriors, Hanson Home
Works, Hive Remodeling, RemodelCo, Measure Twice, Oakley Homes, SAC
Remodeling, Utah Home Remodel Experts, Wayman Bro's, Utah Basement
Builders, Jacob's Remodeling, Sandy Handyman and Simplified Home Services
(a holding page). A contractor who does not market window work is not a
window lead.

### One to look at

**Relentless Construction LLC** is listed in Utah, but its site redirects
to `relentlesswindowsanddoors.com`, an Arizona window installer serving
Phoenix, Tucson and the Valley. It is a real window company; the Utah
listing looks stale or mis-located.

### 11 unreachable

Dansie Design Build, Innovative Construction, LG Rain Gutter, R&R General
Contractor, RADIN Services, Skyrocket Construction, Odin and Sons (404),
Rosco Construction, Southwest Exterior, Stratford Finish Carpentry (404)
and Gayosso's siding and painting, whose URL in the sheet is misspelt and
does not resolve. Two are dead sites, which is itself a signal.

### 16 with no website

Bighorn Roofing, Build Doctors, Davies Advanced Construction, Kaysville
Roofing, M&M Gutters, Mreal exteriors, Roberts Brothers Siding, Smart
Roofing & Skylights, South Jordan Handyman, Timberline Exteriors, TKI
General Contractor, Top Stone Remodeling, Uplevel Remodeling, Utah Home
Remodeling, Wesley Garrett Home Improvements, West Jordan Roofing. Phone
only -- a call is the only way to settle these, and with no website they
are poor campaign leads regardless.

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
list means an enrichment pass: Apollo or Hunter against the 187 verified
YES rows that have a website, or hand-research for the 69 that do not.

## Duplicates

The 256 YES rows are 242 distinct names and fewer distinct companies:
Valley Glass appears 3x, Marvin Design Gallery, Westlake, Revival,
Window World Utah, Accent Windows, Mountain States and Epic Windows + Doors
twice each. Genuine separate branches, but one company for outreach.

## Output

`utah_window_VERIFIED.csv` in the session scratchpad, not committed. All
667 rows with my Verdict, the reason, the geography basis and what the
sheet said, sorted YES first.
