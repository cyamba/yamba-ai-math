# RR007 Fleet A: paper-only revision

Status: active sole revision stage, 24 October 2026. Initial artifacts and
pins remain intact. New claims here have **author-only informal assurance**
until the reserved distinct final critic reports. Full KR1 is unresolved;
novelty is unverified. No fourth frozen finite candidate, numerical trial,
retrieval, dependency, endpoint execution or harness change is authorized.

## R1. A complete intrinsic weight-two orbit for the b=1 boundary

This is a universal restricted construction, not a claim for all b. It
addresses all C=(2,1,(k,k+s),(t)) with k,s,t>=0. To make the phase commute
with the reviewed one/three/six reconstruction where possible, define the
following numerical U families, with unspecified exponents nonnegative:

* k=0: `(6,3^(t+2),1^(s+1))` (the retained A3 wall).
* k=3m+1: `(9,6^(m+1),3^t,1^s)`.
* k=3m+2: `(9,8,6^m,3^t,1^s)`.
* k=3m+3, m>=1: `(10,9,6^m,3^t,1^s)`.
* k=3, t>=1: `(10,9,3^t,1^s)`.
* k=3, t=0: `(9,9,1^(s+1))`.

The m>=1 and t>=1 rows are one intrinsic family with marker10 and9,
some6 or3, arbitrary ones. The last row uses a mandatory one. It is
essential: `(10,9)` is not literal U because decoded nine has terminal
height five. The earlier provisional choice that used `(10,9,1^s)` for
s>=1 at k=3,t=0 is superseded here **before any trial or accepted map**;
the present single row commutes with adjoining the free s ones and has
the simpler phase inverse. Both choices were paper-only. No initial
frozen A1–A3 file is changed.

### Exact intrinsic image and parameter recovery

The image consists of exactly the displayed five support/marker families:
the k-zero wall; one9 and positive6s with optional3/1; one9 and one8
with optional6/3/1; one10 and one9 with some6 or3 and optional1; or two9s
and positive1s with no other parts. These predicates are pairwise
disjoint. From the wall recover t=#3-2,s=#1-1,k=0. From the9/6 row
recover m=#6-1, k=3m+1,t=#3,s=#1. From9/8 recover m=#6,k=3m+2 and
t,s by counts. From10/9 recover m=#6,k=3m+3,t=#3,s=#1. From two9s
recover k=3,t=0,s=#1-1. Thus every parameter is intrinsic, including
s independently of k, and equality of different parameter tuples is
impossible.

### Intrinsic operation and inverse

Define W on that union as follows. On the wall replace two3s and one1
by one9. On the9/6 family replace one6 by8. On the9/8 family, if there
is a6 or3, replace8 by10; otherwise replace8 by9 and1. On the10/9
family replace10 by two6s. On the two9 family replace one9 and one1
by two6s. All other entries stay. These replacements each add weight
two and preserve the recovered s,t. They advance k by exactly one.

The lowering operation is defined entirely from the same predicates.
On9/8 replace8 by6. On10/9 replace10 by8. On the two9 family replace
one9 and one1 by8. On9/6 with exactly one6 remove the9 and add two3s
and one1, reaching the wall. On9/6 with at least two6s, replace two6s
by10 when a6,3 or1 remains below9; when none remains use instead
`(9,6,6)->(9,9,1)`. Equivalently the last decision is whether the
reconstructed previous10/9 source would have some6 or3; if not, the
previous source must be the two9 family. This version requires the
following correction: when no6 or3 remains but ones do, the previous
source still belongs to the two9 family, not the10/9 family. Therefore
the actual decision is **some6 or3 remains**, ignoring ones. Replace
two6s by one9 and one1 in the complementary case. The intrinsic wall
has no predecessor in this orbit domain.

The displayed forward substitutions and these reversed substitutions
prove both identities, including the corrected boundary with s>0.
Each lowering step reduces literal weight by two, and the recovered k
decreases by one until the unique wall. This proves termination,
unique orbit endpoints, disjoint orbits and exact image on this b=1
restriction. No iteration history is saved in the output.

All displayed source images are literal: nine height five is bridged
by six height three, eight height four, three height two, or a mandatory
one height one; ten height six has nine height five above a required
six/three below. The other decoded gaps are at most four. Direct
substitution gives weight `13+2k+s+3t` in every row. The images beyond
the retained k-zero wall avoid every A3 image: the new9/6 family has
both9 and6, the9/8 family has both9 and8, the10/9 family has both10
and9, and the exceptional family has two9s. Each violates the earlier
A1/third-single support predicates; A2 and the A3 wall fail either
their lower-level multiplicity conditions or the required full levels.
For9/6 with t>=2, A2's no-one top multiplicity is satisfied, but the
lower6 multiplicity may exceed one; this apparent overlap is a
load-bearing issue considered below before any theorem is retained.

## R2. Exact normal-form reduction of the remaining all-b obligation

For a=2,k>0, reviewed L1 first removes exactly s from the final mu;
L3 removes the final nu gap, leaving final equality; L6 removes common
mu in threes until k in{1,2,3}. Therefore, on the positive-k mixed
sector, it is sufficient to construct a disjoint F_U root image for

