import PartitionH3.ElementaryProduct
import PartitionH3.SignedCancellation
import PartitionH3.Coloring

/-!
The original complete survivor families satisfy a polynomial identity, not
only a degreewise counting identity. Finite summation then matches their
elementary expansion with the tableau alternant expansion. This algebraic
join does not assume or assert a coloring-to-tableau equality.
-/

open scoped BigOperators

noncomputable section

namespace PartitionH3

theorem coeff_add_basic (p q : Coeff) (d : ℕ) :
    (p + q).coeff d = p.coeff d + q.coeff d := by
  rcases p with ⟨p⟩
  rcases q with ⟨q⟩
  simp_rw [← Polynomial.ofFinsupp_add, Polynomial.coeff]
  exact Finsupp.add_apply _ _ _

theorem coeff_X_pow_basic (k d : ℕ) :
    ((Polynomial.X : Coeff) ^ k).coeff d = if k = d then 1 else 0 := by
  rw [Polynomial.X_pow_eq_monomial, Polynomial.coeff_monomial]

theorem list_weight_coefficient {α : Type} (w : α → ℕ) (xs : List α) (d : ℕ) :
    ((xs.map (fun x => (Polynomial.X : Coeff) ^ w x)).sum).coeff d =
      (CornerSlide.degreeCount w d xs : ℤ) := by
  induction xs with
  | nil => simp [CornerSlide.degreeCount]
  | cons x xs ih =>
    simp only [List.map_cons, List.sum_cons, coeff_add_basic, ih, coeff_X_pow_basic]
    by_cases hd : w x = d
    · simp [CornerSlide.degreeCount, hd, Nat.cast_add, add_comm]
    · simp [CornerSlide.degreeCount, hd]

theorem tableauWeight_coefficient {n : ℕ} (H : NaturalUnitInterval n)
    (family : List CornerSlide.Rows) (d : ℕ) :
    (tableauWeight H family).coeff d =
      (CornerSlide.degreeCount (CornerSlide.tableauGraphInversions (natLt H)) d family : ℤ) :=
  list_weight_coefficient _ family d

theorem natLt_asymm {n : ℕ} (H : NaturalUnitInterval n) :
    ∀ i j, natLt H i j → ¬ natLt H j i := by
  intro i j hij hji
  by_cases hi : i < n
  · by_cases hj : j < n
    · have hp : PosetLt H ⟨i, hi⟩ ⟨j, hj⟩ := by simpa [natLt, hi, hj] using hij
      have hq : PosetLt H ⟨j, hj⟩ ⟨i, hi⟩ := by simpa [natLt, hi, hj] using hji
      exact lt_asymm (posetLt_implies_lt H hp) (posetLt_implies_lt H hq)
    · simp [natLt, hi, hj] at hij
  · simp [natLt, hi] at hij

/-- H2 lifted to the actual polynomial weights of the unchanged complete
families. This includes maximal indices and empty next families. -/
theorem tableauCoefficient_eq_next_add_survivor {n : ℕ} (H : NaturalUnitInterval n)
    (hh : HeightTwo H) (k : ℕ) :
    tableauCoefficient H k = tableauCoefficient H (k + 1) + survivorCoefficient H k := by
  apply Polynomial.ext
  intro d
  simp only [tableauCoefficient, survivorCoefficient, coeff_add_basic,
    tableauWeight_coefficient]
  exact_mod_cast CornerSlide.height_two_degreewise_cancellation (natLt H)
    (natLt_asymm H) (heightTwo_natLt_noThreeChain H hh) (List.range n) k d

theorem tableauCoefficient_out_of_range {n : ℕ} (H : NaturalUnitInterval n)
    (k : ℕ) (hk : n < 2 * k) : tableauCoefficient H k = 0 := by
  unfold tableauCoefficient
  rw [CornerSlide.columnFamily_out_of_range (natLt H) (List.range n) k (by simpa using hk)]
  simp [tableauWeight]

theorem tableauCoefficient_after_last {n : ℕ} (H : NaturalUnitInterval n) :
    tableauCoefficient H (n / 2 + 1) = 0 := by
  apply tableauCoefficient_out_of_range
  omega

