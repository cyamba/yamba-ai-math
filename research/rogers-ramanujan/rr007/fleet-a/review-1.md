# RR007 Fleet A: distinct initial semantic review

Reviewer: `critic-a`, the distinct critic role/profile. Completed 24 October
2026 after the initial author and context artifacts were closed. This is
one semantic review round, not statistical error independence, formal
certification, or source reinspection. No network opens were allocated or
used. The review applies to the exact pinned definitions below; it does
not revise A1–A3 or reopen any old ledger.

**Verdict: supported for the explicitly restricted theorems and the
one-sided source representations; incomplete for full KR1.** No
counterexample to a retained A1–A3 claim was found. The `proved` claims
accepted here have complete elementary arguments and distinct semantic
review, with the inherited root characterization qualified below. The
finite trials are separately labeled **empirical exact finite checks**.
No Lean/formal run or novelty claim is made.

## 1. A1–A3: accepted exact partial bijections

The literal C objects are `(a,b,mu,nu)` with nonnegative counts, exact-length
nonnegative ascending vectors, and weight
`Q(a,b)+sum(mu)+3sum(nu)`, where `Q=a²+3ab+3b²`. Literal U is a finite
descending positive numerical tuple `F(h_i)`, with
`F(5q+r)=9q+(0,1,3,6,8)[r]`, and every decoded-height drop, including the
terminal drop to zero, in `0..4`. Empty objects are included where stated.
All quantifiers below range over arbitrary finite objects, not a bound.

* **A1 accepted, proved with distinct semantic review:** all C with
  `a=2,b=0`, onto exactly the five intrinsic U families in
  [A1](candidates/a1-two-singles.md).
* **A2 accepted, proved with distinct semantic review:** all C with
  `a in {0,1}`, every `b`, onto exactly its stated complete-level
  multiplicity image in [A2](candidates/a2-zero-or-one-single.md).
* **A3 accepted, proved with distinct semantic review:** the disjoint
  union of A1, A2, all `a=3,b=0`, and all `a=2,b>=1,mu_1=0`, onto
  precisely the intrinsic union in [A3](candidates/a3-hook-and-wall.md).
  This includes every U of the stated modular rank at most one. Its
  image also contains higher ranks; it is a proper partial map.

Here is the audit of the load-bearing steps.

For A1, the arithmetic cases for `k=mu_1` are exhaustive and disjoint:
zero; positive residue one; residue two; the exceptional three; and the
remaining positive residue-zero integers. Their output supports/markers
distinguish the five branches; their one/six counts determine the stated
parameters uniquely. For marker nine the mandatory one gives decoded
drop `5-1=4`; omitting it would fail. For marker ten the mandatory six
gives `6-3=3`. The remaining supports have valid terminal and intervening
drops as well. Direct substitution in every displayed row gives
`4+2k+s`. Recovering the branch and counts and substituting back proves
both identities on the entire asserted domains. Finite scans and finite
output multiplicities prove termination. The main theorem does not need
any strip-normal-form assertion.

For A2, conjugating an ascending lambda of exact length b gives top V
multiplicity `lambda_1`, and the multiplicity of level k<b is an adjacent
lambda difference (in reversed index order). Thus its conditions are
exactly `c_b>=a+1` and `c_k>=2` below the top, with no absent level.
Conversely these conditions imply nonnegative ascending
`nu_j=lambda_j-(2j-1+a)`, including `b=1`. Presence of ones determines a;
their count minus one determines its sole mu coordinate. Empty V and
empty U cause no ambiguity. Conjugation twice and these subtractions
prove both identities and exact image membership. All consecutive
multiple-of-three levels occur; their decoded gaps are one or two, and
the bottom three has height two. Optional ones have height one. Hence
every image is literal U. Its weight is
`3b²+3ab+3sum(nu)+a+sum(mu)`; since `a²=a` this is the C weight.

