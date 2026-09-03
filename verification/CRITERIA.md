# Task: qualify companies for WINDOW INSTALLATION / WINDOW REPLACEMENT (buildings, not vehicles)

## Goal
The client wants a lead list of companies that **install or replace windows in homes and
buildings** — residential replacement windows, new-construction windows, window glass
replacement in a house/office, commercial storefront glazing. It can be their main service
OR one service among several.

## Hard network constraint
Direct page fetching is BLOCKED in this environment. `WebFetch` returns EGRESS_BLOCKED and
curl gets 403 on CONNECT for every domain. **Use `WebSearch` only.** WebSearch returns real
indexed page titles, URL paths and body text from the company's own site — that is your
evidence. Do NOT attempt WebFetch/curl; do not report sites as "down" because of the block.

## Verdicts
- `YES`  — evidence the company installs or replaces windows in buildings.
- `NO`   — evidence they do NOT (they do something else).
- `UNCLEAR` — searched properly, but no usable evidence either way.
- `CLOSED` — evidence the business is permanently closed / defunct.

## INCLUDE as YES
- Replacement / new window contractors, "windows & doors" companies
- Exterior remodelers where windows are a listed service (siding + windows + roofing etc.)
- Roofers who ALSO list window installation/replacement as a service
- General contractors / remodelers who explicitly list window installation or replacement
- Glass companies doing **residential or commercial window glass replacement**, broken window
  glass repair, insulated/thermal glass unit (IGU) replacement, foggy window repair
- Commercial / storefront glazing contractors (storefront windows, curtain wall, glass fronts)
- Manufacturers or dealers that **also install** for end customers (direct-to-consumer)
- Companies that do auto glass AND residential/commercial window glass — YES, but set
  `also_auto: true` so the client can decide

## EXCLUDE as NO
- Auto glass / windshield repair / car tint / car stereo & audio — **with no** building-window work
- Window CLEANING / washing / pressure washing
- Window TINT or FILM application only (no window install/replacement)
- Blinds, shades, shutters, drapery, window treatments, window coverings
- Locksmiths; garage doors; HVAC; gutters-only; painting-only; fencing; pest; foundation
- Roofing-only (no windows listed)
- Door-only companies (entry/iron/sliding/patio door repair or refinishing, no windows)
- Shower door / mirror / tabletop / cabinet-glass shops with NO house-window work
- Pure wholesale suppliers / distributors / manufacturers that do **not** install or sell to
  end customers
- Window screen repair only (screens are not windows) — NO, note it
- Directory/lead-gen/aggregator sites rather than a real contractor — NO, note it

## Method (per company, do this properly)
1. Run at least ONE `WebSearch`. Good query shapes:
   - `"<Company Name>" <city> TX windows installation replacement services`
   - `<domain> window replacement services`
   - `site:<domain> windows`  (as a plain query: `<domain> windows services`)
2. If the first search is inconclusive, run a SECOND, differently-worded search before
   settling on UNCLEAR. Try the domain alone, or the company name + "services".
3. The Google review snippet given in the batch file is real customer text — it is usable
   supporting evidence (e.g. a review describing a window install), but prefer the company's
   own site content when available.
4. NEVER decide from the domain name alone. "windowsomething.com" is not evidence.
   A name like "XYZ Glass" is not evidence either way — search it.

## Output — CRITICAL
Append one JSON object per company, ONE PER LINE (JSONL), to your assigned output file using
the Write tool (write the whole file at once at the end; do not use Bash heredocs).

Fields, exactly:
```
{"id": 12, "name": "...", "domain": "...", "verdict": "YES|NO|UNCLEAR|CLOSED",
 "confidence": "high|medium|low",
 "window_service": "short description of the window work they do, or \"\" if none",
 "segment": "Residential|Commercial|Both|",
 "also_auto": true|false,
 "primary_business": "short phrase — what they mainly do",
 "evidence": "a short quote or the page title/URL path that proves it",
 "searched": "the query/queries you actually ran"}
```
Every company in your batch must appear exactly once. Do not skip any. Do not invent
evidence — if you did not see it in search results, say so and use UNCLEAR.
