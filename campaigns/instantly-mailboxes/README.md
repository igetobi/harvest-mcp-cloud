# Instantly mailbox rosters

Sending accounts per campaign, kept here because the API integration
available to this session is GET/POST only. Campaign updates are
`PATCH /api/v2/campaigns/{id}`, so a mailbox list cleared in the UI cannot
be restored from here -- only read back and re-entered by hand.

## electrical-contractors-mailboxes.txt

The 11 sending accounts on campaign `867022d5-f8cd-4670-b3b4-c7b6cf23b932`
("Electrical Contractors", paused), captured 10 Nov 2026 at 13:05 UTC from
a campaign listing, half an hour before the list was cleared in the UI at
13:35:37.

These are every Allison account in the workspace. Three of them
(leads / web / local) are now also on the plumbers do-you draft; the other
eight are also on the Window Installation campaign. A mailbox can sit on
several campaigns at once, so re-adding all 11 here conflicts with nothing
while this campaign stays paused.

Nothing else on the campaign was touched: 1,640 leads, 1,140 contacted and
its reply history are all intact. Only the sending accounts were cleared,
and a paused campaign with no sending accounts sends nothing either way.
