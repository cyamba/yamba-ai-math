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

/-- **At most `R - 1` directions of a cube can be entirely good.** In a `d`-dimensional cube of
polynomials of degree `< R` with value `1` at `0`, the directions all of whose edges are good
are at most `R - 1` in number: the sum `H = ∑_B p_B` has degree `< R`, vanishes at the node of
every entirely good direction, and has `H(0) = 2^d ≠ 0`. For `d = R` this is
`no_good_subcube`; applied to subcubes it says that every `d`-dimensional subcube has bad edges
in at least `d - R + 1` of its directions. -/
theorem card_good_directions_lt {d R : ℕ} (t : Fin d → K) (ht : Function.Injective t)
    (p : Finset (Fin d) → K[X]) (hdeg : ∀ B, (p B).natDegree < R)
    (h0 : ∀ B, (p B).eval 0 = 1) (S : Finset (Fin d))
    (hgood : ∀ i ∈ S, ∀ B, i ∉ B → (p B).eval (t i) + (p (insert i B)).eval (t i) = 0) :
    S.card < R := by
  by_contra hS
  rw [not_lt] at hS
  have hzero : ∀ i ∈ S, (∑ B : Finset (Fin d), p B).eval (t i) = 0 := by
    intro i hi
    rw [eval_finsetSum]
    have huniv : (univ : Finset (Finset (Fin d))) = (insert i (univ.erase i)).powerset := by
      rw [Finset.insert_erase (mem_univ i), Finset.powerset_univ]
    have hnot : i ∉ univ.erase i := Finset.notMem_erase i univ
    calc ∑ B : Finset (Fin d), (p B).eval (t i)
        = ∑ B ∈ (insert i (univ.erase i)).powerset, (p B).eval (t i) := by rw [← huniv]
      _ = ∑ B ∈ (univ.erase i).powerset,
            ((p B).eval (t i) + (p (insert i B)).eval (t i)) := by
          rw [Finset.sum_powerset_insert hnot, Finset.sum_add_distrib]
      _ = 0 := by
          apply Finset.sum_eq_zero
          intro B hB
          exact hgood i hi B (fun h => hnot (mem_powerset.1 hB h))
  have hR : 1 ≤ R := by
    have := hdeg ∅
    omega
  have hdegH : (∑ B : Finset (Fin d), p B).natDegree < Fintype.card S := by
    have hle : (∑ B : Finset (Fin d), p B).natDegree ≤ R - 1 := by
      apply natDegree_sum_le_of_forall_le
      intro B _
      have := hdeg B
      omega
    rw [Fintype.card_coe]
    omega
  have hH0 : (∑ B : Finset (Fin d), p B) = 0 := by
    refine eq_zero_of_natDegree_lt_card_of_eval_eq_zero _ (f := fun i : S => t i) ?_ ?_ hdegH
    · intro a b hab
      exact Subtype.ext (ht hab)
    · intro i
      exact hzero i i.2
  have hval : (∑ B : Finset (Fin d), p B).eval 0 = (2 : K) ^ d := by
    rw [eval_finsetSum]
    simp [h0]
  rw [hH0, eval_zero] at hval
  exact (pow_ne_zero d (by norm_num : (2 : K) ≠ 0)) hval.symm

omit [CharZero K] in
/-- **The subcube identity.** For any family on the `R`-cube with degree `< R` and value `1`
at `0`, the edge defects `d(B, i) = p_B(t_i) + p_{B ∪ i}(t_i)` satisfy
`∑_i ℓ_i(0) ∑_{B ∌ i} d(B, i) = 2^R`, where `ℓ_i` is the Lagrange basis of the nodes.
Subresult SR-11 shows that these identities, one per `R`-subcube, are also sufficient:
every edge function satisfying all of them is the defect function of a family. -/
theorem subcube_identity {R : ℕ} (t : Fin R → K) (ht : Function.Injective t)
    (p : Finset (Fin R) → K[X]) (hdeg : ∀ B, (p B).degree < R) (h0 : ∀ B, (p B).eval 0 = 1) :
    ∑ i, (Lagrange.basis univ t i).eval 0 *
        ∑ B ∈ (univ.erase i).powerset, ((p B).eval (t i) + (p (insert i B)).eval (t i))
      = (2 : K) ^ R := by
  have hsplit : ∀ i, ∑ B : Finset (Fin R), (p B).eval (t i)
      = ∑ B ∈ (univ.erase i).powerset, ((p B).eval (t i) + (p (insert i B)).eval (t i)) := by
    intro i
    have huniv : (univ : Finset (Finset (Fin R))) = (insert i (univ.erase i)).powerset := by
      rw [Finset.insert_erase (mem_univ i), Finset.powerset_univ]
    have hnot : i ∉ univ.erase i := Finset.notMem_erase i univ
    rw [huniv, Finset.sum_powerset_insert hnot, Finset.sum_add_distrib]
  have hsum : ∑ B : Finset (Fin R), (p B).eval 0
      = ∑ i, (Lagrange.basis univ t i).eval 0 * ∑ B : Finset (Fin R), (p B).eval (t i) := by
    simp_rw [eval_zero_eq_sum t ht _ (hdeg _), Finset.mul_sum]
    rw [Finset.sum_comm]
  simp_rw [← hsplit]
  rw [← hsum]
  simp [h0]

end EthConsequences.Subcube
