import PartitionH3.Coloring
import PartitionH3.PermutationSign
import PartitionH3.SignedCancellation
import Mathlib.Data.List.FinRange
import Mathlib.Data.Finset.Sort

/-! Actual color classes, including empty classes, form the rows of a labelled
signed array. The converse uses the unique row containing each actual vertex.
No coloring expansion is assumed. -/

noncomputable section

namespace PartitionH3

attribute [local instance] Classical.propDecidable

def colorRow {n m : ℕ} (κ : Fin n → Fin m) (c : Fin m) : List ℕ :=
  ((colorClass κ c).image Fin.val).sort

theorem mem_colorRow {n m : ℕ} (κ : Fin n → Fin m) (c : Fin m) (v : ℕ) :
    v ∈ colorRow κ c ↔ ∃ h : v < n, κ ⟨v, h⟩ = c := by
  simp only [colorRow, Finset.mem_sort, Finset.mem_image]
  constructor
  · rintro ⟨x, hx, rfl⟩
    exact ⟨x.isLt, (Finset.mem_filter.mp hx).2⟩
  · rintro ⟨hv, hc⟩
    exact ⟨⟨v, hv⟩, Finset.mem_filter.mpr ⟨Finset.mem_univ _, hc⟩, rfl⟩

theorem colorRow_length {n m : ℕ} (κ : Fin n → Fin m) (c : Fin m) :
    (colorRow κ c).length = (colorClass κ c).card := by
  simp only [colorRow, Finset.length_sort,
    Finset.card_image_of_injective _ Fin.val_injective]

theorem colorRow_sorted {n m : ℕ} (κ : Fin n → Fin m) (c : Fin m) :
    (colorRow κ c).Pairwise (· < ·) :=
  (Finset.sortedLT_sort _).pairwise

theorem colorRow_chain {n m : ℕ} (H : NaturalUnitInterval n)
    (κ : Fin n → Fin m) (hp : Proper H κ) (c : Fin m) :
    (colorRow κ c).Pairwise (natLt H) := by
  apply List.Pairwise.imp_of_mem (p := colorRow_sorted κ c)
  intro x y hx hy hxy
  obtain ⟨hx, hxc⟩ := (mem_colorRow κ c x).mp hx
  obtain ⟨hy, hyc⟩ := (mem_colorRow κ c y).mp hy
  have h := same_color_comparable H κ hp (show (⟨x, hx⟩ : Fin n) < ⟨y, hy⟩ from hxy)
    (hxc.trans hyc.symm)
  simpa only [natLt, dite_eq_left hx, dite_eq_left hy] using h

def colorArray {n m : ℕ} (κ : Fin n → Fin m) (sigma : Equiv.Perm (Fin m)) :
    SignedArrays.Array :=
  List.ofFn (fun c => ((sigma c).val, colorRow κ c))

theorem colorArray_length {n m : ℕ} (κ : Fin n → Fin m) (sigma : Equiv.Perm (Fin m)) :
    (colorArray κ sigma).length = m := by simp [colorArray]

theorem colorArray_labels {n m : ℕ} (κ : Fin n → Fin m) (sigma : Equiv.Perm (Fin m)) :
    SignedArrays.labels (colorArray κ sigma) = permutationLabels sigma := by
  simp [SignedArrays.labels, colorArray, permutationLabels, List.map_ofFn, Function.comp_def]

theorem colorArray_rows {n m : ℕ} (κ : Fin n → Fin m) (sigma : Equiv.Perm (Fin m)) :
    SignedArrays.rows (colorArray κ sigma) = List.ofFn (colorRow κ) := by
  simp [SignedArrays.rows, colorArray, List.map_ofFn, Function.comp_def]

theorem colorArray_sign {n m : ℕ} (κ : Fin n → Fin m) (sigma : Equiv.Perm (Fin m)) :
    SignedArrays.permutationSign (SignedArrays.labels (colorArray κ sigma)) =
      (Equiv.Perm.sign sigma : ℤ) := by
  rw [colorArray_labels, permutationSign_permutationLabels]

