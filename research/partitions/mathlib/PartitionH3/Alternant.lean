import PartitionH3.Foundations
import Mathlib.GroupTheory.Perm.Sign

/-!
Finite signed monomial alternants over the actual polynomial ring `Poly m`.
The generic elementary-product identity has no coloring-expansion hypothesis.
-/

open scoped BigOperators

noncomputable section

namespace PartitionH3

def powerMonomial {m : ℕ} (gamma : Fin m → ℕ) : Poly m :=
  ∏ i, MvPolynomial.X i ^ gamma i

def indicator {m : ℕ} (T : Finset (Fin m)) (i : Fin m) : ℕ :=
  if i ∈ T then 1 else 0

def bump {m : ℕ} (gamma : Fin m → ℕ) (T : Finset (Fin m)) : Fin m → ℕ :=
  fun i => gamma i + indicator T i

def signCoeff {m : ℕ} (sigma : Equiv.Perm (Fin m)) : Poly m :=
  ((Equiv.Perm.sign sigma : ℤ) : Poly m)

def antisymmetrize {m : ℕ} (p : Poly m) : Poly m :=
  ∑ sigma : Equiv.Perm (Fin m), signCoeff sigma * MvPolynomial.rename sigma p

/-- The actual signed permutation sum of variable monomials. -/
def alternant {m : ℕ} (gamma : Fin m → ℕ) : Poly m :=
  antisymmetrize (powerMonomial gamma)

def delta (m : ℕ) (i : Fin m) : ℕ := m - 1 - i.val

def vandermonde (m : ℕ) : Poly m := alternant (delta m)

theorem delta_cast (m : ℕ) (i : Fin m) :
    (delta m i : ℤ) = (m : ℤ) - 1 - (i.val : ℤ) := by
  have hi := i.isLt
  unfold delta
  omega

theorem alternant_eq_sum {m : ℕ} (gamma : Fin m → ℕ) :
    alternant gamma = ∑ sigma : Equiv.Perm (Fin m),
      signCoeff sigma * ∏ i, MvPolynomial.X (sigma i) ^ gamma i := by
  simp only [alternant, antisymmetrize, powerMonomial, map_prod, map_pow,
    MvPolynomial.rename_X]

theorem powerMonomial_mul_subset {m : ℕ} (gamma : Fin m → ℕ)
    (T : Finset (Fin m)) :
    powerMonomial gamma * (∏ i ∈ T, (MvPolynomial.X i : Poly m)) =
      powerMonomial (bump gamma T) := by
  classical
  unfold powerMonomial bump indicator
  rw [← Finset.prod_ite_mem_eq T (fun i => (MvPolynomial.X i : Poly m)),
    ← Finset.prod_mul_distrib]
  apply Finset.prod_congr rfl
  intro i _
  by_cases hi : i ∈ T <;> simp [hi, pow_succ]

