# Utah window-services site check

62 URLs supplied as a prospect list, checked against two questions: **does the
company offer window services**, and **is it based in Utah**. Rows are kept in
the order they were supplied so the CSV lines up with the source sheet.

| verdict | rows |
|---|---|
| QUALIFIED — offers window services and is Utah-based | 45 |
| EXCLUDED | 11 |
| REVIEW — could not be verified | 3 |
| DUPLICATE — same company listed twice | 3 |

59 unique domains, not 62: `elitewindowsut.com`, `goperformancewindows.com` and
`saltlakewindow.com` each appear twice in the source list.

## Files

| file | rows | what it is |
|---|---|---|
| `utah_window_site_check.csv` | 62 | every URL in source order, with verdict, address and evidence |
| `qualified_utah_window_companies.csv` | 45 | the QUALIFIED rows |
| `excluded.csv` | 17 | EXCLUDED + REVIEW + DUPLICATE, with the reason in `note` |
| `extract_signals.py` | — | pulls Utah/window/other-state signals out of fetched HTML |
| `build_results.py` | — | writes the three CSVs from the verified findings |

Columns: `n, url, company, window_services, utah_based, verdict, city, state,
street_address, phone, services, note, confidence`.

## Why rows were excluded

**Not Utah (5).** `windowanddoorco.com` and `honestviewwindows.com` and
`azvisionwindow.com` are Phoenix, Arizona; `windowanddoorreplacementcompany.com`
is Jupiter, Florida; `sunrise-windows.com` is a Temperance, Michigan
manufacturer.

**Utah, but not window services (6).** `amscowindows.com` (Salt Lake City
manufacturer, sells through dealers, does not install), `silvermountainglass.com`
(decorative and auto glass only), `safelite.com` (windshields),
`ripplecleaners.com` (window *cleaning* only), the `truteam.com` branch
(insulation), and `intermountainwindowsdoors.com` (see below).

## Traps in this list

- **`intermountainwindowsdoors.com` is a parked domain running a pay-per-call
  lead-gen page.** Its own disclaimer: "independent marketing and referral
  platform … not a direct service provider", "no affiliation with prior owner".
  A real Intermountain Windows & Doors LLC operates in Utah (Layton/Centerville)
  but no longer owns this domain. It was the only parked/lead-gen page in the 62.
- **Four sites share one build.** `murraywindowreplacement.com`,
  `windowdoorsaltlake.com`, `windowswestjordan.com` and
  `windowswestvalleycity.com` run a byte-identical WordPress + Elementor 4.2.2 +
  Google Site Kit stack with shared body copy. Each carries its own local street
  address and tracking number, but they may be one operator behind four
  city-targeted sites.
- **"Hurricane" is ambiguous here.** It is a real Utah city (Pro Install LLC is
  in Hurricane, UT) *and* the term for impact glazing, which is what
  `windowanddoorreplacementcompany.com` in Florida means by it. A keyword pass
  alone mislabels that row as Utah.
- **Manufacturer vs manufacturer-installer.** AMSCO is excluded because it only
  manufactures; Advanced Window Products and Peak Windows are qualified because
  each manufactures *and* installs.
- **National operators with Utah HQs or branches.** Performance Windows
  (Pleasant Grove HQ, ~40 offices nationally), Elite Windows (Pleasant Grove
  "CORPORATE", 8 offices), Revival Windows (Vineyard UT plus CO/ID/AZ), Mountain
  West Windows & Doors (3 Utah, 5 Arizona), Window World Utah (franchise),
  Renewal by Andersen Salt Lake City (Minnesota brand). Whether these belong on
  the list is a judgment call, so they are marked rather than dropped.
- **Two qualified companies are in southern or northern Utah, not Salt Lake.**
  Pro Install LLC (Hurricane) and Peak Windows (Hyde Park, Cache Valley).

## Confidence

`confidence` rates the evidence, not the company. Six sites blocked automated
requests or were down — `utahwindowpros.com`, `valleyglass.com`, `truteam.com`,
`sunrise-windows.com`, `utahwindowandglass.com`, `uwdsaltlake.com` — so their
rows rest on directory records, are marked `low` or `medium`, and say in `note`
that the address is unconfirmed. No attempt was made to spoof a browser past a
block.

Thirteen qualified companies publish no street address; their `street_address`
says so, and `city`/`state` carry whatever the site or its contact page states.

## Instantly overlap check

`instantly_overlap.csv` records, for each of the 59 unique domains, whether a
lead on that domain already exists in Instantly.

**10 of the 59 are already in the "Window Installation Campaign (Performance
based Campaign)"** (campaign `77b57a60-1291-4949-bb7e-722a780bb2a7`, status
completed), covering 17 contacts. Every one of those contacts finished the
sequence and none replied; the last send was 16 October 2026, except Mountain
West Windows & Doors on 21 September.

| company | domain | contacts |
|---|---|---|
| EPIC Windows & Doors | epicwd.com | 4 |
| Energy Home Improvements | energyhomeimprovements.com | 3 |
| Revival Windows | gorevivalwindows.com | 3 |
| Advanced Window Products | advancedwindows.com → advancedwindowsusa.com | 1 |
| Elite Windows | elitewindowsut.com | 1 |
| Mountain West Windows & Doors | mwwd.com (email at pellamw.com) | 1 |
| Optimum Windows & Doors | optimumwindowsanddoors.com (email at optimumsolargroup.com) | 1 |
| Renewal by Andersen of Utah | renewalbyandersen.com → rbaslc.com | 1 |
| The Brokerage Windows & Doors | thebrokeragewindows.com | 1 |
| Valley Glass | valleyglass.com | 1 |

The other **49 domains appear nowhere in Instantly** — not in a campaign and
not in an unattached lead list.

### How the check was run

Two passes, because a search on the domain alone would have missed three of the
ten. First, the whole 133-lead roster of the window campaign was pulled and
matched locally on both `company_domain` and the `website` field, which is what
caught Advanced Window Products (trading on advancedwindowsusa.com), Renewal by
Andersen of Utah (rbaslc.com), Optimum (email at optimumsolargroup.com) and
Mountain West (email at pellamw.com). Second, each of the 49 unmatched domains
was searched across all campaigns and lead lists, and each came back empty.

Two near-misses worth recording, since both would be wrong to count as hits:
the campaign's "Pro Install" is a South African company (proinstall.co.za), not
Pro Install LLC of Hurricane, Utah; and the "Window World" leads in Instantly
are Window World **Austin**, sitting in the Texas lead list with no campaign
attached, not Window World Utah.

The window campaign also holds Utah window and glass companies that are not on
this list at all — Jones Paint & Glass, Northern Utah Glass, Skyview Glass,
SONIQ Windows and Doors, St George Windows, Siding Solutions & Construction,
RGS Exteriors and Elevate Windows among them.
