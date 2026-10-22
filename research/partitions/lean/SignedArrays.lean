import CornerSlide

/-!
The height-two signed-array pilot for the H3 bridge. Empty rows are allowed.
Every row is carried with its actual permutation label. Shape equations use
integers, so a negative requested row length is not silently truncated.

This file proves combinatorial statements only. It does not assume or prove a
coloring expansion, an alternant identity, or a polynomial cancellation theorem.
-/

namespace SignedArrays

open CornerSlide
attribute [local instance] Classical.propDecidable

abbrev Entry := Nat × List Nat
abbrev Array := List Entry

def rows (a : Array) : Rows := a.map Prod.snd
def labels (a : Array) : List Nat := a.map Prod.fst
def contents (a : Array) : List Nat := (rows a).flatten

/-- Empty rows are legitimate; the complete filling is still bijective. -/
def ChainArray (r : Nat → Nat → Prop) (vertices : List Nat) (a : Array) : Prop :=
  vertices.Nodup ∧ (contents a).Perm vertices ∧
    ∀ entry ∈ a, entry.2.Pairwise r

def Partition (lambda : Nat → Nat) : Prop :=
  ∀ p q, p ≤ q → lambda q ≤ lambda p

def shiftKey (lambda : Nat → Nat) (p : Nat) : Int :=
  (lambda p : Int) - (p : Int)

/-- The parameter `i` is the row index, and remains an integer. -/
def ShapeAt (lambda : Nat → Nat) : Int → Array → Prop
  | _, [] => True
  | i, (p, row) :: rest =>
      (row.length : Int) = shiftKey lambda p + i ∧ ShapeAt lambda (i + 1) rest

/-- An actual finite permutation, not an arbitrary list of sign labels. -/
def SignedArray (r : Nat → Nat → Prop) (vertices : List Nat)
    (lambda : Nat → Nat) (a : Array) : Prop :=
  (labels a).Perm (List.range a.length) ∧ ShapeAt lambda 0 a ∧ ChainArray r vertices a

theorem shiftKey_strict (lambda : Nat → Nat) (hp : Partition lambda)
    (p q : Nat) (h : p < q) : shiftKey lambda q < shiftKey lambda p := by
  have hm := hp p q (by omega)
  unfold shiftKey
  omega

theorem shiftKey_injective (lambda : Nat → Nat) (hp : Partition lambda)
    (p q : Nat) (h : shiftKey lambda p = shiftKey lambda q) : p = q := by
  by_cases hlt : p < q
  · have := shiftKey_strict lambda hp p q hlt
    omega
  · by_cases hgt : q < p
    · have := shiftKey_strict lambda hp q p hgt
      omega
    · omega

theorem adjacent_length_exclusion (lambda : Nat → Nat) (hp : Partition lambda)
    (i : Int) (p q : Nat) (upper lower : List Nat) (tail : Array)
    (hneq : p ≠ q) (hs : ShapeAt lambda i ((p, upper) :: (q, lower) :: tail)) :
    (lower.length : Int) ≠ (upper.length : Int) + 1 := by
  intro he
  have hk : shiftKey lambda p = shiftKey lambda q := by
    have h₁ := hs.1
    have h₂ := hs.2.1
    omega
  exact hneq (shiftKey_injective lambda hp p q hk)

theorem adjacent_zero_one_excluded (lambda : Nat → Nat) (hp : Partition lambda)
    (i : Int) (p q : Nat) (upper lower : List Nat) (tail : Array)
    (hneq : p ≠ q) (hs : ShapeAt lambda i ((p, upper) :: (q, lower) :: tail)) :
    ¬ (upper.length = 0 ∧ lower.length = 1) := by
  rintro ⟨hu, hl⟩
  exact adjacent_length_exclusion lambda hp i p q upper lower tail hneq hs
    (by simp [hu, hl])

theorem adjacent_one_two_excluded (lambda : Nat → Nat) (hp : Partition lambda)
    (i : Int) (p q : Nat) (upper lower : List Nat) (tail : Array)
    (hneq : p ≠ q) (hs : ShapeAt lambda i ((p, upper) :: (q, lower) :: tail)) :
    ¬ (upper.length = 1 ∧ lower.length = 2) := by
  rintro ⟨hu, hl⟩
  exact adjacent_length_exclusion lambda hp i p q upper lower tail hneq hs
    (by simp [hu, hl])

theorem height_two_row_length_le_two (r : Nat → Nat → Prop)
    (height : NoThreeChain r) (row : List Nat) (hc : row.Pairwise r) :
    row.length ≤ 2 := by
  rcases row with _ | ⟨x, _ | ⟨y, _ | ⟨z, tail⟩⟩⟩
  · simp
  · simp
  · simp
  · have hx := List.pairwise_cons.mp hc
    have hy := List.pairwise_cons.mp hx.2
    exact False.elim (height x y z (hx.1 y (by simp)) (hy.1 z (by simp)))

/-- The complete first-column condition; it also rules out a hole above a cell. -/
def FirstPair (r : Nat → Nat → Prop) : List Nat → List Nat → Prop
  | _, [] => True
  | [], _ :: _ => False
  | x :: _, y :: _ => ¬ r y x

def GoodFirst (r : Nat → Nat → Prop) : Rows → Prop
  | [] => True
  | [_] => True
  | upper :: lower :: rest => FirstPair r upper lower ∧ GoodFirst r (lower :: rest)

def Good (r : Nat → Nat → Prop) (a : Array) : Prop := GoodFirst r (rows a)

/-- Both directions use the same guard `b <_P a`. -/
noncomputable def togglePair (r : Nat → Nat → Prop) : Entry → Entry → Entry × Entry
  | (p, []), (q, [b, a]) =>
      if r b a then ((q, [a]), (p, [b])) else ((p, []), (q, [b, a]))
  | (p, [a]), (q, [b]) =>
      if r b a then ((q, []), (p, [b, a])) else ((p, [a]), (q, [b]))
  | x, y => (x, y)

