#!/usr/bin/env python3
"""Render the electrical plan as HTML for Drive to convert into a Google Doc.

Drive converts h1/h2/h3, p, ul/ol, b, i, a and tables into native Docs
formatting, so headings become real heading styles and show up in the outline.
Merge tags are left as plain text so they survive the conversion untouched.
"""
import html, sys

def esc(t):
    return html.escape(t, quote=False)

def email(subject, lines):
    out = []
    if subject:
        out.append(f"<p><b>Subject:</b> {esc(subject)}</p>")
    body = "<br>".join(esc(l) if l else "" for l in lines)
    out.append(f"<blockquote><p>{body}</p></blockquote>")
    return "\n".join(out)

JOBS = [
    ("job1", "electrical panel upgrades", "$1,500 to $6,500", "Yes, nearly all"),
    ("job2", "whole-home rewires", "$8,000 to $30,000", "Yes, most"),
    ("job3", "whole-house generator installs", "$7,000 to $15,000", "Common"),
    ("job4", "EV charger installs", "$800 to $3,500", "Yes, very common"),
    ("job5", "200 amp service upgrades", "$1,500 to $6,500", "Yes, nearly all"),
]

rows = "\n".join(
    f"<tr><td><b>{v}</b></td><td>{esc(j)}</td><td>{esc(p)}</td><td>{esc(w)}</td></tr>"
    for v, j, p, w in JOBS)

H = f"""<!DOCTYPE html>
<html><head><meta charset="utf-8"><title>Electrical Contractors Campaign Plan</title></head>
<body>

<h1>Electrical Contractors: "Do you do ___?" Campaign Plan</h1>

<p><b>Prepared for:</b> Izzy<br>
<b>From:</b> Tobi<br>
<b>Date:</b> 5 November 2026<br>
<b>Status:</b> awaiting approval to build in Instantly</p>

<h2>1. The idea in one paragraph</h2>

<p>One line, one question, nothing else. We email an electrical contractor and ask
whether they do a specific high-ticket job. It does not read like a cold email, so
more of them answer. When they answer, we start the real conversation: we can send
them leads for that exact job, not general electrical calls.</p>

<p>This is the simple version you asked for on the 4 November call. Tobi is building
the longer, more detailed copy separately, so this runs alongside it rather than
instead of it.</p>

<h2>2. The five jobs we are testing</h2>

<p>Each is a real high-ticket job, in the words an electrician actually uses. Prices
are 2026 US averages, and they are here to show why these five and not others.</p>

<table border="1" cellpadding="6" cellspacing="0">
<tr><td><b>Variable</b></td><td><b>Job</b></td><td><b>What a contractor charges</b></td><td><b>Do most electricians do it?</b></td></tr>
{rows}
</table>

<p><b>Why these five and not the biggest-ticket jobs on earth:</b> the whole thing
only works if the honest answer is yes. A job that pays huge but almost nobody does
gets us "no, we don't do that", and the conversation is over before it starts. So
every job above is big money and widely offered.</p>

<p><b>On job1 and job5:</b> that is the same job twice, in two different sets of
words. How a homeowner says it, and how an electrician says it. It is the cheapest
thing we can learn in this whole test, so it is worth one of the five slots.</p>

<h2>3. The emails</h2>

<h3>Day 0, Step 1: the question</h3>
{email("do you do {{job1}}?", ["Hi {{firstName}},", "", "Do you do {{job1}}?", "", "{{sendingAccountFirstName}}"])}
<p>That is the entire email. No company name, no pitch, no link.</p>

<h3>Day 2, Step 2: the nudge</h3>
<p>Same thread, no subject line.</p>
{email(None, ["Hi {{firstName}},", "", "Just making sure this reached you. Do you take these on?", "", "{{sendingAccountFirstName}}"])}
<p>One human nudge. A real person chasing a quote sends exactly one.</p>

<h3>Day 5, Step 3: the reveal and the offer</h3>
<p>Same thread, no subject line.</p>
{email(None, ["{{firstName}},", "",
 "I should be straight with you about why I asked.", "",
 "I run lead generation for electrical contractors, and that is the job where our leads are worth the most to the contractor. We work pay per sale. No ad spend, no retainer, no setup fee. You pay when the job closes.", "",
 "We take one company per service area and we do not have anyone in {{location}}.", "",
 "Would you be against a 15 minute call to see what we could send you?", "",
 "{{sendingAccountFirstName}} from Black Swan Media"])}

<h3>Day 9, Step 4: close out</h3>
<p>Same thread, no subject line.</p>
{email(None, ["{{firstName}},", "",
 "Should we postpone this to early next quarter? Let me know either way and I will stop following up.", "",
 "Thanks,", "",
 "{{sendingAccountFirstName}} from Black Swan Media"])}

<h2>4. When someone replies "yes we do those"</h2>

<p>This is the most important message in the campaign, and a human sends it, not the
sequence. It is the pivot you described on the call.</p>

{email(None, ["{{firstName}},", "",
 "Good, that is what I was hoping.", "",
 "To be upfront: I am not looking to have one done. I run lead generation for electrical contractors, and we can send you leads for that specific job rather than general service calls.", "",
 "It is pay per sale, so there is no ad spend and nothing up front. We work with one company per service area and we do not have a partner in {{location}} yet.", "",
 "Does Monday or Tuesday afternoon work for 15 minutes?", "",
 "{{sendingAccountFirstName}} from Black Swan Media"])}

<p>Whoever is on the inbox needs this saved as a snippet before we turn the campaign
on, or the replies go cold while we write it.</p>

<h2>5. How the test runs in Instantly</h2>

<p>There are two ways to do this. We recommend the first.</p>

<h3>Option A: five variants of Step 1 (recommended)</h3>

<p>Build Step 1 with five variants, each hardcoding one job. Instantly rotates them
evenly and, with auto variant select set to reply rate, promotes the winner on its
own. That setting is already switched on in our Pest Control and Electrical
campaigns, so there is nothing new to configure.</p>

<ul>
<li>Every lead gets the same sequence, and only the job in Step 1 changes</li>
<li>Reply rate per variant tells us which job pulls, directly</li>
<li>No extra columns on the lead upload</li>
<li>One campaign to watch instead of five</li>
</ul>

<h3>Option B: one email with a job variable per lead</h3>

<p>Upload the leads with a custom column holding the job, and Step 1 merges it in.
This splits the list five ways instead of rotating variants.</p>

<p>Use this if we later want to match the job to the lead, for example sending
generator installs only to contractors in storm states. For a straight read on which
job pulls best, Option A is cleaner.</p>

<h3>One technical note</h3>

<p>If we go the variable route, the variable has to be <b>{{{{job1}}}}</b>, with no
space. <b>{{{{job 1}}}}</b> will not merge, because a space breaks the merge tag in
Instantly, and the email would go out with the raw text showing or the line blank.
Small thing, but it would ruin a send.</p>

</body></html>
"""
open(sys.argv[1], "w").write(H)
print(f"{sys.argv[1]}: {len(H)} chars")
