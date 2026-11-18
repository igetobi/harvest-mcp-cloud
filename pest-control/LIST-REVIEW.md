# Pest control master list - review before Hunter

Apollo accounts export, 4,261 rows, reviewed 18 Nov 2026. Counts only, no
business data committed.

## Verdict: a clean list. 65 rows out, 4,196 to send.

Far better than the Utah window scrape. Every row has a website, there are
no social-profile or site-builder URLs, 4,260 of 4,261 domains are
distinct, and 99% carry a pest-control signal in the name, industry,
keywords or description.

## What to remove

| Reason | Rows |
|---|---|
| Foreign domain, not a US business | 58 |
| Not a pest control company | 5 |
| Duplicate domain | 1 |
| No pest signal anywhere in the record | 1 |
| **Total** | **65** |

### The 58 foreign rows are the same Apollo bug as the window list

Each carries a `.co.uk`, `.com.au`, `.ca`, `.co.za`, `.in`, `.ie`, `.de`
or `.bm` domain while Apollo assigns it a US city. The pairings give it
away:

| Company | Domain | Apollo says |
|---|---|---|
| Canberra Pest Control | canberrapestcontrol.com.au | Mitchell, **South Dakota** |
| JCS Pest Control Nottingham | jcspestcontrol.co.uk | Nottingham, **Pennsylvania** |
| Kenilworth Pest Control Limited | kenilworthpestcontrolltd.co.uk | Kenilworth, **New Jersey** |
| Best Pest Control Sydney | bestpestcontrolsydney.com.au | Sturgeon Bay, **Wisconsin** |
| Bermuda Pest Control | pestcontrol.bm | Warwick, **New York** |

Apollo matched a British, Australian or Bermudian town to a same-named US
town. It is exactly what put seven Syracuse, New York window companies in
a Utah list. **Filtering on Apollo's country field alone will never catch
it** -- all 4,261 rows say United States. The domain TLD is the only
reliable tell.

### The 5 that are not pest control

Holly Springs Chamber of Commerce; The Greek Co (`dollclothesstore.com`);
BBwear (`bbwear.co.uk`, beekeeping clothing); Goose Dogs For Sale; and the
pair "Domain Pest Control" / "Pest Control Domains", which sell domain
names rather than pest control.

`capitalpest.com` appears twice and one copy was dropped.

## What I checked and found nothing wrong with

**417 rows whose company name shares no word with its domain.** Nearly all
are legitimate short or branded domains -- `azpest.com` for Arizona Pest
Control, `nwexterminating.com` for Northwest Exterminating, `ipm4u.com`
for Innovative Pest Management. Not a usable signal; no action taken.

**60 company names appearing more than once** (Premier Pest Control,
Coastal Pest Control, Tri County Pest Control). Different businesses on
different domains sharing a common trade name, not duplicates.

**Only 16 franchise-branded rows** (Orkin, Terminix, Arrow, Critter
Control, Mosquito Joe, Pestmaster). Left in -- too few to matter, and some
franchisees do buy their own leads. Strip them if the pitch is owner-only.

## What this means for the Hunter run

| | |
|---|---|
| Domains to search | 4,196 |
| Hunter balance | 19,876 credits |
| Cost | 1 credit per company that returns emails, nothing for the rest |
| Expected hit rate | ~27%, from the Utah run on a comparable list |
| Expected result | ~1,100 companies with contacts, ~1,100 credits |

Credits are not the constraint. **Call volume is.** Bulk-Domain-Search
accepts 50 domains, but in the Utah run a 50-domain call rate-limited
after 19; batches of 15 ran clean. At 15 per call this list is **~280
calls**, which is impractical in one session.

Options:
1. Upload the domain list to Hunter's own bulk tool in the web app, which
   is built for this size.
2. Have me run a prioritised slice here -- the 710 companies with 6+
   employees would be ~48 calls and are the ones most likely to have a
   published decision maker.

**Size is the real risk.** Median headcount is 3, and 67% of the list has
5 employees or fewer. Hunter can only find what a company has published,
and a three-person pest firm with a contact form and no named staff page
returns nothing. Expect the hit rate to sit at the low end.

## Files

In the session scratchpad: `pest_CLEAN.csv` (4,196 rows, full Apollo
schema), `pest_removed.csv` (the 65, each with its reason) and
`pest_domains.txt` (one domain per line, ready for Hunter's bulk upload).
