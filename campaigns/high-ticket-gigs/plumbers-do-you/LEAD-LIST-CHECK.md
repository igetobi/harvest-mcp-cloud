# Lead list check - "valid-Part 2 People List - MAIN MASTER PLUMBERS + HVAC LIST"

Sheet `1oQzMi08bWwmOfhNRkeYX8nzFAk8G_47a6kRSDs1dHBE`, checked 10 Nov 2026.
**1,641 rows, 78 columns**, same Apollo + email-validation schema as the
electrical list. No lead data is committed here -- counts only.

## Email quality: clean

| | |
|---|---|
| `status: valid` | 1,641 of 1,641 |
| blank email | 0 |
| `accept_all` | 0 |
| webmail | 1 |
| duplicate emails | 3 |
| `Do Not Call` | FALSE on every row |

Already validated upstream with MX and SMTP checks. Nothing here needs
re-verification.

## Targeting: strong

1,503 of 1,641 (92%) are C-suite, Owner or Founder. 760 are tagged
construction, 244 consumer services, 159 facilities services.

## The problem: a third of the list is HVAC, and the copy asks about sewers

The list is a **plumbers + HVAC** master list. Izzy's step 1 asks:

> Do you do sewer line & water main replacements in {{location}}?

Classifying each row on Company Name + Industry + Keywords + Title +
Website:

| Segment | Rows | Share |
|---|---|---|
| plumbing signal present | 1,042 | 63% |
| **HVAC only, no plumbing signal** | **494** | **30%** |
| neither signal | 105 | 6% |

An HVAC-only company answers "no" to that question. Examples in the list:
Brooks Heating and Air Conditioning, Carlson & Stewart Refrigeration,
Swift Air Conditioning, Authority Heating & Cooling.

That matters more than ordinary list waste, because the whole mechanic
depends on the honest answer being yes. A "no" ends the conversation
before the reveal in step 3 ever sends -- which is exactly the reason Izzy
pulled whole house wiring out of the electrical set.

The 105 "neither" rows are mostly generic "mechanical services" firms that
probably do plumbing but cannot be confirmed from the data. One is not a
contractor at all (a counselling practice).

## Rows dropped building the import

| Reason | Rows |
|---|---|
| duplicate email | 3 |
| company not in the US | 1 |
| **total dropped** | **4** |

The 9 rows with a blank Company City were originally dropped too. They are
now kept, with `location` filled from a fallback -- see below.

**1,637 rows ready**, every one with a non-blank `location` -- the 9 blank
cities were recovered rather than dropped, see below. 1,546 of them (94%)
carry a phone number. Final segment split: 1,040 plumbing, 493 HVAC-only,
104 unclear.

## Two other things worth a decision

**185 extra contacts beyond one per company.** 163 domains appear more
than once. Several people at the same firm get the same personal-looking
one-line question from the same sender. The campaign has
`stop_for_company: false`, so a reply from one does not stop the others.
Turning that on, or cutting to one contact per domain, avoids colleagues
comparing notes on what is meant to read like a genuine enquiry.

**Overlap with the old Plumbers campaign was not completed.** Thirteen of
the campaign's fourteen mailboxes already sent 4,626 emails to 1,246
plumbers on the old "performance based plumber leads" copy. Anyone on both
lists gets a very different second approach from the same address. The
Instantly leads endpoint rate-limited and then 502'd partway through
paging that campaign's roster, so this check is still outstanding.

## Decision: send to everything

Tobi's call, 10 Nov: run the whole list including HVAC rather than cut to
the 1,035 plumbing rows, to see what the HVAC segment actually replies.
The `segment` column tags every row plumbing / hvac-only / unclear, so
reply rate can be split by segment afterwards and the question answered
with data instead of a guess.

## The 9 blank cities, filled

Rather than drop them, `location` falls back in this order: Company City,
then the person's City **when the person's State matches the company's**
(so their city is plausibly the service area), then Company State.

| Company | Filled with | From |
|---|---|---|
| ResiXperts | San Antonio | person city |
| American Energy Supply - FuelOilNow.com | Philadelphia | person city |
| Mark Lindsay and Son Plumbing and Heating | New Jersey | company state |
| Northeast Water Wells | Peterborough | person city |
| RBE Inc | Clawson | person city |
| Install Geothermal | Florida | company state |
| Four Quarters Mechanical | Moorestown | person city |
| Custom Critical Cooling | Dallas | person city |
| Northeast Water Wells | Hudson | person city |

Seven get a real city, which reads far better in the one-line question
than a state does. Two fall back to the state: Mark Lindsay has no person
city at all, and Install Geothermal's contact sits in Chicago while the
company is in Florida, so the person's city would have named the wrong
market.

## Files

Built in the session scratchpad, not committed (they carry lead PII):

- `instantly_import_FINAL_1637.csv` -- **the one to import.** 1,637 rows,
  zero blank locations, `segment` column included
- `instantly_import_all.csv` -- earlier 1,628-row version, before the 9
  blank cities were recovered
- `instantly_import_plumbing_only.csv` -- 1,035 rows, HVAC removed
- `excluded_hvac_only.csv` -- the 491 HVAC-only rows

Column order matches what the Instantly importer expects, with
`phoneNumber` named explicitly so the mapping is not missed the way it was
on the electrical import.
