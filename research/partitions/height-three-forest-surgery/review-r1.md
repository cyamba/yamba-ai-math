# P013 review: round one and the single proposed repair

Date: 2026-10-24. Reviewer: separate `frontier_critic` role. This is the
first of at most two proposal/review rounds in P013. The reviewer read the
contract, frozen protocol, source and tests, inspected the saved receipt and
source snapshots, and checked the obstruction below by hand. No reviewer
enumeration, search, coloring-oracle run, test execution or Lean build is
asserted.

**Verdict: supported finite grammar obstruction; universal target
incomplete.** Checked word surgery repairs P012's mark-only boundary
obstruction, but its complete relation has a new isolated negative state
at seven vertices. This is stronger than failure of four selectors and
does not refute coefficient unimodality. The proposed one-edge repair has
a sound conditional inverse argument as a **relation**. There is no
mathematical blocker to the one frozen round-two test; no claim of a
recoverable global pivot or successful injection is supported yet.

## Executed source and evidence boundary

The inspected base revision is
`a0c897fb7bcb0d01a9ccff5593c0471424255b96`, branch
`codex/height-three-coefficient-unimodality`. The saved receipt is P013,
round one, `repair=false`, `source_stable=true` and
`research_validated=false`. All named hashes matched both the source and
the retained `r1-source/` snapshot when initially checked.

| Item | SHA-256 |
| --- | --- |
| Ignored `.runs/h3-forest-surgery/r1.json` | `d2d032da37f170a95d52ec21b59906d473beca45fd0e7e91837c52c34eb3b112` |
| Frozen `protocol.json` | `538832456b04895b18a199ffa5fea9b9148137a7ce1f3ea87dcbba3c6eeea047` |
| Executed `forest_surgery.py`, preserved in `r1-source/` | `4c351ba740544420460b6b111a3952a7cd4a8f0529e48d2c0d6ab0a6a9eb6afb` |
| Edge-added module inspected before round two | `a6de720675f9a0419819450a92c1e716977336144db34c90eedf1e41d63f6667` |
| Written `repair.md` proposal | `16ed915f8ea139a17f3f3e3de58c8d1b26626ca97b0e96bba238cd97c39739cb` |

At repair inspection, the module differed from the executed snapshot only
by the addition of `edge_operations`. That addition is disabled in round
one and had not been searched at this verdict. Existing raw spaces, two
primitives and selectors were not changed, and no round-one rerun is
asserted. After the preflight verdict, the lead reported engineering
amendments for exhausted-round stopping, source binding and reproduction
receipt hashes. Those later amendments and the resulting round-two run
are covered by the [second review](review-r2.md); the edge-added hash above identifies the
earlier inspected version, not an assertion about the final current file.
Hashes bind the evidence to these versions; they are not mathematical proof
certificates or independent attestations of execution history.