inductive PairMove (r : Nat → Nat → Prop) : Entry → Entry → Entry → Entry → Prop
  | stay (x y) : PairMove r x y x y
  | split (p q b a) (h : r b a) :
      PairMove r (p, []) (q, [b, a]) (q, [a]) (p, [b])
  | merge (p q b a) (h : r b a) :
      PairMove r (p, [a]) (q, [b]) (q, []) (p, [b, a])

theorem togglePair_spec (r : Nat → Nat → Prop) (x y : Entry) :
    PairMove r x y (togglePair r x y).1 (togglePair r x y).2 := by
  classical
  rcases x with ⟨p, upper⟩
  rcases y with ⟨q, lower⟩
  rcases upper with _ | ⟨a, _ | ⟨c, us⟩⟩ <;>
    rcases lower with _ | ⟨b, _ | ⟨d, _ | ⟨e, vs⟩⟩⟩
  all_goals first
    | exact PairMove.stay _ _
    | (simp only [togglePair]; split
       · exact PairMove.split _ _ _ _ (by assumption)
       · exact PairMove.stay _ _)
    | (simp only [togglePair]; split
       · exact PairMove.merge _ _ _ _ (by assumption)
       · exact PairMove.stay _ _)

theorem togglePair_involution (r : Nat → Nat → Prop) (x y : Entry) :
    togglePair r (togglePair r x y).1 (togglePair r x y).2 = (x, y) := by
  classical
  rcases x with ⟨p, upper⟩
  rcases y with ⟨q, lower⟩
  rcases upper with _ | ⟨a, _ | ⟨c, us⟩⟩ <;>
    rcases lower with _ | ⟨b, _ | ⟨d, _ | ⟨e, vs⟩⟩⟩
  all_goals first
    | rfl
    | (by_cases h : r b d <;> simp [togglePair, h])
    | (by_cases h : r b a <;> simp [togglePair, h])

theorem pairMove_good (r : Nat → Nat → Prop) (x y x' y' : Entry)
    (h : PairMove r x y x' y') (tail : Array) :
    Good r (x' :: y' :: tail) ↔ Good r (x :: y :: tail) := by
  cases h <;> simp [Good, rows, GoodFirst, FirstPair, *]

