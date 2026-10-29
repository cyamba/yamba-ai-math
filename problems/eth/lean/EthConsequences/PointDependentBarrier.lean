import Mathlib.LinearAlgebra.Matrix.Rank
import Mathlib.LinearAlgebra.FiniteDimensional.Lemmas
import Mathlib.Data.Fintype.BigOperators
import EthConsequences.RankBarrier
import EthConsequences.SubcubeObstruction

/-!
# A rank barrier for point-dependent designs (subresult SR-03)

In openai/math result 378 the replacement forms come from auxiliary rows `P_u(T)`, `u` a label,
with `P_u(0) = δ_u` and `deg P_u < R`. At an evaluation node the design splits each row into a
*local* part (labels allowed by the group rule at that node) and a part determined by the
node's measurements, whose number is at least the rank of that part. The preprint's
construction uses one measurement matrix for every node and rows of a fixed template (its
(2.16) and (4.10)); its Definitions 2.1 and 3.1 allow different matrices at each node.
Subresult SR-01 (`RankBarrier.lean`) bounds the template case. Here we prove a bound that
holds for **arbitrary point-dependent designs**, in or out of the swap algebra:

* `card_le_sum_rank`: if `1 = ∑ᵢ λᵢ (Lᵢ + Nᵢ)` and every `Lᵢ` vanishes on `U × U`, then
  `|U| ≤ ∑ᵢ rank Nᵢ`.
* `point_dependent_barrier`: Lagrange extrapolation to `0` from `R` distinct nodes supplies such
  an identity for any matrix of polynomials of degree `< R` that equals `1` at `0`.
* `label_barrier`: on labels `u = (a_u, d_u) ∈ [r]^Q × [r]^Q` with the group rule
  "`w` is local for `u` at node `i` iff `a_w (pos i) = d_u (pos i)`", any product sets
  `A = ∏ SA`, `B = ∏ SB` that are disjoint at the `R` used positions force
  `|A| |B| ≤ ∑ᵢ rank Nᵢ`.
* `label_barrier_explicit`: with a fixed symbol class `H ⊆ [r]` at `R` distinct positions,
  `|H|^R (r - |H|)^R r^(2(Q-R)) ≤ ∑ᵢ rank Nᵢ`; dividing by `D = r^(2Q)`, the measurements at
  some node are at least a `(|H|(r-|H|)/r²)^R / R ≥ 4^(-R)/R`-fraction of `D` when `r` is even.

The template barrier of SR-01 is Gaussian in `R`; this one is exponential. It is the best
bound this forced-identity argument can give (product sets are optimal for it), not a claim
about all arguments (see SR-03, SR-04).
-/

namespace EthConsequences.PointBarrier

open Matrix Finset Polynomial

variable {K : Type*} [Field K]

section Rank

variable {m n : Type*} [Fintype n]

/-- Subadditivity of matrix rank. -/
theorem rank_add_le (A B : Matrix m n K) : (A + B).rank ≤ A.rank + B.rank := by
  unfold Matrix.rank
  rw [Matrix.mulVecLin_add]
  calc Module.finrank K (LinearMap.range (A.mulVecLin + B.mulVecLin))
      ≤ Module.finrank K
          (LinearMap.range A.mulVecLin ⊔ LinearMap.range B.mulVecLin : Submodule K (m → K)) :=
        Submodule.finrank_mono (LinearMap.range_add_le _ _)
    _ ≤ _ := Submodule.finrank_add_le_finrank_add_finrank _ _

/-- Scaling does not increase rank. -/
theorem rank_smul_le (c : K) (A : Matrix m n K) : (c • A).rank ≤ A.rank := by
  unfold Matrix.rank
  have h : (c • A).mulVecLin = c • A.mulVecLin := by
    ext v i
    simp
  rw [h]
  exact Submodule.finrank_mono (LinearMap.range_smul_le_range _ _)

/-- Rank of a finite sum is at most the sum of the ranks. -/
theorem rank_sum_le {η : Type*} (s : Finset η) (A : η → Matrix m n K) :
    (∑ i ∈ s, A i).rank ≤ ∑ i ∈ s, (A i).rank := by
  classical
  induction s using Finset.induction_on with
  | empty => simp [Matrix.rank_zero]
  | insert a s ha ih =>
    rw [Finset.sum_insert ha, Finset.sum_insert ha]
    exact (rank_add_le _ _).trans (Nat.add_le_add_left ih _)

end Rank

