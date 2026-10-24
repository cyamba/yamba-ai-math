import CornerSlide
import SignedArrays

/-!
# Multi-Dimensional (3D and d-D) Ferrers Diagram Theorems

Supplementary machine-checked Lean 4 verification for:
1. Christopher Yamba's 3D Ferrers diagram resolution of the height-3 corner-slide collision:
   - Exact non-3-chain fiber injectivity (`extract_bubble_inverse` without global height-two restriction).
   - Universal 3D rotation `promote32 : ((u,v),(a,b),(c)) ↦ ((u,v,b),(a,c))` into shape `(3,2)`,
     preserving `Tableau` validity and `tableauGraphInversions` for any transitive asymmetric poset.
2. Universal interior and endpoint hook slides (`hookBubbleEnd`, `hookBubbleMid`) on `(3,1^r) → (2,1^{r+1})`,
   preserving `Tableau` validity and `tableauGraphInversions`.
3. Universal k-dimensional first-column cascade `(0, k) ↔ (k-1, 1)` in `SignedArrays` for all `k ≥ 2`.
4. Scale-3 self-similarity and 6D Ferrers octant weight identities for the Kanade–Russell I₁ (KR1)
   quadratic form `Q(a, b) = a^2 + 3ab + 3b^2`.
-/

namespace MultidimensionalFerrers

open CornerSlide
open SignedArrays
attribute [local instance] Classical.propDecidable

/-! ## 1. Non-3-Chain Fiber Injectivity & 3D Rotation into Shape (3, 2) -/

/-- Local absence of a 3-chain `a <_P z <_P b` between `a` and `b`.
Unlike `NoThreeChain r`, this predicate holds on the 2D fiber inside posets of arbitrary height. -/
def NoLocalThreeChain (r : Nat → Nat → Prop) (a b : Nat) : Prop :=
  ∀ z, r z b → ¬ r a z

theorem bubble_injective_local_fiber (r : Nat → Nat → Prop) [DecidableRel r]
    (a b b' : Nat) (tail tail' : List Nat)
    (hab : r a b) (hab' : r a b')
    (hfib : NoLocalThreeChain r a b)
    (hfib' : NoLocalThreeChain r a b')
    (h : bubbleInsert r b tail = bubbleInsert r b' tail') : b = b' ∧ tail = tail' := by
  have he := congrArg (extractFirst (r a)) h
  rw [extract_bubble_inverse r a b tail hab hfib,
    extract_bubble_inverse r a b' tail' hab' hfib'] at he
  exact Prod.mk.inj (Option.some.inj he)

/-- 3D rotation of a colliding `(2, 2, 1)` tableau `[[u, v], [a, b], [c]]` (where `a <_P c <_P b`)
into shape `(3, 2)` by rotating the 3rd-axis entry `b` into row 1 and `c` into row 2. -/
def promote32 (u v a b c : Nat) : Rows :=
  [[u, v, b], [a, c]]

theorem promote32_perm (u v a b c : Nat) :
    (promote32 u v a b c).flatten.Perm ([[u, v], [a, b], [c]] : Rows).flatten := by
  change [u, v, b, a, c].Perm [u, v, a, b, c]
  exact List.Perm.cons u (List.Perm.cons v (List.Perm.swap a b [c]))

theorem rowValid_triple (r : Nat → Nat → Prop)
    (trans : ∀ x y z, r x y → r y z → r x z) (u v b : Nat)
    (huv : r u v) (hvb : r v b) : RowValid r [u, v, b] := by
  refine ⟨by simp, ?_⟩
  simp [huv, hvb, trans u v b huv hvb]

theorem promote32_tableau_valid (r : Nat → Nat → Prop)
    (trans : ∀ x y z, r x y → r y z → r x z)
    (vertices : List Nat) (u v a b c : Nat)
    (hsource : Tableau r vertices [[u, v], [a, b], [c]])
    (hac : r a c) (hvb : r v b) (hcv : ¬ r c v) :
    Tableau r vertices (promote32 u v a b c) := by
  rcases hsource with ⟨hnodup, hperm, hrows, hcols⟩
  have huv : r u v := (rowValid_pair r u v).mp (hrows [u, v] (by simp))
  have hab : r a b := (rowValid_pair r a b).mp (hrows [a, b] (by simp))
  have hau : ¬ r a u := hcols.1.1
  refine ⟨hnodup, (promote32_perm u v a b c).trans hperm, ?_, ?_⟩
  · intro row hrow
    simp only [promote32, List.mem_cons, List.not_mem_nil, or_false] at hrow
    rcases hrow with rfl | rfl
    · exact rowValid_triple r trans u v b huv hvb
    · exact (rowValid_pair r a c).mpr hac
  · simp [promote32, ColumnsValid, ColumnPair, hau, hcv]

