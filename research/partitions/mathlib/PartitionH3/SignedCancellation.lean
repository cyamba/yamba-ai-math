import PartitionH3.Foundations
import SignedArrays

/-!
Finite cancellation of the checked signed-array involution. The universe
contains every actual signed array of the specified length, including empty
rows. No coloring expansion or identification with a tableau family is used.
-/

open scoped BigOperators

noncomputable section

namespace PartitionH3

attribute [local instance] Classical.propDecidable

/-- Lists of exactly `k` elements from an explicitly finite alphabet. -/
def finiteLists {α : Type*} [DecidableEq α] (s : Finset α) : ℕ → Finset (List α)
  | 0 => {[]}
  | k + 1 => (s ×ˢ finiteLists s k).image (fun p => p.1 :: p.2)

theorem mem_finiteLists {α : Type*} [DecidableEq α] (s : Finset α)
    (k : ℕ) (xs : List α) :
    xs ∈ finiteLists s k ↔ xs.length = k ∧ ∀ x ∈ xs, x ∈ s := by
  induction k generalizing xs with
  | zero =>
      cases xs <;> simp [finiteLists]
  | succ k ih =>
      cases xs with
      | nil => simp [finiteLists]
      | cons x xs =>
          simp only [finiteLists, Finset.mem_image, Finset.mem_product, Prod.exists,
            List.cons.injEq, List.length_cons, List.forall_mem_cons]
          constructor
          · rintro ⟨y, ys, ⟨hy, hys⟩, rfl, rfl⟩
            obtain ⟨hlen, hmem⟩ := (ih _).mp hys
            exact ⟨by omega, hy, hmem⟩
          · rintro ⟨hlen, hx, hmem⟩
            exact ⟨x, xs, ⟨hx, (ih xs).mpr ⟨by omega, hmem⟩⟩, rfl, rfl⟩

/-- Rows cannot be longer than the complete bijective filling. -/
def finiteRows (vertices : List ℕ) : Finset (List ℕ) :=
  (Finset.range (vertices.length + 1)).biUnion (finiteLists vertices.toFinset)

theorem mem_finiteRows (vertices row : List ℕ) :
    row ∈ finiteRows vertices ↔
      row.length ≤ vertices.length ∧ ∀ v ∈ row, v ∈ vertices := by
  simp only [finiteRows, Finset.mem_biUnion, Finset.mem_range, mem_finiteLists,
    List.mem_toFinset]
  constructor
  · rintro ⟨k, hk, he, hm⟩
    exact ⟨by omega, hm⟩
  · rintro ⟨hl, hm⟩
    exact ⟨row.length, by omega, rfl, hm⟩

def signedArrayCandidates (vertices : List ℕ) (m : ℕ) : Finset SignedArrays.Array :=
  finiteLists (Finset.range m ×ˢ finiteRows vertices) m

def signedArrayUniverse (r : ℕ → ℕ → Prop) (vertices : List ℕ)
    (lambda : ℕ → ℕ) (m : ℕ) : Finset SignedArrays.Array := by
  classical
  exact (signedArrayCandidates vertices m).filter (SignedArrays.SignedArray r vertices lambda)

/-- The finite enumeration is complete for actual bijective labelled arrays. -/
theorem mem_signedArrayUniverse (r : ℕ → ℕ → Prop) (vertices : List ℕ)
    (lambda : ℕ → ℕ) (m : ℕ) (a : SignedArrays.Array) :
    a ∈ signedArrayUniverse r vertices lambda m ↔
      SignedArrays.SignedArray r vertices lambda a ∧ a.length = m := by
  classical
  simp only [signedArrayUniverse, Finset.mem_filter]
  constructor
  · rintro ⟨hc, ha⟩
    exact ⟨ha, ((mem_finiteLists _ _ a).mp hc).1⟩
  · rintro ⟨ha, hlen⟩
    refine ⟨(mem_finiteLists _ _ a).mpr ⟨hlen, ?_⟩, ha⟩
    intro entry hem
    apply Finset.mem_product.mpr
    constructor
    · have hp : entry.1 ∈ SignedArrays.labels a := List.mem_map.mpr ⟨entry, hem, rfl⟩
      have hr := ha.1.mem_iff.mp hp
      simpa only [hlen, List.mem_range, Finset.mem_range] using hr
    · apply (mem_finiteRows vertices entry.2).mpr
      have hrow : entry.2 ∈ SignedArrays.rows a := List.mem_map.mpr ⟨entry, hem, rfl⟩
      have hsub := List.sublist_flatten_of_mem hrow
      have hcontents : (SignedArrays.contents a).Perm vertices := ha.2.2.2.1
      refine ⟨?_, ?_⟩
      · have hl := hsub.length_le
        change entry.2.length ≤ (SignedArrays.contents a).length at hl
        rw [hcontents.length_eq] at hl
        exact hl
      · intro v hv
        exact hcontents.mem_iff.mp (List.mem_flatten_of_mem hrow hv)