/-- **Abstract barrier.** If `1 = ∑ᵢ λᵢ • (Lᵢ + Nᵢ)` and every local part `Lᵢ` vanishes on
`U × U`, then `|U| ≤ ∑ᵢ rank Nᵢ`. -/
theorem card_le_sum_rank {ι : Type*} [Fintype ι] [DecidableEq ι] {R : ℕ}
    (lam : Fin R → K) (L N : Fin R → Matrix ι ι K)
    (hsum : ∑ i, lam i • (L i + N i) = 1)
    (U : Finset ι) (hloc : ∀ i, ∀ u ∈ U, ∀ w ∈ U, L i u w = 0) :
    U.card ≤ ∑ i, (N i).rank := by
  have hN : ∑ i, lam i • N i = 1 - ∑ i, lam i • L i := by
    rw [eq_sub_iff_add_eq, ← hsum, ← Finset.sum_add_distrib]
    refine Finset.sum_congr rfl fun i _ => ?_
    rw [smul_add, add_comm]
  have hU : ∀ u ∈ U, ∀ w ∈ U, (∑ i, lam i • N i) u w = if u = w then 1 else 0 := by
    intro u hu w hw
    rw [hN, Matrix.sub_apply, Matrix.one_apply, Matrix.sum_apply]
    have : ∑ i, (lam i • L i) u w = 0 := by
      refine Finset.sum_eq_zero fun i _ => ?_
      rw [Matrix.smul_apply, hloc i u hu w hw, smul_zero]
    rw [this, sub_zero]
  calc U.card ≤ (∑ i, lam i • N i).rank :=
        RankBarrier.card_le_rank_of_principal_identity _ U hU
    _ ≤ ∑ i, (lam i • N i).rank := rank_sum_le _ _
    _ ≤ ∑ i, (N i).rank := Finset.sum_le_sum fun i _ => rank_smul_le _ _

/-- Entrywise Lagrange extrapolation to `0` for a matrix of polynomials of degree `< R`. -/
theorem map_eval_zero_eq_sum {ι : Type*} [Fintype ι] {R : ℕ}
    (P : Matrix ι ι K[X]) (hdeg : ∀ u w, (P u w).degree < R)
    (x : Fin R → K) (hx : Function.Injective x) :
    P.map (eval 0) = ∑ i, ((Lagrange.basis univ x i).eval 0) • P.map (eval (x i)) := by
  ext u w
  rw [Matrix.map_apply, Subcube.eval_zero_eq_sum x hx (P u w) (hdeg u w), Matrix.sum_apply]
  rfl

/-- **Point-dependent barrier.** Let `P` be a matrix of polynomials of degree `< R` with
`P(0) = 1`, and let `x₁, …, x_R` be distinct nodes at which `P(xᵢ) = Lᵢ + Nᵢ`. If every local
part vanishes on `U × U`, the measured parts have total rank at least `|U|`. -/
theorem point_dependent_barrier {ι : Type*} [Fintype ι] [DecidableEq ι] {R : ℕ}
    (P : Matrix ι ι K[X]) (hdeg : ∀ u w, (P u w).degree < R)
    (h0 : P.map (eval 0) = 1)
    (x : Fin R → K) (hx : Function.Injective x)
    (L N : Fin R → Matrix ι ι K)
    (hsplit : ∀ i, P.map (eval (x i)) = L i + N i)
    (U : Finset ι) (hloc : ∀ i, ∀ u ∈ U, ∀ w ∈ U, L i u w = 0) :
    U.card ≤ ∑ i, (N i).rank := by
  refine card_le_sum_rank (fun i => (Lagrange.basis univ x i).eval 0) L N ?_ U hloc
  rw [← h0, map_eval_zero_eq_sum P hdeg x hx]
  refine Finset.sum_congr rfl fun i _ => ?_
  rw [hsplit i]

/-- Auxiliary labels `u = (a_u, d_u)`: a variable schedule and a factor schedule. -/
abbrev Label (r Q : ℕ) := (Fin Q → Fin r) × (Fin Q → Fin r)

/-- **Label barrier.** At node `i` the local entries of row `u` are the labels `w` with
`a_w (pos i) = d_u (pos i)`. For product sets `∏ₜ SA t` and `∏ₜ SB t` whose factors are
disjoint at every used position, `(∏ₜ |SA t|) (∏ₜ |SB t|) ≤ ∑ᵢ rank Nᵢ`. -/
theorem label_barrier {r Q R : ℕ}
    (P : Matrix (Label r Q) (Label r Q) K[X]) (hdeg : ∀ u w, (P u w).degree < R)
    (h0 : P.map (eval 0) = 1)
    (x : Fin R → K) (hx : Function.Injective x) (pos : Fin R → Fin Q)
    (L N : Fin R → Matrix (Label r Q) (Label r Q) K)
    (hsplit : ∀ i, P.map (eval (x i)) = L i + N i)
    (hlocal : ∀ i u w, L i u w ≠ 0 → w.1 (pos i) = u.2 (pos i))
    (SA SB : Fin Q → Finset (Fin r)) (hdisj : ∀ i, Disjoint (SA (pos i)) (SB (pos i))) :
    (∏ t, (SA t).card) * (∏ t, (SB t).card) ≤ ∑ i, (N i).rank := by
  classical
  set U : Finset (Label r Q) := Fintype.piFinset SA ×ˢ Fintype.piFinset SB with hU
  have hcard : U.card = (∏ t, (SA t).card) * (∏ t, (SB t).card) := by
    rw [hU, Finset.card_product, Fintype.card_piFinset, Fintype.card_piFinset]
  rw [← hcard]
  refine point_dependent_barrier P hdeg h0 x hx L N hsplit U ?_
  intro i u hu w hw
  by_contra hne
  have heq := hlocal i u w hne
  rw [hU, Finset.mem_product, Fintype.mem_piFinset, Fintype.mem_piFinset] at hu hw
  have ha : w.1 (pos i) ∈ SA (pos i) := hw.1 (pos i)
  have hb : u.2 (pos i) ∈ SB (pos i) := hu.2 (pos i)
  rw [heq] at ha
  exact Finset.disjoint_left.1 (hdisj i) ha hb

