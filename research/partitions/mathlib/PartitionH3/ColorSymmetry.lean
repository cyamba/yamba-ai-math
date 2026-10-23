import PartitionH3.Coloring
import Mathlib.GroupTheory.Perm.Sign

/-!
Adjacent-color involution on actual colorings. The mask depends only on the
two-color vertex support and its induced graph, so applying the map twice
uses exactly the same mask. Polynomial symmetry requires the additional
properness, height-two and adjacent-color arguments below.
-/

open scoped BigOperators

noncomputable section

namespace PartitionH3

def Adj {n : ℕ} (H : NaturalUnitInterval n) (i j : Fin n) : Prop :=
  Edge H i j ∨ Edge H j i

theorem adj_symm {n : ℕ} (H : NaturalUnitInterval n) (i j : Fin n) :
    Adj H i j ↔ Adj H j i := or_comm

def colorPair {n m : ℕ} (κ : Fin n → Fin m) (a b : Fin m) : Finset (Fin n) :=
  Finset.univ.filter (fun i => κ i = a ∨ κ i = b)

@[simp] theorem mem_colorPair {n m : ℕ} (κ : Fin n → Fin m)
    (a b : Fin m) (i : Fin n) : i ∈ colorPair κ a b ↔ κ i = a ∨ κ i = b := by
  simp [colorPair]

def isolated {n : ℕ} (H : NaturalUnitInterval n) (U : Finset (Fin n)) :
    Finset (Fin n) := by
  classical
  exact U.filter (fun i => ∀ j ∈ U, ¬ Adj H i j)

theorem isolated_subset {n : ℕ} (H : NaturalUnitInterval n) (U : Finset (Fin n)) :
    isolated H U ⊆ U := by
  classical
  exact Finset.filter_subset _ _

def toggleMask {n : ℕ} (H : NaturalUnitInterval n) (U : Finset (Fin n)) :
    Finset (Fin n) :=
  if U.card = 3 ∧ isolated H U = ∅ then U else isolated H U

theorem toggleMask_subset {n : ℕ} (H : NaturalUnitInterval n) (U : Finset (Fin n)) :
    toggleMask H U ⊆ U := by
  unfold toggleMask
  split_ifs
  · exact Finset.Subset.refl _
  · exact isolated_subset H U

def flipOn {n m : ℕ} (a b : Fin m) (S : Finset (Fin n))
    (κ : Fin n → Fin m) : Fin n → Fin m :=
  fun i => if i ∈ S then Equiv.swap a b (κ i) else κ i

theorem flipOn_involutive {n m : ℕ} (a b : Fin m) (S : Finset (Fin n))
    (κ : Fin n → Fin m) : flipOn a b S (flipOn a b S κ) = κ := by
  funext i
  by_cases hi : i ∈ S <;> simp [flipOn, hi]

theorem colorPair_flipOn {n m : ℕ} (a b : Fin m) (S : Finset (Fin n))
    (κ : Fin n → Fin m) : colorPair (flipOn a b S κ) a b = colorPair κ a b := by
  ext i
  by_cases hi : i ∈ S
  · by_cases ha : κ i = a
    · simp [flipOn, hi, ha]
    · by_cases hb : κ i = b
      · simp [flipOn, hi, hb]
      · simp [flipOn, hi, Equiv.swap_apply_of_ne_of_ne ha hb, ha, hb]
  · simp [flipOn, hi]

def toggleColors {n m : ℕ} (H : NaturalUnitInterval n) (a b : Fin m)
    (κ : Fin n → Fin m) : Fin n → Fin m :=
  flipOn a b (toggleMask H (colorPair κ a b)) κ

theorem colorPair_toggleColors {n m : ℕ} (H : NaturalUnitInterval n)
    (a b : Fin m) (κ : Fin n → Fin m) :
    colorPair (toggleColors H a b κ) a b = colorPair κ a b :=
  colorPair_flipOn a b _ κ

theorem toggleColors_involutive {n m : ℕ} (H : NaturalUnitInterval n)
    (a b : Fin m) (κ : Fin n → Fin m) :
    toggleColors H a b (toggleColors H a b κ) = κ := by
  unfold toggleColors
  rw [colorPair_flipOn, flipOn_involutive]

