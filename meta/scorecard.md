# Harness trial scorecard

Use one record per system and paired task. Fix rubric definitions and weights before the trial. These fields are a reporting contract; a response that merely fills them out has not passed evaluation.

## Identity and integrity

| Field | Record |
| --- | --- |
| Trial, candidate, task, and pair IDs | Stable identifiers |
| Champion/challenger | Label plus exact revision |
| Mode | Manual, external command, or replay |
| Provider and configuration | Model/version, tools, seeds, prompt and scorer versions |
| Input/output artifacts | Paths and hashes where available |
| Leakage or contamination | None detected, detected, or unknown; describe evidence and effect |
| Execution errors | Timeouts, invalid output, missing files, blocked dependents, or other failures |
| Deviations | Difference from preregistered plan and when discovered |

## Hard gates

Define each gate's adjudication before the run. Examples:

- No fabricated citation, experiment, execution, proof verification, or result.
- The delivered answer addresses the assigned question and exposes material uncertainty.
- A proof claim has an actual checked argument at the declared assurance level.
- A source-grounded claim is supported by an inspected source at the declared inspection depth.
- The run respects scope, permissions, evaluation isolation, and resource caps.

Record `pass`, `fail`, or `unknown`, reviewer, and supporting evidence. Unknown does not satisfy a mandatory gate. A failed execution remains in the denominator; it is not silently removed as a bad sample.

## Outcome and resources

| Dimension | Suggested measure |
| --- | --- |
| Correctness | Independently adjudicated task success and partial credit defined in advance |
| Evidence | Supported claims / checked material claims, with denominator and source defects |
| Mathematical value | Precise useful statement, valid derivation, informative counterexample, or principled obstruction |
| Coverage | Substantive requested items completed / requested items |
| Calibration | Risk–coverage information or rubric-based uncertainty fidelity, as appropriate |
| Reproducibility | Inputs, configuration, outputs, and verification sufficient to repeat the task |
| Cost | Dispatch proxy, measured input/output tokens, model charges, tool use, elapsed time, peak memory where relevant |
| Human effort | Reviewer time and manual repair effort |
| Correlation | Shared wrong claims or failure modes across workers, with an explicit definition |

Unknown cost measurements must stay unknown. Report provider billing separately from proxy units and tokens. Compare quality at fixed budget or cost at matched quality; give the numerator and denominator for any efficiency ratio. An empty, cheap answer is not a successful outcome.

## Paired decision report

Include number of attempted tasks, gates passed, wins/losses/ties, effect estimates, uncertainty, per-stratum behavior, total resources, leakage, errors, and reviewer disagreement. State the preregistered criterion and whether it was met. Distinguish exploratory evidence from confirmation. Recommend `accept`, `reject`, or `inconclusive` and give the rollback trigger.

## CLI evaluation records

The `compare` command accepts two evaluation JSON records with these fields:

```text
evaluation_id: unique record identifier
candidate_id: pinned system identifier
suite_id: shared evaluation suite identifier
suite_revision: shared suite revision
split: "heldout"
synthetic: true or false
cases:
  - case_id: shared paired task identifier
    answered: boolean
    complete_correct: boolean
    false_claims: nonnegative integer
    unsupported_claims: nonnegative integer
    cost_units: nonnegative finite number
```

Pair the same case IDs under the same suite, revision, and split. This compact machine record reports coverage, completed-correct count and rate, the fraction of answered responses containing any false or unsupported claim, and total cost. False and unsupported claims are distinct labels and may overlap; do not infer one from the other.

The CLI can report observed Pareto dominance: no lower success or coverage, no worse recorded risks, no higher cost, and at least one strict improvement. This is descriptive evidence on the supplied cases. It does not estimate statistical significance, evaluate novelty or proof quality, or authorize promotion. `promotion_authorized` is always false. Synthetic examples are ineligible for a real improvement claim, and replay is not an independent confirmation.

Independent scoring, credible uncertainty, mathematical review, and the promotion decision remain research responsibilities. Preserve the richer scorecard and raw evidence alongside this compact record.