/-- **Explicit form.** With one symbol class `H ⊆ [r]` at `R` distinct positions,
`|H|^R (r - |H|)^R r^(2(Q - R)) ≤ ∑ᵢ rank Nᵢ`. -/
theorem label_barrier_explicit {r Q R : ℕ}
    (P : Matrix (Label r Q) (Label r Q) K[X]) (hdeg : ∀ u w, (P u w).degree < R)
    (h0 : P.map (eval 0) = 1)
    (x : Fin R → K) (hx : Function.Injective x) (pos : Fin R → Fin Q)
    (hpos : Function.Injective pos)
    (L N : Fin R → Matrix (Label r Q) (Label r Q) K)
    (hsplit : ∀ i, P.map (eval (x i)) = L i + N i)
    (hlocal : ∀ i u w, L i u w ≠ 0 → w.1 (pos i) = u.2 (pos i))
    (H : Finset (Fin r)) :
    H.card ^ R * (r - H.card) ^ R * r ^ (2 * (Q - R)) ≤ ∑ i, (N i).rank := by
  classical
  set S : Finset (Fin Q) := univ.image pos with hS
  have hScard : S.card = R := by
    rw [hS, Finset.card_image_of_injective _ hpos, Finset.card_univ, Fintype.card_fin]
  have hc1 : (univ.filter (fun t => t ∈ S)).card = R := by
    rw [Finset.filter_mem_eq_inter, Finset.univ_inter, hScard]
  have hc2 : (univ.filter (fun t => t ∉ S)).card = Q - R := by
    have h := Finset.card_filter_add_card_filter_not
      (s := (univ : Finset (Fin Q))) (fun t => t ∈ S)
    rw [hc1, Finset.card_univ, Fintype.card_fin] at h
    omega
  set SA : Fin Q → Finset (Fin r) := fun t => if t ∈ S then H else univ with hSA
  set SB : Fin Q → Finset (Fin r) := fun t => if t ∈ S then Hᶜ else univ with hSB
  have hdisj : ∀ i, Disjoint (SA (pos i)) (SB (pos i)) := by
    intro i
    have hi : pos i ∈ S := by rw [hS]; exact Finset.mem_image_of_mem _ (Finset.mem_univ i)
    simp only [hSA, hSB, hi, ↓reduceIte]
    exact disjoint_compl_right
  have key := label_barrier P hdeg h0 x hx pos L N hsplit hlocal SA SB hdisj
  have hprodA : ∏ t, (SA t).card = H.card ^ R * r ^ (Q - R) := by
    have h : ∀ t, (SA t).card = if t ∈ S then H.card else r := by
      intro t
      by_cases ht : t ∈ S
      · simp only [hSA, ht, ↓reduceIte]
      · simp only [hSA, ht, ↓reduceIte, Finset.card_univ, Fintype.card_fin]
    rw [Finset.prod_congr rfl (fun t _ => h t), Finset.prod_ite, Finset.prod_const,
      Finset.prod_const, hc1, hc2]
  have hprodB : ∏ t, (SB t).card = (r - H.card) ^ R * r ^ (Q - R) := by
    have h : ∀ t, (SB t).card = if t ∈ S then r - H.card else r := by
      intro t
      by_cases ht : t ∈ S
      · simp only [hSB, ht, ↓reduceIte, Finset.card_compl, Fintype.card_fin]
      · simp only [hSB, ht, ↓reduceIte, Finset.card_univ, Fintype.card_fin]
    rw [Finset.prod_congr rfl (fun t _ => h t), Finset.prod_ite, Finset.prod_const,
      Finset.prod_const, hc1, hc2]
  rw [hprodA, hprodB] at key
  calc H.card ^ R * (r - H.card) ^ R * r ^ (2 * (Q - R))
      = H.card ^ R * r ^ (Q - R) * ((r - H.card) ^ R * r ^ (Q - R)) := by ring
    _ ≤ ∑ i, (N i).rank := key

end EthConsequences.PointBarrier
