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
