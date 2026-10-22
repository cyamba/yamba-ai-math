# Article claims and exact certificate boundaries

Updated 2026-10-22. This index covers every named theorem in
[the article](../paper/main.tex). Declaration names below are fully qualified;
their actual printed types, standard axiom dependencies, and source hashes
are in the fresh [Std record](../lean/verification.json) and
[polynomial record](../mathlib/verification.json).
Compilation certifies these declarations, not every informal consequence or
translation in the article. There is no final Lean declaration for H3.

| Article label and claim | Exact Lean declarations | Material hypotheses and remaining scope | Attribution and semantic verdict | Verification record |
| --- | --- | --- | --- | --- |
| `thm:boundary`: exact boundary criterion | `CornerSlide.demote_valid_iff`; `CornerSlide.flatten_before_after`; `CornerSlide.tableau_graph_inversions_eq_word` | Actual valid source and asymmetric relation. The article's weight conclusion composes unchanged word with row/word equivalence for the valid source and target; no dedicated single theorem packages that composition. | Local argument supported in [original review](reviewer.md); no novelty claim. | Fresh `CornerSlide.lean` check, types and dependency reports in `verification.json`. |
| `thm:count`: no unrestricted two-sector injection | **None** | Total order, every `n >= 5`. Written counting proof; finite enumeration is supporting evidence only. | Written argument supported in [original review](reviewer.md). | [Exact audit](exact-audit.json) and article proof; no Lean certificate for the universal count. |
| `thm:bubblevalid`: validity and weight | `CornerSlide.bubble_tableau_valid`; `CornerSlide.bubble_tableau_graph_inversions`; family instance `CornerSlide.bubbleAt_family` and `CornerSlide.bubbleAt_family_weight` | Asymmetric relation and actual source tableau. Height two is not required. Fixed source shape determines the family split. | Cho–Huh's established injection, Section 3.1, reproduced and attributed; [original review](reviewer.md) and [family review](gap-review.md) support this scope. | Fresh `CornerSlide.lean` and `TableauFamilies.lean` checks in `verification.json`. |
| `thm:injection`: height-two injection | `CornerSlide.extract_bubble_inverse_height_two`; `CornerSlide.bubble_tableau_injective`; `CornerSlide.bubbleAt_family_injective` | `NoThreeChain`, actual source tableaux and equal split indices. The complete fixed source shape supplies the index equality. | Cho–Huh construction; [original review](reviewer.md) and [family review](gap-review.md): supported. | Fresh source checks, printed types and axiom reports in `verification.json`. |
| `thm:positive`: height-two elementary positivity and survivor formula | **No end-to-end declaration**; combinatorial ingredient `CornerSlide.height_two_degreewise_cancellation` | Natural unit interval poset of height at most two. Written proof imports the Shareshian–Wachs expansion and the symmetric-function basis change. Actual coloring equality for every finite alphabet remains H3. | Established Cho–Huh result reproduced; written argument supported subject to stated imports in [original review](reviewer.md). | Written proof and [bounded independent coloring comparison](comparison.json); no final Lean certificate. |
| `thm:formalsigned`: signed-array involution | `SignedArrays.move_involution`; `SignedArrays.move_signedArray`; `SignedArrays.move_tableauGraphInversions`; `SignedArrays.signedArray_fixed_iff_padded`; `SignedArrays.fixed_labels_identity`; `SignedArrays.fixed_row_lengths`; `SignedArrays.move_sign_reversing`; `SignedArrays.fixed_permutationSign` | Actual permutation labels, integer shape equations and bijective chain filling. Fixed-sector conclusions require explicit partitionhood and height two. Sign reversal uses distinct actual labels and a moved array. No finite signed-sum or canonical family bijection is asserted. | Local cancellation route follows the accepted Shareshian–Wachs proof route; no novelty claim. [Separate two-round source review](h3-signed-array-review.md): supported for the exact declarations. | Fresh `SignedArrays.lean` check and 16 added principal reports in `verification.json`; [author handoff](h3-signed-array-handoff.md). |
| `thm:formalcounts`: degreewise survivor identity | `CornerSlide.height_two_degreewise_cancellation`; `CornerSlide.finite_height_two_degreewise_cancellation`; `CornerSlide.empty_vertex_degree_count`; `CornerSlide.single_vertex_degree_count`; `CornerSlide.survivorFamily_empty_source` | Distinct finite vertices, asymmetry and height at most two; the finite-relation version requires those conditions only on the vertex set. Every index and degree; exact full-image complement. | Formalization of the combinatorial part of the known construction; [family review](gap-review.md): supported for H1/H2. | Fresh `WeightedCancellation.lean` check, printed types and dependency reports in `verification.json`. |
| `thm:formalalternant`: generic alternant multiplication, vanishing and valid cancellation | `PartitionH3.alternant_eq_sum`; `PartitionH3.alternant_mul_elementary`; `PartitionH3.alternant_eq_zero_of_eq`; `PartitionH3.vandermonde_delta_coefficient`; `PartitionH3.vandermonde_ne_zero`; `PartitionH3.vandermonde_cancel`; `PartitionH3.vandermonde_empty` | Actual `MvPolynomial (Fin m) (Polynomial Int)`. Generic identity has no bound on `b`; vanishing requires distinct equal-exponent positions. Nonzero/cancellation include `m=0`. No coloring expansion is a premise. | Standard finite alternant algebra along the Shareshian–Wachs route; no novelty claim. [Second algebra review](h3-algebra-review-r2.md): supported for these exact declarations. | Fresh `Alternant.lean` / `Vandermonde.lean` checks and printed signatures/dependencies in the [polynomial record](../mathlib/verification.json). |

