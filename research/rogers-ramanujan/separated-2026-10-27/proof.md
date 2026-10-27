# Exact separated image of the supplied KR1 compiler

Christopher Yamba's supplied note motivates this audit. Date: 27 October 2026.
Status: written proof; separate review recorded in `review.md` when complete.
**Novelty status: NOT VERIFIED.** No Lean certificate is claimed.

## Objects and the actual formula

All tuples in this note are descending. Let a,b be nonnegative integers,
mu=(mu_1,...,mu_a) a weakly decreasing nonnegative integer tuple, and
m=(m_1,...,m_b) another such tuple. The supplied nu is **3m**; the existing
repository's ascending cluster convention instead uses **reverse(m)** as nu.
Write Q(a,b)=a^2+3ab+3b^2 and give the source weight
Q(a,b)+sum(mu)+3sum(m), with dimension a+2b.

For i=1,...,a set

    S_i = 3b+2(a-i)+1+mu_i.

For i=1,...,b set j=b-i+1 and m_i=2q_i+r_i, r_i in {0,1}, and set

    H_i = 3j-1+3q_i+r_i,
    L_i = 3j-2+3q_i+2r_i.

The literal compiler is F(mu,m)=(S_1,...,S_a,H_1,L_1,...,H_b,L_b).
The supplied `carry_lift` never changes and its advertised boundary repair is
`pass`; this is the formula actually executed. No sorting or repair is implicit.

A KR1 gap partition lambda is a descending positive integer tuple satisfying
lambda_i-lambda_(i+2)>=3, and if adjacent parts differ by at most one their
sum is divisible by three. The empty tuple is included.

## Theorem 1: exact validity and raw injectivity

For every source F preserves weight and dimension. It is injective as a map
to **integer tuples**, even when its output is not a gap partition. It is a
KR1 gap partition exactly under the following condition:

* a=0 or b=0; or
* a,b>0 and mu_a >= ceil(3m_1/2).

Consequently collision-freedom cannot certify this candidate's KR1 validity.

Proof. The singleton sum is a^2+3ab+sum(mu). Each pair has weight
6j-3+3m_i; summing gives 3b^2+3sum(m). There are exactly a+2b entries.
The singleton gaps are at least two, so their distance-two gaps are at least
four. Pairs are positive and have difference 1-r_i; their sums are multiples
of three.

Set h(t)=3 floor(t/2)+(t mod 2) and
l(t)=3 floor(t/2)+2(t mod 2). Both functions strictly increase, and
h(t)-l(t)=-(t mod 2), so H_i-L_i=1-r_i. For consecutive pairs, m_i>=m_(i+1), so
H_i-H_(i+1)>=3 and L_i-L_(i+1)>=3. Also
L_i-H_(i+1)=2+l(m_i)-h(m_(i+1))>=2. Thus the entire paired tail is a
valid gap partition; its interpair boundaries are never close.

If both blocks exist, the triple S_a,H_1,L_1 forces S_a-L_1>=3. This is
exactly mu_a>=l(m_1)=ceil(3m_1/2). Conversely this inequality makes
S_a-H_1>=2+r_1, hence the boundary is ordered and not close. If a>=2,
S_(a-1)-H_1>=4+r_1, so the remaining straddling distance-two condition
also holds. All other conditions were checked inside the blocks. This proves
both necessity and sufficiency, including a=0,b=0.

