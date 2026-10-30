---
id: ETH-D10
source: sheet "10 consequences" item 7 (reframed)
category: complexity-consequences
status: open (new question)
novelty: NOT VERIFIED
---

# ETH-D10: Does Extended Frege get `2^{o(n)}` refutations of 3-CNFs?

The sheet says the algorithm "bypasses" exponential lower bounds for Resolution, Cutting Planes and Polynomial
Calculus. Correct framing: there is no conflict, because the algorithm is not a proof in those systems
(preprint Sec. 1.1.1 notes compatibility with regular-resolution lower bounds).

**New question.** A deterministic algorithm with a correctness proof formalisable in a weak theory yields
short propositional proofs: if the correctness of the ETH algorithm is provable in a bounded-arithmetic theory
corresponding to Extended Frege (e.g. `VP` or `S^1_2`-style theories with the required polynomial identities),
then every unsatisfiable 3-CNF has an EF refutation of size `2^{O(n log log n / sqrt(log n))}`.

1. Which ingredients are hard to formalise feasibly: Hermite interpolation over `Q` with exponentially large
   numerators, the swap-algebra identities, the conditional-expectation schedules?
2. Is there a weaker system (e.g. `IPS` / ideal proof system with algebraic circuits) where the algorithm is
   directly a refutation? The algorithm is a sum-of-products identity, which suggests IPS refutations of
   size `2^{o(n)}`. Known exponential lower bounds for restricted IPS fragments would then constrain the
   construction.
