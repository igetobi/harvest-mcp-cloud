# Window-services verification — worker instructions

You are one of five parallel worker sessions finishing a lead-qualification pass over 600
Dallas-area companies. Pass 1 verified 166 of them before its web-search budget ran out; you are
covering part of the remaining 434.

## Your job

1. Read `verification/CRITERIA.md` **in full**. It defines the include/exclude rules, the required
   method and the exact output record format. Follow it exactly.
2. Read your assigned workload file: `verification/todo/session_<N>.txt` (your prompt names N).
   It contains ~87 companies, each with an ID, name, website, domain, the spreadsheet tab a
   previous pass guessed for it, and a real Google review snippet.
3. Research **every** company in your file and decide YES / NO / UNCLEAR / CLOSED.
4. Write one JSON object per company, one per line, to
   `verification/results/session_<N>.jsonl`, using the exact field list in CRITERIA.md.
5. Commit and push to your own branch: `claude/verify-session-<N>`.
   Use `git push -u origin claude/verify-session-<N>`. Do not push to any other branch, and do
   not open a pull request.

## Budget — read this before you start

Your session has a hard cap of **200 WebSearch calls**, and you have ~87 companies. That is about
**2 searches per company**. Spend them deliberately:

- One well-formed search resolves most companies. Reserve a second for genuinely unclear ones.
- Do not burn searches confirming something already obvious from the first result.
- If you are running low, prioritise the companies most likely to flip a verdict (glass shops,
  roofers, exteriors/remodelers, "windows & doors" names) over obvious non-matches
  (dog grooming, car audio, pest control).
- If you do run out, mark the remainder UNCLEAR with `"searched": "none — budget exhausted"` and
  say so plainly in your final message. **Never invent evidence or infer a verdict from a company
  name.** An honest gap is worth more here than a confident guess.

## Network reality

Direct fetching is blocked in this environment: `WebFetch` returns `EGRESS_BLOCKED` and `curl`
gets `403` on CONNECT for every host, including google.com. **`WebSearch` is your only evidence
channel** — it returns real indexed page titles, URL paths and body text from company sites.
Do not waste time trying to route around the block, and do not report a company as "site down"
because of it.

## Reporting back

End with a short summary: counts of YES/NO/UNCLEAR/CLOSED, how many companies you actually
searched, how much of your search budget you used, and any company you found genuinely
ambiguous. Be explicit about anything you could not verify.