For raw injectivity, equal outputs have equal length k. If two source pair
counts differ, take b'>b; then a'=a-2(b'-b), and one of the b' prescribed
close pairs lies entirely inside the first source's singleton block. Its
adjacent difference is at least two there, a contradiction. Hence a,b agree.
Each S_i recovers mu_i directly, and each pair's sum recovers
m_i=(H_i+L_i-6j+3)/3. These are literal inverses to the formulas, proving
injectivity without requiring a valid output. QED.

The smallest failure is weight10:
(a,b,mu,3m)=(1,1,(0,),(3,)) maps to (4,3,3). It violates both the
adjacent-sum condition and the distance-two condition. Weight11 with
mu=(1,) gives (5,3,3), violating the latter only. These witnesses refute
the universal compiler, not the KR1 identity or every possible repair.

## Theorem 2: intrinsic image and explicit inverse

In a KR1 gap partition, mark **every** adjacent pair whose difference is at
most one. Such pairs cannot overlap: an overlapping triple has total span
at most two, contrary to the distance-two condition. Marked pairs and remaining
singletons therefore form a unique atom word.

Call the partition separated if its descending atom word is S^a P^b: every
singleton precedes every close pair. The empty and either pure block are allowed.
F restricted by Theorem1 is a weight- and dimension-preserving bijection onto
exactly these separated gap partitions, for all a,b simultaneously.

Explicit inverse: read a,b from the unique atom word; set

    mu_i = S_i-3b-2(a-i)-1,
    m_i = (H_i+L_i-6(b-i+1)+3)/3.

Proof. Theorem1 shows all admitted outputs have precisely the marked pairs
displayed by F: there are no close singleton, interpair or block boundaries.
It remains to show the inverse is well-defined for every separated target.

Each positive close pair with divisible sum is either (3t-1,3t-2) or
(3t,3t), t>=1. Write its type as r=0 or 1 respectively, and assign its
level ell=2(t-1)+r. In descending order, successive levels differ by at
least two. To see this, their t values weakly decrease by ordering. Equal
t values make their high entries differ by at most one, violating
distance-two; thus their t values strictly decrease.
if they decrease by at least two the level gap is at least three. If the
t difference is one, the only level gap below two has upper type0 and
lower type1. Their high entries differ by two, violating distance-two.
Conversely level gaps at least two suffice by the pair-boundary calculation
in Theorem1. The smallest positive pair has ell>=0.

Hence ell_i>=2(b-i) and m_i=ell_i-2(b-i) is a descending nonnegative
integer tuple. The pair weight is 3(ell_i+1), so this agrees exactly with
the displayed inverse. Consecutive singleton gaps are at least two,
making mu weakly decreasing. If b=0, the smallest singleton is >=1,
so mu_a>=0. If both blocks exist, distance-two at their boundary gives
S_a>=L_1+3=3b+1+l(m_1), whence mu_a>=l(m_1)>=0.
If a=0 there are no singleton inequalities to check.

Substitution recovers every singleton and pair from its mu or m coordinate;
the forward weight and dimension calculation applies. This proves both
inverse identities and surjectivity onto the stated intrinsic image.
Both algorithms terminate after a+b atom operations, using O(a+b) stored
integers and arithmetic on O(log(N+2))-bit values. QED.

This is a **restricted cluster-to-gap endpoint**, not the missing residue-to-
cluster map. It does not automatically combine with other restricted maps.
It is the separated-block case of the more general merge already present in
`../rr003/endpoint-cluster-merge.md`, whose broader assurance is unchanged.

## Theorem 3: positive rational generating function

Let F_(a,b)(q) enumerate separated targets with a singles and b pairs by weight.
Set (q;q)_a=product_(i=1)^a(1-q^i), with empty products one. Then

    F_(a,b)(q) = q^Q(a,b) P_(a,b)(q)
                 / ((q;q)_a product_(i=1)^b(1-q^(6i+3a))),

where the finite positive polynomial is

    P_(a,b)(q) = sum_(epsilon in {0,1}^b)
                  q^(3 sum_(i=1)^b i epsilon_i
                       + a ceil(3 sum_i epsilon_i/2)).

Equivalently, using Gaussian polynomials,

    P_(a,b)(q) = sum_(j=0)^b q^(3j(j+1)/2 + a ceil(3j/2))
                                      [b choose j]_(q^3).

Proof. For a,b>0, write mu_i=l(m_1)+alpha_i; alpha is an unrestricted
descending nonnegative tuple of length a. It contributes 1/(q;q)_a, and
the common shift contributes q^(a l(m_1)). For a=0 the same weight factor
is one without introducing a nonexistent mu entry; for b=0 there is only
the singleton factor. For b>0 put m_(b+1)=0 and
delta_i=m_i-m_(i+1). Then m_1=sum(delta_i), and
sum(m_i)=sum(i delta_i). Write delta_i=2e_i+epsilon_i with e_i>=0 and
epsilon_i in {0,1}. Thus

    3sum(m_i)+a ceil(3m_1/2)
       = sum_i (6i+3a)e_i
          + 3sum_i i epsilon_i + a ceil(3sum_i epsilon_i/2).

Independent geometric sums over e_i give the denominator and the finite
sum over epsilon gives P. Grouping subsets by their size gives the Gaussian
expression: sum_(|epsilon|=j) x^(sum i epsilon_i)
=x^(j(j+1)/2)[b choose j]_x. This is also a combinatorial definition of
the polynomial and requires no imported analytic identity. QED.

In particular F_(1,1)(q)=q^7(1+q^5)/((1-q)(1-q^9)). For a=0 the numerator
is product(1+q^(3i)), which cancels to q^(3b^2)/(q^3;q^3)_b.
For b=0 it reduces to q^(a^2)/(q;q)_a. These are checks of the formula,
not claims of new identities.

## Source comparison and assurance limits

Kurşungöz, *Andrews-Gordon Type Series for Kanade-Russell Conjectures*,
[arXiv:1808.01432v1](https://arxiv.org/pdf/1808.01432), Theorem7 and base
configuration(3), pp5-6, give the existing cluster-series endpoint, with
the same Q and singleton/pair staircase. Theorem statement and base layout
were inspected on 27 October 2026; the entire paper/proof was not audited.
Thus neither the cluster base nor the general endpoint is novel here.
The note's scale3 quadratic decomposition and period6 second difference
follow by expanding Q; neither establishes a recursive partition map.

What this audit adds to this investigation: an exact validity test for the
literal unfinished compiler, a self-contained inverse and image description,
and an explicit positive series for its safe restricted image. The existing
RR003 merge already goes beyond separated blocks. No publication-priority
claim, global target coverage, all-sector U-C disjointness or full KR1 proof
is implied. Finite enumeration below corroborates code, not universal validity.
