# RR003 recursive source seed: a proved restricted auxiliary injection

**Proposed proved lemma, author-only assurance; full KR1 unresolved.** This
is further proposal/revision work inside mechanism B, with no third mechanism,
critic round, new provider or changed objective. Novelty is unverified.

## Why this auxiliary question is concrete

[Xia v1, section 3, (3.8)](https://arxiv.org/html/2609.08816v1)
writes its first auxiliary series as (P2-P3)/q^2. Here P2 uses residues
2,3,6,7 modulo nine and P3 uses 3,4,5,6. I re-inspected Lemma 2.2,
(3.1)-(3.9), their product definitions and the boundary discussion. This
analytic formula does not supply an injection P3 into P2 with an identified
complement, much less all later recursive branches. Such an injection
would be one useful source-side foothold, not the complete branch adapter.

A proposed factorwise injection that leaves all three-divisible parts
unchanged is **refuted** at weight five: the P3 object (5) cannot map to
any partition of five using only non-three P2 parts (2 or 7 modulo nine).
The common three-sector must participate. This does not refute arbitrary
injections or the recursive mechanism.

## Actual infinite-family rule, inverse and invariant

Restrict P3 so its non-three parts are exactly fours and fives, while all
three-divisible residue parts are arbitrary. Write its small counts as
x=count(4), y=2q+r=count(5), r in {0,1}; write D for its three-divisible
subpartition. Define

    Phi(D + 4^x + 5^(2q+r)) = D + 2^(2x+r) + 3^(q+r) + 7^q.

Equivalently replace each four by two twos, each pair of fives by (3,7),
and an odd remaining five by (2,3). These replacements conserve weight:
4x+10q+5r=2(2x+r)+3(q+r)+7q. Output parts are in the P2 residue domain.
There is no weight-indexed table, enumeration, ranking or stored trace.
The source is an infinite family with unbounded x,y and arbitrary D.

The image is intrinsically specified: non-three parts must be only 2,7;
with A=count(2), q=count(7), r=A mod2, require count(3)>=q+r.
Recover x=(A-r)/2, y=2q+r. Remove the twos, sevens and q+r threes, then
restore x fours and y fives. This exactly recovers D, including its original
three count; all other parts were unchanged. Conversely every recognized
image reconstructs a valid source and its forward map restores every
multiplicity. These give both inverse identities and complete coverage
of this specified image, for every weight. The arithmetic and finite count
operations terminate. Conservative bit work is O((N+1)^2 log(N+2)), with
O((N+1)^2) auxiliary bits, within the preferred targets.

The naive rules 4->(2,2), 5->(2,3), retaining D, collide on (3,3,4) and
(5,5), both weight ten. The paired-five rule distinguishes them as
(2,2,3,3) and (3,7). These algebraic witnesses establish why parity and a
separate seven count carry information; finite agreement is not their proof.

## Closest inspected construction and exact extension lemma

[Bridges, Integers 20 (2020), A18](https://math.colgate.edu/~integers/u18/u18.pdf)
uses modular diagrams and recoverable residue-count cases for partition
injections. I inspected the introduction, Theorem 1 and its proof on printed
pp. 5-7, and the final application/discussion. These are prior techniques,
not newly claimed ideas. Its examples also use the name KR1 for a different,
modulo-twelve identity; that notation must not be substituted for RR003.
I have not shown that this elementary seed is absent from prior work.

The exact missing lift is to handle arbitrary 9j+4 and 9j+5 parts while
retaining the quotients, their association with the two residue groups,
and recoverable mixed three-sector data. A rule that merely maps residues
and sorts their attached nine-block diagrams can lose that association.
No such lift is proved here, and even it would not give all source families
H_(n,r), their complements, recursive branches and decreasing measure.
In particular, a restricted P3 injection is not a residue-KR1-to-gap map.

Smallest useful next falsifier: two distinct quotient-decorated sources
with the same proposed lifted image, or a target image whose small-count
parity no longer recovers which quotient data belonged to fives. Require
an actual intrinsic inverse before a broad implementation or global claim.

## Learning

Decisive obligation proved: small branch charges can be recovered by the
parity of twos and the count of sevens, while mixing the common three-sector.
Next step justified by this evidence: seek a quotient-preserving lift or
refute a specified lift; do not assume the restricted seed completes Xia's
product-side recursion. Workflow hypothesis, **unvalidated**: testing which
common factors an object map must mix may narrow a recursive discovery
problem more effectively than cancelling those factors formally. No
higher discovery rate or general harness change has been demonstrated.
