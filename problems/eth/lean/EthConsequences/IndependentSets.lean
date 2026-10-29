import Mathlib.Combinatorics.SimpleGraph.Basic
import Mathlib.Data.Fintype.Pi
import Mathlib.Data.Fintype.Powerset

/-!
# Independent sets as satisfying assignments of a 2-CNF

The first reduction in Corollary 1.3 of openai/math result 378: for a graph `G = (V, E)`,
the independent sets correspond bijectively to the satisfying assignments of
`⋀_{uw ∈ E} (¬x_u ∨ ¬x_w)`. Hence `#IndependentSets(G) = #SAT(F_G)`, and the subexponential
counting algorithm for `2`-CNF transfers to independent-set counting on `|V|` variables.
-/

namespace EthConsequences.IndependentSets

open Finset

variable {V : Type*} [Fintype V] [DecidableEq V] (G : SimpleGraph V) [DecidableRel G.Adj]

/-- Satisfying assignments of the 2-CNF `⋀_{uw ∈ E} (¬x_u ∨ ¬x_w)`. -/
def satAssignments : Finset (V → Bool) :=
  univ.filter (fun x => ∀ u w, G.Adj u w → ¬ (x u = true ∧ x w = true))

/-- Independent sets of `G`, as finsets of vertices. -/
def indepSets : Finset (Finset V) :=
  univ.filter (fun s => ∀ u ∈ s, ∀ w ∈ s, ¬ G.Adj u w)

/-- The number of independent sets equals the number of satisfying assignments of `F_G`. -/
theorem card_indepSets_eq_card_satAssignments :
    (indepSets G).card = (satAssignments G).card := by
  refine Finset.card_bij (fun s _ => fun v => decide (v ∈ s)) ?_ ?_ ?_
  · intro s hs
    simp only [indepSets, satAssignments, mem_filter, mem_univ, true_and] at hs ⊢
    intro u w huw h
    simp only [decide_eq_true_eq] at h
    exact hs u h.1 w h.2 huw
  · intro s _ s' _ h
    ext v
    have := congrFun h v
    simpa using this
  · intro x hx
    refine ⟨univ.filter (fun v => x v = true), ?_, ?_⟩
    · simp only [indepSets, satAssignments, mem_filter, mem_univ, true_and] at hx ⊢
      intro u hu w hw huw
      exact hx u w huw ⟨hu, hw⟩
    · funext v
      cases h : x v <;> simp [h]

/-- The same correspondence for the independent sets of a fixed size `k` (weighting by
`V^|s|` in the tensor-network contraction counts these simultaneously). -/
theorem card_indepSets_size_eq (k : ℕ) :
    ((indepSets G).filter (fun s => s.card = k)).card
      = ((satAssignments G).filter (fun x => (univ.filter (fun v => x v = true)).card = k)).card := by
  refine Finset.card_bij (fun s _ => fun v => decide (v ∈ s)) ?_ ?_ ?_
  · intro s hs
    simp only [indepSets, satAssignments, mem_filter, mem_univ, true_and] at hs ⊢
    refine ⟨?_, ?_⟩
    · intro u w huw h
      simp only [decide_eq_true_eq] at h
      exact hs.1 u h.1 w h.2 huw
    · simpa [Finset.filter_mem_eq_inter] using hs.2
  · intro s _ s' _ h
    ext v
    have := congrFun h v
    simpa using this
  · intro x hx
    refine ⟨univ.filter (fun v => x v = true), ?_, ?_⟩
    · simp only [indepSets, satAssignments, mem_filter, mem_univ, true_and] at hx ⊢
      exact ⟨fun u hu w hw huw => hx.1 u w huw ⟨hu, hw⟩, hx.2⟩
    · funext v
      cases h : x v <;> simp [h]

end EthConsequences.IndependentSets