theorem pairMove_lower_good (r : Nat → Nat → Prop) (x y x' y' : Entry)
    (h : PairMove r x y x' y') (tail : Array) :
    Good r (y' :: tail) ↔ Good r (y :: tail) := by
  cases h with
  | stay => rfl
  | split p q b a _ =>
      cases tail with
      | nil => rfl
      | cons z tail =>
          rcases z with ⟨s, row⟩
          cases row <;> simp [Good, rows, GoodFirst, FirstPair]
  | merge p q b a _ =>
      cases tail with
      | nil => rfl
      | cons z tail =>
          rcases z with ⟨s, row⟩
          cases row <;> simp [Good, rows, GoodFirst, FirstPair]

theorem pairMove_labels_perm (r : Nat → Nat → Prop) (x y x' y' : Entry)
    (h : PairMove r x y x' y') (tail : Array) :
    (labels (x' :: y' :: tail)).Perm (labels (x :: y :: tail)) := by
  cases h with
  | stay => exact List.Perm.refl _
  | split p q b a _ => exact List.Perm.swap p q _
  | merge p q b a _ => exact List.Perm.swap p q _

theorem pairMove_contents_perm (r : Nat → Nat → Prop) (x y x' y' : Entry)
    (h : PairMove r x y x' y') (tail : Array) :
    (contents (x' :: y' :: tail)).Perm (contents (x :: y :: tail)) := by
  cases h with
  | stay => exact List.Perm.refl _
  | split p q b a _ => simpa [contents, rows] using List.Perm.swap b a (contents tail)
  | merge p q b a _ => simpa [contents, rows] using List.Perm.swap a b (contents tail)

theorem pairMove_shape (r : Nat → Nat → Prop) (lambda : Nat → Nat) (i : Int)
    (x y x' y' : Entry) (h : PairMove r x y x' y') (tail : Array) :
    ShapeAt lambda i (x' :: y' :: tail) ↔ ShapeAt lambda i (x :: y :: tail) := by
  cases h with
  | stay => rfl
  | split p q b a _ =>
      simp only [ShapeAt, List.length_nil, List.length_cons]
      constructor
      · rintro ⟨h₁, h₂, ht⟩
        exact ⟨by omega, by omega, ht⟩
      · rintro ⟨h₁, h₂, ht⟩
        exact ⟨by omega, by omega, ht⟩
  | merge p q b a _ =>
      simp only [ShapeAt, List.length_nil, List.length_cons]
      constructor
      · rintro ⟨h₁, h₂, ht⟩
        exact ⟨by omega, by omega, ht⟩
      · rintro ⟨h₁, h₂, ht⟩
        exact ⟨by omega, by omega, ht⟩

theorem pairMove_chains (r : Nat → Nat → Prop) (x y x' y' : Entry)
    (h : PairMove r x y x' y') (tail : Array)
    (hc : ∀ entry ∈ x :: y :: tail, entry.2.Pairwise r) :
    ∀ entry ∈ x' :: y' :: tail, entry.2.Pairwise r := by
  cases h with
  | stay => exact hc
  | split p q b a hba =>
      intro entry he
      simp only [List.mem_cons] at he
      rcases he with rfl | rfl | ht
      · simp
      · simp
      · exact hc entry (by simp [ht])
  | merge p q b a hba =>
      intro entry he
      simp only [List.mem_cons] at he
      rcases he with rfl | rfl | ht
      · simp
      · simpa using hba
      · exact hc entry (by simp [ht])

theorem pairMove_graphInversions (r : Nat → Nat → Prop) [DecidableRel r]
    (x y x' y' : Entry) (h : PairMove r x y x' y') (tail : Array) :
    graphInversions r (contents (x' :: y' :: tail)) =
      graphInversions r (contents (x :: y :: tail)) := by
  cases h with
  | stay => rfl
  | split p q b a hba =>
      simpa [contents, rows] using
        (graph_inversions_comparable_swap r [] (contents tail) b a hba).symm
  | merge p q b a hba =>
      simpa [contents, rows] using
        graph_inversions_comparable_swap r [] (contents tail) b a hba

/-- Inspect the suffix first, hence choose the bottommost first-column defect.
Malformed local boundaries stay fixed; height and signed shape will rule those
out in the fixed-sector theorem below. -/
noncomputable def move (r : Nat → Nat → Prop) : Array → Array
  | [] => []
  | [x] => [x]
  | x :: y :: tail =>
      if Good r (y :: tail) then
        (togglePair r x y).1 :: (togglePair r x y).2 :: tail
      else x :: move r (y :: tail)

theorem good_tail (r : Nat → Nat → Prop) (x : Entry) (tail : Array)
    (h : Good r (x :: tail)) : Good r tail := by
  cases tail with
  | nil => trivial
  | cons y tail => exact h.2

theorem move_cons_bad (r : Nat → Nat → Prop) (x : Entry) (tail : Array)
    (h : ¬ Good r tail) : move r (x :: tail) = x :: move r tail := by
  classical
  cases tail with
  | nil => exact False.elim (h True.intro)
  | cons y tail => simp [move, h]

theorem move_good_step (r : Nat → Nat → Prop) (x y : Entry) (tail : Array)
    (h : Good r (y :: tail)) :
    move r (x :: y :: tail) =
      (togglePair r x y).1 :: (togglePair r x y).2 :: tail := by
  classical
  simp [move, h]

theorem move_good_iff (r : Nat → Nat → Prop) (a : Array) :
    Good r (move r a) ↔ Good r a := by
  classical
  induction a with
  | nil => rfl
  | cons x tail ih =>
      cases tail with
      | nil => rfl
      | cons y tail =>
          by_cases hg : Good r (y :: tail)
          · rw [move_good_step r x y tail hg]
            exact pairMove_good r _ _ _ _ (togglePair_spec r x y) tail
          · rw [move_cons_bad r x (y :: tail) hg]
            have hn : ¬ Good r (move r (y :: tail)) := fun h => hg (ih.mp h)
            exact iff_of_false (fun h => hn (good_tail r x _ h))
              (fun h => hg (good_tail r x _ h))

/-- The bottommost pivot is stable, including across the changed lower row. -/
theorem bottommost_pivot_stable (r : Nat → Nat → Prop) (x y : Entry)
    (tail : Array) (h : Good r (y :: tail)) :
    Good r ((togglePair r x y).2 :: tail) :=
  (pairMove_lower_good r _ _ _ _ (togglePair_spec r x y) tail).mpr h

/-- Universal involutivity does not require a shape or a filling hypothesis.
Those hypotheses are needed to identify all fixed arrays with tableaux. -/
theorem move_involution (r : Nat → Nat → Prop) (a : Array) :
    move r (move r a) = a := by
  classical
  induction a with
  | nil => rfl
  | cons x tail ih =>
      cases tail with
      | nil => rfl
      | cons y tail =>
          by_cases hg : Good r (y :: tail)
          · rw [move_good_step r x y tail hg,
              move_good_step r _ _ tail (bottommost_pivot_stable r x y tail hg),
              togglePair_involution]
          · rw [move_cons_bad r x (y :: tail) hg]
            have hn : ¬ Good r (move r (y :: tail)) :=
              fun h => hg ((move_good_iff r _).mp h)
            rw [move_cons_bad r x _ hn, ih]

theorem move_labels_perm (r : Nat → Nat → Prop) (a : Array) :
    (labels (move r a)).Perm (labels a) := by
  classical
  induction a with
  | nil => exact List.Perm.refl _
  | cons x tail ih =>
      cases tail with
      | nil => exact List.Perm.refl _
      | cons y tail =>
          by_cases hg : Good r (y :: tail)
          · rw [move_good_step r x y tail hg]
            exact pairMove_labels_perm r _ _ _ _ (togglePair_spec r x y) tail
          · rw [move_cons_bad r x (y :: tail) hg]
            exact ih.cons x.1

theorem move_length (r : Nat → Nat → Prop) (a : Array) :
    (move r a).length = a.length := by
  have h := (move_labels_perm r a).length_eq
  simpa [labels] using h

theorem move_contents_perm (r : Nat → Nat → Prop) (a : Array) :
    (contents (move r a)).Perm (contents a) := by
  classical
  induction a with
  | nil => exact List.Perm.refl _
  | cons x tail ih =>
      cases tail with
      | nil => exact List.Perm.refl _
      | cons y tail =>
          by_cases hg : Good r (y :: tail)
          · rw [move_good_step r x y tail hg]
            exact pairMove_contents_perm r _ _ _ _ (togglePair_spec r x y) tail
          · rw [move_cons_bad r x (y :: tail) hg]
            exact ih.append_left x.2

theorem move_shape (r : Nat → Nat → Prop) (lambda : Nat → Nat) (i : Int)
    (a : Array) (h : ShapeAt lambda i a) : ShapeAt lambda i (move r a) := by
  classical
  induction a generalizing i with
  | nil => trivial
  | cons x tail ih =>
      cases tail with
      | nil => exact h
      | cons y tail =>
          by_cases hg : Good r (y :: tail)
          · rw [move_good_step r x y tail hg]
            exact (pairMove_shape r lambda i _ _ _ _ (togglePair_spec r x y) tail).mpr h
          · rw [move_cons_bad r x (y :: tail) hg]
            exact ⟨h.1, ih (i + 1) h.2⟩

theorem move_chains (r : Nat → Nat → Prop) (a : Array)
    (hc : ∀ entry ∈ a, entry.2.Pairwise r) :
    ∀ entry ∈ move r a, entry.2.Pairwise r := by
  classical
  induction a with
  | nil => simp [move]
  | cons x tail ih =>
      cases tail with
      | nil => simpa [move] using hc
      | cons y tail =>
          by_cases hg : Good r (y :: tail)
          · rw [move_good_step r x y tail hg]
            exact pairMove_chains r _ _ _ _ (togglePair_spec r x y) tail hc
          · rw [move_cons_bad r x (y :: tail) hg]
            intro entry he
            rcases List.mem_cons.mp he with hx | ht
            · subst entry; exact hc x (by simp)
            · exact ih (fun e he => hc e (by simp [he])) entry ht

theorem move_signedArray (r : Nat → Nat → Prop) (vertices : List Nat)
    (lambda : Nat → Nat) (a : Array) (h : SignedArray r vertices lambda a) :
    SignedArray r vertices lambda (move r a) := by
  refine ⟨?_, move_shape r lambda 0 a h.2.1, h.2.2.1, ?_,
    move_chains r a h.2.2.2.2⟩
  · rw [move_length]
    exact (move_labels_perm r a).trans h.1
  · exact (move_contents_perm r a).trans h.2.2.2.1

theorem move_graphInversions (r : Nat → Nat → Prop) [DecidableRel r] (a : Array) :
    graphInversions r (contents (move r a)) = graphInversions r (contents a) := by
  classical
  induction a with
  | nil => rfl
  | cons x tail ih =>
      cases tail with
      | nil => rfl
      | cons y tail =>
          by_cases hg : Good r (y :: tail)
          · rw [move_good_step r x y tail hg]
            exact pairMove_graphInversions r _ _ _ _ (togglePair_spec r x y) tail
          · rw [move_cons_bad r x (y :: tail) hg]
            exact wordWeight_append_congr (graphScore r) x.2 _ _
              (move_contents_perm r (y :: tail)) ih

theorem move_tableauGraphInversions (r : Nat → Nat → Prop) [DecidableRel r]
    (vertices : List Nat) (a : Array) (h : ChainArray r vertices a) :
    tableauGraphInversions r (rows (move r a)) = tableauGraphInversions r (rows a) := by
  have hc := move_chains r a h.2.2
  have hrows : ∀ row ∈ rows a, row.Pairwise r := by
    intro row hr
    obtain ⟨entry, he, rfl⟩ := List.mem_map.mp hr
    exact h.2.2 entry he
  have hmrows : ∀ row ∈ rows (move r a), row.Pairwise r := by
    intro row hr
    obtain ⟨entry, he, rfl⟩ := List.mem_map.mp hr
    exact hc entry he
  rw [tableau_graph_inversions_eq_word r _ hmrows,
    tableau_graph_inversions_eq_word r _ hrows]
  exact move_graphInversions r a

theorem row_cases_le_two (row : List Nat) (h : row.length ≤ 2) :
    row = [] ∨ (∃ a, row = [a]) ∨ (∃ a b, row = [a, b]) := by
  rcases row with _ | ⟨a, _ | ⟨b, _ | ⟨c, tail⟩⟩⟩
  · exact Or.inl rfl
  · exact Or.inr (Or.inl ⟨a, rfl⟩)
  · exact Or.inr (Or.inr ⟨a, b, rfl⟩)
  · simp only [List.length_cons] at h
    omega

theorem togglePair_fixed_iff (r : Nat → Nat → Prop) (height : NoThreeChain r)
    (p q : Nat) (upper lower : List Nat)
    (hu : upper.Pairwise r) (hl : lower.Pairwise r)
    (hex : (lower.length : Int) ≠ (upper.length : Int) + 1) :
    togglePair r (p, upper) (q, lower) = ((p, upper), (q, lower)) ↔
      FirstPair r upper lower := by
  classical
  have hul := row_cases_le_two upper (height_two_row_length_le_two r height upper hu)
  have hll := row_cases_le_two lower (height_two_row_length_le_two r height lower hl)
  rcases hul with rfl | ⟨a, rfl⟩ | ⟨a, c, rfl⟩
  · rcases hll with rfl | ⟨b, rfl⟩ | ⟨b, d, rfl⟩
    · simp [togglePair, FirstPair]
    · exact False.elim (hex (by simp))
    · have hbd : r b d := by simpa using hl
      simp [togglePair, FirstPair, hbd]
  · rcases hll with rfl | ⟨b, rfl⟩ | ⟨b, d, rfl⟩
    · simp [togglePair, FirstPair]
    · by_cases hba : r b a <;> simp [togglePair, FirstPair, hba]
    · exact False.elim (hex (by simp))
  · have hac : r a c := by simpa using hu
    rcases hll with rfl | ⟨b, rfl⟩ | ⟨b, d, rfl⟩
    · simp [togglePair, FirstPair]
    · have hba : ¬ r b a := fun hb => height b a c hb hac
      simp [togglePair, FirstPair, hba]
    · have hba : ¬ r b a := fun hb => height b a c hb hac
      simp [togglePair, FirstPair, hba]

/-- The universal map has no spurious fixed points on the intended sectors. -/
theorem move_fixed_iff_good (r : Nat → Nat → Prop) (height : NoThreeChain r)
    (lambda : Nat → Nat) (hp : Partition lambda) (i : Int) (a : Array)
    (hn : (labels a).Nodup) (hs : ShapeAt lambda i a)
    (hc : ∀ entry ∈ a, entry.2.Pairwise r) :
    move r a = a ↔ Good r a := by
  classical
  induction a generalizing i with
  | nil => simp [move, Good, rows, GoodFirst]
  | cons x tail ih =>
      cases tail with
      | nil => simp [move, Good, rows, GoodFirst]
      | cons y tail =>
          have hnt : (labels (y :: tail)).Nodup := (List.nodup_cons.mp hn).2
          have hct : ∀ entry ∈ y :: tail, entry.2.Pairwise r :=
            fun entry he => hc entry (by simp [he])
          by_cases hg : Good r (y :: tail)
          · rw [move_good_step r x y tail hg]
            rcases x with ⟨p, upper⟩
            rcases y with ⟨q, lower⟩
            have hneq : p ≠ q := by
              intro he
              exact (List.nodup_cons.mp hn).1 (by simp [he])
            have he := togglePair_fixed_iff r height p q upper lower
              (hc (p, upper) (by simp)) (hc (q, lower) (by simp))
              (adjacent_length_exclusion lambda hp i p q upper lower tail hneq hs)
            have hgood : Good r ((p, upper) :: (q, lower) :: tail) ↔
                FirstPair r upper lower := by
              change (FirstPair r upper lower ∧ Good r ((q, lower) :: tail)) ↔ _
              simp only [hg, and_true]
            rw [hgood]
            simp only [List.cons.injEq, and_true]
            constructor
            · intro hf
              exact he.mp (Prod.ext hf.1 hf.2)
            · intro hf
              have ht := he.mpr hf
              exact ⟨congrArg Prod.fst ht, congrArg Prod.snd ht⟩
          · rw [move_cons_bad r x (y :: tail) hg]
            apply iff_of_false
            · intro he
              exact hg ((ih (i + 1) hnt hs.2 hct).mp (List.cons.inj he).2)
            · intro he
              exact hg (good_tail r x _ he)

theorem firstPair_of_columnPair (r : Nat → Nat → Prop) (upper lower : List Nat)
    (h : ColumnPair r upper lower) : FirstPair r upper lower := by
  cases lower with
  | nil => trivial
  | cons b lower =>
      cases upper with
      | nil => exact h
      | cons a upper => exact h.1

/-- At height two, a possible second-column descent would form a three-chain.
The shifted shape separately excludes a singleton row above a pair row. -/
theorem columnPair_iff_firstPair (r : Nat → Nat → Prop) (height : NoThreeChain r)
    (upper lower : List Nat) (hu : upper.Pairwise r) (hl : lower.Pairwise r)
    (hex : (lower.length : Int) ≠ (upper.length : Int) + 1) :
    ColumnPair r upper lower ↔ FirstPair r upper lower := by
  constructor
  · exact firstPair_of_columnPair r upper lower
  · intro hf
    have hul := row_cases_le_two upper (height_two_row_length_le_two r height upper hu)
    have hll := row_cases_le_two lower (height_two_row_length_le_two r height lower hl)
    rcases hul with rfl | ⟨a, rfl⟩ | ⟨a, c, rfl⟩
    · rcases hll with rfl | ⟨b, rfl⟩ | ⟨b, d, rfl⟩
      · trivial
      · exact False.elim hf
      · exact False.elim hf
    · rcases hll with rfl | ⟨b, rfl⟩ | ⟨b, d, rfl⟩
      · trivial
      · exact ⟨hf, True.intro⟩
      · exact False.elim (hex (by simp))
    · rcases hll with rfl | ⟨b, rfl⟩ | ⟨b, d, rfl⟩
      · trivial
      · exact ⟨hf, True.intro⟩
      · have hbd : r b d := by simpa using hl
        have hdc : ¬ r d c := fun hd => height b d c hbd hd
        exact ⟨hf, hdc, True.intro⟩

theorem columns_iff_good (r : Nat → Nat → Prop) (height : NoThreeChain r)
    (lambda : Nat → Nat) (hp : Partition lambda) (i : Int) (a : Array)
    (hn : (labels a).Nodup) (hs : ShapeAt lambda i a)
    (hc : ∀ entry ∈ a, entry.2.Pairwise r) :
    ColumnsValid r (rows a) ↔ Good r a := by
  induction a generalizing i with
  | nil => rfl
  | cons x tail ih =>
      cases tail with
      | nil => rfl
      | cons y tail =>
          rcases x with ⟨p, upper⟩
          rcases y with ⟨q, lower⟩
          have hneq : p ≠ q := by
            intro he
            exact (List.nodup_cons.mp hn).1 (by simp [he])
          have he := columnPair_iff_firstPair r height upper lower
            (hc (p, upper) (by simp)) (hc (q, lower) (by simp))
            (adjacent_length_exclusion lambda hp i p q upper lower tail hneq hs)
          have ht := ih (i + 1) (List.nodup_cons.mp hn).2 hs.2
            (fun entry he => hc entry (by simp [he]))
          change (ColumnPair r upper lower ∧ ColumnsValid r (rows ((q, lower) :: tail))) ↔
            (FirstPair r upper lower ∧ Good r ((q, lower) :: tail))
          exact and_congr he ht

theorem columns_tail (r : Nat → Nat → Prop) (row : List Nat) (tail : Rows)
    (h : ColumnsValid r (row :: tail)) : ColumnsValid r tail := by
  cases tail with
  | nil => trivial
  | cons lower tail => exact h.2

theorem columns_prefix (r : Nat → Nat → Prop) (front tail : Rows)
    (h : ColumnsValid r (front ++ tail)) : ColumnsValid r front := by
  induction front with
  | nil => trivial
  | cons row front ih =>
      cases front with
      | nil => trivial
      | cons lower front => exact ⟨h.1, ih h.2⟩

theorem columns_empty_rows (r : Nat → Nat → Prop) (k : Nat) :
    ColumnsValid r (List.replicate k []) := by
  induction k with
  | zero => trivial
  | succ k ih =>
      cases k with
      | zero => trivial
      | succ k => exact ⟨True.intro, ih⟩

theorem columns_padding (r : Nat → Nat → Prop) (body : Rows) (k : Nat) :
    ColumnsValid r (body ++ List.replicate k []) ↔ ColumnsValid r body := by
  induction body with
  | nil => exact iff_of_true (columns_empty_rows r k) True.intro
  | cons row body ih =>
      cases body with
      | nil =>
          cases k with
          | zero => rfl
          | succ k =>
              exact iff_of_true ⟨by cases row <;> trivial,
                columns_empty_rows r (k + 1)⟩ True.intro
      | cons lower body => exact and_congr Iff.rfl ih

theorem flatten_padding (body : Rows) (k : Nat) :
    (body ++ List.replicate k []).flatten = body.flatten := by
  have he : (List.replicate k ([] : List Nat)).flatten = [] := by
    induction k with
    | zero => rfl
    | succ k ih => simp [List.replicate_succ, ih]
  simp [he]

theorem empty_head_padding (r : Nat → Nat → Prop) (tail : Rows)
    (h : ColumnsValid r ([] :: tail)) :
    [] :: tail = List.replicate (tail.length + 1) [] := by
  induction tail with
  | nil => rfl
  | cons row tail ih =>
      cases row with
      | nil =>
          have he := ih h.2
          simpa [List.replicate_succ] using congrArg (List.cons []) he
      | cons x row => exact False.elim h.1

theorem columns_nonempty_decomposition (r : Nat → Nat → Prop) (rs : Rows)
    (h : ColumnsValid r rs) :
    ∃ body k, rs = body ++ List.replicate k [] ∧
      (∀ row ∈ body, row ≠ []) ∧ ColumnsValid r body := by
  induction rs with
  | nil => exact ⟨[], 0, rfl, by simp, True.intro⟩
  | cons row tail ih =>
      by_cases he : row = []
      · subst row
        exact ⟨[], tail.length + 1, empty_head_padding r tail h, by simp, True.intro⟩
      · obtain ⟨body, k, ht, hb, hcols⟩ := ih (columns_tail r row tail h)
        refine ⟨row :: body, k, by simp [ht], ?_, ?_⟩
        · intro x hx
          rcases List.mem_cons.mp hx with rfl | hx
          · exact he
          · exact hb x hx
        · apply columns_prefix r (row :: body) (List.replicate k [])
          simpa [ht] using h

def PaddedTableau (r : Nat → Nat → Prop) (vertices : List Nat) (rs : Rows) : Prop :=
  ∃ body k, rs = body ++ List.replicate k [] ∧ Tableau r vertices body

theorem chainArray_columns_iff_padded (r : Nat → Nat → Prop) (vertices : List Nat)
    (a : Array) (hc : ChainArray r vertices a) :
    ColumnsValid r (rows a) ↔ PaddedTableau r vertices (rows a) := by
  constructor
  · intro hcols
    obtain ⟨body, k, he, hne, hbcols⟩ := columns_nonempty_decomposition r (rows a) hcols
    refine ⟨body, k, he, hc.1, ?_, ?_, hbcols⟩
    · have hf := hc.2.1
      change (rows a).flatten.Perm vertices at hf
      simpa [he, flatten_padding] using hf
    · intro row hr
      refine ⟨hne row hr, ?_⟩
      have hm : row ∈ rows a := by rw [he]; simp [hr]
      obtain ⟨entry, hm, heq⟩ := List.mem_map.mp hm
      exact heq ▸ hc.2.2 entry hm
  · rintro ⟨body, k, he, ht⟩
    rw [he, columns_padding]
    exact ht.2.2.2

/-- Exact fixed-sector characterization, with empties retained as trailing
padding and the existing actual `Tableau` predicate on the nonempty body. -/
theorem signedArray_fixed_iff_padded (r : Nat → Nat → Prop)
    (height : NoThreeChain r) (lambda : Nat → Nat) (hp : Partition lambda)
    (vertices : List Nat) (a : Array) (h : SignedArray r vertices lambda a) :
    move r a = a ↔ PaddedTableau r vertices (rows a) := by
  have hn : (labels a).Nodup := h.1.nodup_iff.mpr List.nodup_range
  exact (move_fixed_iff_good r height lambda hp 0 a hn h.2.1 h.2.2.2.2).trans
    ((columns_iff_good r height lambda hp 0 a hn h.2.1 h.2.2.2.2).symm.trans
      (chainArray_columns_iff_padded r vertices a h.2.2))

theorem columnPair_length (r : Nat → Nat → Prop) (upper lower : List Nat)
    (h : ColumnPair r upper lower) : lower.length ≤ upper.length := by
  induction upper generalizing lower with
  | nil =>
      cases lower with
      | nil => simp
      | cons b lower => exact False.elim h
  | cons a upper ih =>
      cases lower with
      | nil => simp
      | cons b lower =>
          have ht := ih lower h.2
          simp only [List.length_cons]
          omega

theorem shape_column_labels_lt (r : Nat → Nat → Prop) (lambda : Nat → Nat)
    (hp : Partition lambda) (i : Int) (p q : Nat) (upper lower : List Nat)
    (tail : Array) (hs : ShapeAt lambda i ((p, upper) :: (q, lower) :: tail))
    (hc : ColumnPair r upper lower) : p < q := by
  have hl := columnPair_length r upper lower hc
  have hk : shiftKey lambda q < shiftKey lambda p := by
    have h₁ := hs.1
    have h₂ := hs.2.1
    omega
  by_cases he : p = q
  · subst q
    omega
  · by_cases hq : q < p
    · have := shiftKey_strict lambda hp q p hq
      omega
    · omega

theorem column_labels_sorted (r : Nat → Nat → Prop) (lambda : Nat → Nat)
    (hp : Partition lambda) (i : Int) (a : Array)
    (hs : ShapeAt lambda i a) (hc : ColumnsValid r (rows a)) :
    (labels a).Pairwise (· < ·) := by
  induction a generalizing i with
  | nil => simp [labels]
  | cons x tail ih =>
      cases tail with
      | nil => simp [labels]
      | cons y tail =>
          rcases x with ⟨p, upper⟩
          rcases y with ⟨q, lower⟩
          have hpq := shape_column_labels_lt r lambda hp i p q upper lower tail hs hc.1
          have ht := ih (i + 1) hs.2 hc.2
          apply List.pairwise_cons.mpr
          refine ⟨?_, ht⟩
          intro z hz
          rcases List.mem_cons.mp hz with rfl | hz
          · exact hpq
          · exact Nat.lt_trans hpq ((List.pairwise_cons.mp ht).1 z hz)

/-- In a fixed signed sector the finite permutation is exactly the identity. -/
theorem fixed_labels_identity (r : Nat → Nat → Prop) (height : NoThreeChain r)
    (lambda : Nat → Nat) (hp : Partition lambda) (vertices : List Nat)
    (a : Array) (h : SignedArray r vertices lambda a) (hf : move r a = a) :
    labels a = List.range a.length := by
  have hn : (labels a).Nodup := h.1.nodup_iff.mpr List.nodup_range
  have hg := (move_fixed_iff_good r height lambda hp 0 a hn h.2.1 h.2.2.2.2).mp hf
  have hcols := (columns_iff_good r height lambda hp 0 a hn h.2.1 h.2.2.2.2).mpr hg
  exact List.Perm.eq_of_pairwise
    (fun _ _ _ _ hab hba => False.elim (Nat.lt_asymm hab hba))
    (column_labels_sorted r lambda hp 0 a h.2.1 hcols) List.pairwise_lt_range h.1

theorem identity_shape (lambda : Nat → Nat) (start : Nat) (a : Array)
    (hs : ShapeAt lambda (start : Int) a)
    (hl : labels a = List.range' start a.length) :
    (rows a).map List.length = (List.range' start a.length).map lambda := by
  induction a generalizing start with
  | nil => simp [rows]
  | cons entry tail ih =>
      rcases entry with ⟨p, row⟩
      have hh : p = start ∧ labels tail = List.range' (start + 1) tail.length := by
        simpa only [labels, List.map_cons, List.length_cons, List.range'_succ,
          List.cons.injEq] using hl
      rcases hh with ⟨he, htlabels⟩
      subst p
      have hlen : row.length = lambda start := by
        have h := hs.1
        unfold shiftKey at h
        omega
      have ht : ShapeAt lambda ((start + 1 : Nat) : Int) tail := by
        simpa only [Int.natCast_add, Int.natCast_one] using hs.2
      simpa only [rows, List.map_cons, List.length_cons, List.range'_succ, hlen] using
        congrArg (List.cons (lambda start)) (ih (start + 1) ht htlabels)

theorem fixed_row_lengths (r : Nat → Nat → Prop) (height : NoThreeChain r)
    (lambda : Nat → Nat) (hp : Partition lambda) (vertices : List Nat)
    (a : Array) (h : SignedArray r vertices lambda a) (hf : move r a = a) :
    (rows a).map List.length = (List.range a.length).map lambda := by
  have he := fixed_labels_identity r height lambda hp vertices a h hf
  rw [List.range_eq_range'] at he ⊢
  exact identity_shape lambda 0 a h.2.1 he

/-- The determinant sign of a finite permutation, defined by inversion parity. -/
def labelScore (p q : Nat) : Nat := if q < p then 1 else 0

def paritySign (n : Nat) : Int := if n % 2 = 0 then 1 else -1

def permutationSign (ps : List Nat) : Int := paritySign (wordWeight labelScore ps)

theorem paritySign_succ (n : Nat) : paritySign (n + 1) = -paritySign n := by
  have hn := Nat.mod_lt n (by decide : 0 < 2)
  by_cases he : n % 2 = 0
  · simp [paritySign, Nat.add_mod, he]
  · have ho : n % 2 = 1 := by omega
    simp [paritySign, Nat.add_mod, ho]

theorem paritySign_add (m n : Nat) :
    paritySign (m + n) = paritySign m * paritySign n := by
  have hm := Nat.mod_lt m (by decide : 0 < 2)
  have hn := Nat.mod_lt n (by decide : 0 < 2)
  have hm' : m % 2 = 0 ∨ m % 2 = 1 := by omega
  have hn' : n % 2 = 0 ∨ n % 2 = 1 := by omega
  rcases hm' with he | ho <;> rcases hn' with he' | ho' <;>
    simp [paritySign, Nat.add_mod, *]

theorem labelInversions_adjacent (front tail : List Nat) (p q : Nat) (h : p < q) :
    wordWeight labelScore (front ++ q :: p :: tail) =
      wordWeight labelScore (front ++ p :: q :: tail) + 1 := by
  induction front with
  | nil =>
      have hqp : ¬ q < p := by omega
      simp only [List.nil_append, wordWeight, List.map_cons, List.sum_cons,
        labelScore, h, hqp, ↓reduceIte]
      omega
  | cons z front ih =>
      have hp := (List.Perm.swap p q tail).append_left front
      have hs := perm_nat_sum _ _ (hp.map (labelScore z))
      simp only [List.cons_append, wordWeight]
      omega

theorem permutationSign_adjacent_swap (front tail : List Nat) (p q : Nat)
    (hne : p ≠ q) :
    permutationSign (front ++ q :: p :: tail) =
      -permutationSign (front ++ p :: q :: tail) := by
  by_cases h : p < q
  · unfold permutationSign
    rw [labelInversions_adjacent front tail p q h, paritySign_succ]
  · have hq : q < p := by omega
    have he := labelInversions_adjacent front tail q p hq
    unfold permutationSign
    rw [he, paritySign_succ, Int.neg_neg]

theorem permutationSign_cons_flip (p : Nat) (xs ys : List Nat) (hp : xs.Perm ys)
    (hs : permutationSign xs = -permutationSign ys) :
    permutationSign (p :: xs) = -permutationSign (p :: ys) := by
  have he := perm_nat_sum _ _ (hp.map (labelScore p))
  simp only [permutationSign, wordWeight, paritySign_add] at hs ⊢
  rw [he, hs, Int.mul_neg]

theorem pairMove_sign (r : Nat → Nat → Prop) (x y x' y' : Entry)
    (h : PairMove r x y x' y') (tail : Array)
    (hn : (labels (x :: y :: tail)).Nodup) (hm : (x', y') ≠ (x, y)) :
    permutationSign (labels (x' :: y' :: tail)) =
      -permutationSign (labels (x :: y :: tail)) := by
  cases h with
  | stay => exact False.elim (hm rfl)
  | split p q b a _ =>
      have hne : p ≠ q := by
        intro he
        exact (List.nodup_cons.mp hn).1 (by simp [he])
      exact permutationSign_adjacent_swap [] (labels tail) p q hne
  | merge p q b a _ =>
      have hne : p ≠ q := by
        intro he
        exact (List.nodup_cons.mp hn).1 (by simp [he])
      exact permutationSign_adjacent_swap [] (labels tail) p q hne

/-- Every moved array reverses the actual inversion-parity permutation sign.
Distinct labels suffice; height and partition shape identify the moved sector. -/
theorem move_sign_reversing (r : Nat → Nat → Prop) (a : Array)
    (hn : (labels a).Nodup) (hm : move r a ≠ a) :
    permutationSign (labels (move r a)) = -permutationSign (labels a) := by
  classical
  induction a with
  | nil => exact False.elim (hm rfl)
  | cons x tail ih =>
      cases tail with
      | nil => exact False.elim (hm rfl)
      | cons y tail =>
          by_cases hg : Good r (y :: tail)
          · have hp : (togglePair r x y) ≠ (x, y) := by
              intro he
              apply hm
              rw [move_good_step r x y tail hg, he]
            rw [move_good_step r x y tail hg]
            exact pairMove_sign r _ _ _ _ (togglePair_spec r x y) tail hn hp
          · have hmt : move r (y :: tail) ≠ y :: tail := by
              intro he
              apply hm
              rw [move_cons_bad r x (y :: tail) hg, he]
            rw [move_cons_bad r x (y :: tail) hg]
            exact permutationSign_cons_flip x.1 _ _ (move_labels_perm r (y :: tail))
              (ih (List.nodup_cons.mp hn).2 hmt)

theorem signedArray_bad_sign_reversing (r : Nat → Nat → Prop)
    (height : NoThreeChain r) (lambda : Nat → Nat) (hp : Partition lambda)
    (vertices : List Nat) (a : Array) (h : SignedArray r vertices lambda a)
    (hg : ¬ Good r a) :
    permutationSign (labels (move r a)) = -permutationSign (labels a) := by
  have hn : (labels a).Nodup := h.1.nodup_iff.mpr List.nodup_range
  exact move_sign_reversing r a hn
    (fun he => hg ((move_fixed_iff_good r height lambda hp 0 a hn h.2.1 h.2.2.2.2).mp he))

theorem sorted_label_inversions_zero (ps : List Nat) (h : ps.Pairwise (· < ·)) :
    wordWeight labelScore ps = 0 := by
  induction ps with
  | nil => rfl
  | cons p ps ih =>
      have hp := List.pairwise_cons.mp h
      have hz : (ps.map (labelScore p)).sum = 0 := by
        apply sumMap_zero
        intro q hq
        have hlt := hp.1 q hq
        have hqp : ¬ q < p := by omega
        simp [labelScore, hqp]
      simp only [wordWeight, hz, ih hp.2, Nat.zero_add]

theorem identity_permutationSign (m : Nat) : permutationSign (List.range m) = 1 := by
  unfold permutationSign
  rw [sorted_label_inversions_zero _ List.pairwise_lt_range]
  rfl

theorem fixed_permutationSign (r : Nat → Nat → Prop) (height : NoThreeChain r)
    (lambda : Nat → Nat) (hp : Partition lambda) (vertices : List Nat)
    (a : Array) (h : SignedArray r vertices lambda a) (hf : move r a = a) :
    permutationSign (labels a) = 1 := by
  rw [fixed_labels_identity r height lambda hp vertices a h hf, identity_permutationSign]

end SignedArrays

#print axioms SignedArrays.shiftKey_injective
#print axioms SignedArrays.adjacent_length_exclusion
#print axioms SignedArrays.height_two_row_length_le_two
#print axioms SignedArrays.togglePair_involution
#print axioms SignedArrays.bottommost_pivot_stable
#print axioms SignedArrays.move_involution
#print axioms SignedArrays.move_signedArray
#print axioms SignedArrays.move_tableauGraphInversions
#print axioms SignedArrays.move_fixed_iff_good
#print axioms SignedArrays.columns_iff_good
#print axioms SignedArrays.signedArray_fixed_iff_padded
#print axioms SignedArrays.fixed_labels_identity
#print axioms SignedArrays.fixed_row_lengths
#print axioms SignedArrays.move_sign_reversing
#print axioms SignedArrays.signedArray_bad_sign_reversing
#print axioms SignedArrays.fixed_permutationSign
