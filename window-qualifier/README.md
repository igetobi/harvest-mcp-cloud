# window-qualifier

Decides, for a list of companies, which ones **install or replace windows in homes and
buildings**. Vehicles, window cleaning, blinds and window film do not count.

It works by fetching each company's own website and reading it, rather than asking a
language model about each company one at a time. That is the whole point: a 1,700-company
run costs a few minutes of bandwidth and **zero model tokens**, and every verdict quotes
the company's own page text so you can check it yourself.

## Run it

```bash
pip install requests beautifulsoup4
python3 qualify.py --input companies.csv --out qualified.csv
```

Options:

| flag | meaning |
|---|---|
| `--workers N` | parallel fetches, default 12 |
| `--limit N` | stop after N companies, for a quick trial run |
| `--cache DIR` | where fetched pages are stored, default `./cache` |

Every fetched site is cached under `--cache`, keyed by domain. A re-run costs nothing for
sites already fetched, and an interrupted run picks up where it stopped — so you can start
with `--limit 50`, check the output looks right, then run the whole file.

## What it does per company

1. Fetches the homepage, trying `https://` then `http://`.
2. Scores the internal links and follows up to 3 that look like service pages — anything
   whose text or URL mentions windows, glass, services, products, residential or commercial.
   A link with "window" in it is always followed first.
3. Strips scripts and markup, concatenates the visible text.
4. Applies the verdict rules below and records a verbatim quote as evidence.

## Verdicts

| verdict | meaning |
|---|---|
| `YES` | strong window-work signal, or two or more weaker ones |
| `LIKELY` | a single weak signal — worth an eyeball, not a confident yes |
| `NO` | site read fine, no window installation or repair offered |
| `UNKNOWN` | site returned almost no readable text (often a JS-only build) |
| `UNREACHABLE` | site did not load — error or HTTP status is in the `note` column |
| `NO_WEBSITE` | no website in the source data |

`also_vehicle_glass` is a separate column, not a verdict. Plenty of glass shops do
windshields *and* house windows; that column lets you filter them out if you want no
car association in outreach, without the tool silently dropping them.

## Columns out

`name, website, domain, phone, address, rating, review_count, verdict, window_services,
also_vehicle_glass, evidence, note, pages_checked`

`evidence` always contains the exact phrase that triggered the verdict — if it doesn't
read like window work to you, it isn't, and you can throw the row out on sight.

## Input format

The loader expects the Google-export shape: no header row, company names that contain
commas and spill across several columns. It locates the phone, address and website by
their shape rather than by column position, and treats everything before them as the name.
A normal CSV with a header will not parse correctly — adjust `load_companies` if your
export differs.

## Known limits

- A JS-rendered site with no server HTML gives `UNKNOWN`. Those need a headless browser;
  Chromium is available in this environment via Playwright if it becomes worth it.
- A passing mention ("our cafe has a lovely bay window") scores `LIKELY`, never `YES`.
  That is deliberate — weak signals are surfaced for review rather than asserted.
- It reads only the site. A company whose site is a one-page brochure may be
  under-reported; the `pages_checked` column shows how much was actually read.
