import Mathlib.LinearAlgebra.Lagrange
import Mathlib.Algebra.BigOperators.Group.Finset.Powerset
import Mathlib.Data.Fintype.Powerset

/-!
# The subcube obstruction for point-dependent swap-algebra designs (subresult SR-02)

Subresult SR-02 reformulates point-dependent measurement designs in the swap algebra of
openai/math result 378 as the *cube polynomial problem* `CP(Q, R)`: attach to every vertex
`ε ∈ {0,1}^Q` a polynomial `p_ε(T)` of degree `< R` with `p_ε(0) = 1`; an edge
`(ε, ε ⊕ e_t)` in direction `t` is *good* when `p_ε(t) + p_{ε ⊕ e_t}(t) = 0`; bad edges in
direction `t` cost measurements at evaluation point `t`.

This file proves the basic obstruction: **no `R`-dimensional subcube can have all of its
edges good.** Restricting to a subcube in directions `t_1, ..., t_R` (distinct nodes), the
vertices are subsets `B ⊆ Fin R`. Summing the Lagrange extrapolation identity
`p(0) = ∑_i ℓ_i p(t_i)` over all `2^R` vertices, each inner sum over the cube vanishes edge
by edge, while the left side is `2^R ≠ 0`.

Consequently the bad edges must hit every `R`-subcube, which gives the lower bound
`(bad fraction) ≥ 2^(1-R) / R` recorded in SR-02.
-/

namespace EthConsequences.Subcube

open Polynomial Finset

variable {K : Type*} [Field K]

/-- Lagrange extrapolation to `0` from `R` distinct nodes, valid for degree `< R`. -/
theorem eval_zero_eq_sum {R : ℕ} (t : Fin R → K) (ht : Function.Injective t) (p : K[X])
    (hp : p.degree < R) :
    p.eval 0 = ∑ i, (Lagrange.basis univ t i).eval 0 * p.eval (t i) := by
  have hinj : Set.InjOn t (univ : Finset (Fin R)) := ht.injOn
  have hdeg : p.degree < (univ : Finset (Fin R)).card := by simpa using hp
  conv_lhs => rw [Lagrange.eq_interpolate hinj hdeg]
  rw [Lagrange.interpolate_apply, eval_finsetSum]
  refine Finset.sum_congr rfl (fun i _ => ?_)
  rw [eval_mul, eval_C]
  ring

variable [CharZero K]

/-- **Subcube obstruction.** There is no family of polynomials `p B` (one per vertex `B` of
the `R`-cube, encoded as `B : Finset (Fin R)`) of degree `< R` with `p B (0) = 1` such that
every edge `(B, insert i B)` is good: `p B (t i) + p (insert i B) (t i) = 0`. -/
theorem no_good_subcube {R : ℕ} (t : Fin R → K) (ht : Function.Injective t)
    (p : Finset (Fin R) → K[X]) (hdeg : ∀ B, (p B).degree < R) (h0 : ∀ B, (p B).eval 0 = 1)
    (hedge : ∀ i B, i ∉ B → (p B).eval (t i) + (p (insert i B)).eval (t i) = 0) : False := by
  have hsum : ∑ B : Finset (Fin R), (p B).eval 0
      = ∑ i, (Lagrange.basis univ t i).eval 0 * ∑ B : Finset (Fin R), (p B).eval (t i) := by
    simp_rw [eval_zero_eq_sum t ht _ (hdeg _), Finset.mul_sum]
    rw [Finset.sum_comm]
  have hzero : ∀ i, ∑ B : Finset (Fin R), (p B).eval (t i) = 0 := by
    intro i
    have huniv : (univ : Finset (Finset (Fin R))) = (insert i (univ.erase i)).powerset := by
      rw [Finset.insert_erase (mem_univ i), Finset.powerset_univ]
    have hnot : i ∉ univ.erase i := Finset.notMem_erase i univ
    calc ∑ B : Finset (Fin R), (p B).eval (t i)
        = ∑ B ∈ (insert i (univ.erase i)).powerset, (p B).eval (t i) := by rw [← huniv]
      _ = ∑ B ∈ (univ.erase i).powerset,
            ((p B).eval (t i) + (p (insert i B)).eval (t i)) := by
          rw [Finset.sum_powerset_insert hnot, Finset.sum_add_distrib]
      _ = 0 := by
          apply Finset.sum_eq_zero
          intro B hB
          exact hedge i B (fun h => hnot (mem_powerset.1 hB h))
  simp_rw [h0, hzero, mul_zero, Finset.sum_const_zero] at hsum
  simp at hsum

end EthConsequences.Subcube
