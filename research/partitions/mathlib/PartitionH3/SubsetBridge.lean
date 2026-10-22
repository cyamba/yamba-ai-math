import PartitionH3.Alternant
import AlternantSubsets
import Mathlib.Data.List.OfFn
import Mathlib.Algebra.BigOperators.Fin

open scoped BigOperators

noncomputable section

namespace PartitionH3

def subsetBits {m : ℕ} (T : Finset (Fin m)) : List Bool :=
  List.ofFn (fun i => decide (i ∈ T))

def fromBits (m : ℕ) (xs : List Bool) : Finset (Fin m) :=
  Finset.univ.filter (fun i => xs[i.val]?.getD false = true)

theorem ones_ofFn {m : ℕ} (f : Fin m → Bool) :
    AlternantSubsets.ones (List.ofFn f) = ∑ i, if f i then 1 else 0 := by
  induction m with
  | zero => simp [AlternantSubsets.ones]
  | succ m ih =>
      rw [List.ofFn_succ, Fin.sum_univ_succ]
      cases h : f 0 <;> simp [AlternantSubsets.ones, ih]

theorem subsetBits_length {m : ℕ} (T : Finset (Fin m)) :
    (subsetBits T).length = m := by
  simp [subsetBits]

theorem subsetBits_ones {m : ℕ} (T : Finset (Fin m)) :
    AlternantSubsets.ones (subsetBits T) = T.card := by
  rw [subsetBits, ones_ofFn]
  simp only [decide_eq_true_eq]
  rw [← Finset.sum_filter]
  simp

theorem subsetBits_injective {m : ℕ} : Function.Injective (@subsetBits m) := by
  intro S T h
  have he := List.ofFn_injective h
  ext i
  have hi := congrFun he i
  simpa only [decide_eq_decide] using hi

theorem subsetBits_fromBits (m : ℕ) (xs : List Bool) (hlen : xs.length = m) :
    subsetBits (fromBits m xs) = xs := by
  apply List.ext_getElem (by simp [subsetBits, hlen])
  intro i hi hj
  simp only [subsetBits, List.getElem_ofFn, fromBits, Finset.mem_filter,
    Finset.mem_univ, true_and]
  simp [List.getElem?_eq_getElem hj]

theorem fromBits_subsetBits {m : ℕ} (T : Finset (Fin m)) :
    fromBits m (subsetBits T) = T := by
  apply subsetBits_injective
  exact subsetBits_fromBits m _ (subsetBits_length T)

def twoBlockSubset (m a b j : ℕ) : Finset (Fin m) :=
  fromBits m (AlternantSubsets.candidate m a b j)

theorem twoBlockSubset_bits (m a b j : ℕ) (hba : b ≤ a) (hab : a + b ≤ m)
    (hj : j ≤ b) :
    subsetBits (twoBlockSubset m a b j) = AlternantSubsets.candidate m a b j :=
  subsetBits_fromBits m _ (AlternantSubsets.candidate_length m a b j hba hab hj)

theorem twoBlockSubset_card (m a b j : ℕ) (hba : b ≤ a) (hab : a + b ≤ m)
    (hj : j ≤ b) : (twoBlockSubset m a b j).card = b := by
  rw [← subsetBits_ones, twoBlockSubset_bits m a b j hba hab hj]
  exact AlternantSubsets.candidate_ones m a b j hj

/-- The previously checked bit classification transferred to actual subsets,
with cardinality and uniqueness and without excluding the empty case. -/
theorem twoBlockSubset_classification (m a b : ℕ) (hba : b ≤ a)
    (hab : a + b ≤ m) (T : Finset (Fin m)) (hcard : T.card = b) :
    (AlternantSubsets.NoRise ((subsetBits T).take a) ∧
      AlternantSubsets.NoRise ((subsetBits T).drop a)) ↔
      ∃ j, (j ≤ b ∧ T = twoBlockSubset m a b j) ∧
        ∀ k, (k ≤ b ∧ T = twoBlockSubset m a b k) → k = j := by
  have hb : AlternantSubsets.ones (subsetBits T) = b :=
    (subsetBits_ones T).trans hcard
  rw [AlternantSubsets.two_block_classification m a b hba hab
    (subsetBits T) (subsetBits_length T) hb]
  have he : ∀ j, j ≤ b →
      (subsetBits T = AlternantSubsets.candidate m a b j ↔
        T = twoBlockSubset m a b j) := by
    intro j hj
    rw [← twoBlockSubset_bits m a b j hba hab hj]
    exact subsetBits_injective.eq_iff
  constructor
  · rintro ⟨j, ⟨hj, hT⟩, hu⟩
    refine ⟨j, ⟨hj, (he j hj).mp hT⟩, ?_⟩
    rintro k ⟨hk, hTk⟩
    exact hu k ⟨hk, (he k hk).mpr hTk⟩
  · rintro ⟨j, ⟨hj, hT⟩, hu⟩
    refine ⟨j, ⟨hj, (he j hj).mpr hT⟩, ?_⟩
    rintro k ⟨hk, hTk⟩
    exact hu k ⟨hk, (he k hk).mp hTk⟩

end PartitionH3

#check @PartitionH3.twoBlockSubset_classification
#print axioms PartitionH3.subsetBits_ones
#print axioms PartitionH3.subsetBits_injective
#print axioms PartitionH3.subsetBits_fromBits
#print axioms PartitionH3.fromBits_subsetBits
#print axioms PartitionH3.twoBlockSubset_card
#print axioms PartitionH3.twoBlockSubset_classification
