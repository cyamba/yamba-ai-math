# RR007 Fleet A: intrinsic plane-partition context

Status: active context investigation, 24 October 2026. Full KR1 remains
**unresolved**. No U–C candidate has been frozen or tested by this worker.
All `proved` statements here have elementary written arguments with
**author-only assurance**, pending the separate fleet critic. Novelty is
**unverified**. The construction below is a lossless source representation
and a source automorphism, not the missing root bijection.

The two main context claims are **G1**, the exact monotone three-sheet
representation, and **G2**, the exact three-phase recursive hook grammar.
The other constructions below are supporting partial-family lemmas or
decisive failures. For a bounded distinct review, the priorities are:

| Priority | Claim | Review location and obligation |
| --- | --- | --- |
| 1 | G2: full source hook grammar | Final construction section: check phase offsets, terminal drops, maximal-H image test, both inverse identities and weight recurrence. Auxiliary pilot12 is transcription evidence only. |
| 1 | A2: a-zero/a-one mixed conjugation | A2 section; the A author owns the separately frozen cross-domain artifact. Check top multiplicities and disjointness from A1. |
| 2 | G1: monotone three-sheet representation | First section: verify five residue patterns and the exact minimum-difference gap test. |
| 2 | Failure lemmas | Sheet-area collision12, greedy-corner collision11, independent-union collision13 and exhausted-contour obstruction19. Check only their explicitly stated scopes. |
| 3 | Supporting family lemmas | Source boundary slide, a-three family, first-mu-zero wall and resulting rank-one parser. The coordinator approved inclusion of the full a-three and positive-b wall families in the author's final A3 variant before its freeze; this worker supplies written arguments and no separate cross-domain finite run. Do not promote them to a global result. |

All positive entries have author-only assurance. No entry supplies a
universal F_U–F_C map. The G2 grammar is information preserving source
data whose translation to literal C is still missing.

## A monotone three-sheet representation

Let U have decoded descending heights `h_1,...,h_m>0`, with `h_(m+1)=0`
and consecutive drops in `0..4`. Recall

    F(5q+r)=9q+(0,1,3,6,8)[r], 0<=r<=4.

For `h=5q+r`, define the triple

    P_t(h)=3q+min(3,max(0,r-t+1)),  t=1,2,3.

Its five residue patterns are

| r | P(h)-(3q,3q,3q) |
| ---: | --- |
| 0 | (0,0,0) |
| 1 | (1,0,0) |
| 2 | (2,1,0) |
| 3 | (3,2,1) |
| 4 | (3,3,2) |

Take the plane partition with row `j` equal to `P(h_j)`, including its
zero entries. Equivalently its unit cubes are

    {(j,t,z): 1<=j<=m, 1<=t<=3, 1<=z<=P_t(h_j)}.

For each `t`, the sheet `lambda^(t)` is the ordinary partition with row
lengths `(P_t(h_1),...,P_t(h_m))`, dropping trailing zeros only when
interpreting it as an ordinary partition. The common row index remains
available in the full representation. The three sheets are nested.

**Proved, author-only.** This is an ordinary monotone plane partition:
each calibrated row is decreasing in `t`, and the chain `P(0),P(1),...`
is coordinatewise increasing. Its volume is exactly U weight because
`sum_t P_t(h)=F(h)`.

This is the antidiagonal restacking of the existing weighted Ferrers lift.
The multiplicities `(1,2,3,2,1)` are the antidiagonal sizes of a `3 x 3`
square. In each block of five weighted rows, place its cells at
`(s,t) in {1,2,3}^2` with `s+t-1` equal to the row within that block;
the new cube height is `3q+s`. Taking the first `r` antidiagonals gives
precisely the displayed row. It differs from merely viewing the old depth
mask as a plane partition: the latter need not be monotone.

### Exact image and inverse

The image consists exactly of finite three-column plane partitions whose
nonzero rows are calibrated by one of the five displayed patterns, and
whose adjacent rows, including a terminal zero row, satisfy

    min_t(P_jt-P_(j+1)t) <= 2.

