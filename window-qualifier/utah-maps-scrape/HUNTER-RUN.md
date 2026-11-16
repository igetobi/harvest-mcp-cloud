# Hunter run on the 145 Apollo could not match

Run 16 Nov 2026. **43 credits spent**, 19,876 left of 24,000; the quota
resets 15 Dec. Searches cost 1 credit per 10 emails returned and are
charged only when emails come back, so the 106 domains with nothing cost
nothing.

## Result

| | |
|---|---|
| Domains searched | 145 |
| Companies with at least one contact | **39** |
| Emails returned | **62** |
| Personal addresses (a named person) | 33 |
| Generic (info@, sales@, support@) | 29 |
| Verified `valid` by Hunter | 16 |
| Named decision makers (Owner, Director, Manager, Controller) | 9 |

**Hit rate 27%** -- 39 of 145. Combined with Apollo's 88, roughly half the
list now has a route in.

### The best of it

**Revival Windows** (`gorevivalwindows.com`) returned ten contacts
including three owners -- Bridger Allman, Landon Tolman and James
Wadsworth -- all verified valid, with LinkedIn profiles. **Advanced Window
Products** returned four, including Will Miller, Marketing Director and
Owner. Those two alone are worth the run.

### Four domains returned emails that are not usable

| Domain | Why not |
|---|---|
| `mrhandyman.com` | the national Mr. Handyman corporate domain. 108 emails, franchise owners across the US, none of them the Utah branch |
| `soniqwindows.com` | a national franchise: 14 city-branch generics for Austin, Boise, Dallas, Portland, Seattle, Phoenix, Tampa, Nashville |
| `magnawindows.co.uk` | a **UK** company. A `.co.uk` domain should never have survived into a Utah list |
| `vzionglass.com` | Hunter names the organization "Coeur D'Alene", which points at Idaho |

The first two are the franchise-parent problem that Apollo also hit,
arriving by a different route. The last two are more geography that slipped
through: both were service-area listings with no street address.

Also worth pulling: `utahretractableawnings.com` returned a contact, but
retractable awnings are not windows and the row should not have been in
the list.

## The 106 with nothing

Mostly one-person contractors whose site carries a contact form and no
published address. Hunter cannot find what was never published. For these
the options are a crawl of the contact page, the phone number already on
the row (232 of 236 have one), or dropping them.

Several returned an organization name but no email, which at least
confirms the domain is live: Alta Glass & Window, GH Windows, Higgins
Windows & Doors, Granite Peaks Glass, Summit Glass Co, Tony's Roofing &
Windows, Utah Window and Glass, M3 SLC Windows & Doors, Three Sigma
Windows, Total Windows and Glass, Window King, Skyline Windows, Alpine
Doors & Windows, Canyon Ridge Glass, Sugar House Glass and Red G Glass.

## Output

`hunter_contacts.csv` in the session scratchpad: 62 rows, one per email,
joined to the company name, phone and address from our list, sorted
personal addresses first and then by confidence.

**Nothing was saved to Hunter leads.** The run only returned results.
