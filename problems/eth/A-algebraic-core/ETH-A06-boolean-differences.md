---
id: ETH-A06
source: preprint Lemma "boolean-differences" (Sec. 3.3) and Sec. 2.4 inclusion-exclusion
category: algebraic-core
status: solved (Lean)
---

# ETH-A06: Boolean differences (Mobius inversion on the Boolean lattice)

## Statement

If `F(U) = sum_{T subset U} a(T)` for all `U` (values of a multilinear polynomial at indicator vectors
`1_U`), then `a(E) = sum_{U subset E} (-1)^{|E| + |U|} F(U)`.

## Result

**Proved, Lean**: `EthProblems.BooleanDifferences.mobius_powerset` for any commutative ring, by induction on
`E` with `Finset.sum_powerset_insert`. File: [BooleanDifferences.lean](../lean/EthProblems/BooleanDifferences.lean).

## Use in the algorithm

The preprint's identity (2.x): `H(t+z) = sum_{|E| <= q} sum_{U subset E} (-1)^{|E|-|U|} Z_{t,E,U}(z) mod z^J`
is this inversion applied to each coefficient `a_E(x, z)` and summed over `x` with `x_E = 1`.

## Next step

Formalise the full identity (2.x) for truncated polynomial rings `Polynomial K / (X^J)`; this is the last
algebraic step needed for a sorry-free "algebraic core" ([ETH-A07](ETH-A07-algebraic-core-decoupling.md)).
