/-
Problem ETH-A01 (problems/eth/A-algebraic-core/ETH-A01-parity-interpolant.md).

The shifted Newton-basis parity interpolant used in OpenAI's refutation of ETH
(openai/math, preprint "The Exponential Time Hypothesis is False", Oct 25 2026,
Sec. 2.6 Step 2 and Sec. 4) is
  f_{a,b}(z) = (-1)^a * Σ_{j ≤ b} (-2)^j * C(z - a, j).
Writing z = a + k with k : ℕ, its value is (-1)^a * S b k where S is defined below.

Results (all proved, no `sorry`):
* `neg_one_pow_mul_S_of_le`   : interval identity (-1)^k S b k = 1 for k ≤ b.
* `S_succ_right`              : one-step recurrence in k (Pascal).
* `defect_telescope`          : exact closed form of the off-interval defect as an
                                alternating binomial sum.
* `pdf_defect_claim_false`    : the single-binomial defect formula stated in the
                                Gemini problem sheet is false.
* `no_low_degree_parity_match`: no polynomial of degree < R matches ε(-1)^i on R+1
                                consecutive points, so the interval length R used by
                                the paper is the maximum possible for degree R-1.
-/
import Mathlib.Algebra.Group.ForwardDiff
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.LinearCombination

open Finset

namespace EthProblems.Parity

/-- Truncated alternating binomial sum `S b k = Σ_{j ≤ b} (-2)^j C(k,j)`. -/
def S (b k : ℕ) : ℤ := ∑ j ∈ range (b + 1), (-2 : ℤ) ^ j * (k.choose j : ℤ)

/-- Interval identity: the interpolant equals the parity `(-1)^k` on `0 ≤ k ≤ b`. -/
theorem neg_one_pow_mul_S_of_le {b k : ℕ} (hk : k ≤ b) : (-1 : ℤ) ^ k * S b k = 1 := by
  have htrunc : S b k = ∑ j ∈ range (k + 1), (-2 : ℤ) ^ j * (k.choose j : ℤ) := by
    unfold S
    symm
    apply Finset.sum_subset
    · intro j hj
      simp only [mem_range] at *
      omega
    · intro j _ hj
      simp only [mem_range, not_lt] at hj
      rw [Nat.choose_eq_zero_of_lt (by omega)]
      simp
  have hbin : ((-2 : ℤ) + 1) ^ k = ∑ j ∈ range (k + 1), (-2 : ℤ) ^ j * (k.choose j : ℤ) := by
    rw [add_pow]
    apply sum_congr rfl
    intro j _
    ring
  rw [htrunc, ← hbin, ← mul_pow]
  norm_num

