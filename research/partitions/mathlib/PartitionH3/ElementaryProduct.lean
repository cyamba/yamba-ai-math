import PartitionH3.SubsetBridge
import PartitionH3.Vandermonde

/-!
The two-elementary specialization of the actual finite alternant sum.
All exponents are natural numbers; integer expressions are used only after
the index bound has justified the cast of `delta`.
-/

open scoped BigOperators

noncomputable section

namespace PartitionH3

/-- The initial segment of the alphabet, also valid when `a > m`. -/
def prefixSubset (m a : ℕ) : Finset (Fin m) :=
  fromBits m (List.replicate a true ++ List.replicate (m - a) false)

def prefixExponent (m a : ℕ) (i : Fin m) : ℕ :=
  delta m i + if i.val < a then 1 else 0

/-- Under `2*j ≤ n ≤ m`, this is `(2^j,1^(n-2*j),0^(m-n+j))`. -/
def twoColumnShape (m n j : ℕ) (i : Fin m) : ℕ :=
  if i.val < j then 2 else if i.val < n - j then 1 else 0

theorem true_false_bits_getD (p q i : ℕ) :
    (List.replicate p true ++ List.replicate q false)[i]?.getD false =
      decide (i < p) := by
  rw [List.getElem?_append]
  by_cases hi : i < p
  · simp [hi]
  · simp only [List.length_replicate, hi, ↓reduceIte, List.getElem?_replicate]
    split <;> simp

theorem prefixSubset_mem (m a : ℕ) (i : Fin m) :
    i ∈ prefixSubset m a ↔ i.val < a := by
  simp [prefixSubset, fromBits, true_false_bits_getD]

theorem prefixSubset_bits (m a : ℕ) (ha : a ≤ m) :
    subsetBits (prefixSubset m a) =
      List.replicate a true ++ List.replicate (m - a) false := by
  apply subsetBits_fromBits
  simp only [List.length_append, List.length_replicate]
  omega

theorem prefixSubset_card (m a : ℕ) (ha : a ≤ m) :
    (prefixSubset m a).card = a := by
  rw [← subsetBits_ones, prefixSubset_bits m a ha]
  simp [AlternantSubsets.ones_append, AlternantSubsets.ones_replicate_true,
    AlternantSubsets.ones_replicate_false]

theorem bump_delta_prefix (m a : ℕ) :
    bump (delta m) (prefixSubset m a) = prefixExponent m a := by
  funext i
  simp [bump, indicator, prefixExponent, prefixSubset_mem]

theorem noRise_subset_eq_prefix {m a : ℕ} (T : Finset (Fin m))
    (hcard : T.card = a) (h : AlternantSubsets.NoRise (subsetBits T)) :
    T = prefixSubset m a := by
  have he := (AlternantSubsets.noRise_iff_prefix (subsetBits T)).mp h
  rw [subsetBits_ones, hcard, subsetBits_length] at he
  rw [← fromBits_subsetBits T, he]
  rfl

theorem noRise_of_no_adjacent_rise (xs : List Bool)
    (h : ∀ k, k + 1 < xs.length →
      xs[k]?.getD false = false → xs[k + 1]?.getD false = false) :
    AlternantSubsets.NoRise xs := by
  induction xs with
  | nil => trivial
  | cons x xs ih =>
      cases xs with
      | nil => trivial
      | cons y ys =>
          constructor
          · simpa using h 0 (by simp)
          · apply ih
            intro k hk hf
            have hh := h (k + 1) (by simpa using Nat.succ_lt_succ hk)
            simpa only [List.getElem?_cons_succ] using hh hf

theorem exists_adjacent_rise (xs : List Bool)
    (h : ¬ AlternantSubsets.NoRise xs) :
    ∃ k, k + 1 < xs.length ∧ xs[k]?.getD false = false ∧
      xs[k + 1]?.getD false = true := by
  classical
  by_contra hn
  apply h
  apply noRise_of_no_adjacent_rise
  intro k hk hf
  have ht : xs[k + 1]?.getD false ≠ true := by
    intro ht
    exact hn ⟨k, hk, hf, ht⟩
  cases hb : xs[k + 1]?.getD false <;> simp_all

