---
id: ETH-D07
source: sheet "Refuting ETH" consequence 4
category: complexity-consequences
status: audited; sheet claim refuted
---

# ETH-D07: Planar `2^{Theta(sqrt n)}` bounds

**Sheet claim:** feeding planar 3-SAT to the algorithm shifts planar barriers from `2^{Theta(sqrt V)}` to
`2^{O(sqrt V / log V)}`. **Refuted as a consequence.**

* Planar problems already have `2^{O(sqrt V)}` algorithms by planar separators. Reducing a planar instance on
  `V` vertices to SAT gives `N = Theta(V)` variables and time `2^{O(V / sqrt(log V))}`, which is worse.
* What changes: the ETH-conditional *lower bounds* `2^{Omega(sqrt V)}` (3-SAT on `n` variables to planar
  instances with `V = O(n^2)` via crossover gadgets) are no longer justified. They would now follow only from
  `2^{Omega(n)}`-hardness of 3-SAT, which is false.

## Genuine open question

Is there a `2^{o(sqrt V)}` algorithm for planar Independent Set (or planar 3-SAT)? The refutation of ETH gives
neither an algorithm nor a lower bound. A conditional lower bound from a `sqrt(log)`-type hypothesis would give
`2^{Omega(sqrt V / (log V)^{1/2 + o(1)})}` via the same `V = O(n^2)` reduction (substitute `n = sqrt V` into
`T_3SAT(n) = 2^{n / (log n)^{1/2 + o(1)}}`; note `log sqrt V = (1/2) log V`).
