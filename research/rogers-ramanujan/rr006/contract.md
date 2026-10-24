# RR006 proposed resource contract — 24 October 2026

**PROPOSED; NOT ACCEPTED FOR EXECUTION. Research remains stopped.** The current
request authorizes local planning documents and integrity/assignment checks
only. Christopher must renew the research instruction before any branch,
OEIS/web search, enumeration or construction trial starts. This contract does
not reuse RR003/RR004/RR005 time, computation ledgers or review allowances.

## Scope and inputs

Outcome: a reviewed family census, a bounded sequence/source cross-search,
one lossless geometric representation study, distinct/repeated-part analysis,
and at most three ranked construction directions. Follow [plan.md](plan.md).
The ultimate KR1 objective and proof obligations are unchanged; psi on all
residual roots remains missing. Novelty is NOT VERIFIED. Scope success does
not mean full KR1 success.

Verified worktree: `/private/tmp/yamba-ai-math-rr006`, branch
`codex/kr1-rr006-family-search`, clean before this preparation. Preparation
HEAD: `03d46d9db79cbdc2f77159defa5fc0bafcc8f5fd`; RR005 base: `692c65d`.
Do not switch or change another checkout. Preserve the historical handoff,
`preparation-status.json`, all old freezes, failures, ledgers and assurance.
At execution start pin the actual HEAD, dirty diff and hashes of this contract,
plan, role cards, fleet input and all mathematical dependencies; record any
accepted user amendments. A changed contract needs explicit authorization.

## Proposed time and resource envelope

These are fresh proposed ceilings, not an active allowance. Charge this
documentation/planning preparation a conservative **30 minutes**, separately
from future execution. Waiting for Christopher does not run a research clock.
If accepted unchanged, allow **120 further elapsed minutes** from recorded
execution start, for a total charged ceiling of **150 minutes**. Record actual
timestamps and distinguish the conservative planning charge from measured time.

| Future execution phase | Elapsed ceiling | Required exit |
| --- | ---: | --- |
| Recheck, pin inputs, ledger and branch packets | 10 min | Ready inputs, budgets and roles |
| Three initial research branches, concurrently | 35 min | Census, initial search log, geometry note, including failures |
| Cross-search follow-up, rule freeze and bounded pilot | 20 min | Frozen retained candidates/results or exact gaps |
| Separate review, one correction pass, final review if needed | 35 min | Scoped verdicts and final assurance table |
| Synthesis, integrity checks, accounting and handoff | 20 min | Local completion record, at most three next directions |

Unused time does not increase another phase by default. End discovery after
its phase. Stop at any binding cap and use remaining closing allocation to
report incompleteness. Stop immediately on a renewed user stop instruction.

| Resource | Proposed binding limit and accounting |
| --- | --- |
| Research profiles | Four distinct child profiles: mathematician, scout, geometer, critic. Root coordinates/summarizes outside worker dispatch accounting; its time remains inside the clock. |
| Concurrency | At most three executing children and four active participants including root. Critic runs after research handoffs; no nested agents. |
| Dispatch | At most eight stage invocations and 20 declared proxy units, per table below. Failed launches count; no automatic retry or replacement fleet. |
| Feedback | One unrolled DAG, at most two semantic review opportunities and one substantive correction pass. No repeated discovery cycle. |
| Local computation | Cumulative child wall time <=600 seconds across root, branches, critic and integrity checks. Reserve 30 bootstrap/maintenance +150 census +150 geometry/pilots +180 critic +90 closing seconds. Log failed commands too; do not reset a ledger. |
| Memory | Local analysis children: combined active peak RSS budget 2 GiB; use <=512 MiB per child when three run concurrently. Measure where available, stop on breach; this is not a reservation for model/service memory. |
| Storage | <=1 GiB incremental local artifacts from the recorded execution baseline, with >=5 GiB free-space floor. Include new analysis files/bytecode; record existing worktree allocation separately. No user-file deletion. |
| Sequence/source retrieval | <=12 query strings total, including retries/variants: up to six initial, six follow-up. <=18 source page/document opens total, including critic reinspection, and <=six detailed source records. Log no-hits, errors and access limits; no bulk scraping. |
| New candidates | <=three frozen rule variants across branches; failed variants count. One proposed 3D encoding with a 2D baseline. |
| Finite mathematics | Pilot actual input and output weights <=12; extend to <=30 only after the frozen pilot passes and budget remains. No isolated above-bound control or new high-weight sequence generation. Existing larger witnesses are symbolic-only. |