For a calibrated row, recover `q=floor(P_j3/3)` and then recover the unique
residue `r` from the displayed pattern. Output `h_j=5q+r`, then `F(h_j)`.
Forbid the all-zero row except as trailing padding. Empty maps to empty.
This inverse and the image predicate do not consult a trace or a table of
objects. The five fixed residue patterns are part of the representation.

**Proved, author-only.** The gap predicate is exact. For `h>=k`, periodicity
gives `P(k+5)=P(k)+(3,3,3)`. If `h-k>=5`, every coordinate difference is at
least three. If `h-k<=4`, then `P(h)<=P(k+5)` coordinatewise and at least
one inequality is strict, since `P(h)` and `P(k+5)` are distinct. Thus the
minimum difference is at most two. This proves both directions, including
the final height drop. The row calibration and the gap condition therefore
give both inverse identities on exactly the declared domains.

No iteration is used; scans terminate on finite rows. The compressed
representation uses three integers per U column. Explicit cube generation
visits exactly `N` cubes at weight `N`. This gives no asymptotic advantage
over the original representation and adds no information.

## Coarse context can still discard the needed branch

### Sheet areas

**Refuted:** retaining only the three sheet areas suffices to recover U,
even with common weight supplied. An explicit witness within weight twelve
is

    U_1=(8,3,1), h_1=(4,2,1),
    P rows=(3,3,2),(2,1,0),(1,0,0);
    U_2=(6,6), h_2=(3,3),
    P rows=(3,2,1),(3,2,1).

Both have sheet areas `(6,4,2)` and total weight twelve. Their reviewed
RR005 normal forms have different F_U roots: `(8)` versus empty. The
identity is `P(4)+P(2)+P(1)=2P(3)`. No minimality claim is made. This is a
paper calculation, not an executed sweep. It does not exclude a parser of
the ordered sheet boundaries.

### Ordinary sheet Durfee coordinates

Let `D_t` be the ordinary Durfee-square rank of `lambda^(t)`.

**Proved, author-only.**

    0<=D_3<=D_2<=D_1<=D_3+2.

Indeed every row satisfies `0<=P_1(h)-P_3(h)<=2`. If `D_1=d>=2`, then
`lambda^(3)_d >= d-2`, and monotonicity gives a Durfee square of size
`d-2` in sheet three. The cases `d=0,1` are immediate. Nesting gives the
other inequalities.

Consequently the particular choice `x=D_1,y=D_3,a=x-y,b=y` for the
Eisenstein/Durfee identity

    Q(a,b)=(a+b)^2+(a+b)b+b^2

would force `a<=2`. It cannot cover full C, or the valid F_C root
`(4,0,(0,0,0,0),())` of weight sixteen (the latter is a symbolic witness,
not a new above-twelve execution). The same difference bound applies to
choosing any two ordinary sheet Durfee ranks. It does not rule out oblique
cuts, Frobenius boundary data, or a full ordered-boundary parser. The main
A author derives a stronger counting obstruction for any function of the
entire Durfee triple; see that author's artifact for its argument and scope.

## First-feasible local corner insertion fails

Here is an exact natural mechanism considered and refuted before any
finite trial. It is not a cross-domain candidate or a consumed fleet
variant. A one-cube increase of a calibrated row is possible only at
decoded phase `h mod 5` equal to zero or four. Define `G` on literal U by
scanning rows from tallest to shortest, raising the first such height by
one for which the sorted result remains literal U. If none is feasible,
append height one. It always has total weight change `+1`; the membership
test gives its domain/image membership and finite scanning gives
termination. An exact inverse would have to recover whether a row was
raised or a terminal row was appended.

**Refuted:** G is injective. The exact source/output collision is

    h=(4,1,1), U=(8,1,1) -> h'=(5,1,1), U'=(9,1,1);
    h=(5,1),   U=(9,1)   -> h'=(5,1,1), U'=(9,1,1).

In the first source, raising four to five is feasible. In the second,
raising five to six exposes the forbidden gap `6-1=5`; the one cannot
receive a one-cube increment, so G appends a one. Both sources have
weight ten and the output has weight eleven. An inverse can return at
most one predecessor, so an arbitrary priority cannot repair this rule.
The lost information is whether the top phase advanced or a terminal row
was created. No program was run for this witness.

## An exact recoverable boundary slide

