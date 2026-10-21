import TableauFamilies

/-!
Degreewise counting for complete finite tableau families. All identities use
addition of natural counts. There is no assumed polynomial-coefficient bridge.
-/

namespace CornerSlide

def degreeCount {α : Type} (weight : α → Nat) (degree : Nat) (xs : List α) : Nat :=
  (xs.filter (fun x => weight x == degree)).length

theorem degreeCount_perm {α : Type} (weight : α → Nat) (degree : Nat)
    {xs ys : List α} (hp : xs.Perm ys) :
    degreeCount weight degree xs = degreeCount weight degree ys := by
  exact (hp.filter (fun x => weight x == degree)).length_eq

theorem degreeCount_partition {α : Type} (weight : α → Nat) (degree : Nat)
    (p : α → Bool) (xs : List α) :
    degreeCount weight degree xs = degreeCount weight degree (xs.filter p) +
      degreeCount weight degree (xs.filter (fun x => !(p x))) := by
  induction xs with
  | nil => simp [degreeCount]
  | cons x xs ih =>
      cases hp : p x <;> by_cases hw : weight x = degree <;>
        simp [degreeCount, hp, hw] at ih ⊢ <;> omega

theorem map_nodup_on {α β : Type} (f : α → β) (xs : List α)
    (hn : xs.Nodup)
    (hi : ∀ x ∈ xs, ∀ y ∈ xs, f x = f y → x = y) : (xs.map f).Nodup := by
  induction xs with
  | nil => simp
  | cons x xs ih =>
      have hh := List.nodup_cons.mp hn
      apply List.nodup_cons.mpr
      constructor
      · intro hm
        obtain ⟨y, hy, he⟩ := List.mem_map.mp hm
        have hxy := hi x (by simp) y (by simp [hy]) he.symm
        exact hh.1 (hxy ▸ hy)
      · exact ih hh.2 (fun a ha b hb => hi a (by simp [ha]) b (by simp [hb]))

theorem degreeCount_map {α β : Type} (f : α → β)
    (sourceWeight : α → Nat) (targetWeight : β → Nat) (degree : Nat)
    (xs : List α) (hw : ∀ x ∈ xs, targetWeight (f x) = sourceWeight x) :
    degreeCount targetWeight degree (xs.map f) = degreeCount sourceWeight degree xs := by
  induction xs with
  | nil => rfl
  | cons x xs ih =>
      have ht := ih (fun y hy => hw y (by simp [hy]))
      have hx := hw x (by simp)
      by_cases hd : sourceWeight x = degree <;>
        simp [degreeCount, hx, hd] at ht ⊢ <;> exact ht

/-- A finite injection decomposes the target, degree by degree, into its image
and the complement of its full image. The caller supplies actual lists; the
tableau corollary below proves completeness of those lists. -/
theorem degreewise_cancellation {α β : Type} [BEq β] [LawfulBEq β]
    (source : List α) (target : List β) (f : α → β)
    (sourceWeight : α → Nat) (targetWeight : β → Nat)
    (sourceNodup : source.Nodup) (targetNodup : target.Nodup)
    (maps : ∀ x ∈ source, f x ∈ target)
    (injective : ∀ x ∈ source, ∀ y ∈ source, f x = f y → x = y)
    (preserves : ∀ x ∈ source, targetWeight (f x) = sourceWeight x)
    (degree : Nat) :
    degreeCount targetWeight degree target = degreeCount sourceWeight degree source +
      degreeCount targetWeight degree
        (target.filter (fun y => decide (y ∉ source.map f))) := by
  let image := source.map f
  have hn : image.Nodup := map_nodup_on f source sourceNodup injective
  have hf : (target.filter (fun y => decide (y ∈ image))).Perm image := by
    apply (List.perm_ext_iff_of_nodup (targetNodup.filter _) hn).mpr
    intro y
    simp only [List.mem_filter, decide_eq_true_eq]
    constructor
    · exact And.right
    · intro hy
      obtain ⟨x, hx, he⟩ := List.mem_map.mp hy
      exact ⟨he ▸ maps x hx, hy⟩
  have hp := degreeCount_partition targetWeight degree
    (fun y => decide (y ∈ image)) target
  rw [degreeCount_perm targetWeight degree hf,
    degreeCount_map f sourceWeight targetWeight degree source preserves] at hp
  simpa [image] using hp