The coloring subsection uses `PartitionH3.same_color_comparable`,
`PartitionH3.colorClass_card_le_two`, `PartitionH3.reverseColors_involutive`,
`PartitionH3.proper_reverseColors_iff`, `PartitionH3.ascents_reverseColors`,
`PartitionH3.descents_reverseColors` and
`PartitionH3.descents_eq_colorRowInversions`. The class bound assumes actual
properness and height two. The last equality is with the defined finite-pair
statistic, not the original list-array statistic. Increasing color rows
correspond to descents. The [second review](h3-algebra-review-r2.md) records
the correction and its two-vertex counterexample; the regression remains in
the tests.

The displayed two-elementary specialization is explicitly a written target,
not a checked theorem. Its Boolean classification is
`AlternantSubsets.two_block_classification`; actual subset transfer is
`PartitionH3.twoBlockSubset_classification`, with `b <= a`, `a+b <= m`,
actual cardinality and two-block no-rise hypotheses. See the two algebra
reviews for their exact supported scope. The worked three-vertex example
uses the independent coloring oracle and tableau enumeration; it is neither
a new theorem nor a substitute for H3.

## Open obligations that must not be hidden by the index

The universal signed-array map and generic finite alternant identity are
checked, as are Vandermonde nonzero/cancellation and color reversal/finite-pair
orientation. Still absent are the two-elementary specialization, dominant
coefficient reconstruction, adjacent-color symmetry, actual coloring/list
array bijections, complete finite signed-sector cancellation, canonical
padding/family bijections, the list/library permutation-sign interface,
inverse-permutation coloring coefficient reindexing, the H2 polynomial lift
and specialization to all alphabets (including zero). These are tracked by the
[H3 contracts](../h3-bridge-plan.md). Neither matching finite computations nor
the existing list-based involution supplies these absent polynomial results.

The 2026-10-22 lead checks built five Std modules and the separate five-module
Mathlib bridge freshly, checking 54 and 28 principal standard-axiom reports
respectively. The article compiled in its existing built-in editor after the
finite alternant section, coloring diagram and worked example were added.
`verify_all.py` produces a separate source-bound repository/checker/two-
certificate receipt under ignored `.runs/partition-verification/`; a missing
dependency or failed stage cannot produce success. These are different
assurance checks; none closes H3 or certifies novelty. P007 has used its
16-unit/two-review boundary; P009 remains unstarted with incomplete inputs.
