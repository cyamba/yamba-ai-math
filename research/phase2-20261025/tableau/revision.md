# Reserved refinement: complete finite n=6 local cancellation

Author packet, 2026-10-24 UTC. This is the single reserved refinement within
the already frozen at-most-three-label routing family 2. It does not replace
or modify the original author packet, its 151 supported assignments, or any
closed RR006/RR007 ledger. Distinct final review is pending at this freeze.

**Supported finite result, author checked:** the explicit local algorithm in
`revision_local.py` and `revision_layers.py` maps all 3,980 negative
occurrences for `[e_(5,1)]` across all 132 natural unit interval orders on
six naturally labeled elements to distinct positive occurrences, preserving
`inv_G`. Its entrywise inverse recognizes exactly these images among all
6,800 positive occurrences. The map uses no list of tableaux, weight rank,
saved matching, global used set, or per-poset lookup table.

**Proved partial-map result, ordinary author proof below:** its layered
admission rule is injective, preserves weight, has an intrinsic inverse,
and terminates on its explicitly defined domain. **Totality on the 132
size-six orders is established by exhaustive computation, not by a new
symbolic classification of every remaining case.** No totality theorem for
arbitrary posets, larger n, other elementary coefficients, or the full
Stanley–Stembridge problem is claimed. Novelty remains unverified. No proof
assistant was used. The final constant-size inversion guard is intentional:
the proof does not assume that every exploratory comparability shortcut
alone suffices outside the finite class checked.

## Objects, domain, and multiplicities

Use the original packet's conventions: `u <_P v` iff `h[u-1] < v`, where
`i <= h_i <= 6` and h is weakly increasing. A tableau has strict P-chain
rows, and a lower entry is never P-less than the entry immediately above
it. `G` is the incomparability graph. For an edge `{i,j}`, i<j, its inversion
contribution is one iff j occurs in a strictly earlier row than i. Columns
within a row make no contribution.

The literal signed coefficient is

`2 T6 - T51 - T42 + T411 + T321 - T3111 - T2211 + T21111`.

The two positive `T6` occurrences retain the distinct determinant tags
`row0` and `row1`. They are never merged. The other positive tags are `411`,
`321`, and `21111`. Negative shapes each have one occurrence here. Raw
opposite-sign determinant occurrences for other coefficients remain in the
original inventory; the present refinement does not coalesce them.

## Intrinsic extension lemma and inverse

Let F be a partial weight-preserving injection with exact inverse I. A new
layer prescribes at most one candidate `p(S)` for each source S. This is a
fixed six-entry rearrangement, sometimes with a comparable-prefix insertion.
The candidate must be a valid positive tableau and must pass the explicit
15-pair test `inv_G(S) = inv_G(p(S))`. For a proposed target T, construct a
finite ordered list E(T) of entry extractions from T. Filter it to sources S
which are valid, have F(S) undefined, and satisfy `p(S)=T`. If I(T) is
defined, the entire list is empty. Otherwise select its first member, if
any. Extend F only on that member, and extend I(T) by returning it.

Proof: old assignments are unchanged. New targets are outside the old
image by the I(T) test. At any new target, precisely one extracted source
is admitted; hence two new sources cannot collide. Every admitted source
is absent from the old domain. Validity and weight hold by their explicit
local tests. A source S has a new image T precisely when S is the first
filtered member of E(T); the inverse uses the identical predicate and
returns S. Thus the inverse recognizes exactly the extended image. This
argument needs neither Hall's theorem nor a mutable owner dictionary.

Every p(S) used here has S in its extraction list E(p(S)); the list is
obtained by deleting the newly inserted entries or undoing a fixed slot
permutation. This completeness is checked directly in the descriptions
below. Lists are ordered by increasing displayed slot indices. Only this
local priority is used: there is no ordering of all tableaux or of a
weight fiber.

Termination: each call at layer l consults only F or I at l-1. Computing
the candidate list at layer l does not call layer l. There are exactly
22 layers above the base. Each layer extracts at most 36 candidate sources
from the six entries of its one input target. The recursion is therefore
well founded with rank l; it is a finite tree even without caching. An
extremely loose operation bound obeys `B_l <= 76 B_(l-1) + C` for a fixed
six-entry local constant C. Caching changes runtime, not definitions or
ownership: functions are pure, and cached values can be erased without
changing their return values. This is a bounded local algorithm, without
a claim that its unoptimized recursive implementation is efficient.

## Base layer

The base preserves all original 151 assignments and gives them priority.
It then tries two inverse-bubble candidates for a T3111 source
`R/a/b/c`: merge a with b, then with c, subject to valid T321 output,
absence from the original image, and exact recovery by `bubble_demote`
at row 1. This gives an intrinsic inverse on its T321 images: demote that
row and require the forward merge to reproduce the target.

Remaining sources use a common demotion to T21111: remove the last cell
of the T3111 arm, or the last cell of the second T2211 row, and insert it
after the maximal initial suffix-leg prefix whose entries are P-less than
it. A removed T2211 endpoint is kept after the first singleton a. The
leg-relative order of all other entries is retained. A target has at most
four hook antecedents, found by extracting a singleton and appending it
to the two-cell arm, followed by at most three pair antecedents, found by
extracting a later singleton and appending it to the first singleton.
Filter for valid sources and exact demotion reproduction; exclude the
original domain and the already merged hooks. Select the first candidate.
This is the extension lemma with at most seven entry extractions.

