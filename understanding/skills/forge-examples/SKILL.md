---
name: forge-examples
description: Generate and verify examples for a definition, theorem, construction or algorithm. Smallest and typical cases, edge cases, a non-example for each hypothesis, counterexamples to tempting generalizations, parametric families and stress tests, all computed by code over a stated range. Use whenever an explanation, exercise, figure or application needs concrete instances.
---

# Forge examples

## Kinds of examples

| Kind | Purpose |
| --- | --- |
| Smallest nontrivial | First contact; checkable by hand |
| Typical | Shows general behavior rather than a coincidence of small numbers |
| Edge or extreme | Boundary parameters, empty or degenerate cases, equality cases |
| Non-example per hypothesis | Violates one hypothesis; the conclusion visibly fails |
| Counterexample to a tempting generalization | Protects against the most likely misreading |
| Parametric family | Shows how the structure grows with n, q or another parameter |
| Stress test | Random or large inputs checking claimed properties of code (inverse maps, invariants, weights) |

Aim for the fewest examples that make both the pattern and its limits visible.

## Steps

1. **Implement the definitions directly** and plainly in code before anything clever, with the
   Python standard library and exact arithmetic (integers, `fractions.Fraction`) where possible.
2. **Generate and verify.** Check claimed properties by computation (weight preserved, maps
   mutually inverse, counts equal) over a stated finite range, and report the range.
3. **Select** the examples to show and say what to notice in each.
4. **Non-examples** show the failing conclusion explicitly, not just the violated hypothesis.
5. **Search for a counterexample** to the most tempting stronger statement. If none appears, write
   "none found up to N", never "it is true".
6. **Save** the script beside the output with fixed seeds and the command that reproduces it.

## Rules

- **Finite checks are evidence, not proof.** An example table never stands in for a universal
  claim. Finite agreement cannot define or certify a construction either.
- **Small numbers mislead.** Include at least one example beyond the range where coincidences
  happen.
- **If an example contradicts the source**, stop. Recheck the definitions and the code, then
  record it as a possible counterexample (`unverified`) and route it (see "Feed the solver" in
  the entry skill).
