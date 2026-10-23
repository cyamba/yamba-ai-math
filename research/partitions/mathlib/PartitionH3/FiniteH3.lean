import PartitionH3.ChromaticArrays
import PartitionH3.SurvivorAlgebra

/-!
The coloring-to-tableau identity is proved from dominant coefficients of
actual alternating polynomials. The survivor formula follows by the checked
H2 telescope and cancellation of the nonzero Vandermonde. This module first
uses an alphabet at least as large as the vertex set.
-/

open scoped BigOperators

noncomputable section

namespace PartitionH3

attribute [local instance] Classical.propDecidable

theorem chromatic_other_partition_coefficient_zero {n m : ℕ}
    (H : NaturalUnitInterval n) (hh : HeightTwo H) (hm : n ≤ m)
    (lambda : ℕ → ℕ) (hp : SignedArrays.Partition lambda)
    (hother : ∀ k, 2 * k ≤ n →
      (fun i => delta m i + lambda i.val) ≠
        (fun i => delta m i + twoColumnShape m n k i)) :
    (vandermonde m * chromatic H m).coeff
      (powerExponent (fun i => delta m i + lambda i.val)) = 0 := by
  rw [chromatic_signedArray_coefficient H hh lambda,
    natural_signed_array_cancellation H hh lambda hp m]
  apply Finset.sum_eq_zero
  intro a ha
  obtain ⟨haA, haP⟩ := Finset.mem_filter.mp ha
  obtain ⟨haS, haL⟩ := (mem_signedArrayUniverse (natLt H) (List.range n) lambda m a).mp haA
  have haF := (SignedArrays.signedArray_fixed_iff_padded (natLt H)
    (heightTwo_natLt_noThreeChain H hh) lambda hp (List.range n) a haS).mpr haP
  obtain ⟨k, hk, _, hs⟩ := fixed_signedArray_shape (natLt H)
    (heightTwo_natLt_noThreeChain H hh) (List.range n) lambda hp a haS haF
  simp only [List.length_range, haL] at hk hs
  have he : (List.range m).map lambda =
      (List.range m).map (twoColumnPartition n k) := by
    rw [hs, twoColumnPartition_range m n k hk hm]
  exfalso
  apply hother k hk
  funext i
  exact congrArg (fun t => delta m i + t) ((range_map_eq_iff _ _ m).mp he i)

theorem tableauAlternantExpansion_isAlternating {n : ℕ}
    (H : NaturalUnitInterval n) (m : ℕ) :
    IsAlternating (tableauAlternantExpansion H m) := by
  apply alternating_sum
  intro k _
  exact alternating_C_mul _ _ (alternant_isAlternating _)

theorem tableauAlternantExpansion_twoColumn_coefficient {n m : ℕ}
    (H : NaturalUnitInterval n) (hm : n ≤ m) (k : ℕ) (hk : 2 * k ≤ n) :
    (tableauAlternantExpansion H m).coeff
      (powerExponent (fun i => delta m i + twoColumnShape m n k i)) =
      tableauCoefficient H k := by
  have hkR : k ∈ Finset.range (n / 2 + 1) := by
    simp only [Finset.mem_range]
    omega
  rw [tableauAlternantExpansion, MvPolynomial.coeff_sum]
  calc
    _ = ∑ j ∈ Finset.range (n / 2 + 1),
        if j = k then tableauCoefficient H k else 0 := by
      apply Finset.sum_congr rfl
      intro j hj
      have hj' : 2 * j ≤ n := by have := Finset.mem_range.mp hj; omega
      rw [MvPolynomial.coeff_C_mul, alternant_dominant_coefficient _ _
        (twoColumnShape_strictAnti m n j) (twoColumnShape_strictAnti m n k)]
      simp only [twoColumn_exponent_eq_iff m n j k hm hj' hk]
      split_ifs with he
      · subst j
        simp
      · simp
    _ = _ := by simp [hkR]

/-- The complete actual-coloring/tableau alternant identity, with no assumed
Schur expansion, cancellation certificate or coefficient premise. -/
theorem vandermonde_mul_chromatic_eq_tableauAlternantExpansion {n m : ℕ}
    (H : NaturalUnitInterval n) (hh : HeightTwo H) (hm : n ≤ m) :
    vandermonde m * chromatic H m = tableauAlternantExpansion H m := by
  apply alternating_eq_of_dominant_coeff _ _
    (vandermonde_mul_isAlternating _ (chromatic_isSymmetric H hh))
    (tableauAlternantExpansion_isAlternating H m)
  intro gamma hg
  by_cases hex : ∃ k, 2 * k ≤ n ∧ gamma =
      (fun i => delta m i + twoColumnShape m n k i)
  · obtain ⟨k, hk, rfl⟩ := hex
    rw [chromatic_twoColumn_coefficient H hh hm k hk,
      tableauAlternantExpansion_twoColumn_coefficient H hm k hk]
  · have hegamma : (fun i => delta m i + dominantPartition gamma i.val) = gamma :=
      funext (delta_add_dominantPartition gamma hg)
    have hz := chromatic_other_partition_coefficient_zero H hh hm
      (dominantPartition gamma) (dominantPartition_partition gamma hg) (by
        intro k hk he
        exact hex ⟨k, hk, hegamma.symm.trans he⟩)
    rw [hegamma] at hz
    rw [hz, tableauAlternantExpansion, MvPolynomial.coeff_sum]
    symm
    apply Finset.sum_eq_zero
    intro k hk
    have hk' : 2 * k ≤ n := by have := Finset.mem_range.mp hk; omega
    have he : (fun i => delta m i + twoColumnShape m n k i) ≠ gamma := by
      intro he
      exact hex ⟨k, hk', he.symm⟩
    rw [MvPolynomial.coeff_C_mul, alternant_dominant_coefficient _ _
      (twoColumnShape_strictAnti m n k) hg]
    simp only [he, reduceIte, mul_zero]

theorem height_two_survivor_expansion_large_alphabet {n m : ℕ}
    (H : NaturalUnitInterval n) (hh : HeightTwo H) (hm : n ≤ m) :
    chromatic H m = survivorExpansion H m := by
  apply (vandermonde_cancel _ _).mp
  rw [vandermonde_mul_chromatic_eq_tableauAlternantExpansion H hh hm,
    vandermonde_mul_survivorExpansion H hh m hm]

end PartitionH3

#check @PartitionH3.height_two_survivor_expansion_large_alphabet
#print axioms PartitionH3.chromatic_other_partition_coefficient_zero
#print axioms PartitionH3.tableauAlternantExpansion_isAlternating
#print axioms PartitionH3.tableauAlternantExpansion_twoColumn_coefficient
#print axioms PartitionH3.vandermonde_mul_chromatic_eq_tableauAlternantExpansion
#print axioms PartitionH3.height_two_survivor_expansion_large_alphabet
