import Mathlib.Algebra.Polynomial.Roots

/-!
# Uniqueness of Hermite (confluent) interpolation

openai/math result 378 recovers `H(0) = #F` from the first `J` Taylor coefficients of
`H(t + z)` at the nodes `t = 1, ..., Q`, using `QJ > deg H` (Section 2.5 and Section 3.3).
The data determine `H` because two polynomials with the same jets differ by a multiple of
`(T - t)^J` at every node, hence by a multiple of `∏_t (T - t)^J`, whose degree `QJ`
exceeds the degree bound. This file proves that uniqueness statement over any field.
-/

namespace EthConsequences.Hermite

open Polynomial Finset
open scoped Function

variable {K : Type*} [Field K]

/-- A polynomial of degree `< |s| * J` divisible by `(X - t)^J` for every node `t ∈ s`
is zero. -/
theorem eq_zero_of_jets_vanish (s : Finset K) (J : ℕ) (p : K[X])
    (hdeg : p.natDegree < s.card * J) (hdvd : ∀ t ∈ s, (X - C t) ^ J ∣ p) : p = 0 := by
  by_contra hp
  have hcop : (s : Set K).Pairwise (IsCoprime on fun t : K => (X - C t) ^ J) := by
    intro a _ b _ hab
    exact (pairwise_coprime_X_sub_C (s := id) Function.injective_id hab).pow
  have hprod : (∏ t ∈ s, (X - C t) ^ J) ∣ p := Finset.prod_dvd_of_coprime hcop hdvd
  have hne : ∀ t ∈ s, (X - C t) ^ J ≠ 0 := fun t _ => pow_ne_zero _ (X_sub_C_ne_zero t)
  have hdegprod : (∏ t ∈ s, (X - C t) ^ J).natDegree = s.card * J := by
    rw [natDegree_prod _ _ hne]
    simp [natDegree_pow]
  have := natDegree_le_of_dvd hprod hp
  omega

/-- Hermite uniqueness: two polynomials of degree `< |s| * J` whose differences vanish to
order `J` at every node coincide. In particular the Taylor data `[z^j] H(t + z)`, `j < J`,
`t ∈ s`, determine `H` and hence `H(0)`. -/
theorem eq_of_jets_eq (s : Finset K) (J : ℕ) (p q : K[X])
    (hp : p.natDegree < s.card * J) (hq : q.natDegree < s.card * J)
    (hdvd : ∀ t ∈ s, (X - C t) ^ J ∣ p - q) : p = q := by
  have hdeg : (p - q).natDegree < s.card * J :=
    lt_of_le_of_lt (natDegree_sub_le p q) (max_lt hp hq)
  exact sub_eq_zero.1 (eq_zero_of_jets_vanish s J (p - q) hdeg hdvd)

end EthConsequences.Hermite