The primary comparison remains [Tom v2](https://arxiv.org/html/2311.08020v2),
Definitions 3.1/3.3, Lemma 3.11, Proposition 3.7 and Definition 4.7.
The original path and clique rules are established mathematics. Accepting
only valid, weight-preserving instances outside their hypotheses does not
turn their general applicability into a theorem. Novelty of the selected
unimodality family remains unverified; this review makes no new exhaustive
literature-search claim.

## Complete states, decoder and moves

The inherited parent-forest and composition enumerators retain all raw
forests, all compatible ordered composition tuples of type `(n-4,3,1)` and
all permitted marks. Parent identities are retained even when words or
weights coincide. Repeated equal composition parts are not artificially
labelled. Both epsilon values are added, with the same lower-half degree
restriction as P012. The code computes the entire signed coefficient
before restriction, checks reciprocity and the first-difference identity,
and checks state uniqueness. No convenient two-sector cancellation is
substituted for that space.

The decoder follows the parent recovery in Tom's Lemma 3.11: successive
left-to-right maxima are joined, and every other entry has the rightmost
earlier greater entry as parent. It additionally requires the proposed
word to begin with its minimum, verifies every parent edge, and checks
that the actual canonical tree listing is exactly the proposed word.
This final round trip prevents an invalid transformed permutation from
being accepted as a tree. Valid source words recover their original parent
trees; no choice of an alternative tree with the same word is introduced.

`startmin` and `startr` use inverse sequences of swaps of adjacent label
ranks, not positions. A break cuts the canonical word at its last
composition part; a join considers every pair in minima order whose
second composition is a single part, including nonconsecutive components.
It decodes the proposed words, retains epsilon and the first mark, and
recomputes the **global** forest inversion after reordering components by
their minima. Thus cross-component inversion changes are included.

On an accepted word pair, suffix length and inverse rank swaps recover
the words, compositions and marks. Decoder uniqueness then recovers the
trees. Type is unchanged, component count changes by one and epsilon is
fixed, so sign reverses. The accepted global degree equation supplies
weight preservation. This proves a conditional symmetric relation; it
does not prove that every negative state has a legal word move.

The mark primitive changes exactly one mark by one and toggles epsilon,
with the direction forced by equal effective degree. Every saved move is
checked against the exact signed universe, and the code checks reverse
membership in the **same primitive**. Each deterministic selector is
tested in both directions; only reciprocal choices count as paired.
Directed collisions and recovery failures are retained separately.

If there is no isolated negative, augmenting paths use only these grammar
edges. A failed augmentation returns a negative subset with its complete
neighbor set and checks the strict cardinality deficiency. A successful
augmentation is merely a finite grammar-constrained matching, not an
explanatory construction or universal proof.

## Saved outcomes and an independently checked obstruction

All four development cases completed and each full coefficient agrees
with a newly executed independent coloring/subset-expansion oracle. None
was capped. No held-out case was evaluated in round one.

| Development `h` | Marked forest triples | Lower-half negative states | Complete-grammar result |
| --- | ---: | ---: | --- |
| `(2,4,4,6,7,7,7)` | 320 | 258 | Diagnostic matching saturates all negatives |
| `(3,6,6,6,7,7,7)` | 2,352 | 2,091 | Isolated negative at degree 2 |
| `(3,3,3,6,6,6,8,8)` | 0 | 0 | Empty target space |
| `(3,5,5,7,7,7,8,8)` | 5,024 | 4,485 | Isolated negative at degree 2 |

On the old example, all four selectors still fail, leaving respectively
`98,95,81,82` negative states unpaired. The diagnostic matching's existence
shows why selector failure alone would not refute that grammar there.
The new seven-vertex and nonzero eight-vertex cases instead have isolates,
so no matching using their frozen grammar can cover all negatives.

The disjoint-clique vector gives `K_3` disjoint union `K_3` disjoint union
`K_2`. No tree has enough vertices for the target part four, so there are
no type-`(4,3,1)` forest triples. Its trivial success cannot certify a
nonempty boundary family or repair P012's missing nonempty exceptional
tableau-sector coverage. The gap is retained, without replacing this case.

For the seven-vertex isolate, take

\[
 h=(3,6,6,6,7,7,7),\quad
 p=(0,3,5,5,7,7,0),\quad
 \alpha=((1),(3,3)),\quad r=(1,1),\quad\epsilon=0.
\]

The tree components are the singleton `1` and a six-vertex tree with
canonical word `2,3,5,4,7,6`. Thus the global word is
`1,2,3,5,4,7,6`; its graph inversions are exactly `{4,5}` and `{6,7}`.
There are 14 graph edges and the bounce contacts are `0,3,6,7`, so the
poset has height three and effective degree `2<=7`. Three composition
parts, two trees and epsilon zero give negative sign.

No mark can decrease from one. The only breakable composition is `(3,3)`.
Its last-part cut gives head `2,3,5` and tail `4,7,6`. The tail already
starts with its minimum, so rank normalization does nothing. It cannot
be a decreasing-tree canonical word: after starting at `4`, reading `7`
requires the absent edge `{4,7}`, since `h(4)=6`. The only component pair
cannot join under word surgery because its second composition has two
parts. Therefore this negative state has **no legal primitive neighbor**.
This is a written finite obstruction, computationally confirmed, not a
Lean certificate. Seven is the smallest permitted size; minimal degree
and lexicographic claims beyond this witness rely on the saved finite
enumeration and do not establish a globally minimal Hessenberg vector.

The exact coefficient on this example is zero. On the old example it is
`q^3(1+q)^3`, and on the nonzero size-eight example it is `q^5(1+q)^4`.
All computed lower-half differences are nonnegative. The obstruction
concerns the move grammar and is compatible with the conjecture.

## Conditional review of the sole round-two repair

The [written repair](repair.md) adds all single parent-edge cuts and joins,
retaining the old primitives. A cut gives two decreasing subtrees. Each
nonempty composition boundary is assigned to those subtrees in either
order when sizes agree. All other component payloads and epsilon remain
unchanged. If the original mark is `r`, the full global inversion numbers
give precisely

\[
 r_A+r_B=r+1+I_{\rm old}-I_{\rm new}.
\]

The code visits every bounded first mark and solves for the second; it
retains all pairs in the two allowed first-part intervals. A join adds an
edge from a component root to a larger adjacent vertex of a different
component and considers both composition concatenation orders. It solves

\[
 r_J=r_A+r_B-1+I_{\rm old}-I_{\rm new},
\]

and checks the resulting first-part bound. These are inverse rearrangements
of the same global degree identity. Cutting the added edge, choosing the
recorded composition boundary and recovering the original mark pair
returns the original state. Conversely, joining across a cut edge returns
the original parent tree. The multiset of composition parts is unchanged;
the component count changes by one and epsilon stays fixed, so total sign
reverses. Hence the relation is symmetric, valid and degree preserving.
The code recomputes canonical words rather than assuming a local inversion
formula, and charges edge, boundary, ordering and tested mark candidates.

The repair does address the displayed isolate: adding parent edge `1->2`
keeps its global word and inversion number, and composition `(1,3,3)`
with mark one gives a positive one-tree state of the same degree. This
checks one legal pair by hand, not coverage of all failures.

A cut edge and a composition boundary are witnesses of reverse membership,
not extra labels in the raw signed space. Several witnesses, original
mark pairs or sources may produce the same destination. Therefore the
conditional argument does **not** establish inverse recovery of a selected
map. Round two must retain the same-primitive reverse check, exact universe
check, reciprocal selectors, collision accounting and grammar diagnostic.
Scalar compensation may fail its bounds; no universal existence argument
has been supplied.

The four repaired selectors and the unchanged held-out vectors must be
frozen before their test. Selection may use only development outcomes and
must be locked before any held-out evaluation. A cap remains incomplete;
neither a failed nor an empty case may be replaced. This is the one allowed
repair. A second failure ends P013; a third primitive proposal or substantial
Lean development is outside this phase.

## Resources and assurance level

The measured round-one receipt reports 449,218 extensions, 102,855
candidate charges, approximately 5.527842 wall seconds, 5.333120 process
seconds and 33,128,448 bytes peak RSS. The candidate charges include raw
component/pair attempts, same-primitive reverse checks and any augmenting
path work. Recursive coloring visits are charged as extensions. Observed
values are below every declared round and case ceiling. Artifact output
uses the inherited aggregate directory guard; the inspected output
directory contained 271,801 bytes. RSS monitoring is sampled, not an OS
reservation. These measurements are not asymptotic complexity bounds.

Protocol regeneration, including the deterministic frozen-vector ranking,
occurs before the computation budget starts; engineering tests and this
source review are also separate from the research counters. Their work
should remain separately identified rather than being folded into the
reported research wall time. Tests cover rank-map inverses, decoder round
trips, conditional relation reversibility, the old obstruction's repair,
full state census, fresh held-outs, Hall certificates and caps; the added
edge-repair tests were read without reviewer execution.

The accepted theorem target remains conjectural and its novelty unverified.
There is a written conditional relation proof and a written finite grammar
obstruction, plus exact computational evidence. There is no universal
unimodality proof, new positivity theorem or new Lean certificate.
