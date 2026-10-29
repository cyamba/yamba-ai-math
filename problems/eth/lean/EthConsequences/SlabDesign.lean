import Mathlib.LinearAlgebra.Lagrange
import Mathlib.LinearAlgebra.Finsupp.LinearCombination
import Mathlib.Algebra.Polynomial.BigOperators
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Data.Nat.Choose.Sum

/-!
# Global formulas and the slab construction (subresult SR-04)

Point-dependent designs in the swap algebra of openai/math result 378 reduce to the *cube
polynomial problem* (SR-02): attach to every vertex `ε` of `{0,1}^Q` (encoded by its support
`ε : Finset (Fin Q)`) a polynomial `p ε` of degree `< R` with `p ε (0) = 1`; the edge
`(ε, insert t ε)` in direction `t` is good when `p ε (x t) + p (insert t ε) (x t) = 0`. Bad
edges in direction `t` are the measurements needed at node `t`.

This file proves:

* `G_edge`: a **global formula** `G(T, ε) = ∑_S γ_S χ_S(ε) ∏_{s∈S} (1 - T/x_s)` takes the same
  value at both ends of every edge in direction `t` when evaluated at `T = x t`. Its degree is
  at most the largest `|S|` with `γ_S ≠ 0`, and `G(0, ε) = ∑_S γ_S χ_S(ε)`.
* `exists_gamma`: every polynomial of degree `≤ d` in the Hamming weight `|ε|` is a combination
  of characters `χ_S` with `|S| ≤ d` (characteristic zero).
* `slab_design`: cutting the weights `0, …, Q` into slabs of `R` consecutive values and using on
  each slab the global formula whose value at `0` interpolates `(-1)^{|ε|}` there, every edge
  inside a slab is good.
* `slab_design_bound`: for a suitable offset of the slabs, **in every direction at most a
  `1/R` fraction of the edges is bad**, for every `Q`.

The single-matrix construction of the preprint fails on a Gaussian fraction
`≈ exp(-R²/(8Q))` of the edges (SR-01 shows this is optimal for single-matrix designs); the slab
construction fails on at most `1/R`, independently of `Q`. The general lower bound for
point-dependent designs is exponential in `R` (`PointDependentBarrier.lean`, SR-03).
-/

namespace EthConsequences.SlabDesign

open Finset Polynomial

variable {K : Type*} [Field K] {Q : ℕ}

/-- Characters of the cube, with a vertex encoded by its support. -/
def chi (S ε : Finset (Fin Q)) : K := ∏ s ∈ S, if s ∈ ε then (-1 : K) else 1

theorem chi_empty (ε : Finset (Fin Q)) : chi (K := K) ∅ ε = 1 := by simp [chi]

theorem chi_insert_of_notMem {S ε : Finset (Fin Q)} {t : Fin Q} (ht : t ∉ S) :
    chi (K := K) S (insert t ε) = chi S ε := by
  unfold chi
  refine Finset.prod_congr rfl fun s hs => ?_
  have hst : s ≠ t := fun h => ht (h ▸ hs)
  simp [Finset.mem_insert, hst]

/-- Multiplying by a one-coordinate sign moves a character by a symmetric difference. -/
theorem chi_symmDiff_singleton (S ε : Finset (Fin Q)) (s : Fin Q) :
    chi (K := K) (symmDiff S {s}) ε = (if s ∈ ε then (-1 : K) else 1) * chi S ε := by
  by_cases hs : s ∈ S
  · have h1 : symmDiff S {s} = S.erase s := by
      ext a
      simp only [Finset.mem_symmDiff, Finset.mem_singleton, Finset.mem_erase]
      constructor
      · rintro (⟨ha, hne⟩ | ⟨rfl, hna⟩)
        · exact ⟨hne, ha⟩
        · exact absurd hs hna
      · rintro ⟨hne, ha⟩
        exact Or.inl ⟨ha, hne⟩
    rw [h1]
    unfold chi
    rw [← Finset.mul_prod_erase S _ hs, ← mul_assoc]
    by_cases hε : s ∈ ε <;> simp [hε]
  · have h1 : symmDiff S {s} = insert s S := by
      ext a
      simp only [Finset.mem_symmDiff, Finset.mem_singleton, Finset.mem_insert]
      constructor
      · rintro (⟨ha, _⟩ | ⟨rfl, _⟩)
        · exact Or.inr ha
        · exact Or.inl rfl
      · rintro (rfl | ha)
        · exact Or.inr ⟨rfl, hs⟩
        · exact Or.inl ⟨ha, fun h => hs (h ▸ ha)⟩
    rw [h1]
    unfold chi
    rw [Finset.prod_insert hs]

