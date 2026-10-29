# ETH-G01. Decouple the algebraic counting core from the Turing-machine plumbing

| Field | Value |
| --- | --- |
| Category | Formalization |
| Source items | "YMB-ETH-01: decouple the algebraic spectral core from PrimitiveMachine tape plumbing"; Lean blueprint in the source (`deformedPartitionSum_at_one`) |
| Status | **Building blocks Lean-verified; assembly open** |
| Depends on the upstream theorem | No for the algebraic theorem |
| Score (I/B/T/L/Lean) | 3 / 2 / 3 / 4 / 5, composite **3.0** |
| Subresults | Lean modules in [`lean/`](../lean/EthConsequences.lean): `BooleanDifferences`, `Separation`, `HermiteUniqueness`, `GradedCounting` |

## Task

State and prove in Lean, with Mathlib and without any machine model, the **abstract counting
theorem**: given polynomial factors $\Phi_e$, replacement forms $\vec P_{e,v}(T)$ of degree $\le R$
with $\vec P_{e,v}(0)=\delta_v$, and an $(r,\tau,D)$-design at each node $t=1,\dots,Q$ (Definition
3.1), the quantity computed by the routine of Proposition 3.4 (Taylor data by Boolean
differences, group sums after fixing measurements, Hermite recovery) equals
$\sum_{x\in\{0,1\}^n}\prod_e\Phi_e(x)$.

## Correction to the source blueprint

The source's target "#k-SAT equals a linear combination of $\mathrm{poly}(n)\,2^{O_k(n/\log n)}$
rational evaluations of low-degree deformed polynomials" has the wrong exponent and the wrong
mechanism; its warm-up `deformedPartitionSum_at_one` is the trivial $t=1$ case of the
clause-violation generating function, now `Graded.deformation_identity` (SR-08 row 3).

## Plan

1. Definitions: designs as data (groups, assignments, measurement matrices, the kernel
   condition of Definition 3.1(4) as an equality of linear forms).
2. Per node: `Separation.sum_prod_eq_sum_measurements` applied to the transformed factors with the
   formal input fixed; per Taylor order: `BooleanDifferences.boolean_differences`.
3. Recovery: `Hermite.eq_of_jets_eq`, plus a constructive interpolation (or the residue formula
   of [ETH-B04](../02-algebraic-identities/ETH-B04-hermite-weights-and-bit-lengths.md)).
4. Complexity is out of scope; a separate cost statement can count loop iterations.

## Resource boundary

Two Lean agents over one or two iterations; a reviewer checks that the formal statement matches
Proposition 3.4.
