# P014 second and final review: a complete grammar obstruction

Date: 2026-10-24. Reviewer: separate `frontier_critic` role. This closes the
second of two P014 proposal/review rounds. The reviewer inspected the frozen
specifications, both executed source snapshots and receipts, the current
implementation, and the written [obstruction](obstruction.md). The reviewer
did not enumerate states, run a research search, run tests or Lean, modify
implementation, or use another agent. File hashing and reading saved JSON
are provenance checks, not additional research executions.

**Verdict: the proposed direct-neighbor cancellation construction is
refuted, including its sole digit repair.** Two actual negative states of
degree three have exactly one positive neighbor in the union of all five
frozen primitive groups. The complete-neighborhood certificate is supported
both by the recorded computation and the independent finite argument below.
This is stronger than failure of the four selectors. It is not a
counterexample to coefficient unimodality, and does not exclude a future
rule whose pairs are composite transformations with a different neighbor
relation. The universal partial inverse arguments remain valid; the
universal covering theorem remains incomplete.

## Evidence and source bindings

The repository is `https://github.com/cyamba/yamba-ai-math.git`, branch
`codex/height-three-coefficient-unimodality`, base revision
`a0c897fb7bcb0d01a9ccff5593c0471424255b96`. The current repository and
branch were read during this review. Earlier P012/P013 and publication/Lean
work remain outside this review's edit scope.

The saved round-one receipt is `.runs/h3-forest-transport/r1.json`, SHA-256
`f0d4a08c2c026f54ab04c857a8b08576fefa45394d7092f52b3e40c0f32b456e`.
The round-two receipt is `.runs/h3-forest-transport/r2.json`, SHA-256
`effd44d23a9494e2296cb0b9a66ad9c1565486dd70956d8ec2e4738aa65e474e`.
Its input hash equals the former receipt exactly. Every source hash in
each receipt agrees with its corresponding `r1-source/` or `r2-source/`
snapshot; the round-two source hashes also agree with the current files.

The executed round-one `forest_transport.py` hash is
`f866bc0074ec95219a10ba5f78ff16152e23f28e1e0f72c96928072df5ad1cf0`;
round two's is
`f2595de7e9c704ce8edeb8563ab3c4009f2b6db6d883c30b412c5c28f0f9286e`.
The snapshot diff adds record reconstruction, direct Hall verification and
its CLI entrypoint. It changes none of the five candidate generators,
degree/sign filters, selectors or frozen development data. The digit
generator was already present, inactive, in the round-one source. Thus this
is the one predeclared repair plus a narrower verification driver, not an
unrecorded second repair or a round-one rerun.

Additional bindings checked against those snapshots are:

| Artifact | SHA-256 |
| --- | --- |
| P014 README | `32134439f3395b7859e1edb4d94e1f3dea8ed66de4f032695a3176211533ad4e` |
| P014 program | `a7568e09cf202d16e564233a4ab9a57773183d9e173cde849bc676b382125718` |
| Original frozen protocol | `4aa14240af040cc78a71067135a02df84a48a6157d4a795626c728d18dfb3a82` |
| Round-two repair description | `72eb9894fd025c8de8464484bdce025e8d67c348d13b2bab433f09c5f6c13b6f` |
| Round-two verification protocol | `286139e2e9c4bc5d824eca57acf69187a6a153d7c279d2d1e740ff5caea320d8` |
| Inherited `forest_surgery.py` | `7920ad3a5725bdf01250eedf1c5d7f3606431a69fde4e6c669ed7af9af7987d3` |
| Inherited `forest_triples.py` | `da0a87a2a79c0ae84f40c46d73b80b051c43d22414effb3cc01abb3ef73a1287` |

The round-two protocol permits only receipt-hash rebinding when every other
specification field agrees. In this execution there is no rebind: its
recorded input is the preserved round-one receipt. The later written
obstruction and explanatory positive objects are semantic review material,
not additional executed search inputs or an additional primitive.

## Complete space and round-one findings

