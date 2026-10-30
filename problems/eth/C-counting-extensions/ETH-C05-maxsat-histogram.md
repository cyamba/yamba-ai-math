---
id: ETH-C05
source: YMB-ETH-07 ("Polynomial-space Max-3-SAT via the algebraic certificate")
category: counting-extensions
status: identity proved in Lean; bounded-density algorithm sketched
---

# ETH-C05: Max-SAT histogram via the deformed partition function

## Identity (proved, Lean)

For 0/1 clause indicators `Phi_C(x)`:
`prod_C (1 + t (Phi_C(x) - 1)) = (1 - t)^{u(x)}`, `u(x)` = number of violated clauses, so
`Z_F(t) = sum_x prod_C (1 + t(Phi_C(x) - 1)) = sum_j h_j (1 - t)^j` and `Z_F(1) = #F`.
Lean: `EthProblems.DeformedSum.prod_deform_eq_pow`, `deformed_sum_eq`, `deformed_sum_at_one`
([DeformedSum.lean](../lean/EthProblems/DeformedSum.lean)).

## Algorithm for bounded density (proof sketch)

Assume `m <= Dn`. Convert each clause to a 3-CNF OR-chain whose output variable `z_e` equals the clause value;
gate variables are determined by `x`. The factor `1 + t(z_e - 1)` reads one variable. Copy variables to
bounded occurrence (`O_k(Dn)` variables). The interpolation algorithm computes the weighted sum at
`m + 1` rational points `t`; Vandermonde inversion gives every `h_j`. Time `2^{O_{k,D}(rho(n))}`, polynomial
space. This gives exact Max-k-SAT for linear-size formulas, strengthening Cor. 1.1 in that regime.

Note the sheet says "using the 378 spectral block algorithm ... with polynomial overhead": the deformation here
deforms clause *values*, the paper deforms clause *inputs*; the two compose (evaluate the paper's `H` with
these weighted factors).

## Open

Dense case: [ETH-C03](ETH-C03-dense-exact-maxsat.md).
