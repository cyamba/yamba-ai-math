# RR006 Ferrers, layers and recoverable information

Date: 24 October 2026. Stage: `geometry`, geometer profile; three dispatch
proxy units. The renewed instruction accepts the RR006 contract; historical
preparation-only headers in the contract/handoff remain historical records.

**Initial conclusion:** one exact unit-cube lift of the literal U domain is
lossless and has volume equal to weight. Its layers are completely determined
by the original weighted Ferrers diagram, so the lift adds no information for
recovering a branch already lost by a map. A separate elementary obstruction
shows that a full A–B bijection cannot preserve the literal distinct/repeated
split. Neither conclusion constructs the missing residual-root bijection.

All new `proved` claims below have a written elementary argument and are
**author-only pending RR006 separate criticism**. No formal checker or new
mathematical program was run in this stage. Novelty is **unverified**. The
RR005 normal forms and P/Q obstruction retain their earlier separate informal
review; the RR003 endpoints and late L-phase arguments retain author-only
assurance. No closed ledger/review allowance is reopened.

## Inputs and the 2D baseline

Inspected the twenty exposed records in
[illustrations/cases.json](illustrations/cases.json) and their
[assurance note](illustrations/README.md). They are already exposed examples,
not a held-out test. Some are duplicate objects across the two requested lists.
The unmatched weight-eight illustration is explicitly unassigned. No direct
Ferrers sliding map is inferred from the pictures.

For a descending ordinary partition `p=(p_1,...,p_l)`, use the bottom-aligned
Ferrers cells `(j,i)` with `1<=i<=l`, `1<=j<=p_i`. The horizontal coordinate
`j` runs rightwards and row coordinate `i` upwards; row 1 is the longest.
Every cell has unit weight for the literal A/B baseline, so area is ordinary
partition weight. Recover the descending row lengths and reverse them for
the public ascending A/B tuple. Empty has no cells. This is a representation
of a given partition, not an A–B map.

Literal A consists of positive ascending `p` satisfying

    p_(i+2)-p_i >= 3,
    p_(i+1)-p_i <= 1  =>  p_i+p_(i+1) == 0 (mod 3).

Literal B consists of positive ascending parts in residues `{1,3,6,8}` modulo
nine, with arbitrary multiplicities. Keep these domains separate from U.

For U write

    u=(u_1>=...>=u_m>0), u_j=F(h_j),
    F(5q+r)=9q+(0,1,3,6,8)[r], 0<=r<=4,
    h_1>=...>=h_m>0, h_(m+1)=0,
    0 <= h_j-h_(j+1) <= 4.

Thus `F` is strictly increasing on nonnegative integers. Each `u_j` is in
residues `{0,1,3,6,8}` modulo nine, but those residue conditions alone do not
define U. The drop to zero is essential. U's weight is `N=sum_j F(h_j)`.
The **decoded weighted Ferrers baseline** is

    D(U) = {(j,i): 1<=j<=m, 1<=i<=h_j}.

Its columns are arranged tallest first, left to right. Row `i` has cell weight

    w_i = (1,2,3,2,1)[(i-1) mod 5].

Then `sum_(i=1)^h w_i=F(h)`. Ordinary area `sum_j h_j` is generally not U's
weight: `U=(3)` has decoded height 2, area 2 and weight 3. A drawing that uses
decoded height as unit volume without the weights changes the mathematical
weight. Alternatively the ordinary Ferrers diagram of the numerical tuple
`u` has area N and is already lossless; decoding exposes the 5-flat constraint
more directly, without adding information.

The U representation is the conjugate of the weighted-row model W in the
existing literal definitions: `h_j-h_(j+1)` is the multiplicity of W row
length j, and the terminal inequality makes every such multiplicity <=4.
This elementary interface is distinct from the full B–U Stockhofe endpoint.
Any use of the latter's new RR003 implementation remains conditional on its
author-only endpoint audit; it receives no new review merely from this lift.

## G1: one exact lossless layered encoding