For A3's third-single rows, `y mod 3`, then the zero/nonzero tests on x
and y, partition all `x,y,z>=0`. The output markers 8,10,9,12, or the
six/one-three pattern distinguish the cases. The inverses recover
`(x,y)=(t-1,3m+1),(t-1,3m+2),(0,3(m-1)),(t,0),(t+1,3m)` respectively.
Here m is the actual six count and t the actual three count. In the
marker12 case `m>=1` is essential; `x=1` permits zero threes and is valid
because the drop from height seven to the mandatory height three is
four. Marker10 without sixes still has a mandatory three, giving drop
four. Marker9 has a mandatory three. These facts check the extreme
tails, not just the interior of the tables. Each displayed numerical
weight simplifies to `9+3x+2y+z`. Counting and substitution therefore
give both identities for every third-single object.

For the wall, conjugation translates `lambda_1=1` and all subsequent
gaps at least two into `c_B=1` and `c_k>=2` for k<B. Positive b is
equivalent to `B>=2`; ones recover s. Subtracting `2j+1` from
`lambda_(j+1)` gives nonnegative ascending nu, including the `b=1`
boundary. No extra gap condition is needed there. The size is
`3(b+1)²+3sum(nu)+s+1=Q(2,b)+s+3sum(nu)`. Literal validity follows
from complete consecutive levels as for A2. The conjugation involution
and recovered one count establish exact image and both inverse
identities. All conjugations, scans and reconstructions are finite.

Disjointness is universal. A1 either uses a nonmultiple marker, lacks
three, or has exactly one three with ones; its nine branch lacks six.
A2 requires complete levels and, if it has ones, top multiplicity at
least two. Each new third-single branch either has a nonmultiple marker,
exactly one three below six, lacks six below nine, or lacks nine below
twelve. The wall has ones, complete levels, top multiplicity one, and
at least two threes. These certificates exclude every cross-sector
overlap, including the marker12 case with no threes. The C sectors are
also disjoint by a,b and the first-mu test. No source priority is used.

For one-hook coverage, the exact definition is
`D=max({j>=1:u_j>3(j-1)} union {0})`; it is not the alternate weak
threshold sometimes used for a different statistic. For nonempty U,
`D=1` is equivalent to `u_2<=3`. Thus either the object uses only 3/1,
or it has exactly one larger top. Terminal validity and the gap to a
height at most two restrict that top to 6,8,9,10. A nine needs a lower
row and a ten needs a three. For a 3/1 object, zero/one/multiple threes
and presence of ones select the A1/A2 rows in the context table. For a
six top, the cases of zero, one, or at least two threes select A1,
third-single, or the A2/wall split according to presence of ones.
Eight, nine and ten select the remaining displayed A1/third-single
rows. This is exhaustive and disjoint and proves inclusion of the
entire one-hook sector, independently of the finite census.

## 2. Source encodings: accepted within their one-sided scope

**G1 accepted, proved with distinct semantic review.** For every positive
h, the row `P(h)` is nonzero, calibrated by exactly one residue pattern,
and `sum P(h)=F(h)`. Coordinate monotonicity gives an ordinary plane
partition. From its third coordinate, `floor(P_3/3)` recovers q; the
pattern recovers r. Periodicity adds `(3,3,3)` after five heights. A
height difference at least five therefore gives minimum coordinate
drop at least three. A height difference at most four gives drops at
most three with at least one strictly smaller, hence minimum at most
two. This proves the exact terminal-inclusive gap predicate and both
inverse identities, without discarding common row order or padding.

**G2 accepted, proved with distinct semantic review.** The phase identity
`F_t(k+d_t)-3=F_(t+1 mod3)(k)` holds for `c=(0,2,3)`, `d=(2,1,2)`;
the final transition is exactly the five-height/nine-weight period of F.
The stated small heights are precisely the positive rows removed on
subtracting three. After removal of a top row and all small rows,
surviving decoded gaps are unchanged. If small rows were present, the
bottom survivor had height at most `d_t+4`; otherwise its old terminal
height was at most four. Its shifted terminal height is therefore at
most four in either case. The inner object belongs to the next phase.

