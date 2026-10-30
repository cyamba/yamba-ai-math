---
id: ETH-B01
source: new (this program); answers YAMBA-378-06 negatively
category: exponent-frontier
status: proved; core lemma machine-checked (Lean 4 + Mathlib); article written (revision 2 after referee pass)
novelty: NOT VERIFIED (the preprint is five days old; no follow-up work found on 2026-10-30)
---

# ETH-B01: Routing rigidity and the optimality of the interpolation route

Full write-up: [articles/sqrt-log-barrier.md](../articles/sqrt-log-barrier.md).

## Routing rigidity lemma (proved, Lean)

Index `u = (a_u, d_u) in [r]^Q x [r]^Q`, `D = r^{2Q}`. Call `M in K^{D x D}` *routing-supported with
defect `R`* if `M[u,w] != 0` implies `Ham(d_u, a_w) <= R - 1`. Then for **every** such `M`, commutative or
not, every symbol split `[r] = X ⊔ Y` and all `k_1 + k_2 >= Q + R`,

`rank(I - M) >= #{u : a_u has >= k_1 symbols in X, d_u has >= k_2 symbols in Y}`.

With `|X| = r/2`, `k_1 = k_2 = ceil((Q+R)/2)`: `rank(I - M) >= D Pr[Bin(Q, 1/2) >= (Q+R)/2]^2 = D e^{-(1+o(1)) R^2/Q}`
for `R = o(Q)`, `R >> sqrt(Q)`.

*Proof.* On the product block `T` every `d_u` and `a_w` disagree on `>= k_1 + k_2 - Q >= R` positions, so
`M[T, T] = 0` and `(I - M)[T,T] = I`. Lean: `EthProblems.RoutingRigidity.rank_one_sub_ge_card_block`.

## Template barrier (proved; revised after referee pass)

In the preprint's interpolation template (Secs. 2.3-2.6, 3, 4), rows have the form
`<P_u(T), zeta> = ((I - M_0) zeta)_u + sum_w M_0[u,w] prod_{s in E_{u,w}}(1 - T/s) zeta_w`; the degree bound
`R - 1` forces exactly the routing support, measurements are taken on the full auxiliary space
(`c = rank(I - M_0)`, `r h c` rows, `h >= max(1, M/D)`), and Hermite recovery needs `q >= n(R-1)/Q` Taylor
coefficients per node. Keeping the `log(Q/R)` factor of the Taylor cost, the exponent of every such
instantiation is at least

`c rho(n) = c n (log log n)^2 / sqrt(log n)`

for an absolute `c > 0`, for every choice of `r, Q, R, tau, D` and every `M_0` (commutative or not).
**So the preprint's interpolation route is optimal for its own template up to a constant factor.**

## Corollaries

* Chebyshev, Pade, Krawtchouk and weighted-`L_2` choices of `f` ([ETH-B02](ETH-B02-spectral-approximants.md)),
  non-symmetric `gamma_S` and non-commutative `M_0` cannot improve the interpolation route beyond constants.
  Non-commutative `M_0` can improve `R` by at most `sqrt 2` at equal `eps` (`(3,2,2)`: 10 to 9 numerically).
* **The preprint's tensor-contraction method beats this template**: `n log log n / sqrt(log n)` in general and
  `n / sqrt(log n)` at bounded density, including on bounded-occurrence inputs. It must therefore violate a
  template assumption (Cauchy deformation on packets instead of swap routing, recursion, structured
  recovery). Locating which one is now a top problem ([ETH-B04](ETH-B04-loglog-gap.md)).
* **Open relaxations of the template** (not covered by the barrier): node-dependent polynomial rows (only
  `eps >= 4^{-R}` known, [ETH-B03](ETH-B03-polynomial-row-routing.md)) and measurement on used labels only,
  where type-balanced labelings avoid every product block ([ETH-B07](ETH-B07-sparse-embedding-escape.md)).

## Supporting results

* **Lemma B (biased Smolensky; proof sketch, exact check for `Q <= 4`).** For `h` of degree `<= d` on `{0,1}^Q` and `0 < p <= 1/2`,
  `Pr_{mu_p}[h != (-1)^{|y|}] >= E_{m ~ Bin(Q,2p)} 2^{-m} sum_{i > floor(m/2)+d} C(m,i)`. This is the
  eigenvalue-side view of the commutative case; exact check in
  [checks/smolensky_biased_check.py](../checks/smolensky_biased_check.py).
* **One-dimensional shadow (Lean).** `no_low_degree_parity_match`: degree `< R` cannot match parity on
  `R + 1` consecutive integers.
* Numerical scan of the cost model: [checks/template_barrier_numeric.py](../checks/template_barrier_numeric.py).
