import Std

/-!
An exact validity criterion for splitting the last two-cell row of a P-tableau,
and a formalization of the height-two bubbling injection of Cho and Huh,
arXiv:1711.07152, Section 3.1. The local validity and inverse statements concern
arbitrary row fronts and singleton suffixes. This file does not formalize the
symmetric-function identities connecting the injection with e-positivity.
-/

namespace CornerSlide

abbrev Rows := List (List Nat)

/-- Strict chains along rows, with no empty row. -/
def RowValid (r : Nat → Nat → Prop) (row : List Nat) : Prop :=
  row ≠ [] ∧ row.Pairwise r

/-- Every lower cell has an upper cell and does not lie strictly below it in P.
The existence requirement also imposes weakly decreasing row lengths. -/
def ColumnPair (r : Nat → Nat → Prop) : List Nat → List Nat → Prop
  | _, [] => True
  | [], _ :: _ => False
  | x :: xs, y :: ys => ¬ r y x ∧ ColumnPair r xs ys

/-- The adjacent vertical comparisons in every column. -/
def ColumnsValid (r : Nat → Nat → Prop) : Rows → Prop
  | [] => True
  | [_] => True
  | upper :: lower :: rest => ColumnPair r upper lower ∧ ColumnsValid r (lower :: rest)

def ShapeAndOrder (r : Nat → Nat → Prop) (rows : Rows) : Prop :=
  (∀ row ∈ rows, RowValid r row) ∧ ColumnsValid r rows

/-- An actual bijective filling of the distinct vertex list `vertices`. -/
def Tableau (r : Nat → Nat → Prop) (vertices : List Nat) (rows : Rows) : Prop :=
  vertices.Nodup ∧ rows.flatten.Perm vertices ∧ ShapeAndOrder r rows

def singletons (tail : List Nat) : Rows := tail.map (fun x => [x])

def before (front : Rows) (c d : Nat) (tail : List Nat) : Rows :=
  front ++ ([c, d] :: singletons tail)

def after (front : Rows) (c d : Nat) (tail : List Nat) : Rows :=
  front ++ ([c] :: [d] :: singletons tail)

/-- This is the one additional vertical comparison introduced below `d`. -/
def Boundary (r : Nat → Nat → Prop) (d : Nat) : List Nat → Prop
  | [] => True
  | z :: _ => ¬ r z d

theorem rowValid_singleton (r : Nat → Nat → Prop) (x : Nat) : RowValid r [x] := by
  simp [RowValid]

theorem rowValid_pair (r : Nat → Nat → Prop) (c d : Nat) :
    RowValid r [c, d] ↔ r c d := by
  simp [RowValid]

theorem columnPair_shorten (r : Nat → Nat → Prop) (upper : List Nat) (c d : Nat)
    (h : ColumnPair r upper [c, d]) : ColumnPair r upper [c] := by
  cases upper with
  | nil => simp [ColumnPair] at h
  | cons x xs => simpa [ColumnPair] using h.1

theorem flatten_before_after (front : Rows) (c d : Nat) (tail : List Nat) :
    (before front c d tail).flatten = (after front c d tail).flatten := by
  simp [before, after]

theorem rows_before_after (r : Nat → Nat → Prop) (front : Rows) (c d : Nat)
    (tail : List Nat) (h : ∀ row ∈ before front c d tail, RowValid r row) :
    ∀ row ∈ after front c d tail, RowValid r row := by
  intro row hr
  simp only [after, List.mem_append, List.mem_cons] at hr
  rcases hr with hp | hc | hd | ht
  · exact h row (by simp [before, hp])
  · subst row; exact rowValid_singleton r c
  · subst row; exact rowValid_singleton r d
  · exact h row (by simp [before, ht])

theorem pair_relation (r : Nat → Nat → Prop) (front : Rows) (c d : Nat)
    (tail : List Nat) (h : ∀ row ∈ before front c d tail, RowValid r row) : r c d := by
  exact (rowValid_pair r c d).mp (h [c, d] (by simp [before]))

