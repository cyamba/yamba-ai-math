# RR003 auxiliary P2 branch by telescoping involutions

**Proposed proved auxiliary theorem, author-only assurance.** There are
explicit mutually inverse algorithms

    P2 <-> P3 disjoint-union K,

where P2 has residue parts 2,3,6,7 modulo9 and P3 has 3,4,5,6. K is the
literal cut family below. This is mechanism B's first product-side source
branch, not a complete KR1 residue-to-gap map or all recursive source states.
Both scheduled critic challenges preceded this final author proposal.
No separate semantic review or novelty verification is claimed.

## Literal complement and the mathematical advantage

A cut is (j,D), j>=0, of weight 9j+2+|D|. Its partition D may use:

* three-divisible residues 3,6 modulo9, except the literal part3;
* parts 9i+2,9i+7 with i<=j, except the literal part2;
* parts 9i+4,9i+5 with i>=j.

There are no other parts or hidden colors. j is explicit data on the
auxiliary family and is recovered by the forward algorithm; no saved path
is supplied to its inverse. K has no weight-zero object. Replacing its
weight by |K|-2 gives a positive literal model for the first source-side
auxiliary series (P2-P3)/q^2 appearing in Xia's (3.8), rather than declaring
a signed product to be a family. A full match with later recursive branches
is still missing. In particular P2, P3 are auxiliary residue families, not
RR003's original P1 residue domain.

Write P_i=(1-q^(9i+2))(1-q^(9i+7)),
Q_i=(1-q^(9i+4))(1-q^(9i+5)). Their exact local difference is

    Q_i-P_i = q^(9i+2)(1-q^2)(1-q^3).

Telescoping a finite product, then cancelling the factors 1-q^2 and 1-q^3
against the available small-part denominators, gives the above positive cut
family. This algebra suggests the objects; the explicit involutions below
supply the maps and proof. No coefficient agreement or rank matching is used.
This changes residue counts when quotient data require it, so it is not
the fixed-count lift refuted in recursive-seed-lift-obstruction.md.

## Actual finite state space and rules

Fix the input weight N and L=floor(N/9)+1. All non-three parts of weight
at most N have indices below L. An ordinary partition D in the state space
uses residues 2,3,4,5,6,7 modulo9; its non-three indices are below L.
All marks are subsets, so each marked value occurs at most once in the mark
set, separately from its arbitrary multiplicity in D. Every state has
combined weight N, counting its partition, marks and stated charge.

Layer0: label A or B and marks from all Q-pairs or all P-pairs respectively.
There is no charge. Its sign is (-1)^number_of_marks for A, its negative
for B. Here A will yield P2 and B P3 after denominator cancellation.

Layer1: a cut index 0<=j<L, local label Q or P, a subset of that local pair,
and other marks from Q_i for i<j and P_i for i>j. Its sign is the negative
of the raw product sign: Q has base minus, P base plus, multiplied by
(-1)^total_marks. Local values contribute their actual weights.

Layer2: a cut j, compulsory charge x=9j+2, local mark subset of {2,3},
and other marks from Q_i for i<j and P_i for i>j. Sign is
(-1)^total_marks. Local marks contribute two and/or three, besides charge x.

Two deterministic involutions act on this space. A cancellation toggle
chooses the **smallest eligible value** in its specified denominator list:
a value is eligible when marked or present in D. If marked, remove its mark
and add it to D; otherwise remove one copy from D and mark it. All other
data stay fixed. If none is eligible the state is fixed. The same smallest
value remains eligible after toggling, while every smaller one remains
ineligible; thus this is an involution, including arbitrary repetitions.

Alpha on layer0 moves A to the last layer1 Q cut, or B to the first layer1
P cut, using the same marks and D. On layer1, a Q cut moves right to the
next P cut; a P cut moves left to the previous Q cut. The same absolute
marks are retained and reclassified as local or other. At the endpoints
it returns to layer0 A or B. These pairs are literally reciprocal.
On layer2 alpha performs the cancellation toggle with denominator values
Q_i (i<j), P_i (i>j), 2 and3.

Beta on layer0 performs the cancellation toggle with all Q-values for A
or all P-values for B. On layer1 it pairs Q-empty with P-empty and Q-full
with P-full at the same cut. Empty weights agree; full weights agree since
(9j+4)+(9j+5)=(9j+2)+(9j+7). The four remaining local singletons pass to
layer2 as follows, retaining other marks and D:

| Layer1 local singleton | Layer2 local mark subset, in addition to charge x |
| --- | --- |
| P: x | empty |
| Q: x+2 | {2} |
| Q: x+3 | {3} |
| P: x+5 | {2,3} |

Beta on layer2 uses this table in reverse. This four-case table is a local
polynomial identity, not an enumerated image table by weight. It applies
uniformly for every j and N.

## All edges, fixed points and termination

