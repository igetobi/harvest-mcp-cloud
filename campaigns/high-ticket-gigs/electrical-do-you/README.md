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

**One lead was already in the campaign:** a single row from this list, added by
API to confirm the field shape and that `location` lands in the
payload. It is a real row from this list. Instantly's importer dedupes on email,
so re-importing the file is safe.

## Why the file was not pushed by API

The Instantly API creates leads one at a time, so 1,834 rows would be 1,834
calls. The UI importer takes the CSV in one pass and maps the columns, which is
both faster and what the dedupe options are built for.

## Activation, then paused back

Turned on 6 Nov 2026 at 13:24 UTC, then paused 34 seconds later at 13:24:47
when the user said they wanted to switch it on themselves. Status is now 2
(paused). **Nothing sent** -- the activation fell at 08:24 EST, before the
09:00 window opened, and the campaign's sent-email list is empty.

State as built, and as it will send once switched on:

- 1,834 leads imported, every row carrying a non-blank `location`
- 20 inboxes, daily limit 300, 9 min gap, up to 5 min random wait
- Schedule 09:00-17:00 Mon-Fri America/Detroit, start date 2026-11-06
- Step delays 2 / 3 / 4 / 1 days, so sends land on day 0, 2, 5 and 9
- First email text-only, no link or open tracking, stop on reply,
  match lead ESP, auto variant select on reply rate

Pre-flight on the import file before activating:

```
rows: 1834
blank location: 0
suspicious location values: 0
longest city name: 21 -> Hillsborough Township
```

### Open items

1. Step 3 reads "(we only get paid when you close the job)". The source doc
   stops mid-word at "(we onl", so that closing is a reconstruction and still
   needs Izzy's confirmation. It first sends on day 5, so there is time.
2. `phoneNumber` imported empty on every lead even though 1,737 of the 1,834
   rows carry a number. Harmless for email, but it is the exact field a
   dialer would need. Re-import with Phone mapped to fix it.
3. Not built: the generators-only and EV-chargers-only split that Izzy asked
   about. Those would be variants 2 and 3 on step 1.
