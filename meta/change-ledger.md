# Harness change ledger

Initial state: no harness improvement trial has been executed. There are no accepted or rejected experimental changes. The table below registers an example candidate only.

| ID | Change | State | Parent champion | Evaluation | Decision |
| --- | --- | --- | --- | --- | --- |
| M0001 | Independent first pass before pair reconciliation | proposed; unexecuted | To be pinned before a trial | Not created | No decision |

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
