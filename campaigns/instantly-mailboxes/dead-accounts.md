# Dead sending accounts, 10 Nov 2026

Two accounts, not one. Both on the **blackswanlocal.com** domain, both with
`status: -1` and `autofix_failed: true` in the accounts API:

| Account | status | Error |
|---|---|---|
| `allison@blackswanlocal.com` | -1 | `EAUTH` on `AUTH XOAUTH2` -- "can't create new access token for user" |
| `ashley@blackswanlocal.com` | -1 | same failure state, autofix failed |

Every other one of the 44 accounts in the workspace is `status: 1`.

Two addresses on one domain failing the same OAuth refresh is a
domain-level connection failure, not two coincidental mailbox problems.
Instantly's own autofix has already tried and given up, so reconnecting is
a manual job.

The UI says these were "removed from the workspace". The API still lists
them, with their warmup history and a score of 100. They are disconnected,
not deleted -- so reconnecting the OAuth should bring them back with their
warmup intact rather than starting from cold.

## What this hits

| Campaign | Dead accounts on it |
|---|---|
| Electrical Contractors (`867022d5`, paused) | `allison@blackswanlocal.com` -- being removed by hand |
| Plumbers - Do You (`3c29a2f8`, draft) | **both** |

The plumbers draft was built with 16 mailboxes at a 240/day limit. Two of
them cannot send, so the real ceiling is **14 x 15 = 210/day**.

Nothing is broken right now: the campaign is a draft with zero leads and is
not sending. The choice is to reconnect blackswanlocal.com before launch
and keep 16, or drop both and rebuild at 14 / 210.
