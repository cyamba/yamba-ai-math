import Mathlib.LinearAlgebra.Matrix.Rank
import Mathlib.InformationTheory.Hamming

/-!
# The isoperimetric rank barrier for the spectral matrix construction (subresult SR-01)

In openai/math result 378 (Section 2.7, Step 2, and Section 4.2) the replacement forms are
built from an auxiliary matrix `M₀` indexed by labels `u = (a_u, d_u) ∈ [r]^Q × [r]^Q` and a
measurement matrix `C` subject to

* (support) `M₀ u w ≠ 0 → |E_{u,w}| ≤ R - 1`, where `E_{u,w} = {t | a_w t ≠ d_u t}`, so
  `|E_{u,w}| = hammingDist d_u a_w`;
* (kernel) `M₀ ξ = ξ` for every `ξ ∈ ker C`.

The number of measurements `c` (rows of `C`) drives the measurement cost of the algorithm.
We prove that for **any** such pair and any sets `A, B ⊆ [r]^Q` at Hamming distance at
least `R`,

  `|A| * |B| ≤ rank (1 - M₀) ≤ c`.

With threshold sets for the count of coordinates in a fixed symbol class `H`, this gives the
binomial-tail lower bound of SR-01, showing that the paper's choice `M₀ = V₀ f(W₀)` is
optimal up to a constant factor in `R`.
-/

namespace EthConsequences.RankBarrier

open Matrix Finset

variable {K : Type*} [Field K]

