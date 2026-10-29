import Mathlib.Data.Nat.Choose.Sum
import Mathlib.Algebra.BigOperators.Group.Finset.Powerset
import Mathlib.Data.Fintype.Powerset
import Mathlib.Tactic.Ring

/-!
# Boolean differences: recovering a diagonal sum from fixed Boolean substitutions

This file formalizes the combinatorial core of Lemma 3.2 ("Boolean differences") in
openai/math result 378. Boolean points of `{0,1}^ι` are encoded as finsets `x : Finset ι`
(the support). For a function `f : Finset ι → R` the Möbius coefficients on the Boolean
lattice are

  `mobius f E = ∑_{U ⊆ E} (-1)^{|E \ U|} f U`.

* `mobius_inversion`: `f X = ∑_{E ⊆ X} mobius f E` (Möbius inversion on subsets).
* `boolean_differences`: if, for every Boolean point `x`, the function `g x` has Möbius
  coefficients vanishing above size `q` (this is what "degree at most `q`" means for the
  multilinear representative of the paper's polynomial `p_x`), then the diagonal sum
  `∑_x g x x` equals the inclusion and exclusion over pairs `U ⊆ E`, `|E| ≤ q`, of sums in
  which the substituted point `U` is fixed and only the summation range `x ⊇ E` varies.

This is exactly the identity used to compute Taylor coefficients by fixed Boolean
substitutions (preprint, equation (3.6)).
-/

namespace EthConsequences.BooleanDifferences

open Finset

variable {ι : Type*} [DecidableEq ι] {R : Type*} [CommRing R]

/-- Möbius coefficients on the Boolean lattice of subsets. -/
def mobius (f : Finset ι → R) (E : Finset ι) : R :=
  ∑ U ∈ E.powerset, (-1 : R) ^ (E \ U).card * f U

/-- One-step expansion of a Möbius coefficient at `insert a E`. -/
theorem mobius_insert (f : Finset ι → R) {a : ι} {E : Finset ι} (ha : a ∉ E) :
    mobius f (insert a E) = -mobius f E + mobius (fun U => f (insert a U)) E := by
  unfold mobius
  rw [Finset.sum_powerset_insert ha]
  have h1 : ∀ U ∈ E.powerset,
      (-1 : R) ^ (insert a E \ U).card * f U = -((-1 : R) ^ (E \ U).card * f U) := by
    intro U hU
    have haU : a ∉ U := fun h => ha (mem_powerset.1 hU h)
    rw [Finset.insert_sdiff_of_notMem _ haU, Finset.card_insert_of_notMem
      (fun h => ha (Finset.mem_sdiff.1 h).1), pow_succ]
    ring
  have h2 : ∀ U ∈ E.powerset,
      (-1 : R) ^ (insert a E \ insert a U).card * f (insert a U)
        = (-1 : R) ^ (E \ U).card * f (insert a U) := by
    intro U _
    rw [Finset.insert_sdiff_insert, Finset.sdiff_insert_of_notMem ha]
  rw [Finset.sum_congr rfl h1, Finset.sum_congr rfl h2, Finset.sum_neg_distrib]

/-- Möbius inversion on the Boolean lattice: `f X = ∑_{E ⊆ X} mobius f E`. -/
theorem mobius_inversion (X : Finset ι) : ∀ f : Finset ι → R,
    ∑ E ∈ X.powerset, mobius f E = f X := by
  induction X using Finset.induction_on with
  | empty =>
    intro f
    simp [mobius]
  | insert a X ha ih =>
    intro f
    rw [Finset.sum_powerset_insert ha]
    have h : ∀ E ∈ X.powerset,
        mobius f (insert a E) = -mobius f E + mobius (fun U => f (insert a U)) E :=
      fun E hE => mobius_insert f (fun h => ha (mem_powerset.1 hE h))
    rw [Finset.sum_congr rfl h, Finset.sum_add_distrib, Finset.sum_neg_distrib, ih f,
      ih (fun U => f (insert a U))]
    ring

variable [Fintype ι]

/-- **Boolean differences** (openai/math 378, Lemma 3.2, combinatorial core).
If every `g x` has Möbius coefficients supported on sets of size at most `q`, then
`∑_x g x x = ∑_{|E| ≤ q} ∑_{U ⊆ E} (-1)^{|E \ U|} ∑_{x ⊇ E} g x U`. -/
theorem boolean_differences (q : ℕ) (g : Finset ι → Finset ι → R)
    (hdeg : ∀ x E, q < E.card → mobius (g x) E = 0) :
    ∑ x : Finset ι, g x x
      = ∑ E ∈ (univ : Finset (Finset ι)).filter (fun E => E.card ≤ q),
          ∑ U ∈ E.powerset, (-1 : R) ^ (E \ U).card *
            ∑ x ∈ (univ : Finset (Finset ι)).filter (fun x => E ⊆ x), g x U := by
  -- Step 1: expand each diagonal value by Möbius inversion and drop large E.
  have step1 : ∀ x : Finset ι, g x x
      = ∑ E ∈ (univ : Finset (Finset ι)).filter (fun E => E.card ≤ q),
          if E ⊆ x then mobius (g x) E else 0 := by
    intro x
    rw [← mobius_inversion x (g x)]
    rw [Finset.sum_ite, Finset.sum_const_zero, add_zero]
    symm
    apply Finset.sum_subset
    · intro E hE
      simp only [mem_filter, mem_univ, true_and] at hE
      exact mem_powerset.2 hE.2
    · intro E hE hnot
      have hEx : E ⊆ x := mem_powerset.1 hE
      have : ¬ E.card ≤ q := by
        intro hq
        exact hnot (by simp [hq, hEx])
      exact hdeg x E (by omega)
  rw [Finset.sum_congr rfl (fun x _ => step1 x), Finset.sum_comm]
  refine Finset.sum_congr rfl (fun E _ => ?_)
  -- Step 2: swap the remaining sums.
  rw [← Finset.sum_filter]
  unfold mobius
  rw [Finset.sum_comm]
  refine Finset.sum_congr rfl (fun U _ => ?_)
  rw [Finset.mul_sum]

end EthConsequences.BooleanDifferences
