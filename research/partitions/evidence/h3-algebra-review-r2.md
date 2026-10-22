# P007 round 2: actual polynomial ingredients

Reviewed 2026-10-22 by `/root/h3_semantic_critic`, a separate reviewer role
from author `/root/h3_lean_algebra` and continuing author `/root`. This is the
second and final substantive P007 algebra challenge. It does not reopen the
completed P008 signed-array reviews. Distinct roles do not establish
independent errors or different models. The critic edited no proof source.

**Verdict: supported for the checked interfaces below; P007 and H3 remain
incomplete.** The generic alternant-product gate has an actual checked
polynomial theorem. No logical defect was found in the reviewed declarations.
The explanatory color-row orientation error found during this challenge was
corrected within the same round; its smallest counterexample is retained below.

## Frozen sources and assurance

The review inspected [the revision handoff](h3-algebra-revision-r1.md), all
five source files, and the exact statement inventory and hash map in
[`../mathlib/verification.json`](../mathlib/verification.json).

| Source under `../mathlib/PartitionH3/` | Reviewed SHA-256 |
| --- | --- |
| `Foundations.lean` | `875a7c0afbcb534e069353c93da9825758023bcc0a3d1891399008a99823562b` |
| `Coloring.lean` | `dc415218fa4d625d96a711469d11aadf016437a6dd1a79c7337e21422dc12235` |
| `Alternant.lean` | `f903afbdd32b36e2c83dcfdc3bc86654305431da74569de1e8895ca65a6a4caf` |
| `Vandermonde.lean` | `450de9316322b90674611407fc4cd8d8654ec79e5b74b7df702d56e6f87f30f8` |
| `SubsetBridge.lean` | `6acac3a84779ea950c566406b0f71be9a908fb31a9f3256fe50cecbbb5b27deb` |

The configured toolchain is Lean 4.34.1 with Mathlib pinned to
`d13f23b723b8a846827a245b89c10fc7d3f11612`. The critic independently ran
`lake env lean` on each of these five files using existing dependencies.
All five checks exited zero without diagnostics, printing the stated exact
types and all 28 principal dependency reports. Reports contained only
`propext`, `Quot.sound`, and, where needed, `Classical.choice`.
This independently checks the sources with existing imported products; it
does not constitute a second fresh-project build. The lead's separate
source-bound record reports a fresh temporary project build with only pinned
dependency products reused. The critic did not repeat provisioning, measure
the provisioning resource receipt, or perform finite numerical experiments.
The initial coloring snapshot was
`c4972fff520a90de2871ed62d817e5fde0396bb937195a51ecd92a98b2048f30`;
the table pins the final comment correction. The critic inspected the
corrected wording and repeated the direct coloring check successfully. The
lead is refreshing the source-bound record for that final hash separately.

## Findings and precise supported scope

1. **Supported: actual generic alternant multiplication and action.**
   `Poly m` is exactly `MvPolynomial (Fin m) (Polynomial Int)`.
   `alternant_eq_sum` identifies `alternant gamma` with the actual signed
   sum of `product_i X_(sigma i)^(gamma i)` over `Equiv.Perm (Fin m)`.
   `signCoeff` is the library permutation sign cast into that ring, not an
   arbitrary sign witness. `rename_perm_mul` uses the action
   `rename sigma (rename tau p) = rename (sigma * tau) p`; right composition
   with the swap therefore has the required orientation. The main checked
   interface is exactly

   ```lean
   alternant_mul_elementary {m : Nat} (gamma : Fin m → Nat) (b : Nat) :
     alternant gamma * elementary m b =
       ∑ T ∈ (Finset.univ : Finset (Fin m)).powersetCard b,
         alternant (bump gamma T)
   ```

   It has no bound on `b`, coloring-expansion premise, or positivity
   assumption. `elementary` is the actual subset-defined Mathlib `esymm`;
   its symmetry, finite distribution, and the `rename` action provide the
   required reindexing. This closes the corresponding missing generic
   polynomial ingredient from round 1.

2. **Supported: repeated-exponent vanishing in the concrete ring.**
   `alternant_eq_zero_of_eq` assumes distinct `p,q : Fin m` and
   `gamma p = gamma q`, and concludes the actual alternant is zero.
   The proof first obtains `A = -A` by right-swapped antisymmetrization.
   It then derives `2*A=0`, uses the ring's no-zero-divisors instance, and
   rules out `2=0` by applying the multivariate constant coefficient and
   then the univariate constant coefficient, reducing to integers.
   This step is valid for the specified domain. It does not purport to
   prove the same implication in an arbitrary ring with 2-torsion.

