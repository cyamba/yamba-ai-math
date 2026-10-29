# RR007 Fleet A: final distinct paper review

Reviewer: `critic-a`, reserved final critic invocation. The author revision
was closed and pinned at21:56:53 UTC on24 October2026. This review reads
the closed text and exact local dependencies; it executes no new finite
trial, author/external research module, endpoint, formal checker or
above-thirty control. No source open, dependency, agent or external
message is added. Earlier reviews, definitions, pins and closed ledgers
remain unchanged.

**Verdict: supported for the restricted paper algorithms R7/H and the
stronger H1/W corollary; incomplete for full KR1.** The load-bearing
claims have complete elementary arguments and distinct semantic review
as specified below. They have no new implementation or finite-run
evidence. This upgrades their paper-proof assurance here, without
retroactively editing the old author-only records. It is not a formal
certificate or novelty verification.

## 1. Accepted: complete old g2 on all a<=2, with an exact recognizer

**Proved, distinct semantic review.** I reviewed the whole direct
definition, including the earlier first/second maps and the final
author-only holes, in the pinned `rr003_columns.py`, `rr003_revision.py`,
`rr003_a2.py`, round-two proposal and final revision. All were read as
text, not imported. The theorem accepted is an explicit weight-preserving
bijection from every literal C with `a<=2` onto its stated intrinsic
subset of literal U. It is neither a full U image theorem nor a
source-move equivalence theorem.

For the first map, let `delta_j=nu_(b-j+1)-nu_(b-j)` and let D_b have
two copies of each3j. These deltas are arbitrary nonnegative integers;
`sum(j*delta_j)=sum(nu)`, and reversed cumulative summation is their
unique exact-length inverse. The four baselines have weights
`3b²`, `3b²+3b+1+mu_1`, `3b²+6b+4+s`, and
`3b²+6b+6+s`, respectively for a=0, a=1, and a=2 with k=0,1.
Thus adding delta columns gives precisely the literal C weight.
The empty/all-one cases are explicit. Otherwise complete support,
the one count, and top multiplicity distinguish a=0, a=1, k=0.
The k=1 output has a singleton top and exactly the missing penultimate
level; its lower counts are at least two. These tests recover b and
the baseline uniquely. A two-level jump among multiples of three has
decoded gap at most four, including the bare-six b=0 boundary.
All other baselines are complete levels, so literal validity follows.

The b=0 extension has exactly one8, or one9 with mandatory ones and
no3, or one9 and exactly one3. Its six count and one count recover the
quotient and tail. The compulsory one in the second case supplies the
height-five-to-height-one terminal bridge when no six is present.
The supports distinguish these branches from the first map and each
other. Their weights are respectively `8+6j+s`, `10+6j+s`, and
`12+6j+s`, exactly `4+2k+s` in the three residues of k-2.

For mixed markers, `4x+5y=k+2`, `0<=y<=3` is canonical: reducing
modulo four determines y and then x. Its nonnegative nonzero solutions
cover exactly `k>=2` except4,5,9. The dense baseline plus extra top
has size `3b²+6b`; marker size is `2k+4`. Complete multiple-of-three
support, lower multiplicities at least two, and top at least three
give the exact inverse. Removing markers and ones and subtracting
that baseline leaves precisely the arbitrary deltas. Conversely these
tests reconstruct every accepted U. Markers10 of height six can fall
to the baseline three of height two by four even at b=1; larger b
only subdivides drops. The mixed image has positive three support,
excluding the b=0 single8 image, and markers exclude the other old
supports. Neither of the other three missing k values has a canonical
nonnegative marker solution, so those domains remain disjoint.

The final holes are also sound. Their template/minimum-one weights,
before all free increments, are the following exact symbolic values:

| k | b | Weight |
| --- | --- | --- |
| 4 | 1,2; then b>=3 | 21,36; then `3b²+6b+12` |
| 5 | 1,2,3; then b>=4 | 23,38,59; then `3b²+6b+14` |
| 9 | 1,2,3,4,5; then b>=6 | 31,46,67,94,127; then `3b²+6b+22` |