For reverse data, adding d to inner heights produces heights strictly
above the recorded small range. Appending exactly the recorded small
multiplicities and a maximal positive H therefore makes the next parse
remove exactly one H and those same small rows. Ties at H are
indistinguishable equal rows, so introduce no choice. The finite
literal-membership test is the exact remaining admission predicate.
Conversely this reversal reconstructs each source multiplicity. The
weight recurrence follows term by term: every retained row loses three,
and the top/small rows have their displayed weights. At least one row
is removed per recursion, giving termination. This is a complete
lossless grammar of U_t; it is not an F_C image theorem.

**L1 accepted, proved with distinct semantic review.** In ascending
heights an allowed increment in `0..4` crosses a multiple of five iff
the residue decreases. Equal residues force zero increment. Beginning
from height zero and a nonzero first residue, induction gives exactly
`h_i=5d_i+r_i`. Conversely this formula gives each increment in `0..4`
and positive heights. Expanding `F(h_i)=9d_i+p[r_i]` gives the stated
descent-weight formula by a finite interchange of sums. Both encodings
and all inverse parameters are intrinsic finite words.

**L2 accepted as a complete gap-coordinate rewriting of the inherited
RR006 F_C characterization**, not as a fresh independent re-proof of
that root characterization. Each nonnegative gap contributes once to
every succeeding coordinate; hence its cost is `a-i+1` or
`3(b-j+1)`. The displayed forced zero gaps, bounded delta, exceptional
`a=2,b=0` k range, and free costs follow exactly by substitution in the
named RR006 branches. Cumulative summation is the inverse. This
qualification also applies when the no-go arguments below invoke F_C
membership. No equivalence of the complete U grammar and these C
shells has been proved.

## 3. Obstructions: accepted only with their exact quantifiers

**L3 accepted, proved with distinct semantic review, conditional only on
the named inherited root characterization.** Each row's adjacent sheet
difference is at most one, so successive sheet Durfee ranks differ by
zero or one. Durfee squares in the three sheets contribute disjoint
volume, at least `D_1²+D_2²+D_3²`. At weight at most417, `D_1>=13`
would force at least `169+144+121=434`, impossible. There are at most
one rank triple at `D_1=0`, three at one, and four at each of two
through twelve: 48 total. The 49 zero-arm F_C objects with `3<=a<=9`,
`1<=b<=7` have distinct count pairs and weight at most417. A
weight-preserving surjection whose count pair depends only on the
rank triple would need at least49 different triples. This is the
contradiction. No object at weight417 or434 was newly executed. The
proof excludes this statistic-based recovery class, not all richer
boundaries or a universal bijection.

**L4 accepted, proved with distinct semantic review.** After all-one
strings are excluded, the literal rank-one classification used above
gives exactly the five terms in G and the subtraction of the empty
nine tail. The four profiles with `b+floor(a/2)=1` give exactly H.
Putting G over `(1-q)(1-q²)(1-q³)` gives numerator
`q³-q⁵+q⁶-q¹⁴`; H gives `q³-q⁵+q⁶`. Thus the exact difference stated
in the author artifact follows by polynomial arithmetic. This rules
out that sector invariant, not arbitrary hook interactions. The first
difference14 is a symbolic coefficient consequence, not a new trial.

The area collision at12 and greedy-corner collision at11 are verified
by the displayed calibrated rows and gap tests. The independent-union
collision at13 gives two literal distinct C preimages of the same U,
so priority cannot make that rule injective. The contour obstruction
at19 exhausts precisely the positive length-two, sum-six gap-two
lambda possibilities `(1,5),(2,4)`, both already occupied as stated.
Its conclusion is confined to that contour/one-tail class. These are
valid negative results; they are not general impossibility theorems.
The boundary slide has an exact inverse membership test and weight
identity `8+1=9`; it is an accepted source involution, with no global
C interpretation promoted by this review.

## 4. Old direct gap/C endpoint: separately reviewed formulation