theorem bump_prefix_cast {m : ℕ} (a : ℕ) (T : Finset (Fin m)) (i : Fin m) :
    (bump (prefixExponent m a) T i : ℤ) =
      AlternantSubsets.exponent m a i.val ((subsetBits T)[i.val]?.getD false) := by
  classical
  simp [bump, prefixExponent, indicator, Nat.cast_add, delta_cast,
    AlternantSubsets.exponent, subsetBits, i.isLt]

/-- The bit collision is an equality of the actual natural exponent entries. -/
theorem bump_prefix_adjacent_collision {m : ℕ} (a k : ℕ) (T : Finset (Fin m))
    (hk : k + 1 < m) (hcut : k + 1 ≠ a)
    (hf : (subsetBits T)[k]?.getD false = false)
    (ht : (subsetBits T)[k + 1]?.getD false = true) :
    bump (prefixExponent m a) T ⟨k, by omega⟩ =
      bump (prefixExponent m a) T ⟨k + 1, hk⟩ := by
  apply Int.ofNat_inj.mp
  rw [bump_prefix_cast, bump_prefix_cast]
  exact (AlternantSubsets.adjacent_exponent_collision m a k _ _).mpr ⟨hcut, hf, ht⟩

/-- Every subset outside the two no-rise blocks contributes zero. -/
theorem alternant_bump_prefix_eq_zero {m : ℕ} (a : ℕ) (T : Finset (Fin m))
    (h : ¬ (AlternantSubsets.NoRise ((subsetBits T).take a) ∧
      AlternantSubsets.NoRise ((subsetBits T).drop a))) :
    alternant (bump (prefixExponent m a) T) = 0 := by
  classical
  have hlen := subsetBits_length T
  by_cases ht : AlternantSubsets.NoRise ((subsetBits T).take a)
  · have hd : ¬ AlternantSubsets.NoRise ((subsetBits T).drop a) := fun hd => h ⟨ht, hd⟩
    obtain ⟨k, hk, hf, hr⟩ := exists_adjacent_rise _ hd
    have hm : a + k + 1 < m := by simp only [List.length_drop, hlen] at hk; omega
    have hf' : (subsetBits T)[a + k]?.getD false = false := by
      simpa only [List.getElem?_drop] using hf
    have hr' : (subsetBits T)[a + k + 1]?.getD false = true := by
      simpa only [List.getElem?_drop, Nat.add_assoc] using hr
    exact alternant_eq_zero_of_eq _ ⟨a + k, by omega⟩ ⟨a + k + 1, hm⟩
      (by intro he; have := congrArg Fin.val he; simp only at this; omega)
      (bump_prefix_adjacent_collision a (a + k) T hm (by omega) hf' hr')
  · obtain ⟨k, hk, hf, hr⟩ := exists_adjacent_rise _ ht
    have hka : k + 1 < a := by simp only [List.length_take] at hk; omega
    have hm : k + 1 < m := by simp only [List.length_take, hlen] at hk; omega
    rw [List.getElem?_take_of_lt (by omega : k < a)] at hf
    rw [List.getElem?_take_of_lt hka] at hr
    exact alternant_eq_zero_of_eq _ ⟨k, by omega⟩ ⟨k + 1, hm⟩
      (by intro he; have := congrArg Fin.val he; simp only at this; omega)
      (bump_prefix_adjacent_collision a k T hm (by omega) hf hr)