Each equals `Q(2,b)+2k`. In parity branches, `nu_1=2q+r`, r=0 or1,
adds q sixes and r threes, hence weight `3nu_1`; the residual inverse
is unique. In ordinary branches delta columns give `3sum(nu)`.
Adding s ones gives exactly the total C weight.

Literal validity includes every terminal boundary. The decoded marker
heights17,19,26 are9,11,14. In their dense families the worst gaps to
the dense top occur respectively at b=3,4,6 and are four; for higher b
the markers are closer to or inside the dense interval. The exceptional
fixed supports have successive and terminal gaps at most four. Every
ordinary free column lies inside this interval and subdivides a valid
drop; parity3/6 and extra ones also subdivide permitted drops. No
unlisted terminal case is needed.

The intrinsic recognition separates all holes at every weight. The
marker-free k4,b1 branch has exactly one9, exactly one6 and at least
two3s; it fails old complete-support lower counts and the old singleton
one-hole and b=0 predicates. The k5/9,b1 branches have respectively
one/two10s, at least their fixed six counts, at most one3, and the
required minimum ones. They cannot be old mixed marker images, which
require larger three support. A single17 uses a singleton top9 to
identify b=2, otherwise a dense top to identify b>=3; two17s identify
k9,b2. A single19 with singleton top12 distinguishes b=2 from b=3
by absence/presence of9; a dense top identifies b>=4. A26 with one10
uses its multiplicity to identify b=3,4,5; a single26 without10 uses
the dense top for b>=6. Ordinary increments cannot change these
distinguishing exceptional tops or create the excluded9 at k5,b2.
Subtracting the unique template/minimum ones, rejecting negative or
unlisted residuals, and checking the parity range is both necessary
and sufficient. The unchanged code performs those tests. It can
initially recognize a malformed template head and then reject its
residual; it does not accept that head alone as an image certificate.

This proves exact image, both identities and finite termination for
the entire g2, including arbitrary b, repeated nu and zero padding.
The previously author-only final holes receive distinct paper review
in this document only. Old recorded finite results are not new evidence
from this stage and were not rerun.

## 2. Accepted: repaired g3 and universal disjointness from g2

**Proved, distinct semantic review.** The exact R7.3 table partitions
all `x,y,z>=0`: y=0; y=1,2; y=3 with its x/z exceptions; and the
three residue classes for y>=4. The heads mean exactly their displayed
literal multiplicities and entire supports. Extra parts, repeated
markers or unlisted12/17/etc. are rejected.

The inverse cases are exhaustive and unique. With only6/3/1, at most
one3 and `2q+r>=3` recover `x=2q+r-3,y=0`. Single8/10 with positive
threes has either no6 and one/two3s, or exactly one6 and positive3;
these recover y=1/2 and x. The remaining single10,one6,no3 case
recovers `x=0,y=3,z=#1+1`, while the separate `(9,6)` without ones
recovers z=0. The10+8 head recovers the y=3,x>=1 split from its six
and three counts. The9+8 head recovers `q=#6+1,y=3q+1,x=#3`.
The10+9 head with some6 or3 recovers `y=3q+2`; bare10+9 is rejected.
Two9s with positive ones and no6/3 recover the exact `y=5,x=0`
exception, subtracting its one compulsory one.

The last branch has at least two9s and positive three support. With
no6 its exact count of9s is two and `M=0,T=#3`. Otherwise its
predicate is `9^r6^p3^t`, `r>=2,p,t>=1,min(p,t)=1`, and the inverse
is `l=r-2,M=p+l,T=t+l`. Then
`min(M-1,T-1)=l+min(p-1,t-1)=l`. This proves both compositions,
including the tie p=t=1, and recovers `q=M+2,x=T-1` uniquely. All
ones in this branch are exactly the free z ones. This normalized
branch is disjoint from the exceptional two9/no3 branch and all
single-marker heads. Thus the entire table has an exact image test
and both inverse identities.

