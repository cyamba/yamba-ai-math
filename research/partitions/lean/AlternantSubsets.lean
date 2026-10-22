import Std

/-!
Finite subset combinatorics for the two-column alternant identity.
Only the bundled Std library is used. These statements do not assert a
polynomial identity or assume that any coloring polynomial is symmetric.
-/

namespace AlternantSubsets

def NoRise : List Bool → Prop
  | [] => True
  | [_] => True
  | x :: y :: xs => (x = false → y = false) ∧ NoRise (y :: xs)

def ones : List Bool → Nat
  | [] => 0
  | true :: xs => 1 + ones xs
  | false :: xs => ones xs

theorem ones_le_length (xs : List Bool) : ones xs ≤ xs.length := by
  induction xs with
  | nil => simp [ones]
  | cons x xs ih => cases x <;> simp_all [ones] <;> omega

theorem ones_append (xs ys : List Bool) : ones (xs ++ ys) = ones xs + ones ys := by
  induction xs with
  | nil => simp [ones]
  | cons x xs ih => cases x <;> simp_all [ones] <;> omega

theorem ones_replicate_true (n : Nat) : ones (List.replicate n true) = n := by
  induction n with
  | zero => rfl
  | succ n ih => simp [List.replicate_succ, ones, ih, Nat.add_comm]

theorem ones_replicate_false (n : Nat) : ones (List.replicate n false) = 0 := by
  induction n with
  | zero => rfl
  | succ n ih => simp [List.replicate_succ, ones, ih]

theorem noRise_tail (x : Bool) (xs : List Bool) (h : NoRise (x :: xs)) : NoRise xs := by
  cases xs with
  | nil => trivial
  | cons y ys => exact h.2

theorem false_head_forces_false (xs : List Bool) (h : NoRise (false :: xs)) :
    xs = List.replicate xs.length false := by
  induction xs with
  | nil => rfl
  | cons b bs ih =>
      have hb : b = false := h.1 rfl
      subst b
      have ht := ih h.2
      simpa [List.replicate_succ] using congrArg (List.cons false) ht

theorem noRise_replicates (p q : Nat) :
    NoRise (List.replicate p true ++ List.replicate q false) := by
  have hf : ∀ n, NoRise (List.replicate n false) := by
    intro n
    induction n with
    | zero => trivial
    | succ n ih =>
        cases n with
        | zero => trivial
        | succ n => exact ⟨fun _ => rfl, ih⟩
  induction p with
  | zero => exact hf q
  | succ p ih =>
      cases p with
      | zero =>
          cases q with
          | zero => trivial
          | succ q => exact ⟨by simp, hf (q + 1)⟩
      | succ p => exact ⟨by simp, ih⟩

/-- Collision-free bits in one block form its unique initial segment. -/
theorem noRise_iff_prefix (xs : List Bool) :
    NoRise xs ↔ xs = List.replicate (ones xs) true ++
      List.replicate (xs.length - ones xs) false := by
  constructor
  · intro h
    induction xs with
    | nil => rfl
    | cons b bs ih =>
        cases b with
        | false =>
            have he := false_head_forces_false bs h
            have hz : ones bs = 0 := by rw [he, ones_replicate_false]
            simpa [ones, hz, List.replicate_succ] using congrArg (List.cons false) he
        | true =>
            have he := ih (noRise_tail true bs h)
            have hl := ones_le_length bs
            have hd : (true :: bs).length - ones (true :: bs) = bs.length - ones bs := by
              simp only [List.length_cons, ones]
              omega
            simpa [ones, hd, List.replicate_succ, List.cons_append, Nat.add_comm] using
              congrArg (List.cons true) he
  · intro h
    rw [h]
    exact noRise_replicates _ _

/-- Integer exponents avoid silently truncating a negative expression. -/
def exponent (m a i : Nat) (bit : Bool) : Int :=
  (m : Int) - 1 - (i : Int) + (if i < a then 1 else 0) + (if bit then 1 else 0)

/-- At the cut there is no collision. Elsewhere exactly a 0-to-1 rise collides. -/
theorem adjacent_exponent_collision (m a i : Nat) (x y : Bool) :
    exponent m a i x = exponent m a (i + 1) y ↔
      i + 1 ≠ a ∧ x = false ∧ y = true := by
  by_cases h₁ : i < a <;> by_cases h₂ : i + 1 < a <;>
    cases x <;> cases y <;> simp [exponent, h₁, h₂] <;> omega

theorem adjacent_exponent_weakly_decreasing (m a i : Nat) (x y : Bool) :
    exponent m a (i + 1) y ≤ exponent m a i x := by
  by_cases h₁ : i < a <;> by_cases h₂ : i + 1 < a <;>
    cases x <;> cases y <;> simp [exponent, h₁, h₂] <;> omega

def candidate (m a b j : Nat) : List Bool :=
  (List.replicate j true ++ List.replicate (a - j) false) ++
  (List.replicate (b - j) true ++ List.replicate (m - a - (b - j)) false)