**Definition.** Use integer-indexed, axis-aligned unit cubes. Cube `(j,i,z)`
means the half-open block `[j-1,j) x [i-1,i) x [z-1,z)`. The first two axes
have the orientation fixed above; `z` is depth, upwards from zero. Define

    L(U) = {(j,i,z): (j,i) in D(U), 1<=z<=w_i}.

Every cube has unit volume and unit weight. There are no free colors, labels,
cuts, carries or coordinates. At depth 1 there is all of D; depth 2 contains
exactly rows `i == 2,3,4 (mod 5)` of D; depth 3 contains exactly rows
`i == 3 (mod 5)` of D. Residues here use row indices 1,2,3,4,5, with row 5
congruent to zero. No depth above 3 is permitted.

**Exact admissible domain.** A finite cube set S is admitted iff either S is
empty or all of the following hold:

1. Its `(j,i)` support consists of contiguous columns `j=1,...,m`, each with
   contiguous rows `i=1,...,h_j`, and positive nonincreasing heights.
2. At each supported `(j,i)`, the depth coordinates are **exactly**
   `1,...,w_i`, including all those cubes and no others.
3. The heights, including the final zero, have drops in `0,...,4`.

These are intrinsic membership conditions on S. This domain is a constrained
extrusion of weighted Ferrers diagrams; it is not the set of arbitrary plane
partitions. In fact its depth profile is periodic in i and need not be
monotone, so generic plane-partition operations do not preserve the domain.

**Projection and reconstruction.** The `(j,i)` support projection `pi(S)`
returns D. Recover each height `h_j=max{i:(j,i) in pi(S)}`, and output the
descending tuple `(F(h_1),...,F(h_m))`. On empty output the empty tuple.
The admissible-domain test is also the exact image predicate; no forward
trace or hidden table is consulted.

**Proved, author-only.** L is a bijection from all literal U onto exactly the
stated cube domain; both inverse identities hold. Indeed, the positive depth
1 sheet recovers precisely D, whose column lengths recover h and hence U by
F. Conversely the domain's exact depth-mask requirement forces every cube of
S to agree with L of that recovered U. The height test is precisely literal U
membership. This also handles repeated columns, absent rows and empty input.
No recursive step is used; reconstruction scans a finite support.

**Proved, author-only.** Its volume equals U weight:

    volume(L(U)) = sum_j sum_(i=1)^(h_j) w_i
                 = sum_j F(h_j) = N.

Since every `w_i>=1`, the 2D support has at most N cells and the cube set has
exactly N cubes. Explicit generation takes O(N) elementary cell/cube visits;
with coordinates written in binary this is O(N log(N+2)) bit output/work and
storage by direct lists. This is an encoding bound, not a bound for a missing
root map. The compressed list of h or U already stores the same information;
no compression or algorithmic advantage over the matched 2D representation
is claimed. All layer masks are recovered from row position alone.

## G2: what a projection can lose

The stated `(j,i)` projection is lossless. A shadow that additionally forgets
j, retaining only occupied `(i,z)`, is not. The smallest positive ambiguity
by maximum input weight is `U=(1)` versus `U=(1,1)`, of weights 1 and 2:
both shadows are `{(1,1)}`. This is minimal because empty has empty shadow
and there is only one positive U of weight 1.

Even supplying the weight does not make that shadow sufficient. At weight 6,

    U1=(3,1,1,1), h1=(2,1,1,1),
    U2=(3,3),     h2=(2,2)

are distinct literal U with the same `(i,z)` shadow: the two weighted rows
with depths 1 and 2. These are the first equal-weight ambiguity for this
specific shadow. To see minimality without enumeration, a common maximum
height 1 leaves only ones, fixed by weight; maximum height 2 allows
`U=(3^a,1^b)`, `a>=1`, and the first two solutions of `3a+b=N` with different
a occur at N=6. A maximum height >=3 requires N>=6 and at N=6 only `(6)`.
These are paper checks, not an executed sweep.

This does not claim every geometric projection is lossy; it identifies the
precise information, horizontal multiplicities, discarded by this shadow.

## G3: deterministic layers cannot repair an existing collision

