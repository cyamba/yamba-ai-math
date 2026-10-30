/-
Problems ETH-B01 / ETH-B03 (problems/eth/B-exponent-frontier/).

Routing rigidity: the core of the sqrt(log n) barrier for the replacement-form template of
OpenAI's ETH refutation (Sec. 2.6, Steps 2-3). Auxiliary coordinates are pairs `u = (a_u, d_u)`
of strings in `α^Q`; a matrix `M` is *routing-supported with defect R* if `M u w ≠ 0` implies that
`d_u` and `a_w` differ in fewer than `R` positions. The template needs `rank (1 - M)` small
(it is the number of measurements) and needs this support condition (it bounds the degree of the
replacement forms by `R - 1`).

Main result (`rank_one_sub_ge_card_block`): for every routing-supported `M` (commutative or not)
and every symbol predicate `X`, the set `T` of indices whose `a`-string has at least `k₁` symbols in
`X` and whose `d`-string has at least `k₂` symbols outside `X`, with `k₁ + k₂ ≥ Q + R`, satisfies
`#T ≤ rank (1 - M)`. With `|X| = r/2` and `k₁ = k₂ = ⌈(Q+R)/2⌉` this gives
`rank (1 - M) ≥ r^{2Q} Pr[Bin(Q,1/2) ≥ ⌈(Q+R)/2⌉]^2 = D exp(-(1+o(1)) R^2 / Q)`.
-/
import Mathlib.LinearAlgebra.Matrix.Rank

open Finset

namespace EthProblems.RoutingRigidity

/-- If `a` has at least `k₁` symbols in `X` and `d` has at least `k₂` symbols outside `X`, with
`k₁ + k₂ ≥ Q + R`, then `a` and `d` differ in at least `R` positions. -/
theorem hamming_ge_of_split {Q : ℕ} {α : Type*} [DecidableEq α] (X : α → Prop) [DecidablePred X]
    (a d : Fin Q → α) (k₁ k₂ R : ℕ) (hk : Q + R ≤ k₁ + k₂)
    (ha : k₁ ≤ #(univ.filter fun s => X (a s)))
    (hd : k₂ ≤ #(univ.filter fun s => ¬ X (d s))) :
    R ≤ #(univ.filter fun s => a s ≠ d s) := by
  classical
  set A := univ.filter fun s => X (a s)
  set B := univ.filter fun s => ¬ X (d s)
  have hsub : A ∩ B ⊆ univ.filter fun s => a s ≠ d s := by
    intro s hs
    simp only [A, B, mem_inter, mem_filter, mem_univ, true_and] at hs
    simp only [mem_filter, mem_univ, true_and]
    intro h
    exact hs.2 (h ▸ hs.1)
  have hunion : #(A ∪ B) ≤ Q := by
    simpa using card_le_univ (A ∪ B)
  have hiu := card_union_add_card_inter A B
  have := card_le_card hsub
  omega

/-- A zero principal block forces rank: if `M` vanishes on `T × T` then `#T ≤ rank (1 - M)`. -/
theorem card_le_rank_of_zero_block {ι K : Type*} [Fintype ι] [DecidableEq ι] [Field K]
    (M : Matrix ι ι K) (T : Finset ι) (hT : ∀ u ∈ T, ∀ w ∈ T, M u w = 0) :
    #T ≤ (1 - M).rank := by
  have h : (1 - M).submatrix (fun x : T => (x : ι)) (fun x : T => (x : ι)) = 1 := by
    ext ⟨u, hu⟩ ⟨w, hw⟩
    simp only [Matrix.submatrix_apply, Matrix.sub_apply, Matrix.one_apply, hT u hu w hw,
      sub_zero, Subtype.mk.injEq]
  have hle := Matrix.rank_submatrix_le (1 - M) (fun x : T => (x : ι)) (fun x : T => (x : ι))
  rw [h, Matrix.rank_one, Fintype.card_coe] at hle
  exact hle

/-- **Routing rigidity.** Every routing-supported matrix with defect `R` (commutative or not) has
`rank (1 - M) ≥ #T` for the split block `T`. -/
theorem rank_one_sub_ge_card_block {Q : ℕ} {α K : Type*} [Fintype α] [DecidableEq α] [Field K]
    (R : ℕ) (M : Matrix ((Fin Q → α) × (Fin Q → α)) ((Fin Q → α) × (Fin Q → α)) K)
    (hM : ∀ u w, M u w ≠ 0 → #(univ.filter fun s => u.2 s ≠ w.1 s) < R)
    (X : α → Prop) [DecidablePred X] (k₁ k₂ : ℕ) (hk : Q + R ≤ k₁ + k₂) :
    #(univ.filter fun u : (Fin Q → α) × (Fin Q → α) =>
        k₁ ≤ #(univ.filter fun s => X (u.1 s)) ∧ k₂ ≤ #(univ.filter fun s => ¬ X (u.2 s)))
      ≤ (1 - M).rank := by
  apply card_le_rank_of_zero_block
  intro u hu w hw
  simp only [mem_filter, mem_univ, true_and] at hu hw
  by_contra hne
  have hlt := hM u w hne
  -- `a_w = w.1` has ≥ k₁ symbols in X, `d_u = u.2` has ≥ k₂ symbols outside X.
  have hge := hamming_ge_of_split X w.1 u.2 k₁ k₂ R hk hw.1 hu.2
  have hsymm : (univ.filter fun s => w.1 s ≠ u.2 s) = (univ.filter fun s => u.2 s ≠ w.1 s) := by
    ext s
    simp [ne_comm]
  rw [hsymm] at hge
  omega

end EthProblems.RoutingRigidity