/-- `φ_S(T) = ∏_{s ∈ S} (1 - T / x_s)`. -/
noncomputable def phi (x : Fin Q → K) (S : Finset (Fin Q)) : K[X] :=
  ∏ s ∈ S, (1 - C (x s)⁻¹ * X)

theorem phi_eval_node {x : Fin Q → K} (hx : ∀ t, x t ≠ 0) {S : Finset (Fin Q)} {t : Fin Q}
    (ht : t ∈ S) : (phi x S).eval (x t) = 0 := by
  unfold phi
  rw [eval_prod]
  apply Finset.prod_eq_zero ht
  simp [hx t]

theorem phi_eval_zero (x : Fin Q → K) (S : Finset (Fin Q)) : (phi x S).eval 0 = 1 := by
  simp [phi, eval_prod]

theorem natDegree_phi_le (x : Fin Q → K) (S : Finset (Fin Q)) :
    (phi x S).natDegree ≤ S.card := by
  unfold phi
  refine (natDegree_prod_le _ _).trans ?_
  calc ∑ s ∈ S, (1 - C (x s)⁻¹ * X).natDegree ≤ ∑ _s ∈ S, 1 := by
        refine Finset.sum_le_sum fun s _ => ?_
        refine (natDegree_sub_le _ _).trans ?_
        simp only [natDegree_one, zero_le, max_le_iff, true_and]
        exact (natDegree_C_mul_le _ _).trans natDegree_X_le
    _ = S.card := by simp

/-- A global formula `G(T, ε) = ∑_S γ_S χ_S(ε) φ_S(T)`. -/
noncomputable def G (x : Fin Q → K) (γ : Finset (Fin Q) → K) (ε : Finset (Fin Q)) : K[X] :=
  ∑ S, C (γ S * chi S ε) * phi x S

theorem G_eval_zero (x : Fin Q → K) (γ : Finset (Fin Q) → K) (ε : Finset (Fin Q)) :
    (G x γ ε).eval 0 = ∑ S, γ S * chi S ε := by
  simp [G, eval_finsetSum, phi_eval_zero]

/-- **Global formulas never fail on an edge**: at `T = x t` both ends of an edge in direction
`t` give the same value. -/
theorem G_edge {x : Fin Q → K} (hx : ∀ t, x t ≠ 0) (γ : Finset (Fin Q) → K)
    {ε : Finset (Fin Q)} (t : Fin Q) :
    (G x γ (insert t ε)).eval (x t) = (G x γ ε).eval (x t) := by
  unfold G
  simp only [eval_finsetSum, eval_mul, eval_C]
  refine Finset.sum_congr rfl fun S _ => ?_
  by_cases htS : t ∈ S
  · rw [phi_eval_node hx htS, mul_zero, mul_zero]
  · rw [chi_insert_of_notMem htS]

theorem natDegree_G_le (x : Fin Q → K) (γ : Finset (Fin Q) → K) {d : ℕ}
    (hγ : ∀ S, d < S.card → γ S = 0) (ε : Finset (Fin Q)) : (G x γ ε).natDegree ≤ d := by
  unfold G
  refine natDegree_sum_le_of_forall_le _ _ fun S _ => ?_
  by_cases hS : d < S.card
  · simp [hγ S hS]
  · exact (natDegree_C_mul_le _ _).trans ((natDegree_phi_le x S).trans (by omega))

