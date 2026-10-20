# M0001: Independent first pass before pair reconciliation

- State: **proposed; unexecuted example**
- Champion revision: not yet selected
- Challenger revision: not yet implemented
- Evaluation: not yet created
- Result or promotion decision: none

## Hypothesis

Keeping a derivation worker and a counterexample worker isolated until both submit their first outputs may reduce premature agreement. Any benefit must exceed the cost of duplicate work and later reconciliation.

## Proposed change

For a bounded pair investigation, give both workers the same original brief and separate role instructions. Withhold peer answers until both first outputs are recorded. Then expose the two outputs to a synthesis stage. Keep the number of calls, allowed tools, evidence, total dispatch budget, and output requirements matched to the champion.

The champion comparison would use the current collaboration pattern selected and pinned before the trial. It must not be invented after observing the challenger.

## Proposed evaluation

Use a mixture of small theorem checks with known invalid arguments, true lemmas with checkable proofs, and claims requiring a concrete counterexample. Include cases where the initial attractive answer is wrong. An independent evaluator should prepare and hold active tasks outside candidate access.

Preregister task count, scoring, fixed resource caps, task strata, uncertainty method, and minimum useful gain before any held-out execution. Score valid corrections, missed errors, false rejections, substantive coverage, reviewer effort, token and elapsed costs, and overlap in wrong claims. Compare with a single worker given the same total budget and independent retries where feasible.

## Predictions and falsifiers

The challenger should find more distinct valid objections without increasing false objections enough to erase the benefit. Reject or park the proposal if it only lengthens reports, loses correctness, inflates cost beyond the cap, or fails the preregistered practical improvement threshold. A null result is useful evidence about this topology on the tested tasks.

## Boundaries and rollback

This proposal changes information flow for one topology. It does not change research goals, evidence gates, permissions, tools, or spending authority. Reverting the topology configuration to the pinned champion must restore the previous workflow. Record any trial and decision in `meta/change-ledger.md`; do not interpret this document as an accepted improvement.
