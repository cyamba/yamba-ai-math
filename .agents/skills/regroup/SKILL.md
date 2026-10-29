---
name: regroup
description: Reflect on a KR1 research checkpoint, distinguish proved progress from open obligations, and choose a bounded next step or feedback task.
---

# Regroup around the objective

Use at a scheduled review or handoff, after a decisive obstruction, or when
the operator asks to pause and reflect. Keep the reflection proportionate to the
remaining budget. It does not add critic rounds or restart a closed investigation.

Read root CLAUDE.md and AGENTS.md, the current result, applicable contract, and
only the proofs or receipts needed to resolve the status. Start from
[the current handoff](../../../research/rogers-ramanujan/NEXT_SESSION.md) and the
[pinned target](../../../research/rogers-ramanujan/TARGET.md); read only the last ten
lines of [the session log](../../../meta/session-log.md).

Record a short dated checkpoint in the canonical research folder:

- Original objective and exact current completion status.
- What was proved, refuted, or only observed; link evidence and distinguish
  separate semantic review from author argument and executable checks.
- Decisive unresolved lemma, strongest obstruction, and at most two promising
  directions. Explain why the evidence justifies the next step.
- One transferable workflow hypothesis, explicitly unvalidated. Do not infer a
  better discovery rate from a successful session or a useful counterexample.
- Trace each open obligation back to the pinned target. Name obligations that
  no longer serve it, and results whose scope delta no glue argument closes.
- Stall check: an obligation that survived two attempts or review rounds
  without closing is not attacked again directly. First run its smallest-case
  falsifier and log a refutation in the project's failure ledger; if it
  survives, decompose it glue-first (sub-lemmas plus a reviewed glue argument,
  the `decomposer` role and `decompose` fleet) before releasing sub-lemmas.
- One bounded next action, deliverable, resource boundary and stop condition.

Append one line for the workflow decision to the session log.

Use delegate-for-feedback for a useful human subproblem; use yamba-post to park
cross-project findings without following them here. Keep pending tasks discoverable
in [feedback.md](../../../research/rogers-ramanujan/feedback.md), with stable IDs.
For a new mathematical direction, load explore-angle and exploration instructions.
For a change of mechanism, use pivot. A short reflection may conclude that the
present approach is still strongest; a pivot is not required.