The failed insertion contains a useful weight-preserving interaction.
Define S to consist of literal height tuples

    (H,4,1^s), s>=2,

where four occurs exactly once, all entries of H are at least five, and
H may be empty. Literal validity implies `min(H)<=8` when H is nonempty.
Define

    K:(H,4,1^s) -> (H,5,1^(s-1)).

Numerically this replaces one `(8,1)` by one nine. It moves one cube from
a terminal sheet-one row to sheet three of the row formerly calibrated by
phase four.

The exact image T consists of literal U with at least one one, at least
one decoded five, no decoded two/three/four, and for which replacing one
five by four and appending one yields literal U. Equivalently, after
removing one five, the remaining non-one minimum is at most eight, or
there is no such remaining entry. The inverse is that stated replacement.
Multiplicity of fives introduces no choice: equal columns are
indistinguishable. S and T are disjoint by their least non-one heights.

**Proved, author-only.** K is an exact weight-preserving bijection S to T.
For a source, the upper neighbor of the unique four was at most eight;
raising four to five keeps its gap at most three, and the remaining one
has gap four below five. At least one one remains. Thus the target is
literal. The inverse membership test is exactly the original gap test,
and it restores every multiplicity. Weight is preserved because
`F(4)+F(1)=8+1=9=F(5)`. Both operations terminate after a finite scan.
Swapping S with T by K and its inverse, and fixing all other U, gives a
canonical involution of all U. No external bit is appended.

For example `(8,1,1)<->(9,1)`. If the two equal-increment seed families
were matched as suggested in RR006, this would implement the C balancing
move `(2,0,(2,4),()) <-> (2,0,(3,3),())`. That interpretation is
**unverified** beyond this family. The general H context has no C parser.

The positive point is narrow: an intrinsic boundary can recover the phase
of a volume-preserving interaction when domain and image are disjoint.
The remaining lemma is to turn such slides into a terminating canonical
particle extraction with a global inverse, whose two free arm families
have the exact F_C costs supplied by the A author. Neither this involution
nor the three-sheet encoding supplies that lemma.

## A2: a uniform conjugation construction, including mixed objects

The coordinator approved this mechanism before its finite freeze. The A
author owns the frozen candidate and executable checks. This section gives
the construction argument independently of those checks. It is a separate
alternative partial map; it is not added to the old RR005 normal-form map.

Let C have `a in {0,1}`, arbitrary `b>=0`, and its usual exact-length
ascending increments. Set

    lambda_j=2j-1+a+nu_j, 1<=j<=b.

These are positive ascending parts separated by at least two. Let V be
their ordinary conjugate (using descending lambda for conjugation). Output

    U=3V                         when a=0;
    U=3V union 1^(mu_1+1)       when a=1.

For `b=0`, V is empty: the outputs are empty for `a=0`, and the indicated
nonempty string of ones for `a=1`. This is a uniform construction for
unbounded b and includes the mixed family `a=1,b>=1`.

### Exact image and inverse

If `b>=1`, V has every positive level from one through b. Write `c_k` for
the multiplicity of level k. The exact conditions are

    c_b>=a+1;  c_k>=2 for 1<=k<b.

The a-zero image has no ones and consists of three times such a V with
`c_b>=1`. Its empty case is included. The a-one image has at least one
one, all its other parts are multiples of three, and the resulting V has
the displayed multiplicities with `c_b>=2`. Its no-multiple-of-three case
is a nonempty string of ones. In either nonempty V, b is its largest part.

Recover a from absence or presence of ones. For a one, recover
`mu_1=(number of ones)-1`. Divide the remaining parts by three, conjugate
to the ascending lambda, and set

    nu_j=lambda_j-(2j-1+a).

For b zero use empty nu. The stated image conditions are exactly what
makes these recovered increments nonnegative and ascending: the least
lambda is `c_b>=a+1`, while successive lambda differences are the lower
level multiplicities and hence at least two. Both inverse identities are
ordinary conjugation followed by these explicit subtractions.

**Proved, author-only.** All outputs are literal U. Consecutive distinct
multiple-of-three parts differ by three, which corresponds to decoded
height gaps at most two; the minimum such part is three. Appending ones
adds the permitted gap from decoded height two to one. Repetitions add
zero drops. The terminal drop is at most two. The weight is

    3*sum(lambda)=3b^2+3ab+3*sum(nu),

