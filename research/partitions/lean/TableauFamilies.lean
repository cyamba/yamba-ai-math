import CornerSlide

/-!
Complete finite families of actual tableaux. The enumerator ranges over all
fillings from a fixed finite vertex list, then checks actual tableau validity.
No completeness hypothesis is supplied by a caller.
-/

namespace CornerSlide

def words (vertices : List Nat) : Nat → List (List Nat)
  | 0 => [[]]
  | n + 1 => vertices.flatMap (fun x => (words vertices n).map (x :: ·))

theorem mem_words (vertices xs : List Nat) (n : Nat) :
    xs ∈ words vertices n ↔ xs.length = n ∧ ∀ x ∈ xs, x ∈ vertices := by
  induction n generalizing xs with
  | zero => cases xs <;> simp [words]
  | succ n ih =>
      cases xs with
      | nil => simp [words]
      | cons x xs =>
          simp only [words, List.mem_flatMap, List.mem_map]
          constructor
          · rintro ⟨y, hy, ys, hys, he⟩
            have hpair := List.cons.inj he
            rcases hpair with ⟨rfl, rfl⟩
            obtain ⟨hlen, hmem⟩ := (ih ys).mp hys
            exact ⟨by simp [hlen], fun z hz => by
              rcases List.mem_cons.mp hz with rfl | hz
              · exact hy
              · exact hmem z hz⟩
          · rintro ⟨hlen, hmem⟩
            refine ⟨x, hmem x (by simp), xs, ?_, rfl⟩
            apply (ih xs).mpr
            exact ⟨by simpa using hlen, fun z hz => hmem z (by simp [hz])⟩

def fillings (vertices : List Nat) : List Nat → List Rows
  | [] => [[]]
  | size :: shape => (words vertices size).flatMap
      (fun row => (fillings vertices shape).map (row :: ·))

theorem mem_fillings (vertices : List Nat) (shape : List Nat) (rows : Rows) :
    rows ∈ fillings vertices shape ↔
      rows.map List.length = shape ∧ ∀ x ∈ rows.flatten, x ∈ vertices := by
  induction shape generalizing rows with
  | nil => cases rows <;> simp [fillings]
  | cons size shape ih =>
      cases rows with
      | nil => simp [fillings]
      | cons row rows =>
          simp only [fillings, List.mem_flatMap, List.mem_map]
          constructor
          · rintro ⟨a, ha, rest, hrest, he⟩
            have hpair := List.cons.inj he
            rcases hpair with ⟨rfl, rfl⟩
            obtain ⟨hlen, hm⟩ := (mem_words vertices a size).mp ha
            obtain ⟨hs, hr⟩ := (ih rest).mp hrest
            refine ⟨by simp [hlen, hs], ?_⟩
            intro x hx
            rcases List.mem_append.mp hx with hx | hx
            · exact hm x hx
            · exact hr x hx
          · rintro ⟨hs, hm⟩
            have hpair := List.cons.inj hs
            refine ⟨row, (mem_words vertices row size).mpr ⟨hpair.1, ?_⟩,
              rows, (ih rows).mpr ⟨hpair.2, ?_⟩, rfl⟩
            · intro x hx; exact hm x (by simp [hx])
            · intro x hx; exact hm x (by simp [hx])

def unique {α : Type} [DecidableEq α] : List α → List α
  | [] => []
  | x :: xs => if x ∈ xs then unique xs else x :: unique xs

theorem mem_unique {α : Type} [DecidableEq α] (xs : List α) (x : α) :
    x ∈ unique xs ↔ x ∈ xs := by
  induction xs with
  | nil => simp [unique]
  | cons y ys ih =>
      by_cases hy : y ∈ ys
      · simp only [unique, hy, ↓reduceIte, ih]
        simp only [List.mem_cons]
        constructor
        · exact Or.inr
        · rintro (rfl | hx)
          · exact hy
          · exact hx
      · simp [unique, hy, ih]

