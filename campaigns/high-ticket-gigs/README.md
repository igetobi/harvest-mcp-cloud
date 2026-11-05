# High-ticket gig variables for the "do you do ___?" campaigns

Built for the simple first-email test from the 4 Nov client acquisition meeting:
one line, one question, one variable, A/B tested across variants.

```
Hi {{firstName}},

Do you do {{gig}}?

{{sendingAccountFirstName}} from Black Swan Media
```

Five niches, five variants each, US residential. `high_ticket_gigs.csv` holds
the ranked table with prices and warnings; `instantly_variants.csv` is the flat
version, one row per variant with the subject and body already written.

## The selection rule

High ticket alone is the wrong filter. The mechanic only works if the honest
answer is **yes** — a "no, we don't do that" ends the conversation before it
starts and costs an inbox a reply it could have had. So every variant was
scored on **ticket size times how many companies in the niche actually do it**,
and the ones that are big money but rare are ranked lower and flagged.

Geothermal HVAC is the clearest example of what got left out: $15,000–$50,000 a
job, and almost nobody on a general HVAC list installs it. Same story for
whole-house water filtration in plumbing. Both would read as "do you do
[thing we don't do]?".

The reverse trap is in the window niche. The list is called window *repair*,
but a repair is a few hundred dollars. All five window variants are
replacement work, because that is where the five-figure jobs are.

## Rank 1 per niche, if you only test one

| niche | variant | typical US ticket |
|---|---|---|
| plumbers | sewer line replacements | $4,000 – $15,000 |
| electricians | electrical panel upgrades | $1,500 – $6,500 |
| hvac | full system replacements | $7,000 – $16,000 |
| pest control | termite treatments | $620 – $1,500/yr |
| window | full home window replacements | $6,000 – $24,000 |

## Deliberate wording pairs

Three variants exist to test *words*, not services, which is the cheapest
learning in the set:

- electricians: `electrical panel upgrades` vs `200 amp service upgrades` — the
  same job in homeowner words and in trade words.
- hvac: `full system replacements` vs `AC replacements` — the same money, one
  phrased as a project and one as the thing the customer asks for.
- plumbers: `sewer line replacements` vs `trenchless sewer line replacements` —
  adding one word raises the ticket and narrows who can say yes.

## Regional variables — segment before you send

Four variants are dead in the wrong market and will pull a flat zero:

- `hurricane impact windows` — Florida, Texas and the Gulf. **Note this does
  not fit the Utah window list we just qualified.**
- `termite tenting` — Florida, California, the Southeast.
- `crawl space encapsulation` — crawl-space markets, so not the Southwest.
- `egress window installs` — basement markets.

## Pricing

Figures are 2026 US cost-guide and contractor-pricing data, pulled 5 Nov 2026.
They are planning ranges, not quotes, and the sources disagree by a wide margin
on the larger jobs — whole-home rewire estimates ran from $8,000 to $30,000
across three sources. They are here to rank the variants by ticket size, which
they are good enough for; don't quote them to a prospect.

One figure is not verified: `egress window installs`. It is in the table as a
candidate with the price left blank rather than guessed.

Sources: Angi 2026 cost data (window replacement, impact windows, patio doors,
termite tenting, bed bug treatment, HVAC replacement, plumbing repair),
HomeGuide, HomeAdvisor, EnergySage, QuoteScore, and contractor pricing guides
(snapscopeai, pipelineon, costprism, hvacprojectcost, pestprothermal,
atticareusa).
