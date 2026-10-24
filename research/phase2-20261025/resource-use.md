# Closed Phase 2 resource use

Captured 2026-10-24T22:49:54.420083+00:00. Elapsed preparation and execution to accounting:
38.17 of120 authorized minutes. The inherited30-minute charge and
the closed RR006/RR007 time/dispatch ledgers were not reused.

- 10/10 child stages;26/30 dispatch proxy units;five distinct profiles;
  at most three concurrent children. The unused four units do not authorize
  another discovery round. Same-model role separation does not imply
  independent errors. Proxy units are not money or tokens.
- 76 serialized verification subprocesses; 89.328101s wall of1200s;
  82.039958s CPU. All calls have saved commands,
  timeout, exit status, stdout and stderr in `verification/receipts/`.
- Peak observed numerical-process RSS was
  72,482,816 bytes
  (69.12MiB).
  This post-exit measurement is not a hard transient guarantee and excludes
  model/service memory. Target was512MiB per numerical child.
- Fresh artifacts at capture were 6,073,075 bytes, including both
  canonical and ignored copies of fresh receipts, below1GiB. The copied closed
  RR007 raw baseline and caches are excluded; small final manifest/accounting
  writes follow this measurement.

Failed charged subprocesses: kr-critic-geometry30 (exit 1), closure-repository-check (exit 1). The geometry failure exposed the
false quotient terminal<=1 claim. The first closure repository check ran
before the resource file existed and flagged its missing local link. Its
corrected rerun is retained; no failed command was discarded. Candidate
collisions, bad formulas and historical pin qualifications are additional
research findings, not necessarily nonzero process exits.

The29 harness,15 partition and10 verification-protocol tests passed. Final
repository and current acceptance-pin checks passed as recorded at closure.
The full legacy suite was not run because it constructs KR fixtures above40;
no harness behavior changed. Initial census gates were12,30,40 and tableau
through5 then6. The recursive author's correction call labeled12 additionally
replayed its fixed C18 witness after40 was exposed; the critic's final pilot
is strict12. No object exceeded the overall40/six bounds. High-b/high-gap
claims received symbolic review without above40 instances.

Model/service compute, tokens and monetary cost are unmeasured. There was no
new paid provider, dependency, web retrieval, publication, push or external
message. No formal proof checker ran; novelty remains unverified.

See `resource-use.json` for exact values and the archived/raw ledger SHA-256.
Old closed ledgers and immutable input pins are checked separately. This is
the final accounting for this attempt; do not append new runs to it.

Administrative finalization captured 2026-10-24T22:50:47.354901+00:00, 39.06 elapsed minutes from the fresh start. No numerical calls occurred after
the accounting snapshot; the following local Git commit records this packet.
