import PartitionH3.FamilyPadding

/-!
The finite fixed-array sum is reindexed onto the original complete tableau
family. Labels, zero-length padding, multiplicities and inversion weights
are all retained in this bijection.
-/

open scoped BigOperators

noncomputable section

namespace PartitionH3

attribute [local instance] Classical.propDecidable

theorem paddedIdentityArray_mem (r : ℕ → ℕ → Prop) (vertices shape : List ℕ)
    (lambda : ℕ → ℕ) (pad : ℕ)
    (hshape : (List.range (shape.length + pad)).map lambda =
      shape ++ List.replicate pad 0)
    (body : CornerSlide.Rows) (hb : body ∈ CornerSlide.family r vertices shape) :
    paddedIdentityArray pad body ∈
      (signedArrayUniverse r vertices lambda (shape.length + pad)).filter
        (fun a => SignedArrays.PaddedTableau r vertices (SignedArrays.rows a)) := by
  classical
  obtain ⟨ht, hs⟩ := (CornerSlide.mem_family r vertices shape body).mp hb
  have hbl : body.length = shape.length := by
    have he := congrArg List.length hs
    simpa only [List.length_map] using he
  have hlen : (body ++ List.replicate pad []).length = shape.length + pad := by
    simp [hbl]
  apply Finset.mem_filter.mpr
  constructor
  · apply (mem_signedArrayUniverse r vertices lambda _ _).mpr
    constructor
    · apply identityArray_signed
      · exact ht.1
      · simpa only [SignedArrays.flatten_padding] using ht.2.1
      · intro row hr
        rcases List.mem_append.mp hr with hr | hr
        · exact (ht.2.2.1 row hr).2
        · have he : row = [] := (List.mem_replicate.mp hr).2
          simp [he]
      · rw [List.map_append, List.map_replicate, hs, hlen, hshape]
        rfl
    · simpa only [paddedIdentityArray, identityArrayAt_length] using hlen
  · rw [paddedIdentityArray, identityArrayAt_rows]
    exact ⟨body, pad, rfl, ht⟩

theorem paddedSignedArrays_eq_image (r : ℕ → ℕ → Prop) [DecidableRel r]
    (height : CornerSlide.NoThreeChain r) (vertices shape : List ℕ)
    (hpos : ∀ d ∈ shape, 0 < d) (lambda : ℕ → ℕ)
    (hp : SignedArrays.Partition lambda) (pad : ℕ)
    (hshape : (List.range (shape.length + pad)).map lambda =
      shape ++ List.replicate pad 0) :
    (signedArrayUniverse r vertices lambda (shape.length + pad)).filter
        (fun a => SignedArrays.PaddedTableau r vertices (SignedArrays.rows a)) =
      (CornerSlide.family r vertices shape).toFinset.image (paddedIdentityArray pad) := by
  classical
  ext a
  constructor
  · intro ha
    obtain ⟨haA, haP⟩ := Finset.mem_filter.mp ha
    obtain ⟨haS, haL⟩ := (mem_signedArrayUniverse r vertices lambda _ a).mp haA
    have haF := (SignedArrays.signedArray_fixed_iff_padded r height lambda hp vertices
      a haS).mpr haP
    have hlabels := SignedArrays.fixed_labels_identity r height lambda hp vertices a haS haF
    have hlengths := SignedArrays.fixed_row_lengths r height lambda hp vertices a haS haF
    rw [haL, hshape] at hlengths
    have hb := (padded_rows_iff_complete_family r vertices shape hpos
      (SignedArrays.rows a) pad hlengths).mp haP
    have he := (rows_padding_decomposition (SignedArrays.rows a) shape pad hlengths).1
    apply Finset.mem_image.mpr
    refine ⟨(SignedArrays.rows a).take shape.length, List.mem_toFinset.mpr hb, ?_⟩
    have haI := array_eq_identity_of_labels a hlabels
    rw [he] at haI
    exact haI.symm
  · rintro ha
    obtain ⟨body, hb, rfl⟩ := Finset.mem_image.mp ha
    exact paddedIdentityArray_mem r vertices shape lambda pad hshape body
      (List.mem_toFinset.mp hb)

theorem sum_toFinset_map {α M : Type*} [DecidableEq α] [AddCommMonoid M]
    (f : α → M) (xs : List α) (hn : xs.Nodup) :
    (xs.map f).sum = ∑ x ∈ xs.toFinset, f x := by
  induction xs with
  | nil => simp
  | cons x xs ih =>
    have hh := List.nodup_cons.mp hn
    simp [hh.1, ih hh.2]

/-- Exact weighted identification with every member of the existing family.
The explicit shape condition includes every padded zero row. -/
theorem signedArray_sum_eq_complete_family (r : ℕ → ℕ → Prop) [DecidableRel r]
    (height : CornerSlide.NoThreeChain r) (vertices shape : List ℕ)
    (hpos : ∀ d ∈ shape, 0 < d) (lambda : ℕ → ℕ)
    (hp : SignedArrays.Partition lambda) (pad : ℕ)
    (hshape : (List.range (shape.length + pad)).map lambda =
      shape ++ List.replicate pad 0) :
    (∑ a ∈ signedArrayUniverse r vertices lambda (shape.length + pad),
      signedArrayWeight r a) =
    ((CornerSlide.family r vertices shape).map
      (fun body => (Polynomial.X : Coeff) ^ CornerSlide.tableauGraphInversions r body)).sum := by
  classical
  rw [signedArray_universe_cancellation r height vertices lambda hp,
    paddedSignedArrays_eq_image r height vertices shape hpos lambda hp pad hshape]
  rw [Finset.sum_image (fun _ _ _ _ he => paddedIdentityArray_injective pad he)]
  rw [sum_toFinset_map _ _ (CornerSlide.family_nodup r vertices shape)]
  apply Finset.sum_congr rfl
  intro body _
  simp only [unsignedArrayWeight, paddedIdentityArray, identityArrayAt_rows,
    tableauGraphInversions_padding]

end PartitionH3

#check @PartitionH3.signedArray_sum_eq_complete_family
#print axioms PartitionH3.paddedIdentityArray_mem
#print axioms PartitionH3.paddedSignedArrays_eq_image
#print axioms PartitionH3.sum_toFinset_map
#print axioms PartitionH3.signedArray_sum_eq_complete_family
