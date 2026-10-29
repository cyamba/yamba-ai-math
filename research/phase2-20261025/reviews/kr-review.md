# Phase 2 KR distinct review — initial frozen packets

25 October 2026, Europe/Stockholm. Reviewer is distinct from both KR authors;
this does not assert statistically independent model errors. **Verdict:
conditional** for the combined packet because one recursive geometric claim is
refuted. The new restricted H2 theorem T1 and C-only reductions T2 are
**proved with distinct ordinary semantic review**, as scoped below. Full KR1
and the requested complete a3/a4/a5 unification remain **incomplete**. No formal
proof checker, source-equivalence certification or novelty certification is
claimed. No prior ledger has been reopened or edited.

Reviewed input freezes: sectors `2726b54ebc29f57b0286c09cb3a660bf008c84ced94f9051256ebceee7342653`
(28 pins), recursive `6007a54c5a8e33fb4d10a6e021ad6ff6257b7dbb4b6e077733316c600e92b972`
(13 pins). All pins matched before review. Exact dependency and final integrity
records are in `kr-dependencies.json`. This verdict concerns those original
packets, not any later correction. A reserved author correction/final review
may resolve finding 1; it is not presumed accepted here.

## 1. High: dropping quotient zeros invalidates the claimed global range

**Target:** recursive `author.md`, candidate 3: child terminal height at most
one, hence child U=(3) globally absent. **Status: refuted.** Parent
`U=(10,3)` has decoded heights `(6,2)`, gap four and terminal two. Its weight
is 13. Quotient heights are `(2,0)`; removing zero leaves child `(3)`.
The original author's bounded U-cut implementation does not enforce the false
range exclusion; this is an argument error, not a failure of its finite
membership counts.

My independent geometry check passed through 12, then failed through 30 on
that exact upstream exclusion. The failed invocation, v1 script and precise
witness are preserved in `kr-geometriccheck-v1.py`,
`kr-geometric-v1-failure.json` and meter receipt `kr-critic-geometry30`.
The reported universal no-parent conclusion for child `(3)` must be withdrawn.

**Decisive repair proposal, pending a separately frozen author correction:**
the final positive quotient has height at most two, because its parent height
is either terminal at most four or followed by a height at most two, with a
drop at most four. Thus that parent height is at most six. A parent yielding
exact child `(3)` needs a height at least six, costing at least ten. It also
needs a valid tail: any such top is not terminal, and the next height is at
least two, costing at least three. Consequently minimum parent cost is 13,
attained by `(10,3)`. This leaves the particular weight-nine commutation
obstruction intact, with a weight argument instead of a global range argument.
A genuinely absent child is `(6)`, decoded terminal height three. The exact
C grammar requires it from parent `(0,2,(),(1,1))` of weight 18, whose child
is `(2,0,(1,1),())` and whose retained H1 child value is `(6)`.

My version-2 check records these repairs as independently tested proposals;
it does not silently replace the failed v1 or accept an unseen author revision.
The two other cut failures, lower-sheet `(8)->(2)` at eight and every-third-row
`(9,9,9,1)->(9)` at 28, are supported. For the latter, a bad terminal retained
height is at least five, requiring three initial columns of cost at least
nine and an additional positive tail. A bad internal retained drop needs
upper retained height at least six, making the first three columns alone cost
at least 30. Thus 28 is the true minimum for that fixed rule.

## 2. No defect found: T1 is an exact restricted H2 extension

**Target:** sectors T1 and `extension.py`. **Status: proved, distinct ordinary
semantic review.** Its domain is precisely the old D1 (`a<=2` or `a3,b0`),
the two common-mu b0 planes for a4/a5, and all riggings with a3,b>=49,
a4,b>=65, a5,b>=79. It does not cover all b for these a values.

