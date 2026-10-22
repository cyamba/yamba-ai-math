# Separate semantic review of the H3 signed-array pilot

Reviewed 2026-10-22 by `/root/h3_semantic_critic`, separately from the author
`/root/h3_lean_algebra`. These are distinct role identities, not a claim of
independent errors or different models. This is the second and final
substantive review of the signed-array pilot; the earlier route preflight was
not an implementation review. No proof source was edited by the critic.

**Verdict: supported for the exact list-based signed-array statements below;
H3 remains incomplete. No actionable mathematical defect found.**

## Reviewed source and check

- `../lean/SignedArrays.lean`, SHA-256
  `c33f65fbae13d490d5fb1bcd83d4ded974b7cbac2a25ab5a826aac4b974412ad`.
- Imported `../lean/CornerSlide.lean`, SHA-256
  `b4f5c7efa75e4a311d84e1db4115e8d27ecedf4f364ad9cdd459f5a33b962af1`.
- The critic inspected both the source semantics and
  [the author handoff](h3-signed-array-handoff.md), then independently ran
  `lake env lean SignedArrays.lean` with the installed Lean 4.34.0 toolchain.
  It exited zero without diagnostics. All 16 printed axiom reports used only
  `propext`, `Quot.sound`, and, where needed, `Classical.choice`. Source hashes
  were unchanged after this check.
- This critic check reused existing imports. It was not a fresh source-only
  reproduction; the author's separate fresh-copy check is identified in the
  handoff. Repository-wide verification and verifier integration remain the
  lead's responsibility. No provisioning or finite numerical experiment was
  used to justify the universal statements.

## Exact scope and checked declarations

`SignedArray r vertices lambda a` requires that `labels a` actually permute
`range a.length`, that every row satisfy the integer shape equation
`length(row_i) = lambda(pi(i)) - pi(i) + i`, and that the flattened rows
bijectively fill the distinct supplied vertices with actual chain rows.
It does not itself assert partitionhood or height two.

The reviewed principal declarations are:

| Declarations | Supported statement and material hypotheses |
| --- | --- |
| `shiftKey_injective`, `adjacent_length_exclusion` | Explicit `Partition lambda` makes shifted keys distinct and excludes an adjacent increase of exactly one; row lengths are cast to integers. |
| `height_two_row_length_le_two` | Actual chain rows have length at most two under `CornerSlide.NoThreeChain r`. |
| `togglePair_involution`, `bottommost_pivot_stable`, `move_involution` | The actual toggle and suffix-first move are involutions for every relation and array. The suffix predicate checks first-column conditions, so unchanged lower first entry suffices for pivot stability. |
| `move_signedArray` | The same vertex filling, actual label permutation, integer shape equations, and chain rows survive the move. No partition or height assumption is needed for preservation. |
| `move_tableauGraphInversions` | Under `ChainArray`, the existing actual `CornerSlide.tableauGraphInversions` is preserved. The proof uses the existing word equivalence and comparable-swap theorem, with the original natural-label `graphScore`. |
| `move_fixed_iff_good`, `columns_iff_good` | Under explicit partitionhood, height two, distinct labels, integer shape and chain rows, fixedness is exactly the good first-column predicate, and that predicate is exactly all-column validity. The excluded singleton/pair case uses shifted shape; a second-column descent in two pair rows contradicts height two. |
| `signedArray_fixed_iff_padded` | Under `SignedArray`, partitionhood and height two, `move r a = a` iff the rows equal `body ++ replicate k []` for an actual existing `CornerSlide.Tableau r vertices body`. |
| `fixed_labels_identity`, `fixed_row_lengths` | The fixed signed sector has `labels a = range a.length` and the entire padded row profile equals `(range a.length).map lambda`. |
| `move_sign_reversing` | Distinct labels and `move r a ≠ a` imply `permutationSign (labels (move r a)) = -permutationSign (labels a)`. This is the parity of the actual label inversion count, not an unconstrained sign field. |
| `signedArray_bad_sign_reversing`, `fixed_permutationSign` | With explicit partitionhood, height two and `SignedArray`, every bad first-column sector reverses sign and every fixed sector has sign `1`. |

The key fixed-sector signature is exactly:

```lean
signedArray_fixed_iff_padded (r : Nat → Nat → Prop)
  (height : NoThreeChain r) (lambda : Nat → Nat) (hp : Partition lambda)
  (vertices : List Nat) (a : Array) (h : SignedArray r vertices lambda a) :
  move r a = a ↔ PaddedTableau r vertices (rows a)
```

The conclusions are neither coefficient-expansion assumptions nor proxy
tableau predicates. The tableau body includes the original nonempty-row,
shape/order, column and bijective-filling conditions. The independent identity
label and padded-length lemmas supply the specified partition shape.

## Retained integration obligations

1. Enumerate the complete fixed-length finite signed sectors without
   duplication and prove signed-sum cancellation using this involution.
2. Prove the canonical padding/removal bijection with the existing complete
   `CornerSlide.family`; the present existential padded characterization is
   not that finite counting bijection.
3. Match the inversion-parity sign to whichever permutation/alternant
   interface integration chooses, including inverse-permutation reindexing.
4. Prove the actual coloring symmetry and ascent/descent orientation,
   alternant coefficient identity, elementary identities, polynomial
   reconstruction/cancellation, and variable specialization. Connect the
   result to the complete survivor families from H2.
5. Run the lead's final source-bound and repository verification, and keep
   primary-source attribution separate from kernel checking.

These are absent results, not hidden assumptions or defects in the reviewed
pilot. The pilot proves no final actual-coloring expansion, H3 completion,
general positivity theorem, or novelty claim. No third signed-array semantic
review round was used.