All images are literal U. The largest displayed decoded height is six,
and the potentially dangerous10+9 head always has6 or3 below it.
Its exception has two9s and a mandatory one. A10/8 head ends at
height four or has a lower6/3; a single10 has a three or six bridge.
Repeated9s in the normalized branch have6/3 below. Every remaining
terminal or intervening drop is at most four. Direct substitution in
each row gives `9+3x+2y+z`. The last normalization uses `6+3=9`,
and the exceptional y=3,x=0,z>=1 row has size `16+(z-1)=15+z`.
All procedures are finite counts, arithmetic and reconstruction.

Disjointness from the entire g2 follows by its complete classification,
not by an untested small-weight sample. The y=0 image has at most
one3 and, if it has no3, at least two6s; it is neither an old dense
lower-count image nor a singleton one-hole image. The single8/10
families have at most two3s when no6 is present, and exactly one6
otherwise, violating the corresponding old mixed top requirement.
Their positive3 excludes the old single8 carrier; the10/6 exception
has only one6, excluding the parity k5,b1 hole. The bare9/6 head
has no mandatory one and no required three support. The10/8 head
has insufficient lower support for a mixed baseline. Heads9/8 and
10/9 have exactly one9, whereas an old mixed image containing level9
requires top count at least three. The exceptional two9/no3 family
has none of the old singleton9 support/counts. The final normalized
branch either omits6 with two9s, violating the old singleton one-hole
rule, or has a lower6/3 multiplicity one, violating the old complete
support test. Multiple9s exclude old b=0 and k4,b1 carriers. No g3
image has17,19,26 or double10. This exhausts g2's possible images.

Consequently `g=g2 union g3` is an intrinsic weight-preserving
injection with exact inverse on
`D1={a<=2} union {a=3,b=0}`. No imported endpoint or coefficient
identity is required for this theorem.

## 3. Accepted: alternating extension H, all-b W, and stronger H1

**Proved, distinct semantic review.** For f=A3 its source D0 is a
subset of D1: every a=0/1, all a2,b0, all a3,b0, and the mixed
zero-first-mu wall lie there. Every component operation has the
literal domain/image and inverse reviewed above or in review-1.

On a new source d outside D0, write `u_0=g(d)` and, while possible,
`u_(i+1)=g(f^{-1}(u_i))`. These are explicit local evaluations of
the two image tests and maps at the same literal weight. A repeated
u-value would cancel g and f successively backwards. Eventually it
would identify the initial new source with an old source in D0,
impossible. The U fiber at that weight is finite, so the path exits
f(D0). No state history, rank list or enumeration is used to execute
the path. Finiteness proves termination, rather than supplying its
output by a finite matching. The stated `2^N+1` bound is a safe crude
exponential bound, not an efficiency improvement.

The reverse test is exact and total on literal U as a decision/rejection
algorithm. Initial points in f(D0) return their old source immediately.
Otherwise use g inverse when available; accept on a new source, and on
an old source move along f. If g is undefined, reject. This reverse
path cannot repeat: cancel its f/g edges backwards, and a repetition
would put its initial point in f(D0), contrary to the initial test.
The finite fixed-weight fiber therefore forces acceptance or rejection.
A component with an f-only and a g-only target and no new source is
properly rejected; the extended image is not the union of the two
images. A reverse-accepted path retraces uniquely to a new source and
its forward path exits at the original initial target. Conversely every
forward exit retraces to its original new source. These arguments prove
both identities and separate the new image from the old f image.

The literal weight is unchanged along every path and every source/target
remains in its validated domain. Thus H is a weight-preserving bijection
from D1 onto the exact reverse-accepted image and extends A3 identically.
This is a complete paper algorithm and proof. No implementation or
runtime test of the new path construction is present.

On the intrinsic X2 where `H^{-1}` returns `a=2,b>=1`, incrementing
both mu coordinates by one and applying H defines W. The inverse
decrements both precisely when k>0. Source-domain closure follows
from the entire a=2 sector of D1. Conjugation by the proved H gives
both identities, literal validity, weight change two, and unique
recovery of `k,b,s,nu`. Every lowering step reduces k until zero.
Since H fixes A3, that endpoint is exactly the original mixed wall
for the recovered b,s,nu. Different parameters or levels cannot
meet by H injectivity. This covers arbitrary repeated/equal nu and
all b, without a new free parameter or an extrapolation from b=1.

