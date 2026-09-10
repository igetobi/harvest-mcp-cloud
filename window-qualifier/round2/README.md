# Round 2 — the companies the scraper could not settle

The site scrape (`../qualify.py`) resolved 1,163 of 1,746 companies from their own
websites, and prior research plus name/review keywords covered another 197. These 386
are what is left. Your workload file holds a slice of them.

Each one is here for a reason, shown as `why unresolved`:

| status | meaning |
|---|---|
| `NO_WEBSITE` | no website in the source data at all — search is the only route |
| `UNREACHABLE` | site did not load: dead domain, bot-blocked, or a bad certificate |
| `UNKNOWN` | site loaded but rendered its content in JavaScript, so there was no text |
| `SOCIAL_ONLY` | the "website" is a Facebook/Instagram/Yelp profile, not a real site |

For `UNKNOWN` especially, search works where the scraper failed: Google has already
rendered those pages, so the indexed text is exactly what the scraper could not see.

## The question

Does this company **install or repair windows in homes and buildings**? Full rules are in
`../../verification/CRITERIA.md` — read it. In short: replacement and new windows, window
glass and insulated-unit replacement, storefront glazing all count. Vehicles, window
cleaning, blinds and window film do not. A shop doing vehicle glass **and** building glass
counts, flagged.

## Budget — read before starting

You have a hard cap of **200 WebSearch calls** for ~78 companies, so about 2 each.

- One good search settles most. Keep the second for genuinely unclear cases.
- Spend them where a verdict could flip: glass shops, roofers, exteriors, remodelers,
  "windows & doors" names. Don't burn searches confirming a dog groomer.
- If you run out, mark the rest `UNCLEAR` with `"searched": "none — budget exhausted"`
  and say so. **Never infer a verdict from a company name.** An honest gap beats a guess.

Many of these have little or no web presence — that is why they are here. `UNCLEAR` after
two real searches is a legitimate, useful answer. Do not manufacture confidence.

## Output

Write one JSON object per company, one per line, to `results/session_<N>.jsonl`:

```
{"n": 12, "name": "...", "domain": "...", "verdict": "YES|NO|UNCLEAR|CLOSED",
 "confidence": "high|medium|low", "window_service": "", "segment": "Residential|Commercial|Both|",
 "also_auto": false, "primary_business": "", "evidence": "quote or page title/URL",
 "searched": "the queries you actually ran"}
```

Then commit and push to `claude/verify2-session-<N>`. Do not open a pull request.
Report your counts, how many you actually searched, and anything genuinely ambiguous.
