# Electrical Contractors — "Do you do ___?" Campaign Plan

**Prepared for:** Izzy
**From:** Tobi
**Date:** 5 November 2026
**Status:** awaiting approval to build in Instantly

---

## 1. The idea in one paragraph

One line, one question, nothing else. We email an electrical contractor and ask
whether they do a specific high-ticket job. It does not read like a cold email,
so more of them answer. When they answer, we start the real conversation: we can
send them leads for *that exact job*, not general electrical calls.

This is the simple version you asked for on the 4 November call. Tobi is building
the longer, more detailed copy separately — this runs alongside it, not instead
of it.

---

## 2. The five jobs we are testing

Each is a real high-ticket job, in the words an electrician actually uses. Prices
are 2026 US averages, and they are here to show why these five and not others.

| | Job | What a contractor charges | Do most electricians do it? |
|---|---|---|---|
| **job1** | electrical panel upgrades | $1,500 – $6,500 | Yes — nearly all |
| **job2** | whole-home rewires | $8,000 – $30,000 | Yes — most |
| **job3** | whole-house generator installs | $7,000 – $15,000 | Common |
| **job4** | EV charger installs | $800 – $3,500 | Yes — very common |
| **job5** | 200 amp service upgrades | $1,500 – $6,500 | Yes — nearly all |

**Why these five and not the biggest-ticket jobs on earth:** the whole thing only
works if the honest answer is **yes**. A job that pays huge but almost nobody does
gets us "no, we don't do that" and the conversation is over before it starts. So
every job above is big money **and** widely offered.

**On job1 and job5:** that is the same job twice, in two different sets of words —
how a homeowner says it, and how an electrician says it. Cheapest thing we can
learn in this whole test, so it is worth one of the five slots.

---

## 3. The emails

### Day 0 — Step 1: the question

**Subject:** `do you do {{job1}}?`

> Hi {{firstName}},
>
> Do you do {{job1}}?
>
> {{sendingAccountFirstName}}

That is the entire email. No company name, no pitch, no link.

### Day 2 — Step 2: the nudge

Same thread, no subject line.

> Hi {{firstName}},
>
> Just making sure this reached you. Do you take these on?
>
> {{sendingAccountFirstName}}

One human nudge. A real person chasing a quote sends exactly one.

### Day 5 — Step 3: the reveal and the offer

Same thread, no subject line.

> {{firstName}},
>
> I should be straight with you about why I asked.
>
> I run lead generation for electrical contractors, and that is the job where our
> leads are worth the most to the contractor. We work pay per sale. No ad spend,
> no retainer, no setup fee. You pay when the job closes.
>
> We take one company per service area and we do not have anyone in {{location}}.
>
> Would you be against a 15 minute call to see what we could send you?
>
> {{sendingAccountFirstName}} from Black Swan Media

### Day 9 — Step 4: close out

Same thread, no subject line.

> {{firstName}},
>
> Should we postpone this to early next quarter? Let me know either way and I will
> stop following up.
>
> Thanks,
>
> {{sendingAccountFirstName}} from Black Swan Media

---

## 4. When someone replies "yes we do those"

This is the most important message in the campaign, and a human sends it, not the
sequence. It is the pivot you described on the call.

> {{firstName}},
>
> Good, that is what I was hoping.
>
> To be upfront: I am not looking to have one done. I run lead generation for
> electrical contractors, and we can send you leads for that specific job rather
> than general service calls.
>
> It is pay per sale, so there is no ad spend and nothing up front. We work with
> one company per service area and we do not have a partner in {{location}} yet.
>
> Does Monday or Tuesday afternoon work for 15 minutes?
>
> {{sendingAccountFirstName}} from Black Swan Media

Whoever is on the inbox needs this saved as a snippet before we turn the campaign
on, or the replies go cold while we write it.

---

## 5. How the test runs in Instantly

There are two ways to do this. **We recommend the first.**

### Option A — five variants of Step 1 (recommended)

Build Step 1 with five variants, each hardcoding one job. Instantly rotates them
evenly and, with **auto variant select set to reply rate**, promotes the winner on
its own. That setting is already switched on in our Pest Control and Electrical
campaigns, so there is nothing new to configure.

- Every lead gets the same sequence; only the job in Step 1 changes
- Reply rate per variant tells us which job pulls, directly
- No extra columns on the lead upload
- One campaign to watch instead of five

### Option B — one email with a `{{job1}}` variable per lead

Upload the leads with a custom column holding the job, and Step 1 merges it in.
This splits the list five ways instead of rotating variants.

Use this if we later want to match the job to the lead — for example sending
`generator installs` only to contractors in storm states. For a straight read on
which job pulls best, Option A is cleaner.

### One technical note

If we go the variable route, the variable has to be **`{{job1}}`**, with no space.
`{{job 1}}` will not merge — spaces break merge tags in Instantly, and the email
would go out with the raw text showing or the line blank. Small thing, but it
would ruin a send.