/-! ### Low Fourier degree of symmetric polynomials -/

/-- Generators of the span of characters of degree at most `d`. -/
def gen (d : ℕ) (S : Finset (Fin Q)) : Finset (Fin Q) → K :=
  if S.card ≤ d then fun ε => chi S ε else 0

/-- Functions on the cube of Fourier degree at most `d`. -/
def lowSpan (K : Type*) [Field K] (Q d : ℕ) : Submodule K (Finset (Fin Q) → K) :=
  Submodule.span K (Set.range (gen (K := K) (Q := Q) d))

theorem chi_mem_lowSpan {d : ℕ} {S : Finset (Fin Q)} (h : S.card ≤ d) :
    (fun ε => chi (K := K) S ε) ∈ lowSpan K Q d := by
  apply Submodule.subset_span
  exact ⟨S, by simp [gen, h]⟩

theorem lowSpan_mono {d e : ℕ} (h : d ≤ e) : lowSpan K Q d ≤ lowSpan K Q e := by
  apply Submodule.span_le.2
  rintro _ ⟨S, rfl⟩
  unfold gen
  split_ifs with hS
  · exact chi_mem_lowSpan (hS.trans h)
  · exact Submodule.zero_mem _

/-- Multiplication by the Hamming weight, as a linear map. -/
def weightMul (K : Type*) [Field K] (Q : ℕ) :
    (Finset (Fin Q) → K) →ₗ[K] (Finset (Fin Q) → K) where
  toFun f ε := (ε.card : K) * f ε
  map_add' f g := by ext ε; simp [mul_add]
  map_smul' c f := by ext ε; simp [mul_left_comm]

theorem card_symmDiff_singleton_le (S : Finset (Fin Q)) (s : Fin Q) :
    (symmDiff S {s}).card ≤ S.card + 1 := by
  calc (symmDiff S {s}).card ≤ (S ∪ {s}).card := Finset.card_le_card symmDiff_le_sup
    _ ≤ S.card + ({s} : Finset (Fin Q)).card := Finset.card_union_le _ _
    _ = S.card + 1 := by rw [Finset.card_singleton]

theorem weightMul_chi_mem (h2 : (2 : K) ≠ 0) {d : ℕ} {S : Finset (Fin Q)} (hS : S.card ≤ d) :
    weightMul K Q (fun ε => chi S ε) ∈ lowSpan K Q (d + 1) := by
  have key : weightMul K Q (fun ε => chi S ε)
      = ∑ s : Fin Q, (2⁻¹ : K) •
          ((fun ε => chi (K := K) S ε) - fun ε => chi (symmDiff S {s}) ε) := by
    ext ε
    simp only [weightMul, LinearMap.coe_mk, AddHom.coe_mk, Finset.sum_apply, Pi.smul_apply,
      Pi.sub_apply, smul_eq_mul, chi_symmDiff_singleton]
    have hcard : (ε.card : K) = ∑ s : Fin Q, (if s ∈ ε then (1 : K) else 0) := by
      rw [Finset.sum_boole, Finset.filter_mem_eq_inter, Finset.univ_inter]
    rw [hcard, Finset.sum_mul]
    refine Finset.sum_congr rfl fun s _ => ?_
    by_cases hs : s ∈ ε
    · simp only [hs, ↓reduceIte]
      field_simp
      ring
    · simp [hs]
  rw [key]
  refine Submodule.sum_mem _ fun s _ => Submodule.smul_mem _ _ (Submodule.sub_mem _ ?_ ?_)
  · exact lowSpan_mono (Nat.le_succ d) (chi_mem_lowSpan hS)
  · exact chi_mem_lowSpan ((card_symmDiff_singleton_le S s).trans (by omega))