**R3 and H1 are also accepted.** The raw R1 family is internally
reversible but its extension-of-A3 claim is refuted by the recorded
weight27 collision. R3 fixes that exact problem: its phase-one
normalization has exact inverse `l=r-1,M=p+l,T=q+l`, with either
`q=0,r=1` or `q>=1,min(p,q)=1`. The same minimum identity proves
both compositions, including ties. It preserves weight and all free
ones, retains a six, and leaves a lower6/3 multiplicity one or a
missing3. It is therefore disjoint from the old dense A2/wall images
and from the other A3 support families. The other raw phases use
9+8,10+9 or two9s and are disjoint as stated.

The raw lowering boundary with two sixes depends on whether any6 or3
remains after their removal; ones are ignored. This correctly selects
the two9/mandatory-one exception even with arbitrarily many free ones.
Every raw forward substitution and this inverse recovers the adjacent
k table, and conjugating by normalization preserves both identities.
Hence the corrected b=1 map is a complete, weight-preserving intrinsic
extension of the original zero-wall. Its domain together with A3 is
still a subset D0' of D1. Applying the same proved path lemma to f1
therefore yields H1, preserving A3 and the whole corrected b=1 map;
its W agrees with R3 on b=1. This is a corollary of the same construction,
not an addition of independently counted images.

## 4. Supporting R4–R6 and the corrected 3D explanation

**R5 accepted, proved with distinct semantic review.** The calibrated
three columns form one finite coordinatewise order ideal. The chain
P(h) is increasing and injective, so inclusion of two ordered padded
boards is equivalent to entrywise domination of decoded heights.
For a numerical3v row the middle entry is v and the outer entries
are `v+epsilon(v),v-epsilon(v)` with epsilon zero precisely when
3 divides v; a numerical one gives `(1,0,0)`. Thus the complete
ordered middle slice plus the specified zero-middle notches recovers
the entire zero-wall contour, b,s and all nu, as stated. Areas alone
remain insufficient.

At `(6,3,3,1)` the existing rows' smallest positive costs are two for
raising6 to8, three for either3 to6, and two for1 to3. A new row costs
at least one, with next new-row size three. Therefore an inclusion
with total volume increase two can only raise6 to8, raise1 to3, or
append two ones. These are exactly the three valid listed boards;
each is already an A3 image of the stated source. This exhausts all
old and appended rows, proving the no-go for inclusion-only W and
its fixed-coordinate-permutation conjugates. It does not exclude
deleting/sliding cubes or a different embedding. The fusion6+3->9
has sheet-volume change `(5,3,1)->(3,3,3)` and preserves middle
volume; this is an exact interpretation, not a universal seam rule.

Root's separate `ferrers-3d-note.md` initially had a zero-/one-based
index error: it used `r-t+1` for t=0,1,2. At h=1 that would give
`(2,1,0)` and wrong volume three. The critic reported this exact
counterexample; root corrected only that explanatory note to `r-t`
and preserved the correction explicitly. I read back the corrected
note, SHA-256
`48b0f329cd0e6b9fcb25e3c8e3c2bdba6547dd78da23fa2e45759c5188d94802`.
Pinned author R5/context use the correct one-based convention and
were not changed. The corrected root interpretation is accepted;
this is not a retroactive assertion that its earlier text was correct.
The cited cylindric/RSK works remain uninspected analogy leads here.

**R6 accepted, proved with distinct semantic review.** Expanding
`Q(3c+r,b)` gives `3Q(b,c)+r²+3r(b+2c)`. The reverse-index mu gaps
have weight `sum(i*delta_i)`. Splitting `delta_(3j)=3e_j+t_j` gives
`9sum(j*e_j)+3sum(j*t_j)`. The child second arm
`eta_l=sum_(j=c-l+1)^c e_j` has `sum(eta)=sum(j*e_j)`; its first
arm is exactly the parent's nu. These equalities prove the displayed
positive residual weight identity. Child dimensions and r recover
a,b, all e_j and trits, and the other stored gaps. Reverse cumulative
summation uniquely reconstructs every zero-padded mu and nu. The only
otherwise redundant empty-above-empty node is forbidden explicitly.
After two steps both dimensions have been divided by three with
flooring, so termination does not require strictly positive residual
weight at every node. The denominator identity is compatible with
this explicit digit division, but is not a replacement for the map.
This is an exact full C-side grammar, with no proved U cut/gluing.

