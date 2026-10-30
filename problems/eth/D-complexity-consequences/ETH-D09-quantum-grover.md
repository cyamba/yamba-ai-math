---
id: ETH-D09
source: sheet "10 consequences" item 6
category: complexity-consequences
status: audited (correct)
---

# ETH-D09: Classical versus Grover for fixed-width SAT

* **Correct.** For fixed `k`, `2^{o(n)}` classical time beats Grover's `2^{n/2}` search asymptotically, so the
  quadratic quantum speedup over brute force is not a speedup over the best classical algorithm for `k`-SAT.
* **Question.** Can amplitude amplification be combined with the algorithm's enumeration (measurement tuples
  times in-group assignments) for a `2^{rho(n)/2}` quantum algorithm? The outer sum is a sum of products, not a
  search, so this needs quantum counting with exact output; likely only constant factors in the exponent.
* Unbounded width (CNF-SAT with `k = Theta(log n)`) remains the regime where Grover is the best known
  general speedup.