theorem colorRows_disjoint {n m : ℕ} (κ : Fin n → Fin m) {c d : Fin m} (hcd : c ≠ d) :
    List.Disjoint (colorRow κ c) (colorRow κ d) := by
  intro v hvc hvd
  obtain ⟨hv, hc⟩ := (mem_colorRow κ c v).mp hvc
  obtain ⟨_, hd⟩ := (mem_colorRow κ d v).mp hvd
  exact hcd (hc.symm.trans hd)

theorem colorRows_contents {n m : ℕ} (κ : Fin n → Fin m) :
    (List.ofFn (colorRow κ)).flatten.Perm (List.range n) := by
  have hn : (List.ofFn (colorRow κ)).flatten.Nodup := by
    apply List.nodup_flatten.mpr
    constructor
    · intro row hr
      obtain ⟨c, rfl⟩ := List.mem_ofFn.mp hr
      exact Finset.sort_nodup _ _
    · apply List.pairwise_iff_getElem.mpr
      intro i j hi hj hij
      simp only [List.getElem_ofFn]
      apply colorRows_disjoint
      intro he
      have hv := congrArg Fin.val he
      simp only at hv
      omega
  apply (List.perm_ext_iff_of_nodup hn List.nodup_range).mpr
  intro v
  simp only [List.mem_flatten, List.mem_ofFn, List.mem_range]
  constructor
  · rintro ⟨row, ⟨c, rfl⟩, hv⟩
    exact ((mem_colorRow κ c v).mp hv).1
  · intro hv
    exact ⟨colorRow κ (κ ⟨v, hv⟩), ⟨κ ⟨v, hv⟩, rfl⟩,
      (mem_colorRow κ _ v).mpr ⟨hv, rfl⟩⟩

theorem colorArray_chain {n m : ℕ} (H : NaturalUnitInterval n)
    (κ : Fin n → Fin m) (hp : Proper H κ) (sigma : Equiv.Perm (Fin m)) :
    SignedArrays.ChainArray (natLt H) (List.range n) (colorArray κ sigma) := by
  refine ⟨List.nodup_range, ?_, ?_⟩
  · simpa only [SignedArrays.contents, colorArray_rows] using colorRows_contents κ
  · intro entry he
    obtain ⟨c, rfl⟩ := List.mem_ofFn.mp he
    exact colorRow_chain H κ hp c

theorem shapeAt_iff_get (lambda : ℕ → ℕ) (a : SignedArrays.Array) (start : ℤ) :
    SignedArrays.ShapeAt lambda start a ↔
      ∀ i : Fin a.length, ((a[i.val]).2.length : ℤ) =
        SignedArrays.shiftKey lambda (a[i.val]).1 + (start + (i.val : ℤ)) := by
  induction a generalizing start with
  | nil => simp [SignedArrays.ShapeAt]
  | cons entry tail ih =>
      cases entry with
      | mk p row =>
          simp only [SignedArrays.ShapeAt, ih, List.length_cons, Fin.forall_fin_succ,
            List.getElem_cons_zero, List.getElem_cons_succ, Fin.val_zero, Fin.val_succ,
            Nat.cast_zero, Nat.cast_add, Nat.cast_one, add_zero]
          constructor <;> rintro ⟨h0, ht⟩ <;> refine ⟨h0, ?_⟩ <;>
            intro i <;> have := ht i <;> omega

theorem colorArray_signed_iff {n m : ℕ} (H : NaturalUnitInterval n)
    (κ : Fin n → Fin m) (hp : Proper H κ) (sigma : Equiv.Perm (Fin m))
    (lambda : ℕ → ℕ) :
    SignedArrays.SignedArray (natLt H) (List.range n) lambda (colorArray κ sigma) ↔
      ∀ i, ((colorClass κ i).card : ℤ) =
        (lambda (sigma i).val : ℤ) - ((sigma i).val : ℤ) + (i.val : ℤ) := by
  have hl : (SignedArrays.labels (colorArray κ sigma)).Perm (List.range (colorArray κ sigma).length) := by
    rw [colorArray_labels, colorArray_length]
    have hs := sigma.ofFn_comp_perm (fun i => i.val)
    have he : List.ofFn (fun i : Fin m => i.val) = List.range m := by
      simpa [permutationLabels] using permutationLabels_one m
    simpa only [permutationLabels, Function.comp_def, he] using hs
  constructor
  · intro ha i
    have hs := (shapeAt_iff_get lambda (colorArray κ sigma) 0).mp ha.2.1
      ⟨i.val, by simpa only [colorArray_length] using i.isLt⟩
    simpa only [colorArray, List.getElem_ofFn, colorRow_length,
      SignedArrays.shiftKey, zero_add] using hs
  · intro hs
    refine ⟨hl, (shapeAt_iff_get lambda (colorArray κ sigma) 0).mpr ?_,
      colorArray_chain H κ hp sigma⟩
    intro i
    have hi := hs ⟨i.val, by simpa only [colorArray_length] using i.isLt⟩
    simpa only [colorArray, List.getElem_ofFn, colorRow_length,
      SignedArrays.shiftKey, zero_add] using hi

