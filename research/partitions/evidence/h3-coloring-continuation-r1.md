# P011 author revision: actual colorings and complete finite cancellation

Status: **proved by Lean kernel checking; final semantic review pending**.
H3 is incomplete. The exact sources below are frozen for the reserved second
P011 challenge. The first challenge reviewed the written construction, not
these new declarations. No previous P007/P008 review account is reset.

| Source in `mathlib/PartitionH3/` | SHA-256 | Fresh check | Principal dependency reports |
| --- | --- | --- | --- |
| `ColorSymmetry.lean` | `feac033bd1b0c60e0a76bb30bef4a952e4196de234f4961da7d26d881bcfcbd9` | exit 0, 12.958 s | 11 |
| `ColorCoefficients.lean` | `add42ddeec6437c9fb74ac3232c1faa10447c27a7351eced81b240147c5f764a` | exit 0, 2.831 s | 8 |
| `SignedCancellation.lean` | `31a81b5ca7fcb1e85fda791c96feb81498fdccade4f76b03af6ba974a5134656` | exit 0, 10.837 s | 9 |

Each run emitted a new `.olean`, reported no warnings/errors, retained the
same source hash, and printed only `propext`, `Classical.choice`, `Quot.sound`
dependencies. Exact output and JSON receipts are in ignored
`.runs/h3-p011-root-r1/`. These development checks reused locally compiled
imports; the final project verifier must rebuild every project source in a
fresh workspace. Toolchain and manifest pins are unchanged.

## Exact mathematical scope

`chromatic_isSymmetric H hh` proves `MvPolynomial.IsSymmetric (chromatic H m)`
for every natural `n,m`, monotone extensive `NaturalUnitInterval n` and actual
`HeightTwo H`. It has no positive alphabet hypothesis or coloring expansion
premise. The involution acts on actual functions `Fin n -> Fin m`.

The implementation refines the round-1 written rule into a support-only mask:
for the two-color support `U`, swap all vertices when `|U|=3` and there is no
isolated vertex; otherwise swap the isolated vertices. This also swaps some
balanced colorings, which preserves the required monomial. The same support
and graph determine the mask on reapplication, proving unconditional
involutivity. Properness holds for every graph encoded by `H`. For adjacent
colors, isolated swaps preserve each outside-edge comparison. In the
three-vertex path case monotonicity forces `u<z<v`; an explicit permutation
of ordered vertex pairs interchanges the two internal edges. No monotonicity
or adjacency hypothesis from the first review was dropped.

`unflipped_balanced` proves the required aggregate monomial equality. If an
isolated vertex exists, each nonisolated color class has at most one vertex:
two equal-colored vertices together with the isolated vertex would be three
independent vertices, forbidden by height two. Every nonisolated vertex has
an oppositely colored nonisolated neighbor. If there is no isolated vertex
outside the three-vertex branch, class-size bounds and the binary support
cardinality force equal multiplicities. Products are grouped by actual
color fibers. Finite coloring reindexing and generation by adjacent swaps
then prove symmetry, including `m=0,1`.

`vandermonde_chromatic_coefficient H hh lambda` proves the exact equality

```text
coeff_(delta+lambda)(Delta * X)
 = sum sigma,kappa,
   if Proper H kappa and
      forall i, (|class(kappa,i)| : Int)
        = (lambda(sigma i) : Int) - (sigma i : Int) + (i : Int)
   then sign(sigma) * q^(descents H kappa) else 0.
```

Here `sigma` ranges over the actual finite permutation group and `kappa`
over all actual finite coloring functions. The proof uses genuine polynomial
coefficients, symmetry and rename coefficient transport. Color reversal
identifies the ascent and descent polynomials; its permutation direction is
explicit. Negative shifted lengths are not truncated. The `lambda` in this
coefficient theorem is any natural exponent function on `Fin m`; no
partition or desired tableau expansion is assumed.

`mem_signedArrayUniverse` constructs a complete finite enumeration, with
membership **equivalent** to the original `SignedArrays.SignedArray` predicate
and exact array length `m`. Entries have real permutation labels, empty rows
are included, and row bounds follow from the full bijective filling. This
is not a selected subfamily or an assumed finite universe.

`natural_signed_array_cancellation H hh lambda hp m` sums the checked actual
involution over that entire universe. Nonfixed terms cancel using their
opposite original list permutation signs and equal original tableau inversion
statistics. Fixed terms have sign `+1` and are exactly padded tableaux.
Partitionhood is explicit for the fixed-sector theorem. No identification
with the original complete `columnFamily` is assumed or yet proved.

## Attribution, author roles and remaining interfaces

These formalize the established Shareshian--Wachs coloring/alternant route
and the previously checked local signed-array construction. They claim no
new positivity theorem or priority. The original Cho--Huh survivor injection
and complete families are unchanged.

Root authored `ColorSymmetry.lean` and `ColorCoefficients.lean`. The algebra
specialist wrote `SignedCancellation.lean` before its turn returned a usage
limit error. That failed dispatch is retained and counted; root completed
the source check and fixed three linter diagnostics. There was no nested
fleet, new dependency download or toolchain installation. The only project
configuration addition exposes the existing Std `SignedArrays` library to
the pinned Mathlib project.

The outstanding integration is substantive: actual coloring/permutation
sectors must be bijective with the enumerated list arrays, original list
inversions must equal coloring descents, and `Equiv.Perm.sign` must agree
with the original list inversion-parity sign. Canonical removal of trailing
padding must recover the **complete existing families**, not an existential
body predicate. Dominant coefficient support, H2 polynomial lifting and
telescoping, and all-alphabet specialization then remain. None is inferred
from these checks or from finite numerical agreement.

P011 accounting before the reserved second challenge: initial written
proposal 3, first critic challenge 2, root revision 3, additional signed-sum
author dispatch 3 (usage error retained): **11/16** proxy units. The final
challenge costs 2, for **13/16**. Units are not tokens or monetary costs.