**Proved, author-only elementary lemma.** Let `f:S->T` be any map and `E:T->V`
any deterministic output encoding. If `f(x)=f(y)`, then
`E(f(x))=E(f(y))`. If E is injective, then `E o f` is injective exactly when f
is injective. This follows by applying E to equality, and conversely its
injectivity. In particular a canonical lossless lift preserves both equality
and inequality of outputs; it cannot split a fiber already identified by f.

This narrow postcomposition statement does not exclude operations on the
layered **inputs**, a different forward map, or a carry intrinsically stored
and recovered in a permitted literal output. It supplies no impossibility
theorem for 3D constructions in general.

The [reviewed RR005 P/Q collision](../rr005/eight-strip-obstruction.md) is

    X=(2,2,(1,1),(0,0)), Y=(3,1,(3,3,3),(0,)),
    P(X)=Q(Y)=Z=(4,1,(1,2,2,2),(0,)).

The sources have weight 30 and the common output weight 38. These old objects
are inspected **symbolically only**; no above-12 input or endpoint was
executed here. Any deterministic encoding of the C output Z gives the same
encoded object for both sources. The U lift L does not itself encode C or
supply a C–U map. Appending a P/Q source tag to Z would add a choice not
recoverable from Z, hence would change the target domain. Source priority
cannot solve this collision of the already disjoint source branches.

The same lemma applies to the
[RR003 same-cut L failure](../rr003/l-branch-boundary-obstruction.md):

    7 -> (4,3), 11 -> (5,6),
    8 -> (5,3), 10 -> (4,6).

The two local full pairs `7+11` and `8+10` each give `3,4,5,6`; with the same
two appended threes the old common output is `(3,3,3,4,5,6)`. Its canonical
layers cannot identify which source pair was used. The old L inputs have
actual weight 25 and output weight 24; this is symbolic inspection only.
That late L conversion and the
[three/six phase-flag failure](../rr003/l-branch-phase-obstruction.md) retain
RR003 author-only assurance. The latter's eight-to-seven fiber argument
already excludes its specified fixed four/five counts and output levels;
no new encoding overrides those hypotheses or repairs the occupied K image.

A source-derived label can preserve the source distinction while it is still
present. To obtain a literal target bijection it must ultimately be decoded
from the target alone, or be explicitly included and charged in both domains.
Calling it a layer does not discharge that inverse obligation. For the chosen
L, all layers are deterministic, so they merely re-encode existing data.

## G4: distinct versus repeated is an analysis split, not an invariant

For each literal partition domain let D mean all part values occur at most
once and R mean at least one repeated part. Empty is D. On U these predicates
refer to the numerical columns `u_j`, equivalently equality of adjacent
decoded heights, since F is injective. They do **not** refer to repetitions
in the conjugate W rows. On C, mu/nu are exact-length increment vectors,
including zero entries; repetitions of increments are not literal A-part
repetitions and there is no definition-free "distinct C" predicate.

**Proved, author-only.** In A every repeated part has multiplicity exactly
two, is a multiple of three, and any neighboring part outside that pair is
at least three away from it. Three equal parts violate the distance-two
condition. If the repeated value is p, its adjacent equality forces
`2p==0 (mod 3)`, hence `3|p`. For a predecessor q or successor r, the
distance-two triples ending/starting with `(p,p)` give `p-q>=3` or `r-p>=3`.
Conversely a doubled multiple of three satisfies its internal adjacent
condition; the other literal adjacent/distance-two conditions still have to
be checked, so this is not a license to insert pairs arbitrarily.

For distinct A, an adjacent difference-one pair is permitted exactly when
its smaller value is `1 (mod 3)`: `p+(p+1)==0 (mod 3)` iff `p==1 (mod 3)`.
Thus distinct A can contain a close pair such as `(1,2)`. It is not a
"no-cluster" family; the exposed author-only endpoint example has
`A=(1,2)` and `C=(0,1,(),(0,))`, so `b=0` cannot simply stand for distinct A.
The literal close-pair arithmetic does not depend on that endpoint example.

