#!/usr/bin/env python3
"""Render the plumbers plan as HTML for Drive to convert into a Google Doc.

Mirrors the structure of Izzy's edited electrical doc: a paired question in
step 1 with {{city}}, no greeting on the first email, the "right person" nudge
on day 3, and the performance-basis pitch on day 5.
"""
import html, sys

def esc(t): return html.escape(t, quote=False)

def email(subject, lines):
    out = []
    if subject:
        out.append(f"<p><b>Subject:</b> {esc(subject)}</p>")
    out.append("<blockquote><p>" + "<br>".join(esc(l) if l else "" for l in lines) + "</p></blockquote>")
    return "\n".join(out)

JOBS = [
    ("job1", "sewer line replacements", "$4,000 to $15,000",
     "Yes, lead question"),
    ("job2", "water main replacements", "$1,600 to $5,000",
     "Yes, pairs with job1"),
    ("job3", "trenchless sewer line replacements", "top half of the sewer range",
     "Yes, the sharpest filter"),
    ("job4", "whole-home repipes", "$4,000 to $20,000",
     "Reference only"),
    ("job5", "tankless water heater installs", "$3,000 to $12,500",
     "No, every plumber does these"),
]
rows = "\n".join(
    f"<tr><td><b>{v}</b></td><td>{esc(j)}</td><td>{esc(p)}</td><td>{esc(w)}</td></tr>"
    for v, j, p, w in JOBS)

H = f"""<!DOCTYPE html>
<html><head><meta charset="utf-8"><title>Plumbers Campaign Plan</title></head>
<body>

<h1>Plumbers: "Do you do ___?" Campaign Plan</h1>

<p><b>Prepared for:</b> Izzy<br>
<b>From:</b> Tobi<br>
<b>Date:</b> 6 November 2026<br>
<b>Status:</b> awaiting approval to build in Instantly</p>

<p><b>Note:</b> this follows the edits you made to the electrical doc. Same email
structure, same day spacing, two paired jobs in the first question rather than one,
and {{{{city}}}} in the opening line.</p>

<h2>1. The idea in one paragraph</h2>

<p>One line, one question, nothing else. We email a plumbing contractor and ask
whether they do a specific high-ticket job in their city. It does not read like a
cold email, so more of them answer. When they answer, we start the real
conversation: we can send them leads for that exact job, not general plumbing
calls.</p>

<h2>2. The jobs, and which ones are worth split testing</h2>

<p>Your note on whole house wiring applies cleanly to plumbing. Some jobs every
plumber does, so asking tells us nothing. The table separates the two.</p>

<table border="1" cellpadding="6" cellspacing="0">
<tr><td><b>Variable</b></td><td><b>Job</b></td><td><b>What a contractor charges</b></td><td><b>In the split test?</b></td></tr>
{rows}
</table>

<p><b>job4 and job5 are in the table for reference, not for the test.</b> Nearly
every plumber repipes a house and installs tankless heaters, so the answer is
always yes and we learn nothing. That is the same reason you pulled whole house
wiring out of the electrical set.</p>

<p><b>job1 and job2 are the pair.</b> Sewer lines and water mains are both
underground excavation work. A plumber who does one does the other, so they belong
in a single question, the way EV chargers and generators do for electricians.</p>

<p><b>job3 is the sharpest filter we have.</b> Trenchless needs equipment most
plumbers do not own, so a yes tells us we are talking to a serious operator with
the highest-value jobs on the truck. It is the obvious thing to split test the pair
against.</p>

<h2>3. The emails</h2>

<h3>Day 0, Step 1: the question</h3>
{email("do you do sewer & water main replacements?",
       ["Do you do sewer line & water main replacements in {{city}}?", "",
        "{{sendingAccountFirstName}}"])}
<p>No greeting, no company name, no pitch, no link. Same as your electrical edit.</p>

<h3>Day 3, Step 2: the nudge</h3>
{email(None, ["Hi {{firstName}},", "",
 "Not sure if I am contacting the right person. Let me know. Thank you!", "",
 "{{sendingAccountFirstName}}"])}

<h3>Day 5, Step 3: the reveal and the offer</h3>
<p>Same thread, no subject line.</p>
{email(None, ["{{firstName}},", "",
 "We specialize in generating high-ticket appointments for plumbers and plumbing contractors on a performance basis (we only get paid when the job closes).", "",
 "If you are able to take on an additional 10-15 jobs per month, would you be against a 10 minute conversation to see if we would be a good fit?", "",
 "{{sendingAccountFirstName}} from Black Swan Media"])}

<h3>Day 9, Step 4: close out</h3>
<p>Same thread, no subject line.</p>
{email(None, ["{{firstName}},", "",
 "Please let me know your thoughts on my previous message or if I should reach back next quarter?", "",
 "Thanks,", "",
 "{{sendingAccountFirstName}} from Black Swan Media"])}

<h2>4. When someone replies "yes we do those"</h2>

<p>A human sends this, not the sequence. It is the pivot from the call.</p>

{email(None, ["{{firstName}},", "",
 "Good, that is what I was hoping.", "",
 "To be upfront: I am not looking to have one done. I run lead generation for plumbing contractors, and we can send you leads for that specific job rather than general plumbing calls.", "",
 "It is pay per sale, so there is no ad spend and nothing up front. We work with one company per service area and we do not have a partner in {{city}} yet.", "",
 "Does Monday or Tuesday afternoon work for 15 minutes?", "",
 "{{sendingAccountFirstName}} from Black Swan Media"])}

<p>Whoever is on the inbox needs this saved as a snippet before we turn the campaign
on, or the replies go cold while we write it.</p>

<h2>5. How the split test runs</h2>

<p>Two versions of Step 1, everything after it identical, so any difference in
replies is the question itself.</p>

<ul>
<li><b>Version A, the pair (more inboxes):</b> "Do you do sewer line &amp; water main
replacements in {{{{city}}}}?"</li>
<li><b>Version B, the filter (fewer inboxes):</b> "Do you do trenchless sewer line
replacements in {{{{city}}}}?"</li>
</ul>

<p>As you asked on the electrical campaign, the version you favour carries the
larger share of the inboxes and the challenger runs on fewer. Steps 2, 3 and 4 do
not change between versions.</p>

<h3>One thing to set up before we send</h3>

<p>{{{{city}}}} is new. Our Instantly campaigns currently carry {{{{location}}}}, not
{{{{city}}}}, so the column has to be added on the upload or the first line of every
email goes out broken. The Apollo export already has a City column, so it is a
mapping job rather than new research.</p>

<p>The variable also has to be spelled {{{{city}}}} with no space. A space breaks the
merge tag in Instantly and the email sends with the raw text showing.</p>

</body></html>
"""
open(sys.argv[1], "w").write(H)
print(f"{sys.argv[1]}: {len(H)} chars")
