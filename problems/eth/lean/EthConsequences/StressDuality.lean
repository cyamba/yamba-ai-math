import Mathlib.Algebra.Polynomial.BigOperators
import Mathlib.Algebra.Polynomial.Eval.Degree
import Mathlib.Data.Fintype.Powerset

/-!
# Stresses certify infeasibility in the cube polynomial problem (subresult SR-05)

The cube polynomial problem (SR-02) asks for polynomials `p v` of degree `< R`, one for each
vertex `v` of `{0,1}^Q` (encoded by its support), with `p v (0) = 1`, such that the edge
`(v, insert t v)` is good, `p v (x t) + p (insert t v) (x t) = 0`, for as many edges as possible.

Store an edge weight `w t u` at the lower endpoint `u` (`t ∉ u`) and let
`edgeW w v t` be the weight of the edge at `v` in direction `t`, seen from `v`. Call `w` a
**stress** when at every vertex the weighted moments vanish:
`∑ₜ edgeW w v t * x t ^ k = 0` for `1 ≤ k < R`.

* `stress_total_eq_zero`: if every edge carrying nonzero weight is good, the total weight
  `∑ₜ ∑_{u ∌ t} w t u` is zero. Hence a stress with nonzero total certifies that its support
  cannot be entirely good. The `R`-subcube obstruction (`no_good_subcube`) is the stress with
  the Lagrange coefficients of the subcube's directions as weights; the general statement is
  also sufficient for infeasibility by linear-algebra duality (SR-05, informal), and SR-11
  shows that combinations of subcube stresses already suffice.
* `product_edge_good`, `natDegree_product_le`, `product_eval_zero`: the product of two families
  on disjoint sets of directions is a family whose bad edges are contained in those of its
  factors (an edge may become good where the other factor vanishes at the node),
  with degree bound `(R₁ - 1) + (R₂ - 1)`.
-/

namespace EthConsequences.Stress

open Finset Polynomial

variable {K : Type*} [Field K] {Q : ℕ}

/-- The weight of the edge at `v` in direction `t`, stored at the lower endpoint. -/
def edgeW (w : Fin Q → Finset (Fin Q) → K) (v : Finset (Fin Q)) (t : Fin Q) : K :=
  if t ∈ v then w t (v.erase t) else w t v

