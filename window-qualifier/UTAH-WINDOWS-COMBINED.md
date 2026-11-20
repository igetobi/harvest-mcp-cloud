# Utah window companies: combined inventory

Every verified Utah window installation or repair company we hold, merged from all
sources, with each domain graded by whether Apollo can actually resolve it. Built
20 Nov 2026.

## Sources merged

| Source | Contributed |
|---|---|
| Google Maps scrape 1 | 667 rows |
| Google Maps scrape 2 | 1,007 rows |
| Instantly Window Installation campaign | 9 Utah companies found nowhere else |
| Apollo 94-row enrichment | phone/contact data |
| Apollo 512-domain run | 222 returned, 76 good |
| Apollo 595-row keyword run | 75 new, 13 good |

**253 distinct companies after dedupe on domain.**

## Apollo resolution grades

| Grade | Count | Meaning |
|---|---|---|
| Apollo confirmed | 89 | Apollo holds this domain and places the company in Utah. Safe to enrich. |
| Apollo finds wrong org | 20 | Apollo holds the domain but returns an out-of-state parent. |
| Apollo missed | 144 | Submitted in the 512 run; Apollo returned nothing. |
| **Total** | **253** | |

## The franchise trap

These 20 domains belong to national brands or franchise networks. Apollo has the
domain, but the company record behind it is the national entity, so enriching them
returns a decision maker in Ohio, Texas or Nebraska rather than the Utah branch.
Sending them to Apollo is not wrong, but the contacts that come back are not
local and should not go into a Utah campaign without checking.

| Domain | What Apollo returns instead |
|---|---|
| acehandymanservices.com | "Handyman Matters" in Colorado |
| aplusqualityglass.com | "A Plus Quality Glass of" in Arizona |
| brightsidewindows.com | "Brightside Windows" in Oregon |
| gatsbyglass.com | "Gatsby Glass®" in Nebraska |
| getmontys.com | "Monty's Handyman Services" in California |
| glassdoctor.com | "Glass Doctor of Dallas Metroplex" in Texas |
| goelevatewindows.com | "Elevate Windows" in Arizona |
| goperformancewindows.com | "Performance Window Fabrications" in England |
| handymanconnection.com | "Handyman Connection" in Ohio |
| harmanhandyman.com | "Handyman Harman" in Illinois |
| harringtonco.com | "Harrington & Company" in New Hampshire |
| luxviewsystems.com | "LuxView" in Tennessee |
| ntywindows.com | "NTY Windows" in Nevada |
| shelley-construction.com | "Shelley Construction LLC" in Ohio |
| stronghousebrands.com | "Stronghouse" in Illinois |
| synergywindow.com | "Synergy Windows of Atlanta, LLC" in Georgia |
| thevantagewindows.com | "Vantage Windows" in Texas |
| truteam.com | "TruTeam" in Florida |
| unitedporte.us | "United Porte Inc." in New Jersey |
| windowdepotusa.com | "Window Depot USA" in Ohio |

## The 144 Apollo missed

These were all submitted in the 512-domain run and came back empty. They are real
companies with working sites and, in almost every case, a phone number from the
Maps scrape - Apollo simply has no company record for them. They are mostly small
local operators, which is exactly the segment Apollo is weakest on.

Re-sending them is cheap but unlikely to return much. The phone numbers we already
hold from Google Maps are the better asset for this group.

## Files

| File | Contents |
|---|---|
| `utah_window_companies_COMBINED.csv` | all 253, with company, city, phone, Apollo grade |
| `utah_window_domains_FOR_APOLLO.txt` | the 89 confirmed domains, one per line |
| `utah_window_domains_FRANCHISE_CAUTION.txt` | the 20 franchise domains |
| `utah_window_domains_APOLLO_MISSED.txt` | the 144 Apollo has no record of |
| `utah_window_domains_ALL_253.txt` | every domain, one per line |

Phone numbers live in the CSVs only, not in this repo.
