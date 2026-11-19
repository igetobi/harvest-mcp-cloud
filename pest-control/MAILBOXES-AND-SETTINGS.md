# Pest Control: mailboxes available, and settings vs the electrical campaign

Checked 18 Nov 2026.

## Mailboxes: only 2 are genuinely free

All 44 accounts are healthy — **both `blackswanlocal.com` accounts were
reconnected today** and are back to status 1 with their warmup scores
intact, so the dead-account problem from 10 Nov is resolved.

| | Mailboxes |
|---|---|
| On an **active** campaign (Electrical Do-You) | 20 |
| On a **paused** campaign only | 22 |
| On **no campaign at all** | **2** |

The two free ones are `allison@blackswanlocal.com` and
`ashley@blackswanlocal.com` — the pair that was broken and has just come
back. That is **30 emails a day**, which against 1,129 leads is about
nine weeks for step 1 alone.

Nothing else is idle. There is no "completed campaign only" pool: every
mailbox on the finished Plumbers and Window campaigns is also attached to
a paused one.

| Campaign | Status | Mailboxes |
|---|---|---|
| Electrical Contractors - Do You | **active** | 20 Julie/Heather |
| Plumbers - Do You | paused | 14 Ashley + 2 Allison |
| Electrical Contractors | paused | 10 Allison |
| Plumbers (old) | completed | 10 Ashley, all also on Plumbers Do-You |
| Window Installation | completed | 8 Allison, all also on Electrical Contractors |
| **Pest Control** | draft | **0** |

### The real options

1. **The 2 free ones only** — 30/day. Safe but slow.
2. **Take the 10 Allison from Electrical Contractors** — it is paused with
   roughly 1,016 leads mid-sequence and has not sent since 2 Nov. With the
   2 free that is 12 mailboxes, **180/day**, about seven working days to
   clear step 1. The cost: if that campaign is ever resumed, its
   mid-sequence leads get follow-ups from a different sender.
3. **Take the 14 from Plumbers - Do You** — paused after only 210 sends of
   1,634 leads, so it is much more likely to be resumed than Electrical
   Contractors. Not recommended.
4. **Buy more mailboxes.** 1,129 leads at a sensible pace wants 20+.

## Settings: Pest Control vs Electrical Do-You

Identical on everything that matters for deliverability: 09:00-17:00 Mon-Fri
America/Detroit, step delays 2/3/4/1, 9 minute gap, 5 minute random wait,
first email text-only, link and open tracking off, stop on reply, match
lead ESP, auto variant select on reply rate, no unsubscribe header, risky
contacts off, bounce protection on.

Four real differences:

| | Pest Control | Electrical Do-You |
|---|---|---|
| **Start date** | **2026-10-19** (a month ago) | 2026-11-06 |
| **Daily limit** | **50** | 300 |
| **Mailboxes** | **none** | 20 |
| Step 1 variants | 2 | 1 |

**Start date is the one to fix.** It is set a month in the past, from when
the campaign was first drafted. Set it to the day you intend to launch.

**Daily limit of 50** does not match any mailbox count you might assign:
12 mailboxes is 180, 2 is 30. Set it to the count times 15.

**Two step-1 variants is a difference, not a defect** — the pest copy
A/B tests two openers with auto variant select on reply rate, which the
electrical campaign does not. Worth keeping.

### Not real differences

The electrical campaign lists `phone` and `personalization` under core
variables and `pause_until` under custom variables where pest control does
not. These are not settings — Instantly adds them from whatever columns
the leads carried, and `pause_until` is internal. Nothing to change.

### Worth noting

Pest control already has `website` under core variables, confirming the
re-import registered it, and `location` and `phoneNumber` under custom
variables. `phoneNumber` is empty on every lead, since Hunter only
returned a phone for 6% of contacts and the import file carried no phone
column.

## Decision: 12 mailboxes

Tobi's call, 19 Nov: the 10 Allison accounts from the paused Electrical
Contractors campaign plus the 2 free `blackswanlocal.com` accounts.
**180/day**, roughly seven working days to clear step 1 on 1,129 leads.

```
allison@blackswanleads.com
allison@blackswanweb.com
allison@blackswanmedia.io
allison.moore@blackswanmedia.io
allison@blackswansystems.co
allison.moore@blackswansystems.co
allison@blackswanoutreach.com
allison.moore@blackswanoutreach.com
allison@blackswanmediateam.com
allison.moore@blackswanmediateam.com
allison@blackswanlocal.com
ashley@blackswanlocal.com
```

**Has to be done in the UI.** Setting `email_list` on an existing campaign
is `PATCH /api/v2/campaigns/{id}`, which this integration does not expose;
`POST /campaigns/{id}` and `POST /campaigns/{id}/accounts` both return 404.
Rebuilding the campaign would carry the mailboxes at creation but would
also discard the 1,129 leads already imported, so pasting the list is both
quicker and safer.

Set at the same time, on the same screen:

| Field | To |
|---|---|
| Daily limit | **180** (12 x 15) |
| Start date | **the launch day** — currently 2026-10-19, a month past |

### Two of the twelve are shared with a second paused campaign

`allison@blackswanleads.com` and `allison@blackswanweb.com` sit on
**Plumbers - Do You** as well as Electrical Contractors. Harmless while
both stay paused, but if Plumbers - Do You is resumed those two split
their 15/day between the campaigns and pest control's real ceiling drops
to about 165.

### Electrical Contractors is not changed

The 10 Allison accounts stay attached to it. Nothing needs removing while
it is paused, and stripping them would break sender continuity for its
~1,016 mid-sequence leads if it is ever resumed. The only thing to avoid
is resuming Electrical Contractors while pest control is running, which
would have both campaigns drawing on the same ten mailboxes.

## Live

Activated 19 Nov 2026, 12:43 UTC. Final state:

| | |
|---|---|
| Status | 1, active |
| Mailboxes | 12 |
| Daily limit | 180 |
| Start date | 2026-11-19 |
| Schedule | 09:00-17:00 Mon-Fri America/Detroit |
| Step delays | 2 / 3 / 4 / 1 -> sends land day 0, 2, 5, 9 |
| Leads | 1,129, zero blank `location` or `companyName`, `website` on every row |
| Step 1 | two variants, auto variant select on reply rate |

Nothing had sent at the time of the check: activation fell at 07:43 EST,
before the 09:00 window opens.

### Watch list

1. **Day 2 new-lead count.** The daily limit is shared across all four
   steps. On the electrical campaign day 1 was 300 new leads and day 2 was
   300 sends but only **14** new. Expect the same shape here: ~180 on day
   one, then roughly 45 new a day once follow-ups are in flight, so about
   five weeks for step 1 rather than seven days.
2. **Do not resume Electrical Contractors or Plumbers - Do You** while
   this runs. All ten Allison accounts are still attached to Electrical
   Contractors, and `allison@blackswanleads.com` and
   `allison@blackswanweb.com` are also on Plumbers - Do You. Resuming
   either splits the same mailboxes two ways.
3. **509 of the 1,129 are second or third contacts at a company already
   being emailed.** `stop_for_company` is false, so a reply from one does
   not stop the others. Worth turning on, or pruning to the 620
   one-per-company set.