theorem weightMul_mem (h2 : (2 : K) ≠ 0) {d : ℕ} {f : Finset (Fin Q) → K}
    (hf : f ∈ lowSpan K Q d) : weightMul K Q f ∈ lowSpan K Q (d + 1) := by
  have h : lowSpan K Q d ≤ (lowSpan K Q (d + 1)).comap (weightMul K Q) := by
    apply Submodule.span_le.2
    rintro _ ⟨S, rfl⟩
    simp only [SetLike.mem_coe, Submodule.mem_comap]
    unfold gen
    split_ifs with hS
    · exact weightMul_chi_mem h2 hS
    · rw [LinearMap.map_zero]
      exact Submodule.zero_mem _
  exact h hf

theorem pow_card_mem (h2 : (2 : K) ≠ 0) (k : ℕ) :
    (fun ε : Finset (Fin Q) => (ε.card : K) ^ k) ∈ lowSpan K Q k := by
  induction k with
  | zero =>
    have h : (fun ε : Finset (Fin Q) => (ε.card : K) ^ 0) = fun ε => chi (K := K) ∅ ε := by
      funext ε
      simp [chi]
    rw [h]
    exact chi_mem_lowSpan (by simp)
  | succ k ih =>
    have h := weightMul_mem h2 ih
    have e : weightMul K Q (fun ε : Finset (Fin Q) => (ε.card : K) ^ k)
        = fun ε : Finset (Fin Q) => (ε.card : K) ^ (k + 1) := by
      funext ε
      simp [weightMul, pow_succ, mul_comm]
    rwa [e] at h

theorem poly_card_mem (h2 : (2 : K) ≠ 0) (f : K[X]) {d : ℕ} (hf : f.natDegree ≤ d) :
    (fun ε : Finset (Fin Q) => f.eval (ε.card : K)) ∈ lowSpan K Q d := by
  have e : (fun ε : Finset (Fin Q) => f.eval (ε.card : K))
      = ∑ i ∈ range (f.natDegree + 1),
          f.coeff i • (fun ε : Finset (Fin Q) => (ε.card : K) ^ i) := by
    funext ε
    rw [eval_eq_sum_range]
    simp [Finset.sum_apply, smul_eq_mul]
  rw [e]
  refine Submodule.sum_mem _ fun i hi => Submodule.smul_mem _ _ ?_
  have hi' := Finset.mem_range.1 hi
  exact lowSpan_mono (by omega) (pow_card_mem h2 i)

/-- **Symmetric polynomials have low Fourier degree.** -/
theorem exists_gamma (h2 : (2 : K) ≠ 0) (f : K[X]) {d : ℕ} (hf : f.natDegree ≤ d) :
    ∃ γ : Finset (Fin Q) → K, (∀ S, d < S.card → γ S = 0) ∧
      ∀ ε, ∑ S, γ S * chi S ε = f.eval (ε.card : K) := by
  obtain ⟨c, hc⟩ := (Submodule.mem_span_range_iff_exists_fun K).1 (poly_card_mem (Q := Q) h2 f hf)
  refine ⟨fun S => if S.card ≤ d then c S else 0, ?_, ?_⟩
  · intro S hS
    simp [show ¬ S.card ≤ d by omega]
  · intro ε
    rw [← congrFun hc ε, Finset.sum_apply]
    refine Finset.sum_congr rfl fun S _ => ?_
    by_cases hS : S.card ≤ d
    · simp only [gen, hS, ↓reduceIte, Pi.smul_apply, smul_eq_mul]
    · simp only [gen, hS, ↓reduceIte, Pi.smul_apply, smul_eq_mul, zero_mul, Pi.zero_apply,
        mul_zero]

/-! ### The slab construction -/

section Slab

variable [CharZero K]

/-- The weights `w ≤ Q` in slab `k`: `(w + s0) / R = k`. -/
def slabSet (Q R s0 k : ℕ) : Finset ℕ := (range (Q + 1)).filter (fun w => (w + s0) / R = k)

