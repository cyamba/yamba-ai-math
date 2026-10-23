import PartitionH3.ElementaryProduct
import PartitionH3.SignedCancellation

/-!
Natural exponent vectors used in finite alternating reconstruction are
staircases plus genuine partitions, extended by zero outside the alphabet.
-/

noncomputable section

namespace PartitionH3

def dominantPartition {m : ℕ} (gamma : Fin m → ℕ) (k : ℕ) : ℕ :=
  if hk : k < m then gamma ⟨k, hk⟩ - delta m ⟨k, hk⟩ else 0

theorem dominant_ge_delta {m : ℕ} (gamma : Fin m → ℕ) (hg : StrictAnti gamma)
    (i : Fin m) : delta m i ≤ gamma i := by
  have haux : ∀ d k (hk : k < m), m - 1 - k = d → d ≤ gamma ⟨k, hk⟩ := by
    intro d
    induction d with
    | zero => intro k hk _; exact Nat.zero_le _
    | succ d ih =>
      intro k hk he
      have hk' : k + 1 < m := by omega
      have hd := ih (k + 1) hk' (by omega)
      have hlt : gamma ⟨k + 1, hk'⟩ < gamma ⟨k, hk⟩ :=
        hg (show (⟨k, hk⟩ : Fin m) < ⟨k + 1, hk'⟩ by
          change k < k + 1
          omega)
      omega
  exact haux (m - 1 - i.val) i.val i.isLt rfl

theorem dominantPartition_partition {m : ℕ} (gamma : Fin m → ℕ)
    (hg : StrictAnti gamma) : SignedArrays.Partition (dominantPartition gamma) := by
  apply antitone_nat_of_succ_le
  intro k
  by_cases hk : k + 1 < m
  · have hk0 : k < m := by omega
    simp only [dominantPartition, dite_eq_left hk, dite_eq_left hk0]
    have hlt : gamma ⟨k + 1, hk⟩ < gamma ⟨k, hk0⟩ :=
      hg (show (⟨k, hk0⟩ : Fin m) < ⟨k + 1, hk⟩ by
        change k < k + 1
        omega)
    have hb := dominant_ge_delta gamma hg ⟨k, hk0⟩
    unfold delta at *
    simp only at *
    omega
  · simp only [dominantPartition, dite_eq_right hk]
    exact Nat.zero_le _

theorem delta_add_dominantPartition {m : ℕ} (gamma : Fin m → ℕ)
    (hg : StrictAnti gamma) (i : Fin m) :
    delta m i + dominantPartition gamma i.val = gamma i := by
  simp only [dominantPartition, dite_eq_left i.isLt]
  exact Nat.add_sub_of_le (dominant_ge_delta gamma hg i)

theorem delta_add_partition_strictAnti (m : ℕ) (lambda : ℕ → ℕ)
    (hp : SignedArrays.Partition lambda) :
    StrictAnti (fun i : Fin m => delta m i + lambda i.val) := by
  intro i j hij
  have hlt : i.val < j.val := hij
  have hl := hp i.val j.val (Nat.le_of_lt hlt)
  have hi := i.isLt
  have hj := j.isLt
  change delta m j + lambda j.val < delta m i + lambda i.val
  unfold delta
  omega

def twoColumnPartition (n k i : ℕ) : ℕ :=
  if i < k then 2 else if i < n - k then 1 else 0

theorem twoColumnPartition_partition (n k : ℕ) :
    SignedArrays.Partition (twoColumnPartition n k) := by
  intro i j hij
  unfold twoColumnPartition
  split_ifs <;> omega

theorem twoColumnShape_strictAnti (m n k : ℕ) :
    StrictAnti (fun i => delta m i + twoColumnShape m n k i) := by
  exact delta_add_partition_strictAnti m _ (twoColumnPartition_partition n k)

/-- A decreasing list with entries bounded by two has exactly three blocks.
Zero rows remain present in the last block. -/
theorem bounded_partition_three_blocks (xs : List ℕ)
    (hp : xs.Pairwise (fun x y => y ≤ x)) (hb : ∀ x ∈ xs, x ≤ 2) :
    ∃ k l z, xs = List.replicate k 2 ++ List.replicate l 1 ++ List.replicate z 0 := by
  induction xs with
  | nil => exact ⟨0, 0, 0, rfl⟩
  | cons x xs ih =>
    obtain ⟨hh, ht⟩ := List.pairwise_cons.mp hp
    obtain ⟨k, l, z, he⟩ := ih ht (fun y hy => hb y (List.mem_cons_of_mem x hy))
    have hx := hb x (by simp)
    have hxcase : x = 0 ∨ x = 1 ∨ x = 2 := by omega
    rcases hxcase with rfl | rfl | rfl
    · have hk : k = 0 := by
        by_contra hn
        have hm : 2 ∈ xs := by simp [he, hn]
        have := hh 2 hm
        omega
      have hl : l = 0 := by
        by_contra hn
        have hm : 1 ∈ xs := by simp [he, hn]
        have := hh 1 hm
        omega
      refine ⟨0, 0, z + 1, ?_⟩
      simp [he, hk, hl, List.replicate_succ]
    · have hk : k = 0 := by
        by_contra hn
        have hm : 2 ∈ xs := by simp [he, hn]
        have := hh 2 hm
        omega
      refine ⟨0, l + 1, z, ?_⟩
      simp [he, hk, List.replicate_succ]
    · refine ⟨k + 1, l, z, ?_⟩
      simp [he, List.replicate_succ]

