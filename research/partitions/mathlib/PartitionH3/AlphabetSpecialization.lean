import PartitionH3.SurvivorAlgebra

/-! Setting the variables outside a smaller initial alphabet to zero. The
maps and finite sums include an empty target alphabet. -/

open scoped BigOperators

noncomputable section

namespace PartitionH3

attribute [local instance] Classical.propDecidable

def lowerVariable (r : ℕ) {m : ℕ} (c : Fin m) : Poly r :=
  if hc : c.val < r then MvPolynomial.X ⟨c.val, hc⟩ else 0

def specialize {r m : ℕ} (_h : r ≤ m) : Poly m →+* Poly r :=
  MvPolynomial.eval₂Hom MvPolynomial.C (lowerVariable r)

theorem specialize_C {r m : ℕ} (h : r ≤ m) (c : Coeff) :
    specialize h (MvPolynomial.C c) = MvPolynomial.C c :=
  MvPolynomial.eval₂Hom_C _ _ _

theorem specialize_X {r m : ℕ} (h : r ≤ m) (c : Fin m) :
    specialize h (MvPolynomial.X c) = lowerVariable r c :=
  MvPolynomial.eval₂Hom_X' _ _ _

def liftColor {n r m : ℕ} (h : r ≤ m) (κ : Fin n → Fin r) : Fin n → Fin m :=
  fun v => Fin.castLE h (κ v)

theorem liftColor_injective {n r m : ℕ} (h : r ≤ m) :
    Function.Injective (liftColor (n := n) h) := by
  intro κ ρ he
  funext v
  apply Fin.ext
  exact congrArg (fun f : Fin n → Fin m => (f v).val) he

theorem proper_liftColor {n r m : ℕ} (H : NaturalUnitInterval n)
    (h : r ≤ m) (κ : Fin n → Fin r) : Proper H (liftColor h κ) ↔ Proper H κ := by
  constructor
  · intro hp i j he hc
    apply hp i j he
    exact congrArg (Fin.castLE h) hc
  · intro hp i j he hc
    apply hp i j he
    exact Fin.ext (congrArg (fun c : Fin m => c.val) hc)

theorem ascents_liftColor {n r m : ℕ} (H : NaturalUnitInterval n)
    (h : r ≤ m) (κ : Fin n → Fin r) : ascents H (liftColor h κ) = ascents H κ := rfl

theorem specialize_colorMonomial_lift {n r m : ℕ} (h : r ≤ m)
    (κ : Fin n → Fin r) :
    specialize h (colorMonomial (liftColor h κ)) = colorMonomial κ := by
  simp only [colorMonomial, map_prod, specialize_X]
  apply Finset.prod_congr rfl
  intro v _
  rw [lowerVariable, dite_eq_left (show (liftColor h κ v).val < r from (κ v).isLt)]
  apply congrArg MvPolynomial.X
  exact Fin.ext rfl

theorem specialize_colorMonomial_zero {n r m : ℕ} (h : r ≤ m)
    (κ : Fin n → Fin m) (v : Fin n) (hv : ¬ (κ v).val < r) :
    specialize h (colorMonomial κ) = 0 := by
  simp only [colorMonomial, map_prod, specialize_X]
  apply Finset.prod_eq_zero (Finset.mem_univ v)
  simp only [lowerVariable, dite_eq_right hv]

theorem coloring_in_lift_image {n r m : ℕ} (h : r ≤ m) (κ : Fin n → Fin m)
    (hall : ∀ v, (κ v).val < r) :
    κ ∈ Finset.univ.image (liftColor (n := n) h) := by
  let ρ : Fin n → Fin r := fun v => ⟨(κ v).val, hall v⟩
  apply Finset.mem_image.mpr
  refine ⟨ρ, Finset.mem_univ _, ?_⟩
  funext v
  exact Fin.ext rfl

theorem specialize_chromatic {n r m : ℕ} (H : NaturalUnitInterval n) (h : r ≤ m) :
    specialize h (chromatic H m) = chromatic H r := by
  rw [chromatic, map_sum]
  let f := fun κ : Fin n → Fin m => specialize h
    (if Proper H κ then MvPolynomial.C (Polynomial.X ^ ascents H κ) * colorMonomial κ else 0)
  change (∑ κ, f κ) = _
  calc
    _ = ∑ κ ∈ Finset.univ.image (liftColor (n := n) h), f κ := by
      symm
      apply Finset.sum_subset (Finset.subset_univ _)
      intro κ _ hnot
      have hbad : ¬ ∀ v, (κ v).val < r := fun hall => hnot (coloring_in_lift_image h κ hall)
      obtain ⟨v, hv⟩ := not_forall.mp hbad
      by_cases hp : Proper H κ
      · simp only [f, hp, reduceIte, map_mul, specialize_C,
          specialize_colorMonomial_zero h κ v hv, mul_zero]
      · simp only [f, hp, reduceIte, map_zero]
    _ = ∑ ρ : Fin n → Fin r, f (liftColor h ρ) := by
      rw [Finset.sum_image]
      exact fun _ _ _ _ he => liftColor_injective h he
    _ = _ := by
      rw [chromatic]
      apply Finset.sum_congr rfl
      intro ρ _
      by_cases hp : Proper H ρ
      · simp only [f, (proper_liftColor H h ρ).mpr hp, hp, reduceIte,
          map_mul, specialize_C, ascents_liftColor, specialize_colorMonomial_lift]
      · simp only [f, proper_liftColor H h ρ, hp, reduceIte, map_zero]

