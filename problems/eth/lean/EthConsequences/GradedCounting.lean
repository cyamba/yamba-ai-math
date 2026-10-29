import Mathlib.Algebra.Polynomial.BigOperators
import Mathlib.Algebra.Polynomial.Coeff
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Data.Fintype.Pi

/-!
# Graded counting: histograms and weight enumerators (subresult SR-07)

Tensor contraction over the truncated ring `(ℤ/2^p)[V]/(V^ℓ)` (preprint, Theorem D.1) computes
sums of products of local factors whose values are polynomials in `V`. This file proves the
algebraic identities that turn such sums into the two graded counts used in SR-07:

* `sum_pow_eq`: for any grading `wt` bounded by `N` and any finite set `S`,
  `∑_{x ∈ S} V^{wt x} = ∑_{w ≤ N} #{x ∈ S | wt x = w} V^w`, so the coefficients of the
  contraction are the exact counts in each grade;
* `prod_ite_eq_pow`: a product of local factors `if sat then 1 else V` equals `V^{#violated}`;
* `histogram_identity`: hence `∑_x ∏_e (if sat_e x then 1 else V) = ∑_j h_j V^j`, where `h_j` is
  the number of assignments violating exactly `j` constraints (Max-SAT histogram);
* `deformation_identity`: evaluating at `V = 1 - t` gives the identity
  `∑_x ∏_e (1 + t (φ_e(x) - 1)) = ∑_j h_j (1 - t)^j` used in the Gemini blueprint (problem
  YMB-ETH-07), with `φ_e ∈ {0,1}` the clause indicator;
* `weight_identity`: `∑_{x ∈ SAT} ∏_i (if x i then V else 1) = ∑_w c_w V^w`, the weight
  enumerator (problem YMB-ETH-03).
-/

namespace EthConsequences.Graded

open Finset Polynomial

variable {α : Type*} [Fintype α]
variable {R : Type*} [CommRing R]

omit [Fintype α] in
/-- Grading identity: a sum of monomials `V^{wt x}` collects the counts of each grade. -/
theorem sum_pow_eq (S : Finset α) (wt : α → ℕ) (N : ℕ) (hN : ∀ x ∈ S, wt x ≤ N) :
    ∑ x ∈ S, (X : R[X]) ^ wt x
      = ∑ w ∈ range (N + 1), C ((S.filter (fun x => wt x = w)).card : R) * X ^ w := by
  rw [← Finset.sum_fiberwise_of_maps_to (g := wt) (t := range (N + 1))
    (fun x hx => Finset.mem_range.2 (Nat.lt_succ_of_le (hN x hx)))]
  refine Finset.sum_congr rfl fun w _ => ?_
  rw [Finset.sum_congr rfl (fun x hx => by rw [(Finset.mem_filter.1 hx).2]), Finset.sum_const,
    nsmul_eq_mul, ← C_eq_natCast]

variable {ι : Type*} [Fintype ι]

/-- Number of violated constraints. -/
def viol (sat : ι → α → Prop) [∀ e x, Decidable (sat e x)] (x : α) : ℕ :=
  (univ.filter (fun e => ¬ sat e x)).card

/-- Number of assignments violating exactly `j` constraints. -/
def hist (sat : ι → α → Prop) [∀ e x, Decidable (sat e x)] (j : ℕ) : ℕ :=
  (univ.filter (fun x => viol sat x = j)).card

omit [Fintype α] in
/-- Local graded factors multiply to `V^{#violated}`. -/
theorem prod_ite_eq_pow (sat : ι → α → Prop) [∀ e x, Decidable (sat e x)] (x : α) :
    ∏ e, (if sat e x then (1 : R[X]) else X) = X ^ viol sat x := by
  rw [Finset.prod_ite, Finset.prod_const_one, one_mul, Finset.prod_const]
  rfl

/-- **Histogram identity.** -/
theorem histogram_identity (sat : ι → α → Prop) [∀ e x, Decidable (sat e x)] :
    ∑ x, ∏ e, (if sat e x then (1 : R[X]) else X)
      = ∑ j ∈ range (Fintype.card ι + 1), C (hist sat j : R) * X ^ j := by
  simp_rw [prod_ite_eq_pow]
  refine sum_pow_eq univ (viol sat) (Fintype.card ι) fun x _ => ?_
  exact (Finset.card_le_univ _)

/-- The coefficients of the graded contraction are the histogram. -/
theorem coeff_histogram (sat : ι → α → Prop) [∀ e x, Decidable (sat e x)] {j : ℕ}
    (hj : j ≤ Fintype.card ι) :
    (∑ x, ∏ e, (if sat e x then (1 : R[X]) else X)).coeff j = hist sat j := by
  rw [histogram_identity, finsetSum_coeff]
  simp_rw [coeff_C_mul, coeff_X_pow]
  rw [Finset.sum_eq_single j]
  · simp
  · intro b _ hb
    simp [hb.symm]
  · intro h
    exact absurd (Finset.mem_range.2 (Nat.lt_succ_of_le hj)) h

/-- **Deformation identity** (clause indicators `φ_e ∈ {0,1}`). -/
theorem deformation_identity (sat : ι → α → Prop) [∀ e x, Decidable (sat e x)] (t : R) :
    ∑ x, ∏ e, (1 + t * ((if sat e x then 1 else 0) - 1))
      = ∑ j ∈ range (Fintype.card ι + 1), (hist sat j : R) * (1 - t) ^ j := by
  have h := congrArg (eval (1 - t)) (histogram_identity (R := R) sat)
  simp only [eval_finsetSum, eval_prod, eval_mul, eval_C, eval_pow, eval_X] at h
  rw [← h]
  refine Finset.sum_congr rfl fun x _ => Finset.prod_congr rfl fun e _ => ?_
  split_ifs
  · simp
  · simp only [eval_X]
    ring

/-- **Weight enumerator identity.** For a set `SAT` of Boolean assignments, the local factors
`if x i then V else 1` produce `∑_w c_w V^w`, `c_w` the number of members of Hamming weight `w`. -/
theorem weight_identity {n : ℕ} (SAT : Finset (Fin n → Bool)) :
    ∑ x ∈ SAT, ∏ i, (if x i = true then (X : R[X]) else 1)
      = ∑ w ∈ range (n + 1),
          C ((SAT.filter (fun x => (univ.filter (fun i => x i = true)).card = w)).card : R)
            * X ^ w := by
  have hprod : ∀ x : Fin n → Bool,
      ∏ i, (if x i = true then (X : R[X]) else 1) = X ^ (univ.filter (fun i => x i = true)).card := by
    intro x
    rw [Finset.prod_ite, Finset.prod_const_one, mul_one, Finset.prod_const]
  simp_rw [hprod]
  refine sum_pow_eq SAT _ n fun x _ => ?_
  calc (univ.filter (fun i => x i = true)).card ≤ (univ : Finset (Fin n)).card :=
        Finset.card_le_univ _
    _ = n := by rw [Finset.card_univ, Fintype.card_fin]

end EthConsequences.Graded
