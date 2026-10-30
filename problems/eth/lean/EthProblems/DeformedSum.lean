/-
Problems ETH-C05 / ETH-C07 (problems/eth/C-counting-extensions/).

Spectral deformation of the clause product: for 0/1-valued clause indicators,
`Π_C (1 + t (Φ_C - 1)) = (1 - t)^{#unsatisfied clauses}`. Summing over assignments,
`Z_F(t) = Σ_r h_r (1-t)^r` where `h_r` is the number of assignments violating exactly
`r` clauses, so interpolating `Z_F` recovers the full Max-SAT histogram, and
`Z_F(1) = #F`.
-/
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Tactic.Ring

open Finset

namespace EthProblems.DeformedSum

theorem prod_deform_eq_pow {ι R : Type*} [CommRing R] [DecidableEq R]
    (F : Finset ι) (φ : ι → R) (hφ : ∀ i ∈ F, φ i = 0 ∨ φ i = 1) (t : R) :
    ∏ i ∈ F, (1 + t * (φ i - 1)) = (1 - t) ^ #(F.filter (fun i => φ i = 0)) := by
  have h0 : ∏ i ∈ F.filter (fun i => φ i = 0), (1 + t * (φ i - 1)) =
      (1 - t) ^ #(F.filter (fun i => φ i = 0)) := by
    rw [prod_congr rfl (g := fun _ => 1 - t), prod_const]
    intro i hi
    rw [(mem_filter.mp hi).2]
    ring
  have h1 : ∏ i ∈ F.filter (fun i => ¬ φ i = 0), (1 + t * (φ i - 1)) = 1 := by
    apply prod_eq_one
    intro i hi
    obtain ⟨hiF, hne⟩ := mem_filter.mp hi
    rcases hφ i hiF with h | h
    · exact absurd h hne
    · rw [h]
      ring
  rw [← prod_filter_mul_prod_filter_not F (fun i => φ i = 0), h0, h1, mul_one]

/-- Summed form: the deformed partition function is the Max-SAT histogram polynomial. -/
theorem deformed_sum_eq {α ι R : Type*} [CommRing R] [DecidableEq R]
    (X : Finset α) (F : Finset ι) (Φ : α → ι → R)
    (hΦ : ∀ x ∈ X, ∀ i ∈ F, Φ x i = 0 ∨ Φ x i = 1) (t : R) :
    ∑ x ∈ X, ∏ i ∈ F, (1 + t * (Φ x i - 1)) =
      ∑ x ∈ X, (1 - t) ^ #(F.filter (fun i => Φ x i = 0)) :=
  sum_congr rfl fun x hx => prod_deform_eq_pow F (Φ x) (hΦ x hx) t

/-- At `t = 1` the deformed sum counts the assignments violating no clause. -/
theorem deformed_sum_at_one {α ι R : Type*} [CommRing R] [DecidableEq R]
    (X : Finset α) (F : Finset ι) (Φ : α → ι → R)
    (hΦ : ∀ x ∈ X, ∀ i ∈ F, Φ x i = 0 ∨ Φ x i = 1) :
    ∑ x ∈ X, ∏ i ∈ F, (1 + 1 * (Φ x i - 1)) =
      (#(X.filter (fun x => #(F.filter (fun i => Φ x i = 0)) = 0)) : R) := by
  rw [deformed_sum_eq X F Φ hΦ 1, sub_self, Finset.card_filter]
  push_cast
  apply sum_congr rfl
  intro x _
  by_cases h : #(F.filter (fun i => Φ x i = 0)) = 0 <;> simp [h]

end EthProblems.DeformedSum
