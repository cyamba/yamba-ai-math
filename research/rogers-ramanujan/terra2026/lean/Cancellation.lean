import Std
namespace KR1Cancellation
abbrev Cell := Bool × Nat

def eligible : Cell → Bool
 | (false, 0) => false
 | _ => true

def toggle : Cell → Cell
 | (false, 0) => (false, 0)
 | (false, n+1) => (true, n)
 | (true, n) => (false, n+1)

def cancel : List Cell → List Cell
 | [] => []
 | x :: xs => if eligible x then toggle x :: xs else x :: cancel xs

def hasEligible : List Cell → Bool
 | [] => false
 | x :: xs => eligible x || hasEligible xs

def parity : List Cell → Bool
 | [] => false
 | (b,_) :: xs => Bool.xor b (parity xs)

def cellWeight (x : Cell) : Nat := (if x.1 then 1 else 0) + x.2

def weight (start : Nat) : List Cell → Nat
 | [] => 0
 | x :: xs => start * cellWeight x + weight (start+1) xs

theorem toggle_eligible (x : Cell) : eligible (toggle x) = eligible x := by
  rcases x with ⟨b,n⟩
  cases b <;> cases n <;> simp [toggle, eligible]

theorem toggle_involution (x : Cell) : toggle (toggle x) = x := by
  rcases x with ⟨b,n⟩
  cases b <;> cases n <;> simp [toggle]

theorem toggle_weight (x : Cell) : cellWeight (toggle x) = cellWeight x := by
  rcases x with ⟨b,n⟩
  cases b <;> cases n <;> simp [toggle, cellWeight] <;> omega

theorem toggle_marker (x : Cell) (h : eligible x = true) : (toggle x).1 = !x.1 := by
  rcases x with ⟨b,n⟩
  cases b <;> cases n <;> simp_all [toggle, eligible]

theorem cancel_involution (xs : List Cell) : cancel (cancel xs) = xs := by
  induction xs with
  | nil => rfl
  | cons x xs ih =>
    cases h : eligible x with
    | false => simp [cancel, h, ih]
    | true => simp [cancel, h, toggle_eligible, toggle_involution]

theorem cancel_weight (xs : List Cell) (start : Nat) :
    weight start (cancel xs) = weight start xs := by
  induction xs generalizing start with
  | nil => rfl
  | cons x xs ih =>
    cases h : eligible x with
    | false => simp [cancel, h, weight, ih]
    | true => simp [cancel, h, weight, toggle_weight]

theorem cancel_parity (xs : List Cell) (h : hasEligible xs = true) :
    parity (cancel xs) = !(parity xs) := by
  induction xs with
  | nil => simp [hasEligible] at h
  | cons x xs ih =>
    rcases x with ⟨b,n⟩
    cases b <;> cases n <;> simp_all [hasEligible, eligible, cancel, toggle, parity, Bool.xor]

theorem cancel_fixed (xs : List Cell) : cancel xs = xs ↔ hasEligible xs = false := by
  induction xs with
  | nil => simp [cancel, hasEligible]
  | cons x xs ih =>
    cases h : eligible x with
    | false => simp [cancel, hasEligible, h, ih]
    | true =>
      have ht := toggle_marker x h
      have neq : toggle x ≠ x := by
        intro eq
        have := congrArg Prod.fst eq
        rw [ht] at this
        cases hx : x.1 <;> simp [hx] at this
      simp [cancel, hasEligible, h, neq]

theorem inactive_is_zero (x : Cell) : eligible x = false ↔ x = (false, 0) := by
  rcases x with ⟨b,n⟩
  cases b <;> cases n <;> simp [eligible]

theorem no_eligible_iff (xs : List Cell) :
    hasEligible xs = false ↔ ∀ x ∈ xs, x = (false, 0) := by
  induction xs with
  | nil => simp [hasEligible]
  | cons x xs ih =>
    simp [hasEligible, inactive_is_zero, ih]

theorem fixed_iff_all_zero (xs : List Cell) :
    cancel xs = xs ↔ ∀ x ∈ xs, x = (false, 0) := by
  rw [cancel_fixed, no_eligible_iff]

theorem cancel_weight_nine (xs : List Cell) :
    9 * weight 1 (cancel xs) = 9 * weight 1 xs := by
  rw [cancel_weight]

#print axioms toggle_involution
#print axioms cancel_involution
#print axioms cancel_weight
#print axioms cancel_parity
#print axioms cancel_fixed
#print axioms fixed_iff_all_zero
#print axioms cancel_weight_nine
end KR1Cancellation
