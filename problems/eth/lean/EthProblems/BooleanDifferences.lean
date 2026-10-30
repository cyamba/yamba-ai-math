/-
Problem ETH-A06 (problems/eth/A-algebraic-core/ETH-A06-boolean-differences.md).

Möbius inversion on the Boolean lattice, the identity behind Lemma "Taylor coefficients
from fixed Boolean substitutions" in OpenAI's ETH refutation: if `F U = Σ_{T ⊆ U} a T`
(evaluation of a multilinear polynomial at the indicator `1_U`), then
`a E = Σ_{U ⊆ E} (-1)^{|E|+|U|} F U`.
-/
import Mathlib.Algebra.BigOperators.Group.Finset.Powerset
import Mathlib.Tactic.Ring

open Finset

namespace EthProblems.BooleanDifferences

theorem mobius_powerset {α R : Type*} [DecidableEq α] [CommRing R] (E : Finset α) :
    ∀ a : Finset α → R,
      ∑ U ∈ E.powerset, (-1 : R) ^ (#E + #U) * (∑ T ∈ U.powerset, a T) = a E := by
  induction E using Finset.induction_on with
  | empty => intro a; simp
  | insert x E hx ih =>
    intro a
    rw [Finset.sum_powerset_insert hx]
    have h1 : ∀ U ∈ E.powerset, (-1 : R) ^ (#(insert x E) + #U) * (∑ T ∈ U.powerset, a T)
        = -((-1 : R) ^ (#E + #U) * ∑ T ∈ U.powerset, a T) := by
      intro U _
      rw [card_insert_of_notMem hx]
      ring
    have h2 : ∀ U ∈ E.powerset,
        (-1 : R) ^ (#(insert x E) + #(insert x U)) * (∑ T ∈ (insert x U).powerset, a T)
          = (-1 : R) ^ (#E + #U) *
              ((∑ T ∈ U.powerset, a T) + ∑ T ∈ U.powerset, a (insert x T)) := by
      intro U hU
      have hxU : x ∉ U := fun h => hx (mem_powerset.mp hU h)
      rw [card_insert_of_notMem hx, card_insert_of_notMem hxU, sum_powerset_insert hxU]
      ring
    rw [sum_congr rfl h1, sum_congr rfl h2, sum_neg_distrib]
    simp_rw [mul_add]
    rw [sum_add_distrib, ih (fun T => a (insert x T))]
    ring

end EthProblems.BooleanDifferences