`(2,b,(r,r),nu), b>=1,r in{1,2,3}, nu_b=nu_(b-1)`

(with the previous entry interpreted as zero at b=1), and then recover
the reviewed strip counts intrinsically. This is a sufficient route,
not a claim that the retained A3 zero-wall is normal-form compatible.
In fact it is not. The intrinsic root image must also avoid all strip
descendants already assigned by A3. The b=1 prospective roots are
`(9,6)`, `(9,8)`, `(9,9,1)`, but root disjointness alone does not prove
descendant disjointness from the alternative A3 map.

The root characterization and the old strip proofs retain the exact
assurance accepted in the initial separate review. No new execution of
them is performed here. The unknown remains a general interacting root
parser, not a matter of attaching a previously lost phase bit.

## R3. Refutation of the raw R1 extension and a canonical repair

The last disjointness assertion in R1 is **refuted**. At weight27,
`C=(2,1,(4,4),(2))` has raw R1 output `(9,6,6,3,3)`. This is also
the retained A2 image of `(0,3,(),(0,0,0))`. With positive ones, the
same support enters the retained A3 zero-wall: its three-level contour
has top multiplicity1 and both lower multiplicities at least2. Thus
internal reversibility of the raw chemical cycle does not establish an
extension of A3. This symbolic witness is not a newly executed trial.

There is, however, an intrinsic weight-preserving normalization of its
entire offending phase. Write a raw phase-one object as
`(9,6^M,3^T,1^s)`, M>=1,T,s>=0. Put l=0 if T=0, and otherwise
`l=min(M-1,T-1)`. Fuse l copies of `(6,3)` into l additional9s:

`Tnorm(9,6^M,3^T,1^s)=(9^(l+1),6^(M-l),3^(T-l),1^s)`.

This is not a choice of a trace: the image predicate is exactly
`9^r 6^p 3^q 1^s`, with r,p>=1, and either q=0,r=1, or q>=1 and
min(p,q)=1. On that intrinsic predicate recover l=r-1,M=p+l,T=q+l.
For q>=1, the identity
`min(M-1,T-1)=l+min(p-1,q-1)=l`
proves both directions. When q=0 the first branch forces l=0. This
also handles ties p=q=1 without choosing an order of fusion. No ones
are used in the predicate, so arbitrary s is recovered independently.

Let Tnorm be the identity on every other raw family of R1. These
families have markers8,10, or no6 in the exceptional two9 case, so the
normalization domain/image do not intersect them. Define the corrected
map by this Tnorm after the R1 table. Define its operation by the
conjugate `W=Tnorm o Wraw o Tnorm^{-1}` on the intrinsic corrected union.
Every constituent is explicit above. Its inverse is the same conjugate
of the raw lowering operation. In particular one first reconstructs
M,T from r,p,q if the source is normalized phase one; no saved k or
history is supplied. Both identities follow by cancellation of the
two Tnorm inverses, including the q=0 branch, r=1 branch, ties, and
the exceptional `(9,9,1^(s+1))` branch at k=3,t=0. In the raw inverse,
the decision between this exception and a10/9 source depends on some
remaining6 or3, and never on the free ones.

All normalized outputs remain literal U. The smallest non-one support
is6 when q=0, and is3 when q>0; the adjacent decoded drops among9,6,3,1
are at most4. Weight is unchanged by 6+3=9. Normalized phase-one images
cannot be A2 or the A3 zero-wall: when q>=1 one of the lower6/3 counts
is exactly1, whereas those three-level contours require both at least2;
when q=0 level3 is absent. They cannot be A1 or the retained third-single
family, since they have both9 and6. The other raw phases avoid A3 by
their marker pairs9+8,10+9, or their two9s. This proves an exact universal
extension for **b=1 only** of the retained zero-wall, disjoint from all
other A3 images. Parameter recovery is raw R1 recovery after Tnorm^{-1};
in particular t=T and k=3(M-1)+1 in the normalized phase. Lowering drops
k by one and the literal weight by two, ending at the unique k=0 wall.
All assertions in this paragraph have author-only informal assurance.

Root suggested an alternate repair of the same collision region: for
k=3m+1,m>=1,t>=2 replace `9+6+6+3+3` by `12+8+6+1`, giving
`(12,8,6^m,3^(t-2),1^(s+1))`. It is literal, weight-preserving, and its
markers recover m,t,s while avoiding A3. This is an assessed alternate
paper clue, **not included** in the chosen Tnorm construction; it has
not been trialled or promoted to another candidate.

The exact next lemma is a multi-level analogue of Tnorm preserving the
entire ordered nu contour. The present two-level minimum cannot simply
be applied independently at each level: a carry changes the contour
that supplies the next level's free nu gap. No claim for b>=2 follows.

## R4. A separate exact full a<=2 encoding into the product family B

This is an alternative basis, not an overlay on A3. It is universal on
the stated restricted domain, independent of any endpoint theorem, and
has author-only informal assurance. No finite instance was executed.

