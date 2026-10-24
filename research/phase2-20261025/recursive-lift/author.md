# Phase 2 recursive/Ferrers author handoff

25 October 2026, Europe/Stockholm. **Full KR1 remains unresolved. Novelty is
unverified.** The C lemma below was already proved with distinct ordinary
semantic review in RR007 R6; this phase implements it and checks the literal
reverse language through 40. The new geometric observations and candidate
failures below have author-only ordinary proof assurance until the Phase 2
critic reviews them. No formal prover was run.

## Exact C grammar, implemented without search

Let C consist of `(a,b,mu,nu)`, where `a,b>=0` and the two arms are ascending
nonnegative integer vectors of exact lengths a,b. Its weight is
`Q(a,b)+sum(mu)+3sum(nu)`, with `Q=a²+3ab+3b²`. The unique terminal is
`(0,0,(),())`.

For `a=3c+r`, `0<=r<3`, set `mu_0=0` and
`delta_i=mu_(a-i+1)-mu_(a-i)` for `1<=i<=a`. Set
`delta_(3j)=3e_j+t_j`, `0<=t_j<3`, and
`eta_l=sum_(j=c-l+1)^c e_j` for `1<=l<=c`.
The child is exactly `(b,c,nu,eta)`. The boundary consists of r, the ordered
gaps delta_i with `3` not dividing i, and the ordered trits t_j.

**Proved, previously reviewed:**

`wt(C)=3wt(child)+r²+3r(b+2c)`
`       +sum_(3∤i) i*delta_i +sum_(j=1)^c 3j*t_j`.

Indeed `sum(mu)=sum i*delta_i`, while the divisible positions contribute
`9sum j*e_j+3sum j*t_j`. The eta definition gives
`sum(eta)=sum j*e_j`; the child's first arm is precisely the old nu.
The remaining equality is expansion of Q. Every residual term is
nonnegative, but it need not be positive.

The intrinsic reverse language is a terminal or a node with an admitted
child and the following data. If the child dimensions are `(a',b')`, set
`b=a'`, `c=b'`, `a=3c+r`. Require r in `0,1,2`, exactly `a-c` nonnegative
nonthree gaps, and exactly c trits in `0,1,2`. Forbid `a=b=0`; this prevents
an empty node above the terminal. Recover e as the reverse gaps of eta,
set `delta_(3j)=3e_j+t_j`, insert the stored other gaps, and reverse-cumulate
to reconstruct mu. Set nu equal to the child's first arm.

This reconstructs all coordinates exactly, including zeros and repeated
entries. Euclidean quotient/remainder uniqueness proves both identities,
not merely injectivity. Applying the dimension transformation twice yields
`(floor(a/3),floor(b/3))`; thus the recursion terminates at the unique
terminal. These algorithms use no enumeration, rank, saved orbit history,
external choices or growing table. The C child weight is never greater
than one third of the parent weight.

`triadic.py` implements this statement. `verify.py` uses two genuinely
different finite generators: direct exact-length arm enumeration and a
bottom-up recursive grammar generator enumerating independent boundary
digits by their weights. The latter is **not** `encode(c_exact(...))`.
It tests `decode(encode(C))=C`, `encode(decode(tree))=tree`, exact equality
of the forward and independent reverse languages, weights, and five
malformed-node rejections. It also compares direct C records against the
pre-existing literal `kr1.cluster_data` generator.

| Maximum weight | Literal C | Independently admitted trees | Maximum depth |
|---:|---:|---:|---:|
| 12 | 59 | 59 | 3 |
| 30 | 1,393 | 1,393 | 4 |
| 40 | 5,461 | 5,461 | 4 |

All counts include the empty object and aggregate weights zero through the
bound. At 40 there are 5,460 nonterminal sources, 72 zero-residual edges,
1,913 sources with at least one positive top-level trit, 1,819 sources with
zero in mu, 1,985 with a repeated mu entry and 139 with a repeated nu entry.
These within-arm repetition statistics are not literal A/B distinct-part
statistics. At weight exactly 40 there are 660 C records. The pilots ran
in the required order 12,30,40 on unchanged frozen scripts. They establish
finite transcription checks, not a new universal KR1 result.

## A lattice interpretation of the scale-three operation

**Proved, author-only geometric reformulation.** In the Euclidean embedding
`v(a,b)=(a+3b/2, sqrt(3)b/2)`, squared length is Q. The integer linear map
`T(x,y)=(3y,x)` satisfies `Q(T(x,y))=3Q(x,y)` and `T²=3I`.
Normalized by sqrt(3), it is reflection across the line at angle 15 degrees
in this embedding: its matrix is
`[[sqrt(3)/2,1/2],[1/2,-sqrt(3)/2]]`.
The parent core is `T(b,c)+(r,0)`. Expanding the squared length of this
point gives precisely the boundary core cost `r²+3r(b+2c)`. Thus r selects
one of three lattice cosets for the first coordinate, rather than a free
geometric color. This explains the norm identity and alternating child
dimensions. It does not define an action on U or a Ferrers cut, and it is
not evidence that an arbitrary fixed symmetry of U will preserve a map.

## Three frozen U cuts and exact failures

The corrected lossless Ferrers solid has ordered rows
`P_t(5q+r)=3q+clamp(r-t,0,3)`, `t=0,1,2`. Each row is nonincreasing in t,
each slice is a partition, and its row sum is F(h), so its volume is the
literal U weight. Strict monotonicity of F recovers h from this row sum.
The following three families were frozen before numerical execution in
`candidate-rules.md`. None is promoted to a U/C lift.

