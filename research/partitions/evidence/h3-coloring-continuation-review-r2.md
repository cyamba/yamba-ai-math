# P011 round 2: symmetry, coefficients and finite cancellation

Reviewed 2026-10-23 by `/root/h3_semantic_critic`, separately from the authors
identified in [the frozen handoff](h3-coloring-continuation-r1.md). This is
the second and final P011 challenge, not another historical P008 review.
Distinct roles do not establish independent errors or different models.
The critic edited no proof source.

**Verdict: supported for the exact interfaces below.** No actionable
semantic defect was found. Actual chromatic symmetry, signed coloring
coefficient extraction, and cancellation over the constructed complete
signed-array universe are checked results. Their correspondence with one
another and with the existing complete tableau families remains unproved;
H3 is incomplete.

## Source-bound scope and execution

| Source under `../mathlib/PartitionH3/` | Reviewed SHA-256 |
| --- | --- |
| `ColorSymmetry.lean` | `feac033bd1b0c60e0a76bb30bef4a952e4196de234f4961da7d26d881bcfcbd9` |
| `ColorCoefficients.lean` | `add42ddeec6437c9fb74ac3232c1faa10447c27a7351eced81b240147c5f764a` |
| `SignedCancellation.lean` | `31a81b5ca7fcb1e85fda791c96feb81498fdccade4f76b03af6ba974a5134656` |

The handoff snapshot SHA-256 is
`571bc311a411e0b21105d2f4a87506049650235996792462e2b7c86dea9afca9`.
The imported original `../lean/SignedArrays.lean` retains its previously
reviewed hash
`c33f65fbae13d490d5fb1bcd83d4ded974b7cbac2a25ab5a826aac4b974412ad`;
this review uses its frozen interface rather than reopening its two reviews.

The critic independently ran `lake env lean` on each of the three new
sources using existing Lean 4.34.1 and pinned Mathlib dependencies. All
three exited zero without diagnostics. The actual outputs printed the
principal types and all **28** dependency reports (11, 8 and 9), using only
`propext`, `Classical.choice`, and `Quot.sound`. Source hashes were unchanged
after checking. These were direct source checks with existing imports, not
a second fresh-project reproduction.

The critic also inspected the three JSON receipts in
`.runs/h3-p011-root-r1/`. Their source hashes match the frozen files, and
the actual log hashes match their respective recorded values:

- `ColorSymmetry.log`:
  `c79905806b4fddeee9ea71a6aa268bd06bf0ca5c025a04932c949324046698c8`.
- `ColorCoefficients.log`:
  `91d08c4c3217545d63219ceaba63a68eb28b161e0f97d74d1922fbf0d3e1b4b3`.
- `SignedCancellation.log`:
  `3b4886b6cbf807e77f8a223cc94eb64736531a230f013e7989800cd54f90dfd4`.

Those receipts separately record successful fresh output-file checks.
The critic did not independently measure their elapsed times or provision
dependencies. Final all-source clean verification remains separate.

## Findings

1. **The support-only revision is sound and proves actual symmetry.**
   `toggleMask` depends only on the actual two-color support and its induced
   graph: use the entire support precisely when its cardinality is three
   and it has no isolated vertex; otherwise use its isolated vertices.
   `colorPair_flipOn` preserves this support on every coloring, so
   `toggleColors_involutive` needs neither properness nor height. Properness
   is preserved in both branches, including on improper colorings via the
   proved equivalence. The map need not retain the round-1 identity rule
   on every balanced coloring; the required aggregate monomial and ascent
   invariants, rather than that implementation choice, are proved.

   The exact final interface is

   ```lean
   chromatic_isSymmetric {n m : Nat} (H : NaturalUnitInterval n)
     (hh : HeightTwo H) : MvPolynomial.IsSymmetric (chromatic H m)
   ```

   It concerns the actual proper-function sum, not a symmetric witness or
   assumed expansion. Adjacent swaps generate the full finite permutation
   group; the proof handles the zero-variable group explicitly and does
   not exclude `m=1` or `n=0`.

2. **Ascent and monomial preservation have the needed distinct arguments.**
   Isolated flips preserve each incident outside-edge comparison using
   adjacency of the two colors. The three-vertex full-swap branch proves
   the comparable double class and the middle singleton in natural label
   order using actual monotonicity. `path_internal_edges` identifies both
   internal ordered edges, and the ascent proof swaps those two ordered
   pairs while preserving every other contribution. Thus it does not
   incorrectly assert that each internal edge keeps its ascent status.
   `unflipped_balanced` proves equality of the two actual unflipped color
   fibers: with an isolated vertex, two equal-colored nonisolated vertices
   would yield three independent vertices; without one, the class-size
   bounds and support cardinality exclude unequal residual counts.
   Fiberwise products then prove the actual monomial-renaming equality.
   Neither pointwise swapping of every coloring nor a positivity premise
   is assumed.

