---
name: apply-theorem
description: Show how to use a theorem or construction. A statement card, a hypothesis checklist, recognition cues, standard moves, three graded worked applications, common misuses and a consequence map. Use when someone asks how to apply a result, where it is useful or what it implies.
---

# Apply a theorem

## Build the application guide

1. **Statement card**: the precise statement, its status and source, and the forms used most in
   practice (corollaries, the contrapositive, special cases).
2. **Hypothesis checklist**: how to verify each hypothesis in practice, and what to do when one
   fails (a weaker version, a different result, a reduction).
3. **Recognition cues**: what in a problem signals this result (the shape of the objects, the
   question asked, the quantities present).
4. **Standard moves**: the two to four typical uses, for example to count, to construct, to rule
   out a case, to transfer a property, or to bound.
5. **Worked applications, graded**: one routine, one that needs a reformulation first, one that
   combines the result with another. Solve each step by step and make the moment the theorem
   enters visible.
6. **Misuses**: a dropped or misread hypothesis, an applied converse, existence mistaken for a
   construction, finite evidence treated as general.
7. **Consequence map**: what it implies, what implies it, its neighbors; for this repository,
   which projects might use it, phrased as questions.

## Rules

- An application inside the repository's research is a new claim. Label it and send it through
  the solver (`audit-theorem` in `skills/`) before anything depends on it.
- When the result is `unverified` or a `conjecture`, every application inherits that status and
  is written conditionally: "if the result holds, then ...".
