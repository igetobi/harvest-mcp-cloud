# Every Utah window domain we hold, from every source

Built 20 Nov 2026 by merging every list in this project.

## 512 distinct domains

| Verdict | Domains | |
|---|---|---|
| **YES** | 227 | verified window installer or repairer in Utah |
| **YES-WEAK** | 4 | handyman franchises that list window work among many trades |
| **IN INSTANTLY ONLY** | 9 | already being emailed, neither Maps scrape found them |
| CHECK | 10 | exterior contractors, no website to settle it |
| UNREACHABLE | 18 | site dead or refused |
| FRANCHISE | 8 | national brands, split out deliberately |
| NO | 205 | cleaning, tinting, coverings, auto glass, other trades |
| REMOVED | 12 | manufacturers, pet doors, out-of-state service listings |
| NOT UTAH | 10 | the Syracuse NY and AZ/OR/NM rows |
| NOT OURS | 6 | Apollo mis-matches |
| CLIENT | 1 | Solara |
| unclassifiable | 1 | a Linktree URL |

**240 are worth contacting**: the 227 YES, the 4 handyman-weak and the 9
only Instantly knows about.

## Where they came from

| Source | Domains |
|---|---|
| Google Maps scrape 2 (1,007 rows) | 497 |
| Google Maps scrape 1 (667 rows) | 329 |
| The verified list (236) | 236 |
| Final after Apollo reconciliation (227) | 227 |
| Apollo accounts export (94) | 94 |
| Hunter contacts (39 companies) | 39 |
| Instantly Window campaign, Utah leads | 20 |

A domain counts under every source it appears in, so these overlap heavily.

## Nine companies only Instantly knows about

The Window campaign holds 133 leads; **35 carry a Utah location** and nine
of those are on domains neither Maps scrape returned:

| Domain | Company |
|---|---|
| advancedwindowsusa.com | Advanced Window Products |
| chooserevival.com | Revival Windows |
| rbaslc.com | Renewal by Andersen of Utah |
| soniqwindowsanddoors.com | SONIQ Windows and Doors |
| skyviewglass.com | Skyview Glass |
| stgeorgewindows.com | St George Windows Doors & More |
| cornerstonehomeremodel.com | Cornerstone Home Remodel |
| gobighorn.com | BigHorn Roofing |
| harringtonco.com | Harrington |

Four are **second domains for companies already on the list**:
`advancedwindowsusa.com` against our `advancedwindows.com`,
`chooserevival.com` against `gorevivalwindows.com`,
`soniqwindowsanddoors.com` against `soniqwindows.com`, and `rbaslc.com`
for a Renewal by Andersen franchise we hold on the corporate domain.
Dedupe on domain alone will not catch these, so a company can be emailed
twice under two brands.

Also note the Window campaign is **not** a Utah campaign: of its 133
leads only 35 are Utah, the rest are Phoenix, Orlando, Omaha, Fort Worth,
Oklahoma City and others.

## Files

In the session scratchpad:

- `utah_window_domains_ALL.csv` — all 512, with verdict, company name,
  every source it came from, and the reason for any exclusion
- `utah_window_domains_GOOD.csv` — the 240 worth contacting
- `utah_window_domains_GOOD.txt` — those 240 as a plain domain list

## What Apollo did with all 512

The full 512 went to Apollo on 20 Nov, not the 240 contactable subset.
Apollo returned **222 companies**. Only **76 are usable**.

| | Rows |
|---|---|
| Apollo returned | 222 |
| **Keep** — our YES / weak / Instantly-only, and Apollo agrees it is Utah | **76** |
| Drop | 146 |

The 146 break down as:

| Reason | Rows |
|---|---|
| **We had already marked it NO** | 90 |
| Not one of our 512 at all | 9 |
| National franchise we split out | 7 |
| Already marked NOT UTAH | 6 |
| Already removed (manufacturers, pet doors) | 6 |
| Apollo mis-match we had identified | 5 |
| Unreachable site | 3 |
| Our YES, but Apollo places it out of state | 20 |

**90 of the 222 are window cleaners, tinting shops, blind sellers and auto
glass firms** that were classified and rejected weeks ago. Sending the
whole 512 bought their Apollo records back at full price.

### Apollo also returned nine companies that were never on the list

| Apollo returned | Where |
|---|---|
| **Squarespace** | New York |
| **United States Air Force** (`af.mil`) | Texas |
| **Linktree** | Melbourne |
| **Bath Fitter** | Quebec |
| Lansing Building Products | Virginia |
| Relentless Windows & Doors | Gilbert, Arizona |
| Intermountain Martin Doors | Payson, Utah |
| Right Choice Garage Doors | Layton, Utah |
| Stan Barlow Construction | Spanish Fork, Utah |

The first four come from the site-builder and link-aggregator domains in
the list: `dripwindowcleaning.squarespace.com` resolves to Squarespace,
`linktr.ee` to Linktree. It is the same failure that returned two Indian
companies on the pest control run, and the reason those rows carry a
`Site type` flag.

### Credits

2,547 of 2,570 consumed this cycle, **23 left**, resetting 3 Dec. Direct
dials are at 482.

Had the 240 contactable domains gone instead of all 512, the same ~76
useful records would have come back: every one of them is in that subset.

## Files

- `apollo_KEEP.csv` — the 76 worth keeping, with Apollo's phone, headcount,
  city and industry
- `apollo_DROP.csv` — the 146, each with the reason