Every nonfixed alpha and beta edge reverses sign and preserves combined
weight. For cancellation this follows by moving one marked factor to or
from D. The telescope edges retain all absolute marks and reverse their
base sign. The local table preserves charge plus marks and has the displayed
opposite signs across layers. These arguments also prove alpha^2=beta^2=id
on every state, not just paths reached in finite tests.

Beta's fixed points are exactly layer0 A with no marks and no Q-parts,
namely actual P2 partitions with positive sign, and layer0 B with no marks
and no P-parts, namely P3 with negative sign. Alpha's fixed points are
exactly layer2 with no marks and no forbidden denominator parts, namely
actual K with positive sign. There are no other fixed points.

At fixed weight the state space is finite: marks, j, charge and all partition
parts are bounded by N. Remove the self-loops at fixed points and regard
alpha/beta as differently colored edges. Every vertex has degree two except
these endpoints, which have degree one. A path starting at an endpoint
cannot enter a cycle: involutivity would give an entry vertex three incident
edges, or repeat the preceding edge without alternating colors. Thus the
alternating path reaches another endpoint after finitely many edges.
This is a termination argument from explicit reversible rules; it does not
list the state space, save visited objects or select a ranked target.

## Algorithms, both inverse identities and exact domains

To split a P2 partition, embed it as layer0 A with no marks. Apply alpha,
then beta, alternating until the next involution fixes the current state.
If the endpoint is layer0 B, return its P3 partition. Otherwise it is a
layer2 K cut, returned with its intrinsically produced j and partition.

To join a P3 partition, embed layer0 B with no marks and start with alpha.
To join a K cut, embed its layer2 state with no marks and start with beta.
Both paths end at layer0 A, whose partition is the output P2 object.
Indeed a negative B endpoint, followed by alpha, has positive sign before
beta and negative sign before alpha, so it cannot end at negative B or
positive K. Similarly a positive K start can end only at positive A. A
positive A start can end only at B or K. Reversing the same alternating path
restores every original state. This proves the two inverse identities,
disjointness of images, and exhaustive coverage of the whole P2 domain.
All terminal partitions/cuts have exact weight N by the edge invariant.
The code rr003_product_involution.py implements precisely these rules.

## Cost, contract exception and attribution

No polynomial runtime proof is supplied. A crude rigorous bound is enough
to distinguish correctness from the preferred design target. There are at
most (2+8L) 2^(2L) 2^(N+1) states: each layer has at most its cut/local
choices, at most 2L mark slots, and no more than 2^(N+1) partitions (bounded
by compositions). A nonrepeating path has at most this many vertices.
Straight list operations and sorting give a conservative
O((N+1)^3 log(N+2) 2^(3N+3)) bit-work bound. Only one current state and a
step counter are stored; O((N+1)^2) auxiliary bits suffice. The work bound
exceeds the preferred quartic target. If incorporated in a complete map,
the work contract must explicitly allow this exponential bound unless a
sharper bound is proved. No binding RR003 investigation limit is relaxed.
All finite testing still uses the existing ten-minute/RAM/storage/deadline
limits. No complete-map complexity follows from this auxiliary construction.

The method is established anti-telescoping combined with the Garsia–Milne
involution principle. [Bridges, A18 (2020), printed pp.13-14](https://math.colgate.edu/~integers/u18/u18.pdf)
was inspected for an actual anti-telescoping application; it credits Andrews.
[Garsia–Milne's original PNAS article](https://pmc.ncbi.nlm.nih.gov/articles/PMC319275/)
was inspected at the abstract/metadata level; its scanned full argument
was not re-audited here. The finite-path proof needed for these particular
maps is supplied above, so no uninspected imported theorem is substituted
for it. [Xia's (3.8)](https://arxiv.org/html/2609.08816v1)
motivates which auxiliary branch to seek. This is a bounded source comparison,
not proof that this elementary application is new. Novelty remains unverified.

## Freeze, smallest falsifier and learning

Freeze the code, domain, smallest-toggle priority, inverse and this argument
before the weight12 pilot. Advance to30 only after it passes. Check actual
P2, P3 and K objects, validity, weight, collisions, missing images and both
inverse paths, and directly audit the reached involution edges. Report walk
lengths and resource receipts. The first objects are previously exposed
in other RR003 domains where applicable; these are not held-out claims.
A smallest useful falsifier is a noninvolutive edge, weight/sign mismatch,
wrong endpoint type or inverse round-trip failure. No finite test would
replace the universal finite-path argument or a separate semantic review.

Decisive proof obligation supplied: actual terminating reversible object
operations realizing one positive source-side branch, including an intrinsic
complement. The next unresolved obligation is a complete compatible family
of later H_(n,r) branches beginning from original P1, with explicit auxiliary
state and endpoint algorithms to the gap path code. This first P2 split alone
does not imply that such a family has been constructed. The U–C global
canonical decomposition remains the leading alternative. Workflow hypothesis,
**unvalidated**: turning a local positive telescoping identity into two
involutions can retain information that fixed-count quotient lifts lose.
No discovery-rate improvement, third mechanism or mathematical completion
is claimed. Lean certification and exposition remain subsequent obligations.