theorem promote32_tableau_graph_inversions (r : Nat → Nat → Prop) [DecidableRel r]
    (trans : ∀ x y z, r x y → r y z → r x z)
    (vertices : List Nat) (u v a b c : Nat)
    (hsource : Tableau r vertices [[u, v], [a, b], [c]])
    (hac : r a c) (hvb : r v b) (hcv : ¬ r c v) :
    tableauGraphInversions r (promote32 u v a b c) =
      tableauGraphInversions r [[u, v], [a, b], [c]] := by
  have htarget := promote32_tableau_valid r trans vertices u v a b c hsource hac hvb hcv
  have hab : r a b := (rowValid_pair r a b).mp (hsource.2.2.1 [a, b] (by simp))
  rw [tableau_graph_inversions_eq_word r _ (fun row hr => (htarget.2.2.1 row hr).2),
    tableau_graph_inversions_eq_word r _ (fun row hr => (hsource.2.2.1 row hr).2)]
  simpa [promote32] using
    (graph_inversions_comparable_swap r [u, v] [c] a b hab).symm

/-- Concrete verification on the height-3 collision witness `T₂ = [[1, 2], [3, 5], [4]]`
from Theorem 4.3 of the paper: rotating into `[[1, 2, 5], [3, 4]]` produces a valid `(3, 2)`
tableau and eliminates the collision with `T₁ = [[1, 2], [3, 4], [5]]`. -/
theorem collision_witness_promoted_valid :
    Tableau fiveOrder [1, 2, 3, 4, 5] (promote32 1 2 3 5 4) ∧
    tableauGraphInversions fiveOrder (promote32 1 2 3 5 4) =
      tableauGraphInversions fiveOrder [[1, 2], [3, 5], [4]] := by
  constructor
  · simp [promote32, Tableau, ShapeAndOrder, RowValid, ColumnsValid, ColumnPair, fiveOrder]
    decide
  · decide

/-! ## 2. Universal Interior and Endpoint Hook Slides `(3, 1^m) → (2, 1^{m+1})` -/

def hookBefore (u v w : Nat) (tail : List Nat) : Rows :=
  [u, v, w] :: singletons tail

def hookBubbleEnd (r : Nat → Nat → Prop) [DecidableRel r]
    (u v w : Nat) (tail : List Nat) : Rows :=
  [u, v] :: singletons (bubbleInsert r w tail)

def hookBubbleMid (r : Nat → Nat → Prop) [DecidableRel r]
    (u v w : Nat) (tail : List Nat) : Rows :=
  [u, w] :: singletons (bubbleInsert r v tail)

theorem columns_triple_singletons (r : Nat → Nat → Prop) (u v w : Nat) (tail : List Nat) :
    ColumnsValid r ([u, v, w] :: singletons tail) ↔ NoDescent r (u :: tail) := by
  cases tail with
  | nil => simp [singletons, ColumnsValid, NoDescent]
  | cons z zs =>
      change ((¬ r z u ∧ True) ∧ ColumnsValid r (singletons (z :: zs))) ↔
        (¬ r z u ∧ NoDescent r (z :: zs))
      simp only [and_true, columns_singletons]

theorem hookBubbleEnd_tableau_valid (r : Nat → Nat → Prop) [DecidableRel r]
    (asym : ∀ x y, r x y → ¬ r y x) (vertices : List Nat)
    (u v w : Nat) (tail : List Nat)
    (h : Tableau r vertices (hookBefore u v w tail)) :
    Tableau r vertices (hookBubbleEnd r u v w tail) := by
  rcases h with ⟨hnodup, hperm, hrows, hcols⟩
  have htriple := (hrows [u, v, w] (by simp [hookBefore])).2
  have huv : r u v := (List.pairwise_cons.mp htriple).1 v (by simp)
  have huw : r u w := (List.pairwise_cons.mp htriple).1 w (by simp)
  have hnd : NoDescent r (u :: tail) := (columns_triple_singletons r u v w tail).mp hcols
  have hnd' : NoDescent r (u :: bubbleInsert r w tail) :=
    bubble_noDescent r asym u w tail huw hnd
  have hp : (hookBubbleEnd r u v w tail).flatten.Perm (hookBefore u v w tail).flatten := by
    simpa [hookBubbleEnd, hookBefore, flatten_singletons] using
      List.Perm.cons u (List.Perm.cons v (bubble_perm r w tail))
  refine ⟨hnodup, hp.trans hperm, ?_, (columns_pair_singletons r u v _).mpr hnd'⟩
  intro row hr
  simp only [hookBubbleEnd, List.mem_cons] at hr
  rcases hr with rfl | ht
  · exact (rowValid_pair r u v).mpr huv
  · obtain ⟨x, _, rfl⟩ := List.mem_map.mp ht
    exact rowValid_singleton r x

