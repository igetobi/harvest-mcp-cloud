# "Do you do ___?" campaigns — plumbers, HVAC, electricians

Copy for the simple-first-email test Izzy asked for on the 4 Nov call. Three
niches, five step-1 variants each, then one shared follow-up sequence per niche.

What the call asked for, and what this does with it:

- **"business owner first name, do you do blank question mark"** — step 1 is that
  and nothing else. One line.
- **"blank is going to be one of the most high ticket services that niche does"** —
  the five variants per niche are the ranked list in `high_ticket_gigs.csv`.
- **"three or four jobs that are high ticket... so we could do like a variation... heavy test"** (Tobi) — five variants, same body, only the service changes, so the
  reply-rate difference is the service name and nothing else.
- **"if they respond, then we start the conversation of, we want to send you more
  sewer line leads, specific to a service, not just plumbing leads in general"** —
  that is the reply handler at the bottom. It is the most important piece of copy
  here and the one a human sends, not the sequence.

## Two deliberate choices, flag them before this goes live

**1. Step 1 is signed with a first name only — no company, no title, no link.**
Izzy's brief was that it must not read like a cold email, and "from Black Swan
Media" under a one-line question is what gives it away. The company name appears
on step 3 and on the reply. If you'd rather not run it that way, V5 in each niche
is identical copy signed the normal way, so the test tells you what the anonymity
is actually worth.

**2. Izzy called it "a little bit of a bait and switch" — it is, and that is a
real cost, not just a tactic.** An owner who answers thinking a customer wants a
sewer line replaced and gets a lead-gen pitch may be annoyed enough to mark it
as spam, and those complaints land on inboxes you are also using for the other
campaigns. Worth watching the spam rate on these sends specifically, separately
from reply rate. The step-3 reveal opens by admitting why the first email was
asked, which is the cheapest way to take the sting out of it.

---

# PLUMBERS

## Step 1 — the question (A/B, 5 variants, no pre-delay)

**V1** · subject: `do you do sewer line replacements?`
```
Hi {{firstName}},

Do you do sewer line replacements?

{{sendingAccountFirstName}}
```

**V2** · subject: `do you do whole-home repipes?`
```
Hi {{firstName}},

Do you do whole-home repipes?

{{sendingAccountFirstName}}
```

**V3** · subject: `do you do water main replacements?`
```
Hi {{firstName}},

Do you do water main replacements?

{{sendingAccountFirstName}}
```

**V4** · subject: `do you do tankless water heater installs?`
```
Hi {{firstName}},

Do you do tankless water heater installs?

{{sendingAccountFirstName}}
```

**V5** · subject: `do you do sewer line replacements?` — control for the signature
```
Hi {{firstName}},

Do you do sewer line replacements?

{{sendingAccountFirstName}} from Black Swan Media
```

## Step 2 — bump (+3 days, same thread, no subject)
```
Hi {{firstName}},

Just making sure this reached you. Do you take these on?

{{sendingAccountFirstName}}
```

## Step 3 — the reveal and the offer (+4 days, same thread, no subject)
```
{{firstName}},

I should be straight with you about why I asked.

I run lead generation for plumbing companies, and that is the job where our
leads are worth the most to the contractor. We work pay per sale. No ad spend,
no retainer, no setup fee. You pay when the job closes.

We take one company per service area and we do not have anyone in {{location}}.

Would you be against a 15 minute call to see what we could send you?

{{sendingAccountFirstName}} from Black Swan Media
```

## Step 4 — close out (+1 day, same thread, no subject)
```
{{firstName}},

Should we postpone this to early next quarter? Let me know either way and I
will stop following up.

Thanks,

{{sendingAccountFirstName}} from Black Swan Media
```

## Reply handler — they say yes, they do that work
```
{{firstName}},

Good, that is what I was hoping.

To be upfront: I am not looking to have one done. I run lead generation for
plumbing companies, and we can send you leads for that specific job rather than
general plumbing calls.

It is pay per sale, so there is no ad spend and nothing up front. We work with
one company per service area and we do not have a partner in {{location}} yet.

Does Monday or Tuesday afternoon work for 15 minutes?

{{sendingAccountFirstName}} from Black Swan Media
```

---

# HVAC

## Step 1 — the question (A/B, 5 variants, no pre-delay)

**V1** · subject: `do you do full system replacements?`
```
Hi {{firstName}},

Do you do full system replacements?

{{sendingAccountFirstName}}
```

**V2** · subject: `do you do AC replacements?`
```
Hi {{firstName}},

Do you do AC replacements?

{{sendingAccountFirstName}}
```

**V3** · subject: `do you do heat pump installs?`
```
Hi {{firstName}},

Do you do heat pump installs?

{{sendingAccountFirstName}}
```

**V4** · subject: `do you do new ductwork?`
```
Hi {{firstName}},

Do you do new ductwork?

{{sendingAccountFirstName}}
```

**V5** · subject: `do you do mini split installs?`
```
Hi {{firstName}},

Do you do mini split installs?

{{sendingAccountFirstName}}
```