/-- The one-block sum has exactly its initial-segment term. -/
theorem vandermonde_mul_elementary (m a : ℕ) (ha : a ≤ m) :
    vandermonde m * elementary m a = alternant (prefixExponent m a) := by
  classical
  rw [vandermonde, alternant_mul_elementary, ← bump_delta_prefix m a]
  apply Finset.sum_eq_single (prefixSubset m a)
  · intro T hT hne
    have hcard : T.card = a := (Finset.mem_powersetCard.mp hT).2
    have hn : ¬ AlternantSubsets.NoRise (subsetBits T) := by
      intro hn
      exact hne (noRise_subset_eq_prefix T hcard hn)
    have hg : prefixExponent m 0 = delta m := by
      funext i
      simp [prefixExponent]
    have hz := alternant_bump_prefix_eq_zero 0 T (by
      simpa [AlternantSubsets.NoRise] using hn)
    simpa only [hg] using hz
  · intro hn
    exact (hn (Finset.mem_powersetCard.mpr
      ⟨Finset.subset_univ _, prefixSubset_card m a ha⟩)).elim

theorem candidate_getD (m a b j i : ℕ) (hj : j ≤ a) :
    (AlternantSubsets.candidate m a b j)[i]?.getD false =
      if i < a then decide (i < j) else decide (i - a < b - j) := by
  unfold AlternantSubsets.candidate
  rw [List.getElem?_append]
  have hl : (List.replicate j true ++ List.replicate (a - j) false).length = a := by
    simp only [List.length_append, List.length_replicate]
    omega
  rw [hl]
  by_cases hi : i < a
  · rw [ite_eq_left hi, ite_eq_left hi, true_false_bits_getD]
  · rw [ite_eq_right hi, ite_eq_right hi, true_false_bits_getD]

theorem twoBlockSubset_mem (m a b j : ℕ) (hj : j ≤ a) (i : Fin m) :
    i ∈ twoBlockSubset m a b j ↔
      i.val < j ∨ (a ≤ i.val ∧ i.val < a + (b - j)) := by
  simp only [twoBlockSubset, fromBits, Finset.mem_filter, Finset.mem_univ,
    true_and, candidate_getD m a b j i.val hj]
  by_cases hi : i.val < a
  · simp only [hi, ↓reduceIte, decide_eq_true_eq]
    omega
  · simp only [hi, ↓reduceIte, decide_eq_true_eq]
    omega

/-- The surviving subset has exactly the requested two-column exponents. -/
theorem bump_prefix_twoBlockSubset (m a b j : ℕ) (hba : b ≤ a) (hj : j ≤ b) :
    bump (prefixExponent m a) (twoBlockSubset m a b j) =
      fun i => delta m i + twoColumnShape m (a + b) j i := by
  funext i
  have hja : j ≤ a := hj.trans hba
  have hn : a + b - j = a + (b - j) := by omega
  simp only [bump, prefixExponent, indicator, twoColumnShape,
    twoBlockSubset_mem m a b j hja, hn]
  split_ifs <;> omega