**Accepted, proved with distinct semantic review:** the direct formulas
in [RR003 endpoint-cluster-merge.md](../../rr003/endpoint-cluster-merge.md)
give a universal weight-preserving mutually inverse map between all
literal ascending KR1 gap partitions and all literal C. This review
is new RR007 evidence; the old file, ledgers and prior author-only
labels are not rewritten. The precise equivalence to source move
descriptions and the cited primary theorem was not reinspected.

Here is the full logical audit. Close pairs cannot overlap because
three parts in two overlapping close pairs span at most two, violating
the distance-two gap. A close pair's allowed sum gives uniquely
`P_(2r)=(3r+1,3r+2)` or `P_(2r+1)=(3r+3,3r+3)`. All remaining atoms
are singles. Checking the adjacent pair boundary gives precisely
`s<=L(l)` on its left, `s>=R(l)` on its right, and `m>=l+2` between
successive pair atoms. Singles separated by no pair differ by at
least two. Conversely these atom conditions imply the literal
adjacent-sum and distance-two requirements: a triple containing a
pair is handled by its boundary, while three singles span at least
four. The displayed L,R formulas also give
`L(l+2)=L(l)+3`, `R(l+2)=R(l)+3`, adjacent L increments at most two,
and `R(l)-3=L(l+1)+1`.

Extraction produces ascending nonnegative arms. Two successive singles
with h intervening pairs differ by at least `3h+2`: for h>0 use the
left/right pair bounds and a rise of at least two pair levels per
successive pair. Subtracting `3q+2i+1` therefore leaves ascending mu.
Before the first single, q pairs force its value at least `3q+1`.
For pairs with h intervening singles, if their level difference were
at most `h+1`, the L-increment bound and `R-L>=5` would imply
`L(m)-R(l)<=2h-3`; the h singles require at least `2h-2`, a
contradiction. Thus subtraction of `2j+z` leaves ascending nu. If h
singles precede the first pair, then `L(l)>=2h-1` and
`L(l)<=2l-1`, giving `l>=h`. Empty vectors need no first-coordinate
argument. All lengths, zero coordinates and positive parts are retained.

The merge consumes one arm coordinate at each step. Successive singles
are separated by at least two and successive pair levels by at least
two, directly from ascending arms. If a selected single is immediately
followed by a pair, the single-selection threshold is precisely its
needed left bound: the prospective pair level rises by one after the
single. If a pair is immediately followed by a single, its failed
single threshold says `S>L(l+1)`. The single after that pair is `S+3`,
which is at least `R(l)` by the displayed identity. This proves every
atom boundary, including when one arm becomes exhausted, and hence
literal validity of every merged output.

The proof also checks nonadjacent competing atoms. If the next actual
atom is a single and the next pair follows h>=1 singles, that pair's
level is `l+h`; the last single is at least `S+2(h-1)` and at most
`L(l+h)`. The L-increment bound yields `S<=L(l+1)`, the merge's
single decision. If the next atom is a pair and the next single
follows h>=1 pairs, that single has value `S+3h`; the last intervening
pair has level at least `l+2(h-1)` and right bound at least
`R(l)+3(h-1)`. Consequently `S>=R(l)-3=L(l+1)+1`, the pair decision.
Induction recovers the entire original atom word, values and levels.
For the other identity, the merge formulas make each extraction
coordinate exactly the supplied coordinate, since the now-valid
output has precisely those nonoverlapping close pairs. Both inverse
identities follow without a counting identity.

Finally each pair has size `3(l+1)`. Every single/pair combination has
exactly one order, so `sum q_i+sum z_j=ab`. Substitution in the two
extraction sums gives total weight `Q(a,b)+sum(mu)+3sum(nu)`.
Extraction scans finitely many parts and merge consumes a coordinate
at every iteration, proving termination. The reviewed Python file
implements exactly these formulas; it has no top-level run. It was
read, not imported. No U/B endpoint or full A/B composition was
submitted or certified by this endpoint audit.

## 5. Evidence, remaining gap and next exact obligation