theorem hookBubbleEnd_tableau_graph_inversions (r : Nat → Nat → Prop) [DecidableRel r]
    (asym : ∀ x y, r x y → ¬ r y x) (vertices : List Nat)
    (u v w : Nat) (tail : List Nat)
    (h : Tableau r vertices (hookBefore u v w tail)) :
    tableauGraphInversions r (hookBubbleEnd r u v w tail) =
      tableauGraphInversions r (hookBefore u v w tail) := by
  have hb := hookBubbleEnd_tableau_valid r asym vertices u v w tail h
  rw [tableau_graph_inversions_eq_word r _ (fun row hr => (hb.2.2.1 row hr).2),
    tableau_graph_inversions_eq_word r _ (fun row hr => (h.2.2.1 row hr).2)]
  have hw := bubble_wordWeight r (graphScore r) w tail
    (fun z hz => comparable_score_neutral r z w hz)
  have hv := wordWeight_cons_congr (graphScore r) v _ _ (bubble_perm r w tail) hw
  have hu := wordWeight_cons_congr (graphScore r) u _ _ ((bubble_perm r w tail).cons v) hv
  simpa [graphInversions, hookBubbleEnd, hookBefore, flatten_singletons] using hu

theorem hookBubbleMid_tableau_valid (r : Nat → Nat → Prop) [DecidableRel r]
    (asym : ∀ x y, r x y → ¬ r y x) (vertices : List Nat)
    (u v w : Nat) (tail : List Nat)
    (h : Tableau r vertices (hookBefore u v w tail)) :
    Tableau r vertices (hookBubbleMid r u v w tail) := by
  rcases h with ⟨hnodup, hperm, hrows, hcols⟩
  have htriple := (hrows [u, v, w] (by simp [hookBefore])).2
  have huv : r u v := (List.pairwise_cons.mp htriple).1 v (by simp)
  have huw : r u w := (List.pairwise_cons.mp htriple).1 w (by simp)
  have hnd : NoDescent r (u :: tail) := (columns_triple_singletons r u v w tail).mp hcols
  have hnd' : NoDescent r (u :: bubbleInsert r v tail) :=
    bubble_noDescent r asym u v tail huv hnd
  have hp1 : (u :: w :: bubbleInsert r v tail).Perm (u :: w :: v :: tail) :=
    List.Perm.cons u (List.Perm.cons w (bubble_perm r v tail))
  have hp2 : (u :: w :: v :: tail).Perm (u :: v :: w :: tail) :=
    List.Perm.cons u (List.Perm.swap v w tail)
  have hp : (hookBubbleMid r u v w tail).flatten.Perm (hookBefore u v w tail).flatten := by
    simpa [hookBubbleMid, hookBefore, flatten_singletons] using hp1.trans hp2
  refine ⟨hnodup, hp.trans hperm, ?_, (columns_pair_singletons r u w _).mpr hnd'⟩
  intro row hr
  simp only [hookBubbleMid, List.mem_cons] at hr
  rcases hr with rfl | ht
  · exact (rowValid_pair r u w).mpr huw
  · obtain ⟨x, _, rfl⟩ := List.mem_map.mp ht
    exact rowValid_singleton r x

