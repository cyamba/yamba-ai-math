# Reading and reproducing Phase 2

This is a local bounded research attempt, not a harness change. The initial
and revised author packets are separately frozen and separately reviewed.
Start with `result.md`, then read the relevant full author argument and critic
verdict. The raw external scratch in `inputs/` is untrusted historical data;
several scripts contain unguarded loops, absolute imports and refuted claims.
Do not execute those files as a reproduction shortcut.

## Dependencies and bounds

All new implementations use Python's standard library and the tracked RR003,
RR006 and RR007 implementations named in their freeze manifests. Their proof
assurance is inherited explicitly; a fresh numerical replay does not upgrade
source attribution or formal certification. The copied ignored RR007 raw
archive is separately pinned and is not a substitute for a tracked code
requirement. No dependencies were installed.

Fresh numeric checks were gated through weight12, then30, then40; tableau
checks ran through size5 before size6. High-b KR tails were reviewed as symbolic
formulas, without constructing a high-b numerical example above40. Independent
critic generators and image-recognition tests are distinguished from unchanged
author-code reproduction in the reviews.

## Commands and outputs

Every numerical command, exit status, timeout, wall time, CPU time and observed
RSS appears in the saved subprocess ledger and its canonical verbatim copy at
`verification/receipts/subprocess.jsonl`. The attempt meter is serialized
and has a fixed deadline. Once this attempt closes, do not extend its deadline,
borrow its unused units, overwrite its ledger, or describe a later run as part
of this closed attempt. A new numerical run needs its own resource record.

Some author drivers write fixed result filenames (and some refuse overwrites).
Reproduce from a disposable clean checkout or adapt only the output path in a
separately pinned reproduction script. Do not overwrite frozen JSON artifacts.
The critic checkers and exact saved command lines show the scope actually run;
read them before selecting a fresh bounded reproduction.

`checks/integrity.py` reads SHA-256 maps without importing mathematical code.
Its default mode compares every historical freeze. Historical preliminary
versions intentionally differ from the final accepted implementation; these
are explained in the journal and final result. Explicit `--manifest` arguments
select the current acceptance boundaries, while the historical failed receipt
remains available. Matching current pins establishes file integrity, not truth.

## Engineering checks

The baseline harness tests (29), partition tests (15), and verification protocol
tests (10) passed. The repository checker passed. The full legacy suite was
not run because it includes explicit KR fixtures above the current weight40
boundary. No harness behavior changed. Final repository/whitespace/integrity
results are recorded at closure. The fresh authored whitespace check passes;
verbatim external inputs and receipt transcripts retain their original whitespace. No formal proof checker was executed.
