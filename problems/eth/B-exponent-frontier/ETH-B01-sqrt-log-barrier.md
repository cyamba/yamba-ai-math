---
id: ETH-B01
source: new (this program); answers YAMBA-378-06 negatively
category: exponent-frontier
status: proved; core lemma machine-checked (Lean 4 + Mathlib); article written
novelty: NOT VERIFIED (the preprint is five days old; no follow-up work found on 2026-10-30)
---

# ETH-B01: A `sqrt(log n)` barrier for the replacement-form template

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

## Template barrier (proved)

In the preprint's template (Secs. 2.3-2.6, 3, 4), rows have the form
`<P_u(T), zeta> = ((I - M_0) zeta)_u + sum_w M_0[u,w] prod_{s in E_{u,w}}(1 - T/s) zeta_w`; the degree bound
`R - 1` forces exactly the routing support, and the measurements number `r h c` with `c >= rank(I - M_0)` and
`h >= max(1, n/D)`. Combining with the lemma: `log(r / 2 tau) <= log(1/eps) <= (1+o(1)) R^2 / Q`. The
running-time exponent `n[(R/Q) log(Q/R) + tau log D + 1/r]` is then at least

`c n log log n / sqrt(log n)`

for an absolute `c > 0`, for every choice of `r, Q, R, tau, D` and every `M_0` (commutative or not).

## Corollaries

* The preprint's interval interpolation is optimal within its algebra up to constants in `R` (factor
  `sqrt 2`): the commutative construction achieves `log(1/eps) ~ R^2/(2Q)`, the universal bound is
  `~ R^2/Q`. Non-commutative `M_0` can only improve constants ([ETH-B03](ETH-B03-polynomial-row-routing.md):
  `(3,2,2)` goes from 10 to 9 numerically).
* Chebyshev, Pade, Krawtchouk and weighted-`L_2` choices of `f` ([ETH-B02](ETH-B02-spectral-approximants.md))
  cannot change the order.
* The interpolation route's `(log log n)^2/sqrt(log n)` is a `log log n` factor above the barrier; the
  tensor-contraction route of Theorem 1 attains `log log n / sqrt(log n)`, i.e. matches it.
* **Remaining escapes**: general polynomial rows (`rho_{u,t}` varying with the node; only `eps >= 4^{-R}` is
  known, [ETH-B03](ETH-B03-polynomial-row-routing.md)), rank savings on filled coordinates
  ([ETH-B07](ETH-B07-sparse-embedding-escape.md)), or a different recovery than Taylor jets.

## Supporting results

* **Lemma B (biased Smolensky, proved).** For `h` of degree `<= d` on `{0,1}^Q` and `0 < p <= 1/2`,
  `Pr_{mu_p}[h != (-1)^{|y|}] >= E_{m ~ Bin(Q,2p)} 2^{-m} sum_{i > floor(m/2)+d} C(m,i)`. This is the
  eigenvalue-side view of the commutative case; exact check in
  [checks/smolensky_biased_check.py](../checks/smolensky_biased_check.py).
* **One-dimensional shadow (Lean).** `no_low_degree_parity_match`: degree `< R` cannot match parity on
  `R + 1` consecutive integers.
* Numerical scan of the cost model: [checks/template_barrier_numeric.py](../checks/template_barrier_numeric.py).