3. **Coefficient direction, integer shape and descent weight are correct.**
   `vandermonde_weighted_coefficient` explicitly requires symmetry for a
   generic weight. The actual chromatic specialization discharges that
   premise using the new symmetry theorem and the proved color-reversal
   equality. It concludes, for every `lambda : Fin m → Nat`,

   ```text
   coeff_(delta+lambda)(Delta * chromatic H m)
     = sum sigma,kappa,
       if Proper H kappa and
          forall i, (colorDegree kappa i : Int)
            = (lambda (sigma i) : Int) - (sigma i).val + i.val
       then sign(sigma) * q^(descents H kappa) else 0.
   ```

   `coeff_rename_at` correctly transports the target exponent to
   `alpha (sigma i)`. Applying it inside antisymmetrization yields the
   displayed forward permutation labels; this is consistent with the
   intended array shape, not an accidental inverse substitution.
   `shifted_color_shape` casts bounded `delta` entries before deriving an
   integer equation. Negative requested lengths cannot be filled and are
   never truncated. Partitionhood is not silently assumed for `lambda`.

4. **The array universe is complete and finite, including empty rows.**
   `finiteLists` enumerates every exact-length list over its finite
   alphabet, and `finiteRows` includes length zero and all rows up to the
   full filling length. Every row of a signed array is a sublist of its
   bijective flattened filling, proving those bounds rather than assuming
   them. The exact public membership theorem is

   ```lean
   mem_signedArrayUniverse (r : Nat → Nat → Prop) (vertices : List Nat)
     (lambda : Nat → Nat) (m : Nat) (a : SignedArrays.Array) :
     a ∈ signedArrayUniverse r vertices lambda m ↔
       SignedArrays.SignedArray r vertices lambda a ∧ a.length = m
   ```

   The enumeration is a `Finset`, so it introduces no duplicate
   multiplicities. There is no selected-subfamily or enumeration-completeness
   premise. With zero slots the only candidate is `[]`; its actual filling
   predicate decides whether it belongs. Empty rows remain available at
   every slot count. No nonempty vertex or alphabet restriction occurs.

5. **Finite cancellation has the claimed original sign and statistic.**
   `signedArrayWeight` uses the original list inversion-parity sign and
   `CornerSlide.tableauGraphInversions`, cast into `Polynomial Int`.
   Nonfixed terms cancel by the previously checked actual involution,
   sign reversal and original statistic preservation. The generic theorem
   for an arbitrary finite set `A` has an explicit exact-membership premise;
   `signedArray_universe_cancellation` discharges it with the constructed
   universe from item 4. Under explicit global partitionhood and height
   two, the remaining terms have sign one and satisfy the actual original
   `PaddedTableau` predicate. `heightTwo_natLt_noThreeChain` proves the
   finite-to-Nat height transfer, including false relations outside the
   supplied vertices. Consequently `natural_signed_array_cancellation`
   is an unconditional finite-sum identity under its stated `HeightTwo H`
   and `SignedArrays.Partition lambda` hypotheses. It does not yet identify
   that padded-array sum with `CornerSlide.columnFamily` or a coloring sum.

## Retained interfaces and accounting

The signed-coloring sum in item 3 and signed-array sum in item 5 are still
different mathematical objects. Integration must prove their actual
bijection, reconcile `Fin m` exponent functions with the Nat partition
interface, identify coloring descents with the original list statistic,
and equate library permutation sign with original list parity sign.
Canonical padding removal must biject with the full existing tableau
families. Dominant-support restriction, H2 polynomial lifting/telescoping,
natural-coefficient transfer and all-alphabet specialization remain.
Neither agreement of names nor these separate checked identities supplies
any of those results. No H3 completion or novelty claim is supported yet.

The handoff retains the signed-source author's usage-limit failure and the
lead's subsequent checks/linter corrections. This challenge adds 2 declared
proxy units to 11, giving **13 of 16**. Both P011 review rounds are now used;
unused numerical allowance does not authorize a third challenge. Historical
P007/P008 accounts stay frozen. This is manual collaboration, and units are
neither tokens nor monetary costs.
