import Mathlib.RingTheory.MvPolynomial.Symmetric.Defs
import Mathlib.Algebra.Polynomial.Basic
import WeightedCancellation

/-!
Actual finite coloring and subset polynomials for H3.
No Schur expansion, positivity witness, or final coloring identity is assumed.
-/

open scoped BigOperators

noncomputable section

namespace PartitionH3

abbrev Coeff := Polynomial ℤ
abbrev Poly (m : ℕ) := MvPolynomial (Fin m) Coeff

structure NaturalUnitInterval (n : ℕ) where
  h : Fin n → Fin n
  extensive : ∀ i, i ≤ h i
  monotone : Monotone h

def PosetLt {n : ℕ} (H : NaturalUnitInterval n) (i j : Fin n) : Prop := H.h i < j

def HeightTwo {n : ℕ} (H : NaturalUnitInterval n) : Prop :=
  ∀ i j k, ¬ (PosetLt H i j ∧ PosetLt H j k)

def Edge {n : ℕ} (H : NaturalUnitInterval n) (i j : Fin n) : Prop :=
  i < j ∧ j ≤ H.h i

def Proper {n m : ℕ} (H : NaturalUnitInterval n) (κ : Fin n → Fin m) : Prop :=
  ∀ i j, Edge H i j → κ i ≠ κ j

def ascents {n m : ℕ} (H : NaturalUnitInterval n) (κ : Fin n → Fin m) : ℕ := by
  classical
  exact (Finset.univ.filter (fun p : Fin n × Fin n =>
    Edge H p.1 p.2 ∧ κ p.1 < κ p.2)).card

def descents {n m : ℕ} (H : NaturalUnitInterval n) (κ : Fin n → Fin m) : ℕ := by
  classical
  exact (Finset.univ.filter (fun p : Fin n × Fin n =>
    Edge H p.1 p.2 ∧ κ p.2 < κ p.1)).card

def colorMonomial {n m : ℕ} (κ : Fin n → Fin m) : Poly m :=
  ∏ i, MvPolynomial.X (κ i)

def chromatic {n : ℕ} (H : NaturalUnitInterval n) (m : ℕ) : Poly m := by
  classical
  exact ∑ κ : Fin n → Fin m,
    if Proper H κ then MvPolynomial.C (Polynomial.X ^ ascents H κ) * colorMonomial κ else 0

def elementary (m k : ℕ) : Poly m := MvPolynomial.esymm (Fin m) Coeff k

/-- Extension by false to the Nat labels used by the original complete families. -/
def natLt {n : ℕ} (H : NaturalUnitInterval n) (i j : ℕ) : Prop :=
  if hi : i < n then
    if hj : j < n then PosetLt H ⟨i, hi⟩ ⟨j, hj⟩ else False
  else False

noncomputable instance natLt_decidable {n : ℕ} (H : NaturalUnitInterval n) :
    DecidableRel (natLt H) := Classical.decRel _

def tableauWeight {n : ℕ} (H : NaturalUnitInterval n) (family : List CornerSlide.Rows) :
    Coeff :=
  (family.map (fun rows =>
    Polynomial.X ^ CornerSlide.tableauGraphInversions (natLt H) rows)).sum

/-- Uses the complete existing family, including its out-of-range guard. -/
def tableauCoefficient {n : ℕ} (H : NaturalUnitInterval n) (k : ℕ) : Coeff :=
  tableauWeight H (CornerSlide.columnFamily (natLt H) (List.range n) k)

/-- Uses the full image complement of the original bubbling injection. -/
def survivorCoefficient {n : ℕ} (H : NaturalUnitInterval n) (k : ℕ) : Coeff :=
  tableauWeight H (CornerSlide.survivorFamily (natLt H) (List.range n) k)

theorem elementary_zero (m : ℕ) : elementary m 0 = 1 := by
  simp [elementary]

theorem elementary_isSymmetric (m k : ℕ) :
    MvPolynomial.IsSymmetric (elementary m k) :=
  MvPolynomial.esymm_isSymmetric (Fin m) Coeff k

theorem chromatic_empty (H : NaturalUnitInterval 0) (m : ℕ) : chromatic H m = 1 := by
  classical
  simp [chromatic, Proper, Edge, ascents, colorMonomial]

theorem chromatic_zero_alphabet {n : ℕ} (hn : 0 < n) (H : NaturalUnitInterval n) :
    chromatic H 0 = 0 := by
  classical
  let : Nonempty (Fin n) := ⟨⟨0, hn⟩⟩
  simp [chromatic]

end PartitionH3

#check @PartitionH3.chromatic
#check @PartitionH3.elementary
#check @PartitionH3.tableauCoefficient
#check @PartitionH3.survivorCoefficient
#print axioms PartitionH3.elementary_zero
#print axioms PartitionH3.elementary_isSymmetric
#print axioms PartitionH3.chromatic_empty
#print axioms PartitionH3.chromatic_zero_alphabet