theorem slabSet_card_le (Q R s0 k : ℕ) (hR : 0 < R) : (slabSet Q R s0 k).card ≤ R := by
  calc (slabSet Q R s0 k).card ≤ (range R).card := by
        refine Finset.card_le_card_of_injOn (fun w => (w + s0) % R) ?_ ?_
        · intro w _
          simpa using Nat.mod_lt _ hR
        · intro w hw w' hw' h
          have hw2 := (Finset.mem_filter.1 (Finset.mem_coe.1 hw)).2
          have hw2' := (Finset.mem_filter.1 (Finset.mem_coe.1 hw')).2
          have e1 := Nat.div_add_mod (w + s0) R
          have e2 := Nat.div_add_mod (w' + s0) R
          simp only at h
          rw [hw2, h] at e1
          rw [hw2'] at e2
          omega
    _ = R := Finset.card_range R

theorem cast_injOn (s : Finset ℕ) : Set.InjOn (fun w : ℕ => (w : K)) s :=
  fun _ _ _ _ h => Nat.cast_injective h

/-- The degree `< R` polynomial interpolating `(-1)^w` on slab `k`. -/
noncomputable def slabPoly (Q R s0 k : ℕ) : K[X] :=
  Lagrange.interpolate (slabSet Q R s0 k) (fun w : ℕ => (w : K)) (fun w => (-1 : K) ^ w)

theorem slabPoly_natDegree (Q R s0 k : ℕ) (hR : 0 < R) :
    (slabPoly (K := K) Q R s0 k).natDegree ≤ R - 1 := by
  refine natDegree_le_of_degree_le ((Lagrange.degree_interpolate_le _ (cast_injOn _)).trans ?_)
  exact_mod_cast Nat.sub_le_sub_right (slabSet_card_le Q R s0 k hR) 1

theorem slabPoly_eval {Q R s0 k w : ℕ} (hw : w ∈ slabSet Q R s0 k) :
    (slabPoly (K := K) Q R s0 k).eval (w : K) = (-1) ^ w :=
  Lagrange.eval_interpolate_at_node _ (cast_injOn _) hw

/-- Fourier coefficients of the slab polynomials. -/
noncomputable def slabGamma (Q R s0 : ℕ) (hR : 0 < R) (k : ℕ) : Finset (Fin Q) → K :=
  Classical.choose (exists_gamma (Q := Q) (two_ne_zero) (slabPoly (K := K) Q R s0 k)
    (slabPoly_natDegree Q R s0 k hR))

theorem slabGamma_spec (Q R s0 : ℕ) (hR : 0 < R) (k : ℕ) :
    (∀ S, R - 1 < S.card → slabGamma (K := K) Q R s0 hR k S = 0) ∧
      ∀ ε, ∑ S, slabGamma (K := K) Q R s0 hR k S * chi S ε
        = (slabPoly (K := K) Q R s0 k).eval (ε.card : K) :=
  Classical.choose_spec (exists_gamma (Q := Q) (two_ne_zero) (slabPoly (K := K) Q R s0 k)
    (slabPoly_natDegree Q R s0 k hR))

/-- The slab family: on slab `k` use `(-1)^{|ε|}` times the global formula of slab `k`. -/
noncomputable def slabFamily (x : Fin Q → K) (R s0 : ℕ) (hR : 0 < R) (ε : Finset (Fin Q)) :
    K[X] :=
  C ((-1 : K) ^ ε.card) * G x (slabGamma Q R s0 hR ((ε.card + s0) / R)) ε

theorem slab_natDegree (x : Fin Q → K) (R s0 : ℕ) (hR : 0 < R) (ε : Finset (Fin Q)) :
    (slabFamily x R s0 hR ε).natDegree ≤ R - 1 :=
  (natDegree_C_mul_le _ _).trans (natDegree_G_le x _ (slabGamma_spec Q R s0 hR _).1 ε)

theorem slab_eval_zero (x : Fin Q → K) (R s0 : ℕ) (hR : 0 < R) (ε : Finset (Fin Q)) :
    (slabFamily x R s0 hR ε).eval 0 = 1 := by
  unfold slabFamily
  rw [eval_mul, eval_C, G_eval_zero, (slabGamma_spec Q R s0 hR _).2 ε]
  have hmem : ε.card ∈ slabSet Q R s0 ((ε.card + s0) / R) := by
    simp only [slabSet, Finset.mem_filter, Finset.mem_range, and_true]
    have := Finset.card_le_univ ε
    rw [Fintype.card_fin] at this
    omega
  rw [slabPoly_eval hmem, ← pow_add, ← two_mul, pow_mul, neg_one_sq, one_pow]

/-- **Slab design.** Every edge whose endpoints lie in the same slab is good. -/
theorem slab_edge_good {x : Fin Q → K} (hx : ∀ t, x t ≠ 0) (R s0 : ℕ) (hR : 0 < R)
    {ε : Finset (Fin Q)} {t : Fin Q} (ht : t ∉ ε) (hslab : (ε.card + 1 + s0) % R ≠ 0) :
    (slabFamily x R s0 hR ε).eval (x t) + (slabFamily x R s0 hR (insert t ε)).eval (x t)
      = 0 := by
  have hcard : (insert t ε).card = ε.card + 1 := Finset.card_insert_of_notMem ht
  have hk : (ε.card + 1 + s0) / R = (ε.card + s0) / R := by
    have h := Nat.succ_div (a := ε.card + s0) (b := R)
    have hnd : ¬ R ∣ ε.card + s0 + 1 := by
      rw [Nat.dvd_iff_mod_eq_zero]
      rwa [show ε.card + s0 + 1 = ε.card + 1 + s0 by ring]
    simp only [hnd, ↓reduceIte, add_zero] at h
    rw [show ε.card + 1 + s0 = ε.card + s0 + 1 by ring, h]
  unfold slabFamily
  rw [hcard, hk]
  simp only [eval_mul, eval_C]
  rw [G_edge hx]
  ring

/-- At most one offset `s0 < R` puts a given level boundary at weight `m → m + 1`. -/
theorem card_offsets_le_one (R m : ℕ) :
    ((range R).filter (fun s0 => (m + 1 + s0) % R = 0)).card ≤ 1 := by
  refine Finset.card_le_one.2 fun a ha b hb => ?_
  simp only [Finset.mem_filter, Finset.mem_range] at ha hb
  have h : a ≡ b [MOD R] := by
    have h1 : m + 1 + a ≡ m + 1 + b [MOD R] := by
      unfold Nat.ModEq
      rw [ha.2, hb.2]
    exact Nat.ModEq.add_left_cancel' (m + 1) h1
  unfold Nat.ModEq at h
  rwa [Nat.mod_eq_of_lt ha.1, Nat.mod_eq_of_lt hb.1] at h

/-- The number of boundary edges in direction `t` for offset `s0`. -/
theorem boundary_count_eq (hQ : 1 ≤ Q) (R s0 : ℕ) (t : Fin Q) :
    ((univ : Finset (Finset (Fin Q))).filter
        (fun ε => t ∉ ε ∧ (ε.card + 1 + s0) % R = 0)).card
      = ∑ m ∈ range Q, (Q - 1).choose m * (if (m + 1 + s0) % R = 0 then 1 else 0) := by
  have hset : (univ : Finset (Finset (Fin Q))).filter
        (fun ε => t ∉ ε ∧ (ε.card + 1 + s0) % R = 0)
      = (univ.erase t).powerset.filter (fun ε => (ε.card + 1 + s0) % R = 0) := by
    ext ε
    simp only [Finset.mem_filter, Finset.mem_univ, true_and, Finset.mem_powerset]
    constructor
    · rintro ⟨ht, h⟩
      refine ⟨fun a ha => Finset.mem_erase.2 ⟨fun hat => ht (hat ▸ ha), Finset.mem_univ a⟩, h⟩
    · rintro ⟨hsub, h⟩
      exact ⟨fun ht => (Finset.mem_erase.1 (hsub ht)).1 rfl, h⟩
  have herase : (univ.erase t).card = Q - 1 := by
    rw [Finset.card_erase_of_mem (Finset.mem_univ t), Finset.card_univ, Fintype.card_fin]
  have hpow := Finset.sum_powerset_apply_card
    (fun m => if (m + 1 + s0) % R = 0 then (1 : ℕ) else 0) (x := univ.erase t)
  rw [hset, Finset.card_filter, hpow, herase, show Q - 1 + 1 = Q by omega]
  simp [smul_eq_mul]

/-- **Slab bound.** For some offset `s0 < R` the slab family has, in every direction, at most
`2^(Q-1) / R` bad edges (out of `2^(Q-1)`), for every number of directions `Q`. -/
theorem slab_design_bound [DecidableEq K] {x : Fin Q → K} (hx : ∀ t, x t ≠ 0) (hQ : 1 ≤ Q)
    (R : ℕ) (hR : 0 < R) :
    ∃ s0 < R, (∀ ε, (slabFamily x R s0 hR ε).natDegree ≤ R - 1) ∧
      (∀ ε, (slabFamily x R s0 hR ε).eval 0 = 1) ∧
      ∀ t : Fin Q, R * ((univ : Finset (Finset (Fin Q))).filter (fun ε => t ∉ ε ∧
          (slabFamily x R s0 hR ε).eval (x t)
            + (slabFamily x R s0 hR (insert t ε)).eval (x t) ≠ 0)).card ≤ 2 ^ (Q - 1) := by
  set B : ℕ → ℕ := fun s0 =>
    ∑ m ∈ range Q, (Q - 1).choose m * (if (m + 1 + s0) % R = 0 then 1 else 0) with hB
  have hsum : ∑ s0 ∈ range R, B s0 ≤ 2 ^ (Q - 1) := by
    rw [hB, Finset.sum_comm]
    calc ∑ m ∈ range Q, ∑ s0 ∈ range R,
            (Q - 1).choose m * (if (m + 1 + s0) % R = 0 then 1 else 0)
        ≤ ∑ m ∈ range Q, (Q - 1).choose m := by
          refine Finset.sum_le_sum fun m _ => ?_
          rw [← Finset.mul_sum, Finset.sum_boole]
          simpa using Nat.mul_le_mul_left ((Q - 1).choose m) (card_offsets_le_one R m)
      _ = 2 ^ (Q - 1) := by
          have h := Nat.sum_range_choose (Q - 1)
          rwa [show Q - 1 + 1 = Q by omega] at h
  obtain ⟨s0, hs0, hle⟩ := Finset.exists_le_of_sum_le (s := range R)
    (f := fun s0 => R * B s0) (g := fun _ => 2 ^ (Q - 1)) (Finset.nonempty_range_iff.2 hR.ne')
    (by rw [← Finset.mul_sum, Finset.sum_const, Finset.card_range, smul_eq_mul]
        exact Nat.mul_le_mul_left R hsum)
  refine ⟨s0, Finset.mem_range.1 hs0, slab_natDegree x R s0 hR, slab_eval_zero x R s0 hR, ?_⟩
  intro t
  calc R * ((univ : Finset (Finset (Fin Q))).filter (fun ε => t ∉ ε ∧
          (slabFamily x R s0 hR ε).eval (x t)
            + (slabFamily x R s0 hR (insert t ε)).eval (x t) ≠ 0)).card
      ≤ R * ((univ : Finset (Finset (Fin Q))).filter
          (fun ε => t ∉ ε ∧ (ε.card + 1 + s0) % R = 0)).card := by
        refine Nat.mul_le_mul_left R (Finset.card_le_card fun ε hε => ?_)
        simp only [Finset.mem_filter, Finset.mem_univ, true_and] at hε ⊢
        refine ⟨hε.1, ?_⟩
        by_contra hne
        exact hε.2 (slab_edge_good hx R s0 hR hε.1 hne)
    _ = R * B s0 := by rw [boundary_count_eq hQ R s0 t]
    _ ≤ 2 ^ (Q - 1) := hle

end Slab

end EthConsequences.SlabDesign
