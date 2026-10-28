---
name: step-by-step
description: Turn a proof, derivation, construction or algorithm into numbered, individually checkable steps, each with its justification and motivation, plus checkpoints on a concrete example. Use for proof walkthroughs, worked solutions, tracing bijections and reading formal (Lean) proofs.
---

# Step by step

## Build the steps

1. **Goal and givens**: what is to be shown, the hypotheses, the definitions, and earlier
   results with their sources.
2. **The plan first**: the proof skeleton in three to seven moves. Readers need the map before
   the walk.
3. **Expand** each move into steps small enough to verify locally.
4. **Tag every step** with its justification:
   `[definition]`, `[hypothesis: name]`, `[result: name and source]`, `[computation]`,
   `[algebra]`, `[case split]`, `[induction hypothesis]`, `[construction]`,
   `[without loss of generality: why allowed]`, `[formal: Lean declaration]`.
5. **Separate validity from motivation**: the tag says why the step is valid; one short line
   says why we take it, where it would otherwise look unmotivated.
6. **Checkpoints**: after key moves, run the steps on the smallest example and show the
   intermediate objects (forge-examples).
7. **Recap**: a table of which hypothesis was used where. An unused hypothesis is a signal to
   investigate (a stronger statement, or a missed use).

## Gaps

When a step cannot be justified from the source, mark it **GAP** and say what is missing. Do not
invent a justification; route the gap (see "Feed the solver" in the entry skill). "Clearly",
"it is easy to see" and "similarly" each need a short reason or an explicit step.

## Formal proofs

List the main declarations in dependency order, give each an informal statement, explain a
tactic only where it carries an idea, and record what the formal statement assumes (definitions,
axioms, imported libraries). A machine check covers the formal statement, not its translation
from ordinary language.

## Algorithms and bijections

Give the state, the loop invariant, the step rule, the termination measure and the inverse.
Trace one small input completely, then one input that exercises an edge case.

## Format

Numbered steps, one claim per line, displayed formulas for anything nontrivial, and a closing
"what we used" table.