plus `1+mu_1=a^2+sum(mu)` when a one. Thus this is an exact
weight-preserving bijection onto precisely its stated image. The finite
conjugation and scans terminate. It is not a map of all C.

### Disjointness from A1 and the old baseline conflict

The two-single A1 image consists of `(3,1^(s+1))`, pure positive strings
of sixes with optional ones, `(8,6^m,1^s)`, `(9,1^(s+1))`, or
`(10,6^m,1^s)` with the latter m positive. A2 a-one with b positive has at
least two threes. A1 has at most one three, and its one-three branch has
mandatory ones. A2 a-zero with b at least two also has at least two
threes; with b one it is pure threes; with b zero it is empty. The A2
a-one b-zero image is pure ones. These predicates prove disjointness of
the entire A1 and A2 images, not just the finite pilots.

The overlap with the **old** global empty-root baseline is real and is
not hidden. A2 sends

    C=(0,2,(),(0,0)) -> U=(6,3,3), weight twelve.

The reviewed old strips take this same U to empty F_U with counts
`n1=0,n3=2,n6=1`. On C, rebuilding those counts gives

    empty --R6--> (2,0,(1,1),())
          --R3--> (3,0,(0,0,0),())
          --R3--> (3,0,(1,1,1),()).

Thus the old C partner of U is `(3,0,(1,1,1),())`, not the A2 object.
The alternative A1/A2 union is coherent because its own image predicates
are disjoint. It cannot be silently overlaid with the old map.

## First mixed ambiguity of independent union

The shift `lambda_j=2j-1+a+nu_j` gives the correct interaction energy
`3ab` for any a, but independently adding an a-single U code loses the
profile. This proposed mechanism is already **refuted symbolically**,
before a trial or a new freeze:

    C_X=(2,1,(0,0),(0)), weight thirteen.

The shifted pair lambda is `(3)`, producing three threes. The A1 code
for the two singles with zero increments is `(3,1)`. Their union is
`(3,3,3,3,1)`. But the approved A2 object

    C_Y=(1,1,(0,),(2)), also weight thirteen,

has lambda `(4)` and produces exactly the same U. Thirteen is the least
possible weight of an a-two mixed object, since its base is already
`Q(2,1)=13`; this is a first obstruction for that domain, not a claim
that every imaginable independent-union extension first fails there.
No above-twelve inputs or outputs were executed for this argument.

The exact remaining issue is to supply a recoverable separator between
the single code and the shifted pair train. Choosing a source priority
does not restore the C profile that this union has erased.

## The a-three boundary-wall extension

The following full `a=3,b=0` family construction was recorded first as a
proof-level candidate, with no finite run and no candidate slot spent by
this worker. It illustrates an intrinsic gap separator that avoids the
A2 collision. Before the author's final A3 freeze, the coordinator
approved its inclusion together with the positive-b wall below. The
author owns that cross-domain freeze and its finite checks.

Write `mu=(x,x+y,x+y+z)` with x,y,z nonnegative, so weight is
`9+3x+2y+z`. Define the following five disjoint branches, where m is
nonnegative except when stated otherwise:

| C condition | U output |
| --- | --- |
| y=3m+1 | (8,6^m,3^(x+1),1^z) |
| y=3m+2 | (10,6^m,3^(x+1),1^z) |
| y=3m, x=0 | (6^(m+1),3,1^z) |
| y=0, x>=1 | (9,3^x,1^z) |
| y=3m, m>=1, x>=1 | (12,6^m,3^(x-1),1^z) |

These are literal U: the distinct decoded heights in each branch are
subsets of `(4,3,2,1)`, `(6,3,2,1)`, `(3,2,1)`, `(5,2,1)` or
`(7,3,2,1)`, with the connecting heights three or two included as needed
by the stated positive exponents. All gaps including the terminal are
at most four. Each row of the table has the required weight.

The exact image is the displayed five U families with exactly their
stated marker multiplicities and exponent ranges. The marker (8,10,
no such marker but some sixes and exactly one three,9,12) recovers the
branch. Counting threes/sixes/ones recovers x,m,z, then y. Thus both
inverse identities hold by direct substitution; no choices are retained.