theorem swap_lt_outside {m : ℕ} (a b x y : Fin m)
    (hab : b.val = a.val + 1) (hya : y ≠ a) (hyb : y ≠ b) :
    (Equiv.swap a b x < y ↔ x < y) ∧
      (y < Equiv.swap a b x ↔ y < x) := by
  have hya' : y.val ≠ a.val := fun h => hya (Fin.ext h)
  have hyb' : y.val ≠ b.val := fun h => hyb (Fin.ext h)
  by_cases hx : x = a
  · subst x
    simp only [Equiv.swap_apply_left, Fin.lt_def]
    omega
  · by_cases hx' : x = b
    · subst x
      simp only [Equiv.swap_apply_right, Fin.lt_def]
      omega
    · rw [Equiv.swap_apply_of_ne_of_ne hx hx']
      exact ⟨Iff.rfl, Iff.rfl⟩

theorem proper_colorSwap {n m : ℕ} (H : NaturalUnitInterval n)
    (a b : Fin m) (κ : Fin n → Fin m) :
    Proper H (fun i => Equiv.swap a b (κ i)) ↔ Proper H κ := by
  constructor
  · intro hp i j he hc
    exact hp i j he (congrArg (Equiv.swap a b) hc)
  · intro hp i j he hc
    exact hp i j he ((Equiv.swap a b).injective hc)

theorem colorMonomial_colorSwap {n m : ℕ} (a b : Fin m)
    (κ : Fin n → Fin m) :
    colorMonomial (fun i => Equiv.swap a b (κ i)) =
      MvPolynomial.rename (Equiv.swap a b) (colorMonomial κ) := by
  simp [colorMonomial, map_prod, MvPolynomial.rename_X]

theorem proper_neq_of_adj {n m : ℕ} (H : NaturalUnitInterval n)
    (κ : Fin n → Fin m) (hp : Proper H κ) {i j : Fin n} (he : Adj H i j) :
    κ i ≠ κ j := by
  rcases he with he | he
  · exact hp i j he
  · exact (hp j i he).symm

theorem nonadjacent_comparable {n : ℕ} (H : NaturalUnitInterval n)
    {i j : Fin n} (hne : i ≠ j) (he : ¬ Adj H i j) :
    PosetLt H i j ∨ PosetLt H j i := by
  by_cases hij : i < j
  · left
    by_contra h
    exact he (Or.inl ⟨hij, le_of_not_gt h⟩)
  · right
    by_contra h
    exact he (Or.inr ⟨by omega, le_of_not_gt h⟩)

theorem no_three_independent {n : ℕ} (H : NaturalUnitInterval n) (hh : HeightTwo H)
    (x y z : Fin n) (hxy : x ≠ y) (hxz : x ≠ z) (hyz : y ≠ z)
    (h1 : ¬ Adj H x y) (h2 : ¬ Adj H x z) (h3 : ¬ Adj H y z) : False := by
  have go : ∀ u v w : Fin n, u < v → v < w →
      ¬ Adj H u v → ¬ Adj H v w → False := by
    intro u v w huv hvw h uvw
    have huv' : PosetLt H u v := by
      by_contra hc
      exact h (Or.inl ⟨huv, le_of_not_gt hc⟩)
    have hvw' : PosetLt H v w := by
      by_contra hc
      exact uvw (Or.inl ⟨hvw, le_of_not_gt hc⟩)
    exact hh u v w ⟨huv', hvw'⟩
  have h1' : ¬ Adj H y x := fun h => h1 ((adj_symm H y x).mp h)
  have h2' : ¬ Adj H z x := fun h => h2 ((adj_symm H z x).mp h)
  have h3' : ¬ Adj H z y := fun h => h3 ((adj_symm H z y).mp h)
  by_cases h : x < y
  · by_cases h' : y < z
    · exact go x y z h h' h1 h3
    · by_cases h'' : x < z
      · exact go x z y h'' (by omega) h2 h3'
      · exact go z x y (by omega) h h2' h1
  · by_cases h' : x < z
    · exact go y x z (by omega) h' h1' h2
    · by_cases h'' : y < z
      · exact go y z x h'' (by omega) h3 h2'
      · exact go z y x (by omega) (by omega) h3' h1'

theorem isolated_flip_edge {n m : ℕ} (H : NaturalUnitInterval n)
    (a b : Fin m) (κ : Fin n → Fin m) {i j : Fin n} (he : Edge H i j) :
    (i ∈ isolated H (colorPair κ a b) → j ∉ colorPair κ a b) ∧
      (j ∈ isolated H (colorPair κ a b) → i ∉ colorPair κ a b) := by
  classical
  constructor
  · intro hi hj
    exact (Finset.mem_filter.mp hi).2 j hj (Or.inl he)
  · intro hj hi
    exact (Finset.mem_filter.mp hj).2 i hi (Or.inr he)

theorem isolated_flip_proper {n m : ℕ} (H : NaturalUnitInterval n)
    (a b : Fin m) (κ : Fin n → Fin m) (hp : Proper H κ) :
    Proper H (flipOn a b (isolated H (colorPair κ a b)) κ) := by
  intro i j he
  have ho := isolated_flip_edge H a b κ he
  by_cases hi : i ∈ isolated H (colorPair κ a b)
  · have hj : j ∉ isolated H (colorPair κ a b) :=
      fun h => ho.1 hi (isolated_subset H _ h)
    have hc : κ i = a ∨ κ i = b :=
      (mem_colorPair κ a b i).mp (isolated_subset H _ hi)
    have hn : κ j ≠ a ∧ κ j ≠ b := by simpa using ho.1 hi
    rcases hc with hc | hc <;> simp [flipOn, hi, hj, hc, hn.1.symm, hn.2.symm]
  · by_cases hj : j ∈ isolated H (colorPair κ a b)
    · have hc : κ j = a ∨ κ j = b :=
        (mem_colorPair κ a b j).mp (isolated_subset H _ hj)
      have hn : κ i ≠ a ∧ κ i ≠ b := by simpa using ho.2 hj
      rcases hc with hc | hc <;> simp [flipOn, hi, hj, hc, hn.1, hn.2]
    · simpa [flipOn, hi, hj] using hp i j he

theorem isolated_flip_ascent_pair {n m : ℕ} (H : NaturalUnitInterval n)
    (a b : Fin m) (hab : b.val = a.val + 1) (κ : Fin n → Fin m)
    (i j : Fin n) (he : Edge H i j) :
    flipOn a b (isolated H (colorPair κ a b)) κ i <
      flipOn a b (isolated H (colorPair κ a b)) κ j ↔ κ i < κ j := by
  have ho := isolated_flip_edge H a b κ he
  by_cases hi : i ∈ isolated H (colorPair κ a b)
  · have hj : j ∉ isolated H (colorPair κ a b) :=
      fun h => ho.1 hi (isolated_subset H _ h)
    have hn : κ j ≠ a ∧ κ j ≠ b := by simpa using ho.1 hi
    simpa [flipOn, hi, hj] using (swap_lt_outside a b (κ i) (κ j) hab hn.1 hn.2).1
  · by_cases hj : j ∈ isolated H (colorPair κ a b)
    · have hn : κ i ≠ a ∧ κ i ≠ b := by simpa using ho.2 hj
      simpa [flipOn, hi, hj] using (swap_lt_outside a b (κ j) (κ i) hab hn.1 hn.2).2
    · simp [flipOn, hi, hj]

theorem isolated_flip_ascents {n m : ℕ} (H : NaturalUnitInterval n)
    (a b : Fin m) (hab : b.val = a.val + 1) (κ : Fin n → Fin m) :
    ascents H (flipOn a b (isolated H (colorPair κ a b)) κ) = ascents H κ := by
  classical
  unfold ascents
  congr 1
  ext p
  simp only [Finset.mem_filter, Finset.mem_univ, true_and]
  constructor
  · rintro ⟨he, hc⟩
    exact ⟨he, (isolated_flip_ascent_pair H a b hab κ p.1 p.2 he).mp hc⟩
  · rintro ⟨he, hc⟩
    exact ⟨he, (isolated_flip_ascent_pair H a b hab κ p.1 p.2 he).mpr hc⟩

theorem flipOn_colorPair_eq_swap {n m : ℕ} (a b : Fin m)
    (κ : Fin n → Fin m) :
    flipOn a b (colorPair κ a b) κ = fun i => Equiv.swap a b (κ i) := by
  funext i
  by_cases hi : i ∈ colorPair κ a b
  · simp [flipOn, hi]
  · have hn : κ i ≠ a ∧ κ i ≠ b := by simpa using hi
    simp [flipOn, hi, Equiv.swap_apply_of_ne_of_ne hn.1 hn.2]

theorem toggleColors_proper {n m : ℕ} (H : NaturalUnitInterval n)
    (a b : Fin m) (κ : Fin n → Fin m) (hp : Proper H κ) :
    Proper H (toggleColors H a b κ) := by
  unfold toggleColors toggleMask
  split_ifs
  · rw [flipOn_colorPair_eq_swap]
    exact (proper_colorSwap H a b κ).mpr hp
  · exact isolated_flip_proper H a b κ hp

theorem proper_toggleColors_iff {n m : ℕ} (H : NaturalUnitInterval n)
    (a b : Fin m) (κ : Fin n → Fin m) :
    Proper H (toggleColors H a b κ) ↔ Proper H κ := by
  constructor
  · intro hp
    simpa only [toggleColors_involutive] using toggleColors_proper H a b _ hp
  · exact toggleColors_proper H a b κ

theorem middle_of_two_edges {n : ℕ} (H : NaturalUnitInterval n)
    {u v z : Fin n} (hp : PosetLt H u v) (hu : Adj H u z) (hv : Adj H z v) :
    u < z ∧ z < v := by
  have huv := posetLt_implies_lt H hp
  have hzv : z < v := by
    rcases hu with hu | hu
    · exact lt_of_le_of_lt hu.2 hp
    · exact lt_trans hu.1 huv
  have huz : u < z := by
    by_contra hc
    have hzu : z ≤ u := le_of_not_gt hc
    have hm := H.monotone hzu
    rcases hv with hv | hv
    · exact (not_lt_of_ge (le_trans hv.2 hm)) hp
    · exact lt_asymm hzv hv.1
  exact ⟨huz, hzv⟩

theorem swap_ascent_outside {n m : ℕ} (a b : Fin m)
    (hab : b.val = a.val + 1) (κ : Fin n → Fin m) (i j : Fin n)
    (ho : i ∉ colorPair κ a b ∨ j ∉ colorPair κ a b) :
    Equiv.swap a b (κ i) < Equiv.swap a b (κ j) ↔ κ i < κ j := by
  rcases ho with hi | hj
  · have hn : κ i ≠ a ∧ κ i ≠ b := by simpa using hi
    rw [Equiv.swap_apply_of_ne_of_ne hn.1 hn.2]
    exact (swap_lt_outside a b (κ j) (κ i) hab hn.1 hn.2).2
  · have hn : κ j ≠ a ∧ κ j ≠ b := by simpa using hj
    rw [Equiv.swap_apply_of_ne_of_ne hn.1 hn.2]
    exact (swap_lt_outside a b (κ i) (κ j) hab hn.1 hn.2).1

theorem swap_ascent_inside {m : ℕ} (a b x y : Fin m) (hne : a ≠ b)
    (hx : x = a ∨ x = b) (hy : y = a ∨ y = b) (hxy : x ≠ y) :
    Equiv.swap a b x < Equiv.swap a b y ↔ y < x := by
  rcases hx with rfl | rfl <;> rcases hy with rfl | rfl
  · exact (hxy rfl).elim
  · simp
  · simp
  · exact (hxy rfl).elim

theorem no_three_equal_colors {n m : ℕ} (H : NaturalUnitInterval n)
    (hh : HeightTwo H) (κ : Fin n → Fin m) (hp : Proper H κ)
    (x y z : Fin n) (hxy : x ≠ y) (hxz : x ≠ z) (hyz : y ≠ z)
    (hc : κ x = κ y) (hc' : κ x = κ z) : False := by
  apply no_three_independent H hh x y z hxy hxz hyz
  · exact fun he => proper_neq_of_adj H κ hp he hc
  · exact fun he => proper_neq_of_adj H κ hp he hc'
  · exact fun he => proper_neq_of_adj H κ hp he (hc.symm.trans hc')

theorem three_support_pair {n m : ℕ} (H : NaturalUnitInterval n)
    (hh : HeightTwo H) (a b : Fin m) (κ : Fin n → Fin m) (hp : Proper H κ)
    (hcard : (colorPair κ a b).card = 3) :
    ∃ u v z : Fin n, u < v ∧ u ≠ z ∧ v ≠ z ∧
      colorPair κ a b = {u, v, z} ∧ κ u = κ v ∧ κ z ≠ κ u := by
  classical
  obtain ⟨x, y, z, hxy, hxz, hyz, hs⟩ := Finset.card_eq_three.mp hcard
  have go : ∀ x y z : Fin n, x ≠ y → x ≠ z → y ≠ z →
      colorPair κ a b = {x, y, z} → κ x = κ y → κ z ≠ κ x →
      ∃ u v z : Fin n, u < v ∧ u ≠ z ∧ v ≠ z ∧
        colorPair κ a b = {u, v, z} ∧ κ u = κ v ∧ κ z ≠ κ u := by
    intro x y z hxy hxz hyz hs hc hd
    by_cases ho : x < y
    · exact ⟨x, y, z, ho, hxz, hyz, hs, hc, hd⟩
    · exact ⟨y, x, z, by omega, hyz, hxz,
        by simpa only [Finset.insert_comm] using hs,
        hc.symm, by simpa only [← hc] using hd⟩
  by_cases hc : κ x = κ y
  · apply go x y z hxy hxz hyz hs hc
    intro hd
    exact no_three_equal_colors H hh κ hp x y z hxy hxz hyz hc hd.symm
  · by_cases hc' : κ x = κ z
    · apply go x z y hxz hxy hyz.symm
      · simpa only [Finset.pair_comm] using hs
      · exact hc'
      · exact Ne.symm hc
    · have hx : κ x = a ∨ κ x = b := by rw [← mem_colorPair, hs]; simp
      have hy : κ y = a ∨ κ y = b := by rw [← mem_colorPair, hs]; simp
      have hz : κ z = a ∨ κ z = b := by rw [← mem_colorPair, hs]; simp
      have hyz' : κ y = κ z := by rcases hx with hx | hx <;>
        rcases hy with hy | hy <;> rcases hz with hz | hz <;> simp_all
      apply go y z x hyz hxy.symm hxz.symm
      · rw [hs]; ext t; simp only [Finset.mem_insert, Finset.mem_singleton]; tauto
      · exact hyz'
      · exact hc

@[simp] theorem not_adj_self {n : ℕ} (H : NaturalUnitInterval n) (i : Fin n) :
    ¬ Adj H i i := by simp [Adj, Edge]

theorem three_support_path {n m : ℕ} (H : NaturalUnitInterval n)
    (hh : HeightTwo H) (a b : Fin m) (κ : Fin n → Fin m) (hp : Proper H κ)
    (hcard : (colorPair κ a b).card = 3)
    (hiso : isolated H (colorPair κ a b) = ∅) :
    ∃ u v z : Fin n, u < z ∧ z < v ∧
      colorPair κ a b = {u, v, z} ∧ κ u = κ v ∧ κ z ≠ κ u ∧
      Edge H u z ∧ Edge H z v := by
  classical
  obtain ⟨u, v, z, huv, huz, hvz, hs, hc, hd⟩ :=
    three_support_pair H hh a b κ hp hcard
  have hna : ¬ Adj H u v := fun he => proper_neq_of_adj H κ hp he hc
  have hu : Adj H u z := by
    by_contra he
    have hi : u ∈ isolated H (colorPair κ a b) := by
      apply Finset.mem_filter.mpr
      refine ⟨by rw [hs]; simp, ?_⟩
      intro j hj
      rw [hs] at hj
      simp only [Finset.mem_insert, Finset.mem_singleton] at hj
      rcases hj with hj | hj | hj <;> subst j
      · exact not_adj_self H u
      · exact hna
      · exact he
    simp [hiso] at hi
  have hv : Adj H z v := by
    by_contra he
    have hi : v ∈ isolated H (colorPair κ a b) := by
      apply Finset.mem_filter.mpr
      refine ⟨by rw [hs]; simp, ?_⟩
      intro j hj
      rw [hs] at hj
      simp only [Finset.mem_insert, Finset.mem_singleton] at hj
      rcases hj with hj | hj | hj <;> subst j
      · exact fun h => hna ((adj_symm H v u).mp h)
      · exact not_adj_self H v
      · exact fun h => he ((adj_symm H v z).mp h)
    simp [hiso] at hi
  have hm := middle_of_two_edges H (same_color_comparable H κ hp huv hc) hu hv
  refine ⟨u, v, z, hm.1, hm.2, hs, hc, hd, ?_, ?_⟩
  · rcases hu with hu | hu
    · exact hu
    · exact (lt_asymm hm.1 hu.1).elim
  · rcases hv with hv | hv
    · exact hv
    · exact (lt_asymm hm.2 hv.1).elim

theorem path_internal_edges {n m : ℕ} (H : NaturalUnitInterval n)
    (a b : Fin m) (κ : Fin n → Fin m) (hp : Proper H κ)
    (u v z : Fin n) (huz : u < z) (hzv : z < v)
    (hs : colorPair κ a b = {u, v, z}) (hc : κ u = κ v)
    (heu : Edge H u z) (hev : Edge H z v) (i j : Fin n)
    (hi : i ∈ colorPair κ a b) (hj : j ∈ colorPair κ a b) :
    Edge H i j ↔ (i = u ∧ j = z) ∨ (i = z ∧ j = v) := by
  have hne : ¬ Edge H u v := fun h => hp u v h hc
  rw [hs] at hi hj
  simp only [Finset.mem_insert, Finset.mem_singleton] at hi hj
  rcases hi with hi | hi | hi <;> rcases hj with hj | hj | hj <;>
    subst i <;> subst j <;> simp_all [Edge] <;> omega

theorem path_colorSwap_ascents {n m : ℕ} (H : NaturalUnitInterval n)
    (a b : Fin m) (hab : b.val = a.val + 1) (κ : Fin n → Fin m)
    (hp : Proper H κ) (u v z : Fin n) (huz : u < z) (hzv : z < v)
    (hs : colorPair κ a b = {u, v, z}) (hc : κ u = κ v)
    (hd : κ z ≠ κ u) (heu : Edge H u z) (hev : Edge H z v) :
    ascents H (fun i => Equiv.swap a b (κ i)) = ascents H κ := by
  classical
  have hne : a ≠ b := by intro h; have := congrArg Fin.val h; omega
  have hcu : κ u = a ∨ κ u = b := by rw [← mem_colorPair, hs]; simp
  have hcv : κ v = a ∨ κ v = b := by rw [← mem_colorPair, hs]; simp
  have hcz : κ z = a ∨ κ z = b := by rw [← mem_colorPair, hs]; simp
  have hzv' : κ z ≠ κ v := by simpa only [← hc] using hd
  have hswp : Equiv.swap a b (κ u) < Equiv.swap a b (κ z) ↔ κ z < κ v := by
    simpa only [hc] using swap_ascent_inside a b (κ u) (κ z) hne hcu hcz hd.symm
  have hswq : Equiv.swap a b (κ z) < Equiv.swap a b (κ v) ↔ κ u < κ z := by
    simpa only [hc] using swap_ascent_inside a b (κ z) (κ v) hne hcz hcv hzv'
  unfold ascents
  apply Finset.card_equiv (Equiv.swap (u, z) (z, v))
  intro p
  simp only [Finset.mem_filter, Finset.mem_univ, true_and]
  by_cases hpu : p = (u, z)
  · subst p
    simpa only [Equiv.swap_apply_left, heu, hev, true_and] using hswp
  · by_cases hpv : p = (z, v)
    · subst p
      simpa only [Equiv.swap_apply_right, heu, hev, true_and] using hswq
    · rw [Equiv.swap_apply_of_ne_of_ne hpu hpv]
      by_cases he : Edge H p.1 p.2
      · have ho : p.1 ∉ colorPair κ a b ∨ p.2 ∉ colorPair κ a b := by
          by_contra hn
          push Not at hn
          have he' := (path_internal_edges H a b κ hp u v z huz hzv hs hc
            heu hev p.1 p.2 hn.1 hn.2).mp he
          rcases he' with ⟨hi, hj⟩ | ⟨hi, hj⟩
          · exact hpu (Prod.ext hi hj)
          · exact hpv (Prod.ext hi hj)
        simpa only [he, true_and] using swap_ascent_outside a b hab κ p.1 p.2 ho
      · simp [he]

theorem toggleColors_ascents {n m : ℕ} (H : NaturalUnitInterval n)
    (hh : HeightTwo H) (a b : Fin m) (hab : b.val = a.val + 1)
    (κ : Fin n → Fin m) (hp : Proper H κ) :
    ascents H (toggleColors H a b κ) = ascents H κ := by
  unfold toggleColors toggleMask
  split_ifs with h
  · rw [flipOn_colorPair_eq_swap]
    obtain ⟨u, v, z, huz, hzv, hs, hc, hd, heu, hev⟩ :=
      three_support_path H hh a b κ hp h.1 h.2
    exact path_colorSwap_ascents H a b hab κ hp u v z huz hzv hs hc hd heu hev
  · exact isolated_flip_ascents H a b hab κ

def nonisolated {n : ℕ} (H : NaturalUnitInterval n) (U : Finset (Fin n)) :=
  U \ isolated H U

theorem nonisolated_neighbor {n : ℕ} (H : NaturalUnitInterval n)
    (U : Finset (Fin n)) (i : Fin n) (hi : i ∈ nonisolated H U) :
    ∃ j ∈ nonisolated H U, Adj H i j := by
  classical
  have hiU := (Finset.mem_sdiff.mp hi).1
  have hiI := (Finset.mem_sdiff.mp hi).2
  have hex : ∃ j ∈ U, Adj H i j := by
    by_contra hn
    push Not at hn
    exact hiI (Finset.mem_filter.mpr ⟨hiU, hn⟩)
  obtain ⟨j, hjU, he⟩ := hex
  refine ⟨j, Finset.mem_sdiff.mpr ⟨hjU, ?_⟩, he⟩
  intro hjI
  exact (Finset.mem_filter.mp hjI).2 i hiU ((adj_symm H i j).mp he)

theorem nonisolated_class_le_one {n m : ℕ} (H : NaturalUnitInterval n)
    (hh : HeightTwo H) (κ : Fin n → Fin m) (hp : Proper H κ)
    (U : Finset (Fin n)) (hI : (isolated H U).Nonempty) (c : Fin m) :
    ((nonisolated H U).filter (fun i => κ i = c)).card ≤ 1 := by
  classical
  obtain ⟨x, hx⟩ := hI
  by_contra hn
  obtain ⟨y, hy, z, hz, hyz⟩ := Finset.one_lt_card.mp (by omega :
    1 < ((nonisolated H U).filter (fun i => κ i = c)).card)
  have hyN := (Finset.mem_filter.mp hy).1
  have hzN := (Finset.mem_filter.mp hz).1
  have hxy : x ≠ y := by intro h; subst y; exact (Finset.mem_sdiff.mp hyN).2 hx
  have hxz : x ≠ z := by intro h; subst z; exact (Finset.mem_sdiff.mp hzN).2 hx
  apply no_three_independent H hh x y z hxy hxz hyz
  · exact (Finset.mem_filter.mp hx).2 y (Finset.mem_sdiff.mp hyN).1
  · exact (Finset.mem_filter.mp hx).2 z (Finset.mem_sdiff.mp hzN).1
  · intro he
    exact proper_neq_of_adj H κ hp he
      ((Finset.mem_filter.mp hy).2.trans (Finset.mem_filter.mp hz).2.symm)

theorem nonisolated_binary_nonempty {n m : ℕ} (H : NaturalUnitInterval n)
    (a b : Fin m) (κ : Fin n → Fin m) (hp : Proper H κ) :
    ((nonisolated H (colorPair κ a b)).filter (fun i => κ i = a)).Nonempty ↔
      ((nonisolated H (colorPair κ a b)).filter (fun i => κ i = b)).Nonempty := by
  classical
  have go : ∀ c d : Fin m, (c = a ∧ d = b) ∨ (c = b ∧ d = a) →
      ((nonisolated H (colorPair κ a b)).filter (fun i => κ i = c)).Nonempty →
      ((nonisolated H (colorPair κ a b)).filter (fun i => κ i = d)).Nonempty := by
    intro c d hcd ⟨i, hi⟩
    have hiN := (Finset.mem_filter.mp hi).1
    have hic := (Finset.mem_filter.mp hi).2
    obtain ⟨j, hj, he⟩ := nonisolated_neighbor H _ i hiN
    have hjab := (mem_colorPair κ a b j).mp (Finset.mem_sdiff.mp hj).1
    have hji := proper_neq_of_adj H κ hp he
    have hjd : κ j = d := by rcases hcd with ⟨rfl, rfl⟩ | ⟨rfl, rfl⟩ <;>
      rcases hjab with hjab | hjab <;> simp_all
    exact ⟨j, Finset.mem_filter.mpr ⟨hj, hjd⟩⟩
  exact ⟨go a b (Or.inl ⟨rfl, rfl⟩), go b a (Or.inr ⟨rfl, rfl⟩)⟩

theorem nonisolated_balanced_of_isolated {n m : ℕ} (H : NaturalUnitInterval n)
    (hh : HeightTwo H) (a b : Fin m) (κ : Fin n → Fin m) (hp : Proper H κ)
    (hI : (isolated H (colorPair κ a b)).Nonempty) :
    ((nonisolated H (colorPair κ a b)).filter (fun i => κ i = a)).card =
      ((nonisolated H (colorPair κ a b)).filter (fun i => κ i = b)).card := by
  have ha := nonisolated_class_le_one H hh κ hp _ hI a
  have hb := nonisolated_class_le_one H hh κ hp _ hI b
  have he := nonisolated_binary_nonempty H a b κ hp
  rw [← Finset.card_pos, ← Finset.card_pos] at he
  omega

theorem binary_card_split {n m : ℕ} (a b : Fin m) (hne : a ≠ b)
    (κ : Fin n → Fin m) (S : Finset (Fin n)) (hs : S ⊆ colorPair κ a b) :
    S.card = (S.filter (fun i => κ i = a)).card +
      (S.filter (fun i => κ i = b)).card := by
  classical
  have hu : S.filter (fun i => κ i = a) ∪ S.filter (fun i => κ i = b) = S := by
    ext i
    simp only [Finset.mem_union, Finset.mem_filter]
    constructor
    · rintro (⟨hi, _⟩ | ⟨hi, _⟩) <;> exact hi
    · intro hi
      rcases (mem_colorPair κ a b i).mp (hs hi) with ha | hb
      · exact Or.inl ⟨hi, ha⟩
      · exact Or.inr ⟨hi, hb⟩
  have hd : Disjoint (S.filter (fun i => κ i = a))
      (S.filter (fun i => κ i = b)) := by
    apply Finset.disjoint_left.mpr
    intro i hi hj
    exact hne ((Finset.mem_filter.mp hi).2.symm.trans (Finset.mem_filter.mp hj).2)
  rw [← Finset.card_union_of_disjoint hd, hu]

theorem colorPair_fiber {n m : ℕ} (a b : Fin m) (κ : Fin n → Fin m) :
    (colorPair κ a b).filter (fun i => κ i = a) = colorClass κ a ∧
      (colorPair κ a b).filter (fun i => κ i = b) = colorClass κ b := by
  constructor <;> ext i <;> simp [colorPair, colorClass] <;> tauto

theorem unflipped_balanced {n m : ℕ} (H : NaturalUnitInterval n)
    (hh : HeightTwo H) (a b : Fin m) (hne : a ≠ b)
    (κ : Fin n → Fin m) (hp : Proper H κ) :
    ((colorPair κ a b \ toggleMask H (colorPair κ a b)).filter
      (fun i => κ i = a)).card =
    ((colorPair κ a b \ toggleMask H (colorPair κ a b)).filter
      (fun i => κ i = b)).card := by
  classical
  unfold toggleMask
  split_ifs with h
  · simp
  · by_cases hI : (isolated H (colorPair κ a b)).Nonempty
    · exact nonisolated_balanced_of_isolated H hh a b κ hp hI
    · have he : isolated H (colorPair κ a b) = ∅ := Finset.not_nonempty_iff_eq_empty.mp hI
      have hn : (colorPair κ a b).card ≠ 3 := fun hc => h ⟨hc, he⟩
      have hs := binary_card_split a b hne κ (colorPair κ a b) (Finset.Subset.refl _)
      have ha := colorClass_card_le_two H hh κ hp a
      have hb := colorClass_card_le_two H hh κ hp b
      have hne' := nonisolated_binary_nonempty H a b κ hp
      simp only [nonisolated, he, Finset.sdiff_empty] at hne'
      rw [← Finset.card_pos, ← Finset.card_pos] at hne'
      rw [(colorPair_fiber a b κ).1, (colorPair_fiber a b κ).2] at hs hne'
      simp only [he, Finset.sdiff_empty, (colorPair_fiber a b κ).1,
        (colorPair_fiber a b κ).2]
      omega

theorem prod_colorPowers {n m : ℕ} (κ : Fin n → Fin m)
    (S : Finset (Fin n)) (f : Fin m → Poly m) :
    (∏ i ∈ S, f (κ i)) = ∏ c, f c ^ (S.filter (fun i => κ i = c)).card := by
  classical
  rw [← Finset.prod_fiberwise' S κ f]
  simp only [Finset.prod_const]

theorem prod_colorSwap_of_balanced {n m : ℕ} (a b : Fin m)
    (κ : Fin n → Fin m) (S : Finset (Fin n))
    (hc : (S.filter (fun i => κ i = a)).card = (S.filter (fun i => κ i = b)).card) :
    (∏ i ∈ S, (MvPolynomial.X (Equiv.swap a b (κ i)) : Poly m)) =
      ∏ i ∈ S, (MvPolynomial.X (κ i) : Poly m) := by
  classical
  have hf : ∀ c, (S.filter (fun i => κ i = c)).card =
      (S.filter (fun i => κ i = Equiv.swap a b c)).card := by
    intro c
    by_cases ha : c = a
    · subst c; simpa using hc
    · by_cases hb : c = b
      · subst c; simpa using hc.symm
      · rw [Equiv.swap_apply_of_ne_of_ne ha hb]
  rw [prod_colorPowers κ S (fun c => MvPolynomial.X (Equiv.swap a b c)),
    prod_colorPowers κ S (fun c => MvPolynomial.X c)]
  calc
    _ = ∏ c, (MvPolynomial.X (Equiv.swap a b c) : Poly m) ^
        (S.filter (fun i => κ i = Equiv.swap a b c)).card := by
      apply Finset.prod_congr rfl
      intro c _
      rw [hf]
    _ = _ := Equiv.prod_comp (Equiv.swap a b)
      (fun c => (MvPolynomial.X c : Poly m) ^ (S.filter (fun i => κ i = c)).card)

theorem complement_pair_fiber {n m : ℕ} (a b c : Fin m)
    (hc : c = a ∨ c = b) (κ : Fin n → Fin m) (S : Finset (Fin n)) :
    Sᶜ.filter (fun i => κ i = c) =
      (colorPair κ a b \ S).filter (fun i => κ i = c) := by
  classical
  ext i
  simp only [Finset.mem_filter, Finset.mem_compl, Finset.mem_sdiff, mem_colorPair]
  rcases hc with rfl | rfl <;> tauto

theorem colorMonomial_flipOn_of_balanced {n m : ℕ} (a b : Fin m)
    (κ : Fin n → Fin m) (S : Finset (Fin n))
    (hc : (Sᶜ.filter (fun i => κ i = a)).card =
      (Sᶜ.filter (fun i => κ i = b)).card) :
    colorMonomial (flipOn a b S κ) =
      MvPolynomial.rename (Equiv.swap a b) (colorMonomial κ) := by
  classical
  rw [← colorMonomial_colorSwap]
  unfold colorMonomial
  rw [← Finset.prod_mul_prod_compl S, ← Finset.prod_mul_prod_compl S]
  congr 1
  · apply Finset.prod_congr rfl
    intro i hi
    simp [flipOn, hi]
  · calc
      _ = ∏ i ∈ Sᶜ, (MvPolynomial.X (κ i) : Poly m) := by
        apply Finset.prod_congr rfl
        intro i hi
        simp [flipOn, Finset.mem_compl.mp hi]
      _ = _ := (prod_colorSwap_of_balanced a b κ Sᶜ hc).symm

theorem colorMonomial_toggleColors {n m : ℕ} (H : NaturalUnitInterval n)
    (hh : HeightTwo H) (a b : Fin m) (hne : a ≠ b)
    (κ : Fin n → Fin m) (hp : Proper H κ) :
    colorMonomial (toggleColors H a b κ) =
      MvPolynomial.rename (Equiv.swap a b) (colorMonomial κ) := by
  apply colorMonomial_flipOn_of_balanced
  rw [complement_pair_fiber a b a (Or.inl rfl),
    complement_pair_fiber a b b (Or.inr rfl)]
  exact unflipped_balanced H hh a b hne κ hp

theorem chromatic_adjacent_swap {n m : ℕ} (H : NaturalUnitInterval n)
    (hh : HeightTwo H) (a b : Fin m) (hab : b.val = a.val + 1) :
    MvPolynomial.rename (Equiv.swap a b) (chromatic H m) = chromatic H m := by
  classical
  have hne : a ≠ b := by intro h; have := congrArg Fin.val h; omega
  let e : (Fin n → Fin m) ≃ (Fin n → Fin m) :=
    Function.Involutive.toPerm (toggleColors H a b) (toggleColors_involutive H a b)
  unfold chromatic
  rw [map_sum]
  apply Fintype.sum_equiv e
  intro κ
  change MvPolynomial.rename (Equiv.swap a b)
    (if Proper H κ then MvPolynomial.C (Polynomial.X ^ ascents H κ) * colorMonomial κ
      else 0) =
    if Proper H (toggleColors H a b κ) then
      MvPolynomial.C (Polynomial.X ^ ascents H (toggleColors H a b κ)) *
        colorMonomial (toggleColors H a b κ) else 0
  by_cases hp : Proper H κ
  · simp only [hp, proper_toggleColors_iff, reduceIte, map_mul, MvPolynomial.rename_C,
      toggleColors_ascents H hh a b hab κ hp,
      colorMonomial_toggleColors H hh a b hne κ hp]
  · simp [hp, proper_toggleColors_iff]

theorem isSymmetric_of_adjacent {m : ℕ} (p : Poly m)
    (h : ∀ a b : Fin m, b.val = a.val + 1 →
      MvPolynomial.rename (Equiv.swap a b) p = p) : MvPolynomial.IsSymmetric p := by
  classical
  let S : Submonoid (Equiv.Perm (Fin m)) := {
    carrier := {sigma | MvPolynomial.rename sigma p = p}
    one_mem' := by simp
    mul_mem' := by
      intro sigma tau hs ht
      change MvPolynomial.rename (sigma * tau) p = p
      have hc : MvPolynomial.rename (sigma * tau) p =
          MvPolynomial.rename sigma (MvPolynomial.rename tau p) := by
        rw [MvPolynomial.rename_rename]
        rfl
      rw [hc, ht, hs] }
  have htop : S = ⊤ := by
    cases m with
    | zero =>
      apply top_unique
      intro sigma _
      have he : sigma = 1 := Subsingleton.elim _ _
      simpa only [he] using S.one_mem
    | succ k =>
      have hg : Submonoid.closure
          (Set.range fun i : Fin k => Equiv.swap i.castSucc i.succ) ≤ S := by
        apply Submonoid.closure_le.mpr
        rintro _ ⟨i, rfl⟩
        exact h i.castSucc i.succ rfl
      rw [Equiv.Perm.mclosure_swap_castSucc_succ] at hg
      exact top_unique hg
  intro sigma
  have hm : sigma ∈ S := by rw [htop]; trivial
  exact hm

theorem chromatic_isSymmetric {n m : ℕ} (H : NaturalUnitInterval n)
    (hh : HeightTwo H) : MvPolynomial.IsSymmetric (chromatic H m) :=
  isSymmetric_of_adjacent _ (chromatic_adjacent_swap H hh)

end PartitionH3

#check @PartitionH3.toggleColors_involutive
#print axioms PartitionH3.toggleColors_involutive
#print axioms PartitionH3.swap_lt_outside
#check @PartitionH3.chromatic_isSymmetric
#print axioms PartitionH3.proper_toggleColors_iff
#print axioms PartitionH3.middle_of_two_edges
#print axioms PartitionH3.path_internal_edges
#print axioms PartitionH3.toggleColors_ascents
#print axioms PartitionH3.unflipped_balanced
#print axioms PartitionH3.colorMonomial_toggleColors
#print axioms PartitionH3.chromatic_adjacent_swap
#print axioms PartitionH3.isSymmetric_of_adjacent
#print axioms PartitionH3.chromatic_isSymmetric