/-- The two-block survivor sum, before identifying the first elementary factor. -/
theorem prefix_alternant_mul_elementary (m a b : ℕ) (hba : b ≤ a)
    (hab : a + b ≤ m) :
    alternant (prefixExponent m a) * elementary m b =
      ∑ j ∈ Finset.range (b + 1),
        alternant (fun i => delta m i + twoColumnShape m (a + b) j i) := by
  classical
  rw [alternant_mul_elementary]
  let s := (Finset.univ : Finset (Fin m)).powersetCard b
  let g := s.filter (fun T => AlternantSubsets.NoRise ((subsetBits T).take a) ∧
    AlternantSubsets.NoRise ((subsetBits T).drop a))
  have hs : ∀ T ∈ s, T.card = b := by
    intro T hT
    exact (Finset.mem_powersetCard.mp hT).2
  change (∑ T ∈ s, alternant (bump (prefixExponent m a) T)) = _
  calc
    (∑ T ∈ s, alternant (bump (prefixExponent m a) T)) =
        ∑ T ∈ g, alternant (bump (prefixExponent m a) T) := by
      symm
      apply Finset.sum_subset (Finset.filter_subset _ _)
      intro T hT hn
      apply alternant_bump_prefix_eq_zero
      intro hg
      exact hn (Finset.mem_filter.mpr ⟨hT, hg⟩)
    _ = ∑ j ∈ Finset.range (b + 1),
        alternant (fun i => delta m i + twoColumnShape m (a + b) j i) := by
      symm
      apply Finset.sum_bij (fun j _ => twoBlockSubset m a b j)
      · intro j hj
        have hjb : j ≤ b := Nat.le_of_lt_succ (Finset.mem_range.mp hj)
        apply Finset.mem_filter.mpr
        refine ⟨Finset.mem_powersetCard.mpr
          ⟨Finset.subset_univ _, twoBlockSubset_card m a b j hba hab hjb⟩, ?_⟩
        rw [twoBlockSubset_bits m a b j hba hab hjb]
        exact AlternantSubsets.candidate_noRise m a b j (hjb.trans hba)
      · intro j hj k hk he
        have hjb : j ≤ b := Nat.le_of_lt_succ (Finset.mem_range.mp hj)
        have hkb : k ≤ b := Nat.le_of_lt_succ (Finset.mem_range.mp hk)
        apply AlternantSubsets.candidate_injective m a b j k
          (hjb.trans hba) (hkb.trans hba)
        simpa only [twoBlockSubset_bits m a b j hba hab hjb,
          twoBlockSubset_bits m a b k hba hab hkb] using congrArg subsetBits he
      · intro T hT
        obtain ⟨hTs, hTg⟩ := Finset.mem_filter.mp hT
        obtain ⟨j, ⟨hj, he⟩, _⟩ :=
          (twoBlockSubset_classification m a b hba hab T (hs T hTs)).mp hTg
        exact ⟨j, Finset.mem_range.mpr (by omega), he.symm⟩
      · intro j hj
        have hjb : j ≤ b := Nat.le_of_lt_succ (Finset.mem_range.mp hj)
        rw [bump_prefix_twoBlockSubset m a b j hba hjb]

/-- The actual finite polynomial identity, including `m = 0` and `b = 0`. -/
theorem vandermonde_mul_two_elementary (m a b : ℕ) (hba : b ≤ a)
    (hab : a + b ≤ m) :
    vandermonde m * elementary m a * elementary m b =
      ∑ j ∈ Finset.range (b + 1),
        alternant (fun i => delta m i + twoColumnShape m (a + b) j i) := by
  rw [vandermonde_mul_elementary m a (by omega)]
  exact prefix_alternant_mul_elementary m a b hba hab

theorem vandermonde_mul_two_elementary_empty :
    vandermonde 0 * elementary 0 0 * elementary 0 0 =
      ∑ j ∈ Finset.range 1,
        alternant (fun i => delta 0 i + twoColumnShape 0 0 j i) :=
  vandermonde_mul_two_elementary 0 0 0 (by omega) (by omega)

theorem vandermonde_mul_two_elementary_zero (m a : ℕ) (ha : a ≤ m) :
    vandermonde m * elementary m a * elementary m 0 =
      alternant (fun i => delta m i + twoColumnShape m a 0 i) := by
  simpa using vandermonde_mul_two_elementary m a 0 (by omega) (by omega)

end PartitionH3

#check @PartitionH3.vandermonde_mul_two_elementary
#print axioms PartitionH3.bump_prefix_adjacent_collision
#print axioms PartitionH3.alternant_bump_prefix_eq_zero
#print axioms PartitionH3.vandermonde_mul_elementary
#print axioms PartitionH3.bump_prefix_twoBlockSubset
#print axioms PartitionH3.prefix_alternant_mul_elementary
#print axioms PartitionH3.vandermonde_mul_two_elementary
#print axioms PartitionH3.vandermonde_mul_two_elementary_empty
#print axioms PartitionH3.vandermonde_mul_two_elementary_zero
