import PartitionH3.H3

/-! The actual coloring and survivor formula over natural coefficients.
The signed proof is transported through an injective coefficient map;
the natural polynomial is defined by the original finite combinatorial sums.
-/

open scoped BigOperators

noncomputable section

namespace PartitionH3

abbrev NatCoeff := Polynomial ℕ
abbrev NatPoly (r : ℕ) := MvPolynomial (Fin r) NatCoeff

def natColorMonomial {n r : ℕ} (κ : Fin n → Fin r) : NatPoly r :=
  ∏ i, MvPolynomial.X (κ i)

def natChromatic {n : ℕ} (H : NaturalUnitInterval n) (r : ℕ) : NatPoly r := by
  classical
  exact ∑ κ : Fin n → Fin r,
    if Proper H κ then MvPolynomial.C (Polynomial.X ^ ascents H κ) * natColorMonomial κ else 0

def natElementary (r k : ℕ) : NatPoly r := MvPolynomial.esymm (Fin r) NatCoeff k

def natTableauWeight {n : ℕ} (H : NaturalUnitInterval n)
    (family : List CornerSlide.Rows) : NatCoeff :=
  (family.map (fun rows =>
    Polynomial.X ^ CornerSlide.tableauGraphInversions (natLt H) rows)).sum

def natSurvivorCoefficient {n : ℕ} (H : NaturalUnitInterval n) (k : ℕ) : NatCoeff :=
  natTableauWeight H (CornerSlide.survivorFamily (natLt H) (List.range n) k)

def coefficientCast : NatCoeff →+* Coeff :=
  (Polynomial.toFinsuppIso ℤ).symm.toRingHom.comp
    ((AddMonoidAlgebra.mapRingHom ℕ (Nat.castRingHom ℤ)).comp
      (Polynomial.toFinsuppIso ℕ).toRingHom)

def naturalCast (r : ℕ) : NatPoly r →+* Poly r := MvPolynomial.map coefficientCast

theorem coefficientCast_injective : Function.Injective coefficientCast := by
  intro p q hp
  apply Polynomial.ext
  intro d
  have hd := congrArg (fun p : Coeff => p.coeff d) hp
  change (p.coeff d : ℤ) = (q.coeff d : ℤ) at hd
  exact Nat.cast_injective hd

theorem naturalCast_injective (r : ℕ) : Function.Injective (naturalCast r) := by
  exact MvPolynomial.map_injective coefficientCast coefficientCast_injective

theorem coefficientCast_X : coefficientCast Polynomial.X = Polynomial.X := by
  apply Polynomial.ext
  intro d
  change ((Polynomial.X : NatCoeff).coeff d : ℤ) = (Polynomial.X : Coeff).coeff d
  simp [Polynomial.coeff_X]

theorem naturalCast_colorMonomial {n r : ℕ} (κ : Fin n → Fin r) :
    naturalCast r (natColorMonomial κ) = colorMonomial κ := by
  simp [naturalCast, natColorMonomial, colorMonomial]

theorem naturalCast_chromatic {n : ℕ} (H : NaturalUnitInterval n) (r : ℕ) :
    naturalCast r (natChromatic H r) = chromatic H r := by
  classical
  simp only [natChromatic, chromatic, map_sum]
  apply Finset.sum_congr rfl
  intro κ _
  by_cases hp : Proper H κ
  · simp only [hp, reduceIte, map_mul, naturalCast_colorMonomial]
    rw [naturalCast, MvPolynomial.map_C, map_pow, coefficientCast_X]
  · simp only [hp, reduceIte, map_zero]

theorem naturalCast_elementary (r k : ℕ) :
    naturalCast r (natElementary r k) = elementary r k := by
  simp [naturalCast, natElementary, elementary, MvPolynomial.esymm]

theorem coefficientCast_tableauWeight {n : ℕ} (H : NaturalUnitInterval n)
    (family : List CornerSlide.Rows) :
    coefficientCast (natTableauWeight H family) = tableauWeight H family := by
  induction family with
  | nil => simp [natTableauWeight, tableauWeight]
  | cons rows family ih =>
    simp only [natTableauWeight, tableauWeight, List.map_cons, List.sum_cons] at ih ⊢
    rw [map_add, map_pow, coefficientCast_X, ih]

theorem coefficientCast_survivorCoefficient {n : ℕ} (H : NaturalUnitInterval n) (k : ℕ) :
    coefficientCast (natSurvivorCoefficient H k) = survivorCoefficient H k :=
  coefficientCast_tableauWeight H _

/-- The all-alphabet formula in the natural coefficient semiring itself. -/
theorem height_two_survivor_expansion_nat {n : ℕ} (H : NaturalUnitInterval n)
    (hh : HeightTwo H) (r : ℕ) :
    natChromatic H r =
      ∑ k ∈ Finset.range (n / 2 + 1),
        MvPolynomial.C (natSurvivorCoefficient H k) *
          natElementary r (n - k) * natElementary r k := by
  apply naturalCast_injective r
  simp only [map_sum, map_mul, naturalCast_chromatic, naturalCast_elementary]
  simp only [naturalCast, MvPolynomial.map_C, coefficientCast_survivorCoefficient]
  exact height_two_survivor_expansion H hh r

end PartitionH3

#check @PartitionH3.height_two_survivor_expansion_nat
#print axioms PartitionH3.coefficientCast_injective
#print axioms PartitionH3.naturalCast_injective
#print axioms PartitionH3.naturalCast_colorMonomial
#print axioms PartitionH3.naturalCast_chromatic
#print axioms PartitionH3.naturalCast_elementary
#print axioms PartitionH3.coefficientCast_tableauWeight
#print axioms PartitionH3.coefficientCast_survivorCoefficient
#print axioms PartitionH3.height_two_survivor_expansion_nat
