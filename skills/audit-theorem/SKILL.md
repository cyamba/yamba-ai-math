---
name: audit-theorem
description: Audit a mathematical claim or proof about learning, architectures, attention, factuality, or agent systems and identify decisive counterexamples and remaining obligations.
---

# Audit a theorem

Extract the exact statement, quantifiers, definitions, and assumptions before reviewing the proof. Check dimensions, norms, probability spaces, parameter dependencies, and boundary cases. Distinguish expressivity, approximation, estimation, optimization, and measured system performance.

Try a smallest counterexample and a degenerate case first. Check the step that carries the main conclusion, not just the easy lemmas. When a larger model class contains the proposed architecture, a superiority statement needs a resource, data, optimization, or distribution restriction. Check whether a purported geometry preserves labels and whether compression erases a rare distinction.

For attention arguments, avoid transferring rank bounds on logits to post-softmax weights. For verification, identify the target truth relation, false-acceptance assumptions, coverage, and dependence between checks. A sound checker relative to false evidence cannot certify world truth. Numerical checks can refute a universal statement but do not prove it.

Return the formal statement, a verdict of `supported`, `conditional`, `incomplete`, or `refuted`, and prioritized findings with the precise failing step or missing assumption. Separate a complete proof from a repair conjecture. Cite verified sources for imported results and record remaining proof obligations.

Recommend the narrowest defensible statement and one decisive next check. Use a distinct reviewer when the fleet requires it; distinct agent identity does not itself imply independent errors.
