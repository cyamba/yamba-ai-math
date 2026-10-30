---
id: ETH-C01
source: YMB-ETH-03 ("q-series lifting"); sheet consequence on FPT; preprint Cor. 1.2
category: counting-extensions
status: proof sketch (conditional on Theorem 1)
---

# ETH-C01: Weight enumerator `Z_F(q)` and k-Vertex Cover in `2^{o(k)}`

## Statement

For a `k`-CNF `F` on `n` variables let `c_w(F) = #{x in SAT(F) : |x| = w}` and `Z_F(q) = sum_w c_w(F) q^w`.

**Claim (proof sketch).** For fixed `k`, all `c_0(F), ..., c_n(F)` can be computed deterministically in
`(n+m)^{O_k(1)} 2^{O_k(rho(n))}` time and polynomial space, `rho(n) = n (log log n)^2 / sqrt(log n)`.

## Sketch

1. Fix a rational `q`. `Z_F(q) = sum_x prod_e Phi_e(x) prod_v (1 + (q-1) x_v)` is a sum of products of
   low-degree factors with bounded scopes. The algorithm of Secs. 2-3 never uses that factors are
   satisfaction indicators except to read off `H(0)`; adding one unary factor per variable keeps occurrences
   bounded (`+1`) and the product degree linear, so `H_q(0) = Z_F(q)`.
2. Sparsification is disjoint on the same variable set, so `Z_F(q) = sum_leaves Z_G(q)`. In the Tovey copying
   step attach the weight to one copy only; OR-gate variables get weight 1. Both maps are bijections on
   satisfying assignments preserving the original coordinates.
3. Evaluate at `q = 0, 1, ..., n` and solve the Vandermonde system (`O(n^3)` exact arithmetic).

**Gap to close.** The faster route (Sec. 2.8, sparse `F_2` equations with the Beigel-Tarui lift) computes counts
modulo `2^l`. Weighted sums with integer `q` remain integers bounded by `(q+1)^n 2^n`, so take `l` of size
`O(n log n)`; check that the truncation-by-`h`-copies argument still keeps the product degree `O(n)` (it does
if `l = O(n)` only; with `l = O(n log n)` the degree may grow to `O(n log n)`). Safer: use the interpolation
route only, whose exponent is `rho(n)`.

## Consequence: k-Vertex Cover (proof sketch)

Kernelize to a graph `G'` on `<= 2k` vertices (Nemhauser-Trotter / crown reduction, polynomial time). Encode
independent sets of `G'` as the 2-CNF `AND_{uv in E'} (not x_u or not x_v)` on `2k` variables. The weight
enumerator gives the number of independent sets of every size, hence the minimum vertex cover of `G'`.
Time `poly(n) + 2^{O(k (log log k)^2 / sqrt(log k))}`. Under ETH no `2^{o(k)} poly(n)` algorithm was believed
to exist (see Cygan et al., *Parameterized Algorithms*, 2015, chapter on ETH-based lower bounds); this gives one, conditional on Theorem 1.
**Novelty: NOT VERIFIED**, it is an immediate corollary once C01 is proved.

## Tasks

1. Write the full proof of the claim along the preprint's Secs. 3-5 with weights; verify bit-length bounds.
2. Lean: the identity layer (weights as extra unary factors) on top of [ETH-A07](../A-algebraic-core/ETH-A07-algebraic-core-decoupling.md).
3. Extend the list: Max-Ones-k-SAT, exact-weight #k-SAT, Hamming-weight-constrained local inversion.
