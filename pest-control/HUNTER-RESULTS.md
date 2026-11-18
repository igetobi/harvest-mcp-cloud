# Hunter bulk, run 2 - pest control

Bulk 2226525, 18 Nov 2026. 4,196 domains, **3,079 emails found**, 2,595
downloaded as valid for **949 credits**.

Run 1 (bulk 2226517) returned 182 emails for ~194 credits. The only
difference was the required-fields filter: run 1 demanded a phone number,
run 2 demanded a full name. Same list, same everything else, **17x the
result**.

## What came back

| | |
|---|---|
| Contacts | 2,586 after removing 9 foreign rows |
| Distinct companies | **946** of 4,196 (23%) |
| Contacts per company | avg 2.7, max 10 |
| Verification | 100% valid |
| Type | 100% personal, zero role mailboxes |
| Median confidence | 95 |

Field fill:

| Field | Filled |
|---|---|
| Email, first name, last name | 100% |
| **Job title** | **90%** |
| LinkedIn URL | 81% |
| Department | 89% |
| Headcount | 94% |
| Phone number | 6% |

**A correction to the estimate I gave before the run:** I predicted ~25%
of results would carry a job title, from the unfiltered Utah run. The real
figure is 90%. Setting Type to Personal and the departments to Executive /
Finance / Sales / Marketing "in priority" steers Hunter toward staff it
holds real role data for, which the Utah run did not do. The advice to
drop the filter was right; the number attached to it was too pessimistic.

Phone number at 6% confirms the diagnosis of run 1: requiring it threw
away 94% of the available contacts.

## Decision makers

**764 contacts at 528 companies** carry a decision-maker title:

| Title | Count |
|---|---|
| Owner | 189 |
| President | 100 |
| General Manager | 54 |
| Vice President | 35 |
| Chief Executive Officer / CEO | 65 |
| Director of Operations | 30 |
| Chief Operating Officer | 23 |
| Founder / Co-Founder | 32 |

## QC

Clean. Zero duplicate emails, zero role mailboxes
(`info@`, `sales@`), zero domains that were not on the list sent.

**Nine foreign rows removed**, seven of them Orkin Brazil on
`orkinbrasil.com.br`. That domain got through the earlier TLD filter
because the pattern tested for `.br` as the final label but not `.com.br`
-- my miss, now fixed in the output.

Four companies carry a non-US country code that looks like a Hunter
mis-code rather than a real foreign business: Brunswick Pest Control (GB),
Scout Pest Control (GR), TruNorth Pest Control (GE, most likely Georgia
the US state rather than the country) and Degesch Canada (CA, genuinely
Canadian). They are left in; worth an eye before sending.

The 287 contacts filed under "Medical & Health" are pest control
technicians. Hunter's department classifier, not a list problem.

## Files

- `pest_contacts_ALL.csv` -- 2,586 contacts
- `pest_DECISION_MAKERS.csv` -- 764 contacts at 528 companies, sorted
  owner/president first
- `pest_one_per_company.csv` -- 946 rows, the most senior contact at each
  company: 519 decision makers, 319 other titled, 108 untitled

## Targeting: decision makers plus sales

The filter was set from the leads already loaded in Instantly rather than
invented. Sampling 100 leads from each of two live campaigns:

**Plumbers** -- Chief Executive Officer 17, CFO 11, Co-Owner 9, CEO 8,
CFO 8, Marketing Director 8, Owner 4, President/CEO 3, Founder 3, and a
long tail of combined owner/president titles. Sales roles: effectively
none.

**Electrical Contractors - Do You** -- President 40, Vice President 11,
Business Owner 7, Owner 6, VP of Operations 3, Company Owner 3, CFO 3,
Small Business Owner 2. Sales roles: 1 of 100.

So the established pattern is **owner, president, C-suite and VP**, with
CFO and Marketing Director both deliberately included. Sales was not part
of it, and is the addition asked for here.

### Result

**1,129 contacts at 620 companies**, from 2,586.

| Group | Contacts |
|---|---|
| Decision makers (title) | 770 |
| Sales (title) | 306 |
| Sales (Hunter department, untitled) | 33 |
| Decision makers (Hunter department, untitled) | 20 |

Top titles: Owner 188, President 100, General Manager 54, Sales Manager
50, Sales Representative 46, Account Manager 40, Vice President 35, CEO
65 across both spellings, Director of Operations 30, COO 23, Founder 20,
Account Executive 18, Marketing Director 15.

Adding sales brings **620 companies into reach rather than 528** -- 92
companies where Hunter found a salesperson but no owner.

### What was left out

1,457 contacts: 258 with no title at all, then Pest Control Technician
103, Pest Control 103, Operations Manager 61, Office Manager 61, Service
Manager 60, Customer Service Rep 46, Branch Manager 40, Technician 34.
Field and admin staff who cannot commission lead generation.

Operations Manager and Branch Manager are the judgement calls -- at a
small pest firm either could be the decision maker. They are excluded to
match the existing campaigns, which carry neither. Say the word and they
add ~100 contacts back.

### Files

- `pest_TARGETED.csv` -- 1,129 contacts, `Target group` column, sorted
  owner/president first then sales
- `pest_TARGETED_one_per_company.csv` -- 620 rows, best contact per company

## Import-ready files: company name and location

Two columns added at the front, `companyName` and `location`, so the file
can go straight into a campaign.

### companyName

Hunter's `Organization` field, cleaned so it reads naturally mid-sentence.
**49 of 1,129 changed**, the rest were already fine:

| Before | After |
|---|---|
| Patriot Pest Management - Pace, FL | Patriot Pest Management |
| Harris Pest Control, Inc. | Harris Pest Control |
| Hamtramck Pest Control LLC. | Hamtramck Pest Control |
| Rid-A-Bug Exterminating Co. Inc. | Rid-A-Bug Exterminating |
| ROADRUNNER EXTERMINATING | Roadrunner Exterminating |
| Home Inspectors Greenville, NC | Home Inspectors Greenville |

Rules: strip a trailing legal suffix (Inc, LLC, Ltd, Corp, PLLC, Co), strip
a trailing city/state or tagline after a spaced dash or pipe, and title-case
names shouted in full capitals.

Two bugs were caught and fixed before this shipped:

1. The tagline rule first allowed an unspaced hyphen, which truncated
   **A-1 Exterminators to "A"**, Nu-Tech to "Nu", Yates-Astro to "Yates"
   and Bug-A-Salt to "Bug-A". The separator now has to have spaces around
   it.
2. Title-casing turned the acronyms **MMPC into "Mmpc"** and HDMK into
   "Hdmk". Single-word capitalised names of five characters or fewer are
   now left alone, so MMPC and HDMK keep their form while MOLECAT and
   ROADRUNNER are still fixed.

Nothing is blank, and no name was shortened to something that is not a
real company name.

### location

Zero blanks across 1,129 rows. Filled in this order:

| Source | Rows |
|---|---|
| Hunter's City | 1,065 |
| Apollo's Company City, joined on domain | 58 |
| State name as the fallback | 6 |

A `location source` column records which was used for each row, so the six
state rows can be spotted and swapped for a real city later. They are
Hoffman's Exterminating (New Jersey, 4 contacts), Above & Beyond Pest
Control (Florida) and The Pest Rangers (Pennsylvania).

States are written in full -- "New Jersey", not "NJ" -- so the line reads
"...in New Jersey?" rather than "...in NJ?". No two-letter codes remain.

### Files

- `pest_IMPORT_1129.csv` -- all 1,129 targeted contacts
- `pest_IMPORT_one_per_company.csv` -- 620 rows, one per company
