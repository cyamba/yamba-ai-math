# RR003 final recursive revision: retain charge information in cluster coordinates

**Proposed proved restricted theorem; author-only assurance.** This stays
inside mechanism B, repairing the refuted one-charge insertion by changing
its internal representation. It uses classical ternary Glaisher and the
attributed gap–cluster endpoint, expressed by the independently proved
direct merge in [the endpoint argument](endpoint-cluster-merge.md).
No universal KR1 map, independent review of this repair, Lean certificate
or novelty claim is supplied. The failed rule and both reviews are retained.

## Structural failure and an infinite counterexample family

The two preserved cores P=(3,3,6,9,9,12) and Q=(3,3,6,6,12,12) have weight
42 and map to the same weight-43 output under the old single/double rule.
Adjoin the same arbitrary multiset R of multiples of three at least 21,
with each multiplicity at most two. The old moves never touch R, stop at
charge16, and output (3,6,9,9,16) union R. Hence the failure extends to an
infinite collision family, not just one isolated weight. All cores and
outputs satisfy their literal gap predicates; the gap to R is at least five.
At a state where both old branches are enabled, the count at the current
index is positive. Taking the double branch then makes that count at least
three. Consequently any variant retaining those two moves and the invariant
that every core count is at most two must take the single branch there.
Changing priority alone cannot fix the collision while keeping that invariant.
A new rule, state or representation is required. These are symbolic author
arguments extending the separately reviewed exact witness.

## Exact repaired source and forward rule

The source is the genuine infinite subfamily B_small: zero, one or two
copies of the **part 1**, together with arbitrary B parts divisible by three.
It excludes larger parts congruent to 1 or 8 modulo nine, and excludes three
or more ones. Write t in {0,1,2} for the one count. Apply classical ternary
Glaisher to the remaining parts, obtaining a gap core K with all parts
multiples of three and multiplicities at most two. For t=0 return K.
For t>0 extract C=(a,b,mu,nu) from K by the explicit cluster inverse.

* If a>0, increase only the last mu coordinate by t.
* If a=0, replace C by (1,b,(t-1,),nu-(1,...,1)).

Reconstruct the gap partition by the direct merge. The second branch is
always defined: with no singles, every pair of the three-divisible core
is (3r,3r), hence its level is odd, and nu_j=level-2j is odd, ascending and
at least one. For b=0 the vector is empty and the empty core is allowed.
The first branch keeps mu ascending. Both therefore yield literal C data.

## Intrinsic inverse and proof

For an actual gap partition whose every part is divisible by three, use
inverse Glaisher and t=0. Otherwise extract C. If a=1 and mu=(0,) or (1,),
recover t=mu_1+1, restore a=0 and add one to each nu coordinate. In the other
branch require a>0, put

    t = (mu_a-a-1) modulo 3,

require t in {1,2}, subtract it from the last mu, and require a valid vector.
Reconstruct the proposed core K and require every part of K divisible by
three. Reject objects failing these intrinsic tests; accepted ones return
t ones followed by inverse Glaisher(K).

Why is t intrinsic? In any all-three-divisible core, the last single s has
a-1 earlier singles and q earlier pairs. Its coordinate is
mu_a=s-3q-2(a-1)-1, so mu_a is congruent to a+1 modulo three. Increasing it
by t changes exactly that residue. The a=0 conversion has a=1 with mu=t-1
in {0,1}. An original a=1 core has its single coordinate congruent to two
and at least two; raising by t gives at least three or four. Thus the two
inverse branches cannot overlap. In every repaired t>0 image the last
single has residue t modulo three (its formula is mu_a+3q+2(a-1)+1), so
it cannot be confused with the t=0 all-three-divisible image. These facts
prove exact recovery of t and the original C, hence both inverse identities
on B_small and its intrinsically recognized image.

Weight: the a>0 branch adds t to |mu|. In the a=0 branch,
Q(1,b)-Q(0,b)=3b+1, subtracting one from every nu lowers 3|nu| by 3b,
and the new mu contributes t-1. The net change is exactly t. Glaisher
preserves core weight, so the map preserves the full residue weight.
All stages terminate and satisfy the earlier conservative quadratic work
and auxiliary-space bounds. These are universal written arguments, not a
consequence of finite enumeration. Their assurance remains author-only.

## Exact improvement and remaining obligation

The old weight-43 collision is separated. P extracts to
C=(2,2,(2,3),(1,2)), while Q extracts to C=(0,3,(),(1,1,3)). The repaired
one-charge rules keep these data distinct, taking P to (3,3,6,9,9,13) and
Q to (1,2,4,5,7,12,12). These literal outputs are checked as direct witnesses,
not a sweep beyond weight 30. The representation's concrete advantage is
that increment data survive every operation and its inverse recognizes the
branch without a saved path.

The next lemma is a disjoint recoverable extension for arbitrary residue
parts 9r+1 and 9r+8 and arbitrary one multiplicity, with compatible repeated
insertions or matching recursions. Carrying three ones into one 3 immediately
loses information: source (1,1,1) and source (3) would become the same core.
Increasing the last mu by a general 9r+1 also does not retain r separately
from the original mu value. Neither shortcut is a universal extension.
The U–C global decomposition remains the leading alternative obligation.
The original mathematical objective and success criterion are unchanged.

Workflow hypothesis, **unvalidated**: a refuted local insertion may become
reversible on a useful infinite subfamily after moving to established
intrinsic coordinates. This does not establish a higher discovery success
rate or authorize broader harness changes.