The images are disjoint from A1, which has no three except its exactly
one-three/ones branch, and from A2: the first two have an eight or ten;
the third has exactly one three; the fourth omits the level six between
three and nine; the fifth omits nine between six and twelve. A2 always
has all multiple-of-three levels through its maximum. Consequently this
is a coherent further partial extension of the alternative A1/A2 basis.

The last two branches implement a boundary gap rather than preserving
the old strips. In particular `mu=(1,1,1)` goes to `(9,3)`, leaving
`(6,3,3)` to A2. This is still only a fixed-a family. The first uncovered
mixed profile `a=2,b=1` at weight thirteen and all higher-a root grammars
remain outside it. No finite completeness claim follows.

## A recoverable wall for unbounded mixed b

There is a further positive mixed boundary, independent of the
a-three proposal. Let `a=2`, `mu=(0,s)`, and let b and ascending nu be
arbitrary. Define the ascending gap-two partition

    lambda=(1, 3+nu_1, 5+nu_2, ..., 2b+1+nu_b),

and output `U=3 lambda^T union 1^(s+1)`. Its b-zero case is exactly the
already included A1 branch `(3,1^(s+1))`; b positive extends that branch
to arbitrarily many pairs.

The exact image has at least one one, all other parts multiples of three,
and V obtained by dividing those other parts by three has every level
from one to its maximum B, with

    c_B=1; c_k>=2 for 1<=k<B.

Recover `b=B-1`, `s=(number of ones)-1`, conjugate V to ascending lambda,
and put `nu_j=lambda_(j+1)-(2j+1)`. The top multiplicity one says exactly
`lambda_1=1`, and the lower multiplicities at least two give all remaining
nonnegative ascending nu. This proves both inverse identities on exactly
the stated image. Empty V is excluded.

**Proved, author-only.** Conjugation gives literal U for the same reasons
as A2. The weight is

    3(b+1)^2+3*sum(nu)+s+1
       = Q(2,b)+sum(mu)+3*sum(nu).

This wall is disjoint from A2: its positive unit tail distinguishes a
one-object, but its maximum multiplicity one excludes the A2 a-one
image, whose maximum multiplicity is at least two. Its b-positive image
is also disjoint from A1, because it has at least two threes and A1's
only three-containing branch has exactly one. It is disjoint from each
of the a-three branches: those either have eight/ten, a missing
multiple-of-three level, or exactly one three. All operations are finite.

For the final A3 union, add only `b>=1` from this wall: the `b=0` case
already belongs to A1, so it is one branch, not an additional preimage.
More explicitly, the a-three 12-marker branch always omits nine even
when `x=1` also removes all threes. Every wall with maximum twelve
contains all of three, six, nine and twelve. The a-three nine-marker
branch omits six, while its marker-free six branch has exactly one
three. Every positive-b wall has `B>=2` and at least two threes. These
intrinsic predicates prove disjointness at the boundary cases as well.
The resulting union contains the full rank-one sector discussed below;
its full image also contains objects of higher modular Durfee rank.

For the first mixed zero core this gives

    (2,1,(0,0),(0)) -> (6,3,3,1), weight thirteen.

This is a symbolic construction and has not been executed above twelve.
The recovery of a wall from the top multiplicity works for every b. The
domain is still proper: it requires the first mu increment to be zero.
It is not the remaining full global parser.

### An exact obstruction to the most direct wall bump

Suppose one tries to extend this wall to nonzero first mu by retaining
all three properties: `lambda` has length `B=b+1`, its gaps are at least
two, and the output unit tail remains `1^(s+1)` for `mu=(k,k+s)`.
Already at `C=(2,1,(3,3),(0))`, of weight nineteen, this requires length
two lambda of weight six and exactly one output one. The only positive
ascending possibilities with gap at least two are

    lambda=(1,5) or lambda=(2,4).

The first is already the wall image of `(2,1,(0,0),(2))`; the second is
already the A2 image of `(1,2,(0),(0,0))`. All three C objects have weight
nineteen. Thus **every** output in this narrow contour class is occupied,
not just the result of a chosen bump priority. This is a paper proof,
with no above-twelve execution. A full extension must change a contour
property or its encoding: for example length, a recovered gap defect,
modular row ends, or the unit-tail encoding. No such full inverse is
provided here.

