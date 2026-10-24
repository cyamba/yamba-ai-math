# RR003 round 1 — restricted inverse-first theorem

**Status:** proposed written proof of a restricted theorem; universal
KR1 bridge **incomplete**, novelty **unverified**, no Lean certificate.
The formulas below are frozen before their implementation verification.
Discovery exposure: all U through weight 12; previous RR002 traces.

## Exact domains and formulas

Write U in descending order. Put D(3j)=5q+t_r when j=3q+r, r=0,1,2,
where t=(0,2,3). This is the literal inverse of the weighted height F
on multiples of three. Consecutive positive j values change D by 1 or 2;
a gap of two j values changes D by 3 or 4. A final column 3 has height 2.

Let S_C consist of all C with a=0 or a=1, or a=2 and mu_1 in {0,1}.
All b and all nonnegative ascending nu are allowed. Set nu_0=0 and

    delta_j = nu_(b-j+1) - nu_(b-j),   1<=j<=b.

Then delta_j>=0 and sum(j delta_j)=sum(nu_i). Multiplicities below are
literal multiplicities of the U column value 3j; write 1^s for s ones.

1. a=0,b=0: U=(). For a=0,b>0, use m_b=1+delta_b and
   m_j=2+delta_j for j<b, with no ones.
2. a=1: use m_j=2+delta_j for all j<=b and 1^(1+mu_1).
3. a=2,mu_1=0: use m_j=2+delta_j for j<=b, one column 3(b+1),
   and 1^(1+mu_2).
4. a=2,mu_1=1: use m_j=2+delta_j for j<=b, one column 3(b+2),
   no column 3(b+1), and 1^(mu_2-1).

The empty b ranges in cases 2–4 are intentional.

## Intrinsic recognition and inverse

Separate the ones, s, from positive multiples of three, with indices j
and multiplicities m_j. Reject any other column residues.

* Empty U: case 1 with a=b=0.
* No non-one columns, s>=1: case 2, a=1,b=0,mu=(s-1).
* No ones, full support {1,...,L}, m_j>=2 for j<L, m_L>=1:
  case 1, a=0,b=L; delta_L=m_L-1, delta_j=m_j-2 otherwise.
* Ones present, full support {1,...,L}, every m_j>=2: case 2,
  a=1,b=L,mu=(s-1),delta_j=m_j-2.
* Ones present, full support {1,...,L}, m_L=1 and m_j>=2 for j<L:
  case 3, a=2,b=L-1,mu=(0,s-1),delta_j=m_j-2 for j<=b.
* Support {1,...,b} union {b+2}, m_(b+2)=1 and m_j>=2 for j<=b,
  any s>=0: case 4, a=2,mu=(1,s+1),delta_j=m_j-2.

In each case recover nu_i=sum(delta_j for j=b-i+1,...,b).
These disjoint tests define S_U without execution history or enumeration.
Reject other U as outside the restricted image. Verify literal U validity
before recognition. Every claimed a,b is recovered by these tests, only
on S_U; no global statistic on all U has been proved.

## Universal written argument for the restricted claim

**Validity.** Each listed multiplicity is positive where support is
required. Index gaps are one, except the single gap of two in case 4.
The D formula shows every adjacent height drop is <5. At the bottom,
index 1 has height 2, and an optional one has height 1. For b=0 in
case 4, the sole non-one column is 6 of height 3. Thus the terminal
height is <5 in every case, and U decodes to a literal valid W.

**Weight.** Baseline weights in cases 1–3 are respectively
3b^2, 1+3b(b+1), and 3b(b+1)+3(b+1)+1=3b^2+6b+4.
In case 4 the baseline non-one weight is 3b(b+1)+3(b+2)=3b^2+6b+6;
the number of ones is mu_2-1. Hence every case has weight
Q(a,b)+sum(mu)+3sum(nu), including the empty case. The delta identity
follows by telescoping, not by finite counting.

**Both inverses and coverage of S_U.** The support patterns and one
counts distinguish the six recognition branches. Subtracting the stated
minimum multiplicities gives uniquely nonnegative delta_j. Cumulative
sums recover an ascending exact-length nu, and taking its differences
recovers those same deltas. The ones recover exactly the stated mu.
Conversely rebuilding these multiplicities recovers each U in S_U.
No cardinality premise is used. This proves both inverse identities
on the explicitly restricted domains for every weight.

**Reversible operations.** Adding one column 3j increases delta_j by one,
equivalently raising the last j entries of nu by one, of weight 3j.
Its inverse is removal of a copy above the branch's baseline count.
Appending one increases the last mu entry by one in cases 2–4, with
inverse removal above the branch's minimum ones count.
Finally, in case 3 replace its unique largest column 3(b+1) and one
terminal one by 3(b+2). Weight rises by two. This is exactly
mu=(0,v) -> (1,v+1), leaving nu unchanged; its image is case 4.
The single missing level and largest singleton identify the reverse
split, which restores a terminal one. This is an infinite mixed-family
reversible operation, not an iteration rule for arbitrary mu_1.

**Termination and cost.** Construction iterates finitely over b and
output multiplicities; recognition scans U and b, then cumulative sums.
In unary weight N, b<=N and output length<=N. A simple list/sort and
conjugation implementation uses at most O((N+1)^2 log(N+2)) bit work and
O((N+1)^2) auxiliary bits, conservatively within the preferred targets.
Diagnostics and enumerating all objects are outside the map complexity.

## What remains unproved and smallest falsifiers

This is not the full bridge. The first excluded C is
(2,0,(2,2),()), weight 8. U=(8) is the first outside S_U.
Sectors a>=3 and common increments mu_1>=2 remain unresolved.

A tempting extension is to increase only the largest column by two after
the proved merge. It cannot be a universal cost-two rule: at b=0, the
successive top values 6,8,10 eventually give invalid singleton U=(10),
whose decoded terminal height is 6; adding ones still leaves height drop
6-1=5. At b=1, the first raised top 9 would become 11, which is not
in the image of F. These are exact obstructions to maximum-only updates,
not to general core-and-increment constructions. The next lemma must
specify a reversible carry across these boundaries and recover its
branches without collapsing already assigned sectors.

## Round-one learning record

Decisive obligation: a general intrinsically recoverable carry, not
termination or more coefficient agreement. Actually proved here: the
restricted formulas above, pending separate semantic review. Justified
next step: review their quantifiers/inverses and test literal domains;
if a credible carry cannot be supplied, investigate mechanism B.
Workflow hypothesis (unvalidated): intrinsic image recognition makes
uncovered sectors more explicit than normalization-only diagnostics.
