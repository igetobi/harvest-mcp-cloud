# Website checks: 75 new Apollo window finds (Utah)

Checked 20 Nov 2026. Source: the 75 rows of the 595-row Apollo export that were
not already in our Utah window inventory. Each domain was fetched and read; the
verdict is what the site itself says, not what Apollo classified it as.

## Result

| Verdict | Count |
|---|---|
| YES | 18 |
| NO | 35 |
| UNCLEAR | 2 |
| DEAD | 19 |
| HIJACKED | 1 |
| **Total** | **75** |

**13 confirmed Utah window installers or repairers.** That is a 17% hit rate on
this batch, well below the ~78% the filter sample predicted.

## Keep (13)

| # | Company | Domain | Apollo city | Evidence |
|---|---|---|---|---|
| 16 | UOME Windows And Doors | buildwithuome.com | Murray | German Aluplast window systems, in-house installation |
| 17 | HDI Glass | bountifulwindows.com | Bountiful | window installation and replacement service pages |
| 24 | PROVUE WINDOWS LLC | provuewindows.com | North Salt Lake | window replacement and window installation pages |
| 26 | Kimball Roofing | kimballroof.net | Heber City | window replacement & repair listed, roofing primary |
| 35 | Moyes Glass | moyesglass.com | Ogden | window repair and replacement across the Wasatch Front |
| 44 | KOR Window Systems | korwindows.com | Salt Lake City | European-style windows and doors, installation and support |
| 45 | Daylight Glass | daylightglassutah.com | Morgan | window installation solutions |
| 48 | Legacy Windows LLC | thelegacywindows.com | Layton | "We install brand-new windows" |
| 55 | VIZN Home Soultions | viznhome.com | Lehi | door, window and trim installation |
| 66 | Midway Windows & Doors | midway-windows.com | Midway | residential and commercial window replacement and installation |
| 68 | Barker Glass | barkerglass.com | Willard | "install new windows, replace outdated ones" |
| 71 | Faus Glass | fausglass.com | Saint George | residential window glass replacement |
| 74 | GORDON'S GLASS CO | gordonsglass.net | Logan | residential window glass replacement, mostly repair |

Phone numbers are in the delivered CSV, not here.

Judgement calls inside that set: Kimball Roofing is roofing-first with window
replacement as a listed service; Faus Glass and Gordon's Glass are glass shops
that replace window glass rather than fit whole units. Keep or drop by how tight
the offer needs to be.

## Out-of-state leakage through the location filter (6)

Apollo assigned every one of these a plausible Utah city. The site says otherwise.
This is the same city-name collision seen in the Utah window scrape (Syracuse NY)
and the pest control list (Canberra -> Mitchell, South Dakota). There is no way to
catch it from the export alone, because Apollo also stamps Country = United States
on every row. The website is the only tell.

| # | Company | Domain | Apollo city | Actually | Window work? |
|---|---|---|---|---|---|
| 34 | SKYLINE CONTRACTORS | skylinecontractorsllc.com | Riverton | NY | YES |
| 38 | Wholesale Window and Door Co | wholesalewindowco.com | Orem | CA | YES |
| 39 | Hillcrest Construction Inc | hillcrestconstruction-inc.com | Midvale | CO | NO |
| 59 | Paulson's Construction, Inc. | paulsonsconstruction.com | Salt Lake City | MI | YES |
| 60 | Rocky Mountain Contracting | rockymountaincontracting.net | Sandy | WY | YES |
| 64 | Ray Building Co | raybuildingcompany.com | Saratoga Springs | AL | NO |

## Dead, parked and hijacked domains (20)

Do not mail any of these.

| # | Company | Domain | Why |
|---|---|---|---|
| 2 | Glass Recycling Group | glassrecyclinggroup.com | DNS does not resolve |
| 6 | Quality Hardware and Glass | qualityhardwareandglass.com | HTTP 503 on two separate attempts |
| 7 | PHILS GLASS, INC. | philsglassinc.com | DNS does not resolve |
| 12 | Uniglass | uniglass.net | DNS does not resolve |
| 14 | Top Tier Windows and Doors LLC | toptierwd.com | DNS does not resolve |
| 19 | Vinyl Guys Inc. | vinylguysinc.com | page returns 200 with only "Loading..." on all paths |
| 20 | Top Notch Glass | topnotchglass.com | redirects to a GoDaddy for-sale parked page |
| 22 | Wholesale Windows & Doors | wholesalewindowinc.com | HTTP 503 on two separate attempts |
| 25 | Revision Kitchen and Bath | revision-ut.com | HTTP 503 on two separate attempts |
| 28 | Jim Carver & Sons | jcands.com | HTTP 202 empty body on two attempts |
| 29 | Integrity Glass | fomototo4.lat | domain now an Indonesian gambling site |
| 32 | The General Contractors | thegeneralcontractors.com | redirects to a HugeDomains for-sale page |
| 36 | J Z Construction | jzconstruction.com | DNS does not resolve |
| 37 | Biofire Inc | biofireinc.com | HTTP 503 on two attempts |
| 40 | House to HOME Construction (Utah) | housetohomefix.com | DNS does not resolve |
| 49 | Nova Glass Solutions | novaglass.net | HTTP 503 on two attempts |
| 51 | J Wagoner Glass INC | windowsogden.com | HTTP 403, blocks automated fetch |
| 56 | TNT Industries LLC | tnthomeexteriors.com | HTTP 503 on two attempts |
| 61 | Design Stone Works | designstoneworks.com | HTTP 503 on two attempts |
| 63 | Utah County Handyman | utahcountyhandyman.com | HTTP 404 |

Integrity Glass is the notable one: the domain Apollo holds for it now serves an
Indonesian gambling site. Two others are parked for sale.

Caveat on the 503/403/202 rows: ten of these twenty returned a server error or an
empty body rather than a DNS failure, across two passes run some time apart. A DNS
failure means the domain is gone; a 503 or 403 can equally mean the site blocks
automated fetching. So some of those ten may be live companies we simply cannot
read this way. If the keeper list needs more volume, that is the set to check by
hand or by phone before writing them off - in particular J Wagoner Glass
(windowsogden.com, a 403) and Quality Hardware and Glass, whose names suggest real
window work.

## Unresolved (2)

| # | Company | Domain | Why |
|---|---|---|---|
| 9 | Utah Discount Windows & Doors | utahdiscountwindows.com | pay-per-call referral page, not a direct provider |
| 47 | P3 Windows and Doors, now trading as Viewpoint Utah (Park City) | p3windows.com | window and door showroom, installation not stated |

## What the industry filter let through

The NO set is a list of things the construction / building-materials /
glass-and-ceramics industry filter cannot separate from window work: staircases and
railings, commercial masonry, cultured marble, shower enclosures, pet doors, garage
doors, hollow metal door frames, barrier netting, concrete cutting, industrial
boiler contracting, pool tile, stoneware pottery, event decoration, art glass
exhibitions, a glass-machinery dealer and a used building-materials marketplace.

The filter is still the right one to run - it is recall we want from Apollo - but
nothing in the export distinguishes these, so the website pass is not optional.

Both unresolved rows are worth a manual look rather than a drop: #9 may be a lead
broker rather than a contractor, which would make it a competitor, and #47 is a
Park City window and door showroom that very likely installs but does not say so
on the page that loaded.
