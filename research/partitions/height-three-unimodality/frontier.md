# Height-three coefficient unimodality: frontier and exact signed space

Inspected 2026-10-23. This is the separate critic's literature audit and
written algebraic derivation, prepared before either construction review.
It records no new universal positivity or unimodality proof, no new Lean
certificate, and no independently rebuilt external certificate.

## 1. Selected unresolved-theorem target

Let `h : [n] -> [n]` be weakly increasing with `i <= h(i) <= n`. Write
`u <_P v` when `h(u) < v`, and let `G=inc(P)` have edges
`{u,v}` with `u<v<=h(u)`. Assume the longest strict chain of `P` has
**exactly three elements**, and `n>=7`. Use the actual Shareshian--Wachs
proper-coloring function, weighted by its edge-ascent statistic, and set

\[
 \lambda_n=(n-4,3,1),\qquad
 c_{\lambda_n}(q)=[e_{\lambda_n}]X_G(\mathbf x;q),\qquad M=|E(G)|.
\]

**Conjecture / selected target:** writing `c_d=[q^d]c_lambda(q)` and
`c_{-1}=0`, prove

\[
 c_d-c_{d-1}\ge0\qquad(0\le d\le\lfloor M/2\rfloor).
\]

Together with established reciprocity `c_d=c_{M-d}`, this proves unimodality
with center `M/2`, including the identically zero coefficient. Reciprocity
does not imply these inequalities. The `d=0` inequality is retained in the
contract. Degrees outside `0,...,M` are zero.

**Novelty status: unverified.** No proof of this whole family was found in
the inspected literature through 2026-10-23. This bounded audit cannot certify
the nonexistence of other prior work. Success must resolve these inequalities;
a new cancellation proof of already reported coefficient positivity alone
does not satisfy the user's accepted objective. A proof confined to an
already covered graph subclass would need a new, separately checked claim.

There is no new formalization target yet. The existing end-to-end declarations
`PartitionH3.height_two_survivor_expansion` and
`PartitionH3.height_two_survivor_expansion_nat` formalize the established
Cho--Huh height-two result. Their hypotheses do not cover the present target.
The [claim-to-theorem index](../evidence/claim-to-theorem-index.md) preserves
their exact certificate boundary, and distinguishes the written universal
two-sector cardinality obstruction from finite computations and Lean results.
Earlier failed corner slides and that obstruction remain evidence.

## 2. Primary-source frontier and inspection limits