Comparable-prefix demotion changes row order only between the removed
label and the passed prefix, all of whose labels are comparable to it.
Changing a same-row comparable pair into different rows creates no G
edge. All other incomparability-edge row orders remain unchanged. Thus
demotion preserves `inv_G`. The inverse-bubble branch is its reverse and
preserves the same weight. The original 151 cases retain the earlier
reviewed proof and image predicates. The new T321 and T21111 tags are
disjoint, and the exclusion tests avoid every original image.

The base covers 3,214 of the 3,980 finite sources. The previous source
variants are retained as discovery records; their incomplete domains are
not silently relabeled as complete.

## The twenty-two prescribed layers

Write a pair-sector source as `S = uv/ab/c/d`, with u<_P v and a<_P b.
Write `ins_R(x)` for insertion of x in the unique P-chain position in R,
requiring comparison with every member. Write `ins_L(x)` for insertion
after the maximal initial segment of L consisting of entries P-less than
x. Every displayed output additionally passes full tableau validity and
the explicit six-entry weight guard. Exact guards and left-to-right slot
orders are in `prescribed` and `preimages`; the code is part of the claim.

| Layer | Prescribed operation / target | Maximum entry extractions |
|---|---|---:|
| 1 | For hook `u x w/a/b/c`, remove its middle arm cell x into the singleton leg by `ins` | 4 |
| 2 | `ins_uv(c)/ab/d`, requiring c comparable with a,b | 3 |
| 3 | `ins_uv(d)/ab/c`, requiring d comparable with a,b,c | 3 |
| 4 | Merge uv and ab into one P-chain; target `chain/c/d` | 6 |
| 5 | If u,v,a,b form a P-chain: retain its extremes as the top row; insert its two middle labels into leg c,d, in reverse chain order | 36 |
| 6 | If v<_P b: `ub / ins_(a,c,d)(v)` | 4 |
| 7 | Top row uc; insert b then v into leg a,d; c comparable with u,v,a,b | 12 |
| 8 | Top row ud; insert b then v into leg a,c; d comparable with u,v,a,b,c | 12 |
| 9 | `uvb/ad/c` if v<_P b, a<_P d, c<_P d | 1 |
| 10 | Top row ub; insert v into a,c,d after a comparable prefix, exactly one smaller incomparable entry, and another comparable prefix; v<b and v parallel b | 4 |
| 11 | `ins_uvb(d)/a/c`, with the layer-9 comparison guards | 4 |
| 12 | Top row ua; insert b then v into leg c,d; u<_P a and v comparable with a | 12 |
| 13 | `ins_uvb(c)/a/d` if v<_P b and a<_P c | 4 |
| 14 | `ins_uab(d)/v/c` if u<_P a, c<_P d and v comparable with a,b,d | 4 |
| 15 | `uab/vd/c` if u<_P a, v<_P d, c<_P d and v comparable with a,b | 1 |
| 16 | `uav/cb/d` if u<_P a<_P v and c<_P b | 1 |
| 17 | `ucb/av/d`, subject to the three-edge balance below | 1 |
| 18 | `ua/c/v/b/d`, subject to edge balance | 1 |
| 19 | `udb/av/c`, subject to edge balance | 1 |
| 20 | `uvc/ad/b`, subject to edge balance | 1 |
| 21 | `uv/c/a/b/d`, subject to edge balance | 1 |
| 22 | `ud/a/c/v/b`, subject to edge balance | 1 |

For layers 4 and 5 choose the two retained arm entries in increasing
target-slot order; for layer 5 first choose two of four leg entries as
the chain middles. This gives at most `6*6=36` candidates. Layers 7,8,12
choose ordered distinct slots for v,b, hence at most `4*3=12`. Remaining
layers have the bounds displayed. A source with a prescribed image is
recovered by one of these cuts; each is then filtered for exact forward
reproduction, which excludes any spurious reassembly. The fixed
permutation layers have exactly one inverse slot assignment.

In particular, layers 7 and 15 add no new finite assignments, but remain
explicitly present: they are not hidden trials or counted as successes.
All 22 layers refine one already frozen routing family; no fourth
candidate family or new discovery fleet was introduced.

## Inversion balances and the useful triangle clue

For an incomparable pair x,y with x in an earlier source row than y,
reversing their row order changes `inv_G` by `sgn(y-x)`. Define this term
as zero for comparable pairs. A same-row source or target pair is
comparable because rows are P-chains. Thus its edge contribution is zero.
In layers 17–22 the lists below give all pairs whose strict row orders
reverse, after comparable same-row cases are discarded. Require their
term sum to be zero. This is an entrywise order test, not a test against
a histogram of weights.