**Proved, author-only: an exact obstruction to preserving the split.** At
weight 2 the only A object is `(2)`, which is D: the only other ordinary
partition `(1,1)` fails its adjacent condition. The only B object is
`(1,1)`, which is R, since the next permitted residue part is 3. Therefore
no full weight-preserving A–B bijection can send all D objects to D and all
R objects to R. Any complete construction based on this split must include
crossing branches or use a different intrinsic classification. This is an
obstruction to that proposed invariant, not to studying the two cohorts.

The saved pictures already illustrate the crossing. At N=2, `A=(2)` is D
while `B=(1,1)` and `U=(1,1)` are R. At N=3 the distinct `A=(3)` is displayed
against repeated `B=(1,1,1)`; the other distinct `A=(1,2)` is displayed
against distinct `B=(3)`. At N=7 distinct `A=(1,2,4)` is displayed against
repeated `B=(1,3,3)` and U. These endpoint examples retain author-only
assurance; the weight-two obstruction above is independently literal.

The separately reviewed U strips also cross its own cohorts:

    R1_U((1))=(1,1),        weights 1 -> 2;
    R3_U((3))=(3,3),        weights 3 -> 6;
    R6_U((6))=(6,6),        weights 6 -> 12.

Each follows directly from the reviewed append branch on its stated domain;
these are symbolic examples, not new executable checks. Their inverse
removals cross back. Hence census tables must distinguish a full object's
cohort from its residual root's cohort; counting descendants does not keep
the root's distinctness fixed.

## G5: U is not B and no geometric symmetry is assumed

Repeated B parts have arbitrary multiplicity. U repeats have no multiplicity
ceiling either, but U also has the decoded-drop constraint and permits some
numerical multiples of nine. For example `U=(9,1)` has heights `(5,1)` and
drops 4,1, hence is valid U of weight 10; it is not a B partition. Conversely
`B=(10)` is valid B, while numerical `U=(10)` would have height 6 and an
invalid terminal drop 6. A lift of U is therefore not automatically a lift
of the identical B tuple, and distinctness cannot be transported by simply
renaming the domain. The full endpoint requires its actual algorithm and
original assurance.

**Proved, author-only counterexample to a tempting structural bias.** Swapping
the two Ferrers axes of D is not a U weight symmetry. `U=(3)` has one decoded
column of height 2 and weight 3. Transposing its two-cell support gives two
decoded columns of height 1, namely `U=(1,1)`, of weight 2. Both are literal
U, but their weights differ. A corresponding 3D axis swap also need not
respect the fixed depth-mask rule. Therefore no row/column exchange group
action or equivariance is imposed. The layers' orientation is mathematical
data specified by the encoding, not a free symmetry.

## Stage disposition and next obligation

No new U–C/root-map rule is proposed or implemented. The chosen lift is one
representation, not a frozen rule variant; it consumes no new-map variant
slot. Its exact image predicate, inverse, volume, empty case and full U
coverage are specified above. There is no recursive termination or new
cross-domain coverage argument to test. No changes to the 1/3/6 grammar,
overlay of old partial maps, or recursive-route trial were made.

The useful next geometry obligation is precise: if a future root rule uses
a phase/carry, prove from its actual undecorated output a unique recovery
predicate distinguishing all claimed branches, including the symbolic P/Q
and lost-phase fibers. If it cannot be recovered, record the exact collision
and stop that rule; do not retain a source trace as an inverse. Root will
assess this alongside census/source clues in the authorized geometry-finish
stage, without implying that a successful carry exists.

For the later critic: review G1's literal domain and both reconstruction
identities, G2's stated shadow/minimality quantifiers, G3's narrow
postcomposition scope, G4's weight-two obstruction and strip crossings, and
G5's orientation example. These new claims remain author-only until that
review. No A/B endpoint theorem, full root match, novelty or full KR1 result
is claimed.

Resources for this initial stage: no mathematical process, new enumeration,
pilot, query, source-page open, dependency/provider, nested agent or external
message. File-read utilities took approximately twelve child wall seconds
under root's shared conservative maintenance reservation; no failed command
was observed. No new map variant used. Model tokens/runtime and service
memory are unknown where not exposed. Durable output is this note; original
failures, endpoint assurance distinctions and closed ledgers are unchanged.

