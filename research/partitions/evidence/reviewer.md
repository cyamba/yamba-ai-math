# Independent review of the proposed corner slide

Initial review: 2026-10-20. Final mathematical review: 2026-10-21. Role: separate critic and literature reviewer. The reviewer used the same underlying model family as the coordinator; separate role identity does not establish statistically independent errors.

**Verdict: refuted** for the PDF's unrestricted all-size corner-slide claim. **Supported by an elementary argument** for the restricted local repair below. This document does not certify a solution of the general elementary-positivity or coefficient-interpretation problem.

## Exact statement and counterexample

Use English tableaux: rows are strict chains in a poset P, and an entry immediately below another may not be smaller in P. Every element occurs exactly once. The supplied PDF proposes splitting the final two-cell row (a,b) of a tableau of shape (2^(k+1),1^m) into successive singleton rows a and b. This would produce shape (2^k,1^(m+2)).

The first missing condition appears at n=5, k=1, m=1. For h=(3,4,4,5,5), with i <_P j iff h(i)<j, the tableau

```text
1 4
2 5
3
```

is valid, but its proposed demotion

```text
1 4
2
5
3
```

is invalid because 3 <_P 5. The incomparability graph has edges 12,13,23,24,34,45 and is connected. The poset has no three-element chain. Thus adding connectedness or poset height at most two does not repair the slide. The source tableau has graph-inversion degree 2. This is a counterexample to tableau validity, not to elementary positivity.

There is also an obstruction to *any* injection between these two shapes for unrestricted natural unit interval orders. For the total order h=(1,2,3,4,5), all graph-inversion degrees are zero. Shape (2,1,1,1) has four tableaux; shape (2,2,1) has five. The five negative-shape tableaux have row-major words 12345,12354,13245,13254,14253. Therefore no injection from the entire negative shape to the proposed positive shape exists. Wider signed determinant sectors cannot generally be discarded.

## Complete local repair

Let P be any finite poset and let T be a valid tableau of shape (2^(k+1),1^m). Write its final two-cell row as (a,b), followed by singleton entries c_1,...,c_m. Splitting (a,b) into singleton rows is valid **if and only if**

> m=0, or c_1 is not smaller than b in P.

Proof: the only new column comparisons are a above b and, when m>0, b above c_1. Since a <_P b, asymmetry gives that b is not smaller than a. The second comparison is exactly the displayed condition. All other row and column conditions are inherited. This proves necessity and sufficiency, not merely a sufficient condition.

The map is injective: recover T by joining those two specified singleton rows. Its image consists exactly of positive-shape tableaux for which a <_P b and, if k>0, b is not smaller than the existing second-column entry immediately above its old position. To verify the inverse, the only possibly missing first-column comparison is a above c_1. If c_1 <_P a, then transitivity and a <_P b give c_1 <_P b, contradicting validity of the positive tableau. This completes the inverse argument.

The row-major word is identical before and after splitting. In a tableau with chain rows, two entries from one row are never adjacent in the incomparability graph. Consequently the usual tableau inversion statistic, which counts an edge whose smaller endpoint is in a lower row, equals the graph-inversion statistic of its row-major word. The restricted injection therefore preserves the exact q-grading.

This provides a cancellation on precisely the admissible negative tableaux. It leaves inadmissible negative tableaux unresolved and does not yield positivity of a full elementary coefficient. No novelty claim is made for this local lemma.

## Formalization audit of the supplied PDF

The `ParametricDJTBoundary` structure printed on PDF pages 25–26 stores a word, two boundary entries, and a Boolean flag. Its positive validity predicate omits the comparison with the first following suffix entry. It also does not establish an equivalence with actual bijectively filled tableaux or with the full signed dual Jacobi–Trudi configurations. A theorem about toggling this flag, even if compiled, therefore does not prove the advertised general tableau theorem. The supplied finite C_09 enumeration likewise requires a separately verified link to actual tableaux and their complete enumeration.

## Stronger repair under the height-two hypothesis