Before any local analysis process, reserve its remaining allowance and log the
command/bounds/output path. Use a fresh attempt-only meter or an existing
general facility that writes exclusively to `.runs/rr006/`; never reuse an old
attempt's meter/ledger. Serialize local compute if concurrent accounting is not
reliable. Post-exit RSS/storage observations are not hard transient guarantees;
record that limitation. Stop computation if reliable boundary checks cannot be
arranged within scope. Record model tokens/runtime, retrieval and communication
usage where exposed; unavailable measurements are **unknown**, not zero. Proxy
units are neither money, tokens nor evidence of scientific quality.

## Stage assignment and cost

Use existing [role definitions](../../../agents/registry.json), specialized by
the partition tasks in the plan. The geometric role receives combinatorial
encoding/inverse obligations, not an unrelated AI performance experiment.

| Stage | Role | Requires / hard tag | Dependencies | Proxy units |
| --- | --- | --- | --- | ---: |
| census | mathematician | formalization / first-principles | Pinned inputs | 3 |
| survey | scout | literature / primary-sources | Pinned inputs | 2 |
| geometry | geometer | geometry, formalization / structure-seeking | Pinned inputs | 3 |
| cross-search | scout | literature / primary-sources | census, survey, geometry | 2 |
| geometry-finish | geometer | geometry, formalization / structure-seeking | census, geometry, cross-search | 3 |
| review-1 | critic | falsification / constructive-skeptic | census, cross-search, geometry-finish | 2 |
| revise | mathematician | formalization / first-principles | review-1 | 3 |
| review-final | critic | falsification / constructive-skeptic | revise, review-1 | 2 |
| Maximum | four distinct profiles | | | **20** |

Topological groups are `{census,survey,geometry}` -> `{cross-search}` ->
`{geometry-finish}` -> `{review-1}` -> `{revise}` -> `{review-final}`.
Later stages can record a no-change/blocked outcome or be skipped when not
needed; skipped stages cost no dispatch. Corrections cannot add a fourth
candidate or reopen discovery. Root integration adds no new mathematical
claims after review. Any substantive unreviewed addition stays author-only.
If a failed launch consumes a reserved review slot and remaining caps cannot
support required criticism, report the assurance gap rather than borrowing
from old reviews. Separate profiles do not guarantee independent errors.

The study-local fleet is stored outside the global registry and supplied to
the existing planner in memory for an assignment-only check. One planner round
contains this already unrolled DAG; it must not be multiplied into two full
research rounds. The exact solver's objective is declared dispatch cost, not
research quality. Planning validation is not worker execution or semantic review.

## Evidence and external boundaries

Freeze candidate definitions, claimed families, inverse/image predicates,
weight/termination arguments, dependencies and hashes before trials. Check
literal U/C membership, empty input, exact-length zero padding, repetitions,
terminal drops, weight, collisions, missing images and both round trips. Do
not silently filter a failed image or ignore unassigned cases. All exposed
weights remain discovery evidence. Sequence equality, coefficient counts,
rank matching, hidden tables and saved traces cannot define/certify the final
bijection. Preferred eventual construction bounds remain quartic unary work
and quadratic auxiliary bits; no such bound is presumed for a new map.

Keep work local; no push, publication, external messages, OEIS submissions,
Drive actions, new dependencies, paid providers or general harness changes.
Read-only OEIS/primary-source web retrieval begins only with renewed execution
authorization. CY-KR1-001/002 remains PENDING; no external delivery is implied.

RR006 plans research documents and ignored analysis artifacts, not functional
repository changes. If a functional repository change becomes necessary, stop
that path and expose the scope/verification issue. Do not bypass the required
unittest suite or relax the strict research ceiling to replay legacy high-weight
fixtures. Documentation-only preparation uses link/catalog/assignment checks;
no mathematical verifier or legacy full-suite replay is authorized now.

## Completion and stop gates

Useful scoped completion requires reproducible census denominators, a complete
bounded search log (including no-hits), a precise lossless encoding or exact
information-loss obstruction, a tried-rule table preserving failures, and a
separate critic verdict on every retained new substantive claim. If a component
cannot be completed, mark it incomplete; do not redefine that as success.
Preserve unresolved objections and endpoint/author-only dependencies.

Full KR1 completion still requires universal validity, weight, termination,
both inverses, full executable A/B composition and separate semantic review;
Lean certification/exposition remain subsequent obligations. No finite census,
root-count equality or collection of infinite families alone meets that gate.

Close at the first binding budget, unrecoverable execution/accounting failure,
missing required input, instruction conflict or user stop. Save the exact
condition, work performed, failed attempts, deviations, resources (unknown
where unavailable), review scope and next unresolved lemma. Raw receipts stay
in fresh `.runs/rr006/`; deliberately reviewed evidence belongs in this folder.
No execution start/deadline or fresh research ledger exists during preparation.
