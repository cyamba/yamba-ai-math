import PartitionH3.Alternant

open scoped BigOperators

noncomputable section

namespace PartitionH3

def powerExponent {m : ℕ} (gamma : Fin m → ℕ) : Fin m →₀ ℕ :=
  Finsupp.onFinset Finset.univ gamma (by simp)

@[simp] theorem powerExponent_apply {m : ℕ} (gamma : Fin m → ℕ) (i : Fin m) :
    powerExponent gamma i = gamma i := by
  simp [powerExponent]

theorem powerExponent_injective {m : ℕ} :
    Function.Injective (@powerExponent m) := by
  intro f g h
  funext i
  simpa only [powerExponent_apply] using congrArg (fun e => e i) h

theorem powerMonomial_eq_monomial {m : ℕ} (gamma : Fin m → ℕ) :
    powerMonomial gamma = MvPolynomial.monomial (powerExponent gamma) 1 := by
  unfold powerMonomial
  rw [MvPolynomial.prod_X_pow]
  congr 1
  ext i
  simp [powerExponent, Finsupp.indicator]

theorem rename_powerMonomial {m : ℕ} (sigma : Equiv.Perm (Fin m))
    (gamma : Fin m → ℕ) :
    MvPolynomial.rename sigma (powerMonomial gamma) =
      powerMonomial (fun i => gamma (sigma.symm i)) := by
  calc
    MvPolynomial.rename sigma (powerMonomial gamma) =
        ∏ i, (MvPolynomial.X (sigma i) : Poly m) ^ gamma (sigma.symm (sigma i)) := by
      simp only [powerMonomial, map_prod, map_pow, MvPolynomial.rename_X,
        Equiv.symm_apply_apply]
    _ = powerMonomial (fun i => gamma (sigma.symm i)) :=
      Equiv.prod_comp sigma (fun i => (MvPolynomial.X i : Poly m) ^ gamma (sigma.symm i))

theorem delta_injective (m : ℕ) : Function.Injective (delta m) := by
  intro i j h
  have he := congrArg (fun k : ℕ => (k : ℤ)) h
  rw [delta_cast, delta_cast] at he
  apply Fin.ext
  omega

theorem delta_permutation_eq_iff {m : ℕ} (sigma : Equiv.Perm (Fin m)) :
    powerExponent (fun i => delta m (sigma.symm i)) = powerExponent (delta m) ↔
      sigma = 1 := by
  constructor
  · intro h
    have he := powerExponent_injective h
    apply Equiv.ext
    intro i
    have hi := congrFun he (sigma i)
    simpa only [Equiv.symm_apply_apply, Equiv.Perm.one_apply] using
      ((delta_injective m) hi).symm
  · rintro rfl
    rfl

theorem coeff_signed_delta {m : ℕ} (sigma : Equiv.Perm (Fin m)) :
    (signCoeff sigma * MvPolynomial.rename sigma (powerMonomial (delta m))).coeff
      (powerExponent (delta m)) = if sigma = 1 then 1 else 0 := by
  classical
  have hc : signCoeff sigma =
      MvPolynomial.C (((Equiv.Perm.sign sigma : ℤ) : Coeff)) := by
    simp [signCoeff]
  rw [hc, MvPolynomial.coeff_C_mul, rename_powerMonomial, powerMonomial_eq_monomial,
    MvPolynomial.coeff_monomial]
  simp only [delta_permutation_eq_iff]
  split_ifs with hs
  · subst sigma
    simp
  · simp

/-- The coefficient at the strictly decreasing delta vector is exactly one,
including the zero-variable case. -/
theorem vandermonde_delta_coefficient (m : ℕ) :
    (vandermonde m).coeff (powerExponent (delta m)) = 1 := by
  classical
  unfold vandermonde alternant antisymmetrize
  rw [MvPolynomial.coeff_sum]
  simp only [coeff_signed_delta]
  simp

theorem vandermonde_ne_zero (m : ℕ) : vandermonde m ≠ 0 := by
  intro h
  have hc := congrArg (fun p : Poly m => p.coeff (powerExponent (delta m))) h
  rw [vandermonde_delta_coefficient] at hc
  simp at hc

theorem vandermonde_cancel {m : ℕ} (p q : Poly m) :
    vandermonde m * p = vandermonde m * q ↔ p = q := by
  constructor
  · exact mul_left_cancel₀ (vandermonde_ne_zero m)
  · rintro rfl
    rfl

theorem vandermonde_empty : vandermonde 0 = 1 := by
  simp [vandermonde, alternant_eq_sum, signCoeff]

end PartitionH3

#check @PartitionH3.vandermonde_delta_coefficient
#check @PartitionH3.vandermonde_cancel
#print axioms PartitionH3.delta_injective
#print axioms PartitionH3.coeff_signed_delta
#print axioms PartitionH3.vandermonde_delta_coefficient
#print axioms PartitionH3.vandermonde_ne_zero
#print axioms PartitionH3.vandermonde_cancel
#print axioms PartitionH3.vandermonde_empty
