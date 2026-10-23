import PartitionH3.ArrayColorBridge
import PartitionH3.ColorCoefficients
import PartitionH3.FamilyReindex
import PartitionH3.DominantShape

/-!
The actual coloring coefficient sum is transported through the complete
array bijection and the checked involution to the original tableau families.
-/

open scoped BigOperators

noncomputable section

namespace PartitionH3

attribute [local instance] Classical.propDecidable

theorem chromatic_signedArray_coefficient {n m : ℕ} (H : NaturalUnitInterval n)
    (hh : HeightTwo H) (lambda : ℕ → ℕ) :
    (vandermonde m * chromatic H m).coeff
      (powerExponent (fun i => delta m i + lambda i.val)) =
      ∑ a ∈ signedArrayUniverse (natLt H) (List.range n) lambda m,
        signedArrayWeight (natLt H) a := by
  rw [vandermonde_chromatic_coefficient H hh (fun i => lambda i.val),
    signedArray_sum_reindex H lambda m]
  simp only [signedColorUniverse, Finset.sum_filter, Fintype.sum_prod_type,
    signedArrayWeight, colorArray_sign, colorArray_inversions, colorDegree]
  apply Finset.sum_congr rfl
  intro sigma _
  apply Finset.sum_congr rfl
  intro κ _
  by_cases h : Proper H κ ∧ ∀ i, ((colorClass κ i).card : ℤ) =
      (lambda (sigma i).val : ℤ) - (sigma i).val + i.val <;> simp [h]

theorem chromatic_twoColumn_coefficient {n m : ℕ} (H : NaturalUnitInterval n)
    (hh : HeightTwo H) (hm : n ≤ m) (k : ℕ) (hk : 2 * k ≤ n) :
    (vandermonde m * chromatic H m).coeff
      (powerExponent (fun i => delta m i + twoColumnShape m n k i)) =
      tableauCoefficient H k := by
  let shape := CornerSlide.twoColumnShape k (n - 2 * k)
  let pad := m - (n - k)
  have hslen : shape.length = n - k := by
    simp only [shape, CornerSlide.twoColumnShape, List.length_append, List.length_replicate]
    omega
  have htotal : shape.length + pad = m := by dsimp [pad]; omega
  have hpos : ∀ d ∈ shape, 0 < d := by
    intro d hd
    simp only [shape, CornerSlide.twoColumnShape, List.mem_append,
      List.mem_replicate] at hd
    rcases hd with ⟨_, rfl⟩ | ⟨_, rfl⟩ <;> omega
  have hshape : (List.range (shape.length + pad)).map (twoColumnPartition n k) =
      shape ++ List.replicate pad 0 := by
    rw [htotal]
    exact twoColumnPartition_range m n k hk hm
  have he := signedArray_sum_eq_complete_family (natLt H)
    (heightTwo_natLt_noThreeChain H hh) (List.range n) shape hpos
    (twoColumnPartition n k) (twoColumnPartition_partition n k) pad hshape
  rw [htotal] at he
  change (vandermonde m * chromatic H m).coeff
    (powerExponent (fun i => delta m i + twoColumnPartition n k i.val)) = _
  rw [chromatic_signedArray_coefficient H hh (twoColumnPartition n k), he]
  simp only [tableauCoefficient, CornerSlide.columnFamily, List.length_range, hk,
    reduceIte, tableauWeight, shape]

end PartitionH3

#check @PartitionH3.chromatic_signedArray_coefficient
#check @PartitionH3.chromatic_twoColumn_coefficient
#print axioms PartitionH3.chromatic_signedArray_coefficient
#print axioms PartitionH3.chromatic_twoColumn_coefficient