First define a completely intrinsic elementary carrier. Let lambda be
an ordinary partition whose multiplicities are at most2. For each part
`3^v r`, with 3 not dividing r, replace it by `3^v` copies of the B part
`3r`. This preserves triple weight: the output has weight3*sum(lambda).
The output uses exactly the B parts congruent3 or6 modulo9. Conversely,
for each such part3r, write its multiplicity in base3, and replace a
base3 digit d_v by d_v copies of3^v r. These digits lie in{0,1,2}.
Uniqueness of base3 expansion proves both identities and gives the exact
whole image. Call this carrier G3. No free color or trace is present.

For a=0 use `rho_j=2j-1+nu_j`, and output G3(rho). For a=1 use
`rho_j=2j+nu_j`, output G3(rho) and `1^(mu_1+1)`. Thus the decoded
lambda is distinct with gaps at least2, and has minimum respectively1
or2; an empty rho is permitted. These two images are disjoint because
the a=0 image has no ones and the a=1 image has positive ones.

For a=2 write mu=(k,k+s) and `rho_j=2j+1+nu_j`. Thus rho is distinct,
has gaps at least2 and minimum3, and its triple weight is
`3b^2+6b+3sum(nu)`. Add a prefix of ones and twos to rho to form lambda;
apply G3 to lambda; and also add literal B parts1 and8 by this table:

| k class | N and its digits | (c1(lambda),c2(lambda)) | #8 | #1 |
| --- | --- | --- | --- | --- |
| k=0 mod3 | N=k/3=3q+t | (1,t) | 2q | s+1+2q |
| k=1 mod3 | N=(k+2)/3=3q+t>=1 | t0:(0,0); t1:(2,0); t2:(0,2) | 2q | s+2q |
| k=2 mod3 | N=(k-2)/3=3q+t | (0,t) | 2q+1 | s+2q |

Here t is in{0,1,2}. In the middle row the two1s at t=1 replace a
single2, preserving triple weight6. This recoding is necessary to make
the a=2 image disjoint from the natural a=0,1 images. In particular the
unrecoded middle prefix would collide at weight6 with a=0,b=1,nu=(1).

The low weight contributions in the three rows are respectively
`3+6t+16q+(s+1+2q)=4+2k+s`,
`6t+16q+(s+2q)=4+2k+s`, and
`6t+8(2q+1)+(s+2q)=4+2k+s`.
This proves exact literal weight preservation for every b, repeated or
distinct nu, k,s, including b=0. Every output is literally B by its
residue support; no source-to-U assertion is needed for this fact.

### Complete intrinsic image and inverse