/-- One-step recurrence: `S b (k+1) = -S b k - (-2)^(b+1) C(k,b)`. -/
theorem S_succ_right (b k : ℕ) :
    S b (k + 1) = -S b k - (-2 : ℤ) ^ (b + 1) * (k.choose b : ℤ) := by
  induction b with
  | zero => norm_num [S]
  | succ b ih =>
    have h1 : S (b + 1) (k + 1) = S b (k + 1) + (-2 : ℤ) ^ (b + 1) * ((k + 1).choose (b + 1) : ℤ) := by
      unfold S
      rw [sum_range_succ]
    have h2 : S (b + 1) k = S b k + (-2 : ℤ) ^ (b + 1) * (k.choose (b + 1) : ℤ) := by
      unfold S
      rw [sum_range_succ]
    rw [h1, h2, ih, Nat.choose_succ_succ', Nat.cast_add]
    ring

/-- Exact off-interval defect of the parity interpolant:
`(-1)^k S b k - 1 = -(-2)^(b+1) Σ_{m < k} (-1)^(m+1) C(m,b)`.
The summands vanish for `m < b`, so the defect is zero on the interval. -/
theorem defect_telescope (b k : ℕ) :
    (-1 : ℤ) ^ k * S b k - 1 =
      -(-2 : ℤ) ^ (b + 1) * ∑ m ∈ range k, (-1 : ℤ) ^ (m + 1) * (m.choose b : ℤ) := by
  induction k with
  | zero =>
    have h := neg_one_pow_mul_S_of_le (b := b) (k := 0) (Nat.zero_le _)
    simp only [range_zero, sum_empty, mul_zero]
    linarith
  | succ k ih =>
    rw [sum_range_succ, S_succ_right, mul_add, ← ih]
    ring

/-- The first value outside the interval: `(-1)^(b+1) S b (b+1) - 1 = -2^(b+1)`. -/
theorem first_defect (b : ℕ) : (-1 : ℤ) ^ (b + 1) * S b (b + 1) - 1 = -(2 : ℤ) ^ (b + 1) := by
  rw [S_succ_right, Nat.choose_self]
  have h := neg_one_pow_mul_S_of_le (b := b) (k := b) le_rfl
  have e : ((-2 : ℤ)) ^ (b + 1) = (-1) ^ (b + 1) * 2 ^ (b + 1) := by rw [← mul_pow]; norm_num
  rw [e]
  have e2 : ((-1 : ℤ)) ^ (b + 1) * (-1) ^ (b + 1) = 1 := by rw [← mul_pow]; norm_num
  linear_combination h - (2 : ℤ) ^ (b + 1) * e2

/-- The single-binomial defect formula from the problem sheet,
`S b k - (-1)^k = (-2)^(b+1) C(k-1, b)`, is false (take `b = 0`, `k = 2`). -/
theorem pdf_defect_claim_false :
    ¬ ∀ b k : ℕ, b < k → S b k - (-1 : ℤ) ^ k = (-2 : ℤ) ^ (b + 1) * ((k - 1).choose b : ℤ) := by
  intro h
  have := h 0 2 (by norm_num)
  norm_num [S] at this

/-- Optimality of the interval length: a polynomial of degree `< R` cannot agree with
`ε (-1)^i` (`ε ≠ 0`) at the `R+1` consecutive points `x₀, x₀+1, …, x₀+R`.
Hence degree `R-1` interpolates parity on at most `R` consecutive integers, which is
exactly what the paper's construction uses. -/
theorem no_low_degree_parity_match {K : Type*} [Field K] [CharZero K]
    (P : Polynomial K) (R : ℕ) (hP : P.natDegree < R) (x₀ ε : K) (hε : ε ≠ 0) :
    ¬ ∀ i ∈ range (R + 1), P.eval (x₀ + i) = ε * (-1) ^ i := by
  intro h
  have h0 := congr_fun (Polynomial.fwdDiff_iter_eq_zero_of_degree_lt (P := P) hP) x₀
  rw [fwdDiff_iter_eq_sum_shift, Pi.zero_apply] at h0
  have key : ∀ k ∈ range (R + 1),
      ((-1 : ℤ) ^ (R - k) * (R.choose k : ℤ)) • P.eval (x₀ + k • (1 : K)) =
        ε * (-1) ^ R * (R.choose k : K) := by
    intro k hk
    have hkR : k ≤ R := Nat.lt_succ_iff.mp (mem_range.mp hk)
    rw [nsmul_one, h k hk, zsmul_eq_mul]
    push_cast
    have e : ((-1 : K)) ^ (R - k) * (-1) ^ k = (-1) ^ R := by
      rw [← pow_add, Nat.sub_add_cancel hkR]
    linear_combination (ε * (R.choose k : K)) * e
  rw [sum_congr rfl key, ← mul_sum] at h0
  have hs : ∑ k ∈ range (R + 1), (R.choose k : K) = 2 ^ R := by
    exact_mod_cast Nat.sum_range_choose R
  rw [hs] at h0
  have hne : ε * (-1 : K) ^ R * 2 ^ R ≠ 0 :=
    mul_ne_zero (mul_ne_zero hε (pow_ne_zero _ (neg_ne_zero.mpr one_ne_zero)))
      (pow_ne_zero _ (by norm_num : (2 : K) ≠ 0))
  exact hne h0

end EthProblems.Parity
