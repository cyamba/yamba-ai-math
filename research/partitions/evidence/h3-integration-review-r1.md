# P009 integration review, round 1

Date: 2026-10-23. Separate critic; first P009 challenge, 2 dispatch proxy units. No nested agents, dependency provisioning, proof edits, or new review of the frozen P007/P008/P010/P011 contracts.

## Verdict and exact scope

**Supported (proved, Lean-checked):** the actual finite height-two identity over `MvPolynomial (Fin r) (Polynomial Int)`, for every `n` and `r`, including zero:

```lean
PartitionH3.height_two_survivor_expansion :
  ∀ {n : Nat} (H : NaturalUnitInterval n), HeightTwo H →
  ∀ r : Nat,
    chromatic H r =
      ∑ k ∈ Finset.range (n / 2 + 1),
        MvPolynomial.C (survivorCoefficient H k) *
          elementary r (n - k) * elementary r k
```

Here `chromatic` is the actual finite sum over proper colorings, weighted by `q ^ ascents`; `elementary` is the actual elementary symmetric polynomial. `survivorCoefficient` sums the original `CornerSlide.survivorFamily` with its original `tableauGraphInversions` weight. The survivor family is the full-image complement in the complete original family, not a newly chosen representative set. No expansion, coefficient identity, bijection, sign compatibility, or positivity premise is supplied to this final declaration.

No mathematical defect was found in the ten frozen integration modules. The theorem is height two only. This review makes no claim of new mathematical novelty, general height, or performance improvement.

## Independent check and source binding

I inspected all ten modules, their actual definitions and principal declarations, and the author packet. I independently ran, sequentially and without provisioning:

```text
working directory: research/partitions/mathlib
/Users/christopheryamba/.elan/bin/lake env lean PartitionH3/H3.lean
login: false
exit: 0
```

The command printed the all-`n`, all-`r` declaration above and its axiom report:

```text
[propext, Classical.choice, Quot.sound]
```

There were no diagnostics. This direct check used the installed pinned dependency/import products; it is not an independent clean rebuild of the entire dependency graph. Root's combined clean source-bound verification remains separate. No finite experimental checks are being promoted to proof evidence.

All ten independently computed source SHA-256 values matched the frozen packet. The packet inspected was `evidence/h3-integration-r1.md`, SHA-256 `35c5f1007806d179a9850069fe1c6bc0eaf54d1e389e8e8d6bd7792a055ed251`.

| Module under `mathlib/PartitionH3/` | Reviewed SHA-256 |
| --- | --- |
| `PermutationSign.lean` | `ba1fa025a7aad3463491e1b4a08c69964cbfc95aff5a9d08ecf5616f4a069a7c` |
| `ArrayColorBridge.lean` | `bfebc6af39a6dbb4143f4621547262778c57f61a7af9b921e7375dbc44a39f34` |
| `FamilyPadding.lean` | `161e68118d5e3770d6b9a60e61213c796972027db749bce18e32c2100c4e60fb` |
| `FamilyReindex.lean` | `ddece994fc969905a3740d1a633186d927d7a833151b14f4d77049d6807d16d7` |
| `SurvivorAlgebra.lean` | `686ee1886a1d0432f6effd7d3103f97e4834c81407a605c723ba40592e73f27e` |
| `DominantShape.lean` | `8f81190b0937831eb47574d7d95dcc419e388804b52d7b0b81e2a02a7e9bdd62` |
| `ChromaticArrays.lean` | `b9e364b07c43c0a1d59c680e09fb442b35d52ea651b086d68395fb2d1707bf80` |
| `FiniteH3.lean` | `00a70cca54ed12927c227fedec97749ef59e06b0c3093c262ae49d4d6edfed91` |
| `AlphabetSpecialization.lean` | `d02a5715c43282624a64801bd80724c3bbabd2fc4f231c2ed58feeeb16e5cee9` |
| `H3.lean` | `c9ba9bc8ae3ce300648594278a63f56aadb6af349ea9ba659a0a8b2e11cef7c1` |

## Semantic findings

