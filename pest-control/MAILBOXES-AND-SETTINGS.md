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
