# P015 second and final review: a base-case pivot and a part-word obstruction

Date: 2026-10-24. Reviewer: distinct `critic` role implemented by
`frontier_critic`. This is the second and final P015 critic call. The filled
`r2--challenge` handoff, frozen original specifications, first review,
recorded adaptation, actual research receipts, both source snapshots and
new evidence were read. This reviewer ran no research enumeration, tests
or Lean, used no nested agents, proposed no additional move or repair,
and edited only this review. File hashes and saved JSON were inspected
without importing or executing the research implementation.

**Verdict: supported written degree-zero construction and finite
part-word obstruction; refuted four frozen selectors and a wholly
part-word-preserving universal positive-degree cancellation; target theorem
incomplete.** The two written proofs contain no material mathematical
error. Their assurance is written argument with separate semantic review,
supported by exact finite computation where indicated; neither is Lean.
The negative result concerns cancellation that preserves both degree and
the complete ordered part word. It does not refute the larger P015 grammar
or elementary unimodality.

For reference, the unresolved target is, for every height-three natural
unit interval poset on `n>=7` vertices,

`[q^d] (1-q)[e_(n-4,3,1)] X_inc(P_h)(x;q) >= 0`

for `0<=d<=floor(|E|/2)`. In Tom's complete forest space, the flattened
ordered composition word `A` has the prescribed sorted type. For a
partition with `ell` parts, doubled states have sign
`(-1)^(ell-m+epsilon)` and degree
`D=inv_G(w)+sum(r_i-1)+epsilon`. These definitions and the complete
expansion are existing mathematics from [Tom v2](https://arxiv.org/html/2311.08020v2),
Definitions 3.1/3.3, Theorem 3.4 and the tree-word/insertion lemmas,
inspected during this continuous investigation. The target and novelty
claims remain **conjectural** and **unverified**, respectively.

## 1. Supported universal degree-zero pivot, with an independent coloring bridge

**Target:** [degree-zero.md](degree-zero.md), for every natural unit interval
Hessenberg vector on `n>=1` and every partition `lambda` of `n`.
**Priority:** necessary proof gate. **Status:** proved by written argument,
not a new unresolved theorem or formal certificate.

The classification is complete. Degree zero forces every inversion and
mark offset to vanish, and epsilon to be zero. Graph components are
consecutive intervals. Their boundary cuts are exactly
`F={p<n:h(p)=p}`: monotonicity prevents any edge crossing such a cut,
whereas `h(p)>p` supplies edge `p--(p+1)`. Each graph component contains
all its consecutive edges. No forest tree crosses a graph-component cut,
and minima ordering groups its forest components before those of any later
graph component. Zero inversions on consecutive graph edges therefore
force the entire concatenated word to be `1,...,n`.

Consequently each forest component is a consecutive interval. The inverse
tree-word map makes its increasing word the unique consecutive path. A
state is thus determined exactly by its distinct ordered part word `A`
and forest cut set `K`, with `F subset K subset P(A)`, where `P(A)`
consists of the proper prefix sums. Conversely these data give an actual
state: every uncut consecutive edge exists, compositions are the
consecutive chunks of `A`, and marks and epsilon are forced. If `F` is
not contained in `P(A)`, that word has no degree-zero state. Equal parts
are not additionally labelled copies.

When `P(A)\F` is nonempty, choosing its least element and toggling it in
`K` is valid. It preserves the full word, `A`, marks and epsilon, while
changing the number of components by one and hence reversing sign. The
pivot depends only on `A,F`, which are unchanged, so its inverse chooses
the same boundary. This proves collision freedom and coverage of every
negative state without a matching search. The toggled edge is an inherited
edge split/join with the compositions concatenated in their original
order; the written pivot is not an added active experimental selector.

A fixed state has `P(A)=F` and `K=F`. It has one part and one path for
each graph component, positive sign, and `A=gamma`, the ordered list of
graph-component sizes. Exactly one such state exists when
`sort(gamma)=lambda`, and none otherwise. The example joining at `p=3`
correctly sends the two colliding composition orders to distinct one-tree
compositions, preserving the information needed for the reverse choice.

The coloring bridge is independent of the forest expansion. At `q=0`,
each consecutive graph edge forces colors to decrease strictly along its
component interval. Every chosen color set supplies exactly one such
coloring; all further edges are then descents. Components reuse colors
independently. Thus directly from proper colorings,

`X_G(x;0)=product_j e_(|C_j|)(x)`.

This confirms the survivor coefficient without assuming the desired
expansion or positivity. In the height-three target, three graph components
force each induced poset to have height one, since their ordinal sum has
height three; equivalently each graph component is a clique. That
specialization is correct and supplies only the degree-zero boundary case.

**Impact and decisive remaining obligation:** the pivot is a complete
base-case construction, while its proposed invariant `A` cannot be imposed
at every positive degree, as the next finding proves. No substantial Lean
work on the unresolved target follows from this base case alone.

## 2. Supported nine-block proof refutes preservation of the whole part word

**Target:** [partword-obstruction.md](partword-obstruction.md),
`h=(2,4,4,6,7,7,7)`, `A=(3,3,1)` and effective degree one.
**Priority:** decisive structural obstruction. **Status:** proved finite
cardinality obstruction, corroborated by two exact combinatorial
calculations; not Lean.

The graph edges are `12,23,24,34,45,46,56,57,67`, so `M=9` and
degree one is in the required lower half. The poset has height three.
Set `u=[2]_q`, `v=[3]_q`. I checked every block's sign, forced
inter-component inversion shift, tree insertion factors and first-part
mark factors:

| Component sets in minima order | Compositions | Complete signed block |
| --- | --- | --- |
| `1234567` | `(3,3,1)` | `+u^3 v` |
| `123 / 4567` | `(3) / (3,1)` | `-u^2 v^2` |
| `123456 / 7` | `(3,3) / (1)` | `-u^2 v` |
| `124567 / 3` | `(3,3) / (1)` | `-q u^2 v` |
| `123457 / 6` | `(3,3) / (1)` | `-q u v` |
| `123467 / 5` | `(3,3) / (1)` | `-q^2 u v` |
| `123 / 456 / 7` | `(3) / (3) / (1)` | `+u v^2` |
| `123 / 457 / 6` | `(3) / (3) / (1)` | `+q v^2` |
| `123 / 467 / 5` | `(3) / (3) / (1)` | `+q^2 v^2` |

Completeness follows from the composition boundaries, not from a favorable
sample. One component allows one assignment. Two components have sizes
`(3,4)` or `(6,1)`. A connected three-set containing one must be `123`
or `124`, since one has only neighbor two. The latter leaves three
isolated in the complement, so only `123/4567` works. For `(6,1)`,
singleton one violates minima order; deleting two or four disconnects the
six-set. Deleting three, five, six or seven gives precisely the four
listed possibilities. For three components the sizes must be `(3,3,1)`.
If the first triple were `124`, vertex three could neither lie in a
connected remaining triple nor be the last singleton, because its minimum
would precede that triple. Hence the first triple is `123`. Among the
remaining vertices, singleton four would precede the second triple and
give the wrong size order. Singletons five, six and seven give exactly
the final three rows. There are no further component counts or boundaries.

Summing these nine marked blocks gives

`u^3 v-u^2 v^2-(1+q)u^2 v-(q+q^2)u v+u v^2+(q+q^2)v^2`.

Using `1+q=u`, `q+q^2=qu`, the first and third summands cancel and the
`v^2` summands cancel, leaving `C_A(q)=-q u^2 v`. Thus its raw
coefficients are `0,-1,-3,-4,-3,-1` and its lower-half first differences
are `0,-1,-2,-1,1`. All bounded marks and all tree choices are included
through the factors; a zero smaller-neighbor factor would make a block
empty, rather than create another object.

Separately, the positive blocks' raw degree-zero and degree-one counts
are `2,8`; the negative blocks' absolute counts are `2,9`. Epsilon
doubling gives `8+2=10` positive and `9+2=11` negative states at
effective degree one. Consequently even unrestricted matching **within
this fixed `(A,D)` sector** cannot cover the negatives. This refutes any
degree-preserving, positive-survivor cancellation which preserves the
full ordered part word at all degrees. It is stronger than refuting one
local rule but applies to that invariant, not to all transformations.

The full coefficient is the saved coloring-checked `q^3(1+q)^3`, whose
degree-one first difference is zero. Other ordered part sectors compensate
the deficit. P015's larger grammar can change `A`, and its original
adjacent-exchange grammar already has finite saturating matchings on this
graph. Neither the full grammar nor the coefficient conjecture is refuted.
The minimality claim is confined to the first deficient `(n,h,D,A)` among
the four disclosed development vectors, not all natural unit interval
graphs, all invariants or all grammars.

**Impact and decisive remaining obligation:** a universal construction
must sometimes change the ordered composition sector, while retaining
enough information to recover the source. No recoverable universal
choice accomplishing that has been supplied. No stronger literature
novelty claim follows from this local obstruction.

## 3. Round-two adaptation and finite conclusions are accurately separated

**Target:** actual R2 execution and [repair.md](repair.md).
**Priority:** scope and selection integrity. **Status:** exact finite
evidence with a disclosed adaptive diagnostic; full universal construction
incomplete.

The recorded protocol binds the preserved R1 receipt and retains the sole
grammar repair, adjacent pairs to arbitrary pairs with identical payload,
validity, sign and full-statistic filters. The code diff adds direct
selector verification, grouping by part word and a component-set product
calculation; it changes none of the primitive generators or selectors.
The post-R1 part-word diagnostic is explicitly an added structural question
frozen before R2, not an originally preregistered outcome. Re-enumerating
the four original development spaces is a declared second-round census,
not a hidden retry or favorable replacement.

The four direct certificates reconstruct actual source, target and reverse
records from the first development vector, regenerate their complete
all-pairs neighbor groups, and verify the selected target and wrong
reverse. Reverse membership in the underlying primitive relation is
verified separately from selector nonreciprocity. All exchange groups are
empty at those degree-zero states, exactly as predicted in the first
review. These checks refute all four selectors under the permitted repair.
They do **not** compute the full arbitrary-pair graph or a repaired-graph
matching census. There is no new P015 whole-grammar Hall certificate.

The separate capacity census covers the complete lower-half doubled
signed space on all four development vectors. It verifies that summing
the part-word signed counts recovers the full first differences, then
selects the least `(D,A)` deficit in each case for a component-set product
recomputation:

| Development vector | First deficient `A,D` | Positive / negative | Compatible product blocks |
| --- | --- | --- | ---: |
| `(2,4,4,6,7,7,7)` | `(3,3,1)`, `1` | `10 / 11` | 9 |
| `(3,6,6,6,7,7,7)` | `(3,3,1)`, `2` | `48 / 49` | 31 |
| `(3,3,4,6,6,7,8,8)` | `(3,4,1)`, `1` | `10 / 11` | 7 |
| `(3,5,5,7,7,7,8,8)` | `(3,4,1)`, `2` | `55 / 56` | 23 |

Each product calculation agrees with its selected sector's entire
lower-half signed vector. It generates ordered component set partitions
and composition boundaries, not parent forests, and retains assignment
multiplicities when product terms coincide. Its cross-inversion shift and
first-part mark factors agree with Tom's block formula. This is useful
implementation diversity; the two computations still share Tom's existing
insertion theorem and are not independent derivations of that theorem.
The written nine-block exhaustion supplies an additional transparent check
of the first case.

Coloring comparisons in both rounds reuse saved P014 independent coloring
evidence, accurately labelled as reuse. R2 does not run a fresh coloring
oracle or re-enumerate the retained exceptional tableau sector. The new
degree-zero coloring argument is a written independent bridge, not a
reported coloring execution. These distinctions are correctly represented
in `evidence.json`.

**Impact and stopping condition:** no selector locks, and the fresh
held-outs `(5,5,5,5,6,7,8,9,9)` and
`(6,8,9,9,9,9,9,10,10,10)` remain unrun. Their absent outcomes do not
count as success or failure. There is no third P015 repair, research
execution or formal review. A future independently authorized phase would
need a precise universal sector-changing pivot before substantial Lean;
finite saturation or a successful base case does not satisfy that gate.

## 4. Source bindings, preservation and resource accounting supported

**Target:** receipts, snapshots and [evidence.json](evidence.json).
**Priority:** assurance boundary. **Status:** verified saved provenance and
bounded computation; no Lean checking claimed.

The repository and branch were read again: origin
`https://github.com/cyamba/yamba-ai-math.git`, branch
`codex/height-three-coefficient-unimodality`, base
`a0c897fb7bcb0d01a9ccff5593c0471424255b96`. All 174 protected hashes
agree with their current files. Every receipt source hash agrees with its
historical snapshot. All R2 source hashes agree with current sources;
R1's only subsequently changed bound files are the disclosed exchange
module and its tests, whose original bytes remain in `r1-source/`.

| Artifact | SHA-256 |
| --- | --- |
| R1 actual receipt | `e2048852a9befc4f5dbac7ff34fe410ae2fe40a433ac9434995659f8bf228690` |
| R2 actual receipt | `8038412514060aced4151f6b08e622f595ba958775276c8ff5c7efaa7d5ddf5b` |
| Executed R2 `forest_exchange.py` | `9ca5b02bf0af251be45c041b436540d35589e5b83bc53153af9b232ffdf09b13` |
| Frozen R2 specification | `009a20aa93d4f99c924227d1e2c0b3ded005cbdf23432327831b2728505a4166` |
| Recorded scope adaptation | `96a9189bf33b3720cfd0cc834a783d9cb7fb42275d1a006f0deaf6c932e64233` |
| Written degree-zero proof | `3cdb586c66b53ebe8bd726dcebb02720c408f9c92c48518448cce91c660f252a` |
| Post-execution part-word proof | `51d95b8f9ec987c2d5e9560ef793e5a805361c7a5ed43ef7df2a1f3af997261b` |
| Evidence snapshot reviewed | `0b2b63d49573d8324a11dd17988faa6fd1208fac7592d348416957bb30decf04` |

The R2 input hash is exactly the R1 receipt hash. The degree-zero proof,
repair and first review are bound into the executed R2 snapshot. The
part-word proof is explicitly a post-execution written exhaustion and is
bound by the later evidence snapshot, not misrepresented as an executed
input. The evidence's input and receipt hashes agree with their files,
and its copied common fields agree with the actual research receipts.
Subsequent acceptance/ledger edits will require their own refreshed hashes;
the table identifies the version reviewed here.

| Research process | Extensions | Candidate charges | Wall seconds | Sampled peak RSS bytes |
| --- | ---: | ---: | ---: | ---: |
| R1, complete adjacent-grammar development census | 229,926 | 1,635,171 | 3.1159076 | 64,946,176 |
| R2, direct selector checks plus complete part-word census | 46,798 | 9,912 | 0.2178804 | 32,899,072 |

Both completed without caps or case replacements. R2's 12 record-check
extensions plus its four case totals account for its 46,798 extensions;
the remaining candidate charges beyond the four case totals belong to
the direct selector check. Set-partition extensions, attempted factor and
composition tests, and polynomial updates are charged. This is not a full
repaired move-graph computation disguised by a smaller counter.

The limits remain 600 computation seconds, five million extensions and
candidate charges per round, 120 seconds per case, one research process,
sampled 2 GiB RSS and 250 MiB aggregate output-directory bytes. The
inspected run directory, including both snapshots and handoffs, was
1,135,592 bytes. Initial protocol/source preparation, snapshots, engineering
checks and semantic review are separate from the research counters. The
artifact guard is prospective at writes, not an OS quota; sampled RSS is
not an OS reservation. A filled handoff or later harness replay validates
response protocol, not the mathematics. The planned six formal stages
cost 16 declared dispatch proxies; this is the second of the two planned
critic calls, without P014's extra pre-contract critic dispatch. These
proxies do not measure tokens, money or scientific quality.

The narrow supported outcome is a complete elementary degree-zero pivot,
a written obstruction to preserving the whole ordered part word at
positive degree, and retained exact selector failures. The universal
height-three first-difference theorem remains unproved, novelty remains
unverified, and neither new Lean checking nor an independent completed
rebuild of the reported general positivity proof is asserted.