1. **Actual colorings, arrays, signs and statistics are connected.** `colorArray` has exactly `m` rows, including empty color classes, with sorted actual vertex contents. `arrayColor`, `arrayPermutation`, `array_row_canonical` and `colorArray_inverse` recover every signed array in the complete finite universe. `colorArray_injective`, `signedColorUniverse_image` and `signedArray_sum_reindex` account for both directions and multiplicities. `permutationSign_permutationLabels` proves equality of the original list inversion-parity sign and the library permutation sign by actual adjacent position swaps. `colorArray_signed_iff` uses the integer shape equation with the forward permutation. `colorArray_inversions` identifies the original list graph inversion statistic with **descents** of the coloring; the preceding coefficient theorem's ascent-to-descent reversal/symmetry supplies the required direction. Increasing color rows and decreasing numeric endpoints are consistent, including the two-vertex edge witness with colors `(1,0)`, whose descent and row inversion are both one.

2. **Padding identifies the complete original family.** `padded_rows_iff_complete_family` relates a padded fixed array to membership of its prefix in the actual `CornerSlide.family`, with positive body row lengths and exactly the stated trailing zero lengths. It does not assume a preferred enumeration. `paddedSignedArrays_eq_image` recovers the identity labels, full length profile and unique padded body. `signedArray_sum_eq_complete_family` uses padding injectivity, original family nodup, and `tableauGraphInversions_padding`, so neither list multiplicity nor a weight is lost. Empty body shapes and empty rows are admitted where appropriate.

3. **Dominant classification supplies the missing zero coefficients.** `dominant_ge_delta` justifies the natural subtraction in `dominantPartition`; its global partition property includes the transition to zero beyond the alphabet. `fixed_signedArray_shape` uses height two to bound actual chain rows by two and the original filling permutation to establish the total size. `partition_range_three_blocks` then supplies the two/one/zero profile and its bounds. `twoColumn_exponent_eq_iff` prevents duplicate summands. Thus `chromatic_other_partition_coefficient_zero` follows from cancellation of the actual universe, rather than an unproved assertion that only two-column shapes occur. `chromatic_twoColumn_coefficient` uses the exact padded complete family and the original `columnFamily` range condition.

4. **The polynomial lift and alternant reconstruction close the large-alphabet identity.** `tableauWeight_coefficient` identifies each actual polynomial coefficient with the original degree count. `tableauCoefficient_eq_next_add_survivor` lifts H2 coefficientwise, and `survivorCoefficient_eq_sub` takes the difference in `Int[q]`. `tableauCoefficient_after_last` supplies the terminal zero, including `n=0`. `sum_differences_mul_prefix` performs the finite telescope after the actual two-elementary alternant identity. `vandermonde_mul_chromatic_eq_tableauAlternantExpansion` checks all strictly decreasing coefficients using the proved reconstruction/extensionality result and the actual dominant partition above. `height_two_survivor_expansion_large_alphabet` cancels the proved nonzero Vandermonde. None of these steps substitutes a formal symbol for the chromatic polynomial or its families.

5. **Alphabet specialization removes the large-alphabet bound.** `specialize_chromatic` reindexes surviving colorings by the injective lift from `Fin r`; any coloring outside that image has an actual forbidden-color factor sent to zero. `specialize_elementary` does the analogous exact subset-image reindex, with cardinalities preserved and all excluded products zero. Constants, weights and elementary products specialize correctly. Applying this map from `max n r` proves the final theorem for every `r`. The proof includes `r=0`, `n=0`, and `n=r=0`; no positive-alphabet premise is hidden. For the last case the empty coloring, empty tableau and degree-zero elementary factors survive with weight one. These boundary observations trace the universal proof, not a separate finite-test certification.

## Remaining obligations and limits

- **Nat-coefficient transport is not a declaration in this packet.** The exact supported theorem is over `Z[q]`. The earlier bridge plan also requested transfer to natural coefficients by an injective coefficient map. If that remains a formal acceptance requirement, add an actual `Nat[q]` restatement and prove its image is this formula; do not describe such a Lean theorem as already checked. This does not undermine the stated `Z[q]` theorem, whose displayed coefficients are actual sums of nonnegative monomials.
- The independent direct final check passed; the clean combined build/source-bound verification, final exposition and repository acceptance checks are root's remaining verification work. A future source change requires corresponding updated evidence.
- This is a separate critic role, not evidence of independent model errors. The author's usage-limit failure and root's retained/corrected continuation remain recorded in the candidate packet and counted. No failure was erased by this review.

There is no counterexample or repair request against the exact frozen all-alphabet `Z[q]` statement. The natural-coefficient restatement and clean combined verification are explicit scope/assurance qualifications, not premises silently added to the theorem.
