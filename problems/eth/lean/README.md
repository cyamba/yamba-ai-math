# EthProblems (Lean 4 + Mathlib)

Machine-checked components of the [ETH consequences program](../README.md). No `sorry`; every theorem
depends only on `propext`, `Classical.choice`, `Quot.sound` (see [verification.json](verification.json)).

| File | Problem | Main theorems |
| --- | --- | --- |
| [ParityInterpolant.lean](EthProblems/ParityInterpolant.lean) | ETH-A01, ETH-B01 | `neg_one_pow_mul_S_of_le`, `S_succ_right`, `defect_telescope`, `first_defect`, `pdf_defect_claim_false`, `no_low_degree_parity_match` |
| [HermiteUniqueness.lean](EthProblems/HermiteUniqueness.lean) | ETH-A04 | `eq_zero_of_pow_dvd_at_nodes`, `eq_of_taylor_data` |
| [BooleanDifferences.lean](EthProblems/BooleanDifferences.lean) | ETH-A06 | `mobius_powerset` |
| [DeformedSum.lean](EthProblems/DeformedSum.lean) | ETH-C05 | `prod_deform_eq_pow`, `deformed_sum_eq`, `deformed_sum_at_one` |
| [RoutingRigidity.lean](EthProblems/RoutingRigidity.lean) | ETH-B01, ETH-B03 | `hamming_ge_of_split`, `card_le_rank_of_zero_block`, `rank_one_sub_ge_card_block` |

## Build

```sh
cd problems/eth/lean
lake exe cache get          # if the Mathlib cache is reachable; otherwise lake builds the needed closure
lake build EthProblems
lake env lean PrintAxioms.lean
```

Toolchain `leanprover/lean4:v4.34.1`, Mathlib `d13f23b7` (same pin as `research/partitions/mathlib`).
Imports are kept narrow (`ForwardDiff`, `Polynomial.Roots`, `BigOperators.*`, `LinearAlgebra.Matrix.Rank`)
so a cold source build stays near 1.5 hours on 2 cores.