### A possible recursive core, without an arm map

The base energy has exact binary identities

    Q(2c,b)   = 3(b+c)^2 + c^2;
    Q(2c+1,b) = 3(b+c)(b+c+1) + c(c+1)+1.

They suggest a triple Durfee square or rectangle of side `b+c` plus a
smaller residual single contour. This is **conjectural as a construction**:
the algebraic identities themselves are proved by expansion, but no
canonical split of all mu/nu arms, modular phase, image predicate or
inverse has been supplied. Even-index mu gap costs `2j` can be separated
into quotient and remainder modulo three, yielding bulk cost `6j` and
remainder cost `2j*delta`, `delta in {0,1,2}`. This records a possible
fusion mechanism rather than asserting that the necessary phases are
intrinsically recoverable.

## Complete rank-one modular-hook parsing

Define the three-modular Ferrers diagram of numerical U by replacing a
part `u=3q+r` with q full cells of weight three and, when r is one or two,
one terminal cell of weight r. The ordinary support row length is
`ceil(u/3)`. Use its ordinary Durfee rank, distinct from the three sheet
ranks above.

**Proved, author-only.** All U of modular Durfee rank at most one are
parsed by the coherent A1/A2 families, the a-three family, and
the first-mu-zero mixed wall. Indeed rank one means at most one part is
at least six; all other parts are three or one. If such an exceptional
top exists and another row exists, the next decoded height is at most
two, so the top height is at most six, giving top numerical value in
`{6,8,9,10}`. If it is alone, the terminal drop bounds it by eight. The
following disjoint cases give its exact C partner. Let t and s denote
the numbers of threes and ones below the displayed top.

| U form/condition | C partner |
| --- | --- |
| empty | empty |
| only `1^s`, s>=1 | `(1,0,(s-1),())` |
| only `3^t`, t>=1 | `(0,1,(),(t-1))` |
| `3,1^s`, s>=1 | `(2,0,(0,s-1),())` |
| `3^t,1^s`, t>=2,s>=1 | `(1,1,(s-1),(t-2))` |
| `6,1^s` | `(2,0,(1,1+s),())` |
| `6,3,1^s` | `(3,0,(0,0,s),())` |
| `6,3^t`, t>=2 | `(0,2,(),(0,t-2))` |
| `6,3^t,1^s`, t>=2,s>=1 | `(2,1,(0,s-1),(t-2))` |
| `8,1^s` | `(2,0,(2,2+s),())` |
| `8,3^t,1^s`, t>=1 | `(3,0,(t-1,t,t+s),())` |
| `9,1^s`, s>=1 | `(2,0,(3,s+2),())` |
| `9,3^t,1^s`, t>=1 | `(3,0,(t,t,t+s),())` |
| `10,3^t,1^s`, t>=1 | `(3,0,(t-1,t+1,t+1+s),())` |

Unspecified s is nonnegative. The literal U conditions exclude all other
rank-one cases, including ten without a three and nine without a lower
row. Each branch has a distinct intrinsic source predicate. Its inverse
is the corresponding restriction of the previously stated exact family
inverse; those family images are disjoint as proved above. Thus the
displayed image is an explicit finite union of C predicates, not a rank
matching of finite weight lists. Both inverse identities and weights
hold on arbitrarily long modular-hook legs. No finite experiment is used.

This is a complete parser only for one hook. It does not show that hooks
can be independently translated when several are nested.

## Exact three-phase recursive hook grammar

The modular-hook interior closes on three intrinsic phase domains. Put

    c_0=0, c_1=2, c_2=3;
    F_t(h)=F_0(h+c_t)-3t, h>=0, t=0,1,2.

Each `F_t(0)=0`, and each function is positive and strictly increasing
on positive h. Define U_t by the same descending decoded-height and
terminal drop conditions `0..4`, with numerical parts `F_t(h)`. U_0 is
the original literal U. The positive alphabets are shifts of the old
residues by minus three at each phase, not freely added colors. Their
small entries at most three are

