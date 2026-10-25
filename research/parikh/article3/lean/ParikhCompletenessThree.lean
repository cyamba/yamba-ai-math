/-
Copyright (c) 2026 Christopher Yamba. All rights reserved.

Completeness of Parikh matrices for words in which the inner letters occur at most three times
(Conjecture C of Article 3 at n = 3), by the pivot-letter method of `notes/proof-c3.md`.
Same conventions as `ParikhCompleteness.lean`: words are lists of natural numbers and
`E w j m = |w|_{j(j+1)⋯(j+m-1)}`.
-/
import ParikhCompleteness

namespace ParikhCompleteness

/-! ## Deleting, inserting and appending letters -/

/-- Deleting a copy of a letter that does not occur in the pattern changes nothing. -/
theorem occ_delete (c : Nat) : ∀ (q : List Nat), c ∉ q →
    ∀ x y : List Nat, occ (x ++ c :: y) q = occ (x ++ y) q := by
  intro q hq x y
  induction x generalizing q with
  | nil =>
      cases q with
      | nil => simp [occ_nil_pat]
      | cons b q' =>
          have hcb : c ≠ b := fun h => hq (h ▸ List.mem_cons_self)
          simp [occ_cons_cons, hcb]
  | cons z x ih =>
      cases q with
      | nil => simp [occ_nil_pat]
      | cons b q' =>
          have hq' : c ∉ q' := fun h => hq (List.mem_cons_of_mem b h)
          simp only [List.cons_append, occ_cons_cons]
          rw [ih (b :: q') hq, ih q' hq']

/-- **Insertion.** Inserting a copy of `c` adds exactly the occurrences of `p ++ c :: q` that
pass through it, when `c` occurs in neither `p` nor `q`. -/
theorem occ_insert (c : Nat) (q : List Nat) (hq : c ∉ q) : ∀ (p x y : List Nat), c ∉ p →
    occ (x ++ c :: y) (p ++ c :: q) = occ (x ++ y) (p ++ c :: q) + occ x p * occ y q := by
  intro p x y hp
  induction x generalizing p with
  | nil =>
      cases p with
      | nil => simp [occ_cons_cons, occ_nil_pat]
      | cons a p' =>
          have hca : c ≠ a := fun h => hp (h ▸ List.mem_cons_self)
          simp [occ_cons_cons, hca]
  | cons z x ih =>
      cases p with
      | nil =>
          have h1 := ih [] (by simp)
          have h2 := occ_delete c q hq x y
          simp only [List.nil_append, List.cons_append, occ_cons_cons, occ_nil_pat] at h1 h2 ⊢
          rw [h1, h2]
          by_cases hzc : z = c <;> simp [hzc] <;> omega
      | cons a p' =>
          have hp' : c ∉ p' := fun h => hp (List.mem_cons_of_mem a h)
          have h1 := ih (a :: p') hp
          have h2 := ih p' hp'
          simp only [List.cons_append, occ_cons_cons] at h1 h2 ⊢
          rw [h1, h2]
          by_cases hza : z = a <;> simp [hza, Nat.add_mul] <;> omega

/-- Appending letters that avoid the last letter of the pattern changes nothing. -/
theorem occ_append_last (d : Nat) (y : List Nat) (hy : occ y [d] = 0) :
    ∀ (p x : List Nat), occ (x ++ y) (p ++ [d]) = occ x (p ++ [d]) := by
  intro p x
  induction x generalizing p with
  | nil =>
      rw [List.nil_append, occ_absent_mem d y hy _ (by simp)]
      cases p <;> rfl
  | cons z x ih =>
      cases p with
      | nil =>
          have h1 := ih []
          simp only [List.nil_append, List.cons_append, occ_cons_cons, occ_nil_pat] at h1 ⊢
          rw [h1]
      | cons a p' =>
          have h1 := ih (a :: p')
          have h2 := ih p'
          simp only [List.cons_append, occ_cons_cons] at h1 h2 ⊢
          rw [h1, h2]

/-- Prepending letters that avoid the first letter of the pattern changes nothing. -/
theorem occ_prepend_first (d : Nat) (q : List Nat) :
    ∀ x y : List Nat, occ x [d] = 0 → occ (x ++ y) (d :: q) = occ y (d :: q) := by
  intro x y hx
  induction x with
  | nil => rfl
  | cons z x ih =>
      rw [occ_single_cons] at hx
      have hzd : z ≠ d := by intro h; rw [ite_eq_left h] at hx; omega
      rw [ite_eq_right hzd] at hx
      rw [List.cons_append, occ_cons_cons, ite_eq_right hzd, Nat.add_zero]
      exact ih (by omega)

theorem occ_single_append (d : Nat) (x y : List Nat) :
    occ (x ++ y) [d] = occ x [d] + occ y [d] := by
  induction x with
  | nil => simp [occ]
  | cons z x ih =>
      rw [List.cons_append, occ_single_cons, occ_single_cons, ih]; omega

theorem occ_single_insert (c d : Nat) (hcd : c ≠ d) (x y : List Nat) :
    occ (x ++ c :: y) [d] = occ x [d] + occ y [d] := by
  rw [occ_delete c [d] (by simpa using hcd), occ_single_append]

/-! ## Runs -/

theorem run_split (i a b : Nat) : run i (a + 1 + b) = run i a ++ (i + a) :: run (i + a + 1) b := by
  have h := @List.range'_append i (a + 1) b 1
  simp only [Nat.one_mul] at h
  rw [run, ← h, List.range'_concat]
  simp [run, Nat.one_mul, Nat.add_assoc]

theorem run_last (i a : Nat) : run i (a + 1) = run i a ++ [i + a] := by
  simp [run, List.range'_concat]

theorem mem_run (x i n : Nat) : x ∈ run i n ↔ i ≤ x ∧ x < i + n := List.mem_range'_1

/-! ## Splitting at the first copy -/

theorem split_first (c : Nat) : ∀ w : List Nat, occ w [c] ≠ 0 → w = before c w ++ c :: after c w := by
  intro w h
  induction w with
  | nil => simp at h
  | cons x xs ih =>
      by_cases hx : x = c
      · subst hx; simp [before, after]
      · rw [occ_single_cons, ite_eq_right hx, Nat.add_zero] at h
        rw [before_cons_ne c x xs hx, after_cons_ne c x xs hx, List.cons_append, ← ih h]

theorem before_free (c : Nat) : ∀ w : List Nat, occ (before c w) [c] = 0 := by
  intro w
  induction w with
  | nil => rfl
  | cons x xs ih =>
      by_cases hx : x = c
      · subst hx; simp [before]
      · rw [before_cons_ne c x xs hx, occ_single_cons, ite_eq_right hx, ih]

/-! ## The pivot decomposition (Lemma 2.1 of the note) -/

section pivot
variable (c : Nat) (p q : List Nat) (hp : c ∉ p) (hq : c ∉ q)
include hp hq

theorem pivot_one (u0 u1 : List Nat) (h0 : occ u0 [c] = 0) (h1 : occ u1 [c] = 0) :
    occ (u0 ++ c :: u1) (p ++ c :: q) = occ u0 p * occ u1 q := by
  rw [occ_insert c q hq p u0 u1 hp,
    occ_absent_mem c (u0 ++ u1) (by rw [occ_single_append, h0, h1]) _ (by simp)]
  simp

theorem pivot_two (u0 u1 u2 : List Nat) (h0 : occ u0 [c] = 0) (h1 : occ u1 [c] = 0)
    (h2 : occ u2 [c] = 0) :
    occ (u0 ++ c :: (u1 ++ c :: u2)) (p ++ c :: q) =
      occ u0 p * occ (u1 ++ c :: u2) q + occ (u0 ++ u1) p * occ u2 q := by
  rw [occ_insert c q hq p u0 _ hp, ← List.append_assoc,
    pivot_one c p q hp hq (u0 ++ u1) u2 (by rw [occ_single_append, h0, h1]) h2]
  omega

theorem pivot_three (u0 u1 u2 u3 : List Nat) (h0 : occ u0 [c] = 0) (h1 : occ u1 [c] = 0)
    (h2 : occ u2 [c] = 0) (h3 : occ u3 [c] = 0) :
    occ (u0 ++ c :: (u1 ++ c :: (u2 ++ c :: u3))) (p ++ c :: q) =
      occ u0 p * occ (u1 ++ c :: (u2 ++ c :: u3)) q + occ (u0 ++ u1) p * occ (u2 ++ c :: u3) q
        + occ (u0 ++ u1 ++ u2) p * occ u3 q := by
  rw [occ_insert c q hq p u0 _ hp, ← List.append_assoc,
    pivot_two c p q hp hq (u0 ++ u1) u2 u3 (by rw [occ_single_append, h0, h1]) h2 h3]
  omega

end pivot

/-! ## Words with one, two or three copies of a letter -/

theorem decomp_one (c : Nat) (w : List Nat) (h : occ w [c] = 1) :
    ∃ u0 u1, w = u0 ++ c :: u1 ∧ occ u0 [c] = 0 ∧ occ u1 [c] = 0 := by
  have ha := count_after_self c w (by omega)
  exact ⟨before c w, after c w, split_first c w (by omega), before_free c w, by omega⟩

theorem decomp_two (c : Nat) (w : List Nat) (h : occ w [c] = 2) :
    ∃ u0 u1 u2, w = u0 ++ c :: (u1 ++ c :: u2) ∧ occ u0 [c] = 0 ∧ occ u1 [c] = 0 ∧
      occ u2 [c] = 0 := by
  have ha := count_after_self c w (by omega)
  obtain ⟨u1, u2, hA, h1, h2⟩ := decomp_one c (after c w) (by omega)
  refine ⟨before c w, u1, u2, ?_, before_free c w, h1, h2⟩
  rw [← hA]; exact split_first c w (by omega)

theorem decomp_three (c : Nat) (w : List Nat) (h : occ w [c] = 3) :
    ∃ u0 u1 u2 u3, w = u0 ++ c :: (u1 ++ c :: (u2 ++ c :: u3)) ∧ occ u0 [c] = 0 ∧
      occ u1 [c] = 0 ∧ occ u2 [c] = 0 ∧ occ u3 [c] = 0 := by
  have ha := count_after_self c w (by omega)
  obtain ⟨u1, u2, u3, hA, h1, h2, h3⟩ := decomp_two c (after c w) (by omega)
  refine ⟨before c w, u1, u2, u3, ?_, before_free c w, h1, h2, h3⟩
  rw [← hA]; exact split_first c w (by omega)

theorem decomp_zero_entry (c : Nat) (w : List Nat) (h : occ w [c] = 0) (P : List Nat)
    (hP : c ∈ P) : occ w P = 0 := occ_absent_mem c w h P hP

/-! ## The window and its pivot

The window is `j, …, j+s+u+4` (at least five letters) and the pivot is `m = j+s+2`, so
`j < m-1 < m < m+1 < j+s+u+4`. The left pattern `Pj` is `j ⋯ (m-1)` and the right pattern
`Ql` is `(m+1) ⋯ (j+s+u+4)`. -/

theorem entry_split (w : List Nat) (i a b : Nat) :
    E w i (a + 1 + b) = occ w (run i a ++ (i + a) :: run (i + a + 1) b) := by
  rw [E, run_split]

theorem pivot_entries (w : List Nat) (j s u : Nat) :
    E w j (s + 3) = occ w (run j (s + 2) ++ (j + s + 2) :: []) ∧
    E w j (s + 4) = occ w (run j (s + 2) ++ (j + s + 2) :: [j + s + 3]) ∧
    E w j (s + u + 5) = occ w (run j (s + 2) ++ (j + s + 2) :: run (j + s + 3) (u + 2)) ∧
    E w (j + s + 1) 2 = occ w ([j + s + 1] ++ (j + s + 2) :: []) ∧
    E w (j + s + 1) 3 = occ w ([j + s + 1] ++ (j + s + 2) :: [j + s + 3]) ∧
    E w (j + s + 1) (u + 4) = occ w ([j + s + 1] ++ (j + s + 2) :: run (j + s + 3) (u + 2)) ∧
    E w (j + s + 2) 1 = occ w ([] ++ (j + s + 2) :: []) ∧
    E w (j + s + 2) 2 = occ w ([] ++ (j + s + 2) :: [j + s + 3]) ∧
    E w (j + s + 2) (u + 3) = occ w ([] ++ (j + s + 2) :: run (j + s + 3) (u + 2)) := by
  have hl : ∀ i a b n, n = a + 1 + b → E w i n = occ w (run i a ++ (i + a) :: run (i + a + 1) b) :=
    fun i a b n hn => hn ▸ entry_split w i a b
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_⟩
  · rw [hl j (s + 2) 0 (s + 3) (by omega)]; simp [run, Nat.add_assoc]
  · rw [hl j (s + 2) 1 (s + 4) (by omega)]; simp [run, Nat.add_assoc]
  · rw [hl j (s + 2) (u + 2) (s + u + 5) (by omega)]; simp [Nat.add_assoc]
  · rw [hl (j + s + 1) 1 0 2 (by omega)]; simp [run, Nat.add_assoc]
  · rw [hl (j + s + 1) 1 1 3 (by omega)]; simp [run, Nat.add_assoc]
  · rw [hl (j + s + 1) 1 (u + 2) (u + 4) (by omega)]; simp [run, Nat.add_assoc]
  · rw [hl (j + s + 2) 0 0 1 (by omega)]; simp [run]
  · rw [hl (j + s + 2) 0 1 2 (by omega)]; simp [run, Nat.add_assoc]
  · rw [hl (j + s + 2) 0 (u + 2) (u + 3) (by omega)]; simp [run, Nat.add_assoc]

theorem not_mem_left (j s : Nat) : (j + s + 2) ∉ run j (s + 2) := by
  rw [mem_run]; omega

theorem not_mem_right (j s u : Nat) : (j + s + 2) ∉ run (j + s + 3) (u + 2) := by
  rw [mem_run]; omega

theorem left_last (j s : Nat) : run j (s + 2) = run j (s + 1) ++ [j + s + 1] := by
  rw [run_last]; simp [Nat.add_assoc]

theorem right_first (j s u : Nat) : run (j + s + 3) (u + 2) = (j + s + 3) :: run (j + s + 4) (u + 1) := by
  rw [run_succ]

/-! ## Copy data at the pivot (Lemma 2.2 of the note) -/

/-- The copy data of `w` at the pivot `m = j+s+2` when `m` occurs three times. For the `r`-th
copy, `F r` and `a r` count `j⋯(m-1)` and `m-1` before it, and `b r` and `G r` count `m+1` and
`(m+1)⋯(j+s+u+4)` after it. -/
structure Copies3 (w : List Nat) (j s u : Nat) where
  (F1 F2 F3 a1 a2 a3 b1 b2 b3 G1 G2 G3 : Nat)
  e_jm : E w j (s + 3) = F1 + F2 + F3
  e_jm1 : E w j (s + 4) = F1 * b1 + F2 * b2 + F3 * b3
  e_jl : E w j (s + u + 5) = F1 * G1 + F2 * G2 + F3 * G3
  e_am : E w (j + s + 1) 2 = a1 + a2 + a3
  e_am1 : E w (j + s + 1) 3 = a1 * b1 + a2 * b2 + a3 * b3
  e_al : E w (j + s + 1) (u + 4) = a1 * G1 + a2 * G2 + a3 * G3
  e_mm1 : E w (j + s + 2) 2 = b1 + b2 + b3
  e_ml : E w (j + s + 2) (u + 3) = G1 + G2 + G3
  a12 : a1 ≤ a2
  a23 : a2 ≤ a3
  a3n : a3 ≤ E w (j + s + 1) 1
  b21 : b2 ≤ b1
  b32 : b3 ≤ b2
  b1n : b1 ≤ E w (j + s + 3) 1
  F12 : a1 = a2 → F1 = F2
  F23 : a2 = a3 → F2 = F3
  G12 : b1 = b2 → G1 = G2
  G23 : b2 = b3 → G2 = G3
  F1z : a1 = 0 → F1 = 0
  F3t : a3 = E w (j + s + 1) 1 → F3 = E w j (s + 2)
  G3z : b3 = 0 → G3 = 0
  G1t : b1 = E w (j + s + 3) 1 → G1 = E w (j + s + 3) (u + 2)

theorem copies3 (w : List Nat) (j s u : Nat) (h : occ w [j + s + 2] = 3) :
    Nonempty (Copies3 w j s u) := by
  obtain ⟨u0, u1, u2, u3, hw, h0, h1, h2, h3⟩ := decomp_three (j + s + 2) w h
  obtain ⟨e1, e2, e3, e4, e5, e6, _, e8, e9⟩ := pivot_entries w j s u
  have nl := not_mem_left j s
  have nr := not_mem_right j s u
  have P3 := fun (p q : List Nat) (hp : (j + s + 2) ∉ p) (hq : (j + s + 2) ∉ q) =>
    pivot_three (j + s + 2) p q hp hq u0 u1 u2 u3 h0 h1 h2 h3
  have hcd : j + s + 2 ≠ j + s + 1 := by omega
  have hce : j + s + 2 ≠ j + s + 3 := by omega
  have ndm : (j + s + 2) ∉ [j + s + 1] := by simp
  have nem : (j + s + 2) ∉ [j + s + 3] := by simp
  have dmem : (j + s + 1) ∈ run j (s + 2) := by rw [mem_run]; omega
  have emem : (j + s + 3) ∈ run (j + s + 3) (u + 2) := by rw [mem_run]; omega
  -- single-letter counts of the pieces
  have cd : ∀ x y : List Nat, occ (x ++ (j + s + 2) :: y) [j + s + 1] = occ x [j + s + 1] + occ y [j + s + 1] :=
    occ_single_insert _ _ hcd
  have ce : ∀ x y : List Nat, occ (x ++ (j + s + 2) :: y) [j + s + 3] = occ x [j + s + 3] + occ y [j + s + 3] :=
    occ_single_insert _ _ hce
  have sa := occ_single_append (j + s + 1)
  have sb := occ_single_append (j + s + 3)
  -- deleting the copies of the pivot from the left pattern
  have del := occ_delete (j + s + 2) (run j (s + 2)) nl
  have wPj : occ w (run j (s + 2)) = occ (u0 ++ u1 ++ u2 ++ u3) (run j (s + 2)) := by
    rw [hw, del, ← List.append_assoc, del, ← List.append_assoc, del]
  -- prepending pieces that avoid `m+1`
  have pre : ∀ x y : List Nat, occ x [j + s + 3] = 0 →
      occ (x ++ (j + s + 2) :: y) (run (j + s + 3) (u + 2)) = occ y (run (j + s + 3) (u + 2)) := by
    intro x y hx
    rw [right_first, show x ++ (j + s + 2) :: y = (x ++ [j + s + 2]) ++ y by simp]
    exact occ_prepend_first _ _ _ _ (by rw [occ_single_append, hx]; simp [occ])
  -- appending pieces that avoid `m-1`
  have app : ∀ x y : List Nat, occ y [j + s + 1] = 0 →
      occ (x ++ y) (run j (s + 2)) = occ x (run j (s + 2)) := by
    intro x y hy; rw [left_last]; exact occ_append_last _ y hy _ x
  refine ⟨⟨occ u0 (run j (s + 2)), occ (u0 ++ u1) (run j (s + 2)),
      occ (u0 ++ u1 ++ u2) (run j (s + 2)),
      occ u0 [j + s + 1], occ (u0 ++ u1) [j + s + 1], occ (u0 ++ u1 ++ u2) [j + s + 1],
      occ (u1 ++ (j + s + 2) :: (u2 ++ (j + s + 2) :: u3)) [j + s + 3],
      occ (u2 ++ (j + s + 2) :: u3) [j + s + 3], occ u3 [j + s + 3],
      occ (u1 ++ (j + s + 2) :: (u2 ++ (j + s + 2) :: u3)) (run (j + s + 3) (u + 2)),
      occ (u2 ++ (j + s + 2) :: u3) (run (j + s + 3) (u + 2)), occ u3 (run (j + s + 3) (u + 2)),
      ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_⟩⟩
  · rw [e1, hw, P3 _ _ nl (by simp)]; simp [occ_nil_pat]
  · rw [e2, hw, P3 _ _ nl nem]
  · rw [e3, hw, P3 _ _ nl nr]
  · rw [e4, hw, P3 _ _ ndm (by simp)]; simp [occ_nil_pat]
  · rw [e5, hw, P3 _ _ ndm nem]
  · rw [e6, hw, P3 _ _ ndm nr]
  · rw [e8, hw, P3 _ _ (by simp) nem]; simp [occ_nil_pat]
  · rw [e9, hw, P3 _ _ (by simp) nr]; simp [occ_nil_pat]
  · rw [sa]; omega
  · rw [sa (u0 ++ u1)]; omega
  · rw [E_one, hw, cd, cd, cd, sa, sa]; omega
  · rw [ce u1]; omega
  · rw [ce u2]; omega
  · rw [E_one, hw, ce u0]; omega
  · intro hab; rw [sa] at hab; rw [app u0 u1 (by omega)]
  · intro hab; rw [sa (u0 ++ u1)] at hab; rw [app (u0 ++ u1) u2 (by omega)]
  · intro hab; rw [ce] at hab; rw [pre u1 _ (by omega)]
  · intro hab; rw [ce] at hab; rw [pre u2 _ (by omega)]
  · intro ha; exact occ_absent_mem _ u0 ha _ dmem
  · intro ha
    rw [E_one, hw, cd, cd, cd, sa, sa] at ha
    rw [E, wPj, app (u0 ++ u1 ++ u2) u3 (by omega)]
  · intro hb; exact occ_absent_mem _ u3 hb _ emem
  · intro hb
    rw [E_one, hw, ce u0] at hb
    rw [E, hw, pre u0 _ (by omega)]

/-- The copy data when the pivot occurs twice. -/
structure Copies2 (w : List Nat) (j s u : Nat) where
  (F1 F2 a1 a2 b1 b2 G1 G2 : Nat)
  e_jm : E w j (s + 3) = F1 + F2
  e_jm1 : E w j (s + 4) = F1 * b1 + F2 * b2
  e_jl : E w j (s + u + 5) = F1 * G1 + F2 * G2
  e_am : E w (j + s + 1) 2 = a1 + a2
  e_am1 : E w (j + s + 1) 3 = a1 * b1 + a2 * b2
  e_al : E w (j + s + 1) (u + 4) = a1 * G1 + a2 * G2
  e_mm1 : E w (j + s + 2) 2 = b1 + b2
  e_ml : E w (j + s + 2) (u + 3) = G1 + G2
  a12 : a1 ≤ a2
  b21 : b2 ≤ b1
  F12 : a1 = a2 → F1 = F2
  G12 : b1 = b2 → G1 = G2

theorem copies2 (w : List Nat) (j s u : Nat) (h : occ w [j + s + 2] = 2) :
    Nonempty (Copies2 w j s u) := by
  obtain ⟨u0, u1, u2, hw, h0, h1, h2⟩ := decomp_two (j + s + 2) w h
  obtain ⟨e1, e2, e3, e4, e5, e6, _, e8, e9⟩ := pivot_entries w j s u
  have nl := not_mem_left j s
  have nr := not_mem_right j s u
  have P2 := fun (p q : List Nat) (hp : (j + s + 2) ∉ p) (hq : (j + s + 2) ∉ q) =>
    pivot_two (j + s + 2) p q hp hq u0 u1 u2 h0 h1 h2
  have hce : j + s + 2 ≠ j + s + 3 := by omega
  have ndm : (j + s + 2) ∉ [j + s + 1] := by simp
  have nem : (j + s + 2) ∉ [j + s + 3] := by simp
  have ce : ∀ x y : List Nat, occ (x ++ (j + s + 2) :: y) [j + s + 3] = occ x [j + s + 3] + occ y [j + s + 3] :=
    occ_single_insert _ _ hce
  have sa := occ_single_append (j + s + 1)
  have pre : ∀ x y : List Nat, occ x [j + s + 3] = 0 →
      occ (x ++ (j + s + 2) :: y) (run (j + s + 3) (u + 2)) = occ y (run (j + s + 3) (u + 2)) := by
    intro x y hx
    rw [right_first, show x ++ (j + s + 2) :: y = (x ++ [j + s + 2]) ++ y by simp]
    exact occ_prepend_first _ _ _ _ (by rw [occ_single_append, hx]; simp [occ])
  have app : ∀ x y : List Nat, occ y [j + s + 1] = 0 →
      occ (x ++ y) (run j (s + 2)) = occ x (run j (s + 2)) := by
    intro x y hy; rw [left_last]; exact occ_append_last _ y hy _ x
  refine ⟨⟨occ u0 (run j (s + 2)), occ (u0 ++ u1) (run j (s + 2)),
      occ u0 [j + s + 1], occ (u0 ++ u1) [j + s + 1],
      occ (u1 ++ (j + s + 2) :: u2) [j + s + 3], occ u2 [j + s + 3],
      occ (u1 ++ (j + s + 2) :: u2) (run (j + s + 3) (u + 2)), occ u2 (run (j + s + 3) (u + 2)),
      ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_⟩⟩
  · rw [e1, hw, P2 _ _ nl (by simp)]; simp [occ_nil_pat]
  · rw [e2, hw, P2 _ _ nl nem]
  · rw [e3, hw, P2 _ _ nl nr]
  · rw [e4, hw, P2 _ _ ndm (by simp)]; simp [occ_nil_pat]
  · rw [e5, hw, P2 _ _ ndm nem]
  · rw [e6, hw, P2 _ _ ndm nr]
  · rw [e8, hw, P2 _ _ (by simp) nem]; simp [occ_nil_pat]
  · rw [e9, hw, P2 _ _ (by simp) nr]; simp [occ_nil_pat]
  · rw [sa]; omega
  · rw [ce u1]; omega
  · intro hab; rw [sa] at hab; rw [app u0 u1 (by omega)]
  · intro hab; rw [ce u1] at hab; rw [pre u1 _ (by omega)]

/-- One copy of the pivot: the cut rule. -/
theorem corner_one (w : List Nat) (j s u : Nat) (h : occ w [j + s + 2] = 1) :
    E w j (s + u + 5) = E w j (s + 3) * E w (j + s + 2) (u + 3) := by
  obtain ⟨u0, u1, hw, h0, h1⟩ := decomp_one (j + s + 2) w h
  obtain ⟨e1, _, e3, _, _, _, _, _, e9⟩ := pivot_entries w j s u
  have P1 := fun (p q : List Nat) (hp : (j + s + 2) ∉ p) (hq : (j + s + 2) ∉ q) =>
    pivot_one (j + s + 2) p q hp hq u0 u1 h0 h1
  rw [e3, e1, e9, hw, P1 _ _ (not_mem_left j s) (not_mem_right j s u),
    P1 _ _ (not_mem_left j s) (by simp), P1 _ _ (by simp) (not_mem_right j s u)]
  simp [occ_nil_pat]

/-- No copy of the pivot: the corner vanishes. -/
theorem corner_zero (w : List Nat) (j s u : Nat) (h : occ w [j + s + 2] = 0) :
    E w j (s + u + 5) = 0 := by
  unfold E; exact occ_absent_mem _ w h _ (by rw [mem_run]; omega)

/-! ## The rules (§3 of the note), over the integers -/

/-- The pivot minor of Lemma 3.2, expanded along its first row; `Ejl` is the corner. -/
def minorExp (Ejm Ejm1 Ejl Eam Eam1 Eal nm Emm1 Eml : Int) : Int :=
  Ejl * (Eam * Emm1 - Eam1 * nm) + Ejm * (Eam1 * Eml - Eal * Emm1) - Ejm1 * (Eam * Eml - Eal * nm)

/-- Rule 2 for two copies: the pivot minor vanishes. -/
theorem minor_two (w : List Nat) (j s u : Nat) (C : Copies2 w j s u) :
    minorExp (E w j (s + 3)) (E w j (s + 4)) (E w j (s + u + 5)) (E w (j + s + 1) 2)
      (E w (j + s + 1) 3) (E w (j + s + 1) (u + 4)) 2 (E w (j + s + 2) 2)
      (E w (j + s + 2) (u + 3)) = 0 := by
  cases C with
  | mk F1 F2 a1 a2 b1 b2 G1 G2 e1 e2 e3 e4 e5 e6 e8 e9 _ _ _ _ =>
      unfold minorExp
      rw [e1, e2, e3, e4, e5, e6, e8, e9]
      push_cast
      grind

/-- Rule 2 for three copies, when two copies see the same number of letters `m-1` before them
or of letters `m+1` after them. -/
theorem minor_three (w : List Nat) (j s u : Nat) (C : Copies3 w j s u)
    (hnr : C.a1 = C.a2 ∨ C.a2 = C.a3 ∨ C.b1 = C.b2 ∨ C.b2 = C.b3) :
    minorExp (E w j (s + 3)) (E w j (s + 4)) (E w j (s + u + 5)) (E w (j + s + 1) 2)
      (E w (j + s + 1) 3) (E w (j + s + 1) (u + 4)) 3 (E w (j + s + 2) 2)
      (E w (j + s + 2) (u + 3)) = 0 := by
  cases C with
  | mk F1 F2 F3 a1 a2 a3 b1 b2 b3 G1 G2 G3 e1 e2 e3 e4 e5 e6 e8 e9 _ _ _ _ _ _ hF12 hF23 hG12
      hG23 _ _ _ _ =>
      simp only at hnr
      unfold minorExp
      rw [e1, e2, e3, e4, e5, e6, e8, e9]
      push_cast
      rcases hnr with h | h | h | h
      · rw [h, hF12 h]; grind
      · rw [h, hF23 h]; grind
      · rw [h, hG12 h]; grind
      · rw [h, hG23 h]; grind

/-- Rule 1 for two copies (Lemma 3.1: `D = (a2 - a1)(b1 - b2)`). -/
theorem rule1_two (w : List Nat) (j s u : Nat) (C : Copies2 w j s u)
    (hD : E w (j + s + 1) 2 * E w (j + s + 2) 2 = 2 * E w (j + s + 1) 3) :
    2 * E w j (s + u + 5) = E w j (s + 3) * E w (j + s + 2) (u + 3) := by
  cases C with
  | mk F1 F2 a1 a2 b1 b2 G1 G2 e1 _ e3 e4 e5 _ e8 e9 ha hb hF hG =>
      rw [e4, e8, e5] at hD
      rw [e3, e1, e9]
      have hD' : (((a1 + a2) * (b1 + b2) : Nat) : Int) = ((2 * (a1 * b1 + a2 * b2) : Nat) : Int) := by
        rw [hD]
      push_cast at hD'
      have z : ((a2 : Int) - a1) * ((b1 : Int) - b2) = 0 := by grind
      rcases Int.mul_eq_zero.mp z with h | h
      · rw [hF (by omega)]; grind
      · rw [hG (by omega)]; grind

/-- Rule 1 for three copies (Lemma 3.1). -/
theorem rule1_three (w : List Nat) (j s u : Nat) (C : Copies3 w j s u)
    (hD : E w (j + s + 1) 2 * E w (j + s + 2) 2 = 3 * E w (j + s + 1) 3) :
    3 * E w j (s + u + 5) = E w j (s + 3) * E w (j + s + 2) (u + 3) := by
  cases C with
  | mk F1 F2 F3 a1 a2 a3 b1 b2 b3 G1 G2 G3 e1 _ e3 e4 e5 _ e8 e9 h12 h23 _ h21 h32 _ hF12 hF23
      hG12 hG23 _ _ _ _ =>
      rw [e4, e8, e5] at hD
      rw [e3, e1, e9]
      have hD' : (((a1 + a2 + a3) * (b1 + b2 + b3) : Nat) : Int) =
          ((3 * (a1 * b1 + a2 * b2 + a3 * b3) : Nat) : Int) := by rw [hD]
      push_cast at hD'
      have hsum : ((a2 : Int) - a1) * ((b1 : Int) - b2) + ((a3 : Int) - a1) * ((b1 : Int) - b3)
          + ((a3 : Int) - a2) * ((b2 : Int) - b3) = 0 := by grind
      have p1 : 0 ≤ ((a2 : Int) - a1) * ((b1 : Int) - b2) := Int.mul_nonneg (by omega) (by omega)
      have p2 : 0 ≤ ((a3 : Int) - a1) * ((b1 : Int) - b3) := Int.mul_nonneg (by omega) (by omega)
      have p3 : 0 ≤ ((a3 : Int) - a2) * ((b2 : Int) - b3) := Int.mul_nonneg (by omega) (by omega)
      have z1 : ((a2 : Int) - a1) * ((b1 : Int) - b2) = 0 := by omega
      have z2 : ((a3 : Int) - a1) * ((b1 : Int) - b3) = 0 := by omega
      have z3 : ((a3 : Int) - a2) * ((b2 : Int) - b3) = 0 := by omega
      have q1 : ((F1 : Int) - F2) * ((G1 : Int) - G2) = 0 := by
        rcases Int.mul_eq_zero.mp z1 with h | h
        · rw [hF12 (by omega)]; simp
        · rw [hG12 (by omega)]; simp
      have q2 : ((F1 : Int) - F3) * ((G1 : Int) - G3) = 0 := by
        rcases Int.mul_eq_zero.mp z2 with h | h
        · rw [hF12 (by omega), hF23 (by omega)]; simp
        · rw [hG12 (by omega), hG23 (by omega)]; simp
      have q3 : ((F2 : Int) - F3) * ((G2 : Int) - G3) = 0 := by
        rcases Int.mul_eq_zero.mp z3 with h | h
        · rw [hF23 (by omega)]; simp
        · rw [hG23 (by omega)]; simp
      have key : ((3 * (F1 * G1 + F2 * G2 + F3 * G3) : Nat) : Int) =
          (((F1 + F2 + F3) * (G1 + G2 + G3) : Nat) : Int) := by
        push_cast; grind
      exact_mod_cast key

/-! ## The chain lemma (Lemma 3.3 of the note), by evaluation in the kernel -/

/-- The signature `(Σ a, Σ b, Σ a b)` of a chain. -/
def sig3 (a1 a2 a3 b1 b2 b3 : Nat) : Nat × Nat × Nat :=
  (a1 + a2 + a3, b1 + b2 + b3, a1 * b1 + a2 * b2 + a3 * b3)

/-- The sixteen rigid chains `(a1, a2, a3, b1, b2, b3)` with values in `[0, 3]`. -/
def rigidChains : List (Nat × Nat × Nat × Nat × Nat × Nat) :=
  [(0,1,2,2,1,0), (0,1,2,3,1,0), (0,1,2,3,2,0), (0,1,2,3,2,1),
   (0,1,3,2,1,0), (0,1,3,3,1,0), (0,1,3,3,2,0), (0,1,3,3,2,1),
   (0,2,3,2,1,0), (0,2,3,3,1,0), (0,2,3,3,2,0), (0,2,3,3,2,1),
   (1,2,3,2,1,0), (1,2,3,3,1,0), (1,2,3,3,2,0), (1,2,3,3,2,1)]

def upTo3 : List Nat := [0, 1, 2, 3]

/-- Every chain with values in `[0, 3]` that has the signature of a rigid chain is that chain. -/
def chainCheck : Bool :=
  rigidChains.all fun c =>
    upTo3.all fun a1 => upTo3.all fun a2 => upTo3.all fun a3 =>
    upTo3.all fun b1 => upTo3.all fun b2 => upTo3.all fun b3 =>
      !(decide (a1 ≤ a2) && decide (a2 ≤ a3) && decide (b3 ≤ b2) && decide (b2 ≤ b1)) ||
      !(decide (sig3 a1 a2 a3 b1 b2 b3 = sig3 c.1 c.2.1 c.2.2.1 c.2.2.2.1 c.2.2.2.2.1 c.2.2.2.2.2)) ||
      decide ((a1, a2, a3, b1, b2, b3) = c)

theorem chainCheck_eq : chainCheck = true := by decide

/-- Every rigid chain with values in `[0, 3]` is one of the sixteen. -/
def rigidCheck : Bool :=
  upTo3.all fun a1 => upTo3.all fun a2 => upTo3.all fun a3 =>
  upTo3.all fun b1 => upTo3.all fun b2 => upTo3.all fun b3 =>
    !(decide (a1 < a2) && decide (a2 < a3) && decide (b3 < b2) && decide (b2 < b1)) ||
    decide ((a1, a2, a3, b1, b2, b3) ∈ rigidChains)

theorem rigidCheck_eq : rigidCheck = true := by decide

theorem rigidChains_strict : ∀ c ∈ rigidChains,
    c.1 < c.2.1 ∧ c.2.1 < c.2.2.1 ∧ c.2.2.1 ≤ 3 ∧ c.2.2.2.2.2 < c.2.2.2.2.1 ∧
      c.2.2.2.2.1 < c.2.2.2.1 ∧ c.2.2.2.1 ≤ 3 := by decide

theorem mem_upTo3 (x : Nat) (h : x ≤ 3) : x ∈ upTo3 := by
  simp only [upTo3, List.mem_cons, List.mem_nil_iff]; omega

/-- **Lemma 3.3 (chain lemma).** A chain with values in `[0, 3]` with the signature of a rigid
chain is that rigid chain. -/
theorem chain_lemma (c : Nat × Nat × Nat × Nat × Nat × Nat) (hc : c ∈ rigidChains)
    (a1 a2 a3 b1 b2 b3 : Nat) (h12 : a1 ≤ a2) (h23 : a2 ≤ a3) (h3 : a3 ≤ 3)
    (h32 : b3 ≤ b2) (h21 : b2 ≤ b1) (h1 : b1 ≤ 3)
    (hsig : sig3 a1 a2 a3 b1 b2 b3 = sig3 c.1 c.2.1 c.2.2.1 c.2.2.2.1 c.2.2.2.2.1 c.2.2.2.2.2) :
    (a1, a2, a3, b1, b2, b3) = c := by
  have h := chainCheck_eq
  simp only [chainCheck, List.all_eq_true] at h
  have := h c hc a1 (mem_upTo3 a1 (by omega)) a2 (mem_upTo3 a2 (by omega)) a3 (mem_upTo3 a3 h3)
    b1 (mem_upTo3 b1 h1) b2 (mem_upTo3 b2 (by omega)) b3 (mem_upTo3 b3 (by omega))
  simpa [h12, h23, h32, h21, hsig] using this

theorem rigid_mem (a1 a2 a3 b1 b2 b3 : Nat) (h12 : a1 < a2) (h23 : a2 < a3) (h3 : a3 ≤ 3)
    (h32 : b3 < b2) (h21 : b2 < b1) (h1 : b1 ≤ 3) : (a1, a2, a3, b1, b2, b3) ∈ rigidChains := by
  have h := rigidCheck_eq
  simp only [rigidCheck, List.all_eq_true] at h
  have := h a1 (mem_upTo3 a1 (by omega)) a2 (mem_upTo3 a2 (by omega)) a3 (mem_upTo3 a3 h3)
    b1 (mem_upTo3 b1 h1) b2 (mem_upTo3 b2 (by omega)) b3 (mem_upTo3 b3 (by omega))
  simpa [h12, h23, h32, h21] using this

/-! ## The rigid case (Lemma 3.4 of the note) -/

/-- The arithmetic of Lemma 3.4: for a rigid chain, the two linear systems with the same right
sides have the same solutions, so the two corners agree. -/
theorem rigid_arith (a1 a2 a3 b1 b2 b3 F1 F2 F3 F1' F2' F3' G1 G2 G3 G1' G2' G3' : Nat)
    (r12 : a1 < a2) (r23 : a2 < a3) (r3 : a3 ≤ 3) (r32 : b3 < b2) (r21 : b2 < b1) (r1 : b1 ≤ 3)
    (hS : F1 + F2 + F3 = F1' + F2' + F3')
    (hT : F1 * b1 + F2 * b2 + F3 * b3 = F1' * b1 + F2' * b2 + F3' * b3)
    (hU : G1 + G2 + G3 = G1' + G2' + G3')
    (hV : a1 * G1 + a2 * G2 + a3 * G3 = a1 * G1' + a2 * G2' + a3 * G3')
    (hF1 : a1 ≠ 0 ∨ (F1 = 0 ∧ F1' = 0)) (hF3 : a3 ≠ 3 ∨ F3 = F3')
    (hG3 : b3 ≠ 0 ∨ (G3 = 0 ∧ G3' = 0)) (hG1 : b1 ≠ 3 ∨ G1 = G1') :
    F1 * G1 + F2 * G2 + F3 * G3 = F1' * G1' + F2' * G2' + F3' * G3' := by
  have ha : (a1 = 0 ∧ a2 = 1 ∧ a3 = 2) ∨ (a1 = 0 ∧ a2 = 1 ∧ a3 = 3) ∨
      (a1 = 0 ∧ a2 = 2 ∧ a3 = 3) ∨ (a1 = 1 ∧ a2 = 2 ∧ a3 = 3) := by omega
  have hb : (b1 = 2 ∧ b2 = 1 ∧ b3 = 0) ∨ (b1 = 3 ∧ b2 = 1 ∧ b3 = 0) ∨
      (b1 = 3 ∧ b2 = 2 ∧ b3 = 0) ∨ (b1 = 3 ∧ b2 = 2 ∧ b3 = 1) := by omega
  rcases ha with ⟨rfl, rfl, rfl⟩ | ⟨rfl, rfl, rfl⟩ | ⟨rfl, rfl, rfl⟩ | ⟨rfl, rfl, rfl⟩ <;>
  rcases hb with ⟨rfl, rfl, rfl⟩ | ⟨rfl, rfl, rfl⟩ | ⟨rfl, rfl, rfl⟩ | ⟨rfl, rfl, rfl⟩
  all_goals
    have hF1e : F1 = F1' := by omega
    have hF2e : F2 = F2' := by omega
    have hF3e : F3 = F3' := by omega
    have hG1e : G1 = G1' := by omega
    have hG2e : G2 = G2' := by omega
    have hG3e : G3 = G3' := by omega
    rw [hF1e, hF2e, hF3e, hG1e, hG2e, hG3e]

/-- Two words with three copies of the pivot, the same rigid chain and the same shorter counts
have the same corner. -/
theorem rigid_three (w w' : List Nat) (j s u : Nat) (C : Copies3 w j s u) (C' : Copies3 w' j s u)
    (ha1 : C.a1 = C'.a1) (ha2 : C.a2 = C'.a2) (ha3 : C.a3 = C'.a3)
    (hb1 : C.b1 = C'.b1) (hb2 : C.b2 = C'.b2) (hb3 : C.b3 = C'.b3)
    (r12 : C.a1 < C.a2) (r23 : C.a2 < C.a3) (r3 : C.a3 ≤ 3)
    (r32 : C.b3 < C.b2) (r21 : C.b2 < C.b1) (r1 : C.b1 ≤ 3)
    (hna : E w (j + s + 1) 1 ≤ 3) (hnb : E w (j + s + 3) 1 ≤ 3)
    (s1 : E w j (s + 3) = E w' j (s + 3)) (s2 : E w j (s + 4) = E w' j (s + 4))
    (s6 : E w (j + s + 1) (u + 4) = E w' (j + s + 1) (u + 4))
    (s9 : E w (j + s + 2) (u + 3) = E w' (j + s + 2) (u + 3))
    (s10 : E w j (s + 2) = E w' j (s + 2))
    (s11 : E w (j + s + 3) (u + 2) = E w' (j + s + 3) (u + 2))
    (s12 : E w (j + s + 1) 1 = E w' (j + s + 1) 1) (s13 : E w (j + s + 3) 1 = E w' (j + s + 3) 1) :
    E w j (s + u + 5) = E w' j (s + u + 5) := by
  cases C with
  | mk F1 F2 F3 a1 a2 a3 b1 b2 b3 G1 G2 G3 e1 e2 e3 _ _ e6 _ e9 _ _ a3n _ _ b1n _ _ _ _ F1z F3t
      G3z G1t =>
  cases C' with
  | mk F1' F2' F3' a1' a2' a3' b1' b2' b3' G1' G2' G3' e1' e2' e3' _ _ e6' _ e9' _ _ a3n' _ _ b1n'
      _ _ _ _ F1z' F3t' G3z' G1t' =>
  simp only at ha1 ha2 ha3 hb1 hb2 hb3 r12 r23 r3 r32 r21 r1
  subst ha1 ha2 ha3 hb1 hb2 hb3
  rw [e3, e3']
  apply rigid_arith a1 a2 a3 b1 b2 b3 F1 F2 F3 F1' F2' F3' G1 G2 G3 G1' G2' G3'
    r12 r23 r3 r32 r21 r1
  · rw [← e1, ← e1', s1]
  · rw [← e2, ← e2', s2]
  · rw [← e9, ← e9', s9]
  · rw [← e6, ← e6', s6]
  · by_cases h : a1 = 0
    · exact Or.inr ⟨F1z h, F1z' h⟩
    · exact Or.inl h
  · by_cases h : a3 = 3
    · exact Or.inr (by rw [F3t (by omega), F3t' (by omega), s10])
    · exact Or.inl h
  · by_cases h : b3 = 0
    · exact Or.inr ⟨G3z h, G3z' h⟩
    · exact Or.inl h
  · by_cases h : b1 = 3
    · exact Or.inr (by rw [G1t (by omega), G1t' (by omega), s11])
    · exact Or.inl h

/-! ## The pivot theorem (Theorem 4.1 of the note) -/

theorem cancel_minor (D K X X' : Int) (hD : D ≠ 0) (h : X * D + K = 0) (h' : X' * D + K = 0) :
    X = X' := by
  have e1 : X * D = D * X := Int.mul_comm X D
  have e2 : X' * D = D * X' := Int.mul_comm X' D
  exact Int.eq_of_mul_eq_mul_left hD (by omega)

theorem minor_split (Ejm Ejm1 Ejl Eam Eam1 Eal nm Emm1 Eml : Int) :
    minorExp Ejm Ejm1 Ejl Eam Eam1 Eal nm Emm1 Eml =
      Ejl * (Eam * Emm1 - Eam1 * nm) +
        (Ejm * (Eam1 * Eml - Eal * Emm1) - Ejm1 * (Eam * Eml - Eal * nm)) := by
  unfold minorExp; omega

/-- **Theorem 4.1 (pivot theorem).** In the window `j, …, j+s+u+4` (at least five letters), with
pivot `m = j+s+2`: if `m` occurs at most twice, or `m-1`, `m` and `m+1` occur at most three times
each, the window entry is determined by the shorter entries of the window. -/
theorem pivot_theorem (w w' : List Nat) (j s u : Nat)
    (hmult : occ w [j + s + 2] ≤ 2 ∨
      (occ w [j + s + 1] ≤ 3 ∧ occ w [j + s + 2] ≤ 3 ∧ occ w [j + s + 3] ≤ 3))
    (hsame : ∀ i r, j ≤ i → i + r ≤ j + s + u + 5 → r < s + u + 5 → E w i r = E w' i r) :
    E w j (s + u + 5) = E w' j (s + u + 5) := by
  have s1 := hsame j (s + 3) (by omega) (by omega) (by omega)
  have s2 := hsame j (s + 4) (by omega) (by omega) (by omega)
  have s4 := hsame (j + s + 1) 2 (by omega) (by omega) (by omega)
  have s5 := hsame (j + s + 1) 3 (by omega) (by omega) (by omega)
  have s6 := hsame (j + s + 1) (u + 4) (by omega) (by omega) (by omega)
  have s7 := hsame (j + s + 2) 1 (by omega) (by omega) (by omega)
  have s8 := hsame (j + s + 2) 2 (by omega) (by omega) (by omega)
  have s9 := hsame (j + s + 2) (u + 3) (by omega) (by omega) (by omega)
  have s10 := hsame j (s + 2) (by omega) (by omega) (by omega)
  have s11 := hsame (j + s + 3) (u + 2) (by omega) (by omega) (by omega)
  have s12 := hsame (j + s + 1) 1 (by omega) (by omega) (by omega)
  have s13 := hsame (j + s + 3) 1 (by omega) (by omega) (by omega)
  have n7 := s7
  rw [E_one, E_one] at n7
  -- Rule 2: when `D ≠ 0`, the vanishing pivot minor fixes the corner
  have via_minor : ∀ nm : Nat,
      ¬ (E w (j + s + 1) 2 * E w (j + s + 2) 2 = nm * E w (j + s + 1) 3) →
      minorExp (E w j (s + 3)) (E w j (s + 4)) (E w j (s + u + 5)) (E w (j + s + 1) 2)
        (E w (j + s + 1) 3) (E w (j + s + 1) (u + 4)) nm (E w (j + s + 2) 2)
        (E w (j + s + 2) (u + 3)) = 0 →
      minorExp (E w' j (s + 3)) (E w' j (s + 4)) (E w' j (s + u + 5)) (E w' (j + s + 1) 2)
        (E w' (j + s + 1) 3) (E w' (j + s + 1) (u + 4)) nm (E w' (j + s + 2) 2)
        (E w' (j + s + 2) (u + 3)) = 0 →
      E w j (s + u + 5) = E w' j (s + u + 5) := by
    intro nm hD m m'
    rw [← s1, ← s2, ← s4, ← s5, ← s6, ← s8, ← s9, minor_split] at m'
    rw [minor_split] at m
    have hD' : ((E w (j + s + 1) 2 : Int) * E w (j + s + 2) 2 - E w (j + s + 1) 3 * nm) ≠ 0 := by
      intro h; apply hD
      have : ((E w (j + s + 1) 2 * E w (j + s + 2) 2 : Nat) : Int) =
          ((nm * E w (j + s + 1) 3 : Nat) : Int) := by
        push_cast; rw [Int.mul_comm (nm : Int)]; omega
      exact_mod_cast this
    exact_mod_cast cancel_minor _ _ _ _ hD' m m'
  rcases (show occ w [j + s + 2] = 0 ∨ occ w [j + s + 2] = 1 ∨ occ w [j + s + 2] = 2 ∨
      occ w [j + s + 2] = 3 by omega) with h0 | h1 | h2 | h3
  · rw [corner_zero w j s u h0, corner_zero w' j s u (by omega)]
  · rw [corner_one w j s u h1, corner_one w' j s u (by omega), s1, s9]
  · obtain ⟨C⟩ := copies2 w j s u h2
    obtain ⟨C'⟩ := copies2 w' j s u (by omega)
    by_cases hD : E w (j + s + 1) 2 * E w (j + s + 2) 2 = 2 * E w (j + s + 1) 3
    · have r := rule1_two w j s u C hD
      have r' := rule1_two w' j s u C' (by rw [← s4, ← s8, ← s5]; exact hD)
      rw [← s1, ← s9] at r'
      omega
    · exact via_minor 2 hD (minor_two w j s u C) (minor_two w' j s u C')
  · have hb : occ w [j + s + 1] ≤ 3 ∧ occ w [j + s + 3] ≤ 3 := by omega
    have hna : E w (j + s + 1) 1 ≤ 3 := by rw [E_one]; exact hb.1
    have hnb : E w (j + s + 3) 1 ≤ 3 := by rw [E_one]; exact hb.2
    obtain ⟨C⟩ := copies3 w j s u h3
    obtain ⟨C'⟩ := copies3 w' j s u (by omega)
    by_cases hD : E w (j + s + 1) 2 * E w (j + s + 2) 2 = 3 * E w (j + s + 1) 3
    · have r := rule1_three w j s u C hD
      have r' := rule1_three w' j s u C' (by rw [← s4, ← s8, ← s5]; exact hD)
      rw [← s1, ← s9] at r'
      omega
    · by_cases hR : ∃ c ∈ rigidChains,
          sig3 c.1 c.2.1 c.2.2.1 c.2.2.2.1 c.2.2.2.2.1 c.2.2.2.2.2 =
            (E w (j + s + 1) 2, E w (j + s + 2) 2, E w (j + s + 1) 3)
      · -- case (ii): the rigid case
        obtain ⟨c, hc, hsig⟩ := hR
        have ch := chain_lemma c hc C.a1 C.a2 C.a3 C.b1 C.b2 C.b3 C.a12 C.a23
          (by have := C.a3n; omega) C.b32 C.b21 (by have := C.b1n; omega)
          (by rw [hsig]; simp only [sig3]; rw [C.e_am, C.e_mm1, C.e_am1])
        have ch' := chain_lemma c hc C'.a1 C'.a2 C'.a3 C'.b1 C'.b2 C'.b3 C'.a12 C'.a23
          (by have := C'.a3n; omega) C'.b32 C'.b21 (by have := C'.b1n; omega)
          (by rw [hsig, s4, s8, s5]; simp only [sig3]; rw [C'.e_am, C'.e_mm1, C'.e_am1])
        have st := rigidChains_strict c hc
        rw [← ch] at st
        simp only at st
        have e := ch.trans ch'.symm
        simp only [Prod.mk.injEq] at e
        obtain ⟨q1, q2, q3, q4, q5, q6⟩ := e
        exact rigid_three w w' j s u C C' q1 q2 q3 q4 q5 q6 st.1 st.2.1 st.2.2.1 st.2.2.2.1
          st.2.2.2.2.1 st.2.2.2.2.2 hna hnb s1 s2 s6 s9 s10 s11 s12 s13
      · -- case (iii): neither chain is rigid, so both pivot minors vanish
        have nr : ∀ (x : List Nat) (D : Copies3 x j s u),
            E x (j + s + 1) 1 ≤ 3 → E x (j + s + 3) 1 ≤ 3 →
            (E x (j + s + 1) 2, E x (j + s + 2) 2, E x (j + s + 1) 3) =
              (E w (j + s + 1) 2, E w (j + s + 2) 2, E w (j + s + 1) 3) →
            D.a1 = D.a2 ∨ D.a2 = D.a3 ∨ D.b1 = D.b2 ∨ D.b2 = D.b3 := by
          intro x D hxa hxb hxs
          apply Classical.byContradiction
          intro hcon
          apply hR
          have := D.a12; have := D.a23; have := D.b32; have := D.b21
          have := D.a3n; have := D.b1n
          refine ⟨(D.a1, D.a2, D.a3, D.b1, D.b2, D.b3),
            rigid_mem _ _ _ _ _ _ (by omega) (by omega) (by omega) (by omega) (by omega)
              (by omega), ?_⟩
          rw [← hxs]; simp only [sig3]; rw [D.e_am, D.e_mm1, D.e_am1]
        exact via_minor 3 hD
          (minor_three w j s u C (nr w C hna hnb rfl))
          (minor_three w' j s u C' (nr w' C' (by rw [← s12]; exact hna) (by rw [← s13]; exact hnb)
            (by rw [← s4, ← s8, ← s5])))

/-- **Corollary 4.2 (Conjecture C of Article 3 for n = 3).** In a window of at least five letters
whose inner letters occur at most three times, the window entry is determined by the shorter
entries of the window. -/
theorem complete_three (w w' : List Nat) (j u : Nat)
    (hmult : ∀ k, j < k → k < j + u + 4 → occ w [k] ≤ 3)
    (hsame : ∀ i r, j ≤ i → i + r ≤ j + u + 5 → r < u + 5 → E w i r = E w' i r) :
    E w j (u + 5) = E w' j (u + 5) := by
  have h := pivot_theorem w w' j 0 u
    (Or.inr ⟨hmult (j + 0 + 1) (by omega) (by omega), hmult (j + 0 + 2) (by omega) (by omega),
      hmult (j + 0 + 3) (by omega) (by omega)⟩)
    (fun i r h1 h2 h3 => hsame i r h1 (by omega) (by omega))
  simpa using h

/-- **Corollary 4.3 (five diagonals suffice).** In the window `lo, …, hi`, if every letter strictly
between `lo` and `hi` occurs at most three times in `w`, and `w'` agrees with `w` on every entry of
length at most 4 inside the window, then `w` and `w'` agree on every entry inside the window. -/
theorem determined_by_short_three (w w' : List Nat) (lo hi : Nat)
    (hmult : ∀ k, lo < k → k < hi → occ w [k] ≤ 3)
    (hshort : ∀ i r, lo ≤ i → i + r ≤ hi + 1 → r ≤ 4 → E w i r = E w' i r) :
    ∀ r i, lo ≤ i → i + r ≤ hi + 1 → E w i r = E w' i r := by
  intro r
  induction r using Nat.strongRecOn with
  | ind r ih =>
      intro i hi1 hi2
      by_cases hr : r ≤ 4
      · exact hshort i r hi1 hi2 hr
      · obtain ⟨u, rfl⟩ : ∃ u, r = u + 5 := ⟨r - 5, by omega⟩
        apply complete_three w w' i u
        · intro k h1 h2; exact hmult k (by omega) (by omega)
        · intro i' r' h1 h2 h3; exact ih r' h3 i' (by omega) (by omega)

/-- **Corollary 4.4.** If every letter `k` with `lo + 2 ≤ k ≤ hi - 2` occurs at most twice (the
letters `lo`, `lo+1`, `hi-1`, `hi` any number of times), the entries of length at most 4 determine
every entry of the window. -/
theorem determined_by_short_doubled (w w' : List Nat) (lo hi : Nat)
    (hmult : ∀ k, lo + 2 ≤ k → k + 2 ≤ hi → occ w [k] ≤ 2)
    (hshort : ∀ i r, lo ≤ i → i + r ≤ hi + 1 → r ≤ 4 → E w i r = E w' i r) :
    ∀ r i, lo ≤ i → i + r ≤ hi + 1 → E w i r = E w' i r := by
  intro r
  induction r using Nat.strongRecOn with
  | ind r ih =>
      intro i hi1 hi2
      by_cases hr : r ≤ 4
      · exact hshort i r hi1 hi2 hr
      · obtain ⟨u, rfl⟩ : ∃ u, r = u + 5 := ⟨r - 5, by omega⟩
        have h := pivot_theorem w w' i 0 u (Or.inl (hmult (i + 0 + 2) (by omega) (by omega)))
          (fun i' r' h1 h2 h3 => ih r' (by omega) i' (by omega) (by omega))
        simpa using h

end ParikhCompleteness