theorem columns_demote_iff (r : Nat → Nat → Prop)
    (asym : ∀ x y, r x y → ¬ r y x) (front : Rows) (c d : Nat)
    (tail : List Nat) (hcd : r c d)
    (h : ColumnsValid r (before front c d tail)) :
    ColumnsValid r (after front c d tail) ↔ Boundary r d tail := by
  induction front with
  | nil =>
      cases tail with
      | nil => simp [after, singletons, ColumnsValid, ColumnPair, Boundary, asym c d hcd]
      | cons z zs =>
          have htail : ColumnsValid r ([z] :: singletons zs) := by
            exact h.2
          change ((¬ r d c ∧ True) ∧ ((¬ r z d ∧ True) ∧
            ColumnsValid r ([z] :: singletons zs))) ↔ ¬ r z d
          constructor
          · intro ht; exact ht.2.1.1
          · intro hz; exact ⟨⟨asym c d hcd, True.intro⟩, ⟨⟨hz, True.intro⟩, htail⟩⟩
  | cons upper rest ih =>
      cases rest with
      | nil =>
          have hp : ColumnPair r upper [c] := columnPair_shorten r upper c d h.1
          have hlocal := ih h.2
          change ColumnPair r upper [c] ∧
            ColumnsValid r (after [] c d tail) ↔ Boundary r d tail
          simpa only [hp, true_and] using hlocal
      | cons lower more =>
          have hp : ColumnPair r upper lower := h.1
          have hlocal := ih h.2
          change ColumnPair r upper lower ∧
            ColumnsValid r (after (lower :: more) c d tail) ↔ Boundary r d tail
          simpa only [hp, true_and] using hlocal

/-- The corrected arbitrary-size corner-slide theorem. Both sides use actual
bijective P-tableaux, including every row, column, shape, and filling condition. -/
theorem demote_valid_iff (r : Nat → Nat → Prop)
    (asym : ∀ x y, r x y → ¬ r y x) (vertices : List Nat)
    (front : Rows) (c d : Nat) (tail : List Nat)
    (h : Tableau r vertices (before front c d tail)) :
    Tableau r vertices (after front c d tail) ↔ Boundary r d tail := by
  have hcd := pair_relation r front c d tail h.2.2.1
  have hc := columns_demote_iff r asym front c d tail hcd h.2.2.2
  have hr := rows_before_after r front c d tail h.2.2.1
  have hf : (after front c d tail).flatten.Perm vertices := by
    rw [← flatten_before_after]
    exact h.2.1
  constructor
  · intro ht; exact hc.mp ht.2.2.2
  · intro hb; exact ⟨h.1, hf, hr, hc.mpr hb⟩

/-- The row-major word is unchanged, so every statistic defined on that word
is unchanged. This includes graph inversions once their word interpretation is
identified for strict-chain rows of an incomparability tableau. -/
theorem word_statistic_preserved {β : Type} (statistic : List Nat → β)
    (front : Rows) (c d : Nat) (tail : List Nat) :
    statistic (before front c d tail).flatten =
      statistic (after front c d tail).flatten := by
  rw [flatten_before_after]

/-- The natural unit interval order h=(1,2,3,4,5), on its five vertices. -/
def fiveOrder (x y : Nat) : Prop := x < y

theorem fiveOrder_asymmetric : ∀ x y, fiveOrder x y → ¬ fiveOrder y x := by
  intro x y hxy hyx
  exact Nat.lt_asymm hxy hyx

/-- The original filling satisfies every P-tableau condition. -/
theorem counterexample_source :
    Tableau fiveOrder [1, 2, 3, 4, 5] [[1, 2], [3, 5], [4]] := by
  simp [Tableau, ShapeAndOrder, RowValid, ColumnsValid, ColumnPair, fiveOrder]
  decide

/-- Demotion fails at the new comparison 4 <_P 5. -/
theorem counterexample_target_invalid :
    ¬ Tableau fiveOrder [1, 2, 3, 4, 5] [[1, 2], [3], [5], [4]] := by
  simp [Tableau, ShapeAndOrder, RowValid, ColumnsValid, ColumnPair, fiveOrder]

theorem counterexample_boundary_fails : ¬ Boundary fiveOrder 5 [4] := by
  simp only [Boundary, fiveOrder]
  decide

