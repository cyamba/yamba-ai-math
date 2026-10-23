/-
Copyright (c) 2026 Christopher Yamba. All rights reserved.

Completeness of Parikh matrices for words in which the inner letters occur at most twice.
Words are lists of natural-number letters over the ordered alphabet 0 < 1 < 2 < ⋯.
`E w j m` is the Parikh-matrix entry |w|_{j(j+1)⋯(j+m-1)}: the number of occurrences of the
run of `m` consecutive letters starting at `j`, as a scattered subword.
-/

namespace ParikhCompleteness

/-- The number of embeddings of `pat` as a scattered subword of `w`. -/
def occ : List Nat → List Nat → Nat
  | _, [] => 1
  | [], _ :: _ => 0
  | x :: xs, a :: pat => occ xs (a :: pat) + if x = a then occ xs pat else 0

theorem occ_cons_cons (x : Nat) (xs : List Nat) (a : Nat) (pat : List Nat) :
    occ (x :: xs) (a :: pat) = occ xs (a :: pat) + if x = a then occ xs pat else 0 := rfl

/-- The run `j, j+1, …, j+m-1`. -/
def run (j m : Nat) : List Nat := List.range' j m

/-- `E w j m = |w|_{j(j+1)⋯(j+m-1)}`. -/
def E (w : List Nat) (j m : Nat) : Nat := occ w (run j m)