| Layer | Reversed pairs (earlier-source entry, later-source entry) |
|---|---|
| 17 | (a,c), (v,b), (v,c) |
| 18 | (v,a), (v,c), (b,c) |
| 19 | (v,b), (v,d), (a,d), (c,d) |
| 20 | (a,c), (b,c), (b,d) |
| 21 | (a,c), (b,c) |
| 22 | (v,a), (v,c), (v,d), (b,c), (b,d), (a,d), (c,d) |

For layer 10, moving v from the arm into the leg reverses its edge with
b, contributing +1 since v<b. Exactly one smaller incomparable leg
entry crosses it, contributing -1; all other passed entries are
comparable with v. This explains its balance. The original conditional
triangle is a particularly simple two-edge instance with c<v<b. The
important discovery was to permit balanced incomparable crossings,
while recognizing and reserving old image languages intrinsically.

The comparable-insertion layers are useful shortcuts. For assurance,
the program retains the final exact 15-pair equality guard on *every*
prescribed candidate, including them. Accordingly, the partial-map
proof remains valid even without extrapolating their sufficient
comparability descriptions to a larger poset class. The computation
confirms that all admitted six-element cases have equal inversion.

## Exact finite protocol and result

Reproduce from the repository root:

```
python3 research/phase2-20261025/checks/meter.py --label tableau-revision-replay --timeout 30 -- python3 research/phase2-20261025/tableau/revision_final_check.py
```

`revision_final_check.py` checks every negative tableau, every positive
tagged occurrence, target validity, degree equality, absence of
collisions, both directions of exact image recognition, unchanged
original assignments, and membership in the frozen deletion/reinsertion
metric. It uses no coloring enumeration to construct the map. The prior
independent coloring comparison remains a separate check of the signed
coefficient identity, not a substitute for this injection check.

| Obligation | Result |
|---|---:|
| Size-six h vectors | 132 |
| Negative occurrences mapped / total | 3,980 / 3,980 |
| T51 / T42 / T3111 / T2211 | 19 / 96 / 1,273 / 2,592 |
| Positive occurrences tested | 6,800 |
| Positives recognized as images | 3,980 |
| Unmatched positives | 2,820 |
| Original assignments preserved exactly | 151 / 151 |
| Images moving 1 / 2 / 3 labels | 3,242 / 712 / 26 |
| Images moving more than 3 labels | 0 |
| Invalid images, degree changes, collisions, inverse errors | 0 |
| Remaining negative sources | 0 |

Positive counts keep both T6 tags: 1 row0 + 1 row1 + 187 T411 + 782 T321
+ 5,829 T21111 = 6,800. The 2,820 complement is aggregated over all 132
orders; each individual complement is a positively weighted set. Its
weight generating function is the corresponding coefficient by literal
cancellation. The full list of per-h results is in
`revision-final-results.json`.

This delivers complete finite n=6 multi-sector cancellation for this
coefficient, with an explicit local rule and inverse, rather than only
an existence matching. Exhaustive evidence is still part of the
totality assurance. Extending the formula beyond n=6 or removing the
final exhaustive totality step is open.

## Failures, boundaries, and provenance

The one-label family still has its exact two-source Hall witness
`h=(1,2,4,5,6,6)`, sources `14/23/5/6` and `14/25/3/6`, whose sole
one-label neighbor is `14/2/3/5/6`. The triangle adds `135/24/6` and
resolves that component. The wider family is indispensable in this
restricted sense. An isolated T3111-to-T21111 injection is still
obstructed by the prior total-order count; the present construction uses
T321 and other sectors and does not erase that failure.

Intermediate partial domains and exact residual witnesses are preserved
in the revision JSON files. The smallest residual at the 3,971 stage was
`h=(1,2,4,5,5,6)`, source `12/35/4/6`; layer 20 sends it to `124/36/5`
with the two opposing incomparable-edge flips through 4. This is a clue
to the last steps, not evidence of general higher-dimensional totality.
No 3D/Ferrers theorem emerged from this refinement; the substantive
mechanism is the comparison of row-order changes and their inversion
balance. Volume analogy alone is not used as a proof.

Finite augmenting-path diagnostics were run separately after fixing
3,169 and 3,868 assignments: the remaining 811 and 112 sources,
respectively, still admitted complete frozen-family-2 matchings. These
were feasibility diagnostics only and are not queried by the final map.
`revision_patterns.py` enumerated candidate families during discovery;
it is also not imported by the final map. The final algorithm contains
only fixed slot formulas, bounded target-entry cuts, and local tests.

The preliminary `structural-freeze.json` describes the earlier
Theorem-A-only 115-source stage. Development before the final original
17-file freeze changed structural.py and verify_structural.py, so their
two preliminary pins do not match those final files. No preliminary
freeze was rewritten. `structural-initial.py` has the original source
hash, and new `revision-recovered-initial-verifier.py` reconstructs the
exact original verifier bytes and SHA. The accepted final original
packet's 17 pins all match. This version history is distinct from a
claim that every historical freeze pins the latest code.

At most three precise next directions: (1) replace exhaustive size-six
totality by a symbolic case partition for the 22 local layers;
(2) compress the balanced rotations into a smaller comparable/incomparable
crossing lemma with a direct image language; (3) test a separately
authorized n>6 analogue with frozen layers and a distinct critic.
