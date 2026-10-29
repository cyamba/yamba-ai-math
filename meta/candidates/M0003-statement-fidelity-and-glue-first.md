# M0003: Statement fidelity, glue-first decomposition and conjecture generation

- State: **user-authorized revision (2026-10-29); not trial-evaluated**
- Parent champion: `33862d8` (main after #25)
- Challenger: branch `claude/cfsg-harness-learnables`
- Evaluation: preregistered below; no trial run yet
- Promotion decision: none. Merge is the maintainer's decision.

## Motivating evidence

Axiom's Lean formalization of the Classification of Finite Simple Groups
([NR-001](../../novelty_radar/NR-001-cfsg-lean-agent-swarm.md), step 3 "method extraction") reports
practices that address failures this harness can also show. Only claims checked against the
[Axiom post](https://axiommath.ai/research/the-enormous-theorem-formalized/) and the
[repository README](https://github.com/AxiomMath/CFSG) on 2026-10-28 are used here. Credit: the
Axiom team and its advisers Richard Lyons, Dan Nakano and Ronald Solomon, as listed in NR-001; the
lead came from Dr. Samuel Allen Alexander's video. Figures and thresholds that appear only in a
secondary AI-generated summary (role allocation ratios, retry limits, glue-proof line caps, a
declaration count) were not adopted.

| Swarm practice (as reported) | State here before | Change in this candidate |
| --- | --- | --- |
| Target statement fixed outside the swarm (TauCeti) | KR1 target repeated as prose in four files, no hash | [TARGET.md](../../research/rogers-ramanujan/TARGET.md); optional program `target` hash checked at load and every dispatch (`harness/catalog.py`, `harness/runtime.py`) |
| Proofs "under additional, unproved assumptions" deleted; review compared each proved statement with the intended target | Critic gives `conditional`, but nothing diffs a result against the target | Proved claims under a pinned target declare `target_relation` and `scope_delta`; target diff first in `agents/critic.md` and `skills/audit-theorem` |
| Stalled milestones split into precise smaller theorems plus "a short Lean proof" that they imply the milestone | No decomposition step; KR1 lead obligation open since RR003 | `agents/decomposer.md`, `decompose` fleet; stall check in the regroup skill |
| Literature errors found by failed formalization and counterexamples | Mostly present: critic, `terra2026/failure-ledger.md` | Smallest-case falsifier runs before decomposition (regroup) |
| Integration agents traced the final theorem back to prerequisites | Partial (partitions claim index) | Regroup traces open obligations to the pinned target |
| Route choice by what is already formalized, not shortest paper proof | Not stated | Pivot compares routes by unproved prerequisites |
| (Not from the swarm) | No role generates conjectures; mathematician offers at most two | `agents/conjecturer.md`, `discover` fleet |
| Build cache, externalized certificates | Scale far smaller; certificate checks exist per project | Deferred |

Also added: a one-line [session decision log](../session-log.md) read by reflect-before-run, regroup,
pivot and improve-harness, and validated by `scripts/check_repository.py`.

## Self-improvement loops reviewed

- Mathematics harness: reflect-before-run (pre-run tweaks), regroup (checkpoint), pivot (route
  change) and improve-harness (controlled comparison) existed, but no decision persisted across
  sessions except prose handoffs, so a tweak's outcome was never closed. The log closes that loop.
- Framework harness: harness-retro plus `harness-architect` propose one change from benchmark
  records. The benchmark itself had no step questioning whether its axes still track new
  mathematics; the operator layer now carries that review separately from research files.

## Hypothesis and prediction

Pinning the target and declaring scope deltas makes restricted results visible at freeze rather
than in later review; glue-first turns a stalled obligation into sub-lemmas whose sum is already
checked; a conjecture stage widens the set of tested mechanisms. Expected effect: more decisive
findings and novel contributions per run without lower claim integrity, at a modest added cost.

## Preregistered evaluation

The next authorized KR1 program runs on the challenger with `target` pinned. Compare it with the
retrospective KR1 baseline record on the same problem, axis by axis: decisive finding, novel
contribution, idea generation, claim integrity and resource efficiency. One run on one problem is
descriptive only; acceptance needs a paired trial under [meta/protocol.md](../protocol.md).
Falsifier: restricted results still reach review unlabeled, or the decompose stage produces glue
that review rejects without closing any obligation.

## Rollback

Revert the branch commits. Programs without `target` behave exactly as before; the new roles and
fleets are dispatched only when a program names them.