theorem alphabetCast_injective {r m : ℕ} (h : r ≤ m) :
    Function.Injective (Fin.castLE h) := by
  intro c d he
  exact Fin.ext (congrArg (fun c : Fin m => c.val) he)

theorem mem_alphabet_image {r m : ℕ} (h : r ≤ m) (c : Fin m) :
    c ∈ Finset.univ.image (Fin.castLE h) ↔ c.val < r := by
  constructor
  · intro hc
    obtain ⟨d, _, rfl⟩ := Finset.mem_image.mp hc
    exact d.isLt
  · intro hc
    exact Finset.mem_image.mpr ⟨⟨c.val, hc⟩, Finset.mem_univ _, Fin.ext rfl⟩

theorem specialize_elementary {r m : ℕ} (h : r ≤ m) (k : ℕ) :
    specialize h (elementary m k) = elementary r k := by
  let S := (Finset.univ : Finset (Fin r)).powersetCard k
  let T := (Finset.univ : Finset (Fin m)).powersetCard k
  let g := fun s : Finset (Fin m) => ∏ c ∈ s, lowerVariable r c
  have hsub : S.image (fun t => t.image (Fin.castLE h)) ⊆ T := by
    intro s hs
    obtain ⟨t, ht, rfl⟩ := Finset.mem_image.mp hs
    apply Finset.mem_powersetCard.mpr
    refine ⟨Finset.subset_univ _, ?_⟩
    rw [Finset.card_image_of_injective _ (alphabetCast_injective h)]
    exact (Finset.mem_powersetCard.mp ht).2
  simp only [elementary, MvPolynomial.esymm, map_sum, map_prod, specialize_X]
  change (∑ s ∈ T, g s) = ∑ t ∈ S, ∏ c ∈ t, MvPolynomial.X c
  calc
    _ = ∑ s ∈ S.image (fun t => t.image (Fin.castLE h)), g s := by
      symm
      apply Finset.sum_subset hsub
      intro s hs hnot
      have hbad : ∃ c ∈ s, ¬ c.val < r := by
        by_contra! hall
        have hsrange : s ⊆ Finset.univ.image (Fin.castLE h) := by
          intro c hc
          exact (mem_alphabet_image h c).mpr (hall c hc)
        obtain ⟨t, ht⟩ := Finset.subset_univ_image_iff.mp hsrange
        have hcard := Finset.card_image_of_injective t (alphabetCast_injective h)
        rw [ht] at hcard
        have htk : t.card = k := hcard.symm.trans (Finset.mem_powersetCard.mp hs).2
        exact hnot (Finset.mem_image.mpr ⟨t,
          Finset.mem_powersetCard.mpr ⟨Finset.subset_univ _, htk⟩, ht⟩)
      obtain ⟨c, hc, hcr⟩ := hbad
      change (∏ d ∈ s, lowerVariable r d) = 0
      apply Finset.prod_eq_zero hc
      simp only [lowerVariable, dite_eq_right hcr]
    _ = ∑ t ∈ S, g (t.image (Fin.castLE h)) := by
      rw [Finset.sum_image]
      exact fun _ _ _ _ he => Finset.image_injective (alphabetCast_injective h) he
    _ = _ := by
      apply Finset.sum_congr rfl
      intro t _
      dsimp only [g]
      rw [Finset.prod_image]
      · apply Finset.prod_congr rfl
        intro c _
        simp only [lowerVariable, Fin.val_castLE, dite_eq_left c.isLt]
      · exact fun _ _ _ _ he => alphabetCast_injective h he

theorem specialize_survivorExpansion {n r m : ℕ} (H : NaturalUnitInterval n)
    (h : r ≤ m) :
    specialize h (survivorExpansion H m) = survivorExpansion H r := by
  simp only [survivorExpansion, map_sum, map_mul, specialize_C, specialize_elementary]

end PartitionH3

#check @PartitionH3.specialize_chromatic
#print axioms PartitionH3.liftColor_injective
#print axioms PartitionH3.proper_liftColor
#print axioms PartitionH3.specialize_colorMonomial_lift
#print axioms PartitionH3.specialize_colorMonomial_zero
#print axioms PartitionH3.specialize_chromatic
#print axioms PartitionH3.specialize_elementary
#print axioms PartitionH3.specialize_survivorExpansion
