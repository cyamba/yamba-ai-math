---
id: ETH-A03
source: YAMBA-378-03; preprint Sec. 2.6 Step 2 ("Choosing f to fix most basis directions")
category: algebraic-core
status: open (formalisation); counting facts established
---

# ETH-A03: The `{0, +1, -1}` eigenbasis of the swap action

## Statement

On `Q^{[r] x [r]}` the swap `S(e_{ab}) = e_{ba}` has the orthogonal eigenbasis
`e_{aa}` and `e_{ab} + e_{ba}` (`a < b`, eigenvalue `+1`, `r(r+1)/2` vectors) and `e_{ab} - e_{ba}`
(`a < b`, eigenvalue `-1`, `r(r-1)/2` vectors). Tensor products over `Q` positions give an orthogonal basis of
`Q^B`, `B = ([r]x[r])^Q`, with entries in `{0, 1, -1}`, squared norms `2^{(number of off-diagonal factors)}`,
and `C(Q,j) d_-^j d_+^{Q-j}` vectors with exactly `j` antisymmetric factors (`d_+ = r(r+1)/2`,
`d_- = r(r-1)/2`). On such a vector `W_0` acts by `j`, `V_0` by `(-1)^j`, `M_0` by `(-1)^j f(j)`.

## Known

**Established** (preprint; elementary). The `2 x 2` change of basis on `{e_ab, e_ba}` is the Hadamard matrix
`[[1,1],[1,-1]]`, which gives the `{0, +1, -1}` entries.

## Lean plan

* Index set `Fin r x Fin r`; define `sym a b`, `anti a b : Fin r x Fin r -> Z`; prove `v (swap p) = +- v p`.
* Count: `#{(a,b) : a < b} = r.choose 2` via `Finset.card_powersetCard` and the bijection with 2-subsets.
* Tensor product: for `psi u = prod_s psi_s (u s)` show `(Pi_t psi) = eps_t psi`, then
  `#{choices with j antisymmetric factors}` by `Finset.card_pi` and a binomial sum.

## Role

The measurement matrix `C` consists of the exceptional basis vectors. Their integrality and `l_1` norm
`<= D` bound the measurement range `[-D, D]`; any non-commutative replacement ([ETH-B03](../B-exponent-frontier/ETH-B03-polynomial-row-routing.md))
must keep an integral, bounded spanning set for the row space of `I - M_0`.