The critic's own check uses literal definitions and independent
enumerators, with no imports of `kr1`, `rr005_chains`, author trial
scripts, or legacy endpoint modules. It checks all actual U/C inputs
and outputs through the bound, not only proposed forward rows. All
admitted reverse phase-hook data are exhaustively checked through
their nonnegative weight recurrence. Its sheet/descent checks are
forward/inverse transcription checks on the complete literal U
enumeration; their universal word/image claims rest on the arguments
above. The own check is pinned before its pilot in
[critic-a-freeze.json](critic-a-freeze.json).

| Named frozen run | Bound | Literal U/C | A1/A2/A3 | Rank<=1 including empty | Phase sets / admitted reverse |
| --- | ---: | ---: | --- | ---: | --- |
| `a-critic-literal-pilot12` | 12 | 59/59 | 25/27/59 | 58 | 59,18,46 / 58,17,45 |
| `a-critic-literal-through30` | 30 | 1,393/1,393 | 196/206/874 | 547 | 1,393,346,1,196 / 1,392,345,1,195 |

The root explicitly approved the unchanged named thirty extension at
21:18:06 UTC after receiving pilot/hash evidence. The check SHA-256 is
`6c6be584e6da5c29fb85e95eb749faaa7cda39f26d51b8fdabecca0cf2297984`.
The pilot used 0.05499304199474864 seconds and observed peak RSS
21,512,192 bytes; the extension used 0.32489966601133347 seconds and
27,508,736 bytes. All A3 branches were reached by thirty. Its U cohorts
were 29 distinct/845 repeated; C within-vector increment cohorts were
695/179. These are different predicates. A3's874 includes A1's196 and
A2's206 and cannot be added to them, the old baseline, or Fleet B.

The separate old-endpoint pilot is pinned in
[critic-a-endpoint-freeze.json](critic-a-endpoint-freeze.json), own script
SHA-256 `8ec8385e9a57e059c482422f84654a8d532ad79488fa0b655e4412a9878ab4d4`.
`a-critic-endpoint-pilot12` passed on all59 literal gap/C objects per
side, both identities and weight, using 0.07315937499515712 seconds
and observed peak RSS21,381,120 bytes. Gap distinct/repeated cohorts
were56/3; C increment cohorts47/12. The endpoint check imports only
the critic's own guarded literal-definitions module, not old research
code. No endpoint extension was requested or run. Raw rows and meter
receipts are in `.runs/rr007`; peak RSS is post-exit observation, not
a hard transient bound. Every critic subprocess read/check was metered
as `critic-a`; no new dependency, external action, source retrieval,
above-thirty control, or old high-weight fixture was used.

**Full KR1 remains incomplete.** A3 excludes every `a=2,b>=1` object
with positive first mu. The smallest excluded datum is
`(2,1,(1,1),(0))`, weight15: all omitted higher-single profiles start
at least16, while this mixed profile has base13 and needs at least
two increment units. The frozen map rejects it. Count agreement at
twelve cannot establish coverage. The unfrozen first-positive-wall
clue was read as a prospective direction, not executed, incorporated,
or accepted as a theorem by this review.

One high-value next obligation is a **paper-only** intrinsic operation W
on the numerical U / three-phase hook grammar that adds weight two and
raises the common first increment for a two-single mixed object. Starting
from the existing wall
`U0(b,s,nu)=3*(1,3+nu_1,...,2b+1+nu_b)^T union 1^(s+1)`, require
`W^k(U0)` to encode `(2,b,(k,k+s),nu)` for all `b>=1,k,s>=0` and all
ascending nu. A valid result needs an intrinsic image/orbit predicate,
an inverse lowering operator whose weight decreases by two until the
unique k-zero wall is reached, recovery of b,s,nu there, both identities,
and disjointness of different orbits/layers and the other retained A3
sectors. It may use the complete phased hook boundary but cannot retain
external k, a trace or free color. An obstruction or failed derivation
must be preserved precisely. No fourth finite candidate, silent A3
extension, altered pin, or new trial is authorized by this suggestion.

No retained claim requires a corrective author revision. The next stage
would address the missing construction, with its own distinct final
review and unchanged resource/candidate boundaries. All novelty status
remains **unverified**.
