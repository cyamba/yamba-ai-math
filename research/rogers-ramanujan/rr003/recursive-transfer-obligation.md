# RR003 focused recurrence comparison after the two reviews

**Established gap branches; unproved residue-side branch proposal.** This is
further discovery within mechanism B, not a third mechanism, additional
review round or claim that a numerical recurrence defines a bijection.

## A three-state form of the inspected seven-tail grammar

For n>=0 let G_(n,r), r=1,2,3, consist of actual gap partitions with minimum
part at least 3n+r. Put x=3n+1,y=3n+2,z=3n+3. Strip all parts at most z.
The tail branches are exactly:

* r=1: empty, (x), (y), (x,y), (z), (x,z), (z,z).
* r=2: empty, (y), (z), (z,z).
* r=3: empty, (z), (z,z).

When the tail has no z the residual is in G_(n+1,1), when it has one z it
is in G_(n+1,2), and when it has two z's it is in G_(n+1,3). These follow
from the literal adjacent-sum and distance-two predicates. They are an
aggregation of [Chern–Li's previously inspected linking states](https://arxiv.org/html/1809.08655v3),
not a newly discovered gap recurrence. Every branch is disjoint, exhaustive
and inverted by reinserting its displayed tail. Empty partitions terminate
canonically; otherwise max(part)-3n decreases by three on every recursion.
Thus there is a genuine recoverable gap path code, including base cases.

Its transfer matrix in these three states is

    [(1+q^x)(1+q^y), q^z(1+q^x), q^(2z)]
    [1+q^y,         q^z,        q^(2z)]
    [1,             q^z,        q^(2z)] .

The seven, four and three monomial branches, including multiplicity of
possible equal weights, remain distinct literal tails. A matrix entry is
not used to choose a branch by numerical ranking.

## Closest newly inspected analytic construction

[Xia v1, section 3, equations (3.1)–(3.9)](https://arxiv.org/html/2609.08816v1)
uses this positive matrix for three Nahm-sum sequences. The product-side
sequences are expressed by divided differences with finite factors; their
recurrences are proved analytically in section 4. Lemma 2.2 provides a
positive expansion for the divided difference itself, while the prefactors
include (q^3;q^3)_n. I inspected these formulas and their surrounding
arguments, not the full analytic certificates. This does **not** identify
literal source partitions or recoverable residue branches.

The concrete advantage of this comparison is a small positive target branch
system with already proved inverse branches. It replaces a vague request
for “some matching recurrence” by the following exact mathematical obligation.

## Precise source-side conjecture, inverse and smallest falsifier

Find literal, intrinsically recognizable auxiliary source families H_(n,r)
and explicit bijective decompositions with the exact tails/weight offsets
of the matrix above, starting with H_(0,1)=the KR1 residue family. A branch
must be recoverable from its residual and fixed finite label, not from a
saved transcript. Supply a finite decreasing measure for the extraction
and an explicit base case. Reinsert branches to define the inverse path
map, then use the proven gap path decoder. The first source branch rule
is **not yet known**; neither positive matrix coefficients nor the inspected
product-series formulas supply it.

A useful falsifier is one source object fitting two proposed branches,
one uncovered source object, a weight mismatch including state shifts,
or a residual whose branch label cannot be recovered. The already refuted
same-cutoff/length-preserving proposal is preserved in recursive-discovery.md.
The repaired zero/one/two-one family is a genuine restricted map, not a
proof of these larger auxiliary families. A signed cancellation approach
would additionally require actual terminating weight-preserving involutions
and identified unmatched objects; formal cancellation is insufficient.

A related primary source, [Scrimshaw, arXiv:1505.05910](https://arxiv.org/abs/1505.05910),
gives crystal–rigged-configuration bijections in type D4^(3). Its abstract
and the corresponding FPSAC paper's algorithm statements were inspected
as leads only. No identification of RR003's literal U or B with the required
crystals, no vacancy-number match to C, and no endpoint adapter were proved.
This is not a license to cite a crystal theorem as the missing KR1 map.
It is comparison material within the auxiliary-state proposal, not a third
mechanism or an implemented dependency.

## Learning and next step

Decisive obligation: a positive **object-level** source decomposition with
recoverable branch choices. Actually established here: the exact target
branches and the distinction between them and an analytic common recurrence.
The next justified step is to propose one source branch and prove its
injective extraction before implementing the whole recurrence. Workflow
hypothesis, **unvalidated**: comparing an existing analytic transfer matrix
with literal branches may isolate a smaller discovery target. No measured
workflow improvement, general harness redesign or changed success criterion
is claimed. Full residue–gap coverage remains unresolved.