/-- The degreewise identity for every complete two-column source family.
The total number of vertices is enforced by the actual filling predicate. -/
theorem two_column_degreewise_cancellation
    (r : Nat → Nat → Prop) [DecidableRel r]
    (asym : ∀ x y, r x y → ¬ r y x) (height : NoThreeChain r)
    (vertices : List Nat) (k m degree : Nat) :
    degreeCount (tableauGraphInversions r) degree
      (family r vertices (twoColumnShape k (m + 2))) =
    degreeCount (tableauGraphInversions r) degree
      (family r vertices (twoColumnShape (k + 1) m)) +
    degreeCount (tableauGraphInversions r) degree
      ((family r vertices (twoColumnShape k (m + 2))).filter
        (fun rows => decide (rows ∉ (family r vertices (twoColumnShape (k + 1) m)).map
          (bubbleAt r k)))) := by
  classical
  exact degreewise_cancellation _ _ (bubbleAt r k)
    (tableauGraphInversions r) (tableauGraphInversions r)
    (family_nodup r vertices _) (family_nodup r vertices _)
    (fun rows h => bubbleAt_family r asym vertices k m rows h)
    (fun rows h rows' h' he =>
      bubbleAt_family_injective r height vertices k m rows rows' h h' he)
    (fun rows h => bubbleAt_family_weight r asym vertices k m rows h) degree

/-- Guard the shape parameter before taking a natural-number difference. -/
noncomputable def columnFamily (r : Nat → Nat → Prop) (vertices : List Nat)
    (k : Nat) : List Rows :=
  if 2 * k ≤ vertices.length then
    family r vertices (twoColumnShape k (vertices.length - 2 * k)) else []

theorem columnFamily_nodup (r : Nat → Nat → Prop) (vertices : List Nat) (k : Nat) :
    (columnFamily r vertices k).Nodup := by
  unfold columnFamily
  split
  · exact family_nodup r vertices _
  · simp

theorem columnFamily_out_of_range (r : Nat → Nat → Prop) (vertices : List Nat)
    (k : Nat) (h : vertices.length < 2 * k) : columnFamily r vertices k = [] := by
  simp [columnFamily, Nat.not_le.mpr h]

theorem mem_columnFamily (r : Nat → Nat → Prop) (vertices : List Nat)
    (k : Nat) (rows : Rows) :
    rows ∈ columnFamily r vertices k ↔ 2 * k ≤ vertices.length ∧
      Tableau r vertices rows ∧
      rows.map List.length = twoColumnShape k (vertices.length - 2 * k) := by
  by_cases h : 2 * k ≤ vertices.length
  · simp [columnFamily, h, mem_family]
  · simp [columnFamily, h]

noncomputable def survivorFamily (r : Nat → Nat → Prop) [DecidableRel r]
    (vertices : List Nat) (k : Nat) : List Rows := by
  classical
  exact (columnFamily r vertices k).filter
    (fun rows => decide (rows ∉ (columnFamily r vertices (k + 1)).map (bubbleAt r k)))

theorem mem_survivorFamily (r : Nat → Nat → Prop) [DecidableRel r]
    (vertices : List Nat) (k : Nat) (rows : Rows) :
    rows ∈ survivorFamily r vertices k ↔ rows ∈ columnFamily r vertices k ∧
      rows ∉ (columnFamily r vertices (k + 1)).map (bubbleAt r k) := by
  classical
  simp [survivorFamily]

theorem survivorFamily_nodup (r : Nat → Nat → Prop) [DecidableRel r]
    (vertices : List Nat) (k : Nat) : (survivorFamily r vertices k).Nodup := by
  classical
  exact (columnFamily_nodup r vertices k).filter _

theorem survivorFamily_empty_source (r : Nat → Nat → Prop) [DecidableRel r]
    (vertices : List Nat) (k : Nat) (h : vertices.length < 2 * (k + 1)) :
    survivorFamily r vertices k = columnFamily r vertices k := by
  classical
  simp [survivorFamily, columnFamily_out_of_range r vertices (k + 1) h]

theorem columnFamily_empty_vertices (r : Nat → Nat → Prop) :
    columnFamily r [] 0 = [[]] := by
  classical
  have ht : Tableau r [] [] := by
    simp [Tableau, ShapeAndOrder, ColumnsValid]
  simp [columnFamily, twoColumnShape, family, fillings, ht, unique]

theorem columnFamily_single_vertex (r : Nat → Nat → Prop) (x : Nat) :
    columnFamily r [x] 0 = [[[x]]] := by
  classical
  have ht : Tableau r [x] [[x]] := by
    simp [Tableau, ShapeAndOrder, RowValid, ColumnsValid]
  simp [columnFamily, twoColumnShape, family, fillings, words, ht, unique]

theorem empty_vertex_degree_count (r : Nat → Nat → Prop) [DecidableRel r]
    (degree : Nat) :
    degreeCount (tableauGraphInversions r) degree (columnFamily r [] 0) =
      if degree = 0 then 1 else 0 := by
  rw [columnFamily_empty_vertices]
  by_cases hd : degree = 0
  · subst degree; simp [degreeCount, tableauGraphInversions]
  · simp [degreeCount, tableauGraphInversions, hd, Ne.symm hd]

