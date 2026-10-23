import PartitionH3.Vandermonde
import Mathlib.Data.Fin.Tuple.Sort

/-!
Alternating polynomials over `ℤ[q]` are determined by the coefficients at
strictly decreasing natural exponent vectors. Their finite-support expansion
uses these coefficients and the actual signed monomial alternants.
-/

open scoped BigOperators

noncomputable section

namespace PartitionH3

def IsAlternating {m : ℕ} (p : Poly m) : Prop :=
  ∀ sigma : Equiv.Perm (Fin m),
    MvPolynomial.rename sigma p = signCoeff sigma * p

theorem signCoeff_inv {m : ℕ} (sigma : Equiv.Perm (Fin m)) :
    signCoeff sigma⁻¹ = signCoeff sigma := by
  simp [signCoeff, Equiv.Perm.sign_inv]

theorem signCoeff_mul_self {m : ℕ} (sigma : Equiv.Perm (Fin m)) :
    signCoeff sigma * signCoeff sigma = 1 := by
  rw [← signCoeff_inv sigma, ← signCoeff_mul]
  simp [signCoeff]

theorem rename_signCoeff {m : ℕ} (sigma tau : Equiv.Perm (Fin m)) :
    MvPolynomial.rename sigma (signCoeff tau) = signCoeff tau := by
  simp [signCoeff]

theorem signCoeff_eq_C {m : ℕ} (sigma : Equiv.Perm (Fin m)) :
    signCoeff sigma = MvPolynomial.C (((Equiv.Perm.sign sigma : ℤ) : Coeff)) := by
  simp [signCoeff]

theorem rename_antisymmetrize {m : ℕ} (p : Poly m) (sigma : Equiv.Perm (Fin m)) :
    MvPolynomial.rename sigma (antisymmetrize p) =
      signCoeff sigma * antisymmetrize p := by
  classical
  simp only [antisymmetrize, map_sum, map_mul, rename_signCoeff,
    rename_perm_mul, Finset.mul_sum]
  apply Fintype.sum_equiv (Equiv.mulLeft sigma)
  intro tau
  simp only [Equiv.coe_mulLeft, signCoeff_mul]
  rw [← mul_assoc, ← mul_assoc, signCoeff_mul_self, one_mul]

theorem alternant_isAlternating {m : ℕ} (gamma : Fin m → ℕ) :
    IsAlternating (alternant gamma) := by
  intro sigma
  exact rename_antisymmetrize _ sigma

theorem powerExponent_mapDomain {m : ℕ} (gamma : Fin m → ℕ)
    (sigma : Equiv.Perm (Fin m)) :
    (powerExponent gamma).mapDomain sigma =
      powerExponent (fun i => gamma (sigma.symm i)) := by
  ext i
  simp

theorem coeff_rename_powerExponent {m : ℕ} (p : Poly m) (gamma : Fin m → ℕ)
    (sigma : Equiv.Perm (Fin m)) :
    (MvPolynomial.rename sigma p).coeff
      (powerExponent (fun i => gamma (sigma.symm i))) =
      p.coeff (powerExponent gamma) := by
  rw [← powerExponent_mapDomain]
  exact MvPolynomial.coeff_rename_mapDomain sigma sigma.injective p _

/-- Coefficients transform with the same genuine permutation sign. -/
theorem alternating_coefficient_perm {m : ℕ} (p : Poly m) (hp : IsAlternating p)
    (gamma : Fin m → ℕ) (sigma : Equiv.Perm (Fin m)) :
    p.coeff (powerExponent gamma) =
      (((Equiv.Perm.sign sigma : ℤ) : Coeff)) *
        p.coeff (powerExponent (fun i => gamma (sigma.symm i))) := by
  rw [← coeff_rename_powerExponent p gamma sigma, hp sigma,
    signCoeff_eq_C, MvPolynomial.coeff_C_mul]

theorem alternating_coefficient_eq_zero_of_eq {m : ℕ} (p : Poly m)
    (hp : IsAlternating p) (gamma : Fin m → ℕ) (i j : Fin m)
    (hij : i ≠ j) (he : gamma i = gamma j) :
    p.coeff (powerExponent gamma) = 0 := by
  have hgamma : (fun k => gamma ((Equiv.swap i j).symm k)) = gamma := by
    funext k
    by_cases hi : k = i
    · subst k
      simpa using he.symm
    · by_cases hj : k = j
      · subst k
        simpa using he
      · simp [Equiv.swap_apply_def, hi, hj]
  have hc := alternating_coefficient_perm p hp gamma (Equiv.swap i j)
  rw [hgamma] at hc
  have hn : p.coeff (powerExponent gamma) = -p.coeff (powerExponent gamma) := by
    simpa [Equiv.Perm.sign_swap hij] using hc
  apply Polynomial.ext
  intro n
  have hcn := congrArg (fun f : Coeff => f.coeff n) hn
  exact CharZero.eq_neg_self_iff.mp (by simpa only [Polynomial.coeff_neg] using hcn)

