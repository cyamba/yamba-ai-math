# ETH-B07. Measurement separation and Hermite uniqueness

| Field | Value |
| --- | --- |
| Category | Algebraic identities |
| Source items | Preprint Lemma 3.1 and Section 2.5 |
| Status | **Solved and Lean-verified** (algebraic cores) |
| Depends on the upstream theorem | No |
| Score (I/B/T/L/Lean) | 2 / 1 / 4 / 4 / 5, composite **2.6** |
| Subresults | Lean [`Separation.lean`](../lean/EthConsequences/Separation.lean) (`sum_prod_eq_sum_measurements`), [`HermiteUniqueness.lean`](../lean/EthConsequences/HermiteUniqueness.lean) (`eq_zero_of_jets_vanish`, `eq_of_jets_eq`) |

## Statements (Lean)

* Separation: $\sum_x\prod_gA_g(x_g,\mathrm{meas}(x))=\sum_y\prod_g\sum_{u:\,\mathrm{meas}_g(u)=y_g}A_g(u,y)$.
* Hermite uniqueness: two polynomials of degree $<|S|\,J$ whose difference vanishes to order $J$ at
  every node of $S$ coincide; so Taylor data recover $H$ and $H(0)$.

## Next step

Same as [ETH-B06](ETH-B06-boolean-differences.md): assemble the abstract counting theorem in
[ETH-G01](../07-formalization/ETH-G01-decouple-algebraic-core.md).

## Resource boundary

Closed; reuse.