/-- A matrix whose principal submatrix on `U` is the identity has rank at least `|U|`. -/
theorem card_le_rank_of_principal_identity {ι : Type*} [Fintype ι] [DecidableEq ι]
    (N : Matrix ι ι K) (U : Finset ι)
    (hU : ∀ u ∈ U, ∀ w ∈ U, N u w = if u = w then 1 else 0) :
    U.card ≤ N.rank := by
  have hsub : N.submatrix (fun u : U => (u : ι)) (fun u : U => (u : ι)) = (1 : Matrix U U K) := by
    ext u w
    rw [submatrix_apply, hU u u.2 w w.2, one_apply]
    by_cases h : u = w
    · subst h; simp
    · have h' : (u : ι) ≠ (w : ι) := fun e => h (Subtype.ext e)
      simp only [h, h', ite_false]
  have h1 := rank_submatrix_le N (fun u : U => (u : ι)) (fun u : U => (u : ι))
  rw [hsub, rank_one, Fintype.card_coe] at h1
  exact h1

/-- If `ker A ⊆ ker B` then `rank B ≤ rank A` (rank and nullity). -/
theorem rank_le_of_ker_le {m n p : Type*} [Fintype m] [Fintype n] [Fintype p] [DecidableEq n]
    (A : Matrix m n K) (B : Matrix p n K)
    (h : ∀ ξ : n → K, A *ᵥ ξ = 0 → B *ᵥ ξ = 0) : B.rank ≤ A.rank := by
  unfold Matrix.rank
  have hker : LinearMap.ker A.mulVecLin ≤ LinearMap.ker B.mulVecLin := by
    intro ξ hξ
    simp only [LinearMap.mem_ker, Matrix.mulVecLin_apply] at hξ ⊢
    exact h ξ hξ
  have hA := LinearMap.finrank_range_add_finrank_ker A.mulVecLin
  have hB := LinearMap.finrank_range_add_finrank_ker B.mulVecLin
  have hk := Submodule.finrank_mono hker
  omega

/-- Auxiliary labels `u = (a_u, d_u)`: a variable schedule and a factor schedule. -/
abbrev Label (r Q : ℕ) := (Fin Q → Fin r) × (Fin Q → Fin r)

/-- **Isoperimetric rank barrier.** For any `M₀` supported on label pairs with
`hammingDist d_u a_w < R` and any `C` whose kernel `M₀` fixes, and any `A, B` at Hamming
distance at least `R`, the number of measurements is at least `|A| * |B|`. -/
theorem barrier {r Q R : ℕ} {κ : Type*} [Fintype κ]
    (M₀ : Matrix (Label r Q) (Label r Q) K) (C : Matrix κ (Label r Q) K)
    (hsupp : ∀ u w, M₀ u w ≠ 0 → hammingDist u.2 w.1 < R)
    (hker : ∀ ξ, C *ᵥ ξ = 0 → (1 - M₀) *ᵥ ξ = 0)
    (A B : Finset (Fin Q → Fin r)) (hsep : ∀ a ∈ A, ∀ b ∈ B, R ≤ hammingDist b a) :
    A.card * B.card ≤ (1 - M₀).rank ∧ (1 - M₀).rank ≤ Fintype.card κ := by
  constructor
  · have key := card_le_rank_of_principal_identity (1 - M₀) (A ×ˢ B) ?_
    · simpa [Finset.card_product] using key
    intro u hu w hw
    rw [Finset.mem_product] at hu hw
    have h0 : M₀ u w = 0 := by
      by_contra hne
      have h1 := hsupp u w hne
      have h2 := hsep w.1 hw.1 u.2 hu.2
      omega
    simp [Matrix.sub_apply, Matrix.one_apply, h0]
  · exact (rank_le_of_ker_le C (1 - M₀) hker).trans (rank_le_card_height C)

/-- Weight separation: the number of coordinates in a symbol class `H` changes by at most the
Hamming distance. -/
theorem count_le_count_add_hammingDist {Q : ℕ} {α : Type*} [DecidableEq α] (H : Finset α)
    (a b : Fin Q → α) :
    (univ.filter (fun t => a t ∈ H)).card
      ≤ (univ.filter (fun t => b t ∈ H)).card + hammingDist a b := by
  have hsub : univ.filter (fun t => a t ∈ H)
      ⊆ univ.filter (fun t => b t ∈ H) ∪ univ.filter (fun t => a t ≠ b t) := by
    intro t ht
    simp only [mem_filter, mem_univ, true_and, mem_union] at ht ⊢
    by_cases hab : a t = b t
    · left; rw [← hab]; exact ht
    · right; exact hab
  calc (univ.filter (fun t => a t ∈ H)).card
      ≤ (univ.filter (fun t => b t ∈ H) ∪ univ.filter (fun t => a t ≠ b t)).card :=
        card_le_card hsub
    _ ≤ (univ.filter (fun t => b t ∈ H)).card + (univ.filter (fun t => a t ≠ b t)).card :=
        card_union_le _ _
    _ = (univ.filter (fun t => b t ∈ H)).card + hammingDist a b := rfl

/-- Threshold form of the barrier: with `N_H(a) = #{t | a t ∈ H}`, the number of
measurements is at least `#{a | N_H(a) ≥ k + R} * #{b | N_H(b) ≤ k}`. Dividing by
`r^(2Q)` turns this into `Pr[X ≥ k + R] * Pr[X ≤ k]` for `X ~ Bin(Q, |H|/r)`. -/
theorem barrier_threshold {r Q R : ℕ} {κ : Type*} [Fintype κ]
    (M₀ : Matrix (Label r Q) (Label r Q) K) (C : Matrix κ (Label r Q) K)
    (hsupp : ∀ u w, M₀ u w ≠ 0 → hammingDist u.2 w.1 < R)
    (hker : ∀ ξ, C *ᵥ ξ = 0 → (1 - M₀) *ᵥ ξ = 0) (H : Finset (Fin r)) (k : ℕ) :
    (univ.filter (fun a : Fin Q → Fin r => k + R ≤ (univ.filter (fun t => a t ∈ H)).card)).card *
      (univ.filter (fun b : Fin Q → Fin r => (univ.filter (fun t => b t ∈ H)).card ≤ k)).card
      ≤ Fintype.card κ := by
  have hsep : ∀ a ∈ univ.filter (fun a : Fin Q → Fin r =>
        k + R ≤ (univ.filter (fun t => a t ∈ H)).card),
      ∀ b ∈ univ.filter (fun b : Fin Q → Fin r => (univ.filter (fun t => b t ∈ H)).card ≤ k),
      R ≤ hammingDist b a := by
    intro a ha b hb
    simp only [mem_filter, mem_univ, true_and] at ha hb
    have h := count_le_count_add_hammingDist H a b
    rw [hammingDist_comm]
    omega
  obtain ⟨h1, h2⟩ := barrier M₀ C hsupp hker _ _ hsep
  exact h1.trans h2

end EthConsequences.RankBarrier