/-- No exponent positivity or nonempty alphabet hypothesis is needed. -/
theorem alternating_eq_of_dominant_coeff {m : ℕ} (p q : Poly m)
    (hp : IsAlternating p) (hq : IsAlternating q)
    (hc : ∀ gamma : Fin m → ℕ, StrictAnti gamma →
      p.coeff (powerExponent gamma) = q.coeff (powerExponent gamma)) : p = q := by
  classical
  apply MvPolynomial.ext
  intro e
  let gamma : Fin m → ℕ := fun i => e i
  have he : powerExponent gamma = e := by ext i; simp [gamma]
  rw [← he]
  by_cases hinj : Function.Injective gamma
  · let sigma := Tuple.sort (fun i => OrderDual.toDual (gamma i))
    have hs : Antitone (fun i => gamma (sigma i)) :=
      Tuple.monotone_sort (fun i => OrderDual.toDual (gamma i))
    have hstrict : StrictAnti (fun i => gamma (sigma i)) :=
      hs.strictAnti_of_injective (hinj.comp sigma.injective)
    have hdom := hc _ hstrict
    have hpc := alternating_coefficient_perm p hp gamma sigma.symm
    have hqc := alternating_coefficient_perm q hq gamma sigma.symm
    simp only [Equiv.symm_symm] at hpc hqc
    rw [hpc, hqc, hdom]
  · obtain ⟨i, j, heq, hne⟩ := Function.not_injective_iff.mp hinj
    rw [alternating_coefficient_eq_zero_of_eq p hp gamma i j hne heq,
      alternating_coefficient_eq_zero_of_eq q hq gamma i j hne heq]

theorem dominant_permutation_eq_iff {m : ℕ} (gamma eta : Fin m → ℕ)
    (hg : StrictAnti gamma) (he : StrictAnti eta) (sigma : Equiv.Perm (Fin m)) :
    powerExponent (fun i => gamma (sigma.symm i)) = powerExponent eta ↔
      gamma = eta ∧ sigma = 1 := by
  constructor
  · intro h
    have hf := powerExponent_injective h
    have hp : Antitone (gamma ∘ sigma.symm) := by
      change Antitone (fun i => gamma (sigma.symm i))
      rw [hf]
      exact he.antitone
    have h1 : Antitone (gamma ∘ (1 : Equiv.Perm (Fin m))) := by
      simpa using hg.antitone
    have hu := Tuple.unique_antitone hp h1
    have hge : gamma = eta := by
      calc
        gamma = (fun i => gamma (sigma.symm i)) := hu.symm
        _ = eta := hf
    refine ⟨hge, ?_⟩
    apply Equiv.ext
    intro i
    apply hg.injective
    have hi := congrFun hf (sigma i)
    simpa only [Equiv.symm_apply_apply, ← hge, Equiv.Perm.one_apply] using hi.symm
  · rintro ⟨rfl, rfl⟩
    rfl

/-- Distinct decreasing exponent vectors have disjoint dominant coefficients. -/
theorem alternant_dominant_coefficient {m : ℕ} (gamma eta : Fin m → ℕ)
    (hg : StrictAnti gamma) (he : StrictAnti eta) :
    (alternant gamma).coeff (powerExponent eta) = if gamma = eta then 1 else 0 := by
  classical
  have ht (sigma : Equiv.Perm (Fin m)) :
      (signCoeff sigma * MvPolynomial.rename sigma (powerMonomial gamma)).coeff
        (powerExponent eta) = if gamma = eta ∧ sigma = 1 then 1 else 0 := by
    rw [signCoeff_eq_C, MvPolynomial.coeff_C_mul, rename_powerMonomial,
      powerMonomial_eq_monomial, MvPolynomial.coeff_monomial]
    simp only [dominant_permutation_eq_iff gamma eta hg he]
    split_ifs with h
    · rcases h with ⟨_, rfl⟩
      simp
    · simp
  rw [alternant, antisymmetrize, MvPolynomial.coeff_sum]
  simp only [ht]
  by_cases h : gamma = eta <;> simp [h]

theorem alternating_C_mul {m : ℕ} (p : Poly m) (c : Coeff)
    (hp : IsAlternating p) : IsAlternating (MvPolynomial.C c * p) := by
  intro sigma
  rw [map_mul, MvPolynomial.rename_C, hp sigma]
  ring

