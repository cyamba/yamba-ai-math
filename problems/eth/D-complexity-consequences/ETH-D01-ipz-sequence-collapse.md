---
id: ETH-D01
source: sheet "Refuting ETH" consequence 1; sheet "10 consequences" item 1
category: complexity-consequences
status: audited (correct, conditional on Theorem 1)
---

# ETH-D01: Collapse of `s_k`, #ETH, and the sparsification floor

* **Correct.** `s_k = inf{delta : k-SAT in DTIME(2^{delta n})} = 0` for every fixed `k >= 3`; ETH and #ETH
  (Dell-Husfeldt-Marx-Taslaman-Wahlen) are refuted (preprint Sec. 1.1.2). Curticapean's #ETH lower bound for
  perfect matchings in bipartite graphs with `O(v)` edges is contradicted by Cor. 1.2.
* **Corrected.** The sparsification lemma remains a tool; the preprint chooses
  `sigma ~ (log log n)^2 / sqrt(log n)` so the leaf count matches the algorithm's exponent. The sheet's
  "`2^{O(n/log n)}`" is wrong; read `2^{O(n / sqrt(log n))}` up to `log log` factors.

## Open questions

1. Quantify `s_k(n)`-type refinements: define `s_k(f) = inf{delta : k-SAT in 2^{delta f(n)}}` for
   `f(n) = n / sqrt(log n)`. Is `s_3(f) > 0`? (This is [ETH-B08](../B-exponent-frontier/ETH-B08-sqrt-log-hypothesis.md).)
2. Do the IPZ monotonicity results (`s_k < s_{k+1}` infinitely often under ETH) have analogues at the
   new scale?
