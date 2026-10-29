# RR004 round two: a finite obstruction to additive pair-count extraction

**Status: proposed proved finite obstruction; separate review pending.
Complete KR1 unresolved. Novelty status: NOT VERIFIED.**

## Statement and source set

Let S contain the following fourteen literal U objects:

    (1), (1,1), (1,1,1), (3), (3,1), (3,3), (3,3,3),
    (1^7), (3,1^4), (3,3,1), (6,1), (6,1,1,1), (6,3), (6,3,1).

All are valid: decoded heights are descending in {1,2,3}, so their
adjacent and terminal drops are at most three. Their maximum weight is ten.

**Claim.** There is no weight-preserving injection Phi:S -> C and fixed
real signed transition charges e(h,k) such that the pair coordinate of
Phi(U) is sum_i e(h_i,h_(i+1)), including repetitions and the terminal zero.
The a,mu,nu coordinates are otherwise unrestricted. Thus no full U-C
bijection, or even injection, can use this exact pair-count recovery.
No assumption of global U/C count equality or eventual behavior is used.

## Complete finite proof

Write x=e(1,0), d=e(1,1), y=e(2,0), z=e(2,1),
g=e(2,2), t=e(3,1), w=e(3,2).
For every C of weight N, a,b are nonnegative integers and N>=3b^2.

1. All C of weights one and two have b=0. Applied to (1) and
(1,1), this forces x=0 and d=0.

2. At weight three C has only (1,0,(2,),()) and (0,1,(),(0,)).
The source (1,1,1) has b=0 and occupies the sole b=0 target.
Injectivity forces (3) to have b=1; hence y=1.

3. At weight four every C has b=0. Indeed b>=2 costs at least twelve;
a>=1,b=1 costs at least seven; and a=0,b=1 has weights 3+3|nu|.
The source (3,1) gives z+x=0, so z=0.

4. For (3,3), of weight six, b=g+y=g+1 is an integer in {0,1},
because 3b^2<=6. Therefore g is either -1 or 0. If g=-1,
the source (3,3,3), weight nine, has b=2g+y=-1, impossible.
Hence g=0. No infinite repetition lemma is needed.

5. At weight seven the only positive-b target is
(1,1,(0,),(0,)); the b=0 targets are exactly
(1,0,(6,),()), (2,0,(0,3),()), (2,0,(1,2),()).
The three distinct sources (1^7), (3,1^4), (3,3,1) all have
b=0 by x=d=z=g=0, and so occupy all three b=0 targets.
The fourth source (6,1) must have b=1, forcing t=1.

6. At weight nine the positive-b targets are exactly
(0,1,(),(2,)) and (1,1,(2,),(0,)). This follows by considering
b=1,a=0,1 and excluding b>=2 or a>=2,b>=1 by Q.
The sources (3,3,3) and (6,1,1,1) have b=1 and occupy both.
Thus (6,3) must have b=0, so w+y=0 and w=-1.

7. The source (6,3,1), weight ten, now has b=w+z+x=-1.
This contradicts its target being literal C. Both cases for g fail,
so the supposed injection does not exist.

All capacity uses are at a fixed actual weight. The proof never requires
a formula for Phi, a global counting theorem, surjectivity, finite-map
ranking, or the rest of U. It also does not assert minimality of fourteen
objects or weight ten. An added initial-height potential telescopes into
the same charges, as in the first proposal.

## Evidence boundary and implication

This is an exact finite impossibility proof for a restricted statistic
class. A finite witness can refute a universal proposed construction;
finite agreement still cannot prove a universal KR1 construction.
The script checks the stated fibers, forced integer alternatives and
negative witness, not all real charge assignments by numerical search.
Separate semantic criticism must audit the logical exhaustiveness.

The obstruction does not exclude context-dependent charges, a state that
retains run multiplicities, nonlocal marking or cancellation, or general
intrinsic U-C decompositions. It selects no global image for the original
weight-nine C core. A replacement must recover enough context to avoid
these forced relations and then prove exact zero-padded increments,
weight, termination and disjoint exhaustive coverage with both inverses.
No viable replacement has been supplied in RR004.

Dependencies: the literal U and C definitions, elementary inequalities,
and the listed finite fibers derived above. No RR003 author-only premise.
The first review supports the earlier argument, not automatically this
strengthening. All exposed weights remain discovery data. No external
primary literature was newly inspected; preserve prior attribution and
**Novelty status: NOT VERIFIED**. No Lean run, complete bijection,
endpoint acceptance, or general workflow improvement is claimed.
