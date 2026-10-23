import PartitionH3.Alternant
import SignedArrays
import Mathlib.Data.List.OfFn

/-! The original list inversion-parity sign agrees with the actual finite
permutation sign. The proof uses adjacent position swaps, including `m = 0`. -/

noncomputable section

namespace PartitionH3

def permutationLabels {m : ℕ} (sigma : Equiv.Perm (Fin m)) : List ℕ :=
  List.ofFn (fun i => (sigma i).val)

theorem ofFn_two_split {α : Type*} {n : ℕ} (f : Fin (n + 1) → α) (i : Fin n) :
    List.ofFn f = (List.ofFn f).take i.val ++
      f i.castSucc :: f i.succ :: (List.ofFn f).drop (i.val + 2) := by
  have h0 : i.val < (List.ofFn f).length := by simp; omega
  have h1 : i.val + 1 < (List.ofFn f).length := by simp
  calc
    List.ofFn f = (List.ofFn f).take i.val ++ (List.ofFn f).drop i.val :=
      (List.take_append_drop _ _).symm
    _ = _ := by
      rw [List.drop_eq_getElem_cons h0, List.drop_eq_getElem_cons h1]
      simp only [List.getElem_ofFn]
      rfl

theorem ofFn_adjacent_swap {α : Type*} {n : ℕ} (f : Fin (n + 1) → α) (i : Fin n) :
    List.ofFn (fun k => f (Equiv.swap i.castSucc i.succ k)) =
      (List.ofFn f).take i.val ++ f i.succ :: f i.castSucc ::
        (List.ofFn f).drop (i.val + 2) := by
  let g := fun k => f (Equiv.swap i.castSucc i.succ k)
  have ht : (List.ofFn g).take i.val = (List.ofFn f).take i.val := by
    apply List.ext_getElem (by simp)
    intro k hk _
    have hki : k < i.val := by
      simp only [List.length_take, List.length_ofFn] at hk
      omega
    simp only [List.getElem_take, List.getElem_ofFn, g]
    rw [Equiv.swap_apply_of_ne_of_ne]
    · intro he; have hv := congrArg Fin.val he; change k = i.val at hv; omega
    · intro he; have hv := congrArg Fin.val he; change k = i.val + 1 at hv; omega
  have hd : (List.ofFn g).drop (i.val + 2) = (List.ofFn f).drop (i.val + 2) := by
    apply List.ext_getElem (by simp)
    intro k hk _
    simp only [List.getElem_drop, List.getElem_ofFn, g]
    rw [Equiv.swap_apply_of_ne_of_ne]
    · intro he; have hv := congrArg Fin.val he; change i.val + 2 + k = i.val at hv; omega
    · intro he; have hv := congrArg Fin.val he; change i.val + 2 + k = i.val + 1 at hv; omega
  have he := ofFn_two_split g i
  rw [ht, hd] at he
  simpa only [g, Equiv.swap_apply_left, Equiv.swap_apply_right] using he

theorem permutationLabels_one (m : ℕ) :
    permutationLabels (1 : Equiv.Perm (Fin m)) = List.range m := by
  apply List.ext_getElem (by simp [permutationLabels])
  intro k hk hk'
  simp [permutationLabels]

theorem permutationLabels_adjacent_sign {n : ℕ} (sigma : Equiv.Perm (Fin (n + 1)))
    (i : Fin n) :
    SignedArrays.permutationSign (permutationLabels (sigma * Equiv.swap i.castSucc i.succ)) =
      -SignedArrays.permutationSign (permutationLabels sigma) := by
  let f := fun k => (sigma k).val
  have hne : f i.castSucc ≠ f i.succ := by
    intro he
    have hv := congrArg Fin.val (sigma.injective (Fin.ext he))
    simp only [Fin.val_castSucc, Fin.val_succ] at hv
    omega
  have hs := SignedArrays.permutationSign_adjacent_swap
    ((List.ofFn f).take i.val) ((List.ofFn f).drop (i.val + 2))
    (f i.castSucc) (f i.succ) hne
  rw [← ofFn_two_split f i, ← ofFn_adjacent_swap f i] at hs
  exact hs

/-- Compatibility of the original list determinant sign and Mathlib's sign. -/
theorem permutationSign_permutationLabels {m : ℕ} (sigma : Equiv.Perm (Fin m)) :
    SignedArrays.permutationSign (permutationLabels sigma) = (Equiv.Perm.sign sigma : ℤ) := by
  cases m with
  | zero =>
      have he : sigma = 1 := Subsingleton.elim _ _
      rw [he, permutationLabels_one, SignedArrays.identity_permutationSign]
      simp
  | succ n =>
      refine Submonoid.induction_of_closure_eq_top_right
        (motive := fun tau : Equiv.Perm (Fin (n + 1)) =>
          SignedArrays.permutationSign (permutationLabels tau) = (Equiv.Perm.sign tau : ℤ))
        (Equiv.Perm.mclosure_swap_castSucc_succ n) sigma ?_ ?_
      · rw [permutationLabels_one, SignedArrays.identity_permutationSign]
        simp
      · intro tau s hs ih
        obtain ⟨i, rfl⟩ := hs
        have hne : i.castSucc ≠ i.succ := by
          intro he
          have hv := congrArg Fin.val he
          simp only [Fin.val_castSucc, Fin.val_succ] at hv
          omega
        rw [permutationLabels_adjacent_sign, ih, Equiv.Perm.sign_mul, Equiv.Perm.sign_swap hne]
        simp

end PartitionH3

#check @PartitionH3.permutationSign_permutationLabels
#print axioms PartitionH3.ofFn_adjacent_swap
#print axioms PartitionH3.permutationLabels_adjacent_sign
#print axioms PartitionH3.permutationSign_permutationLabels
