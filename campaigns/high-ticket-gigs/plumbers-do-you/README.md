# Plumbers - Do You Campaign

Instantly campaign `3184f23c-f8d4-4978-abc5-06b21afa61fe`, created
10 Nov 2026, **status 0 (draft)**. Copy is Izzy's edit of the plumbers tab
in the shared plan doc, settings cloned from the electrical do-you campaign.

## Izzy's edits to the plumbers copy

Diffed his tab against the version we sent him on 6 Nov.

| Where | Ours | His |
|---|---|---|
| Step 1 subject | do you do sewer & water main replacements? | do you do sewer **line** & water main replacements? |
| Step 1 body | ...in `{{city}}`? | ...in `{{location}}`? |
| Step 1 note | "No greeting, no company name, no pitch, no link." | deleted |
| Step 3 | plumbers and **plumbing** contractors | plumbers and **MEP** contractors |
| Step 3 | (we only get paid when the job closes) | (we only **make money if you do**) |
| Step 3 | an additional **10-15** jobs per month | an additional **7-15** jobs per month |

Sections 1, 2 and 4, the jobs table and the whole split-test section are
untouched.

### What the step-3 edit tells us about the electrical campaign

His electrical doc truncates mid-word at "(we onl". Here he writes the same
clause out in full as **"(we only make money if you do)"**. That is very
likely the sentence the electrical one was meant to carry. The live
electrical campaign currently runs our reconstruction, "(we only get paid
when you close the job)" -- same meaning, his words are shorter. Worth
confirming with him and then matching.

### Still inconsistent in his doc

He changed `{{city}}` to `{{location}}` in step 1 only. Section 4's
reply-pivot snippet and both split-test versions in section 5 still say
`{{city}}`. Step 1 is the one that sends, so the campaign is correct, but
whoever works the replies is reading a snippet with a variable we do not
carry.

## Settings

Cloned from `d2423d95` (electrical do-you):

| | |
|---|---|
| Schedule | 09:00-17:00 Mon-Fri America/Detroit |
| Start date | 2026-11-11 |
| Step delays | 2 / 3 / 4 / 1 days -> sends land day 0, 2, 5, 9 |
| Mailboxes | 10 |
| Daily limit | 150 |
| Email gap | 9 min, up to 5 min random wait |
| First email text only | yes |
| Open tracking | off |
| Stop on reply | yes |
| Match lead ESP | yes |
| Auto variant select | reply rate |

Two deliberate differences from electrical:

1. **Daily limit is 150, not 300.** Every mailbox in the workspace is capped
   at 15/day. Electrical gets 300 because it has 20 mailboxes. This has 10,
   so 150 is the real ceiling and setting 300 would be a number that cannot
   happen.
2. **Step delays follow the live electrical campaign, not the doc.** The doc
   says day 0/3/5/9; the campaign the user edited uses day 0/2/5/9.

`link_tracking` was sent as false but is not echoed back by the API, and
there is no PATCH on this integration to force it. There is not a single
link anywhere in the four steps, so nothing can be wrapped either way --
but it is worth an eye in the UI.

## Mailboxes

Every one of the 44 mailboxes in the workspace is already attached to a
campaign, so "free" means "attached to a campaign that is not sending".

| Mailboxes | Campaign | Status | Usable |
|---|---|---|---|
| 10 Ashley (marketing.co, mediaco.com, mediamarketing.com, medias.co, tactics.com) | Plumbers (old) | 3, completed | **yes - assigned to this campaign** |
| 8 Allison (media.io, mediateam.com, outreach.com, systems.co) | Window Installation | 3, completed | contested, see below |
| 11 Allison | Electrical Contractors | 2, paused | only if that stays paused |
| 3 Ashley (leads, web, local) | Pest Control | 0, draft | yes, if Pest Control is not launching |
| 20 Julie/Heather | Electrical - Do You | 1, **active** | no |

The 10 Ashley mailboxes are the right pick: that campaign is finished, the
persona already signs as Ashley, and these addresses have real plumber
sending history rather than being cold.

The 8 Window mailboxes look free but are a subset of the 11 on the paused
Electrical Contractors campaign -- resuming it would put them back in use.

### Overlap risk

These 10 mailboxes already sent 4,626 emails to 1,246 plumbers on the old
"performance based plumber leads" copy. Any lead on the new list who was
also on the old one gets a second, very different-sounding approach from the
same address. Worth a dedupe against the old campaign before import.

## Not done

- **No lead list.** The campaign has zero leads.
- **Version B (trenchless) is not built.** Izzy's section 5 wants two step-1
  versions with the favoured one on more inboxes. Instantly rotates variants
  inside a campaign evenly, so weighting by inbox needs a second campaign,
  not a second variant.
