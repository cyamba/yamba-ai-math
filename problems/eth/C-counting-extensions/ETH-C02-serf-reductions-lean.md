---
id: ETH-C02
source: YMB-ETH-05 ("Formal SERF reductions in Lean")
category: counting-extensions
status: open (Lean)
---

# ETH-C02: A verified reduction library

## Goal

On top of Mathlib's `SimpleGraph (Fin n)` build parsimonious, variable-count-controlled reductions to
`k`-CNF with proofs:

1. Independent sets: `{S | S independent} ≃ {x : Fin n -> Bool | F_G x}` with `F_G = AND_{uv} (not x_u or not x_v)`.
2. Proper `q`-colourings: one-hot encoding with `qn` variables, `O_q(n + e)` clauses
   (`Fintype.card (G.Coloring (Fin q)) = #SAT(F_{G,q})`).
3. Perfect matchings via a linear-size circuit and the circuit-to-3-CNF reduction (preprint Cor. 1.2).
4. Set Splitting with sets of size `<= k` (preprint Sec. 1.1.3).

Each reduction should state the variable count as a function of the input size, since only reductions with
`O(n)` variables transfer `2^{o(n)}` bounds.

## Notes

* The sheet's `ceil(log2 q)` binary colour encoding needs extra clauses for unused codes and changes the
  count unless `q` is a power of two; the one-hot encoding is simpler to verify.
* Link targets to the comparator `OAI.Algorithms.SubexponentialSAT` definitions so the final theorem is
  "`#IndependentSets` in time ... " end to end.
