# H3 signed-array pilot handoff

**Proved, kernel-checked author result; independent final semantic review is
separate.** Source: `../lean/SignedArrays.lean`, SHA-256
`c33f65fbae13d490d5fb1bcd83d4ded974b7cbac2a25ab5a826aac4b974412ad`.
The source imports only the existing `CornerSlide` module and its bundled Std
dependency. It changes no previously checked source module.

## Exact checked interface

- `ChainArray r vertices a` allows empty rows and requires distinct vertices,
  a permutation filling of that exact vertex list, and actual chain rows.
  `SignedArray` additionally requires the actual label list to permute
  `range a.length` and the integer equations
  `length(row_i) = lambda(pi(i)) - pi(i) + i`.
- `shiftKey_injective` and `adjacent_length_exclusion` use explicit
  `Partition lambda` (weak decrease). Adjacent lengths `(0,1)` and `(1,2)`
  are excluded, without truncated subtraction.
- `togglePair` performs exactly
  `[]/[b,a] <-> [a]/[b]` when `r b a`, swapping the adjacent permutation
  labels too. `move` scans the suffix first and acts at the bottommost
  first-column defect. Malformed local boundaries stay fixed in the general
  definition; `move_fixed_iff_good` rules out those extra fixed cases under
  the actual partition shape, distinct labels, chain rows and
  `CornerSlide.NoThreeChain r`.
- `move_involution` holds for every array and every relation.
  `bottommost_pivot_stable` preserves the good first-column suffix.
  `move_signedArray` preserves the actual label permutation, integer shape,
  row chains and bijective filling. Shape preservation is global, so the
  possible creation of a forbidden `(1,2)` neighbor is not assumed away.
- `move_tableauGraphInversions` preserves the existing actual row-based
  inversion degree. Its proof uses
  `CornerSlide.graph_inversions_comparable_swap` and
  `CornerSlide.tableau_graph_inversions_eq_word`.
- `columns_iff_good` checks all columns. A hypothetical second-column
  descent between two pair rows contradicts the explicit height hypothesis.
  `signedArray_fixed_iff_padded` identifies fixed arrays exactly with
  `body ++ replicate k []`, where `body` is an actual existing `Tableau`.
- `fixed_labels_identity` proves `labels a = range a.length`.
  `fixed_row_lengths` proves the entire padded row profile is
  `(range a.length).map lambda`.
- `permutationSign` is the integer sign defined by the parity of the actual
  label inversion count. `move_sign_reversing` proves sign reversal whenever
  the array is moved and labels are distinct.
  `signedArray_bad_sign_reversing` supplies the intended bad-sector instance;
  `fixed_permutationSign` proves every fixed signed array has sign `1`.

The fixed-sector, identity-permutation and signed bad-sector conclusions all
explicitly assume both partition shape and height at most two. Neither is
silently inferred from `SignedArray`.

## Actual execution and resource receipt

Author direct check: `lake env lean SignedArrays.lean`, Lean **4.34.0**, exit
zero with no diagnostics. A second check copied `CornerSlide.lean`,
`SignedArrays.lean`, and the pinned toolchain file into a fresh temporary
directory, compiled both sources to new `.olean` files, and checked the exact
types of all 16 principal declarations. All four processes exited zero;
source hashes were unchanged before/after. Temporary build storage was
**2,371,167 bytes**, cumulative process wall time **7.6244 seconds**. The
temporary directory was removed. No package, toolchain or Mathlib was installed.

The ignored execution receipt and full output are at
`.runs/h3-signed-array-author-20261022/receipt.json` and `check-0.txt` through
`check-3.txt`. The copied foundation source had SHA-256
`b4f5c7efa75e4a311d84e1db4115e8d27ecedf4f364ad9cdd459f5a33b962af1`;
the toolchain file had SHA-256
`8733782dc070a99b312039cda424f601b80f3be6f6f512627da5ba25adc27632`.

All 16 printed dependency lists contain only `propext`, `Quot.sound` and,
where needed, `Classical.choice`. No proof placeholder, custom axiom,
`unsafe` or `native_decide` is present. Repository-wide validation and the
root's source-bound verifier integration are separate pending checks.

## Remaining H3 obligations

There is no unresolved permutation/sign obligation for the list-based
definitions above. The module does not yet give a finite enumeration and
signed-sum cancellation theorem for all sectors, a canonical padding bijection
to `CornerSlide.family`, or a conversion from this inversion-parity sign to a
separately chosen permutation-library sign. Those are integration obligations,
not hypotheses of the checked theorems.

It also does not prove the actual coloring expansion, alternant identities,
polynomial cancellation, variable specialization, or the final equality with
the complete survivor families. No H3 completion or novelty claim follows from
this pilot alone. The construction follows the accepted H3 proof specification;
primary-source inspection and its attribution remain in the separate source
and semantic review rather than being inferred from compilation.