theorem candidate_take (m a b j : Nat) (hj : j ≤ a) :
    (candidate m a b j).take a =
      List.replicate j true ++ List.replicate (a - j) false := by
  have hl : (List.replicate j true ++ List.replicate (a - j) false).length = a := by
    simp only [List.length_append, List.length_replicate]
    omega
  simpa only [hl, candidate, List.append_assoc] using (List.take_append_length
    (l₁ := List.replicate j true ++ List.replicate (a - j) false)
    (l₂ := List.replicate (b - j) true ++ List.replicate (m - a - (b - j)) false))

theorem candidate_drop (m a b j : Nat) (hj : j ≤ a) :
    (candidate m a b j).drop a =
      List.replicate (b - j) true ++ List.replicate (m - a - (b - j)) false := by
  have hl : (List.replicate j true ++ List.replicate (a - j) false).length = a := by
    simp only [List.length_append, List.length_replicate]
    omega
  simpa only [hl, candidate, List.append_assoc] using (List.drop_append_length
    (l₁ := List.replicate j true ++ List.replicate (a - j) false)
    (l₂ := List.replicate (b - j) true ++ List.replicate (m - a - (b - j)) false))

theorem candidate_length (m a b j : Nat) (hba : b ≤ a) (hab : a + b ≤ m)
    (hj : j ≤ b) : (candidate m a b j).length = m := by
  simp only [candidate, List.length_append, List.length_replicate]
  omega

theorem candidate_ones (m a b j : Nat) (hj : j ≤ b) :
    ones (candidate m a b j) = b := by
  simp only [candidate, ones_append, ones_replicate_true, ones_replicate_false,
    Nat.add_zero]
  omega

theorem candidate_noRise (m a b j : Nat) (hj : j ≤ a) :
    NoRise ((candidate m a b j).take a) ∧ NoRise ((candidate m a b j).drop a) := by
  rw [candidate_take m a b j hj, candidate_drop m a b j hj]
  exact ⟨noRise_replicates _ _, noRise_replicates _ _⟩

theorem candidate_injective (m a b j k : Nat) (hj : j ≤ a) (hk : k ≤ a)
    (he : candidate m a b j = candidate m a b k) : j = k := by
  have ht := congrArg (fun xs => ones (xs.take a)) he
  rw [candidate_take m a b j hj, candidate_take m a b k hk] at ht
  simpa only [ones_append, ones_replicate_true, ones_replicate_false, Nat.add_zero]
    using ht

/-- Exact and unique classification of every two-block subset of size b.
Every j in 0..b is feasible when b ≤ a and a+b ≤ m. -/
theorem two_block_classification (m a b : Nat) (hba : b ≤ a) (hab : a + b ≤ m)
    (xs : List Bool) (hlen : xs.length = m) (hones : ones xs = b) :
    (NoRise (xs.take a) ∧ NoRise (xs.drop a)) ↔
      ∃ j, (j ≤ b ∧ xs = candidate m a b j) ∧
        ∀ k, (k ≤ b ∧ xs = candidate m a b k) → k = j := by
  constructor
  · rintro ⟨ht, hd⟩
    have hl : (xs.take a).length = a := List.length_take_of_le (by omega)
    have hr : (xs.drop a).length = m - a := by simp [hlen]
    have hc : ones (xs.take a) + ones (xs.drop a) = b := by
      rw [← ones_append, List.take_append_drop, hones]
    let j := ones (xs.take a)
    have hj : j ≤ b := by dsimp [j]; omega
    have he : xs = candidate m a b j := by
      have hsplit := (List.take_append_drop a xs).symm
      rw [(noRise_iff_prefix _).mp ht, (noRise_iff_prefix _).mp hd] at hsplit
      have hrest : ones (xs.drop a) = b - j := by dsimp [j]; omega
      simpa only [hl, hr, hrest, candidate, j, List.append_assoc] using hsplit
    refine ⟨j, ⟨hj, he⟩, ?_⟩
    intro k hk
    exact candidate_injective m a b k j (by omega) (by omega) (hk.2.symm.trans he)
  · rintro ⟨j, ⟨hj, he⟩, _⟩
    rw [he]
    exact candidate_noRise m a b j (by omega)

end AlternantSubsets

#check @AlternantSubsets.noRise_iff_prefix
#check @AlternantSubsets.adjacent_exponent_collision
#check @AlternantSubsets.two_block_classification
#print axioms AlternantSubsets.noRise_iff_prefix
#print axioms AlternantSubsets.adjacent_exponent_collision
#print axioms AlternantSubsets.adjacent_exponent_weakly_decreasing
#print axioms AlternantSubsets.candidate_length
#print axioms AlternantSubsets.candidate_ones
#print axioms AlternantSubsets.candidate_injective
#print axioms AlternantSubsets.two_block_classification
