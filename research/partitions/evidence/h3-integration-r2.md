# P009 integration revision, round 2

Date: 2026-10-23. Root author revision, 3 dispatch proxy units; P009 before final review is 11/16. No nested agents or provisioning. The ten integration modules in the round-1 packet are unchanged.

## Exact additional result

`PartitionH3.height_two_survivor_expansion_nat` is the same all-vertex/all-alphabet survivor identity in `MvPolynomial (Fin r) (Polynomial Nat)`. Its chromatic, elementary and tableau polynomials are defined directly by the original actual finite sums; they are not arbitrarily chosen preimages. The coefficient ring map is induced by the natural-to-integer coefficient embedding through the polynomial/Finsupp equivalences already imported. Injectivity at both polynomial levels and identification of the actual sums transport the checked signed-ring equality back to the natural semiring. The height-two hypothesis is unchanged; zero vertices and zero colors remain included.

Source: `research/partitions/mathlib/PartitionH3/NaturalCoefficients.lean`
SHA-256: `7128f7dda5761411ede8ce2ba18894213a9c690606ad0748c6a5e9bb96f8a916`

## Direct check actually performed

Working directory: `research/partitions/mathlib`. Command: `/Users/christopheryamba/.elan/bin/lake env lean PartitionH3/NaturalCoefficients.lean`, login false, exit 0.

```text
@PartitionH3.height_two_survivor_expansion_nat : ∀ {n : ℕ} (H : PartitionH3.NaturalUnitInterval n),
  PartitionH3.HeightTwo H →
    ∀ (r : ℕ),
      PartitionH3.natChromatic H r =
        ∑ k ∈ Finset.range (n / 2 + 1),
          MvPolynomial.C (PartitionH3.natSurvivorCoefficient H k) * PartitionH3.natElementary r (n - k) *
            PartitionH3.natElementary r k
'PartitionH3.coefficientCast_injective' depends on axioms: [propext, Classical.choice, Quot.sound]
'PartitionH3.naturalCast_injective' depends on axioms: [propext, Classical.choice, Quot.sound]
'PartitionH3.naturalCast_colorMonomial' depends on axioms: [propext, Classical.choice, Quot.sound]
'PartitionH3.naturalCast_chromatic' depends on axioms: [propext, Classical.choice, Quot.sound]
'PartitionH3.naturalCast_elementary' depends on axioms: [propext, Classical.choice, Quot.sound]
'PartitionH3.coefficientCast_tableauWeight' depends on axioms: [propext, Classical.choice, Quot.sound]
'PartitionH3.coefficientCast_survivorCoefficient' depends on axioms: [propext, Classical.choice, Quot.sound]
'PartitionH3.height_two_survivor_expansion_nat' depends on axioms: [propext, Classical.choice, Quot.sound]
```

The preceding existing dependency build `lake --no-cache --wfail build PartitionH3.H3` exited 0. An initial direct auxiliary check failed because the H3 object had not yet been built. The first implementation then failed on unavailable polynomial-map API declarations and an explicit-argument mismatch; the next failed on a reflexivity goal and that argument mismatch. These failed checks were not accepted. The retained version uses only already installed imports, coefficient extensionality and direct subset-sum mapping; the final direct check above has no diagnostics and all eight principal reports use only standard axioms.

## Review and acceptance boundary

Review the eight printed auxiliary declarations, their actual definitions, coefficient-map injectivity and absence of extra premises. Preserve the round-1 `Int[q]` verdict and its frozen hashes; this new module closes the explicitly retained natural-coefficient transport item if supported. Root still owes fresh source-bound builds of the original five-module Std project and the full twenty-one-module Mathlib project (137 principal reports), all repository checks, final in-place article compilation and PR integration. No general-height, new theorem priority, provider execution or workflow-quality claim follows.
