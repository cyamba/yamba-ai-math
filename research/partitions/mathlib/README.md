# Finite polynomial bridge for H3

The final all-alphabet height-two theorem is `PartitionH3.height_two_survivor_expansion`
in [H3.lean](PartitionH3/H3.lean). Fresh source checking passed for all 21
modules with 137 principal standard-only axiom reports. The separate
[integration review](../evidence/h3-integration-review-r1.md) and
[natural-transport review](../evidence/h3-integration-review-r2.md) support
the exact source-bound statements. The theorem uses actual proper colorings
and the original complete survivor coefficients, including alphabet zero.
It is separate from the [original Std certificate](../lean/README.md), whose
Lean 4.34.0 pin and independence from Mathlib are preserved.

This project pins Lean **4.34.1** and Mathlib
**`d13f23b723b8a846827a245b89c10fc7d3f11612`**. The committed manifest pins
every transitive Git dependency. All polynomials are actual
`MvPolynomial (Fin m) (Polynomial Int)` values.

| Source | Checked scope |
| --- | --- |
| `PartitionH3/Foundations.lean` | Actual proper-coloring sums with ascent weights; elementary subset products; weights of the existing complete tableau and survivor families; empty/zero-alphabet preliminaries. |
| `PartitionH3/Coloring.lean` | Color classes are comparable and have at most two elements under height two; color reversal preserves properness and exchanges ascents/descents; descents equal the defined finite-pair inversion count for increasing color rows. |
| `PartitionH3/Alternant.lean` | Actual signed monomial alternants; multiplication by an elementary polynomial distributes over all subsets of the prescribed size; repeated exponents force zero. |
| `PartitionH3/Vandermonde.lean` | The coefficient at `delta` is one, hence the alternant is nonzero and multiplication by it cancels; zero variables give one. |
| `PartitionH3/SubsetBridge.lean` | A cardinality-preserving bijection between actual subsets and Boolean lists; unique surviving two-block subsets under the stated no-rise and size hypotheses. |

The exact types, source/configuration hashes, 137 principal dependency reports
and Git revisions are in [verification.json](verification.json). The
[separate semantic review](../evidence/h3-algebra-review-r2.md) supports these
precise interfaces; distinct roles do not imply independent model errors.
The underlying route is Shareshian–Wachs, Sections 4 and 6. The survivor
construction is the attributed Cho–Huh injection. No novelty is claimed.

## Reproduce with existing dependencies

From the repository root:

```sh
python3 research/partitions/mathlib/verify.py --output .runs/mathlib-check.json
python3 research/partitions/verify_all.py
```

The first command checks installed dependencies against the manifest, copies
the project sources and shared Std modules into a fresh temporary project,
builds without reusing project proof products, and checks each bridge source
and a printed statement inventory. Only products of the pinned dependencies
are reused. It rejects diagnostics, missing reports, changed sources,
nonstandard axioms and proof placeholders. Failure writes a failed record and
returns a nonzero exit code. It never installs a missing toolchain/library.

The second command also runs all repository tests, the repository checker
and the original Std certificate. Its default source-bound report is in
ignored `.runs/partition-verification/latest.json`. A passed build record is
different from a completed H3 proof; the bridge record reports the exact checked H3 declaration, while
semantic review remains a separate record. Missing evidence is never inferred.

## Optional initial setup

With elan already available, setup from this directory is:

```sh
elan toolchain install leanprover/lean4:v4.34.1
MATHLIB_NO_CACHE_ON_UPDATE=1 lake update
lake exe cache get Mathlib.RingTheory.MvPolynomial.Symmetric.Defs Mathlib.Algebra.Polynomial.Basic Mathlib.GroupTheory.Perm.Sign
```

This requests the three imports and their transitive dependencies rather
than a full Mathlib cache. Lean and the original Std certificate do not need
Mathlib. The user-selected local setup had a 20 GiB free-space entry buffer,
a 15 GiB additional-storage cap, a 5 GiB free-space stop and a cumulative
60-minute initial build budget with one diagnosed retry. These are resource
bounds for that setup, not minimum requirements of Lean. The recorded setup
used about 4.76 GiB additional allocated storage, within those bounds; see
[the author receipt](../evidence/h3-algebra-revision-r1.md).

## Integration modules

The twenty-one-module project additionally checks `ElementaryProduct`, `Reconstruction`,
`ColorSymmetry`, `ColorCoefficients`, `SignedCancellation`, `PermutationSign`,
`ArrayColorBridge`, `FamilyPadding`, `FamilyReindex`, `SurvivorAlgebra`,
`DominantShape`, `ChromaticArrays`, `FiniteH3`, `AlphabetSpecialization` `H3` and `NaturalCoefficients`.
They supply actual coefficient extraction, complete finite reindexing, list sign
and statistic translation, canonical padding, dominant shape classification,
H2 telescoping, valid cancellation and specialization from max(n,r).

See the [claim index](../evidence/claim-to-theorem-index.md) and
[author handoff](../evidence/h3-integration-r1.md) for exact statements, hypotheses,
source hashes and review status. This is a formalization of an established
height-two result, not a new solution in arbitrary height.

The natural-coefficient restatement is
`PartitionH3.height_two_survivor_expansion_nat`. Its `natChromatic`,
`natElementary` and `natSurvivorCoefficient` are actual finite sums over
`Polynomial Nat`. The proved injective coefficient maps identify them with
the integer sums and transport the equality back, including alphabet zero.
The [auxiliary handoff](../evidence/h3-integration-r2.md) records the exact
source and direct check; the [final review](../evidence/h3-integration-review-r2.md)
and fresh build support the natural-coefficient theorem.