| t | decoded heights removed by subtracting three | numerical entries |
| ---: | --- | --- |
| 0 | 1,2 | 1,3 |
| 1 | 1 | 3 |
| 2 | 1,2 | 2,3 |

Let `d=(2,1,2)`. The identity

    F_t(k+d_t)-3=F_(t+1 mod3)(k), k>=0

holds, using `F_0(k+5)-9=F_0(k)` at the final phase.

**Forward parser.** On nonempty U_t, remove one tallest numerical row,
of decoded height H. Record, for each `1<=h<=d_t`, the number n_h of
remaining rows of decoded height h. Remove those small rows. Subtract
three from every surviving numerical row, equivalently subtract d_t
from its decoded height. Call the inner object V. Recurse at the next
phase until empty. Phase is recursion depth modulo three and is never
an external choice.

**Proved, author-only.** V belongs to U_(t+1). Adjacent surviving height
differences are unchanged. For its bottom height, if some small row was
removed, the old bottom surviving height is at most `d_t+4`, so its new
height is at most four. If no small row was removed, its old terminal
height was already at most four. Removing the top row creates no new
gap above a retained row. Thus every phase membership condition holds.
This is exactly removal of the first ordinary Durfee hook of the modular
diagram: all retained cells lost a full cell of three; shorter rows
contribute their one/two/three terminal cell and then vanish.

**Exact inverse/image.** Given t, H, nonnegative integer counts n_h, and
inner V in the next phase, restore d_t to all its decoded heights, append
n_h copies of each small h, and append H. The data are admitted iff
`H>0`, H is at least every other restored height, and the resulting tuple
is literal U_t. These are intrinsic finite predicates. Reversing the
parser then removes exactly one H and the displayed small multiplicities,
recovering V and the same data; reversing after a forward parse restores
every original multiplicity. Ties at H introduce no choice because equal
rows are indistinguishable.

The exact weight recurrence, with `m=length(V)`, is

    |U_t|=|V|+F_t(H)+3m+sum_(h=1..d_t) n_h F_t(h).

Every removed hook has positive weight and removes at least one row;
both recursion and reconstruction terminate after finitely many rows.
The complete sequence is lossless ordered boundary data. It is a
canonical source parser, not a literal C object: a full construction must
translate this recursive grammar into the C a/b cores and mu/nu arms,
recovering hook phases and interactions from the actual C output. No such
translation or full image equivalence is claimed.

## Resource and assurance boundary (final context handoff)

The coordinator approved one source-representation pilot through weight
twelve, explicitly outside the cross-domain candidate slots. The written
context definition, script and freeze were pinned before execution in
`.runs/rr007/a-context-hook-pin.json`. The script is
`.runs/rr007/a-context-hook.py`; its pinned SHA-256 is
`19ddc888bb85a4b6493be931e22d1b3b30c379ace5bab26f7a85c27df08d32b1`.

**Empirical exact finite check:** the pilot passed with 59, 18 and 46
objects including empty in phases zero, one and two respectively. The
nonempty forward domains and admitted reverse hook-data domains had
exactly 58, 17 and 45 objects respectively. These are separate phase-domain
counts, not assertions of equality with KR1 counts. All constructed outer,
inner and inverse-reconstructed objects had actual weight at most twelve.
The check verified membership, the weight recurrence, both inverse
identities and exhaustive admission of reverse data through that bound.
It did not run the rank-one C parser or any new cross-domain map.

Receipt `.runs/rr007/a-context-hook-pilot12.receipt.json` records elapsed
child time `0.06977775000268593` seconds and observed peak child RSS
`15,958,016` bytes. RSS is a post-exit observation, not a hard transient
limit. No extension through thirty was requested or run. The finite check
supports transcription; universal assurance remains the written argument
at author-only level, pending separate criticism.

All subprocess reads used the fresh RR007 meter, apart from one initial
`pwd` command, which performed no mathematical analysis. No mathematical
script beyond that bounded auxiliary pilot, provider, new dependency,
source retrieval, nested agent, external message or publication was used
by this worker. The displayed
examples are symbolic calculations, with any larger weights explicitly
identified and never newly executed. The U–C candidate slots
remain untouched by this worker. All positive claims await distinct
criticism; none is a formal certificate or a full KR1 result.