/-- Four vertices have no remaining singleton below the split row. -/
theorem demote_bottom_row_valid (r : Nat → Nat → Prop)
    (asym : ∀ x y, r x y → ¬ r y x) (vertices : List Nat)
    (front : Rows) (c d : Nat)
    (h : Tableau r vertices (before front c d [])) :
    Tableau r vertices (after front c d []) := by
  exact (demote_valid_iff r asym vertices front c d [] h).mpr True.intro

/-- Insert `b` after the initial segment whose entries lie below `b` in P. -/
def bubbleInsert (r : Nat → Nat → Prop) [DecidableRel r] (b : Nat) : List Nat → List Nat
  | [] => [b]
  | z :: zs => if r z b then z :: bubbleInsert r b zs else b :: z :: zs

/-- Delete and return the first entry satisfying `p`, retaining the other entries. -/
def extractFirst (p : Nat → Prop) [DecidablePred p] : List Nat → Option (Nat × List Nat)
  | [] => none
  | z :: zs => if p z then some (z, zs) else
      match extractFirst p zs with
      | none => none
      | some (b, rest) => some (b, z :: rest)

theorem extract_bubble_inverse (r : Nat → Nat → Prop) [DecidableRel r]
    (a b : Nat) (tail : List Nat) (hab : r a b)
    (separate : ∀ z, r z b → ¬ r a z) :
    extractFirst (r a) (bubbleInsert r b tail) = some (b, tail) := by
  induction tail with
  | nil => simp [bubbleInsert, extractFirst, hab]
  | cons z zs ih =>
      by_cases hz : r z b
      · simp [bubbleInsert, hz, extractFirst, separate z hz, ih]
      · simp [bubbleInsert, hz, extractFirst, hab]

/-- Height at most two, expressed as the absence of a strict three-element chain.
A relation on a finite vertex set can be extended by false outside that set. -/
def NoThreeChain (r : Nat → Nat → Prop) : Prop :=
  ∀ x y z, r x y → r y z → False

theorem extract_bubble_inverse_height_two (r : Nat → Nat → Prop) [DecidableRel r]
    (height : NoThreeChain r) (a b : Nat) (tail : List Nat) (hab : r a b) :
    extractFirst (r a) (bubbleInsert r b tail) = some (b, tail) := by
  apply extract_bubble_inverse r a b tail hab
  intro z hzb haz
  exact height a z b haz hzb

