# Lean certificate for the tableau correction

Checked on 22 October 2026 with Lean 4.34.0 and its bundled `Std` library.
There are no external Lean dependencies. This formalizes a local obstruction
and the combinatorial core of a known construction; it is not a new solution
of a general positivity conjecture.

The bubbling construction is Cho–Huh's injection `ψ_ℓ`, Section 3.1 of
[*On e-positivity and e-unimodality of chromatic quasisymmetric functions*](https://arxiv.org/abs/1711.07152),
SIAM Journal on Discrete Mathematics 33 (2019), 2286–2315. The article records
the inspected prior work and the complete written coefficient argument.

## Objects and hypotheses

`Tableau r vertices rows` is a list of nonempty rows with:

- strict `r`-chains along every row;
- no descent between vertically adjacent cells, and weakly decreasing row lengths;
- a flattened filling that is a permutation of the distinct list `vertices`.

Thus the predicate includes shape, order, and bijective filling. It is not a
Boolean proxy for those conditions. The relation is on natural-number labels.
A finite poset relation may be extended by false outside its vertex set.
`NoThreeChain r` excludes `r x y` and `r y z` holding together. For a strict
poset relation, this is exactly the height-at-most-two hypothesis.

The source is `front ++ [[c,d]] ++ singletons tail`. The simple demotion splits
the pair into `[c],[d]`. The bubbling map instead inserts `d` after the maximal
initial segment of `tail` consisting of labels `z` with `r z d`. Source
validity supplies `r c d`. `front` and `tail` have arbitrary finite lengths.

## Assurance map

| Lean theorem | Universally checked statement |
| --- | --- |
| `demote_valid_iff` | For a valid source and asymmetric `r`, simple demotion is valid iff the suffix is empty or its first entry is not below `d`. |
| `flatten_before_after` | Simple demotion leaves the entire row-major word unchanged. |
| `counterexample_source`, `counterexample_target_invalid` | The five-vertex total-order filling `[[1,2],[3,5],[4]]` is valid; its direct demotion is invalid. |
| `bubble_tableau_valid` | Bubbling produces an actual valid tableau for every asymmetric `r`; no height hypothesis is needed. |
| `extract_bubble_inverse_height_two` | For height at most two, extraction of the first label above `c` recovers `(d,tail)` from the inserted suffix. |
| `bubble_tableau_injective` | Equal actual output tableaux, with equal split-row indices, recover `front,c,d,tail`. This proves injection of each fixed-shape family, allowing the front and corner labels to vary. |
| `graph_inversions_comparable_swap` | Swapping adjacent comparable labels in any word context preserves graph inversions. |
| `tableau_graph_inversions_eq_word` | For chain rows, the usual row-based graph inversion statistic equals the word statistic. |
| `bubble_tableau_graph_inversions` | Bubbling preserves that actual row-based tableau inversion statistic. |
| `collision_source_other`, `collision_without_height_two` | Two distinct valid total-order tableaux map to `[[1,2],[3],[4],[5]]`. Height at most two is essential for the stated inverse and injection. |

The injection theorem explicitly assumes equal front lengths. In the intended
source shape `(2^(k+1),1^m)`, that length is the fixed integer `k`; it is not
an extra restriction on the fillings. The output shape has `k` two-cell rows
followed by `m+2` singleton rows.

`CornerSlide.lean` also proves the general extraction theorem under its weaker explicit
separation condition, arbitrary-score adjacent-swap lemmas, filling preservation,
and the simple bottom-row corollary. The source prints axiom dependencies for
the principal statements.

## Complete families and weighted cancellation

[TableauFamilies.lean](TableauFamilies.lean) defines all fillings of a fixed
row-length list using a finite vertex list, filters by the actual `Tableau`
predicate, and removes duplicates. Its use of classical decidability makes the
family definition noncomputable; no efficient enumeration algorithm is claimed.

| Lean declaration | Universally checked statement |
| --- | --- |
| `mem_family` | Membership iff actual tableau validity and the exact row-length list; completeness is proved without an enumeration premise. |
| `family_nodup` | Every tableau appears at most once. |
| `pair_decomposition` | Shape `(2^(k+1),1^m)` determines a front of exactly `k` two-cell rows, the final pair, and the singleton suffix. |
| `bubbleAt_family` | The derived split maps the entire source family into shape `(2^k,1^(m+2))`. |
| `bubbleAt_family_injective` | Height at most two gives injectivity on that complete source family. |
| `bubbleAt_family_weight` | The actual row-based inversion degree is preserved on the family. |

[WeightedCancellation.lean](WeightedCancellation.lean) defines `degreeCount`
and proves the image/complement decomposition for any finite weight-preserving
injection. It then instantiates that theorem with these complete families.
`columnFamily r vertices k` is empty when `2*k > vertices.length`; the guard is
tested before the natural-number difference in the shape. `survivorFamily`
is the complement of the **full image** of the next source family.

For every `k` and degree `d`, `height_two_degreewise_cancellation` proves

```text
count(columnFamily k, inv = d)
  = count(columnFamily (k+1), inv = d) + count(survivorFamily k, inv = d).
```

This uses addition of natural counts. It does not rely on truncated subtraction
or assume a polynomial coefficient identity. Empty and one-vertex families
each have exactly one tableau of degree zero, by `empty_vertex_degree_count`
and `single_vertex_degree_count`. `survivorFamily_empty_source` handles the
odd and even maximal indices and every other empty-next-source case.

`finiteRelation vertices base` extends a relation by false outside `vertices`.
`finite_height_two_degreewise_cancellation` requires asymmetry and the absence
of three-element chains only on those vertices, then applies the all-index
theorem to that extension. Transitivity is not needed by the combinatorial
identity; every strict finite poset of height at most two meets its hypotheses.
No equivalence with a separately defined coloring polynomial is assumed.

## Signed arrays with empty rows

[SignedArrays.lean](SignedArrays.lean) adds a checked involution on actual
chain arrays. Empty rows are allowed, the filling is a permutation of the
distinct vertex list, and permutation labels satisfy the integer equations
`length(row_i) = lambda(pi(i)) - pi(i) + i`. Partitionhood and height at most
two are explicit hypotheses where needed; they are not inferred from this
definition.

The suffix-first move toggles `[]/[b,a]` with `[a]/[b]` at the bottommost
first-column defect when `r b a`, swapping the two permutation labels.
`move_involution`, `move_signedArray`, and `move_tableauGraphInversions`
prove involutivity, preservation of the actual shape/filling/row conditions,
and preservation of the existing tableau inversion statistic.
`signedArray_fixed_iff_padded` characterizes fixed arrays as actual
`CornerSlide.Tableau` bodies followed by empty rows; `fixed_labels_identity`
and `fixed_row_lengths` give their identity labels and entire shape profile.
`move_sign_reversing` uses inversion parity of the actual label permutation,
and `fixed_permutationSign` gives sign one on the fixed sector.

The [exact handoff](../evidence/h3-signed-array-handoff.md) and
[separate two-round semantic review](../evidence/h3-signed-array-review.md)
record hypotheses and checked declarations. This is a universal list-based
involution, not yet a finite signed-sum identity. Complete finite sector
enumeration, canonical padding removal into `CornerSlide.family`, and the
alternant permutation-sign interface remain integration obligations.

## Boundary of the certificate

This Std-only project does **not** define chromatic quasisymmetric functions,
Schur or elementary bases, dual Jacobi–Trudi determinants, the imported
Shareshian–Wachs expansion, or the final elementary coefficient formula. It
does not prove the finite count difference `5 > 4` or the infinite hook-count
obstruction. Those parts have written arguments and separate Python checks.
The separate [Mathlib bridge](../mathlib/README.md) now defines actual coloring,
elementary and tableau-weight polynomials and checks generic alternant
multiplication and Vandermonde cancellation. The final height-two positivity
theorem is still not an end-to-end Lean theorem.

[AlternantSubsets.lean](AlternantSubsets.lean) is the fifth Std module.
`noRise_iff_prefix`, `adjacent_exponent_collision` and
`two_block_classification` classify Boolean lists that can avoid repeated
adjacent exponents in the proposed two-elementary identity. The classification
uses integer exponents and includes empty blocks and balanced shapes. Its
seven principal reports were separately [reviewed](../evidence/h3-algebra-review-r1.md).
An actual finite-subset bijection is checked in the Mathlib project, but
the complete two-elementary polynomial specialization remains an obligation.

The checked principal statements use only `propext`, `Quot.sound`, and
`Classical.choice`. Classical choice is used by the finite-family definitions
as well as one original concrete filling proof. There is no `sorryAx`,
custom axiom declaration, `unsafe`, or `native_decide`. See the successful,
source-hash-bound [verification record](verification.json) for actual command
outputs, actual declaration types, and all 54 printed dependency lists. The
[separate semantic review](../evidence/gap-review.md) supports H1/H2 while
retaining the coloring-to-elementary gap H3.

## Reproduce

An installed Lean 4.34.0 toolchain is required. From this directory:

```sh
lake build
lake env lean CornerSlide.lean
lake env lean TableauFamilies.lean
lake env lean WeightedCancellation.lean
lake env lean SignedArrays.lean
lake env lean AlternantSubsets.lean
python3 verify.py --output verification.json
```

The last command copies the five sources and pinned configuration into a fresh
temporary directory without existing build products, builds them, and directly
checks every source. It records an inventory of the actual declaration types,
checks that all
printed axiom lists use the allowed standard foundations, scans the source for
proof placeholders and custom axioms, and records the source/configuration
and verifier hashes. It rejects diagnostics, missing required reports, or source
changes during verification, and writes the report only after success. The
temporary build is removed; the installed Lean/Std toolchain is reused.