theorem unique_nodup {α : Type} [DecidableEq α] (xs : List α) :
    (unique xs).Nodup := by
  induction xs with
  | nil => simp [unique]
  | cons x xs ih =>
      by_cases hx : x ∈ xs
      · simpa [unique, hx] using ih
      · simp only [unique, hx, ↓reduceIte]
        exact List.nodup_cons.mpr ⟨fun hm => hx ((mem_unique xs x).mp hm), ih⟩

noncomputable def family (r : Nat → Nat → Prop) (vertices : List Nat)
    (shape : List Nat) : List Rows := by
  classical
  exact unique ((fillings vertices shape).filter (fun rows => decide (Tableau r vertices rows)))

/-- Membership is equivalent to the complete intended mathematical predicate. -/
theorem mem_family (r : Nat → Nat → Prop) (vertices : List Nat)
    (shape : List Nat) (rows : Rows) :
    rows ∈ family r vertices shape ↔
      Tableau r vertices rows ∧ rows.map List.length = shape := by
  classical
  simp only [family, mem_unique, List.mem_filter, decide_eq_true_eq, mem_fillings]
  constructor
  · rintro ⟨⟨hshape, _⟩, ht⟩; exact ⟨ht, hshape⟩
  · rintro ⟨ht, hshape⟩
    exact ⟨⟨hshape, fun x hx => ht.2.1.mem_iff.mp hx⟩, ht⟩

theorem family_nodup (r : Nat → Nat → Prop) (vertices shape : List Nat) :
    (family r vertices shape).Nodup := by
  classical
  exact unique_nodup _

def twoColumnShape (pairs singles : Nat) : List Nat :=
  List.replicate pairs 2 ++ List.replicate singles 1

theorem shape_singletons (tail : List Nat) :
    (singletons tail).map List.length = List.replicate tail.length 1 := by
  induction tail with
  | nil => rfl
  | cons x xs ih => simpa [singletons, List.replicate_succ] using congrArg (List.cons 1) ih

theorem singleton_decomposition (rows : Rows) (m : Nat)
    (hs : rows.map List.length = List.replicate m 1) :
    ∃ tail, tail.length = m ∧ rows = singletons tail := by
  induction m generalizing rows with
  | zero =>
      have he : rows = [] := by simpa using hs
      subst rows
      exact ⟨[], rfl, rfl⟩
  | succ m ih =>
      cases rows with
      | nil => simp at hs
      | cons row rest =>
          have hh := List.cons.inj hs
          obtain ⟨x, hx⟩ := List.length_eq_one_iff.mp hh.1
          obtain ⟨tail, hlen, he⟩ := ih rest hh.2
          subst row
          subst rest
          exact ⟨x :: tail, by simp [hlen], rfl⟩

theorem pair_decomposition (rows : Rows) (k m : Nat)
    (hs : rows.map List.length = twoColumnShape (k + 1) m) :
    ∃ front c d tail, front.length = k ∧
      front.map List.length = List.replicate k 2 ∧ tail.length = m ∧
      rows = before front c d tail := by
  induction k generalizing rows with
  | zero =>
      cases rows with
      | nil => simp [twoColumnShape] at hs
      | cons row rest =>
          have hh : row.length = 2 ∧ rest.map List.length = List.replicate m 1 := by
            simpa [twoColumnShape] using hs
          have he := List.eq_getElem_of_length_eq_two row hh.1
          obtain ⟨tail, hlen, ht⟩ := singleton_decomposition rest m hh.2
          refine ⟨[], row[0]'(by omega), row[1]'(by omega), tail, rfl, rfl, hlen, ?_⟩
          change row :: rest = [row[0]'(by omega), row[1]'(by omega)] :: singletons tail
          exact congr (congrArg List.cons he) ht
  | succ k ih =>
      cases rows with
      | nil => simp [twoColumnShape] at hs
      | cons row rest =>
          have hh : row.length = 2 ∧ rest.map List.length = twoColumnShape (k + 1) m := by
            simpa [twoColumnShape, List.replicate_succ] using hs
          obtain ⟨front, c, d, tail, hlen, hshape, htail, he⟩ := ih rest hh.2
          refine ⟨row :: front, c, d, tail, by simp [hlen], ?_, htail, ?_⟩
          · simp [hh.1, hshape, List.replicate_succ]
          · simp [before, he]