The four plane languages have complete intrinsic count inverses, including
zero x,z and all compulsory one counts. Their literal weights are
`16+4x+z` and `25+5x+z`. Their ordered decoded heights have every drop and
terminal drop at most four; mandatory ones in both a5 branches supply the
bottom bridge. The four supports cannot intersect each other. Their exclusion
from the inherited images is universal: multiple 8s without a 3/6 contour,
or the 12+8 support, defeat every old isolated/mixed support; the 15+9 family
lacks both 12 and 6 required by dense or single-hole multiple contours;
the single17+9+3 family lacks the six required by its old17 hole and is not
any other old marker set. I inspected `rr003_columns.py`, `rr003_revision.py`,
`rr003_a2.py`, the A3 tags, repaired g3 and b1 phases for this classification.

For the high-b tail, quotient marker counts are multiples of `t_j=j/gcd(j,w_j)`;
dividing them recovers every quotient q_j. The distinct bit coins recover one
ordinary binary integer R; requiring R below the radix product makes mixed
division recover each residue uniquely. The guard 28 occurs exactly a-2
times and is never a multiple-of-three, quotient or bit coin. It therefore
recovers a and separates every tail from all prior g2/g3/f1 and new planes.
Full multiples 3 through 3b recover b and every nu gap by subtracting two.
Every allowed part count, including the mandatory one offset, is inspected;
there is no hidden rank, lookup of source objects, or source-history recovery.

The safe overhead bounds 298/596/966 and excesses at thresholds 303/601/973
prove nonnegative one offsets for every residue word. Since the residue
weight L is nonnegative, this does not rely on a favorable digit sample.
Direct cancellation of the guard/bit weight H gives
`3b²+3b+3sum(nu)+sum(j*d_j*q_j)+H+delta1+E+L-H`,
which is exactly `Q(a,b)+sum(mu)+3sum(nu)`.

Every added high-b marker has numerical value at most 91. At b>=31, the
full contour reaches 93, decoded height 52, while the largest added height is
51. Consecutive contour heights differ by the cycle 1,2,2. Inserted interior
heights subdivide valid gaps; optional ones give the only lower extension,
with terminal at most two. This covers all repeated quotient multiplicities,
empty bit sets and zero nu gaps. It proves U validity without constructing an
above-40 example. I did not instantiate or enumerate any high-b tail object.

Conversely every inverse-accepted tail reconstructs exactly its original
support/counts; integer quotient/remainder uniqueness proves both identities.
Only finite scans, divisions and cumulative sums occur. The tail source and
image sectors are mutually disjoint via guard count and contour top. The
plane inverses have the same exact reconstruction property.

The inherited H1 is the reviewed alternating-path construction. Its new
transcription uses the canonical guarded A3 module and tracked g2 dependencies,
not ignored raw inputs. Its source predicates, f1/g inverses, forward priority
and reverse rejection match the reviewed argument. Repeated vertices would
cancel successive injective edges back to an impossible old/new source
identification; finite fixed-weight fibers force exit or rejection. Crucially,
a target-only component may reject: H1's image is not the union of f1 and g.
Every H1 output is a last f1 or g2/g3 value. The proved disjointness above
therefore makes H2 a direct union preserving H1 literally, despite its more
general executable splice wrapper. This proves the exact stated image and
both inverse identities universally, conditional only on the explicitly
inherited separately reviewed g2/A3/g3/f1 premises, not on coefficient counts.

## 3. No defect found: T2 and the triadic grammar are C-only theorems

**Target:** reductions T2, `reductions.py`, triadic implementation and lattice
interpretation. **Status: proved, distinct ordinary semantic review** of new
T2 and the new transcription/geometric reformulation. The original triadic
paper lemma retains its earlier RR007 distinct-review attribution.

