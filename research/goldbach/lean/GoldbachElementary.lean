import Std

/-!
# Goldbach elementary certificates

These declarations formalize elementary combinatorial and modular observations,
not the binary Goldbach conjecture and not the asymptotic claims in the article.
`PrimeLike` uses the elementary divisor characterization and is deliberately
independent of mathlib. In the target environment we check this file using the
Lean 4.19.0 kernel; the self-executable-path shim only repairs a container
/proc permission issue, and does not change the Lean proof terms.
-/

namespace GoldbachElementary

def PrimeLike (n : Nat) : Prop :=
   2 ≤ n ∧ ∀ d : Nat, d ∣ n → d = 1 ∨ d = n

/-- If a natural number is prime in the divisor sense and divisible by 3,
    it must equal 3. -/
theorem prime_divisible_by_three (n : Nat) (hprime : PrimeLike n)
    (hdiv : 3 ∣ n) : n = 3 := by
  have h := hprime.2 3 hdiv
  omega

/-- All numbers 30k+5 for k≥1 have the proper divisor 5. -/
theorem progression_composite (k : Nat) (hk : 1 ≤ k) :
    ¬ PrimeLike (30 * k + 5) := by
  intro hp
  have hd : 5 ∣ 30 * k + 5 := by
    refine ⟨6 * k + 1, ?_⟩
    omega
  have h := hp.2 5 hd
  omega

/-- A common prime summand for N and N+2. The same p appears in both
    decompositions, and q is its complementary summand for the first. -/
def SharedSummand (N p q : Nat) : Prop :=
  p + q = N ∧ PrimeLike p ∧ PrimeLike q ∧ PrimeLike (q + 2)

/-- For every k≥1, the even targets 30k+8 and 30k+10 have no common prime
    summand. This establishes an obstruction to adjacent-target induction,
    and makes no assertion about the existence of representations separately. -/
theorem no_adjacent_common_summand (k : Nat) (hk : 1 ≤ k) (p q : Nat) :
    ¬ SharedSummand (30 * k + 8) p q := by
  intro hs
  rcases hs with ⟨heq, hp, hq, hq2⟩
  have hcover : 3 ∣ p ∨ 3 ∣ q ∨ 3 ∣ q + 2 := by omega
  rcases hcover with hp3 | hq3 | hq23
  · have hpeq := prime_divisible_by_three p hp hp3
    have hqeq : q = 30 * k + 5 := by omega
    exact progression_composite k hk (hqeq ▸ hq)
  · have hqeq := prime_divisible_by_three q hq hq3
    have hpeq : p = 30 * k + 5 := by omega
    exact progression_composite k hk (hpeq ▸ hp)
  · have hq2eq := prime_divisible_by_three (q + 2) hq2 hq23
    have hqlo := hq.1
    omega

/-- Reflection preserves a decomposition of N into two natural summands. -/
theorem reflection_involution (N p q : Nat) (h : p + q = N) :
    q + p = N := by omega

/-- Symmetry of the two-summand prime predicate, abstracted from counting. -/
theorem prime_pair_symmetry (N p q : Nat)
    (h : p + q = N ∧ PrimeLike p ∧ PrimeLike q) :
    q + p = N ∧ PrimeLike q ∧ PrimeLike p := by
  rcases h with ⟨hs, hp, hq⟩
  exact ⟨reflection_involution N p q hs, hq, hp⟩

/-- The exact inclusion-exclusion identity used by the rough-pair four-cell
    table. The entries are integers to make subtraction unambiguous. -/
theorem four_cell_identity (pp ps sp ss : Int) :
    (pp + ps) + (pp + sp) - (pp + ps + sp + ss) = pp - ss := by
  omega

/-- If `prime` and `semiprime` are the numbers of complements of each type,
    then the Liouville signed count is semiprime minus prime. -/
theorem chen_parity_identity (prime semiprime : Int) :
    ((prime + semiprime) - (semiprime - prime)) / 2 = prime := by
  omega

/-- Finite trial division, with all divisors from zero through n included. -/
def trialPrime (n : Nat) : Bool :=
  decide (2 ≤ n) && (List.range (n + 1)).all (fun d =>
    (n % d != 0) || (d == 1) || (d == n))

/-- Soundness of the executable test relative to the divisor definition. -/
theorem trialPrime_sound (n : Nat) (h : trialPrime n = true) : PrimeLike n := by
  simp only [trialPrime, Bool.and_eq_true, decide_eq_true_eq, List.all_eq_true] at h
  constructor
  · exact h.1
  · intro d hd
    have hdle : d ≤ n := Nat.le_of_dvd (by omega) hd
    have hm : d ∈ List.range (n + 1) := by simp; omega
    have hx := h.2 d hm
    simp only [Bool.or_eq_true, bne_iff_ne, beq_iff_eq] at hx
    have hmod : n % d = 0 := Nat.mod_eq_zero_of_dvd hd
    omega

/-- Completeness of the executable trial division test. -/
theorem trialPrime_complete (n : Nat) (h : PrimeLike n) : trialPrime n = true := by
  simp only [trialPrime, Bool.and_eq_true, decide_eq_true_eq, List.all_eq_true]
  constructor
  · exact h.1
  · intro d hd
    simp only [Bool.or_eq_true, bne_iff_ne, beq_iff_eq]
    by_cases hdiv : d ∣ n
    · rcases h.2 d hdiv with heq | heq
      · exact Or.inl (Or.inr heq)
      · exact Or.inr heq
    · have hnmod : n % d ≠ 0 := by
        intro hz
        exact hdiv (Nat.dvd_of_mod_eq_zero hz)
      exact Or.inl (Or.inl hnmod)

/-- Finite Goldbach summands for 30 found by executable trial division. -/
def sums30 : List Nat :=
  (List.range 31).filter (fun p => trialPrime p && trialPrime (30 - p))

theorem sums30_exact : sums30 = [7, 11, 13, 17, 19, 23] := by decide

/-- The list is exactly the natural summands p in [0,30] for which both
    p and 30−p satisfy the divisor definition of prime. -/
theorem sums30_characterization (p : Nat) :
    p ∈ sums30 ↔ p ≤ 30 ∧ PrimeLike p ∧ PrimeLike (30 - p) := by
  simp only [sums30, List.mem_filter, List.mem_range, Bool.and_eq_true]
  constructor
  · intro h
    exact ⟨by omega, trialPrime_sound p h.2.1, trialPrime_sound (30 - p) h.2.2⟩
  · intro h
    exact ⟨by omega, trialPrime_complete p h.2.1,
      trialPrime_complete (30 - p) h.2.2⟩

theorem prime7 : PrimeLike 7 := trialPrime_sound 7 (by decide)
theorem prime23 : PrimeLike 23 := trialPrime_sound 23 (by decide)

#print axioms sums30_exact
#print axioms sums30_characterization
#print axioms trialPrime_sound
#print axioms trialPrime_complete
#print axioms four_cell_identity
#print axioms chen_parity_identity
#print axioms no_adjacent_common_summand
#print axioms prime_pair_symmetry
end GoldbachElementary