**Verdict: supported; known mathematics reproduced.** Assume P has no three-element chain. Move b past the maximal initial portion of the old singleton suffix consisting of entries z <_P b; insert b just before the first remaining entry, or at the end. The resulting tableau is valid. Its new preceding entry is smaller than b, and its new following entry is not smaller than b. Every crossed pair is comparable and hence a nonedge, so the graph-inversion statistic is preserved.

The moved b is recoverable as the first entry after a which is larger than a in P. No crossed z can satisfy a <_P z, since a <_P z <_P b would be a three-element chain. This proves injectivity. This argument repairs the connected counterexample above by placing 5 below 3.

The hypothesis matters for injectivity. In the total order on five vertices, both `((1,2),(3,4),(5,))` and `((1,2),(3,5),(4,))` map to `((1,2),(3,),(4,),(5,))`. Thus the repair may always produce valid tableaux while failing to cancel them injectively outside height two. The q-refined chromatic corollary also needs the natural unit interval hypothesis for its imported symmetric Schur expansion; the local map alone does not establish symmetry for arbitrary labeled height-two posets.

An independently written exhaustive checker tested every height-at-most-two Hessenberg order for n=2,...,7: 126 orders and 33,474 source tableaux in total. It checked tableau validity, inversion preservation, absence of collisions, and the stated inverse recovery. Source-tableau counts by n were 1, 5, 36, 282, 2,730, and 30,420. These are finite checks of the construction, not a substitute for its universal proof.