[Tom v2](https://arxiv.org/html/2311.08020v2), Definitions 3.1/3.3 and
Theorem 3.4, supplies the complete signed forest expansion. Lemmas 3.11/3.13
supply the tree-list inverse and insertion digits. These are inspected
existing mathematics. The conditional fork relation and the block/SCD
argument were reviewed in [round one](review-r1.md); they do not prove
coverage or novelty.

The inherited enumeration retains every larger-parent forest with at most
three components, every compatible ordered composition tuple of sorted type
`(n-4,3,1)`, and all marks `1<=r_i<=alpha_i[0]`. It computes the full raw
polynomial before imposing the doubled lower-half restriction. The doubled
sign is `(-1)^(3-m+epsilon)` and degree is
`inv_G(word)+sum_i(r_i-1)+epsilon`, so its degree-`d` signed count is exactly
`c_d-c_(d-1)`. Composition orders are genuine different objects; repeated
move witnesses are not additional objects. The coefficient, palindromicity,
first-difference identity and uniqueness checks completed in all four cases.

| Development vector | Negative states | Complete-grammar diagnostic | Four selectors' unpaired counts |
| --- | ---: | --- | --- |
| `(2,4,4,6,7,7,7)` | 258 | Saturates all 258 | `150,193,98,95` |
| `(3,6,6,6,7,7,7)` | 2,091 | Saturates all 2,091 | `1468,1544,767,733` |
| `(3,3,4,6,6,7,8,8)` | 358 | Saturates all 358 | `240,277,148,140` |
| `(3,5,5,7,7,7,8,8)` | 4,485 | Two-to-one Hall deficiency | `3473,3110,1717,1630` |

Grammar saturation is a finite matching diagnostic, not an explanatory
selector or universal theorem. All four fixed selectors fail in every
development case. The first, second and fourth coefficients reuse completed
P013 independent coloring comparisons, explicitly labelled as such. They
were not recolored in P014. The new third case has a fresh independent
coloring/subset-oracle comparison and a complete tableau comparison; all
three representations agree on `q^2(1+q)^5`.

The new boundary comparison actually contains 32 tableaux in the exceptional
negative shape `(3,3,2)` sector with determinant permutation `132` and
indices `(3,4,1)`. The other two sectors have 104 positive and 40 negative
tableaux. This is useful coverage of the n=8 sector missed by the old empty
example, which remains preserved in P013. It is not evidence for discarding
any other sector or for restricting the complete signed space.

## Independent exhaustive check of the Hall subset

Let `h=(3,5,5,7,7,7,8,8)`. The graph has edges

```text
12 13 23 24 25 34 35 45 46 47 56 57 67 78
```

Thus `M=14`. The poset has height three: `1<_P4<_P8` is a chain,
and the earliest possible successive comparable vertices are `1,4,8`,
after which there is no vertex. Take the common parent vector
`(3,5,4,6,7,0,8,0)`. Its two decreasing trees are paths with vertex
sets `A={1,3,4,6}`, `B={2,5,7,8}` and increasing canonical words
`1346`, `2578`. Define `S_13` using compositions `((1,3),(4))` and
`S_31` using `((3,1),(4))`, with marks `(1,1)` and epsilon zero.
Both have sorted type `(4,3,1)`, sign minus, and inversion/degree three:
their graph inversions are exactly `23,24,56`. In particular they lie
below the global midpoint seven. The Hall degree is **three**; degree
four belongs to one rejected word-cut candidate.

Every primitive can be exhausted without a search:

1. **Mark and digit steps.** At epsilon zero a degree-preserving step must
   lower the chosen coordinate by one. Both marks are minimal, and all
   tree insertion digits are zero because the component words are
   increasing. There is no move in either group. The digit repair
   therefore adds no neighbor to either state.
2. **Checked word splitting/joining.** Splitting `S_13` after its first
   composition part produces components with total word `12578346`.
   Its inversions are `35,45,47,67`; marks remain one, so its degree is
   four and it is rejected. Splitting `S_31` produces the positive
   state `U` below. The second component cannot split. The only possible
   word join has candidate word `13462578`; Tom's word inverse would
   require `2->6`, and edge `26` is absent. There is no word join.
3. **Single-edge splitting.** Only `A` can split its composition. Cutting
   `1->3`, `3->4` or `4->6` detaches sizes one, two or three. The
   size-two cut cannot match the composition boundary. The size-one cut
   gives the four-inversion forest above, requiring mark sum
   `1+1+3-4=1`, below the minimum two. The size-three cut gives `U`,
   with unique bounded marks `(1,1,1)`, for either composition order.
4. **Single-edge joining.** The only possible cross-component attachment
   is `6->7`. Its canonical word is `13467528`, with inversion five.
   The forced merged mark is `1+1-1+3-5=-1`. Both composition
   concatenation orders fail that bound. Root eight has no larger neighbor.
5. **Sibling-fork splitting/joining.** Both source components are paths,
   so neither has sibling children to split. The only possible join uses
   root `u=6`, direct child `v=4`, and other-component vertex `p=7`.
   Both required graph edges exist. Its word is `13475268`, again with
   inversion five, and its forced merged mark is again minus one.
   Therefore graph-valid fork geometry supplies no bounded-mark neighbor.
   Root eight cannot join to a larger vertex.

The sole surviving positive object is

```text
U parents       (3,5,4,0,7,0,8,0)
U compositions  ((3),(4),(1))
U marks         (1,1,1)
U epsilon       0
U word          13425786
```

Its inversions are `23,24,67`, so its degree is three and sign plus.
Both negatives reach it by edge splitting; `S_31` additionally reaches
it by word splitting. Its reverse edge join `4->6` recovers either
composition order with mark one. Its reverse word join recovers `S_31`.
These are actual same-primitive inverses. They do not duplicate `U`.

Consequently the five group sizes, in order mark/word/edge/fork/digit,
are exactly `[0,0,1,0,0]` for `S_13` and `[0,1,1,0,0]` for `S_31`.
Their complete neighbor union is `{U}`. The strict inequality `2>1`
precludes an injection pairing every negative with one direct accepted
neighbor. Since the complete round-one graph had no isolated negative,
cardinality two is a smallest deficient subset on this particular graph;
the saved augmentation procedure does not establish global minimality
over Hessenberg vectors or alternative grammars.

## Round-two verifier, resources and omitted evaluation

The direct verifier rebuilds the advertised states from parent vectors and
payloads rather than trusting saved inversion, sign or degree. It checks
actual type and the lower-half condition, enumerates the full five-group
neighborhood of both negatives, compares the resulting set with the
advertised positive set, and checks inverse membership in the same group.
It verifies `2>1`. Complete enumeration of all other signed states is not
needed for this finite Hall argument; complete neighborhood equality is.

The frozen [repair specification](repair.md) deliberately narrows round two
to that decisive certificate, because its sources have no eligible digit
step. This is an honest reduction of scope, not a successful replacement
for the originally possible full repaired-space/held-out evaluation.
No selector was locked, and neither fresh held-out case was run. They
remain `(3,5,5,6,6,9,9,9,9)` and
`(4,4,5,7,7,8,8,10,10,10)`, with no reported outcomes. There is no
held-out success, cap replacement, research rerun or third repair.

| Executed research | Extensions | Candidate charges | Wall seconds | Sampled peak RSS bytes |
| --- | ---: | ---: | ---: | ---: |
| R1, four complete development cases | 252,890 | 1,243,264 | 4.8796185 | 57,098,240 |
| R2, direct Hall verification | 2 | 228 | 0.4615005 | 24,297,472 |

These are separate bounded processes, both completed without caps. The
round-two count of two extensions means two source-verification iterations,
not a fresh enumeration of the forest universe. Its candidate charges
include forward attempts, rejected candidates and the computed inverse
neighborhood. Initial protocol checks, source hashing and input-receipt
parsing occur before the reported timer, and final source rechecking and
file writing occur after its receipt. Recomputing the frozen unrun-held-out
metadata occurs inside the round-two timer; its wall time is not solely
primitive generation. Neither resource receipt claims total session time
or counts engineering tests as research extensions.

The limits remain 600 computation seconds, five million extensions and
five million candidate charges per round, 120 seconds per case, sampled
2 GiB RSS and 250 MiB aggregate output-directory artifacts. The inspected
output directory, including both source snapshots, was 542,763 bytes.
The guard checks prospective total bytes before writing a report; it is
not an OS quota, and sampled RSS is not an OS reservation. No resource
boundary was approached in these executions.

Manual collaboration also needs separate accounting. There were three
critic turns: insertion/SCD preflight before the P014 contract/freeze,
then the two formal reviews. The harness plan's six formal stage dispatches
cost 16 proxy units. Conservatively pricing the extra preflight as another
critic dispatch adds two, for 18 across the broader manual preparation and
review process. This is a disclosed deviation from treating 16 as an
all-inclusive collaboration count; a harness replay at 16 does not erase
it. The preflight is not a third formal construction round, research run
or mathematical repair.

## Meaning for the unresolved target

The coefficient on the obstructing graph is `q^5(1+q)^4`, with lower-half
first differences `0,0,0,0,0,1,3,2`, using the inherited independent coloring
comparison. In particular its degree-three first difference is zero. The
Hall failure concerns permitted transformations, not a negative coefficient
or first difference.

As a separate hand check, the parent vector `(2,4,5,6,7,0,8,0)` gives
component words `1246`, `3578`. With the same respective two composition
tuples, marks `(1,1)` and epsilon one, it gives two distinct positive
degree-three states: the only inversions are `34,56`, so degree is
`2+1=3` and sign is plus. These actual objects lie outside the frozen
neighbor union. Their existence does not define an inverse, a permitted
new primitive or a universal construction. It does expose the structural
obligation to transport component membership while retaining recoverable
composition-order information.

The written block/SCD reduction and universal conditional fork/digit
inverse lemmas survive this negative result. Their claims must remain
separate from the refuted covering construction and finite comparison
results. A future phase would need a precise recoverable cross-block rule
that handles these minimal-coordinate path components, followed by its
own universal coverage and collision argument. This review authorizes no
third P014 proposal or search. The exact height-three elementary-unimodality
theorem remains conjectural in the audited record, novelty remains
unverified, and substantial new Lean formalization remains gated on a
credible universal proof. No new Lean certificate or unresolved theorem
is established by P014.
