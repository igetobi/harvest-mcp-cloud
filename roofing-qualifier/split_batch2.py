#!/usr/bin/env python3
"""Split the batch-2 verdict table into the three working lists.

A YES row's note is either a data-quality *flag* (the row describes a
different company, a different country, a parked domain, injected spam, a
shared call-centre template, a mismatched website or a missing address) or
just a record that the export carried little evidence. Flags are worth a
human look, thin data is not - that is what the confidence column is for -
so thin-data rows stay on the qualified list and only flagged rows move to
the review list.
"""
import csv
import re
import sys

FLAG = re.compile(r'UK company|Scottish company|New Zealand company|Canadian|'
                  r'is a mangled|belongs to|[Dd]escription is for|'
                  r'description places|description serves|description and phone|'
                  r'parked-domain|spam-injected|call-centre description template|'
                  r'does not match|missing from the source row|City missing|'
                  r'truncated|under construction|Description names|'
                  r'phone number \(239\)|\(831\) California|conflict')


def flagged(row):
    return row["verdict"] == "YES" and bool(FLAG.search(row["note"] or ""))


def main(verdicts, qualified, review, excluded):
    rows = list(csv.DictReader(open(verdicts)))
    fields = list(rows[0].keys())

    def write(path, sel):
        with open(path, "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=fields)
            w.writeheader()
            n = 0
            for r in rows:
                if sel(r):
                    w.writerow(r)
                    n += 1
        print(f"{path}: {n}")

    write(qualified, lambda r: r["verdict"] == "YES" and not flagged(r))
    write(review, lambda r: r["verdict"] in ("MAYBE", "UNCLEAR") or flagged(r))
    write(excluded, lambda r: r["verdict"] == "NO")


if __name__ == "__main__":
    main(*sys.argv[1:])
