# Verification, round 2 - `utah_windows` upload, 16 Nov 2026

1,007 rows, a larger scrape than the 667-row sheet and with no
pre-classification column. Counts only, no business data committed.

## What was removed, and why

| Reason | Rows |
|---|---|
| No website at all | 432 |
| Website is a social profile, not a company site | 12 |
| **Not in Utah** | **13** |
| **Kept** | **550** |

### The social-profile rows

Twelve rows listed a Facebook or Instagram page in the Website column:
ADA Windows Plus, H & H Windows (twice), Simple Window Cleaning, Tint &
Clear Bra Specialists, SC Window Tinting, G Rock Designs, Signworks,
Vicus Home Improvement, Xtreme Screens, Derya Handyman, and Handy Dad
(a Linktree). Some are genuine window companies; they simply have no site
of their own.

### The out-of-state rows, and what they say about the scrape

Thirteen rows carry a non-Utah address, and **seven of them are in
Syracuse, New York** -- Window World of Syracuse, Renewal by Andersen,
Comfort Windows & Doors, Universal Windows Direct, Ryan's Windows &
Doors, Affordable Windows, plus Window King of Saratoga Springs.

There is a Syracuse, Utah (84075, in Davis County). The scraper almost
certainly searched "Syracuse" and took New York results. The rest are
Accent Southwest (Albuquerque NM), Magna View and RMK Windows (AZ),
Lowery's Window & Door (Payson AZ), Elite Windows (Colorado Springs CO)
and Lifetime Windows (Salem OR) -- all plausible mismatches on a shared
city or company name. Worth fixing in the scraper, since the same bug
will recur on the next run.

Nine more rows sit on no-code site builders (Wix, GoDaddy, Jobber,
Lovable). They are real sites, so they were kept, and the `Site type`
column marks them.

## Verdicts on the 550 kept

| Verdict | Rows |
|---|---|
| YES, a window installer or repairer | 279 |
| YES-WEAK, window work among many handyman trades | 5 |
| NO | 237 |
| Unreachable site | 18 |
| Still unchecked | 10 |
| Flagged | 1 |

**284 usable leads, 267 distinct companies.**

### 62 website checks run this round

Nine exterior and roofing contractors confirmed they fit windows: Tumi
Exteriors, Revolution Exteriors, RAM Builders, Simpli Exteriors, Big West
Roofing, Dynamic Roofing, Crow Brothers, Awesome Trimwork and MARC
Contracting.

Thirteen confirmed they do not, among them A1 Roofing, Master Roofing,
Legacy Roofing, Bigfoot Roofing, Erie Home, Energy Pro (insulation),
Graydaze (commercial painting) and Salmon Electrical. Ideal Siding Utah
Valley inherits the NO proven on the Salt Lake branch of the same
franchise.

Eighteen more have a live site that never mentions window work, so they
are NO for a window campaign.

### The YES-WEAK group

Ace Handyman Services, Handyman Connection, Mr. Handyman, Harman Handyman
and Monty's all genuinely list window work -- Mr. Handyman names
installation, replacement and frame repair outright. But it is one line on
a menu of twenty trades, and these are franchises rather than window
specialists. They are separated out so they can be included or dropped on
purpose rather than by accident.

### Still open

Ten handyman sites were not reached before fetching began to rate-limit:
Willden's, Utopia Home Services, Desert Wolf, KB Home Repairs, Lovely Home
Services, Nabawi, Dunning and Sons, Hubbell, Pleasant Valley Repair and
Done & Dusted. Eighteen more sites were unreachable outright -- several
return 404, which is its own signal about the business.

## Still no email addresses

This upload has no email or owner column at all, so the enrichment pass is
unchanged: 284 companies with a website to enrich against.

## Output

`utah_windows_VERIFIED_550.csv` in the session scratchpad, sorted YES
first, each row carrying its verdict, the evidence, how geography was
established and whether the site is a real domain or a page builder.

## Final cut: verified and good only

From the 279 YES, three further removals and a dedupe:

| Step | Rows |
|---|---|
| YES after the website checks | 279 |
| less national franchise branches | -11 |
| less pet-door and door-only shops | -3 |
| less duplicate branch rows, merged into one row per company | -28 |
| **FINAL** | **237 companies** |

### Why the franchises came out

Window World Utah, Marvin Design Gallery, Pella of Utah, West Shore Home,
Champion, Renewal by Andersen and DaBella are real window companies, but
they are corporate branches. Lead generation is bought centrally, and
there is no local owner to pitch -- the same reason Home Depot was cut
earlier. They are in `national_franchises.csv` rather than deleted, in
case the pitch ever suits them.

### Why three more came out

**Utah Pet Access**, **Salt City Pet Doors** and **Capital Door Shop**
are all filed by Google under "Window installation service" and are not
window companies. Utah Pet Access had 538 reviews and was sitting seventh
in the list, so category alone would have let it through.

### The dedupe

Twenty-eight rows were extra branches of a company already in the list --
Valley Glass has four, Jones Paint & Glass four, Epic Windows + Doors and
Burton Lumber three each. One row per company now, keeping the branch with
the most reviews, and an `Other branches` column naming the rest so
nothing is lost.

### What the 237 look like

| | |
|---|---|
| With a street address | 152 |
| Service-area businesses, no street address | 85 |
| With a phone number | 232 |
| On their own domain | 234 |
| On a no-code site builder | 3 |
| Have other branches | 22 |

A `Domain` column carries the bare hostname for each company, ready for
an enrichment tool to take as input.