theorem single_vertex_degree_count (r : Nat → Nat → Prop) [DecidableRel r]
    (x degree : Nat) :
    degreeCount (tableauGraphInversions r) degree (columnFamily r [x] 0) =
      if degree = 0 then 1 else 0 := by
  rw [columnFamily_single_vertex]
  by_cases hd : degree = 0
  · subst degree; simp [degreeCount, tableauGraphInversions, crossWeight]
  · simp [degreeCount, tableauGraphInversions, crossWeight, hd, Ne.symm hd]

/-- The requested all-index height-two identity. Empty next families, including
odd and even maximal indices, are handled by the guard, not by extraction. -/
theorem height_two_degreewise_cancellation
    (r : Nat → Nat → Prop) [DecidableRel r]
    (asym : ∀ x y, r x y → ¬ r y x) (height : NoThreeChain r)
    (vertices : List Nat) (k degree : Nat) :
    degreeCount (tableauGraphInversions r) degree (columnFamily r vertices k) =
      degreeCount (tableauGraphInversions r) degree (columnFamily r vertices (k + 1)) +
      degreeCount (tableauGraphInversions r) degree (survivorFamily r vertices k) := by
  classical
  by_cases hs : 2 * (k + 1) ≤ vertices.length
  · have ht : 2 * k ≤ vertices.length := by omega
    have he : vertices.length - 2 * k = (vertices.length - 2 * (k + 1)) + 2 := by omega
    simpa only [survivorFamily, columnFamily, hs, ht, ↓reduceIte, he] using
      two_column_degreewise_cancellation r asym height vertices k
        (vertices.length - 2 * (k + 1)) degree
  · simp [survivorFamily, columnFamily, hs, degreeCount]

/-- Extending a finite-vertex relation by false outside the vertex set turns
the finite height hypothesis into exactly the global hypothesis used above. -/
def finiteRelation (vertices : List Nat) (base : Nat → Nat → Prop) (x y : Nat) : Prop :=
  x ∈ vertices ∧ y ∈ vertices ∧ base x y

instance (vertices : List Nat) (base : Nat → Nat → Prop) [DecidableRel base] :
    DecidableRel (finiteRelation vertices base) := fun x y =>
  inferInstanceAs (Decidable (x ∈ vertices ∧ y ∈ vertices ∧ base x y))

theorem finiteRelation_on_vertices (vertices : List Nat) (base : Nat → Nat → Prop)
    (x y : Nat) (hx : x ∈ vertices) (hy : y ∈ vertices) :
    finiteRelation vertices base x y ↔ base x y := by
  simp [finiteRelation, hx, hy]

theorem finiteRelation_height (vertices : List Nat) (base : Nat → Nat → Prop)
    (height : ∀ x ∈ vertices, ∀ y ∈ vertices, ∀ z ∈ vertices,
      base x y → base y z → False) : NoThreeChain (finiteRelation vertices base) := by
  intro x y z hxy hyz
  exact height x hxy.1 y hxy.2.1 z hyz.2.1 hxy.2.2 hyz.2.2

theorem finiteRelation_asym (vertices : List Nat) (base : Nat → Nat → Prop)
    (asym : ∀ x ∈ vertices, ∀ y ∈ vertices, base x y → ¬ base y x) :
    ∀ x y, finiteRelation vertices base x y → ¬ finiteRelation vertices base y x := by
  intro x y hxy hyx
  exact asym x hxy.1 y hxy.2.1 hxy.2.2 hyx.2.2

/-- Finite posets need height and asymmetry only on their actual vertex set. -/
theorem finite_height_two_degreewise_cancellation
    (vertices : List Nat) (base : Nat → Nat → Prop) [DecidableRel base]
    (asym : ∀ x ∈ vertices, ∀ y ∈ vertices, base x y → ¬ base y x)
    (height : ∀ x ∈ vertices, ∀ y ∈ vertices, ∀ z ∈ vertices,
      base x y → base y z → False) (k degree : Nat) :
    let r := finiteRelation vertices base
    degreeCount (tableauGraphInversions r) degree (columnFamily r vertices k) =
      degreeCount (tableauGraphInversions r) degree (columnFamily r vertices (k + 1)) +
      degreeCount (tableauGraphInversions r) degree (survivorFamily r vertices k) := by
  exact height_two_degreewise_cancellation (finiteRelation vertices base)
    (finiteRelation_asym vertices base asym) (finiteRelation_height vertices base height)
    vertices k degree

end CornerSlide

#print axioms CornerSlide.degreewise_cancellation
#print axioms CornerSlide.two_column_degreewise_cancellation
#print axioms CornerSlide.height_two_degreewise_cancellation
#print axioms CornerSlide.finiteRelation_height
#print axioms CornerSlide.finite_height_two_degreewise_cancellation
#print axioms CornerSlide.mem_survivorFamily
#print axioms CornerSlide.empty_vertex_degree_count
#print axioms CornerSlide.single_vertex_degree_count
#print axioms CornerSlide.survivorFamily_empty_source
