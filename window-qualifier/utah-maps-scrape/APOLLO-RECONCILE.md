# Apollo enrichment, reconciled against our 236

Apollo returned 94 companies from 236 domains. Checked 16 Nov 2026.

## Do they match? Mostly, with three distinct failures

| | Rows |
|---|---|
| Apollo rows whose domain is one of our 236 | 88 |
| Apollo rows that are **not our companies at all** | 6 |

### The 6 that are not ours

| Apollo returned | On domain | Where |
|---|---|---|
| NeoLake Property Repair | jobbersites.com | Salem, New Hampshire |
| techcrew AI | ueniweb.com | Vadodara, India |
| Mr Handy Services | mrhandy.in | Lucknow, India |
| Abco Glass Products | abcoglass.com | — |
| Salt Lake Window Company LLC | utahwindowcompany.com | Salt Lake City |
| JDI Windows | jdiwindows.com | Littleton, Colorado |

The first three are the **no-code site builder problem** landing exactly
where it was flagged. Our rows carried subdomains like
`beckerwindows.jobbersites.com`; stripped to the root, Apollo matched the
site builder's own corporate record and returned whoever it had filed
there, including two Indian companies.

The other three are name collisions: we hold **ABCO Windows & Doors**
(`abcowindowsanddoors.com`), **Salt Lake City Window Company**
(`saltlakewindow.com`) and **JDI Windows** (`jdiwindowsutah.com`). Apollo
returned different businesses on different domains, one of them a Colorado
firm with the same name.

## Of the 88 that do match

| Apollo says | Rows |
|---|---|
| Utah | 63 |
| Outside Utah | 21 |
| No state given | 4 |

The 21 split into two very different cases, and the split is clean:

**18 had a verified Utah street address in the Maps data.** Apollo
returned the national parent, not the local branch: Glass Doctor of Utah
County came back as Glass Doctor of Dallas Metroplex, Window Depot Utah as
Window Depot USA in Ohio, Gatsby Glass of Sandy as the Omaha head office,
Synergy Windows of Salt Lake City as Synergy of Atlanta, All Purpose
Windows as TruTeam in Florida. These are still our Utah businesses --
but **the contacts Apollo attaches will be head-office staff in another
state**, not the local owner. Enriching them gets the wrong person.

**3 were service-area listings with no street address**, which is where
our geography was inferred from Utah zips rather than read off an
address. Apollo gives them real addresses elsewhere, so the inference was
wrong and they are out: RMK Windows (Gilbert AZ), Window Kings
(Clearwater FL) and X Siding (Aurora CO).

## Removed: 9 rows, 236 -> 227

| Company | Why |
|---|---|
| RMK Windows | Apollo places it in Gilbert, Arizona |
| Window Kings | Apollo returns Karoly Windows, Clearwater, Florida |
| X Siding | Apollo places it in Aurora, Colorado |
| Boise Window Medics | name says Idaho, service-area listing only |
| Boise Window Company | name says Idaho, service-area listing only |
| Phoenix Exteriors | `phxexteriors.com`, service-area listing only |
| Cascade Windows (Cornerstone) | national manufacturer, not a local installer |
| Builders FirstSource | national supplier, not a local installer |
| Sierra Pacific Windows | national manufacturer, not a local installer |

The three Boise/Phoenix rows were caught by their own names, not by
Apollo. All six geography removals are service-area listings, which is the
same weakness in one form: **a business with no street address cannot be
placed by the zips it advertises into.** Of our 85 service-area rows
Apollo could only speak to 6, so the other 79 carry that same risk
unverified.

## What Apollo could not match: 148 of 236

69 have a Utah street address, 79 are service-area only. Apollo's coverage
is thin on small owner-operated contractors, which is most of this list.
That is not a fault in the list -- it means **Apollo alone will not get
this campaign to a full sending roster**, and the remaining 148 need
Hunter, a site-crawl for a contact page, or hand research.

## Where that leaves the list

| | |
|---|---|
| Companies after removals | **227** |
| Address confirmed by Apollo | 63 |
| Utah branch, Apollo holds the parent (do not use Apollo's contacts) | 15 |
| Apollo matched, no address | 4 |
| No Apollo record | 145 |