def signedArrayWeight (r : ℕ → ℕ → Prop) [DecidableRel r]
    (a : SignedArrays.Array) : Coeff :=
  (SignedArrays.permutationSign (SignedArrays.labels a) : Coeff) *
    Polynomial.X ^ CornerSlide.tableauGraphInversions r (SignedArrays.rows a)

def unsignedArrayWeight (r : ℕ → ℕ → Prop) [DecidableRel r]
    (a : SignedArrays.Array) : Coeff :=
  Polynomial.X ^ CornerSlide.tableauGraphInversions r (SignedArrays.rows a)

theorem signedArrayWeight_move {r : ℕ → ℕ → Prop} [DecidableRel r]
    (vertices : List ℕ) (lambda : ℕ → ℕ) (a : SignedArrays.Array)
    (ha : SignedArrays.SignedArray r vertices lambda a)
    (hm : SignedArrays.move r a ≠ a) :
    signedArrayWeight r (SignedArrays.move r a) = -signedArrayWeight r a := by
  have hn : (SignedArrays.labels a).Nodup := ha.1.nodup_iff.mpr List.nodup_range
  simp only [signedArrayWeight, SignedArrays.move_sign_reversing r a hn hm,
    SignedArrays.move_tableauGraphInversions r vertices a ha.2.2, Int.cast_neg, neg_mul]

theorem signedArrayWeight_fixed {r : ℕ → ℕ → Prop} [DecidableRel r]
    (height : CornerSlide.NoThreeChain r) (vertices : List ℕ) (lambda : ℕ → ℕ)
    (hp : SignedArrays.Partition lambda) (a : SignedArrays.Array)
    (ha : SignedArrays.SignedArray r vertices lambda a) (hm : SignedArrays.move r a = a) :
    signedArrayWeight r a = unsignedArrayWeight r a := by
  rw [signedArrayWeight, SignedArrays.fixed_permutationSign r height lambda hp vertices a ha hm]
  simp [unsignedArrayWeight]

/-- The actual nonfixed arrays cancel in opposite-sign pairs. -/
theorem signedArray_moved_sum_zero (r : ℕ → ℕ → Prop) [DecidableRel r]
    (vertices : List ℕ) (lambda : ℕ → ℕ) (m : ℕ) (A : Finset SignedArrays.Array)
    (hA : ∀ a, a ∈ A ↔ SignedArrays.SignedArray r vertices lambda a ∧ a.length = m) :
    (∑ a ∈ A.filter (fun a => SignedArrays.move r a ≠ a), signedArrayWeight r a) = 0 := by
  classical
  have hpres : ∀ a ∈ A, SignedArrays.move r a ∈ A := by
    intro a ha
    obtain ⟨hs, hl⟩ := (hA a).mp ha
    exact (hA _).mpr ⟨SignedArrays.move_signedArray r vertices lambda a hs,
      (SignedArrays.move_length r a).trans hl⟩
  apply Finset.sum_involution (fun a _ => SignedArrays.move r a)
  · intro a ha
    obtain ⟨haA, hm⟩ := Finset.mem_filter.mp ha
    rw [signedArrayWeight_move vertices lambda a ((hA a).mp haA).1 hm]
    exact add_neg_cancel _
  · intro a ha _
    exact (Finset.mem_filter.mp ha).2
  · intro a ha
    obtain ⟨haA, hm⟩ := Finset.mem_filter.mp ha
    apply Finset.mem_filter.mpr
    refine ⟨hpres a haA, ?_⟩
    intro he
    rw [SignedArrays.move_involution] at he
    exact hm he.symm
  · intro a _
    exact SignedArrays.move_involution r a

theorem signedArray_sum_eq_fixed (r : ℕ → ℕ → Prop) [DecidableRel r]
    (vertices : List ℕ) (lambda : ℕ → ℕ) (m : ℕ) (A : Finset SignedArrays.Array)
    (hA : ∀ a, a ∈ A ↔ SignedArrays.SignedArray r vertices lambda a ∧ a.length = m) :
    (∑ a ∈ A, signedArrayWeight r a) =
      ∑ a ∈ A.filter (fun a => SignedArrays.move r a = a), signedArrayWeight r a := by
  classical
  have hz := signedArray_moved_sum_zero r vertices lambda m A hA
  have hs := Finset.sum_filter_add_sum_filter_not A
    (fun a => SignedArrays.move r a = a) (signedArrayWeight r)
  rw [hz, add_zero] at hs
  exact hs.symm

