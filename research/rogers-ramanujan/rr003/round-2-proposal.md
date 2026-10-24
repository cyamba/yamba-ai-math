# RR003 round two — zero-pair and mixed-sector common carries

**Proposed proved restricted extension**, pending the second separate semantic
review. Full U–C and residue–gap bijections remain **incomplete**. Novelty remains
**unverified**. Retain the round-one theorem and attribution without alteration.
Discovery exposure: all U,C,A,B through weight 30; explicit insertion witness
at weight 43 derived symbolically, not an enumeration ceiling extension.

## Selected domain and exact additional rules

The revised domain S'_C includes S_C, every C with a=2,b=0, and every C with
a=2,b>0 whose k=mu_1 is not 4,5,9. Only new inputs k>=2 need new formulas. Write mu=(k,k+t), t>=0, and k=3j+r+2 with j>=0 and r=0,1,2.
The new columns, in descending order, are

* r=0: (8,6^j,1^t), so k=3j+2;
* r=1: (9,6^j,1^(t+1)), so k=3j+3;
* r=2: (9,6^j,3,1^t), so k=3j+4.

The cases k=0 and k=1 remain respectively (3,1^(t+1)) and (6,1^t).
The code calls the frozen first map for S_C; the rules above handle the new
b=0 inputs. The mixed inputs use the marker rules below.
No numerical matching, search, table indexed by weight or transcript defines
any map. The three formula branches are uniform for arbitrary j,t.

## Intrinsic inverse and image separation

Validate literal U, including its terminal height. Recognize S_U first by the
frozen round-one inverse. If unsupported, remove ones and count sixes j. Recognize
exactly one of residual multisets {8}, {9} with at least one one, or {9,3}.
Recover k=3j+2,3j+3,3j+4 respectively; t is the ones count, that count minus one,
or that count respectively. Return a=2,b=0,mu=(k,k+t),nu=(). Reject everything else.

The new patterns are mutually disjoint. They are disjoint from S_U: the first
contains 8, forbidden by S_U's all-multiples-of-three-plus-ones condition. The
second has a 9 but no 3, excluding every full-support or specified one-hole
round-one branch; even j=0 cannot fit a one-hole support with its required 3.
The third has exactly one 3 and one 9, which violates all round-one lower-level
multiplicity requirements: if j=0 the only possible one-hole branch requires
at least two 3s, and if j>0 full support requires at least two 3s. Thus testing
the old inverse first neither masks nor duplicates any new input.

## Mixed-sector markers, intrinsic inverse and proof

For b>=1 and k>=2, put y=(k+2) mod 4 in {0,1,2,3} and x=(k+2-5y)/4.
Use this branch exactly when x>=0 and x+y>=1. These conditions hold precisely
for k>=2 excluding 4,5,9: direct substitution handles k=2,...,9, and writing
k+2=4q+r for k>=10 gives x=q-r>=0 (the worst r=3 first occurs at k=13).
Equivalently 4x+5y=k+2 is the canonical nonnegative solution with y<=3.
This is a formula, not a table of enumerated partition images.

Let delta be the same suffix differences of nu as in round one. Start with
2+delta_j copies of 3j for 1<=j<=b, insert one additional 3b, then x copies
of 8, y copies of 10, and t=mu_2-k ones. Decoding heights gives D(8)=4,
D(10)=6. The dense multiples-of-three support already forms a valid path
ending at height two. When b=1, the worst added jump is 6 to 2, still <5;
for b>=2 the dense support only shortens jumps. Adding these markers cannot
invalidate any existing height drop. Thus these are actual U objects.

The baseline plus extra 3b has weight 3b(b+1)+3b=3b^2+6b. Markers have
weight 8x+10y=2k+4. Ones add t. The total is Q(2,b)+2k+t+3|nu|, exactly the input weight; the delta
columns contribute 3|nu| by the telescoping identity. Every identity holds for all b,nu,t.

Intrinsic inverse: these patterns have at least two 3s and non-three marker
8 or 10. Remove those markers and ones. The remaining positive support must
be {3,...,3b} with each count at least two and the top count at least three.
Recover b from this maximum multiple of three, subtract two at every level
and a further one at b, and take reversed cumulative sums to recover nu.
Read x,y from literal marker multiplicities, require y<=3, and recover
k=4x+5y-2, t=the ones count. All recognition conditions are necessary and
sufficient, so reconstruction and decomposition are mutual inverses.

The marker patterns are disjoint from S_U because they contain 8 or 10.
They are disjoint from the b=0 new patterns: b=0 patterns with 8 have no 3;
b=0 patterns with 9 contain no 8 or 10. No prior branch is masked.
This gives intrinsic recovery of a=2,b,k,nu,mu on the stated image, not a
claim to have recovered global a,b on arbitrary U.

Mixed common carries preserve b,nu and t. For k=0 use the already proved
merge; for k=1 replace 3(b+2) by 3b and 8, of cost two. For marker states:

