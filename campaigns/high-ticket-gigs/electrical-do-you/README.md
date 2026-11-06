# Electrical Contractors - Do You Campaign

Draft built in Instantly on 6 Nov 2026.
Campaign id `d2423d95-e934-4ab5-b852-26aafdcdd741`, **status 0 (draft, not sending)**.

> The lead import file is deliberately **not** in this repo. It holds 1,834
> people's names, work emails and phone numbers, which belong in Drive and
> Instantly, not in git. It was delivered to Tobi directly.

## Company location, not person location

The lead list settles it. Across its 1,866 rows:

| | person columns | company columns |
|---|---|---|
| city blank | 121 (6.5%) | 31 (1.7%) |
| city differs from the other | — | **761 rows (41%)** |
| state differs from the other | — | **242 rows (13%)** |

Four in ten leads would get the wrong city, 13% the wrong state, and 121 would
get a broken first line. The offer is "one company per service area", which is
about where the company works, not where the salesperson sleeps. Company City it
is, and the campaign is built that way.

Worth seeing the failure concretely: one lead has a person city in Gauteng,
South Africa against a company city in Illinois. On person location their email
would open "…in Tembisa?".

## Settings, copied from the existing Electrical Contractors campaign

Schedule 09:00-17:00 Mon-Fri America/Detroit · email gap 9 min · random wait 5 ·
first email text only **on** · link tracking **off** · open tracking **off** ·
stop on reply **on** · match lead ESP **on** · auto variant select on reply rate.

Two things deliberately differ:

- **Inboxes.** 20 fresh ones (Julie Shannihan x10, Heather Cao x10), all warmup
  score 100 and unused by any campaign. The existing Electrical campaign runs on
  Allison's 11. Keeping them apart means a spam complaint here cannot damage the
  campaigns already running.
- **Daily limit 300**, being 20 inboxes at their configured 15/day. The old
  campaign's 165 was 11 at 15.

## Sequence, from Izzy's edited copy

Day 0, 3, 5, 9. Step 1 uses `{{location}}`, which the import populates from
Company City.

One edit was needed. Izzy's step 3 in the doc stops mid-word: *"on a performance
basis (we onl"*. It is completed here as **"(we only get paid when you close the
job)"**, which matches the pay-per-sale model used throughout. Needs his
confirmation.

## The lead list

Source: the "valid-Part-2-People-Tobi-New-Electrician-Master-List" sheet.

| | count |
|---|---|
| rows in the sheet | 1,866 |
| dropped, company country not US | 15 |
| dropped, no Company City (the first line would break) | 17 |
| **ready to import** | **1,834** |

Already email-validated upstream: every row is `status: valid` with an MX and
SMTP check, and there are no duplicate addresses. A 12-lead sample spread across
the file was searched in Instantly and none of them exist there, so this is a
genuinely new list rather than an overlap with the 1,640 already in the old
Electrical campaign.

The import file's `location` column is Company City, ready to map onto the
campaign's existing `location` custom variable.

**One lead is already in the campaign:** `mark@hawkeyeelectric.com`, added as a
single API call to confirm the field shape and that `location` lands in the
payload. It is a real row from this list. Instantly's importer dedupes on email,
so re-importing the file is safe.

## Why the file was not pushed by API

The Instantly API creates leads one at a time, so 1,834 rows would be 1,834
calls. The UI importer takes the CSV in one pass and maps the columns, which is
both faster and what the dedupe options are built for.