1. **Lower sheet core: refuted.** Taking the common equal three-layer prism
   with numerical child rows P2 produces child `(2)` from U=`(8)` at weight
   8. Two is not in the literal U alphabet. This is the smallest observed
   failure, and the paper witness is immediate from decoded height four.
   Through 40, 2,504 of 5,461 inputs fail child U membership.
2. **Every-third-row compression: refuted.** U=`(9,9,9,1)`, decoded
   `(5,5,5,1)`, has all drops at most four, including its terminal one.
   Selecting row three leaves `(9)`, decoded `(5)`, with forbidden terminal
   drop five. Its weight is 28, the smallest observed failure after a
   successful through-12 pilot. It is also the true minimum for this fixed
   rule: a bad terminal retained height is at least five and requires the
   first three parent rows to have weight at least nine each, plus a
   further positive row below them to make the original terminal valid.
   A bad internal retained drop instead requires the upper retained height
   to be at least six, so its first three parent rows alone cost at least
   thirty. Through 40, 148 inputs fail membership.
   This preserves the old lesson that the bottom boundary is load-bearing.
3. **Ternary-height compression: exact carrier, but refuted as the retained
   C lift.** Take `floor(h_i/3)`, dropping trailing zeros, as child heights.
   All successive child drops are at most two, and the child's terminal
   height is at most one. Thus it is always a literal U. Store all remainders
   `h_i mod3` in their original order, including entries corresponding to
   vanished rows. They determine the original row count L; pad child heights
   with `L-length(child)` zeros, set `h_i=3q_i+r_i`, and admit the data iff
   the restored heights are positive, descending and five-flat including
   the terminal. This defines a literal intrinsic inverse of this carrier.
   Both directions are immediate quotient/remainder identities.

   Nevertheless, this child range cannot contain `(3)`, whose decoded
   terminal height is two. The exact C grammar already demands child
   `(0,1,(),(0))` for parent `(3,0,(0,0,0),())` of weight nine. The retained
   reviewed g2 sends that child to U=`(3)`. Hence **no possible parent U**
   can make this fixed quotient cut commute with the retained child map
   for this parent. This is a universal range obstruction at parent weight
   nine, not just failure to find a preimage in a sample.

   The finite trials found nonnegative `|U|-3|child|` on all 5,461 inputs
   through 40. That observation is insufficient for the C boundary language,
   and no universal residual-positivity claim is made. A full ordered
   remainder word retains substantial boundary information; its exactness
   does not mean it has the required C costs and admissibility conditions.

The same 12/30/40 trials checked solid volume/order, the padded quotient
identity, and U validity independently from C counts. Their U totals were
59/1,393/5,461. This equality is reported only as finite object accounting.

## Preserved obstructions, promising clue, and remaining lemma

The earlier area collision U=`(8,3,1)` versus `(6,6)` remains: both have
sheet areas `(6,4,2)`. Full ordered slices distinguish them. The earlier
weight-13 inclusion obstruction remains: every weight-15 valid Ferrers
solid containing the lift of `(6,3,3,1)` is one of
`(8,3,3,1)`, `(6,3,3,3)`, `(6,3,3,1,1,1)`. Each is already an A3 image
of a different retained source. The 30 and 40 runs independently enumerated
and exactly recovered these three targets. Therefore adding two positive
cubes, even after a fixed coordinate permutation, cannot supply the coherent
common-arm operation. Deletion, boundary transport, or a changing cut is
still allowed. These are preserved prior results, not new proofs by this
worker.

The sector author sent a useful **unverified bridge clue**, with its exact
algebraic identity separately derivable: for a=3, write
`mu=(x,x+y,x+y+z)`, `B=b+1`, `x=Bq+k`, `0<=k<B`, and
`nu'=(q,q+nu_1,...,q+nu_b)`. Then
`wt(C3,b)=wt(C1,B,(z),nu')+2+2y+3k`.
This repackages arbitrary b into an a=1 carrier, a bounded phase k and
weight-two motion. Existing target cones collide under the naive lift;
the identity is not an injection or a disjoint image theorem. Its precise
benefit is that an all-b fusion must recover k and q, rather than treating
top multiplicity as a free independent column.

The remaining full recursive obligation is a canonical U cut/gluing whose
child can realize every recursively required U image and whose intrinsic
boundary is exactly the ordered nonthree gap/trit language above. It must
recover the index-three core coset and the mod-five Ferrers seam together,
without destroying the already fixed g2/H1 values. Our three naive cuts do
not do this. No all-weight U/C recursion has been constructed.

## Resource and provenance

Only files in this worker's `recursive-lift/` directory were written. No
closed RR006/RR007 record was changed. The source script hashes were saved
before the first pilot in `prepilot-freeze.json`. Six mathematical
subprocesses used the shared meter, labels `recursive-grammar12`,
`recursive-cuts12`, `recursive-grammar30`, `recursive-cuts30`,
`recursive-grammar40`, `recursive-cuts40`. Their recorded wall times are
0.076581125, 0.073905334, 0.285798459, 0.176969500, 0.820327833 and
0.504823667 seconds, totaling **1.938405918 seconds**. The largest observed
peak child RSS was **24,182,784 bytes**, measured after exit. There were no
timeouts or failed numerical invocations, no above-40 input/output, no
web retrieval, external message/provider, dependency install or nested agent.
Preparation/file reads/hash operations are elapsed work, not numerical
subprocess time. No measured service/model compute figure is available.