theorem natLt_implies_nat_lt {n : ℕ} (H : NaturalUnitInterval n) {x y : ℕ}
    (h : natLt H x y) : x < y := by
  by_cases hx : x < n
  · by_cases hy : y < n
    · exact posetLt_implies_lt H (by simpa [natLt, hx, hy] using h)
    · simp [natLt, hx, hy] at h
  · simp [natLt, hx] at h

theorem exists_array_row {n m : ℕ} (a : SignedArrays.Array)
    (hc : (SignedArrays.contents a).Perm (List.range n)) (hl : a.length = m) (v : Fin n) :
    ∃ i : Fin m, v.val ∈ (a[i.val]'(by omega)).2 := by
  have hv := hc.mem_iff.mpr (List.mem_range.mpr v.isLt)
  obtain ⟨row, hr, hv⟩ := List.mem_flatten.mp hv
  obtain ⟨entry, he, rfl⟩ := List.mem_map.mp hr
  obtain ⟨i, hi, he⟩ := List.mem_iff_getElem.mp he
  exact ⟨⟨i, by omega⟩, by simpa only [he] using hv⟩

/-- The inverse coloring uses the unique row containing the vertex. -/
def arrayColor {n m : ℕ} (a : SignedArrays.Array)
    (hc : (SignedArrays.contents a).Perm (List.range n)) (hl : a.length = m) : Fin n → Fin m :=
  fun v => Classical.choose (exists_array_row a hc hl v)

theorem arrayColor_mem {n m : ℕ} (a : SignedArrays.Array)
    (hc : (SignedArrays.contents a).Perm (List.range n)) (hl : a.length = m) (v : Fin n) :
    v.val ∈ (a[(arrayColor a hc hl v).val]'(by have := (arrayColor a hc hl v).isLt; omega)).2 :=
  Classical.choose_spec (exists_array_row a hc hl v)

theorem array_row_unique {n m : ℕ} (a : SignedArrays.Array)
    (hc : (SignedArrays.contents a).Perm (List.range n)) (hl : a.length = m)
    (i j : Fin m) (v : ℕ) (hi : v ∈ (a[i.val]'(by omega)).2)
    (hj : v ∈ (a[j.val]'(by omega)).2) : i = j := by
  have hn : (SignedArrays.contents a).Nodup := hc.nodup_iff.mpr List.nodup_range
  have hd := (List.nodup_flatten.mp hn).2
  by_contra hne
  have hne' : i.val ≠ j.val := fun h => hne (Fin.ext h)
  by_cases hij : i.val < j.val
  · have h := List.pairwise_iff_getElem.mp hd i.val j.val
      (by simp [SignedArrays.rows, hl]) (by simp [SignedArrays.rows, hl]) hij
    have h' : List.Disjoint (a[i.val]'(by omega)).2 (a[j.val]'(by omega)).2 := by
      simpa only [SignedArrays.rows, List.getElem_map] using h
    exact h' hi hj
  · have hji : j.val < i.val := by omega
    have h := List.pairwise_iff_getElem.mp hd j.val i.val
      (by simp [SignedArrays.rows, hl]) (by simp [SignedArrays.rows, hl]) hji
    have h' : List.Disjoint (a[j.val]'(by omega)).2 (a[i.val]'(by omega)).2 := by
      simpa only [SignedArrays.rows, List.getElem_map] using h
    exact h' hj hi

theorem mem_array_row_iff {n m : ℕ} (a : SignedArrays.Array)
    (hc : (SignedArrays.contents a).Perm (List.range n)) (hl : a.length = m)
    (i : Fin m) (v : Fin n) :
    v.val ∈ (a[i.val]'(by omega)).2 ↔ arrayColor a hc hl v = i := by
  constructor
  · intro hv
    exact array_row_unique a hc hl _ i v.val (arrayColor_mem a hc hl v) hv
  · intro he
    simpa only [he] using arrayColor_mem a hc hl v

theorem arrayColor_proper {n m : ℕ} (H : NaturalUnitInterval n) (a : SignedArrays.Array)
    (ha : SignedArrays.ChainArray (natLt H) (List.range n) a) (hl : a.length = m) :
    Proper H (arrayColor a ha.2.1 hl) := by
  intro v w he hcolor
  let i := arrayColor a ha.2.1 hl v
  have hv : v.val ∈ (a[i.val]'(by have := i.isLt; omega)).2 := arrayColor_mem a ha.2.1 hl v
  have hw : w.val ∈ (a[i.val]'(by have := i.isLt; omega)).2 := by
    simpa only [i, hcolor] using arrayColor_mem a ha.2.1 hl w
  have hr := ha.2.2 (a[i.val]'(by have := i.isLt; omega)) (List.getElem_mem _)
  let R := fun x y => natLt H x y ∨ natLt H y x
  have : Std.Symm R := ⟨fun _ _ h => h.symm⟩
  have hp : ((a[i.val]'(by have := i.isLt; omega)).2).Pairwise R :=
    hr.imp (fun h => Or.inl h)
  have hne : v.val ≠ w.val := by have := he.1; omega
  obtain h | h := hp.forall hv hw hne
  · have h' : PosetLt H v w := by simpa only [natLt, dite_eq_left v.isLt, dite_eq_left w.isLt] using h
    exact not_lt_of_ge he.2 h'
  · have h' := natLt_implies_nat_lt H h
    have := he.1
    omega

def arrayLabel {m : ℕ} (a : SignedArrays.Array) (hl : a.length = m)
    (hp : (SignedArrays.labels a).Perm (List.range m)) (i : Fin m) : Fin m :=
  ⟨(a[i.val]'(by omega)).1, by
    apply List.mem_range.mp
    apply hp.mem_iff.mp
    exact List.mem_map.mpr ⟨_, List.getElem_mem (by omega), rfl⟩⟩

theorem arrayLabel_bijective {m : ℕ} (a : SignedArrays.Array) (hl : a.length = m)
    (hp : (SignedArrays.labels a).Perm (List.range m)) :
    Function.Bijective (arrayLabel a hl hp) := by
  constructor
  · intro i j he
    have hn := hp.nodup_iff.mpr List.nodup_range
    have he' : (SignedArrays.labels a)[i.val]'(by simp [SignedArrays.labels, hl]) =
        (SignedArrays.labels a)[j.val]'(by simp [SignedArrays.labels, hl]) := by
      simpa only [SignedArrays.labels, List.getElem_map, arrayLabel] using congrArg Fin.val he
    exact Fin.ext (hn.eq_of_getElem_eq _ _ he')
  · intro j
    have hj := hp.mem_iff.mpr (List.mem_range.mpr j.isLt)
    obtain ⟨entry, he, hj⟩ := List.mem_map.mp hj
    obtain ⟨i, hi, he⟩ := List.mem_iff_getElem.mp he
    refine ⟨⟨i, by omega⟩, Fin.ext ?_⟩
    simpa only [arrayLabel, he] using hj

def arrayPermutation {m : ℕ} (a : SignedArrays.Array) (hl : a.length = m)
    (hp : (SignedArrays.labels a).Perm (List.range m)) : Equiv.Perm (Fin m) :=
  Equiv.ofBijective (arrayLabel a hl hp) (arrayLabel_bijective a hl hp)

theorem array_row_canonical {n m : ℕ} (H : NaturalUnitInterval n) (a : SignedArrays.Array)
    (ha : SignedArrays.ChainArray (natLt H) (List.range n) a) (hl : a.length = m) (i : Fin m) :
    colorRow (arrayColor a ha.2.1 hl) i = (a[i.val]'(by omega)).2 := by
  have hr := ha.2.2 (a[i.val]'(by omega)) (List.getElem_mem _)
  apply (colorRow_sorted _ i).eq_of_mem_iff (hr.imp (fun h => natLt_implies_nat_lt H h))
  intro v
  constructor
  · intro hv
    obtain ⟨hv, hc⟩ := (mem_colorRow _ i v).mp hv
    exact (mem_array_row_iff a ha.2.1 hl i ⟨v, hv⟩).mpr hc
  · intro hv
    have hc : v ∈ SignedArrays.contents a :=
      List.mem_flatten_of_mem (List.mem_map.mpr ⟨_, List.getElem_mem (by omega), rfl⟩) hv
    have hvn := List.mem_range.mp (ha.2.1.mem_iff.mp hc)
    exact (mem_colorRow _ i v).mpr ⟨hvn, (mem_array_row_iff a ha.2.1 hl i ⟨v, hvn⟩).mp hv⟩

/-- Every actual complete chain array is recovered, including all empty rows. -/
theorem colorArray_inverse {n m : ℕ} (H : NaturalUnitInterval n) (a : SignedArrays.Array)
    (ha : SignedArrays.ChainArray (natLt H) (List.range n) a) (hl : a.length = m)
    (hp : (SignedArrays.labels a).Perm (List.range m)) :
    colorArray (arrayColor a ha.2.1 hl) (arrayPermutation a hl hp) = a := by
  apply List.ext_getElem (by simp [colorArray, hl])
  intro i hi hi'
  simp only [colorArray, List.getElem_ofFn]
  apply Prod.ext
  · rfl
  · exact array_row_canonical H a ha hl ⟨i, by simpa only [colorArray_length] using hi⟩

theorem colorArray_injective {n m : ℕ} {κ ρ : Fin n → Fin m}
    {sigma tau : Equiv.Perm (Fin m)} (he : colorArray κ sigma = colorArray ρ tau) :
    sigma = tau ∧ κ = ρ := by
  have hg : ∀ i : Fin m, ((sigma i).val, colorRow κ i) = ((tau i).val, colorRow ρ i) := by
    intro i
    have h := congrArg (fun a : SignedArrays.Array => a[i.val]?) he
    simpa only [colorArray, List.getElem?_ofFn, dite_eq_left i.isLt,
      Option.some.injEq] using h
  constructor
  · apply Equiv.ext
    intro i
    exact Fin.ext (congrArg Prod.fst (hg i))
  · funext v
    have hv : v.val ∈ colorRow κ (κ v) := (mem_colorRow κ _ _).mpr ⟨v.isLt, rfl⟩
    have hrows : colorRow κ (κ v) = colorRow ρ (κ v) := congrArg Prod.snd (hg (κ v))
    rw [hrows] at hv
    exact ((mem_colorRow ρ _ _).mp hv).2.symm

def signedColorUniverse {n : ℕ} (H : NaturalUnitInterval n) (lambda : ℕ → ℕ) (m : ℕ) :
    Finset (Equiv.Perm (Fin m) × (Fin n → Fin m)) :=
  Finset.univ.filter (fun p => Proper H p.2 ∧ ∀ i,
    ((colorClass p.2 i).card : ℤ) =
      (lambda (p.1 i).val : ℤ) - ((p.1 i).val : ℤ) + (i.val : ℤ))

/-- The finite universe is the image of precisely the proper colorings with
the signed coefficient's integer constraints. -/
theorem signedColorUniverse_image {n : ℕ} (H : NaturalUnitInterval n)
    (lambda : ℕ → ℕ) (m : ℕ) :
    (signedColorUniverse H lambda m).image (fun p => colorArray p.2 p.1) =
      signedArrayUniverse (natLt H) (List.range n) lambda m := by
  ext a
  simp only [Finset.mem_image, mem_signedArrayUniverse]
  constructor
  · rintro ⟨⟨sigma, κ⟩, hp, rfl⟩
    obtain ⟨hp, hs⟩ := (Finset.mem_filter.mp hp).2
    exact ⟨(colorArray_signed_iff H κ hp sigma lambda).mpr hs, colorArray_length κ sigma⟩
  · rintro ⟨ha, hl⟩
    let κ := arrayColor a ha.2.2.2.1 hl
    let sigma := arrayPermutation a hl (by simpa only [hl] using ha.1)
    have he : colorArray κ sigma = a := colorArray_inverse H a ha.2.2 hl _
    have hp : Proper H κ := arrayColor_proper H a ha.2.2 hl
    refine ⟨(sigma, κ), Finset.mem_filter.mpr ⟨Finset.mem_univ _, hp, ?_⟩, he⟩
    apply (colorArray_signed_iff H κ hp sigma lambda).mp
    rw [he]
    exact ha

open scoped BigOperators

theorem signedArray_sum_reindex {n : ℕ} (H : NaturalUnitInterval n)
    (lambda : ℕ → ℕ) (m : ℕ) (f : SignedArrays.Array → Coeff) :
    (∑ a ∈ signedArrayUniverse (natLt H) (List.range n) lambda m, f a) =
      ∑ p ∈ signedColorUniverse H lambda m, f (colorArray p.2 p.1) := by
  rw [← signedColorUniverse_image H lambda m, Finset.sum_image]
  intro p _ q _ he
  obtain ⟨h1, h2⟩ := colorArray_injective he
  exact Prod.ext h1 h2

theorem sum_colorRow {n m : ℕ} (κ : Fin n → Fin m) (c : Fin m) (f : ℕ → ℕ) :
    ((colorRow κ c).map f).sum = ∑ v : Fin n, if κ v = c then f v.val else 0 := by
  calc
    ((colorRow κ c).map f).sum =
        ∑ v ∈ (colorClass κ c).image Fin.val, f v := by
      unfold colorRow
      rw [← List.sum_toFinset f (Finset.sort_nodup _ _)]
      simp only [Finset.sort_toFinset]
    _ = ∑ v ∈ colorClass κ c, f v.val := by
      rw [Finset.sum_image]
      exact fun _ _ _ _ h => Fin.val_injective h
    _ = _ := by simp only [colorClass, Finset.sum_filter]

theorem crossWeight_append_right (score : ℕ → ℕ → ℕ) (xs ys zs : List ℕ) :
    CornerSlide.crossWeight score xs (ys ++ zs) =
      CornerSlide.crossWeight score xs ys + CornerSlide.crossWeight score xs zs := by
  simp only [CornerSlide.crossWeight, List.map_append, List.sum_append, List.sum_map_add]

theorem crossWeight_flatten (score : ℕ → ℕ → ℕ) (xs : List ℕ) (rs : List (List ℕ)) :
    CornerSlide.crossWeight score xs rs.flatten =
      (rs.map (fun row => CornerSlide.crossWeight score xs row)).sum := by
  induction rs with
  | nil => simp [CornerSlide.crossWeight]
  | cons row rest ih =>
      simp only [List.flatten_cons, crossWeight_append_right, ih, List.map_cons, List.sum_cons]

theorem tableauInversions_ofFn (r : ℕ → ℕ → Prop) [DecidableRel r]
    {m : ℕ} (rs : Fin m → List ℕ) :
    CornerSlide.tableauGraphInversions r (List.ofFn rs) =
      ∑ i : Fin m, ∑ j : Fin m,
        if i < j then CornerSlide.crossWeight (CornerSlide.graphScore r) (rs i) (rs j) else 0 := by
  induction m with
  | zero => simp [CornerSlide.tableauGraphInversions]
  | succ m ih =>
      simp [List.ofFn_succ, CornerSlide.tableauGraphInversions, crossWeight_flatten,
        List.map_ofFn, List.sum_ofFn, ih, Fin.sum_univ_succ, Function.comp_def]

theorem crossWeight_colorRows {n m : ℕ} (κ : Fin n → Fin m)
    (score : ℕ → ℕ → ℕ) (c d : Fin m) :
    CornerSlide.crossWeight score (colorRow κ c) (colorRow κ d) =
      ∑ x : Fin n, ∑ y : Fin n,
        if κ x = c then if κ y = d then score x.val y.val else 0 else 0 := by
  simp only [CornerSlide.crossWeight, sum_colorRow]
  apply Finset.sum_congr rfl
  intro x _
  by_cases hx : κ x = c <;> simp [hx]

theorem graphScore_natLt {n : ℕ} (H : NaturalUnitInterval n) (x y : Fin n) :
    CornerSlide.graphScore (natLt H) x.val y.val = if Edge H y x then 1 else 0 := by
  have he : (y < x ∧ ¬ PosetLt H x y ∧ ¬ PosetLt H y x) ↔ Edge H y x := by
    rw [edge_iff_incomparable]
    tauto
  simp only [CornerSlide.graphScore, natLt, dite_eq_left x.isLt, dite_eq_left y.isLt]
  exact if_congr he rfl rfl

/-- Actual list row inversions equal actual coloring descents. This identity
holds for every coloring; properness is needed only for the chain filling. -/
theorem colorArray_inversions {n m : ℕ} (H : NaturalUnitInterval n)
    (κ : Fin n → Fin m) (sigma : Equiv.Perm (Fin m)) :
    CornerSlide.tableauGraphInversions (natLt H) (SignedArrays.rows (colorArray κ sigma)) =
      descents H κ := by
  rw [colorArray_rows, tableauInversions_ofFn]
  have hp : (∑ c : Fin m, ∑ d : Fin m,
      if c < d then CornerSlide.crossWeight (CornerSlide.graphScore (natLt H))
        (colorRow κ c) (colorRow κ d) else 0) =
      ∑ x : Fin n, ∑ y : Fin n,
        if κ x < κ y then CornerSlide.graphScore (natLt H) x.val y.val else 0 := by
    simp only [crossWeight_colorRows]
    calc
      _ = ∑ c : Fin m, ∑ d : Fin m, ∑ x : Fin n, ∑ y : Fin n,
          if κ x = c then if κ y = d then
            if c < d then CornerSlide.graphScore (natLt H) x.val y.val else 0 else 0 else 0 := by
        apply Finset.sum_congr rfl
        intro c _
        apply Finset.sum_congr rfl
        intro d _
        by_cases hcd : c < d <;> simp [hcd]
      _ = ∑ x : Fin n, ∑ y : Fin n, ∑ c : Fin m, ∑ d : Fin m,
          if κ x = c then if κ y = d then
            if c < d then CornerSlide.graphScore (natLt H) x.val y.val else 0 else 0 else 0 := by
        calc
          _ = ∑ c : Fin m, ∑ x : Fin n, ∑ y : Fin n, ∑ d : Fin m,
              if κ x = c then if κ y = d then
                if c < d then CornerSlide.graphScore (natLt H) x.val y.val else 0 else 0 else 0 := by
            apply Finset.sum_congr rfl
            intro c _
            rw [Finset.sum_comm]
            apply Finset.sum_congr rfl
            intro x _
            rw [Finset.sum_comm]
          _ = _ := by
            rw [Finset.sum_comm]
            apply Finset.sum_congr rfl
            intro x _
            rw [Finset.sum_comm]
      _ = _ := by simp [Finset.sum_ite_irrel]
  rw [hp, Finset.sum_comm]
  unfold descents
  rw [Finset.card_eq_sum_ones, Finset.sum_filter, Fintype.sum_prod_type]
  apply Finset.sum_congr rfl
  intro y _
  apply Finset.sum_congr rfl
  intro x _
  rw [graphScore_natLt]
  by_cases he : Edge H y x <;> by_cases hc : κ x < κ y <;> simp [he, hc]

end PartitionH3

#check @PartitionH3.colorArray_signed_iff
#print axioms PartitionH3.colorRows_contents
#print axioms PartitionH3.colorArray_chain
#print axioms PartitionH3.shapeAt_iff_get
#print axioms PartitionH3.colorArray_signed_iff
#print axioms PartitionH3.colorArray_sign
#print axioms PartitionH3.colorArray_inverse
#print axioms PartitionH3.colorArray_injective
#print axioms PartitionH3.signedColorUniverse_image
#print axioms PartitionH3.signedArray_sum_reindex
#print axioms PartitionH3.graphScore_natLt
#print axioms PartitionH3.colorArray_inversions