Crucially, the construction is the injection psi_ell already given by Cho–Huh in Section 3.1, with the elementary-coefficient interpretation in Theorem 3.3 of [their primary preprint](https://arxiv.org/pdf/1711.07152). The map and its proof, not just the positivity statement, were inspected. This is a reproduction and formalization target for an existing theorem, not a newly solved open problem.

## Primary-source status check

- Hikita, *A proof of the Stanley–Stembridge conjecture*, v2 (2025-12-25): [primary paper](https://arxiv.org/html/2410.12758v2). Introduction and Section 1.3 inspected. It proves ordinary elementary positivity using nonnegativity for positive real q; Section 1.3 explicitly distinguishes coefficientwise q-positivity. The full proof was not independently audited here.
- Shareshian–Wachs, *Chromatic quasisymmetric functions*: [primary accepted manuscript](https://www.sciencedirect.com/science/article/am/pii/S0001870816000025). Definition 6.1, tableau inversion convention, and Theorem 6.3 inspected. Rows are chains; tableau inversions count the smaller endpoint below the larger endpoint. This supports the convention used above.
- Sagan–Tom, *Chromatic symmetric functions and change of basis* (2026): [primary paper](https://alco.centre-mersenne.org/item/10.5802/alco.468.pdf). Introduction, Theorem 3.14, and Theorem 3.15 inspected. In particular, elementary top-coefficient formulas and three-column coefficient positivity already have substantive prior literature. No full proof audit was performed.
- Siegl, *Toward Lower Bounds for Chromatic Symmetric Functions in the Elementary Basis*, v3 (2026-07-31): [primary paper](https://arxiv.org/pdf/2509.02841). Introduction and theorem/conjecture statements inspected. It records the then-open q-refinement and explicit combinatorial lower-bound targets. Its appendix refutes a proposed powerful-tableau upper bound; that failed conjecture must not be reused as an assumption.
- OpenAI, *Elementary positivity of chromatic quasisymmetric functions* (2026-09-24): [primary preprint](https://github.com/openai/math/blob/main/preprints/Elementary-Positivity-of-Chromatic-Quasisymmetric-Functions-September-24-2026/paper.pdf), [primary metadata](https://raw.githubusercontent.com/openai/math/main/preprints/Elementary-Positivity-of-Chromatic-Quasisymmetric-Functions-September-24-2026/README.md). Theorem 1.1 explicitly claims the full coefficientwise q-positivity result and a terminating permutation witness. Local source sections 1, 5, 6, and 7 were partially inspected. The exact-mask alternating-path argument and the final deduction from the positive-section hypotheses show no identified defect in this partial inspection. The positive-reordering and wall-section foundations were not fully checked. Record this as a **claimed result with partial proof inspection**, not as an independently certified theorem or as a formal Lean proof. The July 2026 paper alone cannot establish that q-positivity remains open as of this review.

**Novelty status: NOT VERIFIED.** The proof repair concerns the specific supplied slide, and the general problem remains outside what this review proves.

## Final article and implementation review, 2026-10-21

The reviewer read the full article source, the current Python tableau and verification modules, the saved comparison report, and the expanded Lean development. **Verdict: supported** for the article's mathematical statements, subject to its stated imported Shareshian–Wachs theorem and the formal-verification boundary below. No substantive mathematical defect was identified in the final construction.

- The infinite cardinality obstruction is valid. For the total order, transposing tableaux gives counts `n-1` and `binom(n-1,2)-1 = n(n-3)/2`. The pair `{2,3}` is the unique forbidden second-row choice in shape `(n-2,2)`. The count difference is positive at five and increases by `n-2` on passing from n to n+1.
- The complete five-vertex dual Jacobi–Trudi identity includes all six displayed sectors. In the total order it evaluates to `4-5-6+5+4-2=0`. Discarding the wider shapes would give a false negative coefficient.
- The comparable-prefix map preserves actual tableaux for every poset. Under the no-three-chain assumption, first-eligible extraction is a left inverse on its image. Because k and the target shape fix the front and distinguished singleton a, this is an injection of the whole stated source family, not merely an injection with fixed a.
- The full height-two coefficient argument is complete as ordinary mathematics. Only shapes with rows of length at most two remain; their two-column determinants give the coefficient difference `F_k-F_(k+1)`. The injection preserves each degree, so the complement of its image gives precisely the coefficient enumerator. The even balanced case has empty next source, with no additional determinant factor. This reproduces the known Cho–Huh result.
- The article makes no unsupported claim that every positive tableau has an eligible extraction. The inverse is claimed on the image. The Python `recover` function correctly verifies source validity and reinsertion before accepting an extracted candidate. This is also a useful executable membership test for that image.
- The code's row-based graph inversion agrees with the article's English-tableau convention. The saved independent proper-coloring comparison covers all 65 Hessenberg vectors for sizes zero through five. The saved bubble report covers the same 33,474 source tableaux and 126 height-two orders as the independent checker described above, with no recorded failures. The finite range remains explicit and is not promoted to a universal proof.
- The final 526-line Lean source was re-read after its formalization was extended. Its predicates use actual bijective tableau fillings. `demote_valid_iff` establishes the general suffix boundary equivalence; `bubble_tableau_valid` establishes actual target validity under asymmetry. `extract_bubble_inverse_height_two` supplies a first-eligible left inverse. `bubble_tableau_injective` recovers the entire front, distinguished pair, and suffix from equal output tableaux whose split rows have the same index, under `NoThreeChain`; fixed source shape supplies that index assumption. `graphScore` contributes one exactly when an earlier label exceeds a later incomparable label. `tableauGraphInversions` sums these contributions across distinct rows. `chain_graph_weight_zero` removes all same-row contributions, and `tableau_graph_inversions_eq_word` formally equates this row-based statistic with the flattened word score for chain rows. `bubble_graph_inversions` proves preservation of the word score, and `bubble_tableau_graph_inversions` consequently proves preservation of the actual row-based tableau statistic under source validity and asymmetry. No height-two assumption is needed for validity or weight preservation; it is needed for injectivity. The cardinality theorem, imported symmetric-function expansion, and final elementary-coefficient theorem remain outside Lean. The reviewer found no semantic gap in these final declarations but did not personally perform the final rebuild; the coordinator/formalizer's hash-bound build evidence records that execution.
- The source-status language is appropriately limited: ordinary Hikita positivity is established background; the September 2026 preprint is recorded as a claimed result with only partial local proof inspection. The article and project do not claim a new solution to either general conjecture.

Two minor editorial issues were returned to the coordinator and their corrections were re-read: out-of-range tableau families are now explicitly empty wherever the final survivor formula refers to the next index, and the weight proof distinguishes b's changed row relation with a from its movement past the singleton prefix in the row-major word. The article date now matches the final review date. No outstanding mathematical or editorial finding from this review remains.
