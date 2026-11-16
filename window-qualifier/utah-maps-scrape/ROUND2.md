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