* y<3 and x>0: replace one 8 by 10. This changes (x,y) to (x-1,y+1).
* y=3: replace three 10s by four 8s. This changes (x,3) to (x+4,0).

Both have exact cost two and implement k->k+1. The absent transition is
when x=0,y<3, leading to one of the unresolved common increments 4 or 9.
The inverse recognizes y>0 as 10->8, or y=0 as 8^4->10^3; at k=2 it
instead replaces 3b and 8 by 3(b+2), and at k=1 undoes the old merge.
Thus all transitions 0->1->2->3 and 6->7->8 are reversible, and all common
increments starting at k>=10 have a proved reversible carry. k=4,5,9
remain outside the mixed domain, rather than being silently assigned.

A naive superposition of the zero-pair six-count gadget would collide with
nu. At b=2, the two C inputs mu=(2,2),nu=(1,1) and mu=(5,5),nu=(0,0)
would both give (8,6^4,3^2), weight 38, under the rule “dense baseline,
extra 3b, plus the b=0 carrier.” The isolated markers avoid that particular
information loss. This explicit algebraic witness is not an enumeration
above the verification ceiling. It does not refute every superposition.

## Universal proof for the combined restricted statement

**Validity.** Decoded heights of 9,8,6,3,1 are 5,4,3,2,1. Repeats introduce
zero drops. The largest drop in the first pattern is 4 to 1 (or terminal 4).
In the second pattern, the required one gives a final drop 5 to 1 when j=0,
and for j>0 the final positive non-one height is 3. In the third, the 3 of
height 2 ensures the final drop from height 5 when j=0 is 3. All terminal
drops are strictly below five. Thus every formula is in the actual U domain.

**Exact weight.** Since b=0,a=2, required weight is 4+2k+t. The three totals
are 8+6j+t, 10+6j+t, and 12+6j+t, exactly the required values after substituting
k. The old theorem handles S_C. The new inverse uniquely recovers j,r,t from
literal multiplicities, so the formulas and inverse compose to the identity
both ways on S'_C and the stated S'_U. These arguments are weight-universal.

**Common raising and lowering.** The intrinsic representation implements
(k,k+t) -> (k+1,k+1+t) at cost two. In columns use the following five branches:

1. k=0: replace 3 and one 1 by 6.
2. k=1: replace the unique 6 by 8.
3. k=3j+2: replace 8 by 9 and one 1.
4. k=3j+3: replace one 1 by 3, keeping 9.
5. k=3j+4: replace 9 and 3 by 8 and one 6.

The fourth branch always has the needed extra one. In the fifth branch the
number of sixes increases j to j+1. Each rule gives exactly the next formula;
its inverse is recognized from that next formula, including k=1 and k=2 at
the start. No history is retained. These are reversible operations, despite
weight increasing by two in the forward direction. Zero t is allowed.

**Termination and cost.** Divmod and counting are finite, with output length
at most N. The revised maps keep the conservative round-one O((N+1)^2 log(N+2))
bit-work and O((N+1)^2) auxiliary-bit bounds in unary weight N. No contract
complexity revision is required for this restricted extension.

## Exact unresolved obligations and falsifiers

The full bridge is not accepted. The first excluded C after this extension is
C=(3,0,(0,0,0),()), weight 9. Mixed omissions now begin at weight 21: C=(2,1,(4,4),(0,)), since Q(2,1)=13
and the increments sum to eight. The omitted common increments are 4,5,9.
An explicit valid uncovered U is (6,3), weight 9: its single 3 excludes all
old recognition branches, and its support excludes all new ones. The zero-pair
extension covers U=(8), the previous first missing image. The frozen run will
check the smallest uncovered objects. None of these limitations claims that no
universal construction exists.

Next extension lemma: handle the mixed values k=4,5,9 with intrinsically
recoverable branches disjoint from all assigned sectors, or replace the current
restricted embedding with a more global statistic when mathematically justified.
The marker construction resolves the nu/six-count ambiguity on its stated domain,
but does not establish that its reserved sectors form the right global cores.
Sectors a>=3 and full coverage remain separate obligations. The original
mathematical objective is unchanged; this restricted embedding need not be
preserved if it obstructs a sound complete construction.

## Round-two learning record

Decisive obligation: image separation and preservation of information in a
mixed carry. Actually proved here: all common mu increments in the complete zero-pair a=2
sector and all mixed-sector carries starting at k>=10, with exact intrinsic
recognition, combined with the earlier arbitrary-b family.
The separate recursive insertion has an exact weight-43 collision; no amount
of agreement through 30 repairs it. Next justified step is semantic review
and a mixed-sector carry lemma, not an accepted global bridge.

Workflow hypothesis, **unvalidated**: symbolic comparison of competing inverse
branches can produce a falsifier beyond the finite verification ceiling and
suggest which statistic the next rule must preserve. RR003 does not measure
broader workflow success or change the original mathematical objective.
