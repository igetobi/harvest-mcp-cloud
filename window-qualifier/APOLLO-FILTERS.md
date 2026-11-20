# Apollo filters for window installation

Measured 20 Nov 2026 against the **96 verified Utah window companies that
Apollo already holds** — a real answer key rather than a guess.

## Your current filter finds 22% of them

Company Keywords = `window installation` OR `window replacement` matches
**22 of the 96**. Seventy-four companies you have already verified as real
window businesses do not carry either phrase in Apollo.

| Filter | Recall |
|---|---|
| `window installation` OR `window replacement` (current) | 22/96 — **22%** |
| Any keyword containing "window" | 43/96 — 44% |
| Keywords containing window, glass or glazing | 49/96 — 51% |
| Company **name** contains window / glass / glazing | 63/96 — 65% |
| **Short description** mentions window or glass | 65/96 — 67% |
| Name **or** keywords **or** description | 87/96 — **90%** |

The ceiling is the data: Keywords is filled on only 69 of 96 records, SIC
on 55, NAICS on 56. Company Name is the only field filled every time, and
Short Description is filled on 82. **No keyword filter can reach a company
whose Apollo record has no keywords** — Northern Utah Glass, Wasatch
Window and Door, R & JL Exteriors and Smith Hardware and Glass all have an
empty Keywords field.

## Two changes worth making first

**1. Remove the employee cap.** Your buckets stop at 51-100. Nine of the
96 sit above it, and they are the biggest: Sunpro (750), Christensen
(500), Burton Lumber (350), Jones Paint & Glass (180), AMSCO (160).

**2. Set Account Location to Utah** if Utah is what you want. It is
currently United States, which is why the results show Carolina Home
Remodeling, Illinois Energy Windows and TR Construction.

## Keyword list

These are the window and glass keywords Apollo actually holds on the 96 —
not invented, counted. Paste the whole block into Company Keywords:

```
energy-efficient windows
window replacement
replacement windows
vinyl windows
windows
window installation
windows installation
custom windows
wood windows
fiberglass windows
aluminum windows
casement windows
architectural windows
window repair
window styles
window manufacturing
glass installation
glass and glazing contractors
residential glass services
commercial glass
insulated glass
low-e glass
architectural glass
energy-efficient glass
glass repair
glass doors
sliding glass doors
glass
```

A greedy pass over the data shows the first five alone
(`energy-efficient windows`, `windows`, `glass installation`,
`window replacement`, `window installation`) carry most of the gain,
reaching 38 of 96 where your current two reach 22.

## Run it as several searches, not one

No single filter gets everything. Run these and union the exports:

**Search A — keywords.** The block above, Utah, employees 1-10 through
200+, domain known.

**Search B — company name.** Apollo's company-name search for `window`,
then `glass`, then `glazing`. This is the single strongest signal at 65%,
and it reaches records with no keywords at all.

**Search C — industry codes.** The codes these companies actually carry:

| Code | What it is | On |
|---|---|---|
| NAICS 238150 | **Glass and Glazing Contractors** | 14 |
| NAICS 236118 | Residential Remodelers | 9 |
| NAICS 444180 | Other Building Material Dealers | 8 |
| NAICS 238160 | Roofing Contractors | 6 |
| SIC 1751 | Carpentry Work | 12 |
| SIC 5211 | Lumber & Building Materials Dealers | 7 |
| SIC 1521 | General Contractors, Single-Family | 6 |

NAICS 238150 is the exact code for this trade, but it is on only 14 of 96,
so it is a supplement and not a filter on its own.

## The nine that no filter reaches

Rosewood Home Remodeling, Burbach, Shelley Construction, Siding Solutions,
Mi Techo Roofing, R & JL Exteriors, Handyman Harman, Handyman Matters and
Monty's Handyman. They do window work, but nothing in their Apollo record
says so. The only way we found them was the Google Maps scrape plus a
website check — which is what the whole Utah exercise was.

That is the honest limit here: Apollo is good for enriching a list you
already have, and partial for building one. A keyword search will not
reproduce the 240.
