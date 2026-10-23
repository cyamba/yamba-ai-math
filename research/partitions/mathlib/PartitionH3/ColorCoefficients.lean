import PartitionH3.ColorSymmetry
import PartitionH3.Reconstruction

/-!
Coefficient extraction from actual proper colorings. The exponent constraint
is retained as an equality of natural exponent vectors; the corresponding
signed integer row-shape equation is proved separately below.
-/

open scoped BigOperators

noncomputable section

namespace PartitionH3

attribute [local instance] Classical.propDecidable

def colorDegree {n m : ℕ} (κ : Fin n → Fin m) (c : Fin m) : ℕ :=
  (colorClass κ c).card

def weightedChromatic {n m : ℕ} (H : NaturalUnitInterval n)
    (w : (Fin n → Fin m) → Coeff) : Poly m := by
  classical
  exact ∑ κ : Fin n → Fin m,
    if Proper H κ then MvPolynomial.C (w κ) * colorMonomial κ else 0

theorem chromatic_eq_weighted {n m : ℕ} (H : NaturalUnitInterval n) :
    chromatic H m = weightedChromatic H (fun κ => Polynomial.X ^ ascents H κ) := rfl

theorem colorMonomial_eq_powerMonomial {n m : ℕ} (κ : Fin n → Fin m) :
    colorMonomial κ = powerMonomial (colorDegree κ) := by
  simpa only [colorMonomial, powerMonomial, colorDegree, colorClass] using
    prod_colorPowers κ Finset.univ (fun c => MvPolynomial.X c)

theorem powerMonomial_mul {m : ℕ} (gamma eta : Fin m → ℕ) :
    powerMonomial gamma * powerMonomial eta =
      powerMonomial (fun i => gamma i + eta i) := by
  simp only [powerMonomial, pow_add, Finset.prod_mul_distrib]

theorem weightedChromatic_power_coefficient {n m : ℕ} (H : NaturalUnitInterval n)
    (w : (Fin n → Fin m) → Coeff) (gamma alpha : Fin m → ℕ) :
    (powerMonomial gamma * weightedChromatic H w).coeff (powerExponent alpha) =
      ∑ κ : Fin n → Fin m,
        if Proper H κ ∧ (fun i => gamma i + colorDegree κ i) = alpha then w κ else 0 := by
  classical
  rw [weightedChromatic, Finset.mul_sum, MvPolynomial.coeff_sum]
  apply Finset.sum_congr rfl
  intro κ _
  by_cases hp : Proper H κ
  · simp only [hp, reduceIte, true_and]
    rw [mul_left_comm, colorMonomial_eq_powerMonomial, powerMonomial_mul,
      MvPolynomial.coeff_C_mul, powerMonomial_eq_monomial, MvPolynomial.coeff_monomial]
    simp only [powerExponent_injective.eq_iff]
    split_ifs <;> simp
  · simp [hp]

theorem coeff_rename_at {m : ℕ} (p : Poly m) (alpha : Fin m → ℕ)
    (sigma : Equiv.Perm (Fin m)) :
    (MvPolynomial.rename sigma p).coeff (powerExponent alpha) =
      p.coeff (powerExponent (fun i => alpha (sigma i))) := by
  have hc := coeff_rename_powerExponent p (fun i => alpha (sigma i)) sigma
  simpa only [Equiv.apply_symm_apply] using hc

