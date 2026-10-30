/-
Problem ETH-A04 (problems/eth/A-algebraic-core/ETH-A04-hermite-recovery.md).

Uniqueness step of the Taylor/Hermite recovery in OpenAI's ETH refutation (Sec. 2.4):
if the first `J` Taylor coefficients of `H` at each of `Q` distinct nodes vanish and
`deg H < Q * J`, then `H = 0`. Equivalently, Taylor data of order `J` at `Q` nodes
determine any polynomial of degree `< Q J`.
-/
import Mathlib.Algebra.Polynomial.Roots

open Polynomial

namespace EthProblems.Hermite

theorem eq_zero_of_pow_dvd_at_nodes {K : Type*} [Field K] (P : K[X]) (S : Finset K) (J : ℕ)
    (hdeg : P.natDegree < S.card * J) (hdvd : ∀ t ∈ S, (X - C t) ^ J ∣ P) : P = 0 := by
  classical
  by_contra hP
  have hle : J • S.val ≤ P.roots := by
    rw [Multiset.le_iff_count]
    intro a
    rw [Multiset.count_nsmul, count_roots]
    by_cases ha : a ∈ S
    · rw [Multiset.count_eq_one_of_mem S.nodup ha, mul_one]
      exact (le_rootMultiplicity_iff hP).mpr (hdvd a ha)
    · rw [Multiset.count_eq_zero_of_notMem ha, mul_zero]
      exact Nat.zero_le _
  have hcard := (Multiset.card_le_card hle).trans (card_roots' P)
  rw [Multiset.card_nsmul, Finset.card_val] at hcard
  rw [mul_comm] at hcard
  omega

/-- Two polynomials of degree `< Q J` with the same order-`J` Taylor data at `Q` distinct
nodes are equal (the data determine `H`, hence `H(0) = #F`). -/
theorem eq_of_taylor_data {K : Type*} [Field K] (P₁ P₂ : K[X]) (S : Finset K) (J : ℕ)
    (h₁ : P₁.natDegree < S.card * J) (h₂ : P₂.natDegree < S.card * J)
    (hdvd : ∀ t ∈ S, (X - C t) ^ J ∣ P₁ - P₂) : P₁ = P₂ := by
  have hdeg : (P₁ - P₂).natDegree < S.card * J :=
    lt_of_le_of_lt (natDegree_sub_le _ _) (max_lt h₁ h₂)
  exact sub_eq_zero.mp (eq_zero_of_pow_dvd_at_nodes _ S J hdeg hdvd)

end EthProblems.Hermite
