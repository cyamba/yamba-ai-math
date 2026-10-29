# Harness change ledger

Initial state: no harness improvement trial has been executed. There are no accepted or rejected experimental changes. The table below registers an example candidate only.

| ID | Change | State | Parent champion | Evaluation | Decision |
| --- | --- | --- | --- | --- | --- |
| M0001 | Independent first pass before pair reconciliation | proposed; unexecuted | To be pinned before a trial | Not created | No decision |
| M0002 | Repository map in `AGENTS.md` (enters every worker packet), `CLAUDE.md`, and the `.claude/` benchmark instrument | user-authorized revision (2026-10-24); not trial-evaluated | `dce6026` | Instrument only; no paired trial run | Merge is the maintainer's decision |
| M0003 | [Statement fidelity, glue-first decomposition and conjecture generation](candidates/M0003-statement-fidelity-and-glue-first.md), plus the session decision log | user-authorized revision (2026-10-29); not trial-evaluated | `33862d8` | Preregistered against the next KR1 run; none executed | Merge is the maintainer's decision |

M0002 was requested directly by the user rather than selected by a trial. The `.claude/` instrument measures framework versions on registered problems and records them under `.claude/bench/records/`; its scores are descriptive and cannot promote any change. The repository-map change alters worker packets and should be benchmarked prospectively against `dce6026` on the same problem before any claim about its effect.

Use the following record for every completed, rejected-before-run, inconclusive, accepted, or rolled-back candidate. Preserve failed candidates rather than replacing them with the latest success.

## Change record template

```text
ID:
Created date:
Author / evaluator / decision owner:
State: proposed | registered | running | accept | reject | inconclusive | rolled_back
Motivating failure:
Exact change and affected paths:
Champion revision / challenger revision:
Evaluation manifest and scorer versions:
Development feedback already observed:
Held-out access and leakage: none_detected | detected | unknown; details
Execution mode, configuration, and run artifacts:
Attempted tasks / completed tasks / execution errors:
Hard-gate outcomes:
Quality effect and uncertainty:
Costs and missing measurements:
Regressions / counterexamples / reviewer disagreement:
Preregistered decision criterion and outcome:
Decision, rationale, owner, and date:
Prior champion and rollback procedure:
Post-promotion checks / rollback trigger / final disposition:
```

An acceptance or rejection is a decision with evidence and an owner. Never backfill a successful result, date, measurement, or independent review that did not happen.
