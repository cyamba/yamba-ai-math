import PartitionH3.FiniteH3
import PartitionH3.AlphabetSpecialization

/-!
The all-alphabet height-two survivor formula. The mathematical theorem and
the underlying injection are established work of Cho and Huh. This file
joins the actual coloring polynomial to the original complete survivors;
it does not assert a solution for posets of arbitrary height.
-/

open scoped BigOperators

noncomputable section

namespace PartitionH3

/-- Unconditional H3, for every finite alphabet, including zero. The only
mathematical hypothesis is height two for the given natural unit interval
poset; every coefficient is the weight of the original survivor family. -/
theorem height_two_survivor_expansion {n : ℕ} (H : NaturalUnitInterval n)
    (hh : HeightTwo H) (r : ℕ) :
    chromatic H r =
      ∑ k ∈ Finset.range (n / 2 + 1),
        MvPolynomial.C (survivorCoefficient H k) * elementary r (n - k) * elementary r k := by
  change chromatic H r = survivorExpansion H r
  have he := congrArg (specialize (Nat.le_max_right n r))
    (height_two_survivor_expansion_large_alphabet (m := max n r) H hh (Nat.le_max_left n r))
  simpa only [specialize_chromatic, specialize_survivorExpansion] using he

end PartitionH3

#check @PartitionH3.height_two_survivor_expansion
#print axioms PartitionH3.height_two_survivor_expansion