| Source | What was inspected and what follows | Consequence here |
| --- | --- | --- |
| [Cho--Huh](https://arxiv.org/html/1711.07152v2), Sections 3--4 | Statements, insertion route and unimodality distinctions; established height-two positivity and additional special families, with unimodality for specified families. Not a full independent proof audit of the paper. | Height-two insertion and its known inverse cannot be advertised as new, nor extended to height three without checking the inverse. |
| [Wang v3, 2026-09-25](https://arxiv.org/html/2210.07567v3), Propositions 3.5/3.7, Theorems 3.9/3.10 and Section 5 | Current primary version inspected. It corrects the coefficient formula to include an extra multiplicity term after sorting. It gives inversion-preserving positivity constructions for last-part gap at most one and further graph families. | Our last-part gap is two. This source does not establish the selected unimodality theorem. The older v2 expansion is insufficient for completeness. |
| [Tom](https://arxiv.org/html/2311.08020v2), Definitions 3.1/3.3, Theorem 3.4, Corollaries 4.18/4.20, Problems 5.1/5.2 | Complete forest-triple signed expansion inspected; cancellation and unimodality for almost-`K`-chains, with broader construction problems. Published [2025 record](https://repositories.cdlib.org/uc/item/9dc0v7wb) also inspected. | Forest triples are an established alternative signed model. Reusing the expansion alone is not a contribution; the full height-three family exceeds those special-case conclusions. |
| [Sagan--Tom author manuscript](https://users.math.msu.edu/users/bsagan/Papers/Old/csfcb.pdf), introduction and final discussion; [2026 journal record](https://alco.centre-mersenne.org/articles/10.5802/alco.468/) | Coefficient restrictions, top-coefficient route and final unimodality/log-concavity discussion inspected. Direct journal PDF retrieval was blocked; complete identity with the inspected author manuscript was not checked. | No inspected theorem supplies this family's unimodality. Do not confuse the number of parts with the largest part in their coefficient results. |
| [Hikita v2](https://arxiv.org/html/2410.12758v2), main statement and introduction; [the `(q,t)` paper](https://arxiv.org/html/2503.23597v1) | The first gives numerical nonnegativity for real positive `q`, including ordinary positivity at `q=1`; this differs from coefficientwise positivity. The second's overview was inspected, not its full proof. | Neither inspected statement establishes the proposed elementary unimodality inequalities. |
| [OpenAI 2026-09-24, pinned introduction](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Elementary-Positivity-of-Chromatic-Quasisymmetric-Functions-September-24-2026/build/sections/01-introduction.tex) and [completion](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Elementary-Positivity-of-Chromatic-Quasisymmetric-Functions-September-24-2026/build/sections/07-completion.tex) | Theorem 1.1, its explicit scope sentence, proof overview and completion inspected in primary TeX. The theorem claims general coefficientwise positivity and expressly makes no assertion of elementary unimodality. | Positivity is **reported proved**, not a defensible unresolved-theorem target here. The separate unimodality target is not subsumed by that theorem. |
| [Kafidov 2026-07-22](https://arxiv.org/html/2607.20595v1), Theorem 2.1 and exact displayed coefficient | Reports a 13-vertex failure of elementary log-concavity; the coefficient remains positive, palindromic and unimodal. Verifier not rerun here. | Universal elementary log-concavity is not a safe replacement target. This does not refute unimodality or the selected family. |

The repository's [external-certificate audit](../evidence/external-certificate-audit.md)
remains a partial source audit, not a completed independent rebuild. The pinned
[`Main.lean`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/Combinatorics/Chromatic/Main.lean)
uses `G.historyWitness` both to obtain a passing finite table and in the final
expansion transfer. Inspecting that table alone does not establish positivity;
the decorated-history, Laurent and wall chain remains substantive audit work.
No circularity has been established. This phase does not rebuild that project.

Even combining elementary positivity, reciprocity and Schur unimodality would
not settle the present target: as a symmetric-function identity,

\[
 (1+q^2)e_3+q e_{21}
 =(1+q+q^2)s_{111}+q s_{21}.
\]

The right-hand Schur coefficients are unimodal with center one; the `e_3`
coefficient is not. This is a written counterexample to that implication,
not a chromatic-function counterexample.

## 3. Height, tableaux and complete determinant sectors

### Height equals bounce number in these conventions

**Written proof; not a new Lean certificate.** Set `b_0=0` and, while
`b_i<n`, define `b_{i+1}=h(b_i+1)`. These are the successive diagonal
contacts of the usual bounce path. They strictly increase, so let `r` be
the first index with `b_r=n`. Each interval
`I_i={b_{i-1}+1,...,b_i}` is an antichain: for `x<y` in it,
`h(x)>=h(b_{i-1}+1)=b_i>=y`. Thus any strict chain has at most `r`
elements. Conversely `a_i=b_{i-1}+1`, for `1<=i<=r`, gives a chain since
`h(a_i)=b_i<a_{i+1}`. Hence height equals `r`, including disconnected
graphs and boundary Hessenberg vectors. The selected height-three family
therefore has bounce number three, rather than merely height bounded by it.

### Raw signed objects

Use the established weighted `P`-tableau Schur expansion. A tableau is a
bijective filling by `[n]` of partition shape `mu`, with rows strictly
increasing in `P` and with no lower column entry below its immediate upper
entry in `P`. Put

\[
 B_\mu(q)=\sum_{T\in\operatorname{PT}_\mu(P)}q^{\operatorname{inv}_G(T)},
\]

where the statistic counts an edge whose larger label is in an earlier row.
Rows are chains and therefore contain no graph edges; consequently this is
also the graph-inversion statistic of the row-major word. Height three
implies `mu_1<=3`.

For each shape retain **every** determinant permutation `sigma` and put

\[
 \alpha_i=\mu'_i-i+\sigma(i),\qquad
 s_\mu=\sum_\sigma\operatorname{sgn}(\sigma)\prod_i e_{\alpha_i}.
\]

The conventions are `e_0=1` and `e_a=0` for `a<0`. A term contributes to
`e_lambda` exactly when every index is nonnegative and sorting its positive
indices gives `lambda`. Keep separate raw objects `(mu,sigma,T)` even if
they yield the same elementary monomial. This records multiplicities without
silently changing the signed space.

For this length-three target, determinants of size below three cannot
contribute; a size-three contributing determinant cannot contain a zero
index because that leaves fewer than three positive factors. This is a
deduced absence of zero factors for this target, not a convention discarding
them from the general determinant expansion. All noncontributing shapes and
permutations must have this explicit filter available to the implementation.

### Written six-permutation derivation and the exceptional boundary

Write `nu=mu'=(a,b,c)`, with `a>=b>=c>=1`. The complete `3 x 3`
determinant has these terms; permutation notation gives its three images.

| `sigma` | Sign | Ordered elementary indices |
| --- | --- | --- |
| `123` | `+` | `(a,b,c)` |
| `312` | `+` | `(a+2,b-1,c-1)` |
| `231` | `+` | `(a+1,b+1,c-2)` |
| `132` | `-` | `(a,b+1,c-1)` |
| `213` | `-` | `(a+1,b-1,c)` |
| `321` | `-` | `(a+2,b,c-2)` |

Let `L=n-4>=3`. Solving for the sorted indices `(L,3,1)` gives:

| Sign | Tableau shape `mu` | Determinant tag | Existence as a partition |
| --- | --- | --- | --- |
| `+` | `3 2^2 1^(n-7)` | `123` | `n>=7` |
| `+` | `3^2 2^2 1^(n-10)` | `312` | `n>=10` |
| `-` | `3^2 1^(n-6)` | `132` | `n>=7` |
| `-` | `3 2^3 1^(n-9)` | `213` | `n>=9` |
| `-` | `3^3 1^(n-9)` | `321` | `n>=9` |
| `-` | `3^2 2` | `132` | **only `n=8`** |

Here `231` has no solution: its already ordered indices would force
`b=2,c=3`. For `132`, the indices are already ordered unless `a=b`.
In the latter case their sorted form is `(a+1,a,c-1)`, which forces
`(a,b,c)=(3,3,2)` and `n=8`. For `213`, the only order reversal is
`b=c`; its last two sorted indices then differ by one, whereas this target's
last two parts differ by two, so it contributes no further case. The other
four displayed triples are weakly decreasing already. Equal target parts at
`n=7` do not create multiple copies of an identical ordered determinant term.
These observations exhaust all six determinant permutations without assuming
a two-sector restriction.

Thus the exact coefficient is

\[
\begin{aligned}
 c_{\lambda_n}(q)={}&B_{3\,2^2\,1^{n-7}}
 +B_{3^2\,2^2\,1^{n-10}}
 -B_{3^2\,1^{n-6}}\\
 &-B_{3\,2^3\,1^{n-9}}
 -B_{3^3\,1^{n-9}}
 -\mathbf1_{n=8}B_{3^2\,2},
\end{aligned}
\]

with impossible shapes omitted. This is a **written algebraic proof** of the
sector identity using the imported Schur expansion and dual Jacobi--Trudi
identity; it is not a Lean certificate or a positivity argument. Some valid
shape sectors can still have empty tableau families for a particular `h`.
The `n=7,8,9,10` boundaries respectively admit two, three, four and five
raw shape/permutation sectors. Those numbers are analytic support counts,
not counts of tableaux or a report of an executed search.

## 4. Complete signed first differences and construction obligations

For every raw contributing object add `epsilon in {0,1}`. Its sign and
effective degree are

\[
 \operatorname{sign}(\mu,\sigma,T,\epsilon)
 =\operatorname{sgn}(\sigma)(-1)^\epsilon,
 \qquad D=\operatorname{inv}_G(T)+\epsilon.
\]

**Written identity:** summing these objects gives

\[
 \sum_{\mu,\sigma,T,\epsilon}
  \operatorname{sgn}(\sigma)(-1)^\epsilon q^D
 =(1-q)c_{\lambda_n}(q).
\]

Its degree-`d` signed count is exactly `c_d-c_{d-1}`. The construction
domain is restricted to `D<=floor(M/2)`. The full doubled space generally
has negative upper-half differences, so a positive-survivor involution on
that full space is not the claim. Degree-preserving moves cannot cross the
restriction boundary.

For the accepted small grammar, same-word reblocking and inversion-preserving
Cho--Huh suffix operations must leave `epsilon` unchanged and reverse the
determinant sign. An adjacent incomparable swap changes graph inversions by
exactly one; equal effective degree forces an `epsilon` toggle and opposite
total signs then require equal determinant signs. Each operation still needs
actual tableau validity, a contributing determinant tag and exact inverse
recovery. Choosing a first or last legal move does not itself make a selector
involutive. Collisions, unmatched negatives and selector-recovery failures
must be recorded separately.

A finite failure of every chosen selector refutes those selectors, not the
whole grammar. A complete grammar-constrained graph may instead admit an
isolated negative state or a finite Hall deficiency; such a verified witness
would certify a local-grammar obstruction. An unrestricted degreewise
matching would merely restate the desired coefficient inequality.

Tom's forest triples provide the comparison route if the tableau grammar
meets an obstruction. A forest triple has decreasing tree components, each
with a composition `alpha` of its size and `1<=r<=alpha_1`; components are
ordered by minima. Its type sorts the compositions, its sign is
`(-1)^(number of parts - number of trees)`, and its weight is the graph
inversion of the concatenated canonical tree words plus `sum(r-1)`.
Restricting to type `lambda_n` and applying the same `epsilon` doubling
therefore gives the same first-difference target. A forest move must account
for both parts of this weight, not just the word inversions.

The next decisive experiment is the bounded, frozen-selector check on the
complete doubled space, including the exceptional `n=8` boundary. Development
examples and held-out structural cases must remain separate. This audit
provides no search results. A credible universal argument, exact theorem
statement, placeholder-free Lean checking without custom axioms and separate
semantic review remain necessary before final theorem acceptance.
