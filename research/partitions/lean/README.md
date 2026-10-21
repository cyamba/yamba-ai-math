# Lean certificate for the tableau correction

Checked on 21 October 2026 with Lean 4.34.0 and its bundled `Std` library.
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

The file also proves the general extraction theorem under its weaker explicit
separation condition, arbitrary-score adjacent-swap lemmas, filling preservation,
and the simple bottom-row corollary. The source prints axiom dependencies for
the principal statements.

## Boundary of the certificate

The Lean development does **not** define chromatic quasisymmetric functions,
Schur or elementary bases, dual Jacobi–Trudi determinants, the imported
Shareshian–Wachs expansion, or the final elementary coefficient formula. It
does not prove the finite count difference `5 > 4` or the infinite hook-count
obstruction. Those parts have written arguments and separate Python checks.
The final height-two positivity theorem is therefore not claimed as an
end-to-end Lean theorem.

The checked principal statements use only `propext`, `Quot.sound`, and, for
one concrete source-filling proof, `Classical.choice`. There is no `sorryAx`,
custom axiom declaration, `unsafe`, or `native_decide`. See the successful,
source-hash-bound [verification record](verification.json) for actual command
outputs and every printed dependency list.

## Reproduce

An installed Lean 4.34.0 toolchain is required. From this directory:

```sh
lake build
lake env lean CornerSlide.lean
python3 verify.py --output verification.json
```

The last command repeats the build and direct source check, checks that all
printed axiom lists use the allowed standard foundations, scans the source for
proof placeholders and custom axioms, and records the source/configuration
hashes. It writes the report only after successful checks. Build products stay
in ignored `.lake/`; the small verification record is intentional review evidence.