For all a in{3,4,5}, expansion gives
`Q(a,b)-Q(a-2,b+1)=a-1`. Dividing delta3 by B=b+1 moves its quotient into
the first child nu value and stores k in `[0,B)`. Subtracting that value from
later child nu entries is a complete inverse because the child arm is sorted.
The a3/a4 child mu gaps and their free boundary digit recover every parent gap.
For a5, the child's first mu entry is exactly 4t and must be divisible by four;
the stored r in `[0,3)` uniquely recovers delta4=3t+r. Its cost identity is
`4delta4=3(4t)+4r`. These prove the three displayed excess formulas and both
identities on their complete child/boundary languages, including all zeros,
ties and all b. The implementation rejects negative boundary gaps, bad k,
bad r and bad a5 divisibility. It uses validated literal C child values.

For the triadic grammar, eta's reverse gaps recover every e_j, while trits
recover delta_(3j)=3e_j+t_j. The other ordered gaps are stored individually;
child dimensions and r recover a,b. Expanding Q and the weighted gap sums
proves the claimed residual identity. Forbidding an empty-above-empty node
removes the only redundant terminal. Two dimension steps divide both original
dimensions by three with floors, so zero residual does not threaten termination.
I inspected the full source and its admission checks, not merely the count.

The Euclidean embedding has squared norm Q; conjugating `(x,y)->(3y,x)` by
that embedding and dividing by sqrt3 gives the displayed reflection matrix,
with axis 15 degrees and square I. This is an exact reformulation of the core
identity. It supplies no U operation. Neither T2 nor the recursive grammar
becomes a U/C map by these algebraic facts; k/r insertion and a valid complete
U cut/gluing remain missing.

## 4. Material incompleteness: finite success does not supply missing sectors

**Target:** complete Phase 2 unification/full KR1. **Status: incomplete.**
The author reports that status correctly. My independent weighted-gap C
generator, direct decoded flat-path U generator and ordinary-partition filters
for literal A/B give 59/1393/5461 objects at cumulative ceilings 12/30/40.
They are not defined by the maps under review. I exercised actual endpoint
implementations in both directions on the full literal A/B sets. This is fresh
finite implementation evidence; endpoint paper assurance and source-equivalence
questions remain attributed to prior reviews.

| Through40 | Full denominator | H1 accepted | H2 accepted |
|---|---:|---:|---:|
| Total | 5461 | 2889 | 3014 |
| A distinct/repeated | 4684/777 | 2326/563 | 2451/563 |
| B distinct/repeated | 325/5136 | 64/2825 | 70/2944 |

Every accepted C/U pair passed weight, literal membership and both identities;
every U reverse acceptance/rejection was checked against the independently
generated forward image. Exactly 2447 U values are rejected by H2 through40.
An independent enumeration of the **entire** allowed reduction child/boundary
language gives exactly 1891 a3,1398 a4,408 a5 parents through40. This reverse
enumeration is not restricted to forward-produced child records. The imported
author bottom-up grammar generator likewise matches my independently generated
C values at all three gates; its reverse enumerator is disclosed as author
code rather than falsely described as a second critic implementation.

First missing source `(4,0,(0,0,1,1),())` and first rejected U `(10,8)` both
have weight18. The missing families include a3,b1..48; a4,b1..64 and its
non-plane b0 riggings; a5,b1..78 and its non-plane b0 riggings; and every
a>=6. No full U/C recursion or total A/B algorithm is established. The new
high-b theorem has no executed high-b instance; its assurance is the symbolic
argument in finding 2, not the through40 census.

## Resource and integrity record

All eight reviewer mathematical subprocesses used the shared meter with
timeout180 and stayed below the assigned 200-second reviewer allowance.
Exact wall/CPU/RSS totals, including the failed first geometry30 call, are in
`kr-resource-use.json`. No numerical KR input/output exceeded weight40. No
external source, message, provider, dependency installation or nested agent was
used. File reads and pin work are elapsed preparation, not numerical subprocess
time. Old ledgers remain immutable. The final pin check covers all 41 original
author dependency entries; any later revision needs its own final review.