theorem bubble_injective_height_two (r : Nat → Nat → Prop) [DecidableRel r]
    (height : NoThreeChain r) (a b b' : Nat) (tail tail' : List Nat)
    (hab : r a b) (hab' : r a b')
    (h : bubbleInsert r b tail = bubbleInsert r b' tail') : b = b' ∧ tail = tail' := by
  have he := congrArg (extractFirst (r a)) h
  rw [extract_bubble_inverse_height_two r height a b tail hab,
    extract_bubble_inverse_height_two r height a b' tail' hab'] at he
  exact Prod.mk.inj (Option.some.inj he)

def NoDescent (r : Nat → Nat → Prop) : List Nat → Prop
  | [] => True
  | [_] => True
  | x :: y :: rest => ¬ r y x ∧ NoDescent r (y :: rest)

theorem columns_singletons (r : Nat → Nat → Prop) (xs : List Nat) :
    ColumnsValid r (singletons xs) ↔ NoDescent r xs := by
  induction xs with
  | nil => simp [singletons, ColumnsValid, NoDescent]
  | cons x xs ih =>
      cases xs with
      | nil => simp [singletons, ColumnsValid, NoDescent]
      | cons y ys =>
          change ((¬ r y x ∧ True) ∧ ColumnsValid r (singletons (y :: ys))) ↔
            (¬ r y x ∧ NoDescent r (y :: ys))
          simp only [and_true, ih]

theorem columns_pair_singletons (r : Nat → Nat → Prop) (c d : Nat) (tail : List Nat) :
    ColumnsValid r ([c, d] :: singletons tail) ↔ NoDescent r (c :: tail) := by
  cases tail with
  | nil => simp [singletons, ColumnsValid, NoDescent]
  | cons z zs =>
      change ((¬ r z c ∧ True) ∧ ColumnsValid r (singletons (z :: zs))) ↔
        (¬ r z c ∧ NoDescent r (z :: zs))
      simp only [and_true, columns_singletons]

theorem bubble_noDescent (r : Nat → Nat → Prop) [DecidableRel r]
    (asym : ∀ x y, r x y → ¬ r y x) (c d : Nat) (tail : List Nat)
    (hcd : r c d) (h : NoDescent r (c :: tail)) :
    NoDescent r (c :: bubbleInsert r d tail) := by
  induction tail generalizing c with
  | nil => exact ⟨asym c d hcd, True.intro⟩
  | cons z zs ih =>
      by_cases hz : r z d
      · simp only [bubbleInsert, hz, ↓reduceIte]
        exact ⟨h.1, ih z hz h.2⟩
      · simp only [bubbleInsert, hz, ↓reduceIte]
        exact ⟨asym c d hcd, ⟨hz, h.2⟩⟩

theorem flatten_singletons (xs : List Nat) : (singletons xs).flatten = xs := by
  induction xs with
  | nil => rfl
  | cons x xs ih => simpa [singletons] using congrArg (List.cons x) ih

theorem bubble_perm (r : Nat → Nat → Prop) [DecidableRel r] (b : Nat) (tail : List Nat) :
    (bubbleInsert r b tail).Perm (b :: tail) := by
  induction tail with
  | nil => exact List.Perm.refl _
  | cons z zs ih =>
      by_cases hz : r z b
      · simp only [bubbleInsert, hz, ↓reduceIte]
        exact (List.Perm.cons z ih).trans (List.Perm.swap _ _ _)
      · simp only [bubbleInsert, hz, ↓reduceIte]
        exact List.Perm.refl _

def bubbleAfter (r : Nat → Nat → Prop) [DecidableRel r]
    (front : Rows) (c d : Nat) (tail : List Nat) : Rows :=
  front ++ ([c] :: singletons (bubbleInsert r d tail))

theorem columns_bubble_valid (r : Nat → Nat → Prop) [DecidableRel r]
    (asym : ∀ x y, r x y → ¬ r y x) (front : Rows) (c d : Nat)
    (tail : List Nat) (hcd : r c d)
    (h : ColumnsValid r (before front c d tail)) :
    ColumnsValid r (bubbleAfter r front c d tail) := by
  induction front with
  | nil =>
      change ColumnsValid r (singletons (c :: bubbleInsert r d tail))
      apply (columns_singletons r _).mpr
      apply bubble_noDescent r asym c d tail hcd
      exact (columns_pair_singletons r c d tail).mp h
  | cons upper rest ih =>
      cases rest with
      | nil => exact ⟨columnPair_shorten r upper c d h.1, ih h.2⟩
      | cons lower more => exact ⟨h.1, ih h.2⟩

theorem rows_bubble_valid (r : Nat → Nat → Prop) [DecidableRel r]
    (front : Rows) (c d : Nat) (tail : List Nat)
    (h : ∀ row ∈ before front c d tail, RowValid r row) :
    ∀ row ∈ bubbleAfter r front c d tail, RowValid r row := by
  intro row hr
  simp only [bubbleAfter, List.mem_append, List.mem_cons] at hr
  rcases hr with hp | hc | ht
  · exact h row (by simp [before, hp])
  · subst row; exact rowValid_singleton r c
  · obtain ⟨x, _, hx⟩ := List.mem_map.mp ht
    subst row
    exact rowValid_singleton r x

theorem bubble_filling_perm (r : Nat → Nat → Prop) [DecidableRel r]
    (front : Rows) (c d : Nat) (tail : List Nat) :
    (bubbleAfter r front c d tail).flatten.Perm (before front c d tail).flatten := by
  have hp := (bubble_perm r d tail).cons c
  simpa [bubbleAfter, before, flatten_singletons] using
    List.Perm.append_left front.flatten hp

/-- The corrected bubbling map always produces a genuine P-tableau. The
height-two assumption is needed for its inverse, not for its validity. -/
theorem bubble_tableau_valid (r : Nat → Nat → Prop) [DecidableRel r]
    (asym : ∀ x y, r x y → ¬ r y x) (vertices : List Nat)
    (front : Rows) (c d : Nat) (tail : List Nat)
    (h : Tableau r vertices (before front c d tail)) :
    Tableau r vertices (bubbleAfter r front c d tail) := by
  have hcd := pair_relation r front c d tail h.2.2.1
  exact ⟨h.1, (bubble_filling_perm r front c d tail).trans h.2.1,
    rows_bubble_valid r front c d tail h.2.2.1,
    columns_bubble_valid r asym front c d tail hcd h.2.2.2⟩

/-- Equal output tableaux, with the split row at the same index, recover all
input rows. The height-two assumption supplies the explicit extraction inverse. -/
theorem bubble_tableau_injective (r : Nat → Nat → Prop) [DecidableRel r]
    (height : NoThreeChain r) (vertices : List Nat)
    (front front' : Rows) (c d c' d' : Nat) (tail tail' : List Nat)
    (hlen : front.length = front'.length)
    (hsource : Tableau r vertices (before front c d tail))
    (hsource' : Tableau r vertices (before front' c' d' tail'))
    (hout : bubbleAfter r front c d tail = bubbleAfter r front' c' d' tail') :
    front = front' ∧ c = c' ∧ d = d' ∧ tail = tail' := by
  have hp := List.append_inj hout hlen
  have hs := List.cons.inj hp.2
  have hc := (List.cons.inj hs.1).1
  have ht := congrArg List.flatten hs.2
  simp only [flatten_singletons] at ht
  have hcd := pair_relation r front c d tail hsource.2.2.1
  have hcd' := pair_relation r front' c' d' tail' hsource'.2.2.1
  rw [← hc] at hcd'
  have hd := bubble_injective_height_two r height c d d' tail tail' hcd hcd' ht
  exact ⟨hp.1, hc, hd.1, hd.2⟩

/-- Weighted inversions in a word. Each ordered pair of positions contributes
`score x y`; the incomparability specialization is given below. -/
def wordWeight (score : Nat → Nat → Nat) : List Nat → Nat
  | [] => 0
  | x :: xs => (xs.map (score x)).sum + wordWeight score xs

theorem perm_nat_sum (xs ys : List Nat) (hp : xs.Perm ys) : xs.sum = ys.sum := by
  induction hp with
  | nil => rfl
  | cons x _ ih => simp only [List.sum_cons, ih]
  | swap x y rest => simp only [List.sum_cons]; omega
  | trans _ _ ih₁ ih₂ => exact ih₁.trans ih₂

theorem wordWeight_cons_congr (score : Nat → Nat → Nat) (x : Nat)
    (xs ys : List Nat) (hp : xs.Perm ys) (hw : wordWeight score xs = wordWeight score ys) :
    wordWeight score (x :: xs) = wordWeight score (x :: ys) := by
  simp only [wordWeight]
  rw [perm_nat_sum _ _ (hp.map (score x)), hw]

theorem wordWeight_append_congr (score : Nat → Nat → Nat) (front xs ys : List Nat)
    (hp : xs.Perm ys) (hw : wordWeight score xs = wordWeight score ys) :
    wordWeight score (front ++ xs) = wordWeight score (front ++ ys) := by
  induction front with
  | nil => exact hw
  | cons x rest ih =>
      exact wordWeight_cons_congr score x _ _ (hp.append_left rest) ih

theorem wordWeight_swap (score : Nat → Nat → Nat) (x y : Nat) (tail : List Nat)
    (hxy : score x y = score y x) :
    wordWeight score (x :: y :: tail) = wordWeight score (y :: x :: tail) := by
  simp only [wordWeight, List.map_cons, List.sum_cons]
  rw [hxy]
  omega

theorem bubble_wordWeight (r : Nat → Nat → Prop) [DecidableRel r]
    (score : Nat → Nat → Nat) (b : Nat) (tail : List Nat)
    (neutral : ∀ z, r z b → score z b = score b z) :
    wordWeight score (bubbleInsert r b tail) = wordWeight score (b :: tail) := by
  induction tail with
  | nil => rfl
  | cons z zs ih =>
      by_cases hz : r z b
      · simp only [bubbleInsert, hz, ↓reduceIte]
        exact (wordWeight_cons_congr score z _ _ (bubble_perm r b zs) ih).trans
          (wordWeight_swap score z b zs (neutral z hz))
      · simp only [bubbleInsert, hz, ↓reduceIte]

/-- An inversion of the incomparability graph: earlier label x exceeds later
label y, and neither strict P-comparison holds. -/
def graphScore (r : Nat → Nat → Prop) [DecidableRel r] (x y : Nat) : Nat :=
  if y < x ∧ ¬ r x y ∧ ¬ r y x then 1 else 0

def graphInversions (r : Nat → Nat → Prop) [DecidableRel r] (word : List Nat) : Nat :=
  wordWeight (graphScore r) word

theorem comparable_score_neutral (r : Nat → Nat → Prop) [DecidableRel r]
    (x y : Nat) (hxy : r x y) : graphScore r x y = graphScore r y x := by
  simp [graphScore, hxy]

/-- Every adjacent swap of P-comparable labels preserves graph inversions. -/
theorem graph_inversions_comparable_swap (r : Nat → Nat → Prop) [DecidableRel r]
    (front tail : List Nat) (x y : Nat) (hxy : r x y) :
    graphInversions r (front ++ x :: y :: tail) =
      graphInversions r (front ++ y :: x :: tail) := by
  apply wordWeight_append_congr (graphScore r) front _ _ (List.Perm.swap _ _ _)
  exact wordWeight_swap (graphScore r) x y tail (comparable_score_neutral r x y hxy)

/-- The bubbling map preserves the inversion statistic of the row-major word.
The row-based interpretation is proved below in `tableau_graph_inversions_eq_word`. -/
theorem bubble_graph_inversions (r : Nat → Nat → Prop) [DecidableRel r]
    (front : Rows) (c d : Nat) (tail : List Nat) :
    graphInversions r (bubbleAfter r front c d tail).flatten =
      graphInversions r (before front c d tail).flatten := by
  have hw := bubble_wordWeight r (graphScore r) d tail
    (fun z hz => comparable_score_neutral r z d hz)
  have hc := wordWeight_cons_congr (graphScore r) c _ _ (bubble_perm r d tail) hw
  simpa [graphInversions, bubbleAfter, before, flatten_singletons] using
    wordWeight_append_congr (graphScore r) front.flatten _ _
      ((bubble_perm r d tail).cons c) hc

def crossWeight (score : Nat → Nat → Nat) (xs ys : List Nat) : Nat :=
  (xs.map (fun x => (ys.map (score x)).sum)).sum

theorem wordWeight_append (score : Nat → Nat → Nat) (xs ys : List Nat) :
    wordWeight score (xs ++ ys) = wordWeight score xs + wordWeight score ys +
      crossWeight score xs ys := by
  induction xs with
  | nil => simp [wordWeight, crossWeight]
  | cons x xs ih =>
      simp only [List.cons_append, wordWeight, List.map_append, List.sum_append,
        crossWeight, List.map_cons, List.sum_cons] at ih ⊢
      omega

theorem sumMap_zero (xs : List Nat) (f : Nat → Nat) (h : ∀ x ∈ xs, f x = 0) :
    (xs.map f).sum = 0 := by
  induction xs with
  | nil => rfl
  | cons x xs ih =>
      simp only [List.map_cons, List.sum_cons]
      rw [h x (by simp), ih (fun y hy => h y (by simp [hy]))]

theorem chain_graph_weight_zero (r : Nat → Nat → Prop) [DecidableRel r]
    (row : List Nat) (h : row.Pairwise r) : wordWeight (graphScore r) row = 0 := by
  induction row with
  | nil => rfl
  | cons x xs ih =>
      have hp := List.pairwise_cons.mp h
      change (xs.map (graphScore r x)).sum + wordWeight (graphScore r) xs = 0
      rw [ih hp.2]
      apply Nat.add_eq_zero_iff.mpr
      exact ⟨sumMap_zero xs (graphScore r x) (fun y hy => by
        simp [graphScore, hp.1 y hy]), rfl⟩

/-- The usual tableau inversion statistic counts pairs in different rows only:
the earlier (higher) label exceeds the later (lower) label and is incomparable. -/
def tableauGraphInversions (r : Nat → Nat → Prop) [DecidableRel r] : Rows → Nat
  | [] => 0
  | row :: rest => crossWeight (graphScore r) row rest.flatten +
      tableauGraphInversions r rest

theorem tableau_graph_inversions_eq_word (r : Nat → Nat → Prop) [DecidableRel r]
    (rows : Rows) (h : ∀ row ∈ rows, row.Pairwise r) :
    tableauGraphInversions r rows = graphInversions r rows.flatten := by
  induction rows with
  | nil => rfl
  | cons row rest ih =>
      have hr := h row (by simp)
      have ht : ∀ x ∈ rest, x.Pairwise r := fun x hx => h x (by simp [hx])
      have hw := wordWeight_append (graphScore r) row rest.flatten
      rw [chain_graph_weight_zero r row hr] at hw
      simp only [tableauGraphInversions, List.flatten_cons, graphInversions] at ih ⊢
      rw [ih ht, hw]
      omega

/-- Weight preservation for the actual row-based P-tableau statistic. -/
theorem bubble_tableau_graph_inversions (r : Nat → Nat → Prop) [DecidableRel r]
    (asym : ∀ x y, r x y → ¬ r y x) (vertices : List Nat)
    (front : Rows) (c d : Nat) (tail : List Nat)
    (h : Tableau r vertices (before front c d tail)) :
    tableauGraphInversions r (bubbleAfter r front c d tail) =
      tableauGraphInversions r (before front c d tail) := by
  have hb := bubble_tableau_valid r asym vertices front c d tail h
  rw [tableau_graph_inversions_eq_word r _ (fun row hr => (hb.2.2.1 row hr).2),
    tableau_graph_inversions_eq_word r _ (fun row hr => (h.2.2.1 row hr).2)]
  exact bubble_graph_inversions r front c d tail

/-- A second valid source for the explicit failure of injectivity at height > 2. -/
theorem collision_source_other :
    Tableau fiveOrder [1, 2, 3, 4, 5] [[1, 2], [3, 4], [5]] := by
  simp [Tableau, ShapeAndOrder, RowValid, ColumnsValid, ColumnPair, fiveOrder]

instance : DecidableRel fiveOrder := fun x y => inferInstanceAs (Decidable (x < y))

theorem collision_without_height_two :
    bubbleAfter fiveOrder [[1, 2]] 3 4 [5] =
      bubbleAfter fiveOrder [[1, 2]] 3 5 [4] ∧
    before [[1, 2]] 3 4 [5] ≠ before [[1, 2]] 3 5 [4] := by
  decide

theorem collision_common_image :
    bubbleAfter fiveOrder [[1, 2]] 3 4 [5] = [[1, 2], [3], [4], [5]] := by
  rfl

end CornerSlide

#print axioms CornerSlide.demote_valid_iff
#print axioms CornerSlide.flatten_before_after
#print axioms CornerSlide.word_statistic_preserved
#print axioms CornerSlide.counterexample_source
#print axioms CornerSlide.counterexample_target_invalid
#print axioms CornerSlide.demote_bottom_row_valid
#print axioms CornerSlide.extract_bubble_inverse_height_two
#print axioms CornerSlide.bubble_injective_height_two
#print axioms CornerSlide.bubble_noDescent
#print axioms CornerSlide.bubble_tableau_valid
#print axioms CornerSlide.bubble_tableau_injective
#print axioms CornerSlide.graph_inversions_comparable_swap
#print axioms CornerSlide.bubble_graph_inversions
#print axioms CornerSlide.tableau_graph_inversions_eq_word
#print axioms CornerSlide.bubble_tableau_graph_inversions
#print axioms CornerSlide.collision_source_other
#print axioms CornerSlide.collision_without_height_two