/-- Fixed terms have positive sign and are exactly the actual padded tableaux.
The remaining padding-to-complete-family bijection is a separate obligation. -/
theorem signedArray_sum_eq_padded (r : ℕ → ℕ → Prop) [DecidableRel r]
    (height : CornerSlide.NoThreeChain r) (vertices : List ℕ) (lambda : ℕ → ℕ)
    (hp : SignedArrays.Partition lambda) (m : ℕ) (A : Finset SignedArrays.Array)
    (hA : ∀ a, a ∈ A ↔ SignedArrays.SignedArray r vertices lambda a ∧ a.length = m) :
    (∑ a ∈ A, signedArrayWeight r a) =
      ∑ a ∈ A.filter (fun a => SignedArrays.PaddedTableau r vertices (SignedArrays.rows a)),
        unsignedArrayWeight r a := by
  classical
  have hf : A.filter (fun a => SignedArrays.move r a = a) =
      A.filter (fun a => SignedArrays.PaddedTableau r vertices (SignedArrays.rows a)) := by
    ext a
    simp only [Finset.mem_filter]
    constructor
    · rintro ⟨ha, hm⟩
      exact ⟨ha, (SignedArrays.signedArray_fixed_iff_padded r height lambda hp vertices a
        ((hA a).mp ha).1).mp hm⟩
    · rintro ⟨ha, hm⟩
      exact ⟨ha, (SignedArrays.signedArray_fixed_iff_padded r height lambda hp vertices a
        ((hA a).mp ha).1).mpr hm⟩
  calc
    (∑ a ∈ A, signedArrayWeight r a) =
        ∑ a ∈ A.filter (fun a => SignedArrays.move r a = a), signedArrayWeight r a :=
      signedArray_sum_eq_fixed r vertices lambda m A hA
    _ = ∑ a ∈ A.filter (fun a => SignedArrays.move r a = a), unsignedArrayWeight r a := by
      apply Finset.sum_congr rfl
      intro a ha
      obtain ⟨haA, hm⟩ := Finset.mem_filter.mp ha
      exact signedArrayWeight_fixed height vertices lambda hp a ((hA a).mp haA).1 hm
    _ = ∑ a ∈ A.filter (fun a =>
        SignedArrays.PaddedTableau r vertices (SignedArrays.rows a)), unsignedArrayWeight r a := by
      rw [hf]

/-- Cancellation over the constructed complete finite signed-array universe. -/
theorem signedArray_universe_cancellation (r : ℕ → ℕ → Prop) [DecidableRel r]
    (height : CornerSlide.NoThreeChain r) (vertices : List ℕ) (lambda : ℕ → ℕ)
    (hp : SignedArrays.Partition lambda) (m : ℕ) :
    (∑ a ∈ signedArrayUniverse r vertices lambda m, signedArrayWeight r a) =
      ∑ a ∈ (signedArrayUniverse r vertices lambda m).filter (fun a =>
        SignedArrays.PaddedTableau r vertices (SignedArrays.rows a)), unsignedArrayWeight r a :=
  signedArray_sum_eq_padded r height vertices lambda hp m _
    (mem_signedArrayUniverse r vertices lambda m)

theorem heightTwo_natLt_noThreeChain {n : ℕ} (H : NaturalUnitInterval n)
    (hh : HeightTwo H) : CornerSlide.NoThreeChain (natLt H) := by
  intro i j k hij hjk
  by_cases hi : i < n
  · by_cases hj : j < n
    · by_cases hk : k < n
      · exact hh ⟨i, hi⟩ ⟨j, hj⟩ ⟨k, hk⟩
          ⟨by simpa [natLt, hi, hj] using hij, by simpa [natLt, hj, hk] using hjk⟩
      · simp [natLt, hj, hk] at hjk
    · simp [natLt, hi, hj] at hij
  · simp [natLt, hi] at hij

/-- The concrete natural-unit-interval specialization retains the full range
of actual vertex labels and all arrays with exactly `m` rows. -/
theorem natural_signed_array_cancellation {n : ℕ} (H : NaturalUnitInterval n)
    (hh : HeightTwo H) (lambda : ℕ → ℕ) (hp : SignedArrays.Partition lambda) (m : ℕ) :
    (∑ a ∈ signedArrayUniverse (natLt H) (List.range n) lambda m,
      signedArrayWeight (natLt H) a) =
      ∑ a ∈ (signedArrayUniverse (natLt H) (List.range n) lambda m).filter (fun a =>
        SignedArrays.PaddedTableau (natLt H) (List.range n) (SignedArrays.rows a)),
        unsignedArrayWeight (natLt H) a :=
  signedArray_universe_cancellation (natLt H) (heightTwo_natLt_noThreeChain H hh)
    (List.range n) lambda hp m

end PartitionH3

#check @PartitionH3.mem_signedArrayUniverse
#check @PartitionH3.signedArray_universe_cancellation
#check @PartitionH3.natural_signed_array_cancellation
#print axioms PartitionH3.mem_finiteLists
#print axioms PartitionH3.mem_signedArrayUniverse
#print axioms PartitionH3.signedArrayWeight_move
#print axioms PartitionH3.signedArray_moved_sum_zero
#print axioms PartitionH3.signedArray_sum_eq_fixed
#print axioms PartitionH3.signedArray_sum_eq_padded
#print axioms PartitionH3.signedArray_universe_cancellation
#print axioms PartitionH3.heightTwo_natLt_noThreeChain
#print axioms PartitionH3.natural_signed_array_cancellation