/-- Vanishing moments collapse a weighted sum of values to a multiple of the value at `0`. -/
theorem moment_collapse {R : ℕ} (x : Fin Q → K) (a : Fin Q → K)
    (hmom : ∀ k, 1 ≤ k → k < R → ∑ t, a t * x t ^ k = 0) (p : K[X]) (hp : p.natDegree < R) :
    ∑ t, a t * p.eval (x t) = (∑ t, a t) * p.eval 0 := by
  have hR : 0 < R := lt_of_le_of_lt (Nat.zero_le _) hp
  have h : ∀ y, p.eval y = ∑ k ∈ range R, p.coeff k * y ^ k := fun y => eval_eq_sum_range' hp y
  simp_rw [h, Finset.mul_sum]
  rw [Finset.sum_comm]
  rw [← Finset.sum_range_add_sum_Ico _ (Nat.one_le_iff_ne_zero.2 hR.ne'),
    ← Finset.sum_range_add_sum_Ico (fun k => (∑ t, a t) * (p.coeff k * (0 : K) ^ k))
      (Nat.one_le_iff_ne_zero.2 hR.ne')]
  have hhigh : ∑ k ∈ Ico 1 R, ∑ t, a t * (p.coeff k * x t ^ k) = 0 := by
    refine Finset.sum_eq_zero fun k hk => ?_
    have hk' := Finset.mem_Ico.1 hk
    calc ∑ t, a t * (p.coeff k * x t ^ k) = p.coeff k * ∑ t, a t * x t ^ k := by
          rw [Finset.mul_sum]
          refine Finset.sum_congr rfl fun t _ => ?_
          ring
      _ = 0 := by rw [hmom k hk'.1 hk'.2, mul_zero]
  have hzero : ∑ k ∈ Ico 1 R, (∑ t, a t) * (p.coeff k * (0 : K) ^ k) = 0 := by
    refine Finset.sum_eq_zero fun k hk => ?_
    have hk1 : k ≠ 0 := by have := (Finset.mem_Ico.1 hk).1; omega
    simp [zero_pow hk1]
  rw [hhigh, hzero]
  simp [Finset.sum_mul]

/-- Double counting: a sum over vertices and directions of edge weights times a function is a
sum over edges of the weight times the values at both endpoints. -/
theorem sum_edgeW (w : Fin Q → Finset (Fin Q) → K) (f : Finset (Fin Q) → Fin Q → K) (t : Fin Q) :
    ∑ v, edgeW w v t * f v t
      = ∑ u ∈ univ.filter (fun u => t ∉ u), w t u * (f u t + f (insert t u) t) := by
  classical
  rw [← Finset.sum_filter_add_sum_filter_not univ (fun v => t ∉ v)]
  have h1 : ∑ v ∈ univ.filter (fun v => t ∉ v), edgeW w v t * f v t
      = ∑ u ∈ univ.filter (fun u => t ∉ u), w t u * f u t := by
    refine Finset.sum_congr rfl fun v hv => ?_
    have hv' : t ∉ v := (Finset.mem_filter.1 hv).2
    simp [edgeW, hv']
  have h2 : ∑ v ∈ univ.filter (fun v => ¬ t ∉ v), edgeW w v t * f v t
      = ∑ u ∈ univ.filter (fun u => t ∉ u), w t u * f (insert t u) t := by
    refine Finset.sum_nbij' (fun v => v.erase t) (fun u => insert t u) ?_ ?_ ?_ ?_ ?_
    · intro v hv
      simp
    · intro u hu
      simp
    · intro v hv
      have hv' : t ∈ v := by simpa using hv
      exact Finset.insert_erase hv'
    · intro u hu
      have hu' : t ∉ u := (Finset.mem_filter.1 hu).2
      exact Finset.erase_insert hu'
    · intro v hv
      have hv' : t ∈ v := by simpa using hv
      simp [edgeW, hv', Finset.insert_erase hv']
  rw [h1, h2, ← Finset.sum_add_distrib]
  refine Finset.sum_congr rfl fun u _ => ?_
  ring

/-- **Stress duality (soundness).** If a stress is supported on good edges, its total weight
vanishes. -/
theorem stress_total_eq_zero [CharZero K] {R : ℕ} (x : Fin Q → K) (p : Finset (Fin Q) → K[X])
    (hdeg : ∀ v, (p v).natDegree < R) (h0 : ∀ v, (p v).eval 0 = 1)
    (w : Fin Q → Finset (Fin Q) → K)
    (hmom : ∀ v k, 1 ≤ k → k < R → ∑ t, edgeW w v t * x t ^ k = 0)
    (hgood : ∀ t u, t ∉ u → w t u ≠ 0 → (p u).eval (x t) + (p (insert t u)).eval (x t) = 0) :
    ∑ t, ∑ u ∈ univ.filter (fun u => t ∉ u), w t u = 0 := by
  have hcollapse : ∀ v, ∑ t, edgeW w v t * (p v).eval (x t) = ∑ t, edgeW w v t := by
    intro v
    rw [moment_collapse x (fun t => edgeW w v t) (hmom v) (p v) (hdeg v), h0 v, mul_one]
  have hleft : ∑ v, ∑ t, edgeW w v t * (p v).eval (x t) = 0 := by
    rw [Finset.sum_comm]
    refine Finset.sum_eq_zero fun t _ => ?_
    rw [sum_edgeW w (fun v t => (p v).eval (x t)) t]
    refine Finset.sum_eq_zero fun u hu => ?_
    have hu' : t ∉ u := (Finset.mem_filter.1 hu).2
    by_cases hw : w t u = 0
    · rw [hw, zero_mul]
    · rw [hgood t u hu' hw, mul_zero]
  have hright : ∑ v, ∑ t, edgeW w v t * (p v).eval (x t)
      = 2 * ∑ t, ∑ u ∈ univ.filter (fun u => t ∉ u), w t u := by
    rw [Finset.sum_congr rfl fun v _ => hcollapse v, Finset.sum_comm, Finset.mul_sum]
    refine Finset.sum_congr rfl fun t _ => ?_
    have := sum_edgeW w (fun _ _ => (1 : K)) t
    simp only [mul_one] at this
    rw [this, Finset.mul_sum]
    refine Finset.sum_congr rfl fun u _ => ?_
    ring
  have h2 : (2 : K) * ∑ t, ∑ u ∈ univ.filter (fun u => t ∉ u), w t u = 0 := by
    rw [← hright, hleft]
  exact (mul_eq_zero.1 h2).resolve_left (by norm_num)

/-! ### Products of designs -/

/-- An edge that is good for the first factor stays good after multiplying both endpoints by
the same second-factor polynomial. -/
theorem product_edge_good {p p' : K[X]} {y : K} (h : p.eval y + p'.eval y = 0) (s : K[X]) :
    (p * s).eval y + (p' * s).eval y = 0 := by
  rw [eval_mul, eval_mul, ← add_mul, h, zero_mul]

theorem natDegree_product_le {p s : K[X]} {R₁ R₂ : ℕ} (hp : p.natDegree ≤ R₁ - 1)
    (hs : s.natDegree ≤ R₂ - 1) : (p * s).natDegree ≤ (R₁ - 1) + (R₂ - 1) :=
  (natDegree_mul_le).trans (Nat.add_le_add hp hs)

theorem product_eval_zero {p s : K[X]} (hp : p.eval 0 = 1) (hs : s.eval 0 = 1) :
    (p * s).eval 0 = 1 := by
  rw [eval_mul, hp, hs, one_mul]

end EthConsequences.Stress
