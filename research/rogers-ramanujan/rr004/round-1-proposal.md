# RR004 round one: obstruction to transition-additive pair recovery

**Status: proposed proved obstruction, author argument awaiting separate
semantic review. Complete KR1 remains unresolved. Novelty status: NOT VERIFIED.**

## Exact attempted extraction and claim

Let U=(F(h_1),...,F(h_l)) be the literal weighted-column domain, with
h_1>=...>=h_l>0, h_(l+1)=0 and each h_i-h_(i+1)<5.
C=(a,b,mu,nu) is exactly the contract's cluster family, not a new model.
The attempted first step was to recover its pair count intrinsically by
fixed local transition energies:
  
    b(U) = sum_i e(h_i,h_(i+1)).

Allow arbitrary real, signed charges e(h,k), depending on both full heights,
not just their residues or difference. They are fixed independently of
weight, column index, repetitions elsewhere and the rest of the input.
The empty sum is zero. No condition is placed on how a,mu,nu would be
recovered. The intended final map must be a weight-preserving bijection.

**Claim.** No weight-preserving bijection U <-> C has this pair-count
formula. This rules out this specific recovery mechanism, not KR1, every
core method, a contextual state, or a multiplicity-dependent extraction.

## Written universal argument

1. **Diagonal charges vanish.** Fix any h>0 and any allowed descending
height path from h to zero. Such a path exists by unit steps. Repeating
its first height m additional times creates valid U_m of weight
N_m=N_0+mF(h), and b(U_m)=b(U_0)+m e(h,h). Every actual C obeys
0<=b<=sqrt(N/3), since N>=Q(a,b)>=3b^2. A negative diagonal charge
eventually makes b negative; a positive one grows linearly past this
square-root bound. Hence e(h,h)=0 for every h. This argument is universal;
a finite repetition check cannot replace it.

2. At weight one the only U is (1) and the only C is
(1,0,(0,),()). Thus e(1,0)=0. All (1^m) have b=0 by step 1.
At weight three the actual U are (3) and (1,1,1); C has exactly one
object with b=1, namely (0,1,(),(0,)), and one with b=0.
Surjectivity/injectivity therefore force e(2,0)=1.

3. At weight four every C has b=0: a=0,b=1 gives only weights
3+3|nu|, a>=1,b>=1 has Q>=7, and b>=2 has Q>=12.
The valid U=(3,1) has heights (2,1), so e(2,1)=0.

4. At weight seven the complete U list is
(1^7), (3,1^4), (3,3,1), (6,1). The first three have b=0 by
steps 1–3. There is exactly one C with b>=1, the datum
(1,1,(0,),(0,)); the other three have b=0. Thus (6,1) must have
b=1, giving e(3,1)=1. Completeness of this tiny U list follows directly:
largest value 8 exceeds seven, so only 1,3,6 can occur; solve their
weight equation and retain literal flatness. The C list follows from Q.

5. At weight nine there are exactly two C with b>=1:
(0,1,(),(2,)) and (1,1,(2,),(0,)). Both have b=1.
The distinct valid objects U=(3,3,3) and U=(6,1,1,1) already have
b=1 by the forced charges. Injectivity occupies both targets.
Consequently the third valid U=(6,3), with heights (3,2), must have
b=0. Its charge is e(3,2)+e(2,0), forcing e(3,2)=-1.
If all charges were required nonnegative, this already refutes the
mechanism at weight nine.

6. The valid U=(6,3,1), weight ten, has decoded heights (3,2,1).
The same formula gives b=-1+0+0=-1, impossible for C.
This contradiction proves the claimed obstruction even for signed charges.

All small lists above are checked directly from the definitions in the
argument; the finite verifier only checks their executable transcription.
In particular, no equality of global generating functions or known KR1
identity is assumed. An additional initial-height potential is covered:
p(h_1) with p(0)=0 telescopes as sum[p(h_i)-p(h_(i+1))], hence can be
absorbed into e. This does not cover arbitrary nonlocal or index-dependent
potentials, and no such broader impossibility is claimed.

## Connection to the first omitted objects and next obligation

U=(6,3) decodes to heights (3,2), W=(2,2,1). The omitted
C=(3,0,(0,0,0),()) has weight nine and still lacks a selected global
image. The argument does not identify these two as a matching pair.
It identifies an obstruction to a tempting intrinsic statistic on this
very source boundary. A global rule must retain context beyond fixed
neighboring-height charges, for instance run multiplicity or a recoverable
marking/cancellation state. No such corrected rule has yet been constructed.

The desired extraction/reconstruction still owes intrinsic a,b, ordered
zero-padded mu,nu, exact Q-weight, disjoint exhaustive coverage, termination
and both inverses. Without that gate there is no broad map implementation
or weight-thirty sweep. A counterexample to the attempted statistic is
progress, never complete KR1 success. Lean/exposition remain subsequent.

## Attribution, dependencies and discovery exposure

Dependencies are only the explicit definitions of U,C and the elementary
bound N>=3b^2. No final RR003 author-only theorem is used as a premise.
The existing kr1.py is an executable transcription checked against those
definitions, not a trusted proof oracle. Both RR003 semantic reviews and
the prior row-position obstruction were inspected as local comparison.
Established endpoint constructions retain Andrews–Keith/Stockhofe and
Kurşungöz attribution. No new external primary source was inspected;
novelty and the closest external equivalent remain unverified.

Discovery exposed the exact objects at weights 1,3,4,7,9,10, including
the first-traces receipt. These are not held-out cases. A successful
certificate run will not be called a successful bijection pilot.

Cost: a constant-size exact obstruction; no prospective full-map work or
space bound is established. Workflow hypothesis, unvalidated: auditing
a pair-count statistic before building its increment machinery can reveal
a forced information deficit. This run does not measure discovery gains.
