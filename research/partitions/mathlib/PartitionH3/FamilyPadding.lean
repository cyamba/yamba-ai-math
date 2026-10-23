import PartitionH3.SignedCancellation

/-!
Canonical removal of zero-length padding. The target is the original
complete `CornerSlide.family`, with its actual membership characterization.
-/

noncomputable section

namespace PartitionH3

def identityArrayAt (start : ℕ) : CornerSlide.Rows → SignedArrays.Array
  | [] => []
  | row :: rest => (start, row) :: identityArrayAt (start + 1) rest

theorem identityArrayAt_rows (start : ℕ) (rs : CornerSlide.Rows) :
    SignedArrays.rows (identityArrayAt start rs) = rs := by
  induction rs generalizing start with
  | nil => rfl
  | cons row rest ih =>
    change row :: SignedArrays.rows (identityArrayAt (start + 1) rest) = row :: rest
    rw [ih]

theorem identityArrayAt_length (start : ℕ) (rs : CornerSlide.Rows) :
    (identityArrayAt start rs).length = rs.length := by
  induction rs generalizing start with
  | nil => rfl
  | cons row rest ih => simp [identityArrayAt, ih]

theorem identityArrayAt_labels (start : ℕ) (rs : CornerSlide.Rows) :
    SignedArrays.labels (identityArrayAt start rs) = List.range' start rs.length := by
  induction rs generalizing start with
  | nil => rfl
  | cons row rest ih =>
    change start :: SignedArrays.labels (identityArrayAt (start + 1) rest) = _
    rw [ih, List.length_cons, List.range'_succ]

theorem array_eq_of_labels_rows (a b : SignedArrays.Array)
    (hl : SignedArrays.labels a = SignedArrays.labels b)
    (hr : SignedArrays.rows a = SignedArrays.rows b) : a = b := by
  induction a generalizing b with
  | nil =>
    cases b with
    | nil => rfl
    | cons entry rest => simp [SignedArrays.rows] at hr
  | cons entry rest ih =>
    cases b with
    | nil => simp [SignedArrays.rows] at hr
    | cons entry' rest' =>
      have hp := List.cons.inj (show entry.1 :: SignedArrays.labels rest =
        entry'.1 :: SignedArrays.labels rest' from hl)
      have hq := List.cons.inj (show entry.2 :: SignedArrays.rows rest =
        entry'.2 :: SignedArrays.rows rest' from hr)
      have he : entry = entry' := Prod.ext hp.1 hq.1
      rw [he, ih rest' hp.2 hq.2]

theorem array_eq_identity_of_labels (a : SignedArrays.Array)
    (hl : SignedArrays.labels a = List.range a.length) :
    a = identityArrayAt 0 (SignedArrays.rows a) := by
  apply array_eq_of_labels_rows
  · rw [identityArrayAt_labels]
    simpa only [SignedArrays.rows, List.length_map, List.range_eq_range'] using hl
  · rw [identityArrayAt_rows]

theorem identityArrayAt_shape (lambda : ℕ → ℕ) (start : ℕ) (rs : CornerSlide.Rows)
    (hs : rs.map List.length = (List.range' start rs.length).map lambda) :
    SignedArrays.ShapeAt lambda (start : ℤ) (identityArrayAt start rs) := by
  induction rs generalizing start with
  | nil => trivial
  | cons row rest ih =>
    have h := List.cons.inj (show row.length :: rest.map List.length =
      lambda start :: (List.range' (start + 1) rest.length).map lambda by
        simpa [List.range'_succ] using hs)
    change (row.length : ℤ) = SignedArrays.shiftKey lambda start + start ∧ _
    constructor
    · unfold SignedArrays.shiftKey
      omega
    · simpa only [Int.natCast_add, Int.natCast_one] using ih (start + 1) h.2

theorem identityArray_signed (r : ℕ → ℕ → Prop) (vertices : List ℕ)
    (lambda : ℕ → ℕ) (rs : CornerSlide.Rows)
    (hv : vertices.Nodup) (hf : rs.flatten.Perm vertices)
    (hc : ∀ row ∈ rs, row.Pairwise r)
    (hs : rs.map List.length = (List.range rs.length).map lambda) :
    SignedArrays.SignedArray r vertices lambda (identityArrayAt 0 rs) := by
  refine ⟨?_, ?_, hv, ?_, ?_⟩
  · rw [identityArrayAt_labels, identityArrayAt_length, List.range_eq_range']
  · apply identityArrayAt_shape
    simpa only [List.range_eq_range'] using hs
  · simpa only [SignedArrays.contents, identityArrayAt_rows] using hf
  · intro entry he
    apply hc entry.2
    rw [← identityArrayAt_rows 0 rs]
    exact List.mem_map.mpr ⟨entry, he, rfl⟩

def paddedIdentityArray (pad : ℕ) (body : CornerSlide.Rows) : SignedArrays.Array :=
  identityArrayAt 0 (body ++ List.replicate pad [])

theorem paddedIdentityArray_injective (pad : ℕ) :
    Function.Injective (paddedIdentityArray pad) := by
  intro body body' he
  have hr := congrArg SignedArrays.rows he
  simp only [paddedIdentityArray, identityArrayAt_rows] at hr
  exact List.append_cancel_right hr

theorem rows_of_zero_lengths (rs : CornerSlide.Rows) (pad : ℕ)
    (h : rs.map List.length = List.replicate pad 0) :
    rs = List.replicate pad [] := by
  induction pad generalizing rs with
  | zero => simpa using h
  | succ pad ih =>
    cases rs with
    | nil => simp at h
    | cons row rest =>
      have hh : row.length = 0 ∧ rest.map List.length = List.replicate pad 0 := by
        simpa only [List.map_cons, List.replicate_succ, List.cons.injEq] using h
      have he : row = [] := List.length_eq_zero_iff.mp hh.1
      simp only [he, ih rest hh.2, List.replicate_succ]

theorem rows_padding_decomposition (rs : CornerSlide.Rows) (shape : List ℕ) (pad : ℕ)
    (h : rs.map List.length = shape ++ List.replicate pad 0) :
    rs = rs.take shape.length ++ List.replicate pad [] ∧
      (rs.take shape.length).map List.length = shape := by
  induction shape generalizing rs with
  | nil =>
    have he := rows_of_zero_lengths rs pad (by simpa using h)
    simp [he]
  | cons d shape ih =>
    cases rs with
    | nil => simp at h
    | cons row rest =>
      have hh : row.length = d ∧
          rest.map List.length = shape ++ List.replicate pad 0 := by
        simpa only [List.map_cons, List.cons_append, List.cons.injEq] using h
      have ht := ih rest hh.2
      constructor
      · simpa only [List.length_cons, List.take_succ_cons, List.cons_append,
          List.cons.injEq, true_and] using ht.1
      · simpa only [List.length_cons, List.take_succ_cons, List.map_cons,
          List.cons.injEq, hh.1, true_and] using ht.2

/-- Positive row lengths distinguish the actual body from its empty padding. -/
theorem padded_rows_iff_complete_family (r : ℕ → ℕ → Prop) (vertices shape : List ℕ)
    (hpos : ∀ d ∈ shape, 0 < d) (rs : CornerSlide.Rows) (pad : ℕ)
    (hlen : rs.map List.length = shape ++ List.replicate pad 0) :
    SignedArrays.PaddedTableau r vertices rs ↔
      rs.take shape.length ∈ CornerSlide.family r vertices shape := by
  classical
  obtain ⟨he, hs⟩ := rows_padding_decomposition rs shape pad hlen
  constructor
  · rintro ⟨body, k, hb, ht⟩
    have hflat : rs.flatten.Perm vertices := by
      rw [hb, SignedArrays.flatten_padding]
      exact ht.2.1
    have hcols : CornerSlide.ColumnsValid r rs := by
      rw [hb, SignedArrays.columns_padding]
      exact ht.2.2.2
    have hchains : ∀ row ∈ rs, row.Pairwise r := by
      intro row hr
      rw [hb] at hr
      rcases List.mem_append.mp hr with hr | hr
      · exact (ht.2.2.1 row hr).2
      · have hz : row = [] := (List.mem_replicate.mp hr).2
        simp [hz]
    apply (CornerSlide.mem_family r vertices shape _).mpr
    refine ⟨⟨ht.1, ?_, ?_, ?_⟩, hs⟩
    · rw [he, SignedArrays.flatten_padding] at hflat
      exact hflat
    · intro row hr
      have hm : row ∈ rs := by rw [he]; exact List.mem_append_left _ hr
      have hl : row.length ∈ shape := by
        rw [← hs]
        exact List.mem_map.mpr ⟨row, hr, rfl⟩
      refine ⟨?_, hchains row hm⟩
      intro hz
      have hp := hpos row.length hl
      simp [hz] at hp
    · rw [he, SignedArrays.columns_padding] at hcols
      exact hcols
  · intro hf
    exact ⟨rs.take shape.length, pad, he,
      ((CornerSlide.mem_family r vertices shape _).mp hf).1⟩

theorem tableauGraphInversions_padding (r : ℕ → ℕ → Prop) [DecidableRel r]
    (body : CornerSlide.Rows) (pad : ℕ) :
    CornerSlide.tableauGraphInversions r (body ++ List.replicate pad []) =
      CornerSlide.tableauGraphInversions r body := by
  induction body with
  | nil =>
    induction pad with
    | zero => rfl
    | succ pad ih =>
      simpa [List.replicate_succ, CornerSlide.tableauGraphInversions,
        CornerSlide.crossWeight] using ih
  | cons row rest ih =>
    simp only [List.cons_append, CornerSlide.tableauGraphInversions,
      SignedArrays.flatten_padding, ih]

end PartitionH3

#check @PartitionH3.padded_rows_iff_complete_family
#print axioms PartitionH3.rows_padding_decomposition
#print axioms PartitionH3.padded_rows_iff_complete_family
#print axioms PartitionH3.tableauGraphInversions_padding