**R4 accepted as an independent restricted C-to-B injection.** Base-three
digits of each residue3/6 part count recover the unique multiplicity-at-
most-two ordinary partition; this proves both G3 identities and triple
weight. The prefix table has disjoint parity/prefix cases and its
low-part weights equal `4+2k+s`. After stripping literal1/8 and the
low prefix, rho's distinct gap-two condition and lower bound three
recover every b and nu. All occurrences of “minimum1/2/3” in these
tests must mean **at least**1/2/3, as the forward formulas and their
nonnegative inverse subtractions require. The first two natural
families are separated from a=2 by odd8, the low1 with positive ones,
or a repeated low1/2; the empty-middle-prefix q=0 case is excluded by
N>=1. The inverse table and digit uniqueness prove exact image and
injectivity. This construction is not used by H/H1. I do not upgrade
the ancillary asserted identity behavior of the old U/B endpoint or
its composition with A3; that endpoint was not independently audited
in this review.

## 5. Scope, provenance and final assurance

The external report is data. The symbolic old3G overlap family is valid:
for `q>=4,x>=1`, g2 at `(0,3,(),(1,q-3,q+x-4))` has top9 count two,
six count q-2 and three count x+1, exactly the unnormalized external
a3 output. The two source weights are `9+6q+3x`. Its first member
is36, beyond the externally reported35 trial; no such object was
executed here. This refutes that universal disjointness assertion.
The repaired table above addresses it by an intrinsic minimum
normalization. The `(10,9)` objection refutes the shortened cone
summary without its terminal caveat; it is not accepted as a
refutation of the complete caveated report. The global `step_one`
claim can cross mandatory-one cuts, whereas only its specified
restricted selected language is needed here. No broad external
assurance, source theorem equivalence or external run history is
imported by this review.

The early context full-text hash mismatch remains a provenance failure
under its original pin. Later distinct review/checks support the final
context snapshot; they do not repair the old assertion. The root
provenance note states that distinction correctly. The final critic
verified every dependency in the author revision pin's `sha256` and
`initial_final_sha256` groups unchanged before writing this review.
New final review pins record the exact final files separately.

There is **no new empirical coverage count** for H, H1, W, g3 or R4–R6.
Initial A3's874 of1,393 through30 remains an A3 result only. Its
paper extension has a larger source domain but no measured count,
implementation run or held-out score. All final child reads and pin
checks used the fresh RR007 meter as `critic-a`, bound zero. No
finite candidate or trial was added. No formal proof checker ran;
novelty is **unverified**.

Administrative exception: an overlong `python -c` final-pin command
failed in meter preflight before a child receipt was created. A metered
read confirmed the pin file was absent; the pin operation was moved to
the named administrative helper `.runs/rr007/a-critic-final-pin.py`.
This was no mathematical execution, and no delivery or successful pin
was claimed from the failed command.

**Full KR1 is still incomplete.** Both H and H1 have source D1 only.
The literal `(4,0,(0,0,0,0),())` at16 lies outside D1; a=3,b>=1 and
all higher sectors are also missing. The literal U=(8,8) at16 lies
outside f, f1 and g: g2's double8 mixed marker needs positive dense
three support, its b=0 carrier has only one8, and g3 has at most one8.
The exact reverse algorithm therefore rejects it immediately. These
are proper-domain/image witnesses, not new matched seeds or a claim
that every lower U has been covered. The remaining central obligation
is an exhaustive arbitrary-a U/C cut and gluing, possibly relating
the two exact recursive grammars, followed by actual implementation,
full endpoint composition and the remaining assurance obligations.