theorem hookBubbleMid_tableau_graph_inversions (r : Nat → Nat → Prop) [DecidableRel r]
    (asym : ∀ x y, r x y → ¬ r y x) (vertices : List Nat)
    (u v w : Nat) (tail : List Nat)
    (h : Tableau r vertices (hookBefore u v w tail)) :
    tableauGraphInversions r (hookBubbleMid r u v w tail) =
      tableauGraphInversions r (hookBefore u v w tail) := by
  have hb := hookBubbleMid_tableau_valid r asym vertices u v w tail h
  have htriple := (h.2.2.1 [u, v, w] (by simp [hookBefore])).2
  have hvw : r v w := (List.pairwise_cons.mp (List.pairwise_cons.mp htriple).2).1 w (by simp)
  rw [tableau_graph_inversions_eq_word r _ (fun row hr => (hb.2.2.1 row hr).2),
    tableau_graph_inversions_eq_word r _ (fun row hr => (h.2.2.1 row hr).2)]
  have hw := bubble_wordWeight r (graphScore r) v tail
    (fun z hz => comparable_score_neutral r z v hz)
  have hcons := wordWeight_cons_congr (graphScore r) w _ _ (bubble_perm r v tail) hw
  have hcons_u := wordWeight_cons_congr (graphScore r) u _ _
    ((bubble_perm r v tail).cons w) hcons
  have hswap := graph_inversions_comparable_swap r [u] tail v w hvw
  simpa [graphInversions, hookBubbleMid, hookBefore, flatten_singletons] using
    hcons_u.trans hswap.symm

/-! ## 3. Universal k-Dimensional First-Column Cascade `(0, k) ↔ (k-1, 1)` in `SignedArrays` -/

theorem perm_append_cons (b : Nat) (as tail : List Nat) :
    (as ++ b :: tail).Perm (b :: as ++ tail) := by
  induction as with
  | nil => exact List.Perm.refl _
  | cons a rest ih =>
      exact (ih.cons a).trans (List.Perm.swap b a (rest ++ tail))

theorem comparable_pass_wordWeight (r : Nat → Nat → Prop) [DecidableRel r]
    (b : Nat) (as tail : List Nat) (hba : ∀ a ∈ as, r b a) :
    wordWeight (graphScore r) (as ++ b :: tail) =
      wordWeight (graphScore r) (b :: as ++ tail) := by
  induction as with
  | nil => rfl
  | cons a rest ih =>
      have h1 : r b a := hba a (by simp)
      have hrest : ∀ x ∈ rest, r b x := fun x hx => hba x (by simp [hx])
      have hstep := wordWeight_cons_congr (graphScore r) a (rest ++ b :: tail) (b :: rest ++ tail)
        (perm_append_cons b rest tail) (ih hrest)
      have hswap := wordWeight_swap (graphScore r) a b (rest ++ tail)
        (comparable_score_neutral r b a h1).symm
      simpa only [List.cons_append] using hstep.trans hswap

/-- Universal `(0, k) ↔ (k-1, 1)` cascade in `SignedArrays`: moving the leading entry `b`
of a strict `k`-chain `b :: as` (`as ≠ []`) to an adjacent empty row preserves
`ShapeAt`, `Good`, chain validity, and `graphInversions` for every poset `r` and every `k ≥ 2`. -/
theorem cascade_split_preserves_all (r : Nat → Nat → Prop) [DecidableRel r]
    (lambda : Nat → Nat) (i : Int) (p q b : Nat) (as : List Nat) (tail : Array)
    (hne : as ≠ []) (hchain : (b :: as).Pairwise r) :
    (ShapeAt lambda i ((q, as) :: (p, [b]) :: tail) ↔
      ShapeAt lambda i ((p, []) :: (q, b :: as) :: tail)) ∧
    (Good r ((q, as) :: (p, [b]) :: tail) ↔
      Good r ((p, []) :: (q, b :: as) :: tail)) ∧
    (Good r ((p, [b]) :: tail) ↔ Good r ((q, b :: as) :: tail)) ∧
    graphInversions r (contents ((q, as) :: (p, [b]) :: tail)) =
      graphInversions r (contents ((p, []) :: (q, b :: as) :: tail)) := by
  rcases List.exists_cons_of_ne_nil hne with ⟨a1, as_rest, rfl⟩
  have hba1 : r b a1 := (List.pairwise_cons.mp hchain).1 a1 (by simp)
  have hbas : ∀ a ∈ a1 :: as_rest, r b a := (List.pairwise_cons.mp hchain).1
  refine ⟨?_, ?_, ?_, ?_⟩
  · simp only [ShapeAt, List.length_nil, List.length_cons]
    constructor <;> (rintro ⟨h₁, h₂, ht⟩; exact ⟨by omega, by omega, ht⟩)
  · simp [Good, rows, GoodFirst, FirstPair, hba1]
  · cases tail with
    | nil => rfl
    | cons z tail =>
        rcases z with ⟨s, row⟩
        cases row <;> simp [Good, rows, GoodFirst, FirstPair]
  · simpa [contents, rows, graphInversions] using
      comparable_pass_wordWeight r b (a1 :: as_rest) (contents tail) hbas