theorem partition_range_three_blocks (lambda : ℕ → ℕ)
    (hp : SignedArrays.Partition lambda) (m n : ℕ)
    (hb : ∀ x ∈ (List.range m).map lambda, x ≤ 2)
    (hsum : ((List.range m).map lambda).sum = n) :
    ∃ k, 2 * k ≤ n ∧ n - k ≤ m ∧
      (List.range m).map lambda =
        CornerSlide.twoColumnShape k (n - 2 * k) ++ List.replicate (m - (n - k)) 0 := by
  have hsort : ((List.range m).map lambda).Pairwise (fun x y => y ≤ x) := by
    apply List.pairwise_map.mpr
    exact List.pairwise_lt_range.imp (fun h => hp _ _ (Nat.le_of_lt h))
  obtain ⟨k, l, z, he⟩ := bounded_partition_three_blocks _ hsort hb
  have hlen := congrArg List.length he
  have hsm := congrArg List.sum he
  simp only [List.length_map, List.length_range, List.length_append,
    List.length_replicate] at hlen
  simp only [hsum, List.sum_append, List.sum_replicate, smul_eq_mul,
    mul_one, mul_zero, add_zero] at hsm
  have hl : l = n - 2 * k := by omega
  have hz : z = m - (n - k) := by omega
  refine ⟨k, by omega, by omega, ?_⟩
  simpa only [CornerSlide.twoColumnShape, hl, hz, List.append_assoc] using he

theorem twoColumnPartition_range (m n k : ℕ) (hk : 2 * k ≤ n) (hm : n ≤ m) :
    (List.range m).map (twoColumnPartition n k) =
      CornerSlide.twoColumnShape k (n - 2 * k) ++ List.replicate (m - (n - k)) 0 := by
  apply List.ext_getElem
  · simp only [List.length_map, List.length_range, List.length_append,
      List.length_replicate, CornerSlide.twoColumnShape]
    omega
  · intro i hi hj
    simp only [List.getElem_map, List.getElem_range, CornerSlide.twoColumnShape,
      List.getElem_append, List.length_append, List.length_replicate,
      List.getElem_replicate, twoColumnPartition]
    split_ifs <;> omega

/-- Height two and the complete bijective filling force every surviving
partition sector to have the original two-column shape. -/
theorem fixed_signedArray_shape (r : ℕ → ℕ → Prop) [DecidableRel r]
    (height : CornerSlide.NoThreeChain r) (vertices : List ℕ) (lambda : ℕ → ℕ)
    (hp : SignedArrays.Partition lambda) (a : SignedArrays.Array)
    (ha : SignedArrays.SignedArray r vertices lambda a) (hf : SignedArrays.move r a = a) :
    ∃ k, 2 * k ≤ vertices.length ∧ vertices.length - k ≤ a.length ∧
      (List.range a.length).map lambda =
        CornerSlide.twoColumnShape k (vertices.length - 2 * k) ++
          List.replicate (a.length - (vertices.length - k)) 0 := by
  have hrow := SignedArrays.fixed_row_lengths r height lambda hp vertices a ha hf
  apply partition_range_three_blocks lambda hp a.length vertices.length
  · intro d hd
    rw [← hrow] at hd
    obtain ⟨row, hr, rfl⟩ := List.mem_map.mp hd
    obtain ⟨entry, he, rfl⟩ := List.mem_map.mp hr
    exact SignedArrays.height_two_row_length_le_two r height entry.2 (ha.2.2.2.2 entry he)
  · rw [← hrow, ← List.length_flatten]
    exact ha.2.2.2.1.length_eq

theorem range_map_eq_iff (f g : ℕ → ℕ) (m : ℕ) :
    (List.range m).map f = (List.range m).map g ↔
      ∀ i : Fin m, f i.val = g i.val := by
  simp only [List.map_inj_left, List.mem_range]
  constructor
  · intro h i
    exact h i.val i.isLt
  · intro h i hi
    exact h ⟨i, hi⟩

theorem twoColumn_exponent_eq_iff (m n k j : ℕ) (hm : n ≤ m)
    (hk : 2 * k ≤ n) (hj : 2 * j ≤ n) :
    (fun i => delta m i + twoColumnShape m n k i) =
      (fun i => delta m i + twoColumnShape m n j i) ↔ k = j := by
  have hneq : ∀ a b : ℕ, a < b → 2 * b ≤ n →
      (fun i => delta m i + twoColumnShape m n a i) ≠
        (fun i => delta m i + twoColumnShape m n b i) := by
    intro a b hab hb he
    have ha : a < m := by omega
    have h := congrFun he ⟨a, ha⟩
    change delta m ⟨a, ha⟩ + twoColumnShape m n a ⟨a, ha⟩ =
      delta m ⟨a, ha⟩ + twoColumnShape m n b ⟨a, ha⟩ at h
    have hs := Nat.add_left_cancel h
    simp only [twoColumnShape, Nat.lt_irrefl, reduceIte, hab] at hs
    split_ifs at hs; omega
  constructor
  · intro he
    rcases lt_trichotomy k j with h | h | h
    · exact False.elim (hneq k j h hj he)
    · exact h
    · exact False.elim (hneq j k h hk he.symm)
  · rintro rfl
    rfl

end PartitionH3

#check @PartitionH3.dominantPartition_partition
#print axioms PartitionH3.dominant_ge_delta
#print axioms PartitionH3.dominantPartition_partition
#print axioms PartitionH3.delta_add_dominantPartition
#print axioms PartitionH3.delta_add_partition_strictAnti
#print axioms PartitionH3.twoColumnPartition_partition
#print axioms PartitionH3.twoColumnShape_strictAnti
#print axioms PartitionH3.bounded_partition_three_blocks
#print axioms PartitionH3.partition_range_three_blocks
#print axioms PartitionH3.twoColumnPartition_range
#print axioms PartitionH3.fixed_signedArray_shape
#print axioms PartitionH3.range_map_eq_iff
#print axioms PartitionH3.twoColumn_exponent_eq_iff
