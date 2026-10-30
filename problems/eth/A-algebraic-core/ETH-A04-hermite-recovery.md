---
id: ETH-A04
source: YAMBA-378-04; preprint Sec. 2.4 ("Recovering the count from Taylor coefficients") and Appendix E
category: algebraic-core
status: uniqueness solved (Lean); explicit weights and bit bounds open
---

# ETH-A04: Hermite recovery of `H(0)` from Taylor jets

## Statement

`H in Q[T]`, `deg H < QJ`, data `h_{t,r} = [z^r] H(t+z)` for `t in {1..Q}`, `r < J`.

1. **Uniqueness.** The data determine `H`.
2. **Weights.** Find explicit `w_{t,r}` with `H(0) = sum_{t,r} w_{t,r} h_{t,r}`.
3. **Bit length.** Bound numerators and denominators of `w_{t,r}`.

## Results

* **Proved, Lean**: if `(X - t)^J | P` for all `t` in a set `S` of `Q` distinct points and
  `natDegree P < Q J` then `P = 0` (`EthProblems.Hermite.eq_zero_of_pow_dvd_at_nodes`), hence equal Taylor
  data imply equality (`eq_of_taylor_data`). File: [HermiteUniqueness.lean](../lean/EthProblems/HermiteUniqueness.lean).
* **Established (classical)**: residue formula. With `Omega(T) = prod_t (T - t)^J`,
  `H(0)/Omega(0) = - sum_t Res_{T=t} H(T) / (T Omega(T))`, so
  `w_{t,r} = -Omega(0) [ (T-t)^{J-1-r} ] ( 1 / (T prod_{s != t} (T - s)^J) )` expanded at `T = t`.
  The sheet's displayed closed form has typographical errors in the inner product; use this one.
* **Unverified (target)**: `lcm(1..Q)^{2J}`-type denominator bound. The preprint's Appendix E bounds the
  interpolation arithmetic directly; a clean combinatorial formula via
  `1/(T - s)^J = sum_k C(-J, k) (t - s)^{-J-k} (T - t)^k` gives denominators dividing
  `prod_{s != t} (t-s)^{J + J - 1}`, i.e. `((Q-1)!)^{2J}` up to a factor `t^{J}`.

## Next steps

* Lean: formalise the residue formula over `Q` (partial fractions in `Polynomial`/`RatFunc`).
* SymPy: tabulate `w_{t,r}` for `Q <= 12`, `J <= 6` and test the conjectured denominator bound.
* Research angle (feeds [ETH-B03](../B-exponent-frontier/ETH-B03-polynomial-row-routing.md)):
  nodes need not be `1..Q`; any `Q` points where designs exist work. Structured nodes (the preprint's
  tensor appendix uses residue-field lifts) can shrink bit lengths.