theorem survivorCoefficient_eq_sub {n : ℕ} (H : NaturalUnitInterval n)
    (hh : HeightTwo H) (k : ℕ) :
    survivorCoefficient H k = tableauCoefficient H k - tableauCoefficient H (k + 1) := by
  have he := tableauCoefficient_eq_next_add_survivor H hh k
  rw [he]
  ring

/-- A finite telescoping identity over any commutative ring. -/
theorem sum_differences_mul_prefix {R : Type*} [CommRing R]
    (T A : ℕ → R) (K : ℕ) :
    (∑ k ∈ Finset.range (K + 1),
      (T k - T (k + 1)) * ∑ j ∈ Finset.range (k + 1), A j) =
    (∑ k ∈ Finset.range (K + 1), T k * A k) -
      T (K + 1) * ∑ j ∈ Finset.range (K + 1), A j := by
  induction K with
  | zero => simp [sub_mul]
  | succ K ih =>
    simp only [Finset.sum_range_succ] at ih ⊢
    rw [ih]
    ring

def survivorExpansion {n : ℕ} (H : NaturalUnitInterval n) (m : ℕ) : Poly m :=
  ∑ k ∈ Finset.range (n / 2 + 1),
    MvPolynomial.C (survivorCoefficient H k) * elementary m (n - k) * elementary m k

def tableauAlternantExpansion {n : ℕ} (H : NaturalUnitInterval n) (m : ℕ) : Poly m :=
  ∑ k ∈ Finset.range (n / 2 + 1), MvPolynomial.C (tableauCoefficient H k) *
    alternant (fun i => delta m i + twoColumnShape m n k i)

/-- The checked algebraic join. Its input is the actual existing survivor
family, and its conclusion is an alternant expansion; H3 still needs to
identify the latter with `vandermonde m * chromatic H m`. -/
theorem vandermonde_mul_survivorExpansion {n : ℕ} (H : NaturalUnitInterval n)
    (hh : HeightTwo H) (m : ℕ) (hm : n ≤ m) :
    vandermonde m * survivorExpansion H m = tableauAlternantExpansion H m := by
  classical
  unfold survivorExpansion tableauAlternantExpansion
  rw [Finset.mul_sum]
  calc
    _ = ∑ k ∈ Finset.range (n / 2 + 1),
        (MvPolynomial.C (tableauCoefficient H k) -
          MvPolynomial.C (tableauCoefficient H (k + 1))) *
          ∑ j ∈ Finset.range (k + 1),
            alternant (fun i => delta m i + twoColumnShape m n j i) := by
      apply Finset.sum_congr rfl
      intro k hk
      have hk' := Finset.mem_range.mp hk
      have hkn : k ≤ n - k := by omega
      have hsum : n - k + k = n := by omega
      have he := vandermonde_mul_two_elementary m (n - k) k hkn (by omega)
      rw [hsum] at he
      rw [survivorCoefficient_eq_sub H hh k, map_sub]
      calc
        _ = (MvPolynomial.C (tableauCoefficient H k) -
            MvPolynomial.C (tableauCoefficient H (k + 1))) *
            (vandermonde m * elementary m (n - k) * elementary m k) := by ring
        _ = _ := by rw [he]
    _ = _ := by
      rw [sum_differences_mul_prefix]
      simp only [tableauCoefficient_after_last, map_zero, zero_mul, sub_zero]

end PartitionH3

#check @PartitionH3.tableauCoefficient_eq_next_add_survivor
#check @PartitionH3.vandermonde_mul_survivorExpansion
#print axioms PartitionH3.list_weight_coefficient
#print axioms PartitionH3.natLt_asymm
#print axioms PartitionH3.tableauCoefficient_eq_next_add_survivor
#print axioms PartitionH3.tableauCoefficient_after_last
#print axioms PartitionH3.survivorCoefficient_eq_sub
#print axioms PartitionH3.sum_differences_mul_prefix
#print axioms PartitionH3.vandermonde_mul_survivorExpansion