theorem alternating_sum {m : ℕ} {α : Type*} (s : Finset α) (f : α → Poly m)
    (h : ∀ a ∈ s, IsAlternating (f a)) : IsAlternating (∑ a ∈ s, f a) := by
  intro sigma
  simp only [map_sum, Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro a ha
  exact h a ha sigma

theorem alternating_mul_symmetric {m : ℕ} (p q : Poly m)
    (hp : IsAlternating p) (hq : MvPolynomial.IsSymmetric q) :
    IsAlternating (p * q) := by
  intro sigma
  rw [map_mul, hp sigma, hq sigma, mul_assoc]

theorem vandermonde_mul_isAlternating {m : ℕ} (p : Poly m)
    (hp : MvPolynomial.IsSymmetric p) : IsAlternating (vandermonde m * p) :=
  alternating_mul_symmetric _ p (alternant_isAlternating (delta m)) hp

/-- This is a subset of the actual polynomial's finite monomial support. -/
def dominantSupport {m : ℕ} (p : Poly m) : Finset (Fin m →₀ ℕ) := by
  classical
  exact p.support.filter (fun e => StrictAnti (fun i => e i))

def dominantReconstruction {m : ℕ} (p : Poly m) : Poly m :=
  ∑ e ∈ dominantSupport p, MvPolynomial.C (p.coeff e) * alternant (fun i => e i)

theorem dominantReconstruction_isAlternating {m : ℕ} (p : Poly m) :
    IsAlternating (dominantReconstruction p) := by
  apply alternating_sum
  intro e _
  exact alternating_C_mul _ _ (alternant_isAlternating _)

theorem dominantReconstruction_coefficient {m : ℕ} (p : Poly m) (eta : Fin m → ℕ)
    (he : StrictAnti eta) :
    (dominantReconstruction p).coeff (powerExponent eta) =
      p.coeff (powerExponent eta) := by
  classical
  rw [dominantReconstruction, MvPolynomial.coeff_sum]
  calc
    (∑ e ∈ dominantSupport p,
        (MvPolynomial.C (p.coeff e) * alternant (fun i => e i)).coeff (powerExponent eta)) =
        ∑ e ∈ dominantSupport p, if e = powerExponent eta then p.coeff e else 0 := by
      apply Finset.sum_congr rfl
      intro e hem
      have hanti : StrictAnti (fun i => e i) := (Finset.mem_filter.mp hem).2
      rw [MvPolynomial.coeff_C_mul, alternant_dominant_coefficient _ _ hanti he]
      have heq : (fun i => e i) = eta ↔ e = powerExponent eta := by
        constructor
        · intro h
          ext i
          simpa only [powerExponent_apply] using congrFun h i
        · rintro rfl
          simp
      simp only [heq]
      split_ifs <;> simp
    _ = p.coeff (powerExponent eta) := by
      by_cases hm : powerExponent eta ∈ p.support
      · have hd : powerExponent eta ∈ dominantSupport p := by
          apply Finset.mem_filter.mpr
          refine ⟨hm, ?_⟩
          simpa only [powerExponent_apply] using he
        simp [hd]
      · have hd : powerExponent eta ∉ dominantSupport p := by
          intro hd
          exact hm (Finset.mem_filter.mp hd).1
        have hz : p.coeff (powerExponent eta) = 0 := MvPolynomial.notMem_support_iff.mp hm
        simp [hd, hz]

/-- Explicit reconstruction with no assumed finite support or desired expansion:
the support is taken from the actual input polynomial itself. -/
theorem alternating_reconstruction {m : ℕ} (p : Poly m) (hp : IsAlternating p) :
    p = ∑ e ∈ dominantSupport p,
      MvPolynomial.C (p.coeff e) * alternant (fun i => e i) := by
  apply alternating_eq_of_dominant_coeff p (dominantReconstruction p) hp
    (dominantReconstruction_isAlternating p)
  intro eta he
  exact (dominantReconstruction_coefficient p eta he).symm

end PartitionH3

#check @PartitionH3.alternating_eq_of_dominant_coeff
#check @PartitionH3.alternating_reconstruction
#print axioms PartitionH3.rename_antisymmetrize
#print axioms PartitionH3.alternant_isAlternating
#print axioms PartitionH3.alternating_coefficient_eq_zero_of_eq
#print axioms PartitionH3.alternating_eq_of_dominant_coeff
#print axioms PartitionH3.dominant_permutation_eq_iff
#print axioms PartitionH3.alternant_dominant_coefficient
#print axioms PartitionH3.vandermonde_mul_isAlternating
#print axioms PartitionH3.dominantReconstruction_isAlternating
#print axioms PartitionH3.dominantReconstruction_coefficient
#print axioms PartitionH3.alternating_reconstruction