First reject any B object containing a part outside literal1, literal8,
and the residue3/6-modulo9 parts. Remove its1s and8s and decode G3 to
lambda. Its multiplicities are intrinsically in{0,1,2}. Remove its
1/2 prefix to get rho. A candidate a=2 image must have rho distinct,
gap at least2 and minimum3. Put q=floor(#8/2).

If #8 is odd, require c1=0 and put t=c2. This is the third row; require
`#1>=2q`, recover N=3q+t,k=3N+2,s=#1-2q.
If #8 is even and c1=1, put t=c2. This is the first row; require
`#1>=1+2q`, recover N=3q+t,k=3N,s=#1-1-2q.
If #8 is even, require one of the three middle-row prefix patterns:
`(0,0),(2,0),(0,2)`, giving t=0,1,2 respectively. Require N=3q+t>=1
and `#1>=2q`; recover k=3N-2,s=#1-2q. Reject other prefix patterns.
In every accepted row set b=len(rho) and `nu_j=rho_j-(2j+1)`.
The gap/minimum conditions imply exactly weakly ascending nonnegative
nu; hence the recovered tuple is literal C. The table and base3
uniqueness prove both identities, as well as injectivity across b.

For the a=0 image require #8=#1=0 and the whole decoded lambda to be
distinct gap2 with minimum1; recover b and nu_j=lambda_j-(2j-1).
For the a=1 image require #8=0,#1>=1 and whole lambda distinct gap2
with minimum2; recover mu_1=#1-1 and nu_j=lambda_j-2j.
These tests are disjoint from the a=2 tests: positive8 excludes a=0/1;
at q=0 the first a=2 row has a low1 and positive ones, and the middle
row must have two low1s or two low2s. A distinct gap2 lambda with
minimum2 cannot satisfy any of those predicates. Empty rho is handled
by the same rules, without a special collision or empty-b marker.

This alternative is **not coherent with A3**. At weight10 its a=2
tuple `(2,0,(3,3),())` maps to B=(6,3,1), whereas the retained A3 map
of `(3,0,(0,0,1),())` gives U=(6,3,1), on which the actual product
endpoint is the identity. Thus one cannot append this family to A3,
compose on an overlapping codomain, or add their finite coverage counts.

### An exact splicing lemma and its missing hypothesis

Let f:D0->X and g:D1->X be weight-preserving injections, with D0 a
subset of D1, every fixed-weight fiber finite, and both intrinsic image
tests and inverses given. For d in D1 outside D0, start x=g(d). While
x belongs to f(D0), replace x by g(f^{-1}(x)). This must terminate
outside f(D0): otherwise a finite repetition and injectivity backtrack
to d in D0, a contradiction. The reverse alternating path uses g^{-1}
and f until reaching D1 outside D0. Distinct paths cannot meet, by the
same backward uniqueness. Assign f on D0 and this terminal value on
the complement. This is an intrinsic injection extending f, with exact
image given by reverse-path termination in the new source domain. It
uses neither rank sorting nor equality of coefficients.

To use this lemma for the requested wall extension, g would have to
cover **all** retained A3 source tuples as well as the new all-b a=2
sector. R4 supplies only a<=2. The entire old a=3,b=0 source is missing
from this auxiliary injection. A path may stop at that old exclusive
source if one merely draws the two partial maps; finiteness does not
repair the missing hypothesis. Consequently R4 does not yet yield the
requested all-b W, even if an accepted full U/B endpoint is supplied.

If such a broad g were constructed with exact image, splicing would
give an A3-coherent extension H on all a=2. Then the operation
`W=H o (k->k+1) o H^{-1}` on that explicit source sector would have
both requested identities and the unique k=0 wall. This is a precise
remaining sufficient lemma, not an already constructed operation.

## R5. Genuine three-dimensional Ferrers geometry and an inclusion no-go

The initial three-sheet lift is the order ideal
`I(U)={(j,t,z):1<=t<=3,1<=z<=P_jt}` in the coordinatewise order,
where for h_j=5q+r,
`P_jt=3q+min(3,max(0,r-t+1))`. Thus the three arrays are actual slices
of one finite 3D Ferrers board, not three unrelated area statistics.
Its volume is the literal U weight and the exact row image determines
every h_j. In particular inclusion of lifted boards is equivalent to
entrywise domination of their ordered decoded-height lists, padded by
zero. Coordinate permutations preserve such inclusion.

For a row of numerical size3v the lift is
`(v+epsilon(v),v,v-epsilon(v))`, where epsilon(v)=0 for3 dividing v
and1 otherwise. A numerical1 row is `(1,0,0)`. Consequently the entire
retained mixed zero-wall can be read from the **middle slice** V, together
with its ordered boundary notches: V has all levels1..B, top multiplicity1
and lower multiplicities at least2; B=b+1, positive zero-middle rows
number s+1, and V conjugated has rows `(1,3+nu_1,...,2b+1+nu_b)`.
This is an exact recovery of all b,s,nu, not a recovery from sheet areas.
The periodic notch epsilon at multiples3 explicitly retains the phase
which an ordinary unweighted middle-area summary would forget.

There is an obstruction to the most natural genuinely3D operation. Take
the smallest mixed wall U0=(6,3,3,1), decoded heights(3,2,2,1), weight13.
Every lifted literal-U board containing I(U0) and having volume15 must
come from one of exactly three height changes:

* raise the height3 row to4, giving U=(8,3,3,1);
* raise the terminal height1 row to2, giving U=(6,3,3,3);
* append two height1 rows, giving U=(6,3,3,1,1,1).

This exhausts new zero rows as well as existing rows: height2->3 costs3,
height1->2 and height3->4 each cost2, no existing row has a cost1 step,
and every new row costs at least1. Each listed change is valid. All
three targets are already retained A3 images, respectively of
`(3,0,(1,2,3),())`, `(0,2,(),(0,1))`, and `(2,1,(0,2),(0))`.
Therefore **no A3-coherent weight-two W can consist solely of adding
two cubes to this 3D order ideal**. This excludes arbitrary choices of
the two cubes, not just a greedy priority, and also excludes conjugating
that inclusion by any fixed permutation of the three coordinates.
It does not exclude cube deletion/slide, a changing embedding, or a
cylindric boundary transfer. The source13 is the minimum mixed-wall
weight; this is a paper exhaustion, not a newly executed trial.

The successful b=1 normalization R3 has a geometric interpretation beyond
inclusion. The volume-preserving fusion6+3->9 changes the sheet-volume
triple from `(3,2,1)+(2,1,0)=(5,3,1)` to `(3,3,3)`: two cubes transfer
from the first slice to the third while the middle volume stays fixed.
The row order and multiplicity-one boundary decide the inverse. This
explains why simply adding dimensions or retaining only volumes cannot
solve the carry. It suggests transporting boundary cells across a seam,
with an intrinsic stopping cut, rather than a positive-cube insertion.

Classical cylindric-plane-partition/RSK analogies supplied by root are
uninspected search-abstract leads only. No cylinder profile or theorem
has been imported. A useful cylinder would need a recoverable seam which
encodes both the weight-one mu and weight-three nu increments; merely
matching the base norm Q, or transposing a cube shadow, does not supply
that seam. The prior sheet-area collision and old cube-shadow failures
remain in force with their original scopes.

## R6. Exact full C-side triadic recursive boundary grammar

This lemma is universal for literal C, but is not a U/C map. It makes
the higher-dimensional recursive target precise. Put a=3c+r,0<=r<=2.
Direct expansion gives
`Q(a,b)=3Q(b,c)+r^2+3r(b+2c)`.
Encode the ascending length-a mu by bounded-part multiplicities delta_i:
`delta_i=mu_(a-i+1)-mu_(a-i)`, with mu_0=0. Thus
`sum(mu)=sum(i*delta_i)` and all delta_i are nonnegative.
For j=1..c divide `delta_(3j)=3e_j+t_j`,0<=t_j<=2. Let eta be the
ascending length-c vector with bounded-part gaps e_j, equivalently
`eta_l=sum_{j=c-l+1}^c e_j`. Form the child
`C'=(b,c,nu,eta)`. Store the intrinsic boundary data r, the delta_i
for3 not dividing i, and the t_j. Then exactly

`wt(C)=3wt(C')+r^2+3r(b+2c)+sum_(3∤i)(i*delta_i)+sum_j(3j*t_j)`.

Every term in this residual weight is nonnegative. The denominator
identity behind the same exact division is
`(q^9;q^9)_c/(q;q)_(3c+r)`
`=product_{j<=c}(1+q^(3j)+q^(6j)) / product_{i<=3c+r,3∤i}(1-q^i)`.
Here this equality is justified by the explicit object division, not
used as a coefficient-equality substitute for a map.

The grammar has an exact inverse. If the child has dimensions(a',b'),
recover b=a',c=b',a=3c+r; its first rigging is the parent's nu. Recover
e_j from the child's second rigging eta, set delta_(3j)=3e_j+t_j,
insert the stored non-divisible delta_i, and cumulatively reconstruct
mu. All zero padding and repeated entries are thereby recovered. Stop
at(a,b)=(0,0), and forbid a spurious all-zero node above that terminal
node. Every other node has exactly the required finite boundary ranges.
After two steps each old dimension is divided by3 with flooring, so
this recursion terminates. These operations prove both identities for
all literal C without enumeration, auxiliary tags or external choices.

Geometrically the child weight has three layers, while division of a
height3j column multiplicity into triples groups volume9j into the inner
rigging and leaves0,1,2 boundary columns. The residues are computed,
not free colors. This gives a genuine recursive prism/boundary template;
it does **not** assert that the three-layer volume is already embedded
as an order ideal of the special U row shape. The exact missing lemma
is a canonical U cut realizing these child dimensions and boundary
digits, including its intrinsic image, inverse gluing and phase wrap.
The initial U three-phase hook grammar and this C triadic grammar are
two exact carriers, not a proved identification between their boundaries.

## R7. A broad auxiliary injection and an A3-coherent all-b a=2 operation

This is the principal new paper result of the revision. It uses the old
explicit RR003 a<=2 map, not R4, and repairs a newly supplied external
a=3 table. The complete construction below is author-only until the
reserved final critic checks it. No external script was imported or run,
no new finite trial was made, and no fourth frozen finite candidate was
created. It is a universal **restricted** map, not full KR1.

### R7.1 The fixed auxiliary map g2 on all a<=2

The exact fixed formulas and image recognizer are in
`research/rogers-ramanujan/rr003/round-2-proposal.md`, its
`round-2-revision.md`, and the unchanged
`research/rogers-ramanujan/checks/rr003_a2.py`. The preceding part was
separately reviewed in RR003; its final three-hole completion was still
author-only. Its universal proof must therefore be checked, not silently
imported as an accepted theorem. Here is its whole forward rule, to make
the new dependency explicit. Put
`delta_j=nu_(b-j+1)-nu_(b-j)`,nu_0=0, and write mu=(k,k+s) at a=2.
Let D_b have two copies of every3j,1<=j<=b. Every ordinary increment
below adds delta_j copies of3j. A parity increment means add q sixes and
r threes when nu_1=2q+r,r in{0,1}.

* a=0: D_b with one top3b removed, then ordinary increments.
* a=1: D_b, ordinary increments, and1^(mu_1+1).
* a=2,k=0: D_b plus3(b+1), ordinary increments, and1^(s+1).
* a=2,k=1: D_b plus3(b+2), ordinary increments, and1^s.
* a=2,b=0,k>=2: write k=3j+r+2,r=0,1,2. Use respectively
  `(8,6^j,1^s)`, `(9,6^j,1^(s+1))`, `(9,6^j,3,1^s)`.
* a=2,b>=1,k>=2,k not in{4,5,9}: let y=(k+2) mod4 and
  x=(k+2-5y)/4. Then x>=0,0<=y<=3,x+y>=1. Use D_b plus an
  extra3b, ordinary increments,8^x,10^y,1^s.

The empty-b a=0 case is empty; no top is removed there. The first four
rules include all their b=0 cases. The three missing k values use the
following fixed templates T, minimum ones h, and increment mode; append
1^(s+h) to T after the increments:

| k | b | T | h | mode |
| --- | --- | --- | --- | --- |
|4|1|9,6,3,3|0|ordinary|
|4|2|17,9,6,3|1|ordinary|
|4|>=3|D_b plus3(b-2),17|1|ordinary|
|5|1|10,6,6|1|parity|
|5|2|19,12,6|1|ordinary|
|5|3|19,12,9,6,6,3,3|1|ordinary|
|5|>=4|D_b plus3(b-2),19|1|ordinary|
|9|1|10,10,6|5|parity|
|9|2|17,17,9,3|0|ordinary|
|9|3,4,5|26^(b-2),18,10,3|10,11,18 respectively|ordinary|
|9|>=6|D_b plus3(b-2),26|2|ordinary|

For its exact image, validate literal U and use the fixed recognizer:
full three-multiple support with lower counts>=2 recovers a=0,1,or
k=0 from the ones and top multiplicity; a top singleton with the single
missing penultimate level recovers k=1. The b=0 carriers are recognized
by removing ones/sixes and testing the three displayed residuals. The
8/10 mixed family requires full three-multiple support, lower counts>=2,
top>=3, and y<=3; marker counts recover k. Finally17/19/26 distinguish
the hole templates, except the marker-free k4,b1 and single/double10
k5/9,b1 branches, recognized by their displayed small support and counts.
Subtract the unique baseline and minimum ones; reject negative counts,
unlisted residual parts or an invalid parity residual. Ordinary residuals
are exactly delta_j, whose reversed cumulative sums recover nu. The
unchanged code and RR003 written proof specify all exceptional top tests.
Thus this is an effective intrinsic image test with both inverse
identities, not an image defined by searching C inputs.

For clarity, the proof used below needs the following classification of
g2 images. Marker-free images are full support with lower counts>=2;
or a top singleton and missing penultimate level with lower counts>=2;
or one9 plus sixes, with mandatory ones or exactly one3; or the k4,b1
pattern one9,one6,at least two3s. Images with only8/10 markers are the
mixed full support with top count>=3, the b0 single8/no3 carrier, or
the k5/9,b1 hole patterns (single10 with>=2 sixes and<=1 three plus
positive ones, or double10). All other holes have17,19,or26. This finite
classification follows directly from the formulas, at every weight.

### R7.2 Provenance and failure of the external a3 table

Root supplied a user-pasted external report and read-only scripts under
`/Users/christopheryamba/.gemini/antigravity/brain/32daf9b4-83c9-4c6b-9f04-e38325f55706/scratch/`.
The files `verify_a3_b0_universal.py` and
`verify_full_kr1_bijection.py` were read through the current meter but
never imported or executed. Their old-a2 dependency is the canonical
RR003 map above. Their finite tests through35 are not this revision's
evidence and do not prove their universal assertion.

Both root and this author found the same symbolic collision in external
branch3G: for y=3q,q>=4,x>=1,z=0, its output
`(9,9,6^(q-2),3^(x+1))` is also g2 of
`(0,3,(),(1,q-3,q+x-4))`. This is a whole paper overlap family, without
executing a new high-weight control. Also the external `step_one` is
not safe on all of U outside g2: old hole templates have mandatory-one
entry cuts. Only the exact selected orbit language below is used.
Root corrected its earlier report objection: the full external theorem
included a terminal caveat omitted by the pasted summary, so (10,9)
refutes only that shortened summary, not the full theorem as written.

### R7.3 Repaired complete g3 on a=3,b=0

Write mu=(x,x+y,x+y+z),x,y,z>=0. In the following table append z ones,
except where the z dependence is explicitly shown. Every power is a
literal multiplicity, and every unlisted part is absent.

| source case | output before the free z ones |
| --- | --- |
|y=0|6^q,3^r where x+3=2q+r,r=0 or1|
|y=1,x<=1|8,3^(x+1)|
|y=1,x>=2|8,6,3^(x-1)|
|y=2,x<=1|10,3^(x+1)|
|y=2,x>=2|10,6,3^(x-1)|
|y=3,x=0|z=0:(9,6); z>=1:(10,6,1^(z-1))|
|y=3,x=1 or2|10,8,3^(x-1)|
|y=3,x>=3|10,8,6,3^(x-3)|
|y=3q+1,q>=1|9,8,6^(q-1),3^x|
|y=5,x=0|9,9,1 (then append z ones)|
|y=3q+2,q>=1, excluding preceding exception|10,9,6^(q-1),3^x|
|y=3q,q>=2|normalize(9,9,6^(q-2),3^(x+1))|

The final normalization is explicit. For M=q-2>=0,T=x+1>=1, if M=0
leave `(9,9,3^T)` unchanged. If M>=1, put l=min(M-1,T-1) and replace
l pairs6+3 by l additional9s. The normalized image is exactly either
`9^2 3^t`,t>=1, with no6; or `9^r 6^p 3^t`,r>=2,p,t>=1,
min(p,t)=1. The inverse in the latter case is
`l=r-2,M=p+l,T=t+l`; in the former M=0,T=t. Recover q=M+2,x=T-1.
The identity min(p+l-1,t+l-1)=l proves both compositions, also when
p=t=1. All ones remain the free z ones in this branch.

Here is the complete inverse/image test for the rest of g3. Read the
entire support, not just a head or area. A source with only6/3/1 must
have #3=r in{0,1},q=#6,2q+r>=3; recover y=0,x=2q+r-3,z=#1.
For head8 alone, require either no6 and #3 in{1,2}, giving y=1,
x=#3-1; or exactlyone6 and positive3, giving x=#3+1. Head10 alone
with those same positive3 alternatives gives y=2. Its remaining
alternative exactlyone6,no3,arbitraryones gives y=3,x=0,z=#1+1.
The separate no-ones pattern(9,6) gives y=3,x=z=0.
Head10+8 with no6 and #3 in{0,1} gives y=3,x=#3+1; with exactlyone6
and arbitrary3 gives y=3,x=#3+3. Head9+8 with arbitrary6/3 gives
q=#6+1,y=3q+1,x=#3. Head10+9 with #6+#3>=1 gives q=#6+1,
y=3q+2,x=#3. Exactlytwo9s with positiveones and no6/3 gives y=5,
x=0,z=#1-1. Finally>=2 nines with positive3 are precisely the normalized
last branch just described. In every nonexceptional case z=#1. Reject
all other supports/counts. These predicates are pairwise disjoint and
are exactly the table's image; consequently reconstruction recovers
every accepted output, and every source recovers its exact x,y,z.

Every table output is literal U. Decoded heights of1,3,6,8,9,10 are
1,2,3,4,5,6. The sole problematic bare10+9 is explicitly excluded by
the required6 or3, and its exceptional replacement has mandatoryone.
The other10 branches have3 or6 or8 as a bridge. Repeated9s in the last
branch have3 or6 below them, so the terminal gap is also valid. Every
other adjacent or terminal drop in the table is at most4. The outputs
have weight9+3x+2y+z: the y=0 equation is3(2q+r)=3(x+3); the other
rows are immediate substitutions; normalization uses6+3=9. The explicit
y=3,x=0 exception has weights15 at z=0 and16+(z-1) for z>=1.

### R7.4 Universal disjointness of g3 from g2

Apply the classification in R7.1. The marker-free y=0 family has at
most one3, so cannot meet a full-support lower>=2 image. Its no3
case has at leasttwo6s, so cannot be the old top-singleton missing-level
case. It has no9, hence cannot meet a zero-pair9 carrier or k4,b1.
The single8/10 families with no6 have at mosttwo3s, whereas a mixed
b1 marker image requires at leastthree. Their with6 cases have exactly
one6, whereas the mixed b2 image requires top6>=3; no larger complete
support is present. Their positive3 excludes the b0 single8 carrier.
The special10,6 family has onlyone6, excluding the k5,b1 hole. It has
no double10. The no-ones(9,6) family cannot meet the old9/sixes carrier,
which requires a one, and has neither required3 nor the old full/one-hole
support. The10+8 family has #3<=1 if6 is absent, and one6 otherwise,
so again cannot satisfy a mixed baseline; its two-marker head excludes
every other g2 branch.

The9+8 and10+9 families have exactlyone9. Any old mixed full support
containing that9 would have top9 count>=3, so they fail its test; they
cannot meet a b0 carrier or a17/19/26 hole. The exceptional two9s and
ones have none of the old permitted9 support/counts. Finally the repaired
last branch has either two9s and missing6, violating the old singleton
one-hole rule, or full3/6/9 support with one lower multiplicity exactly1,
violating lower>=2. Multiple9s exclude the old b0 and k4,b1 carriers.
No g3 image has17,19,or26, or double10. This exhausts g2's classification
and proves disjointness at every weight, independently of finite tests.

It follows that g=g2 union g3 is an effective, weight-preserving injection
on `D1={all C with a<=2} union {all C with a=3,b=0}` with exact image
and intrinsic inverse. This conclusion is subject to the stated final
review of the old g2 completion and all new arguments, not to agreement
between source reports or finite fixtures.

### R7.5 Exact alternating-path extension H and full all-b W

Let D0 be the accepted A3 source domain and f its accepted map. Then
D0 is a subset of D1: it contains a=0/1,all a2,b0,all a3,b0,and the
a2 mixed k=0 wall. Both f and g have intrinsic image tests and inverses.
Define H=f on D0. On d in D1 outside D0 start u=g(d), and while
u belongs to f(D0), replace `u<-g(f^{-1}(u))`. Return the first u
outside f(D0). All operations remain at the same literal weight.

This terminates without a saved trace. At fixed weight N there are
finitely many U partitions, and an iteration cannot repeat. Indeed,
equality between two later g-values can be canceled by injectivity of g;
then the preceding f-values cancel by injectivity of f. Backtracking
any hypothetical repetition reaches the first d and would place it
in D0, contradicting the start condition. Thus after finitely many
steps the path exits f(D0). A crude bound by2^N+1 steps follows since
U_N is contained in the integer partitions of N, hence in the finite
compositions, and no old-source state repeats. This is a termination
bound, not an enumeration or a definition by rank.

Here is the **complete exact image test and inverse**, including target-only
components. Validate literal U. If the initial u is in f(D0), return
f^{-1}(u). Otherwise repeatedly: if u is not in g(D1), reject; set
d=g^{-1}(u); if d is outside D0, accept and return d; if d is in D0,
replace u by f(d) and continue. The initial point is outside f(D0), so
the reverse path cannot enter a cycle: backward uniqueness would force
its initial point into f(D0). Hence it also terminates in the finite
weight fiber. It may reject at a g-undefined target; such a component
has an f-only and a g-only target and no new source. In particular the
image is **not** asserted to be f(D0) union g(D1). The accepted reverse
paths are exactly the forward paths from D1 outside D0. Reversing their
unique edges proves H^{-1}H=identity and HH^{-1}=identity on this exact
image. H extends f literally and its new images avoid every old f image.

Now let X2 be the intrinsic subset on which H^{-1} returns
`(2,b,(k,k+s),nu)` with b>=1. On X2 define
`W(u)=H(2,b,(k+1,k+1+s),nu)`.
Its inverse when k>0 is `H(2,b,(k-1,k-1+s),nu)`; k=0 is the intrinsic
orbit endpoint and has no predecessor in X2. These are deterministic
operations on literal U, using only exact image tests, count formulas
and the terminating paths above. They require no external k, free color,
seed match, stored trace, sorted list or coefficient equality.

Every raising step has literal weight+2 and every lowering step has
weight-2. Both identities follow from those of H. Decoding recovers
b,s,the entire zero-padded nu and k, so arbitrary repeated/equal nu,
nonzero gaps, b=1, free ones and all residue wraps are handled by one
argument. Distinct k levels or different(b,s,nu) cannot meet by H
injectivity. Lowering terminates at the unique k=0 wall, and since H
extends f this endpoint is exactly the retained
`3*(1,3+nu_1,...,2b+1+nu_b)^T +1^(s+1)`.
Thus every requested all-b a=2 datum is an iterate W^k of the required
wall, and every object of X2 has exactly one such expression. All other
A3 images remain fixed by H and disjoint from these new orbit levels.

This solves the revision's **all-b a=2 obligation at author-only written
proof assurance**, contingent on the final critic's dependency checks.
It does not solve full KR1. D1 still omits a=4,b=0 (minimum weight16),
a=3,b>=1 and all higher sectors. R6 gives a full C recursion but its
U-side cut/gluing is not yet constructed. R3 and R4 remain separate
partial constructions; their images/counts are not added to H.

The same theorem has a stronger compatible choice of f, without a new
finite variant. Let f1 be A3 together with the explicit corrected b=1
extension of R3. Its new images are disjoint from A3 and its common
k=0 restriction is identical, so f1 is a single intrinsic injection.
Its source D0' still lies in D1. Apply precisely the same alternating
construction to f1 and g. The resulting H1 preserves A3 **and** the
whole explicit b=1 map; its conjugated W agrees there with R3. Thus
one can choose H1 as the stronger all-b extension, if the final critic
also accepts R3. The exact image algorithm is unchanged except that
f1 replaces f. This is a corollary of the one path lemma, not the
addition of independently counted images or a fourth finite candidate.

## Review priorities and exact retained boundary

1. Check R7.1's old final g2 completion, including all three hole values,
   against its canonical formulas and exact intrinsic recognizer.
2. Check R7.3-4's repaired g3 image/inverse and its disjointness from g2,
   especially missing6, equal lower multiplicities and the y=3 z boundary.
3. Check R7.5's domain inclusion, both path identities, target-only rejection,
   termination and the all-b wall statement. These are the load-bearing
   steps for the new universal restricted theorem.
4. Check R3 for the stronger H1 corollary; R4 is independent and not needed
   by H/H1. Check the three-dimensional exhaustion R5 and full C grammar R6.

No new finite trial was permitted or performed. The initial A1-A3 pins,
scripts and reviews remain untouched. All new assurance in this document
is author-only written mathematical argument pending the distinct final
review. It is not formal certification, a novelty finding, a performance
claim, or a complete universal KR1 bijection. The full task still needs
an intrinsic exhaustive map on every C and every U, with all endpoint
dependencies audited under their precise scopes.

An explicit proper-image witness is U=(8,8), of weight16. It is literal
U (two decoded heights4, terminal drop4), but it lies outside f and f1
and outside g: no g2 b0 branch has two8s, its mixed8-marker branch
requires positive three support with at leastthree3s, and g3 has at
mostone8. Hence the H/H1 reverse image algorithm rejects it immediately.
The literal C=(4,0,(0,0,0,0),()) also has weight16 and is outside D1;
no smaller-weight C is outside D1 since a>=4 costs at least16 and
a=3,b>=1 costs at least21. These are exact scope witnesses, not a
new assigned seed or a claim that every U below16 has been proved covered.

In R7.1's finite image classification, the empty/all-ones cases are
handled separately by the first two forward rules; they clearly cannot
meet any g3 support. Every image test in R7.3 requires the **entire**
support to match the table, so an unlisted12,17,or any other extra part
is rejected even if a short head description appears to match.
