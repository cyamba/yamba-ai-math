import PartitionH3.Foundations

/-!
Structural facts about actual finite proper colorings. Rows are ordered by
increasing color; their graph inversions correspond to coloring descents.
Reversing every color converts ascents to descents.
This file does not assert adjacent-color symmetry or the array bijection.
-/

noncomputable section

namespace PartitionH3

theorem posetLt_implies_lt {n : ℕ} (H : NaturalUnitInterval n) {i j : Fin n}
    (h : PosetLt H i j) : i < j :=
  lt_of_le_of_lt (H.extensive i) h

theorem edge_iff_incomparable {n : ℕ} (H : NaturalUnitInterval n) (i j : Fin n) :
    Edge H i j ↔ i < j ∧ ¬ PosetLt H i j ∧ ¬ PosetLt H j i := by
  constructor
  · rintro ⟨hij, hji⟩
    refine ⟨hij, not_lt_of_ge hji, ?_⟩
    intro h
    exact lt_asymm hij (posetLt_implies_lt H h)
  · rintro ⟨hij, hn, _⟩
    exact ⟨hij, le_of_not_gt hn⟩

/-- Each color class is a chain in the actual naturally labelled poset. -/
theorem same_color_comparable {n m : ℕ} (H : NaturalUnitInterval n)
    (κ : Fin n → Fin m) (hp : Proper H κ) {i j : Fin n} (hij : i < j)
    (hc : κ i = κ j) : PosetLt H i j := by
  by_contra hn
  exact hp i j ⟨hij, le_of_not_gt hn⟩ hc

def colorClass {n m : ℕ} (κ : Fin n → Fin m) (c : Fin m) : Finset (Fin n) :=
  Finset.univ.filter (fun i => κ i = c)

theorem colorClass_card_le_two {n m : ℕ} (H : NaturalUnitInterval n)
    (hh : HeightTwo H) (κ : Fin n → Fin m) (hp : Proper H κ) (c : Fin m) :
    (colorClass κ c).card ≤ 2 := by
  classical
  by_contra hcard
  obtain ⟨x, y, z, hx, hy, hz, hxy, hxz, hyz⟩ :=
    Finset.two_lt_card_iff.mp (by omega : 2 < (colorClass κ c).card)
  have hxc : κ x = c := (Finset.mem_filter.mp hx).2
  have hyc : κ y = c := (Finset.mem_filter.mp hy).2
  have hzc : κ z = c := (Finset.mem_filter.mp hz).2
  have no_three : ∀ u v w : Fin n, u < v → v < w →
      κ u = c → κ v = c → κ w = c → False := by
    intro u v w huv hvw hu hv hw
    exact hh u v w ⟨same_color_comparable H κ hp huv (hu.trans hv.symm),
      same_color_comparable H κ hp hvw (hv.trans hw.symm)⟩
  by_cases h1 : x < y
  · by_cases h2 : y < z
    · exact no_three x y z h1 h2 hxc hyc hzc
    · by_cases h3 : x < z
      · exact no_three x z y h3 (by omega) hxc hzc hyc
      · exact no_three z x y (by omega) h1 hzc hxc hyc
  · by_cases h2 : x < z
    · exact no_three y x z (by omega) h2 hyc hxc hzc
    · by_cases h3 : y < z
      · exact no_three y z x h3 (by omega) hyc hzc hxc
      · exact no_three z y x (by omega) (by omega) hzc hyc hxc

def reverseColors {n m : ℕ} (κ : Fin n → Fin m) : Fin n → Fin m :=
  fun i => Fin.rev (κ i)

theorem reverseColors_involutive {n m : ℕ} (κ : Fin n → Fin m) :
    reverseColors (reverseColors κ) = κ := by
  funext i
  exact Fin.rev_rev _

theorem proper_reverseColors_iff {n m : ℕ} (H : NaturalUnitInterval n)
    (κ : Fin n → Fin m) : Proper H (reverseColors κ) ↔ Proper H κ := by
  constructor
  · intro hp i j he hc
    exact hp i j he (congrArg Fin.rev hc)
  · intro hp i j he hc
    exact hp i j he (Fin.rev_inj.mp hc)

theorem ascents_reverseColors {n m : ℕ} (H : NaturalUnitInterval n)
    (κ : Fin n → Fin m) : ascents H (reverseColors κ) = descents H κ := by
  classical
  unfold ascents descents
  congr 1
  ext p
  simp only [Finset.mem_filter, Finset.mem_univ, true_and]
  change (Edge H p.1 p.2 ∧ Fin.rev (κ p.1) < Fin.rev (κ p.2)) ↔ _
  rw [Fin.rev_lt_rev]

theorem descents_reverseColors {n m : ℕ} (H : NaturalUnitInterval n)
    (κ : Fin n → Fin m) : descents H (reverseColors κ) = ascents H κ := by
  classical
  unfold ascents descents
  congr 1
  ext p
  simp only [Finset.mem_filter, Finset.mem_univ, true_and]
  change (Edge H p.1 p.2 ∧ Fin.rev (κ p.2) < Fin.rev (κ p.1)) ↔ _
  rw [Fin.rev_lt_rev]

/-- Edge inversions when color classes are arranged in increasing color rows.
Connecting these finite pairs with the original list statistic is a separate
array-to-coloring obligation. -/
def colorRowInversions {n m : ℕ} (H : NaturalUnitInterval n)
    (κ : Fin n → Fin m) : ℕ := by
  classical
  exact (Finset.univ.filter (fun p : Fin n × Fin n =>
    p.1 < p.2 ∧ ¬ PosetLt H p.1 p.2 ∧ ¬ PosetLt H p.2 p.1 ∧ κ p.2 < κ p.1)).card

theorem descents_eq_colorRowInversions {n m : ℕ} (H : NaturalUnitInterval n)
    (κ : Fin n → Fin m) : descents H κ = colorRowInversions H κ := by
  classical
  unfold descents colorRowInversions
  congr 1
  ext p
  simp only [Finset.mem_filter, Finset.mem_univ, true_and, edge_iff_incomparable]
  tauto

end PartitionH3

#check @PartitionH3.colorClass_card_le_two
#check @PartitionH3.descents_eq_colorRowInversions
#print axioms PartitionH3.edge_iff_incomparable
#print axioms PartitionH3.same_color_comparable
#print axioms PartitionH3.colorClass_card_le_two
#print axioms PartitionH3.reverseColors_involutive
#print axioms PartitionH3.proper_reverseColors_iff
#print axioms PartitionH3.ascents_reverseColors
#print axioms PartitionH3.descents_reverseColors
#print axioms PartitionH3.descents_eq_colorRowInversions