def bubbleAt (r : Nat → Nat → Prop) [DecidableRel r] : Nat → Rows → Rows
  | 0, [c, d] :: rest => [c] :: singletons (bubbleInsert r d rest.flatten)
  | k + 1, row :: rest => row :: bubbleAt r k rest
  | _, rows => rows

theorem bubbleAt_before (r : Nat → Nat → Prop) [DecidableRel r]
    (front : Rows) (c d : Nat) (tail : List Nat) :
    bubbleAt r front.length (before front c d tail) = bubbleAfter r front c d tail := by
  induction front with
  | nil => simp [bubbleAt, before, bubbleAfter, flatten_singletons]
  | cons row front ih => simpa [before, bubbleAfter, bubbleAt] using congrArg (List.cons row) ih

theorem bubbleAt_family (r : Nat → Nat → Prop) [DecidableRel r]
    (asym : ∀ x y, r x y → ¬ r y x) (vertices : List Nat) (k m : Nat)
    (rows : Rows) (h : rows ∈ family r vertices (twoColumnShape (k + 1) m)) :
    bubbleAt r k rows ∈ family r vertices (twoColumnShape k (m + 2)) := by
  have ht := (mem_family r vertices _ rows).mp h
  obtain ⟨front, c, d, tail, hlen, hshape, htail, he⟩ := pair_decomposition rows k m ht.2
  subst rows
  rw [← hlen, bubbleAt_before]
  apply (mem_family r vertices _ _).mpr
  refine ⟨bubble_tableau_valid r asym vertices front c d tail ht.1, ?_⟩
  have hb := (bubble_perm r d tail).length_eq
  simp only [List.length_cons, htail] at hb
  simp [bubbleAfter, shape_singletons, hshape, twoColumnShape, hb, hlen,
    List.replicate_succ]

theorem bubbleAt_family_injective (r : Nat → Nat → Prop) [DecidableRel r]
    (height : NoThreeChain r) (vertices : List Nat) (k m : Nat)
    (rows rows' : Rows)
    (h : rows ∈ family r vertices (twoColumnShape (k + 1) m))
    (h' : rows' ∈ family r vertices (twoColumnShape (k + 1) m))
    (he : bubbleAt r k rows = bubbleAt r k rows') : rows = rows' := by
  have ht := (mem_family r vertices _ rows).mp h
  have ht' := (mem_family r vertices _ rows').mp h'
  obtain ⟨front, c, d, tail, hlen, _, _, hr⟩ := pair_decomposition rows k m ht.2
  obtain ⟨front', c', d', tail', hlen', _, _, hr'⟩ := pair_decomposition rows' k m ht'.2
  subst rows
  subst rows'
  have hb : bubbleAfter r front c d tail = bubbleAfter r front' c' d' tail' := by
    rw [← bubbleAt_before, ← bubbleAt_before, hlen, hlen']
    exact he
  obtain ⟨hf, hc, hd, htail⟩ := bubble_tableau_injective r height vertices
    front front' c d c' d' tail tail' (by omega) ht.1 ht'.1 hb
  simp [hf, hc, hd, htail]

theorem bubbleAt_family_weight (r : Nat → Nat → Prop) [DecidableRel r]
    (asym : ∀ x y, r x y → ¬ r y x) (vertices : List Nat) (k m : Nat)
    (rows : Rows) (h : rows ∈ family r vertices (twoColumnShape (k + 1) m)) :
    tableauGraphInversions r (bubbleAt r k rows) = tableauGraphInversions r rows := by
  have ht := (mem_family r vertices _ rows).mp h
  obtain ⟨front, c, d, tail, hlen, _, _, hr⟩ := pair_decomposition rows k m ht.2
  subst rows
  rw [← hlen, bubbleAt_before]
  exact bubble_tableau_graph_inversions r asym vertices front c d tail ht.1

end CornerSlide

#print axioms CornerSlide.mem_family
#print axioms CornerSlide.family_nodup
#print axioms CornerSlide.bubbleAt_family
#print axioms CornerSlide.bubbleAt_family_injective
#print axioms CornerSlide.bubbleAt_family_weight