/-- Multiplication by the subset-defined elementary polynomial is an actual
finite polynomial sum, valid also when `b > m`. -/
theorem powerMonomial_mul_elementary {m : ℕ} (gamma : Fin m → ℕ) (b : ℕ) :
    powerMonomial gamma * elementary m b =
      ∑ T ∈ (Finset.univ : Finset (Fin m)).powersetCard b,
        powerMonomial (bump gamma T) := by
  classical
  simp only [elementary, MvPolynomial.esymm, Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro T _
  exact powerMonomial_mul_subset gamma T

theorem antisymmetrize_sum {m : ℕ} {α : Type*} (s : Finset α) (f : α → Poly m) :
    antisymmetrize (∑ t ∈ s, f t) = ∑ t ∈ s, antisymmetrize (f t) := by
  classical
  simp only [antisymmetrize, map_sum, Finset.mul_sum]
  exact Finset.sum_comm

theorem antisymmetrize_mul_symmetric {m : ℕ} (p q : Poly m)
    (hq : MvPolynomial.IsSymmetric q) :
    antisymmetrize (p * q) = antisymmetrize p * q := by
  classical
  simp only [antisymmetrize, Finset.sum_mul]
  apply Finset.sum_congr rfl
  intro sigma _
  rw [map_mul, hq sigma, mul_assoc]

/-- Generic finite alternant--elementary identity over `ℤ[q]`.
No bound on `b`, desired expansion, sign witness or positivity is assumed. -/
theorem alternant_mul_elementary {m : ℕ} (gamma : Fin m → ℕ) (b : ℕ) :
    alternant gamma * elementary m b =
      ∑ T ∈ (Finset.univ : Finset (Fin m)).powersetCard b,
        alternant (bump gamma T) := by
  classical
  change antisymmetrize (powerMonomial gamma) * elementary m b = _
  rw [← antisymmetrize_mul_symmetric _ _ (elementary_isSymmetric m b),
    powerMonomial_mul_elementary, antisymmetrize_sum]
  rfl

theorem signCoeff_mul {m : ℕ} (sigma tau : Equiv.Perm (Fin m)) :
    signCoeff (sigma * tau) = signCoeff sigma * signCoeff tau := by
  simp [signCoeff, Equiv.Perm.sign_mul]

theorem signCoeff_swap {m : ℕ} (p q : Fin m) (hpq : p ≠ q) :
    signCoeff (Equiv.swap p q) = (-1 : Poly m) := by
  simp [signCoeff, Equiv.Perm.sign_swap hpq]

theorem rename_perm_mul {m : ℕ} (sigma tau : Equiv.Perm (Fin m)) (p : Poly m) :
    MvPolynomial.rename sigma (MvPolynomial.rename tau p) =
      MvPolynomial.rename (sigma * tau) p := by
  rw [MvPolynomial.rename_rename]
  rfl

theorem antisymmetrize_rename_swap {m : ℕ} (p : Poly m) (i j : Fin m)
    (hij : i ≠ j) :
    antisymmetrize (MvPolynomial.rename (Equiv.swap i j) p) = -antisymmetrize p := by
  classical
  simp only [antisymmetrize, ← Finset.sum_neg_distrib]
  apply Fintype.sum_equiv (Equiv.mulRight (Equiv.swap i j))
  intro sigma
  simp only [Equiv.coe_mulRight, rename_perm_mul, signCoeff_mul,
    signCoeff_swap i j hij]
  exact ((congrArg (fun z : Poly m =>
    -(z * MvPolynomial.rename (sigma * Equiv.swap i j) p))
    (mul_neg_one (signCoeff sigma))).trans
      ((congrArg Neg.neg (neg_mul _ _)).trans (neg_neg _))).symm

theorem powerMonomial_swap_invariant {m : ℕ} (gamma : Fin m → ℕ) (p q : Fin m)
    (he : gamma p = gamma q) :
    MvPolynomial.rename (Equiv.swap p q) (powerMonomial gamma) = powerMonomial gamma := by
  classical
  have hg : ∀ i, gamma (Equiv.swap p q i) = gamma i := by
    intro i
    by_cases hip : i = p
    · subst i
      simpa using he.symm
    · by_cases hiq : i = q
      · subst i
        simpa using he
      · simp [Equiv.swap_apply_def, hip, hiq]
  calc
    MvPolynomial.rename (Equiv.swap p q) (powerMonomial gamma) =
        ∏ i, (MvPolynomial.X (Equiv.swap p q i) : Poly m) ^ gamma i := by
          simp only [powerMonomial, map_prod, map_pow, MvPolynomial.rename_X]
    _ = ∏ i, (MvPolynomial.X (Equiv.swap p q i) : Poly m) ^ gamma (Equiv.swap p q i) := by
          apply Finset.prod_congr rfl
          intro i _
          rw [hg]
    _ = powerMonomial gamma := Equiv.prod_comp (Equiv.swap p q)
        (fun i => (MvPolynomial.X i : Poly m) ^ gamma i)

/-- Actual repeated-exponent vanishing in the torsion-free ring `Poly m`. -/
theorem alternant_eq_zero_of_eq {m : ℕ} (gamma : Fin m → ℕ) (p q : Fin m)
    (hpq : p ≠ q) (he : gamma p = gamma q) : alternant gamma = 0 := by
  have h := antisymmetrize_rename_swap (powerMonomial gamma) p q hpq
  rw [powerMonomial_swap_invariant gamma p q he] at h
  change alternant gamma = -alternant gamma at h
  have htwo : (2 : Poly m) * alternant gamma = 0 := by
    calc
      (2 : Poly m) * alternant gamma = alternant gamma + alternant gamma := two_mul _
      _ = -alternant gamma + alternant gamma := congrArg (fun x => x + alternant gamma) h
      _ = 0 := neg_add_cancel _
  apply (mul_eq_zero.mp htwo).resolve_left
  intro hz
  have hc := congrArg (fun f : Poly m => (f.coeff 0).coeff 0) hz
  norm_num at hc

end PartitionH3

#check @PartitionH3.alternant_mul_elementary
#check @PartitionH3.alternant_eq_zero_of_eq
#print axioms PartitionH3.alternant_eq_sum
#print axioms PartitionH3.powerMonomial_mul_elementary
#print axioms PartitionH3.alternant_mul_elementary
#print axioms PartitionH3.alternant_eq_zero_of_eq
