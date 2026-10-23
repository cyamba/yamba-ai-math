# P009 integration review, round 2

Date: 2026-10-23. Separate critic; second and final P009 challenge, 2 dispatch proxy units, account 13/16 after dispatch. No nested agents, provisioning, proof/configuration edits, or renewed review of the earlier frozen contracts.

## Verdict

**Supported (proved, Lean-checked):** `PartitionH3.height_two_survivor_expansion_nat` proves the actual all-vertex, all-alphabet survivor identity in `MvPolynomial (Fin r) (Polynomial Nat)`:

```lean
∀ {n : Nat} (H : NaturalUnitInterval n), HeightTwo H →
  ∀ r : Nat,
    natChromatic H r =
      ∑ k ∈ Finset.range (n / 2 + 1),
        MvPolynomial.C (natSurvivorCoefficient H k) *
          natElementary r (n - k) * natElementary r k
```

There are no added expansion, positivity, alphabet-size, or nonemptiness premises. Both zero vertices and zero colors are included. No semantic defect or counterexample was found in the new module. This closes the separately unproved natural-coefficient transport item recorded in the round-1 review. It preserves that review's supported `Z[q]` theorem; it does not retrospectively claim that the natural restatement existed in the round-1 packet.

## Source binding and independent check

I read the frozen author packet and the complete new source, compared its definitions with the integer definitions in `Foundations.lean`, and independently computed these SHA-256 values:

| Artifact | Reviewed SHA-256 |
| --- | --- |
| `mathlib/PartitionH3/NaturalCoefficients.lean` | `7128f7dda5761411ede8ce2ba18894213a9c690606ad0748c6a5e9bb96f8a916` |
| `evidence/h3-integration-r2.md` | `982273c695693e55e707899648dfcd0bd75a7ba3e28607b6a00c34e5248137a4` |

All ten round-1 integration source hashes were recomputed and still match the frozen round-1 packet and the exact values in `h3-integration-review-r1.md`: `PermutationSign`, `ArrayColorBridge`, `FamilyPadding`, `FamilyReindex`, `SurvivorAlgebra`, `DominantShape`, `ChromaticArrays`, `FiniteH3`, `AlphabetSpecialization`, and `H3`. Their prior verdict is preserved; this was a hash check, not an extra substantive review round.

I independently ran one direct Lean check, using the existing installed imports:

```text
working directory: research/partitions/mathlib
/Users/christopheryamba/.elan/bin/lake env lean PartitionH3/NaturalCoefficients.lean
login: false
exit: 0
```

It printed the universal final signature above, no diagnostics, and exactly the following eight principal axiom reports, each limited to `[propext, Classical.choice, Quot.sound]`:

- `coefficientCast_injective`
- `naturalCast_injective`
- `naturalCast_colorMonomial`
- `naturalCast_chromatic`
- `naturalCast_elementary`
- `coefficientCast_tableauWeight`
- `coefficientCast_survivorCoefficient`
- `height_two_survivor_expansion_nat`

This is a successful independent direct check with compiled imports, not an independent clean rebuild of the whole project. Root retains responsibility for the fresh source-bound complete builds and acceptance checks.

## Semantic findings

1. **The coefficient map is the actual natural-to-integer embedding.** `coefficientCast` passes through the polynomial/Finsupp equivalences and `AddMonoidAlgebra.mapRingHom` induced by `Nat.castRingHom Int`. Its injectivity proof applies polynomial coefficient extensionality, reduces equality at every degree to equality of natural coefficients cast into integers, then uses `Nat.cast_injective`. This is not an assumed injective map. `coefficientCast_X` separately verifies the polynomial variable's image.

2. **Injectivity is transported through the outer polynomial layer.** `naturalCast r` is `MvPolynomial.map coefficientCast`; `naturalCast_injective` uses the checked coefficient-map injectivity. Thus equality of the actual natural multivariate polynomials follows from equality of their integer images, without choosing arbitrary preimages or using subtraction in a natural semiring.

3. **The natural objects are actual combinatorial sums.** `natColorMonomial` is the product of the actual coloring variables. `natChromatic` sums over every actual `Fin n → Fin r` coloring, filters by the same `Proper`, and uses the same `ascents` exponent. `natElementary` is the actual library elementary symmetric polynomial. `natTableauWeight` is the original list sum of `q ^ tableauGraphInversions`; `natSurvivorCoefficient` uses the same original `CornerSlide.survivorFamily (natLt H) (List.range n) k`. No change to family membership, list multiplicities, statistic, or coefficient sign is hidden by the transport.

4. **All image identities are proved for those sums.** `naturalCast_colorMonomial`, `naturalCast_chromatic` and `naturalCast_elementary` map products, proper-coloring branches and elementary subset sums to their actual integer counterparts. `coefficientCast_tableauWeight` inducts on the actual list, preserving each summand, and supplies `coefficientCast_survivorCoefficient` directly. These lemmas do not require height two and introduce no additional hypotheses.

5. **The final theorem discharges transport rather than assuming it.** After applying `naturalCast_injective r`, the proof maps both finite sides termwise using those image identities and invokes the already proved `height_two_survivor_expansion H hh r`. Its only mathematical hypothesis beyond `H`'s natural unit interval structure remains `HeightTwo H`. Empty products, empty coloring domains/codomains, degree-zero elementary factors and empty tableau lists are handled by the same actual sum definitions; there is no `0 < n`, `0 < r` or `n ≤ r` restriction.

## Failure accounting and limits

The author packet retains the initial auxiliary check that failed because the `H3` object was not yet built, the first implementation's unavailable map-API and explicit-argument failures, and the following reflexivity/argument failures. Those were author-reported failed checks, not successes or independent checks performed by this critic. The accepted frozen source is the version whose independent direct check above exited zero. The earlier specialist usage-limit failure remains in the round-1 record; this revision does not erase it or reset the account.

The natural-ring auxiliary qualification from round 1 is now closed for the displayed finite theorem. Fresh clean combined verification, repository checks, article compilation and PR integration remain outside this review's check receipt and are assigned to root. No general-height extension, new mathematical priority, independent-model assurance, performance result or provider execution follows from this result.
