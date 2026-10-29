import Mathlib.Data.Nat.Choose.Sum
import Mathlib.Algebra.BigOperators.Intervals
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith
import Mathlib.Algebra.Order.Ring.Abs

/-!
# Newton-basis parity interpolation

In the matrix construction of openai/math result 378 ("The Exponential Time Hypothesis is
False", Section 2.7, Step 2), a polynomial `f` of degree `b` interpolates `(-1)^j` on an
interval `{a, ..., a+b}` of Hamming weights. In the Newton basis centred at `a`,

  `f(a + k) = (-1)^a * S k b`,  where  `S k b = ∑_{j=0}^{b} (-2)^j * C(k, j)`.

We prove:

* `S_of_le`: exactness on the window, `S k b = (-1)^k` for `k ≤ b`;
* `S_succ`: the first-order recurrence `S (k+1) b = -S k b + 2 (-2)^b C(k,b)`;
* `defect_eq`: the closed telescoped defect
  `(-1)^k S k b - 1 = (-1)^(b+1) 2^(b+1) ∑_{m<k} (-1)^m C(m,b)`;
* `abs_defect_le`: the explicit off-window bound `|(-1)^k S k b - 1| ≤ 2^(b+1) C(k-1,b)`.

The recurrence corrects the one stated in the Gemini summary ("YAMBA-378-01"), which is false
already for `b = 1`.
-/

namespace EthConsequences.ParityInterpolation

open Finset

/-- Truncated binomial sum `S(k,b) = ∑_{j=0}^{b} (-2)^j C(k,j)`. -/
def S (k b : ℕ) : ℤ := ∑ j ∈ range (b + 1), (-2 : ℤ) ^ j * (k.choose j : ℤ)

/-- Exactness on the interpolation window: for `k ≤ b`, `S(k,b) = (-1)^k`. -/
theorem S_of_le {k b : ℕ} (hk : k ≤ b) : S k b = (-1) ^ k := by
  unfold S
  have htrunc : ∑ j ∈ range (b + 1), (-2 : ℤ) ^ j * (k.choose j : ℤ)
      = ∑ j ∈ range (k + 1), (-2 : ℤ) ^ j * (k.choose j : ℤ) := by
    symm
    apply Finset.sum_subset (Finset.range_mono (by omega))
    intro j hj hjk
    simp only [Finset.mem_range, not_lt] at hj hjk
    rw [Nat.choose_eq_zero_of_lt (by omega)]
    simp
  rw [htrunc]
  have h := add_pow (-2 : ℤ) 1 k
  rw [show (-2 : ℤ) + 1 = -1 by norm_num] at h
  rw [h]
  refine Finset.sum_congr rfl fun j _ => ?_
  simp

/-- Pascal step for the truncated sums. -/
theorem S_succ (k b : ℕ) :
    S (k + 1) b = -S k b + 2 * (-2 : ℤ) ^ b * (k.choose b : ℤ) := by
  induction b with
  | zero => simp [S]
  | succ b ih =>
    have e1 : S (k + 1) (b + 1)
        = S (k + 1) b + (-2 : ℤ) ^ (b + 1) * ((k + 1).choose (b + 1) : ℤ) := by
      unfold S; rw [Finset.sum_range_succ]
    have e2 : S k (b + 1) = S k b + (-2 : ℤ) ^ (b + 1) * (k.choose (b + 1) : ℤ) := by
      unfold S; rw [Finset.sum_range_succ]
    rw [e1, e2, ih, Nat.choose_succ_succ]
    push_cast
    ring

/-- Closed form of the off-window defect, obtained by telescoping `S_succ`. -/
theorem defect_eq (k b : ℕ) :
    (-1 : ℤ) ^ k * S k b - 1
      = (-1) ^ (b + 1) * 2 ^ (b + 1) * ∑ m ∈ range k, (-1 : ℤ) ^ m * (m.choose b : ℤ) := by
  induction k with
  | zero =>
    simp [S, Finset.sum_range_succ']
  | succ k ih =>
    rw [S_succ, Finset.sum_range_succ]
    have h2 : (-1 : ℤ) ^ (k + 1) = -((-1 : ℤ) ^ k) := by ring
    rw [h2]
    have : (-((-1 : ℤ) ^ k)) * (-S k b + 2 * (-2) ^ b * (k.choose b : ℤ)) - 1
        = ((-1 : ℤ) ^ k * S k b - 1) - (-1) ^ k * 2 * (-2) ^ b * (k.choose b : ℤ) := by ring
    rw [this, ih]
    have h3 : (-2 : ℤ) ^ b = (-1) ^ b * 2 ^ b := by
      rw [show (-2 : ℤ) = (-1) * 2 by norm_num, mul_pow]
    rw [h3]
    ring

/-- Alternating sums of a monotone nonnegative sequence: `0 ≤ (-1)^k A(k+1) ≤ f k`, where
`A(k+1) = ∑_{m ≤ k} (-1)^m f m`. -/
theorem alternating_sum_bounds (f : ℕ → ℤ) (hf0 : ∀ m, 0 ≤ f m) (hmono : Monotone f) (k : ℕ) :
    0 ≤ (-1 : ℤ) ^ k * ∑ m ∈ range (k + 1), (-1 : ℤ) ^ m * f m ∧
      (-1 : ℤ) ^ k * ∑ m ∈ range (k + 1), (-1 : ℤ) ^ m * f m ≤ f k := by
  induction k with
  | zero => simpa using hf0 0
  | succ k ih =>
    obtain ⟨h1, h2⟩ := ih
    have hk : f k ≤ f (k + 1) := hmono (Nat.le_succ k)
    rw [Finset.sum_range_succ]
    have e : (-1 : ℤ) ^ (k + 1) *
        (∑ m ∈ range (k + 1), (-1 : ℤ) ^ m * f m + (-1) ^ (k + 1) * f (k + 1))
        = f (k + 1) - (-1 : ℤ) ^ k * ∑ m ∈ range (k + 1), (-1 : ℤ) ^ m * f m := by
      have hsq : ((-1 : ℤ) ^ (k + 1)) * (-1) ^ (k + 1) = 1 := by
        rw [← mul_pow]; norm_num
      have : (-1 : ℤ) ^ (k + 1) = -((-1 : ℤ) ^ k) := by ring
      calc (-1 : ℤ) ^ (k + 1) *
            (∑ m ∈ range (k + 1), (-1 : ℤ) ^ m * f m + (-1) ^ (k + 1) * f (k + 1))
          = (-1 : ℤ) ^ (k + 1) * ∑ m ∈ range (k + 1), (-1 : ℤ) ^ m * f m
              + ((-1 : ℤ) ^ (k + 1) * (-1) ^ (k + 1)) * f (k + 1) := by ring
        _ = _ := by rw [hsq, this]; ring
    rw [e]
    constructor <;> linarith

/-- Explicit off-window bound: `|(-1)^k S(k,b) - 1| ≤ 2^(b+1) C(k-1,b)` for `k ≥ 1`. -/
theorem abs_defect_le (k b : ℕ) (hk : 1 ≤ k) :
    |(-1 : ℤ) ^ k * S k b - 1| ≤ 2 ^ (b + 1) * ((k - 1).choose b : ℤ) := by
  rw [defect_eq]
  obtain ⟨j, rfl⟩ : ∃ j, k = j + 1 := ⟨k - 1, by omega⟩
  simp only [Nat.add_sub_cancel]
  have hb := alternating_sum_bounds (fun m => ((m.choose b : ℕ) : ℤ))
    (fun m => by positivity)
    (fun x y hxy => by dsimp only; exact_mod_cast Nat.choose_le_choose b hxy) j
  set A := ∑ m ∈ range (j + 1), (-1 : ℤ) ^ m * ((m.choose b : ℕ) : ℤ) with hA
  have habsA : |A| ≤ (j.choose b : ℤ) := by
    have hu : |(-1 : ℤ) ^ j| = 1 := abs_neg_one_pow j
    have : |A| = |(-1 : ℤ) ^ j * A| := by rw [abs_mul, hu, one_mul]
    rw [this, abs_of_nonneg hb.1]
    exact hb.2
  rw [abs_mul, abs_mul]
  have h1 : |(-1 : ℤ) ^ (b + 1)| = 1 := abs_neg_one_pow (b + 1)
  have h2 : |(2 : ℤ) ^ (b + 1)| = 2 ^ (b + 1) := abs_of_nonneg (by positivity)
  rw [h1, h2, one_mul]
  exact mul_le_mul_of_nonneg_left habsA (by positivity)

/-- Sanity check on a concrete instance (`b = 2`, window `{0,1,2}` and defect at `k = 3`). -/
example : S 0 2 = 1 ∧ S 1 2 = -1 ∧ S 2 2 = 1 ∧ S 3 2 = 7 := by
  refine ⟨?_, ?_, ?_, ?_⟩ <;> decide

end EthConsequences.ParityInterpolation
