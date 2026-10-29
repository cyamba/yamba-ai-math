import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Data.Fintype.BigOperators
import Mathlib.Data.Fintype.Pi

/-!
# Separation of a sum over assignments by fixing shared measurements

Algebraic core of Lemma 3.1 ("measurement separation") in openai/math result 378.
Variables are split into groups `g : ι`; group `g` takes values `u : X g` and has a
measurement `meas g u : Y g`. Each group factor `A g` may depend on its own block and on the
measurements of all groups (in the paper: on `x_g` and on `C_h x_h` for `h ≠ g`; the
invariance hypothesis of the preprint is what makes the factor a function of these data).
Fixing the measurement tuple `y` decouples the sum into a product of independent group sums:

  `∑_x ∏_g A_g(x_g, meas(x)) = ∑_y ∏_g ∑_{u : meas_g u = y_g} A_g(u, y)`.

Every Boolean assignment has exactly one measurement tuple, which is the whole proof.
-/

namespace EthConsequences.Separation

open Finset

variable {ι : Type*} [Fintype ι] [DecidableEq ι]
  {X : ι → Type*} [∀ g, Fintype (X g)]
  {Y : ι → Type*} [∀ g, Fintype (Y g)] [∀ g, DecidableEq (Y g)]
  {R : Type*} [CommRing R]

/-- Measurement separation: a sum over all assignments of a product of group factors equals
the sum over measurement tuples of the product of the per-group fibre sums. -/
theorem sum_prod_eq_sum_measurements (meas : ∀ g, X g → Y g)
    (A : ∀ g, X g → (∀ h, Y h) → R) :
    ∑ x : (∀ g, X g), ∏ g, A g (x g) (fun h => meas h (x h))
      = ∑ y : (∀ g, Y g), ∏ g, ∑ u ∈ univ.filter (fun u => meas g u = y g), A g u y := by
  -- Expand each product of sums into a sum over choice functions.
  simp_rw [Finset.prod_univ_sum]
  -- Rewrite the inner sums over `piFinset` as filtered sums over all assignments.
  have hpi : ∀ y : (∀ g, Y g),
      Fintype.piFinset (fun g => univ.filter (fun u => meas g u = y g))
        = univ.filter (fun x : (∀ g, X g) => (fun h => meas h (x h)) = y) := by
    intro y
    ext x
    simp [Fintype.mem_piFinset, funext_iff]
  simp_rw [hpi, Finset.sum_filter]
  rw [Finset.sum_comm]
  refine Finset.sum_congr rfl (fun x _ => ?_)
  rw [Finset.sum_ite_eq]
  simp

end EthConsequences.Separation