## Step 2 — bump (+3 days)
```
Hi {{firstName}},

Just making sure this reached you. Do you take these on?

{{sendingAccountFirstName}}
```

## Step 3 — the reveal and the offer (+4 days)
```
{{firstName}},

I should be straight with you about why I asked.

I run lead generation for HVAC companies, and that is the job where our leads
are worth the most to the contractor. We work pay per sale. No ad spend, no
retainer, no setup fee. You pay when the job closes.

We take one company per service area and we do not have anyone in {{location}}.

Would you be against a 15 minute call to see what we could send you?

{{sendingAccountFirstName}} from Black Swan Media
```

## Step 4 — close out (+1 day)
```
{{firstName}},

Should we postpone this to early next quarter? Let me know either way and I
will stop following up.

Thanks,

{{sendingAccountFirstName}} from Black Swan Media
```

## Reply handler — they say yes
```
{{firstName}},

Good, that is what I was hoping.

To be upfront: I am not looking to have one installed. I run lead generation
for HVAC companies, and we can send you leads for that specific job rather
than general service calls.

It is pay per sale, so there is no ad spend and nothing up front. We work with
one company per service area and we do not have a partner in {{location}} yet.

Does Monday or Tuesday afternoon work for 15 minutes?

{{sendingAccountFirstName}} from Black Swan Media
```

---

# ELECTRICIANS

## Step 1 — the question (A/B, 5 variants, no pre-delay)

**V1** · subject: `do you do electrical panel upgrades?`
```
Hi {{firstName}},

Do you do electrical panel upgrades?

{{sendingAccountFirstName}}
```

**V2** · subject: `do you do whole-home rewires?`
```
Hi {{firstName}},

Do you do whole-home rewires?

{{sendingAccountFirstName}}
```

**V3** · subject: `do you do whole-house generator installs?`
```
Hi {{firstName}},

Do you do whole-house generator installs?

{{sendingAccountFirstName}}
```

**V4** · subject: `do you do EV charger installs?`
```
Hi {{firstName}},

Do you do EV charger installs?

{{sendingAccountFirstName}}
```

**V5** · subject: `do you do 200 amp service upgrades?`
```
Hi {{firstName}},

Do you do 200 amp service upgrades?

{{sendingAccountFirstName}}
```

## Step 2 — bump (+3 days)
```
Hi {{firstName}},

Just making sure this reached you. Do you take these on?

{{sendingAccountFirstName}}
```

## Step 3 — the reveal and the offer (+4 days)
```
{{firstName}},

I should be straight with you about why I asked.

I run lead generation for electrical contractors, and that is the job where our
leads are worth the most to the contractor. We work pay per sale. No ad spend,
no retainer, no setup fee. You pay when the job closes.

We take one company per service area and we do not have anyone in {{location}}.

Would you be against a 15 minute call to see what we could send you?

{{sendingAccountFirstName}} from Black Swan Media
```

## Step 4 — close out (+1 day)
```
{{firstName}},

Should we postpone this to early next quarter? Let me know either way and I
will stop following up.

Thanks,

{{sendingAccountFirstName}} from Black Swan Media
```

## Reply handler — they say yes
```
{{firstName}},

Good, that is what I was hoping.

To be upfront: I am not looking to have one done. I run lead generation for
electrical contractors, and we can send you leads for that specific job rather
than general service calls.

It is pay per sale, so there is no ad spend and nothing up front. We work with
one company per service area and we do not have a partner in {{location}} yet.

Does Monday or Tuesday afternoon work for 15 minutes?

{{sendingAccountFirstName}} from Black Swan Media
```

---

## Settings to match the existing campaigns

Copy these from Electrical Contractors (the newest build):

- first email text only: **on** — matters more here than anywhere, a one-line
  HTML email with tracking pixels is the easiest thing in the world to filter
- link tracking: **off**, open tracking: **off** — already your default, and
  there is no link in step 1 to track anyway
- stop on reply: **on**
- email gap 9 minutes, random wait 5
- `{{sendingAccountFirstName}}` rather than a hardcoded name, so the signature
  matches whichever inbox sent it

## Variables used

`{{firstName}}`, `{{sendingAccountFirstName}}`, `{{location}}`.

`{{location}}` appears in step 3 and in the reply handler. It is already a
custom variable on the Plumbers and Electrical campaigns. Check it is populated
before sending — on the window campaign some leads carry `Utah` and others
`Salt Lake City`, and "we do not have anyone in Utah" reads differently from
"we do not have anyone in Salt Lake City". If a lead has no location, the line
breaks, so either fill it or cut that sentence.

## Reading the test

The only thing that changes between variants is the service name, so reply rate
ranks the services directly. Two things to watch beyond that:

- **Positive vs any reply.** "No we don't do those" is a reply and Instantly
  counts it. Judge the variants on replies that say yes.
- **Spam complaints per variant.** If one service name reads more like a sales
  email than a customer question, it will show up here before it shows up in
  reply rate.