/-! ## 4. Kanade–Russell I₁ (KR1) Scale-3 Self-Similarity & 6D Octant Identities -/

/-- The Kanade–Russell I₁ quadratic form `Q(a, b) = a^2 + 3ab + 3b^2`. -/
def kr1Q (a b : Nat) : Nat :=
  a * a + 3 * a * b + 3 * b * b

/-- Scale-3 self-similarity: writing `a = 3c + r` reduces `Q(3c + r, b)` to a residue-`r`
layer plus `3 * Q(b, c)`. -/
theorem kr1_scale3_self_similarity (c r b : Nat) :
    kr1Q (3 * c + r) b = r * r + 3 * r * (b + 2 * c) + 3 * kr1Q b c := by
  unfold kr1Q
  have he : c * (r * (2 * 3)) = 2 * (c * (r * 3)) := by
    rw [← Nat.mul_assoc r 2 3, Nat.mul_comm r 2, Nat.mul_assoc 2 r 3, Nat.mul_left_comm c 2 (r * 3)]
  simp only [Nat.left_distrib, Nat.right_distrib, Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm]
  omega

/-- Pure scale-3 specialization: `Q(3c, b) = 3 * Q(b, c)`. -/
theorem kr1_scale3_divisible (c b : Nat) :
    kr1Q (3 * c) b = 3 * kr1Q b c := by
  have h := kr1_scale3_self_similarity c 0 b
  simpa using h

/-- Universal `(a - 1)`-column head decomposition above the `ν`-baseline `3b(b + 1)`. -/
theorem kr1_head_offset_identity (a b : Nat) (ha : 1 ≤ a) :
    kr1Q a b = 3 * b * (b + 1) + a * a + 3 * (a - 1) * b := by
  unfold kr1Q
  cases a with
  | zero => omega
  | succ m =>
      simp only [Nat.add_sub_cancel, Nat.left_distrib, Nat.right_distrib, Nat.mul_comm]
      omega

/-- Exact weight of the universal 3-divisible core `(3(b+2), 3(b+1), 3b, 3b, ..., 3, 3)` for `a = 3`. -/
theorem kr1_a3_core_weight (b : Nat) :
    3 * (b + 2) + 3 * (b + 1) + 3 * b * (b + 1) = kr1Q 3 b := by
  unfold kr1Q
  simp only [Nat.right_distrib, Nat.mul_comm]
  omega

/-- The 3D Ferrers octant weight decomposition for `(a = 3, b = 0)`:
writing `d2 = 3 * q2 + r2` maps `(q2, d3, d1) ∈ ℕ³` to step weights `(+6, +3, +1)`,
matching `(6^{q2}, 3^{d3}, 1^{d1})`. -/
theorem kr1_a3_b0_octant_weight (q2 r2 d3 d1 : Nat) :
    (9 + 2 * r2) + 6 * q2 + 3 * d3 + d1 =
      kr1Q 3 0 + 3 * d3 + 2 * (3 * q2 + r2) + d1 := by
  unfold kr1Q
  omega

end MultidimensionalFerrers

#print axioms MultidimensionalFerrers.bubble_injective_local_fiber
#print axioms MultidimensionalFerrers.promote32_tableau_valid
#print axioms MultidimensionalFerrers.promote32_tableau_graph_inversions
#print axioms MultidimensionalFerrers.collision_witness_promoted_valid
#print axioms MultidimensionalFerrers.hookBubbleEnd_tableau_valid
#print axioms MultidimensionalFerrers.hookBubbleEnd_tableau_graph_inversions
#print axioms MultidimensionalFerrers.hookBubbleMid_tableau_valid
#print axioms MultidimensionalFerrers.hookBubbleMid_tableau_graph_inversions
#print axioms MultidimensionalFerrers.cascade_split_preserves_all
#print axioms MultidimensionalFerrers.kr1_scale3_self_similarity
#print axioms MultidimensionalFerrers.kr1_scale3_divisible
#print axioms MultidimensionalFerrers.kr1_head_offset_identity
#print axioms MultidimensionalFerrers.kr1_a3_core_weight
#print axioms MultidimensionalFerrers.kr1_a3_b0_octant_weight