theorem run_succ (j m : Nat) : run j (m + 1) = j :: run (j + 1) m := by
  simp [run, List.range'_succ]

@[simp] theorem E_zero (w : List Nat) (j : Nat) : E w j 0 = 1 := by
  cases w <;> simp [E, run, occ]

@[simp] theorem E_nil (j m : Nat) : E [] j (m + 1) = 0 := by
  simp [E, run_succ, occ]

/-- Prepending a letter: the recursion behind the Parikh matrix morphism. -/
theorem E_cons (x : Nat) (xs : List Nat) (j m : Nat) :
    E (x :: xs) j (m + 1) = E xs j (m + 1) + if x = j then E xs (j + 1) m else 0 := by
  simp only [E, run_succ, occ]

theorem occ_le_cons (x : Nat) (xs pat : List Nat) : occ xs pat ≤ occ (x :: xs) pat := by
  cases pat with
  | nil => simp [occ]
  | cons a pat => rw [occ_cons_cons]; omega

/-- A pattern whose first letter does not occur has no occurrence. -/
theorem occ_head_absent (w : List Nat) (a : Nat) (rest : List Nat) (h : occ w [a] = 0) :
    occ w (a :: rest) = 0 := by
  induction w with
  | nil => simp [occ]
  | cons x xs ih =>
      have h' : occ xs [a] = 0 := by
        have := occ_le_cons x xs [a]; omega
      rw [occ_cons_cons] at h ⊢
      by_cases hx : x = a
      · rw [ite_eq_left hx] at h; simp [occ] at h
      · rw [ite_eq_right hx, ih h']

/-- If no `e` precedes an `e+1`, every run through the edge `e` has no occurrence. -/
theorem E_edge_absent (e : Nat) (w : List Nat) (h : occ w [e, e + 1] = 0) :
    ∀ j a c, j + a = e → E w j (a + c + 2) = 0 := by
  induction w with
  | nil => intro j a c _; exact E_nil j (a + c + 1)
  | cons x xs ih =>
      intro j a c hj
      have h' : occ xs [e, e + 1] = 0 := by
        have := occ_le_cons x xs [e, e + 1]; omega
      have hc : E (x :: xs) j (a + c + 2) = E xs j (a + c + 2) +
          if x = j then E xs (j + 1) (a + c + 1) else 0 := E_cons x xs j (a + c + 1)
      rw [hc, ih h' j a c hj]
      by_cases hx : x = j
      · rw [ite_eq_left hx]
        cases a with
        | zero =>
            have hb : occ xs [e + 1] = 0 := by
              rw [occ_cons_cons, ite_eq_left (by omega)] at h; omega
            have hrun : E xs (j + 1) (0 + c + 1) = occ xs ((e + 1) :: run (e + 2) c) := by
              rw [show 0 + c + 1 = c + 1 by omega]
              simp only [E, run_succ, show j + 1 = e + 1 by omega]
            rw [hrun, occ_head_absent xs (e + 1) _ hb]
        | succ a =>
            have := ih h' (j + 1) a c (by omega)
            rw [show a + 1 + c + 1 = a + c + 2 by omega, this]
      · rw [ite_eq_right hx]

/-- The auxiliary identity: if no `e` lies between two `(e+1)`s, every `(e+1)` follows the
same occurrences of `j⋯e`. -/
theorem single_block (e : Nat) (w : List Nat) (h : occ w [e + 1, e, e + 1] = 0) :
    ∀ j a b, j + a = e →
      E w j (a + b + 2) * E w (e + 1) 1 = E w j (a + 2) * E w (e + 1) (b + 1) := by
  induction w with
  | nil => intro j a b _; simp
  | cons x xs ih =>
      intro j a b hj
      have h' : occ xs [e + 1, e, e + 1] = 0 := by
        have := occ_le_cons x xs [e + 1, e, e + 1]; omega
      have IH := ih h'
      have hA : E (x :: xs) j (a + b + 2) = E xs j (a + b + 2) +
          if x = j then E xs (j + 1) (a + b + 1) else 0 := E_cons x xs j (a + b + 1)
      have hC : E (x :: xs) j (a + 2) = E xs j (a + 2) +
          if x = j then E xs (j + 1) (a + 1) else 0 := E_cons x xs j (a + 1)
      have hN : E (x :: xs) (e + 1) 1 = E xs (e + 1) 1 +
          if x = e + 1 then E xs (e + 2) 0 else 0 := E_cons x xs (e + 1) 0
      have hD : E (x :: xs) (e + 1) (b + 1) = E xs (e + 1) (b + 1) +
          if x = e + 1 then E xs (e + 2) b else 0 := E_cons x xs (e + 1) b
      rw [hA, hC, hN, hD]
      have h0 := IH j a b hj
      by_cases hxj : x = j
      · rw [ite_eq_left hxj, ite_eq_left hxj, ite_eq_right (by omega), ite_eq_right (by omega)]
        simp only [Nat.add_zero]
        cases a with
        | zero =>
            have hje : j = e := by omega
            subst hje
            rw [show 0 + b + 1 = b + 1 by omega, show 0 + 1 = 1 by omega]
            rw [Nat.add_mul, Nat.add_mul, h0, Nat.mul_comm (E xs (j + 1) (b + 1))]
        | succ a =>
            have h1 := IH (j + 1) a b (by omega)
            rw [show a + b + 2 = a + 1 + b + 1 by omega, show a + 2 = a + 1 + 1 by omega] at h1
            rw [Nat.add_mul, Nat.add_mul, h0, h1]
      · rw [ite_eq_right hxj, ite_eq_right hxj]
        simp only [Nat.add_zero]
        by_cases hxe : x = e + 1
        · rw [ite_eq_left hxe, ite_eq_left hxe]
          have hab : occ xs [e, e + 1] = 0 := by
            rw [occ_cons_cons, ite_eq_left hxe] at h; omega
          rw [E_edge_absent e xs hab j a b hj,
            show a + 2 = a + 0 + 2 by omega, E_edge_absent e xs hab j a 0 hj]
          simp
        · rw [ite_eq_right hxe, ite_eq_right hxe]
          simpa using h0

/-- **Rectangle rule.** If `w` has no scattered subword `e (e+1) e (e+1)`, then for every
window `j ≤ e < e+1 ≤ l` the long entry factorises across the edge `e`:
`|w|_{j⋯l} · |w|_{e(e+1)} = |w|_{j⋯(e+1)} · |w|_{e⋯l}`. Here `l = e + 1 + b`. -/
theorem rectangle (e : Nat) (w : List Nat) (h : occ w [e, e + 1, e, e + 1] = 0) :
    ∀ j a b, j + a = e →
      E w j (a + b + 2) * E w e 2 = E w j (a + 2) * E w e (b + 2) := by
  induction w with
  | nil => intro j a b _; simp [show (2 : Nat) = 1 + 1 from rfl]
  | cons x xs ih =>
      intro j a b hj
      cases a with
      | zero =>
          have hje : j = e := by omega
          subst hje
          rw [show 0 + b + 2 = b + 2 by omega, show 0 + 2 = 2 by omega, Nat.mul_comm]
      | succ a =>
          have h' : occ xs [e, e + 1, e, e + 1] = 0 := by
            have := occ_le_cons x xs [e, e + 1, e, e + 1]; omega
          have IH := ih h'
          have hA : E (x :: xs) j (a + 1 + b + 2) = E xs j (a + 1 + b + 2) +
              if x = j then E xs (j + 1) (a + 1 + b + 1) else 0 := E_cons x xs j (a + 1 + b + 1)
          have hC : E (x :: xs) j (a + 1 + 2) = E xs j (a + 1 + 2) +
              if x = j then E xs (j + 1) (a + 1 + 1) else 0 := E_cons x xs j (a + 1 + 1)
          have hX : E (x :: xs) e 2 = E xs e 2 +
              if x = e then E xs (e + 1) 1 else 0 := E_cons x xs e 1
          have hD : E (x :: xs) e (b + 2) = E xs e (b + 2) +
              if x = e then E xs (e + 1) (b + 1) else 0 := E_cons x xs e (b + 1)
          rw [hA, hC, hX, hD]
          have h0 := IH j (a + 1) b hj
          by_cases hxj : x = j
          · rw [ite_eq_left hxj, ite_eq_left hxj, ite_eq_right (by omega), ite_eq_right (by omega)]
            simp only [Nat.add_zero]
            have h1 := IH (j + 1) a b (by omega)
            rw [show a + b + 2 = a + 1 + b + 1 by omega, show a + 2 = a + 1 + 1 by omega] at h1
            rw [Nat.add_mul, Nat.add_mul, h0, h1]
          · rw [ite_eq_right hxj, ite_eq_right hxj]
            simp only [Nat.add_zero]
            by_cases hxe : x = e
            · rw [ite_eq_left hxe, ite_eq_left hxe]
              have hb : occ xs [e + 1, e, e + 1] = 0 := by
                rw [occ_cons_cons, ite_eq_left hxe] at h; omega
              have hs := single_block e xs hb j (a + 1) b hj
              rw [Nat.mul_add, Nat.mul_add, h0, hs]
            · rw [ite_eq_right hxe, ite_eq_right hxe]
              simpa using h0


/-! ## Splitting a word at the first copy of a letter -/

/-- The part of `w` before the first `a` (all of `w` if there is none). -/
def before (a : Nat) : List Nat → List Nat
  | [] => []
  | x :: xs => if x = a then [] else x :: before a xs

/-- The part of `w` after the first `a` (empty if there is none). -/
def after (a : Nat) : List Nat → List Nat
  | [] => []
  | x :: xs => if x = a then xs else after a xs

theorem occ_nil_pat (w : List Nat) : occ w [] = 1 := by cases w <;> rfl

theorem occ_single_cons (x : Nat) (xs : List Nat) (b : Nat) :
    occ (x :: xs) [b] = occ xs [b] + if x = b then 1 else 0 := by
  rw [occ_cons_cons, occ_nil_pat]

@[simp] theorem occ_nil_cons (a : Nat) (p : List Nat) : occ [] (a :: p) = 0 := rfl

theorem before_cons_eq (a : Nat) (xs : List Nat) : before a (a :: xs) = [] := by simp [before]
theorem after_cons_eq (a : Nat) (xs : List Nat) : after a (a :: xs) = xs := by simp [after]
theorem before_cons_ne (a x : Nat) (xs : List Nat) (h : x ≠ a) :
    before a (x :: xs) = x :: before a xs := by simp [before, h]
theorem after_cons_ne (a x : Nat) (xs : List Nat) (h : x ≠ a) :
    after a (x :: xs) = after a xs := by simp [after, h]

/-- Counting a letter `b ≠ a` on both sides of the first `a`. -/
theorem count_split (a b : Nat) (hab : b ≠ a) (w : List Nat) :
    occ w [b] = occ (before a w) [b] + occ (after a w) [b] := by
  induction w with
  | nil => rfl
  | cons x xs ih =>
      by_cases hx : x = a
      · subst hx
        rw [before_cons_eq, after_cons_eq, occ_single_cons, ite_eq_right (Ne.symm hab)]
        simp
      · rw [before_cons_ne a x xs hx, after_cons_ne a x xs hx, occ_single_cons,
          occ_single_cons, ih]
        omega

/-- The copies of `a` after the first one. -/
theorem count_after_self (a : Nat) (w : List Nat) (h : occ w [a] ≠ 0) :
    occ w [a] = occ (after a w) [a] + 1 := by
  induction w with
  | nil => simp at h
  | cons x xs ih =>
      by_cases hx : x = a
      · subst hx; rw [after_cons_eq, occ_single_cons, ite_eq_left rfl]
      · rw [after_cons_ne a x xs hx, occ_single_cons, ite_eq_right hx] at *
        exact ih (by simpa using h)

/-- A pattern containing a letter that does not occur has no occurrence. -/
theorem occ_absent_mem (a : Nat) (w : List Nat) (h : occ w [a] = 0) :
    ∀ pat, a ∈ pat → occ w pat = 0 := by
  induction w with
  | nil => intro pat hp; cases pat with
    | nil => simp at hp
    | cons c p => rfl
  | cons x xs ih =>
      intro pat hp
      have hxa : x ≠ a := by
        intro hxa; rw [occ_single_cons, ite_eq_left hxa] at h; omega
      have h' : occ xs [a] = 0 := by rw [occ_single_cons, ite_eq_right hxa] at h; simpa using h
      cases pat with
      | nil => simp at hp
      | cons c p =>
          rw [occ_cons_cons, ih h' _ hp]
          by_cases hxc : x = c
          · rw [ite_eq_left hxc]
            have hp' : a ∈ p := by
              rcases List.mem_cons.mp hp with hac | hp'
              · exact absurd (hxc.trans hac.symm) hxa
              · exact hp'
            rw [ih h' p hp']
          · rw [ite_eq_right hxc]

/-- **First-letter split (G1).** -/
theorem occ_first (a : Nat) (q w : List Nat) (h : occ w [a] ≠ 0) :
    occ w (a :: q) = occ (after a w) q + occ (after a w) (a :: q) := by
  induction w with
  | nil => simp at h
  | cons x xs ih =>
      by_cases hx : x = a
      · subst hx; rw [after_cons_eq, occ_cons_cons, ite_eq_left rfl]; omega
      · rw [after_cons_ne a x xs hx, occ_cons_cons, ite_eq_right hx, Nat.add_zero]
        rw [occ_single_cons, ite_eq_right hx, Nat.add_zero] at h
        exact ih h

/-- **Second-letter split (G2).** For `j ≠ a`, an occurrence of `j a q` either uses a `j`
before the first `a`, or lies entirely after the first `a`. -/
theorem occ_second (j a : Nat) (hja : j ≠ a) (q w : List Nat) :
    occ w (j :: a :: q) =
      occ (before a w) [j] * occ w (a :: q) + occ (after a w) (j :: a :: q) := by
  induction w with
  | nil => simp [before, after]
  | cons x xs ih =>
      by_cases hx : x = a
      · subst hx
        rw [before_cons_eq, after_cons_eq, occ_cons_cons, ite_eq_right (Ne.symm hja)]
        simp [occ]
      · rw [before_cons_ne a x xs hx, after_cons_ne a x xs hx, occ_cons_cons, ih,
          occ_single_cons, occ_cons_cons x xs a q, ite_eq_right hx, Nat.add_zero]
        by_cases hxj : x = j
        · rw [ite_eq_left hxj, ite_eq_left hxj, Nat.add_mul]; omega
        · rw [ite_eq_right hxj, ite_eq_right hxj]; simp

/-- Skipping: if no `b` precedes the first `a`, the first `b` after the first `a` is the
first `b`. -/
theorem after_after_skip (a b : Nat) (hab : b ≠ a) (w : List Nat)
    (hb : occ (before a w) [b] = 0) (ha : occ w [a] ≠ 0) :
    after b (after a w) = after b w := by
  induction w with
  | nil => simp at ha
  | cons x xs ih =>
      by_cases hx : x = a
      · subst hx; rw [after_cons_eq, after_cons_ne b x xs (Ne.symm hab)]
      · rw [before_cons_ne a x xs hx, occ_single_cons] at hb
        have hxb : x ≠ b := by intro h; rw [ite_eq_left h] at hb; omega
        rw [ite_eq_right hxb, Nat.add_zero] at hb
        rw [occ_single_cons, ite_eq_right hx, Nat.add_zero] at ha
        rw [after_cons_ne a x xs hx, after_cons_ne b x xs hxb]
        exact ih hb ha

/-- If exactly one `b` precedes the first `a`, the first `b` after the first `a` is the
second `b`. -/
theorem after_after_one (a b : Nat) (hab : b ≠ a) (w : List Nat)
    (hb : occ (before a w) [b] = 1) (ha : occ w [a] ≠ 0) :
    after b (after a w) = after b (after b w) := by
  induction w with
  | nil => simp [before] at hb
  | cons x xs ih =>
      by_cases hx : x = a
      · subst hx; rw [before_cons_eq] at hb; simp at hb
      · rw [occ_single_cons, ite_eq_right hx, Nat.add_zero] at ha
        rw [before_cons_ne a x xs hx, occ_single_cons] at hb
        rw [after_cons_ne a x xs hx]
        by_cases hxb : x = b
        · subst hxb
          rw [ite_eq_left rfl] at hb
          rw [after_cons_eq]
          exact after_after_skip a x hab xs (by omega) ha
        · rw [ite_eq_right hxb] at hb
          rw [after_cons_ne b x xs hxb]
          exact ih (by simpa using hb) ha

/-- **Middle split.** If `a` occurs exactly once and not in `p`, every occurrence of
`p a q` passes through that copy. -/
theorem occ_mid (a : Nat) (q : List Nat) :
    ∀ (p w : List Nat), a ∉ p → occ w [a] = 1 →
      occ w (p ++ a :: q) = occ (before a w) p * occ (after a w) q := by
  intro p w
  induction w generalizing p with
  | nil => intro _ h; simp at h
  | cons x xs ih =>
      intro hp h
      by_cases hx : x = a
      · subst hx
        rw [occ_single_cons, ite_eq_left rfl] at h
        have h0 : occ xs [x] = 0 := by omega
        rw [before_cons_eq, after_cons_eq]
        cases p with
        | nil =>
            rw [List.nil_append, occ_cons_cons, ite_eq_left rfl, occ_head_absent xs x q h0,
              occ_nil_pat]
            simp
        | cons c p =>
            have hcx : c ≠ x := fun hc => hp (hc ▸ List.mem_cons_self)
            rw [List.cons_append, occ_cons_cons, ite_eq_right (Ne.symm hcx),
              occ_absent_mem x xs h0 _ (by simp)]
            simp
      · rw [occ_single_cons, ite_eq_right hx, Nat.add_zero] at h
        rw [before_cons_ne a x xs hx, after_cons_ne a x xs hx]
        cases p with
        | nil =>
            have h1 := ih [] (by simp) h
            rw [List.nil_append, occ_nil_pat] at h1
            rw [List.nil_append, occ_cons_cons, ite_eq_right hx, Nat.add_zero, occ_nil_pat, h1]
        | cons c p =>
            have hp' : a ∉ p := fun hm => hp (List.mem_cons_of_mem c hm)
            have h1 := ih (c :: p) hp h
            rw [List.cons_append] at h1
            rw [List.cons_append, occ_cons_cons, occ_cons_cons x (before a xs), h1]
            by_cases hxc : x = c
            · rw [ite_eq_left hxc, ite_eq_left hxc, ih p hp' h, Nat.add_mul]
            · rw [ite_eq_right hxc, ite_eq_right hxc]; simp


/-! ## Small windows -/

theorem E_one (w : List Nat) (k : Nat) : E w k 1 = occ w [k] := by simp [E, run, List.range']
theorem E_two (w : List Nat) (k : Nat) : E w k 2 = occ w [k, k + 1] := by
  simp [E, run, List.range']
theorem E_three (w : List Nat) (k : Nat) : E w k 3 = occ w [k, k + 1, k + 2] := by
  simp [E, run, List.range']

/-! ## Crossings -/

/-- The edge `k` is a **crossing**: `k` and `k+1` occur twice each and interleave as
`k (k+1) k (k+1)`, i.e. exactly three of the four pairs are in order. -/
def crossing (w : List Nat) (k : Nat) : Prop :=
  occ w [k] = 2 ∧ occ w [k + 1] = 2 ∧ occ w [k, k + 1] = 3

/-- The positions forced by a crossing `a b a b` (with `b = a+1`): no `b` before the first
`a`, one `b` between the two `a`s, one `b` after the second `a`. -/
theorem crossing_pos (w : List Nat) (a : Nat) (hc : crossing w a) :
    occ (before a w) [a + 1] = 0 ∧ occ (before a (after a w)) [a + 1] = 1 ∧
    occ (after a (after a w)) [a + 1] = 1 ∧ occ (after a w) [a] = 1 ∧
    occ (after a (after a w)) [a] = 0 := by
  obtain ⟨ha, hb, hab⟩ := hc
  have hne : a + 1 ≠ a := by omega
  have h1 := count_after_self a w (by omega)
  have h2 := count_after_self a (after a w) (by omega)
  have s1 := count_split a (a + 1) hne w
  have s2 := count_split a (a + 1) hne (after a w)
  have f1 := occ_first a [a + 1] w (by omega)
  have f2 := occ_first a [a + 1] (after a w) (by omega)
  have z0 : occ (after a (after a w)) [a, a + 1] = 0 :=
    occ_head_absent _ a [a + 1] (by omega)
  refine ⟨by omega, by omega, by omega, by omega, by omega⟩

/-- `R1 w i t` counts the occurrences of `(i+1)⋯(i+t+1)` after the first `i`; `R2` after the
second `i`. They are the two coordinates of the transfer vector at the letter `i`. -/
def R1 (w : List Nat) (i t : Nat) : Nat := occ (after i w) (run (i + 1) (t + 1))
def R2 (w : List Nat) (i t : Nat) : Nat := occ (after i (after i w)) (run (i + 1) (t + 1))

/-- **Crossing chain.** Along a chain of crossings, the transfer vector is multiplied by
`[[1,1],[0,1]]` at each step. -/
theorem chain (w : List Nat) : ∀ t i, (∀ k, i ≤ k → k < i + t → crossing w k) →
    R1 w i t = R1 w (i + t) 0 + t * R2 w (i + t) 0 ∧ R2 w i t = R2 w (i + t) 0 := by
  intro t
  induction t with
  | zero => intro i _; simp
  | succ t ih =>
      intro i hc
      have IH := ih (i + 1) (fun k h1 h2 => hc k (by omega) (by omega))
      rw [show i + 1 + t = i + (t + 1) by omega] at IH
      obtain ⟨IH1, IH2⟩ := IH
      have hci := hc i (by omega) (by omega)
      obtain ⟨pu, pv, pz, pa1, pa2⟩ := crossing_pos w i hci
      obtain ⟨ha, hb, _⟩ := hci
      have hne : i + 1 ≠ i := by omega
      have skip := after_after_skip i (i + 1) hne w pu (by omega)
      have s1 := count_split i (i + 1) hne w
      have c1 := count_after_self (i + 1) w (by omega)
      have c2 := count_after_self (i + 1) (after (i + 1) w) (by omega)
      have hz : after (i + 1) (after i (after i w)) = after (i + 1) (after (i + 1) w) := by
        rw [after_after_one i (i + 1) hne (after i w) pv (by omega), skip]
      have hq : ∀ v, occ v (run (i + 1) (t + 1 + 1)) =
          occ v ((i + 1) :: run (i + 1 + 1) (t + 1)) := fun v => by rw [run_succ]
      constructor
      · -- R1 i (t+1) = R1 (i+1) t + R2 (i+1) t
        have e1 := occ_first (i + 1) (run (i + 1 + 1) (t + 1)) (after i w) (by omega)
        have e2 := occ_first (i + 1) (run (i + 1 + 1) (t + 1)) (after (i + 1) w) (by omega)
        have e3 := occ_head_absent (after (i + 1) (after (i + 1) w)) (i + 1)
          (run (i + 1 + 1) (t + 1)) (by omega)
        have hR1 : R1 w i (t + 1) = R1 w (i + 1) t + R2 w (i + 1) t := by
          simp only [R1, R2]
          rw [hq, e1, skip, e2, e3]; omega
        rw [hR1, IH1, IH2, Nat.succ_mul]; omega
      · have e1 := occ_first (i + 1) (run (i + 1 + 1) (t + 1)) (after i (after i w)) (by omega)
        have e3 := occ_head_absent (after (i + 1) (after (i + 1) w)) (i + 1)
          (run (i + 1 + 1) (t + 1)) (by omega)
        have hR2 : R2 w i (t + 1) = R2 w (i + 1) t := by
          simp only [R2]
          rw [hq, e1, hz, e3]; omega
        rw [hR2, IH2]

/-- **Case (c): the crossing-chain formula.** If every inner edge of the window
`j, …, j+t+3` is a crossing, the window entry is a function of four short entries. -/
theorem crossing_formula (w : List Nat) (j t : Nat)
    (hc : ∀ k, j + 1 ≤ k → k ≤ j + t + 1 → crossing w k) :
    ∃ a1 b d1 d2 : Nat,
      E w j (t + 4) = a1 * (d1 + (t + 1) * d2 + d2) + b * d2 ∧
      E w j 2 = a1 * 2 + b ∧ E w j 3 = a1 * 3 + b ∧
      E w (j + t + 2) 2 = d1 + d2 ∧ E w (j + t + 1) 3 = (d1 + d2) + d2 := by
  have hja : j ≠ j + 1 := by omega
  have hc1 := hc (j + 1) (by omega) (by omega)
  obtain ⟨pu, pv, pz, pa1, pa2⟩ := crossing_pos w (j + 1) hc1
  obtain ⟨ha, _, hab⟩ := hc1
  -- the chain from the letter j+1 to the letter j+t+2
  obtain ⟨C1, C2⟩ := chain w (t + 1) (j + 1) (fun k h1 h2 => hc k h1 (by omega))
  rw [show j + 1 + (t + 1) = j + t + 2 by omega] at C1 C2
  -- the chain over the last edge, from j+t+1
  have hcl := hc (j + t + 1) (by omega) (by omega)
  obtain ⟨L1, L2⟩ := chain w 1 (j + t + 1) (fun k h1 h2 => by
    have : k = j + t + 1 := by omega
    subst this; exact hcl)
  rw [show j + t + 1 + 1 = j + t + 2 by omega] at L1 L2
  obtain ⟨_, hl2, _⟩ := hcl
  rw [show j + t + 1 + 1 = j + t + 2 by omega] at hl2
  refine ⟨occ (before (j + 1) w) [j], occ (before (j + 1) (after (j + 1) w)) [j],
    R1 w (j + t + 2) 0, R2 w (j + t + 2) 0, ?_, ?_, ?_, ?_, ?_⟩
  · -- the window entry
    have hE : E w j (t + 4) = occ w (j :: (j + 1) :: run (j + 1 + 1) (t + 2)) := by
      simp only [E]; rw [show t + 4 = t + 2 + 1 + 1 by omega, run_succ, run_succ]
    have g1 := occ_second j (j + 1) hja (run (j + 1 + 1) (t + 2)) w
    have g2 := occ_second j (j + 1) hja (run (j + 1 + 1) (t + 2)) (after (j + 1) w)
    have g3 := occ_absent_mem (j + 1) (after (j + 1) (after (j + 1) w)) (by omega)
      (j :: (j + 1) :: run (j + 1 + 1) (t + 2)) (by simp)
    have f1 := occ_first (j + 1) (run (j + 1 + 1) (t + 2)) w (by omega)
    have f2 := occ_first (j + 1) (run (j + 1 + 1) (t + 2)) (after (j + 1) w) (by omega)
    have f3 := occ_head_absent (after (j + 1) (after (j + 1) w)) (j + 1)
      (run (j + 1 + 1) (t + 2)) (by omega)
    have r1 : R1 w (j + 1) (t + 1) = occ (after (j + 1) w) (run (j + 1 + 1) (t + 2)) := rfl
    have r2 : R2 w (j + 1) (t + 1) =
        occ (after (j + 1) (after (j + 1) w)) (run (j + 1 + 1) (t + 2)) := rfl
    rw [hE, g1, g2, g3, f1, f2, f3, ← r1, ← r2, C1, C2]
    simp only [Nat.add_zero]
  · rw [E_two]
    have g1 := occ_second j (j + 1) hja [] w
    have g2 := occ_second j (j + 1) hja [] (after (j + 1) w)
    have g3 := occ_absent_mem (j + 1) (after (j + 1) (after (j + 1) w)) (by omega)
      [j, j + 1] (by simp)
    rw [g1, g2, g3, ha, pa1]; simp
  · rw [E_three]
    have g1 := occ_second j (j + 1) hja [j + 2] w
    have g2 := occ_second j (j + 1) hja [j + 2] (after (j + 1) w)
    have g3 := occ_absent_mem (j + 1) (after (j + 1) (after (j + 1) w)) (by omega)
      [j, j + 1, j + 2] (by simp)
    have f2 := occ_first (j + 1) [j + 1 + 1] (after (j + 1) w) (by omega)
    have f3 := occ_head_absent (after (j + 1) (after (j + 1) w)) (j + 1) [j + 1 + 1] (by omega)
    rw [g1, g2, g3, hab, f2, f3, pz]; simp
  · rw [E_two]
    have f1 := occ_first (j + t + 2) [j + t + 2 + 1] w (by omega)
    have f2 := occ_first (j + t + 2) [j + t + 2 + 1] (after (j + t + 2) w) (by
      have := count_after_self (j + t + 2) w (by omega); omega)
    have f3 := occ_head_absent (after (j + t + 2) (after (j + t + 2) w)) (j + t + 2)
      [j + t + 2 + 1] (by
        have h1 := count_after_self (j + t + 2) w (by omega)
        have h2 := count_after_self (j + t + 2) (after (j + t + 2) w) (by omega)
        omega)
    rw [f1, f2, f3]
    simp [R1, R2, run, List.range']
  · rw [E_three]
    have f1 := occ_first (j + t + 1) [j + t + 1 + 1, j + t + 1 + 2] w (by omega)
    have f2 := occ_first (j + t + 1) [j + t + 1 + 1, j + t + 1 + 2] (after (j + t + 1) w)
      (by have := count_after_self (j + t + 1) w (by omega); omega)
    have f3 := occ_head_absent (after (j + t + 1) (after (j + t + 1) w)) (j + t + 1)
      [j + t + 1 + 1, j + t + 1 + 2] (by
        have h1 := count_after_self (j + t + 1) w (by omega)
        have h2 := count_after_self (j + t + 1) (after (j + t + 1) w) (by omega)
        omega)
    have r1 : R1 w (j + t + 1) 1 =
        occ (after (j + t + 1) w) [j + t + 1 + 1, j + t + 1 + 2] := by
      simp [R1, run, List.range']
    have r2 : R2 w (j + t + 1) 1 =
        occ (after (j + t + 1) (after (j + t + 1) w)) [j + t + 1 + 1, j + t + 1 + 2] := by
      simp [R2, run, List.range']
    rw [f1, f2, f3, ← r1, ← r2, L1, L2]
    simp


/-- With at most two copies of `k` and of `k+1`, an edge that is not a crossing is a rectangle:
the word avoids `k (k+1) k (k+1)`. -/
theorem avoid_of_not_crossing (w : List Nat) (k : Nat) (ha : occ w [k] ≤ 2)
    (hb : occ w [k + 1] ≤ 2) (hnc : ¬ crossing w k) : occ w [k, k + 1, k, k + 1] = 0 := by
  apply Classical.byContradiction
  intro hne
  apply hnc
  have hne' : occ w [k] ≠ 0 := by
    intro h0; exact hne (occ_head_absent w k _ h0)
  have hk1 : k + 1 ≠ k := by omega
  have c1 := count_after_self k w hne'
  have f1 := occ_first k [k + 1, k, k + 1] w hne'
  -- no third copy of k, so the second split leaves nothing
  have hrest : occ (after k w) [k, k + 1, k, k + 1] = 0 := by
    by_cases h1 : occ (after k w) [k] = 0
    · exact occ_head_absent _ k _ h1
    · have c2 := count_after_self k (after k w) h1
      have f2 := occ_first k [k + 1, k, k + 1] (after k w) h1
      have z0 : occ (after k (after k w)) [k] = 0 := by omega
      rw [f2, occ_absent_mem k _ z0 [k + 1, k, k + 1] (by simp),
        occ_absent_mem k _ z0 [k, k + 1, k, k + 1] (by simp)]
  rw [f1, hrest, Nat.add_zero] at hne
  have h1 : occ (after k w) [k] = 1 := by
    have : occ (after k w) [k] ≠ 0 := by
      intro h0; exact hne (occ_absent_mem k _ h0 [k + 1, k, k + 1] (by simp))
    omega
  have hmid := occ_mid k [k + 1] [k + 1] (after k w) (by simp) h1
  simp only [List.cons_append, List.nil_append] at hmid
  rw [hmid, Nat.mul_eq_zero] at hne
  have s1 := count_split k (k + 1) hk1 w
  have s2 := count_split k (k + 1) hk1 (after k w)
  have c2 := count_after_self k (after k w) (by omega)
  have g1 := occ_first k [k + 1] w hne'
  have g2 := occ_first k [k + 1] (after k w) (by omega)
  have g3 := occ_head_absent (after k (after k w)) k [k + 1] (by omega)
  refine ⟨by omega, by omega, by omega⟩

/-! ## The completeness theorem -/

/-- **Completeness for doubled letters.** Consider the window of letters `j, …, j+t+3` (at
least four letters). If every inner letter occurs at most twice in `w`, then the window entry
is determined by the shorter entries of the window: any `w'` that agrees with `w` on all of
them agrees on the window entry too. -/
theorem complete_two (w w' : List Nat) (j t : Nat)
    (hmult : ∀ k, j < k → k < j + t + 3 → occ w [k] ≤ 2)
    (hsame : ∀ i r, j ≤ i → i + r ≤ j + t + 4 → r < t + 4 → E w i r = E w' i r) :
    E w j (t + 4) = E w' j (t + 4) := by
  have cnt : ∀ k, j ≤ k → k + 1 ≤ j + t + 4 → occ w [k] = occ w' [k] := by
    intro k h1 h2; rw [← E_one, ← E_one]; exact hsame k 1 h1 h2 (by omega)
  have pair : ∀ k, j ≤ k → k + 2 ≤ j + t + 4 → occ w [k, k + 1] = occ w' [k, k + 1] := by
    intro k h1 h2; rw [← E_two, ← E_two]; exact hsame k 2 h1 h2 (by omega)
  have hiff : ∀ k, j + 1 ≤ k → k ≤ j + t + 1 → (crossing w k ↔ crossing w' k) := by
    intro k h1 h2
    unfold crossing
    rw [cnt k (by omega) (by omega), cnt (k + 1) (by omega) (by omega),
      pair k (by omega) (by omega)]
  by_cases hall : ∀ k, j + 1 ≤ k → k ≤ j + t + 1 → crossing w k
  · -- case (c): every inner edge is a crossing, for `w` and for `w'`
    have hall' : ∀ k, j + 1 ≤ k → k ≤ j + t + 1 → crossing w' k :=
      fun k h1 h2 => (hiff k h1 h2).mp (hall k h1 h2)
    obtain ⟨a1, b, d1, d2, F, X, Y, X', Y'⟩ := crossing_formula w j t hall
    obtain ⟨a1', b', d1', d2', F', Xp, Yp, Xp', Yp'⟩ := crossing_formula w' j t hall'
    have eX := hsame j 2 (by omega) (by omega) (by omega)
    have eY := hsame j 3 (by omega) (by omega) (by omega)
    have eX' := hsame (j + t + 2) 2 (by omega) (by omega) (by omega)
    have eY' := hsame (j + t + 1) 3 (by omega) (by omega) (by omega)
    have ha : a1 = a1' := by omega
    have hb : b = b' := by omega
    have hd1 : d1 = d1' := by omega
    have hd2 : d2 = d2' := by omega
    rw [F, F', ha, hb, hd1, hd2]
  · -- cases (a), (b): some inner edge is a rectangle
    have hex : ∃ k, j + 1 ≤ k ∧ k ≤ j + t + 1 ∧ ¬ crossing w k := by
      apply Classical.byContradiction
      intro hne; apply hall; intro k h1 h2
      apply Classical.byContradiction; intro hc; exact hne ⟨k, h1, h2, hc⟩
    obtain ⟨k, hk1, hk2, hnc⟩ := hex
    have hnc' : ¬ crossing w' k := fun h => hnc ((hiff k hk1 hk2).mpr h)
    have hka := hmult k (by omega) (by omega)
    have hkb := hmult (k + 1) (by omega) (by omega)
    have av := avoid_of_not_crossing w k hka hkb hnc
    have av' := avoid_of_not_crossing w' k (by rw [← cnt k (by omega) (by omega)]; exact hka)
      (by rw [← cnt (k + 1) (by omega) (by omega)]; exact hkb) hnc'
    obtain ⟨s, rfl⟩ : ∃ s, k = j + 1 + s := ⟨k - j - 1, by omega⟩
    obtain ⟨c, rfl⟩ : ∃ c, t = s + c := ⟨t - s, by omega⟩
    have ht : s + 1 + (c + 1) + 2 = s + c + 4 := by omega
    have R := rectangle (j + 1 + s) w av j (s + 1) (c + 1) (by omega)
    have R' := rectangle (j + 1 + s) w' av' j (s + 1) (c + 1) (by omega)
    rw [ht] at R R'
    have ex := hsame (j + 1 + s) 2 (by omega) (by omega) (by omega)
    have eA := hsame j (s + 1 + 2) (by omega) (by omega) (by omega)
    have eD := hsame (j + 1 + s) (c + 1 + 2) (by omega) (by omega) (by omega)
    by_cases hx : E w (j + 1 + s) 2 = 0
    · -- case (a): the edge is empty, so is the window
      rw [E_two] at hx
      have hx' : occ w' [j + 1 + s, j + 1 + s + 1] = 0 := by
        rw [← E_two, ← ex, E_two]; exact hx
      have z := E_edge_absent (j + 1 + s) w hx j (s + 1) (c + 1) (by omega)
      have z' := E_edge_absent (j + 1 + s) w' hx' j (s + 1) (c + 1) (by omega)
      rw [ht] at z z'
      rw [z, z']
    · -- case (b): the rectangle rule divides out the edge
      apply Nat.eq_of_mul_eq_mul_right (Nat.pos_of_ne_zero hx)
      rw [R, ex, R', eA, eD]

/-- **Corollary (diagonals 2–4 suffice).** In the window of letters `lo, …, hi`, if every
letter strictly between `lo` and `hi` occurs at most twice in `w`, and `w'` agrees with `w` on
every entry of length at most 3 inside the window, then `w` and `w'` agree on every entry
inside the window. For a word whose inner letters occur at most twice, the Parikh matrix is
determined by its first four diagonals. -/
theorem determined_by_short (w w' : List Nat) (lo hi : Nat)
    (hmult : ∀ k, lo < k → k < hi → occ w [k] ≤ 2)
    (hshort : ∀ i r, lo ≤ i → i + r ≤ hi + 1 → r ≤ 3 → E w i r = E w' i r) :
    ∀ r i, lo ≤ i → i + r ≤ hi + 1 → E w i r = E w' i r := by
  intro r
  induction r using Nat.strongRecOn with
  | ind r ih =>
      intro i hi1 hi2
      by_cases hr : r ≤ 3
      · exact hshort i r hi1 hi2 hr
      · obtain ⟨t, rfl⟩ : ∃ t, r = t + 4 := ⟨r - 4, by omega⟩
        apply complete_two w w' i t
        · intro k h1 h2; exact hmult k (by omega) (by omega)
        · intro i' r' h1 h2 h3; exact ih r' h3 i' (by omega) (by omega)


/-! ## Sharpness certificates (checked by evaluation in the kernel) -/

/-- The fourth diagonal is needed: `21332` and `32123` (content `(1,2,2)`) have the same letter
and pair counts but `|w|₁₂₃ = 0` and `1`. -/
theorem sharp_fourth_diagonal :
    (∀ i, i < 4 → ∀ r, r < 3 → 1 ≤ i → i + r ≤ 4 →
      E [2, 1, 3, 3, 2] i r = E [3, 2, 1, 2, 3] i r) ∧
    E [2, 1, 3, 3, 2] 1 3 = 0 ∧ E [3, 2, 1, 2, 3] 1 3 = 1 := by
  decide

/-- "Twice" cannot be raised to "three times": `2343212443` and `3221443234` (content
`(1,3,3,3)`) agree on every entry of length at most 3 but `|w|₁₂₃₄ = 0` and `1`. -/
theorem sharp_three_copies :
    (∀ i, i < 5 → ∀ r, r < 4 → 1 ≤ i → i + r ≤ 5 →
      E [2, 3, 4, 3, 2, 1, 2, 4, 4, 3] i r = E [3, 2, 2, 1, 4, 4, 3, 2, 3, 4] i r) ∧
    E [2, 3, 4, 3, 2, 1, 2, 4, 4, 3] 1 4 = 0 ∧ E [3, 2, 2, 1, 4, 4, 3, 2, 3, 4] 1 4 = 1 := by
  decide


/-- The sharpness family at `n = 3` (content `(1,3,3,3)`, letters `0..3`): the two Parikh
matrices differ only in the corner `|w|₀₁₂₃`. -/
theorem family_three :
    (∀ i, i < 4 → ∀ r, r < 4 → i + r ≤ 4 →
      E [2, 1, 1, 0, 3, 3, 2, 1, 2, 3] i r = E [1, 2, 3, 2, 1, 0, 1, 3, 3, 2] i r) ∧
    E [2, 1, 1, 0, 3, 3, 2, 1, 2, 3] 0 4 = 1 ∧ E [1, 2, 3, 2, 1, 0, 1, 3, 3, 2] 0 4 = 0 := by
  decide

/-- The sharpness family at `n = 4` (content `(1,4,4,4,4)`, letters `0..4`). -/
theorem family_four :
    (∀ i, i < 5 → ∀ r, r < 5 → i + r ≤ 5 →
      E [2, 1, 1, 3, 4, 3, 2, 1, 0, 2, 1, 4, 4, 3, 2, 3, 4] i r =
        E [1, 2, 3, 2, 1, 1, 0, 4, 3, 4, 3, 2, 1, 2, 4, 4, 3] i r) ∧
    E [2, 1, 1, 3, 4, 3, 2, 1, 0, 2, 1, 4, 4, 3, 2, 3, 4] 0 5 = 1 ∧
    E [1, 2, 3, 2, 1, 1, 0, 4, 3, 4, 3, 2, 1, 2, 4, 4, 3] 0 5 = 0 := by
  decide

end ParikhCompleteness