/-- Exact signed coefficient extraction; no tableau expansion is assumed. -/
theorem vandermonde_weighted_coefficient {n m : ℕ} (H : NaturalUnitInterval n)
    (w : (Fin n → Fin m) → Coeff) (hs : MvPolynomial.IsSymmetric (weightedChromatic H w))
    (alpha : Fin m → ℕ) :
    (vandermonde m * weightedChromatic H w).coeff (powerExponent alpha) =
      ∑ sigma : Equiv.Perm (Fin m), ∑ κ : Fin n → Fin m,
        if Proper H κ ∧ (fun i => delta m i + colorDegree κ i) =
            (fun i => alpha (sigma i)) then
          (((Equiv.Perm.sign sigma : ℤ) : Coeff)) * w κ else 0 := by
  classical
  change (alternant (delta m) * weightedChromatic H w).coeff _ = _
  rw [alternant, ← antisymmetrize_mul_symmetric _ _ hs,
    antisymmetrize, MvPolynomial.coeff_sum]
  apply Finset.sum_congr rfl
  intro sigma _
  rw [signCoeff_eq_C, MvPolynomial.coeff_C_mul, coeff_rename_at,
    weightedChromatic_power_coefficient, Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro κ _
  split_ifs <;> simp

def chromaticDesc {n : ℕ} (H : NaturalUnitInterval n) (m : ℕ) : Poly m :=
  weightedChromatic H (fun κ => Polynomial.X ^ descents H κ)

theorem chromaticDesc_eq_rename_reverse {n m : ℕ} (H : NaturalUnitInterval n) :
    chromaticDesc H m = MvPolynomial.rename Fin.rev (chromatic H m) := by
  classical
  let e : (Fin n → Fin m) ≃ (Fin n → Fin m) :=
    Function.Involutive.toPerm reverseColors reverseColors_involutive
  unfold chromaticDesc weightedChromatic chromatic
  rw [map_sum]
  apply Fintype.sum_equiv e
  intro κ
  change (if Proper H κ then MvPolynomial.C (Polynomial.X ^ descents H κ) *
      colorMonomial κ else 0) =
    MvPolynomial.rename Fin.rev (if Proper H (reverseColors κ) then
      MvPolynomial.C (Polynomial.X ^ ascents H (reverseColors κ)) *
        colorMonomial (reverseColors κ) else 0)
  by_cases hp : Proper H κ
  · simp [hp, proper_reverseColors_iff, ascents_reverseColors, colorMonomial,
      map_prod, MvPolynomial.rename_X, reverseColors]
  · simp [hp, proper_reverseColors_iff]

theorem chromaticDesc_eq_chromatic {n m : ℕ} (H : NaturalUnitInterval n)
    (hh : HeightTwo H) : chromaticDesc H m = chromatic H m := by
  rw [chromaticDesc_eq_rename_reverse]
  exact chromatic_isSymmetric H hh Fin.revPerm

theorem shifted_color_shape {n m : ℕ} (κ : Fin n → Fin m)
    (lambda : Fin m → ℕ) (sigma : Equiv.Perm (Fin m)) :
    (fun i => delta m i + colorDegree κ i) =
        (fun i => delta m (sigma i) + lambda (sigma i)) ↔
      ∀ i, (colorDegree κ i : ℤ) =
        (lambda (sigma i) : ℤ) - ((sigma i).val : ℤ) + (i.val : ℤ) := by
  constructor
  · intro h i
    have hi := congrFun h i
    have hd := delta_cast m i
    have hd' := delta_cast m (sigma i)
    omega
  · intro h
    funext i
    have hi := h i
    have hd := delta_cast m i
    have hd' := delta_cast m (sigma i)
    omega

/-- Actual proper-coloring coefficients with the signed integer shape
constraint. Empty and negative requested row lengths are handled literally. -/
theorem vandermonde_chromatic_coefficient {n m : ℕ} (H : NaturalUnitInterval n)
    (hh : HeightTwo H) (lambda : Fin m → ℕ) :
    (vandermonde m * chromatic H m).coeff
        (powerExponent (fun i => delta m i + lambda i)) =
      ∑ sigma : Equiv.Perm (Fin m), ∑ κ : Fin n → Fin m,
        if Proper H κ ∧ (∀ i, (colorDegree κ i : ℤ) =
            (lambda (sigma i) : ℤ) - ((sigma i).val : ℤ) + (i.val : ℤ)) then
          (((Equiv.Perm.sign sigma : ℤ) : Coeff)) * Polynomial.X ^ descents H κ else 0 := by
  classical
  have hs : MvPolynomial.IsSymmetric
      (weightedChromatic H (fun κ : Fin n → Fin m => Polynomial.X ^ descents H κ)) := by
    change MvPolynomial.IsSymmetric (chromaticDesc H m)
    rw [chromaticDesc_eq_chromatic H hh]
    exact chromatic_isSymmetric H hh
  rw [← chromaticDesc_eq_chromatic H hh]
  rw [chromaticDesc, vandermonde_weighted_coefficient H _ hs]
  apply Finset.sum_congr rfl
  intro sigma _
  apply Finset.sum_congr rfl
  intro κ _
  simp only [shifted_color_shape]

end PartitionH3

#check @PartitionH3.vandermonde_weighted_coefficient
#print axioms PartitionH3.colorMonomial_eq_powerMonomial
#print axioms PartitionH3.weightedChromatic_power_coefficient
#print axioms PartitionH3.coeff_rename_at
#print axioms PartitionH3.vandermonde_weighted_coefficient
#print axioms PartitionH3.chromaticDesc_eq_rename_reverse
#check @PartitionH3.vandermonde_chromatic_coefficient
#print axioms PartitionH3.chromaticDesc_eq_chromatic
#print axioms PartitionH3.shifted_color_shape
#print axioms PartitionH3.vandermonde_chromatic_coefficient