## Geometry-finish integration — no new map or pilot

This is the authorized `geometry-finish` invocation, three further dispatch
proxy units. Dependencies read:
[family census](family-census.md), the definitions/root rows/freeze/receipts in
[census data](census-data.json), the updated
[source log](oeis-search-log.md), and
[clues and rules](clues-and-rules.md). The source content below is attributed
to the scout's recorded primary-source inspection; this geometer did not
perform additional web retrieval or upgrade its depth. The census passed its
frozen pilot through12 before the root-authorized unchanged extension30;
reading those saved rows here is not another execution or held-out test.

### Compatibility with the residual grammar

The census's new F_C grammar is a precise target-side constraint. In its
notation V means equal final nu entries, using the zero predecessor when
b=1. Besides empty, it separates a=0 with a terminal triple equality in nu;
a=2 with equal mu entries k in{1,2,3}, V if needed and the b=0,k=1 exception;
and a>=3 with equal final mu entries, preceding mu gap0..2, V if needed and
the stated extra b=0 boundary. Those statements are author proofs from the
reviewed RR005 predecessor tests, pending the RR006 critic.

L(U)'s image predicate proves membership in U, not membership in any of those
C branches. It has no separately defined C output at all. To restrict it to
F_U, recover U from the depth-1 sheet and apply the reviewed intrinsic
L1/L3/L6 failure tests in their proper order. This defines exactly the lifted
F_U subclass and adds no new branch oracle. It does not tell which C grammar
case a root should occupy. A different local motion on cubes would have to
prove its own image, weight, inverse and global coverage obligations.

In particular, the census proves that every nonempty F_C root has a
within-vector repeated increment, while its exposed first nonempty F_U
roots at weights8,10,12 are `(8)`, `(9,1)`, `(9,3)`, all column-distinct.
There is no contradiction: these are different side-specific predicates.
It does refute treating repetition as the same branch symbol on both sides.
The census's first family also has equal/different mu entries according to
whether its unit excess s vanishes, while the k residue controls coverage;
the one-pair family alternates distinct/repeated A phase while remaining
covered. Thus repetition does not become a coverage test after the lift.
These are consequences of the submitted grammar/family statements and
exposed rows; they inherit those statements' assurance, not a new theorem
about endpoint implementations.

The source log is consistent with this assessment. Its Kurşungöz S1 records
the isolated pair move `(1,2)->(3,3)`, showing a phase change under a
weight-three cluster move; it does not identify a U statistic. Its
Andrews–Keith S2 records exactly the periodic weighted-conjugate setting
used by G1, including the 5-flat terminal restriction. This is attribution
and a weight constraint, not evidence that the cube lift advances psi.
A272397 identifies the full B count by its definition; it gives no root
parser, distinction-preserving map, or geometric inverse.

The strengthened integrated conclusion is deliberately narrow: the exact
lift retains all U information already present, but **deterministic
postcomposition of a collided output** cannot recover a discarded branch.
This does not prohibit a new operation before that collision, an intrinsic
carry in a changed allowed output, or a completely different construction.
No unresolved inverse ambiguity exists for L on its stated image. The
unresolved inverse/coverage gap is the missing cross-domain rule itself;
none was supplied, tried or repaired in this stage.

### Two ranked future directions

These are bounded next-session proposals, not accepted algorithms or current
execution authority. They are alternatives for research allocation; neither
is asserted to succeed.