3. **Supported: exact Vandermonde coefficient and cancellation, including
   zero variables.** `rename_powerMonomial` correctly uses
   `gamma (sigma.symm i)` in the exponent at coordinate `i`.
   `delta_cast` proves that the natural expression `m-1-i.val` equals the
   intended integer expression on `Fin m`; `delta_injective` is valid also
   for the empty domain. `coeff_signed_delta` proves that the coefficient
   at `powerExponent (delta m)` is one exactly for `sigma=1`, and zero
   otherwise. Consequently `vandermonde_delta_coefficient m = 1` at that
   coefficient, `vandermonde_ne_zero m`, and

   ```lean
   vandermonde_cancel {m : Nat} (p q : Poly m) :
     vandermonde m * p = vandermonde m * q ↔ p = q
   ```

   are unconditional checked statements. `vandermonde_empty` proves
   `vandermonde 0 = 1`. No unproved product-factorization formula or desired
   expansion is being used to establish nonzero cancellation.

4. **Supported subset bridge; specialization/reconstruction still absent.**
   `subsetBits` records membership on all `Fin m`; the two inverse lemmas
   prove an actual bijection with length-`m` Boolean lists. The length
   hypothesis on `subsetBits_fromBits` prevents truncation from being
   mistaken for an inverse on arbitrary lists. `subsetBits_ones` proves
   actual cardinality, and `twoBlockSubset_classification` requires exactly
   `b<=a`, `a+b<=m`, and `T.card=b`. Its conclusion is the existence of a
   unique `j<=b` with `T=twoBlockSubset m a b j`; feasibility/cardinality
   are checked and include the empty case. This is not yet the polynomial
   two-elementary identity: the no-rise predicate still needs to be linked
   to the actual bumped natural exponents and the finite sum reduced to
   those surviving indices. Dominant-coefficient reconstruction remains
   absent as well. Those are remaining P007 blockers, not hypotheses of
   the completed generic theorem.

5. **Coloring preliminaries supported; row-orientation wording corrected.**
   `chromatic` sums actual proper functions `Fin n → Fin m`, with actual
   color monomials and ascent powers. The two family coefficients refer to
   the original complete column family and full-image survivor complement.
   No equality of these coefficients with `chromatic` is assumed.
   `same_color_comparable` has the actual properness and increasing-vertex
   hypotheses; `colorClass_card_le_two` additionally assumes `HeightTwo`.
   Reversal is involutive, preserves properness, and interchanges the
   actual ascent/descent counts. `descents_eq_colorRowInversions` proves
   equality with the defined finite-pair statistic and does not assume
   properness or height. The definition matches **increasing color rows**,
   as its immediate source comment says. The initial module header and
   revision handoff instead said **descending color rows**. That wording was
   false: take `n=m=2`, `h(0)=h(1)=1`, and colors `(1,0)`. There is one
   descent; increasing color rows give word `[1,0]` with one graph
   inversion, while descending color rows give `[0,1]` with none. The lead
   corrected the header to increasing color rows and the handoff to
   increasing color rows / descending colors on ordered vertex pairs.
   The critic inspected this correction within the same challenge; the
   checked definition/theorem required no repair. This does not supply the
   still-missing equivalence to the original list-array statistic.

## Remaining integration and accounting

P007 still needs the two-elementary specialization and reconstruction.
Adjacent-color symmetry, actual coloring/list-array bijections, complete
signed-sector finite-sum cancellation, list-permutation/library-sign
translation, and the canonical padding/family bijection remain P008/H3
dependencies. The final survivor equality, specialization to arbitrary
alphabet size and natural-coefficient transfer are not established by this
review. P009 cannot treat the whole P007/P008 prerequisites as complete.
No general positivity, H3 completion, external-source novelty, or independent
model claim follows from these checked ingredients.

This bounded challenge added 2 declared proxy units to the reported P007
account of 11, giving 13. The lead applied the orientation wording repair
under the final 3-unit allowance, bringing the account to **16 of 16**.
These units are neither tokens nor money. Inspection of that correction
belongs to this same round; no third algebra challenge or third signed-array
review is claimed here.