| Rank | Exact next lemma and mathematical objects | Closest inspected work / source depth | Smallest falsifier | Fresh resource estimate and drop condition | Remaining global obligation |
| --- | --- | --- | --- | --- | --- |
| 1 | Construct a canonical, reversible U-root context code whose decoded coordinates satisfy **exactly** the census's four disjoint F_C grammar branches (including empty), with `|U|=a^2+3ab+3b^2+sum(mu)+3sum(nu)`. State the code directly from the undecorated root or boundary; a saved path, a fixed adjacent-height charge for b, or an added free phase is not a code. As the first feasibility lemma, account for each exposed root at8,10,12 and explain the complementary branch predicate before implementation. | Reviewed RR005 normal forms and submitted F_C grammar; scout-inspected Kurşungöz Theorem7 cluster construction. RR004 already excludes its stated fixed-transition charge class; source cluster phase alone supplies no opposite-root statistic. | An omitted `(8)`, `(9,1)` or `(9,3)` root, two roots with the same proposed code, or a code producing a negative/unsorted/wrong-length coordinate. These seeds are tests of a universal claim, not its definition. The symbolic P/Q fiber remains a required recovery control if its branches are reused. | Fresh20-minute paper feasibility allocation, at most30seconds standard-library computation only after an exact freeze and input/output-bounded pilot12. Drop the particular code at its first unrepaired ambiguity, wrong weight, missing case, or paper deadline; preserve the failed version. | Prove the code works for **every** F_U and its inverse reaches **every** F_C exactly once, then combine the reviewed strip counts. A seed match or additional infinite family does not discharge this. Full A/B endpoints still retain their own assurance gap. |
| 2 | Prove a genuine specialization lemma for Konan's stated flat/regular colored bijection: finite canonical root encodings on **both** sides, an allowed0/1 minimal-energy matrix and ground, common KR1 size specialization, recoverable colors, and exact closure of the two image subsets under the published map. | Scout-inspected Konan2002.00300v2 Definition2.1/Theorem2.8; statement/ground equations inspected, full proof and KR1 application not audited. It preserves non-ground color order and energy under explicit conditions. This is an **unverified applicability lead**, not psi. | A weight8/10/12 root without a canonical code; two legal colorings of one undecorated root; wrong total weight; failure of the ground/terminal condition; or a mapped colored object outside the opposite root-code image. Resolve the HTML's recorded `c != 0`/ground notation before using the theorem. | Fresh25minutes for primary-proof/assumption work and at most4read-only page opens within a new declared retrieval allowance; no pilot until encodings and closure are formulated. Drop this specialization at the first free label, failed energy/ground equation, mismatched weight or image counterexample, or the paper deadline. This does not refute all colored methods. | Even a theorem-compliant colored correspondence gives a root bijection only after both canonical encodings and exact image closure are proved. Then both inverses, universal coverage and the full KR1 composition/review remain. |

The first direction targets the actual missing parser. The second offers a
specific published framework only if its absent canonical encodings can be
constructed. Merely choosing three extra seed matches, recoloring the
existing cube layers, or assigning ranks within weight is not substituted
for either lemma. No third direction is added to dilute these obligations.

### Retained packet for criticism and final accounting

Retain G1's exact domain/inverse/volume and encoding bound, G2's precisely
specified shadow ambiguities/minimality, G3's postcomposition lemma, G4's
literal A repetition arithmetic and weight-two obstruction/strip crossings,
and G5's U-versus-B/orientation examples. The integration introduces no new
root algorithm or extension of those quantifiers. Its contextual comments
depend on the submitted census grammar/family statements and scout source
records; those must be reviewed with their own original assurances.

Load-bearing local dependencies are the literal U/C definitions and periodic
weights in `checks/kr1.py`; the reviewed RR005 proposals/reviews, including
`rr005_chains.py`/`rr005_six.py` only for operator definitions; the existing
illustrated cases; the symbolic P/Q and RR003 L records; and the four RR006
handoffs listed at this section's start. No code import or new mathematical
execution was used. Root should hash this final note and those exact
dependencies in the retained claim freeze before criticism.

Geometry-finish used approximately5seconds of reported read-only utility wall
time, no failed read command, no query/open, no mathematical process, no new-map
variant and no pilot. The two geometer invocations cost6proxy units total;
approximately17seconds of read utilities across them are for root's shared
conservative maintenance accounting. This corrects the initial rough
9-second estimate by summing child utility times rather than elapsed parallel
batch times. One administrative patch failed because its expected context
was absent; it executed no mathematics and made no change, and the exact
accounting edit then succeeded. Model/runtime/token/service-memory
measurements remain unknown where not exposed. Discovery is now closed for
this branch; later changes may only answer the reserved critic/correction
path, without reopening discovery or any old ledger.
