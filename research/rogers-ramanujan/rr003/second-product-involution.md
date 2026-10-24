# RR003 second explicit auxiliary product split

**Proposed proved auxiliary theorem, author-only assurance.** Inside
mechanism B the same finite-path construction gives

    ({0,1} weighted bit) times P2 <-> P1 disjoint-union L.

The packet (epsilon,p) has weight epsilon+|p|. P1 is the actual KR1 residue
family; P2 uses residues2,3,6,7 modulo9. This is an auxiliary branch split,
not a map from P1 to gap partitions. Full KR1 success and all later recursive
branches remain unresolved. No third critic round or novelty claim is made.

## Actual domain, complement and normalization

Convert a packet to a partition T by replacing every literal2 by two ones
and appending epsilon more ones; other parts stay. Thus T allows literal1,
residues3,6,7, and residue2 parts at least11. Its inverse takes the parity
of the ones count as epsilon and replaces each pair of ones by a two.
Both are literal reversible weight-preserving rules, including zero counts.

Write R_i=(1-q^(9i+7))(1-q^(9i+11)) and
S_i=(1-q^(9i+8))(1-q^(9i+10)). T has R-values and the common literal1
and three-divisible residue parts; P1 has S-values and that same common
family. The exact local identity is

    S_i-R_i = q^(9i+7)(1-q)(1-q^3).

Define L cut objects (j,D), j>=0, of weight 9j+7+|D|. D allows:

* three-divisible residues3,6 modulo9, except literal3;
* 9i+7 and9i+11 for i<=j;
* 9i+8 and9i+10 for i>=j.

There is no literal1. This is an explicit positive model for the auxiliary
((1+q)P2-P1)/q^7 in [Xia v1, (3.8)](https://arxiv.org/html/2609.08816v1),
after removing the compulsory seven charge. The analytic formula is
attribution/motivation; the maps and inverse follow from actual object rules.

## Explicit rules and universal proof

Use exactly the three layers, smallest eligible toggle, alpha/beta walk
and endpoint interfaces in product-involution.md, substituting:

| First split parameter | This split |
| --- | --- |
| P-pair (9i+2,9i+7) | R-pair (9i+7,9i+11) |
| Q-pair (9i+4,9i+5) | S-pair (9i+8,9i+10) |
| common layer2 toggle values 2,3 | 1,3 |
| compulsory charge 9j+2 | 9j+7 |
| layer0 A endpoint P2 | T, then its packet normalization |
| layer0 B endpoint P3 | P1 |
| layer2 fixed endpoint K | L |

The local singleton correspondence becomes
R:x -> charge x, S:x+1 -> charge x plus mark1,
S:x+3 -> charge x plus mark3, R:x+4 -> charge x plus both marks,
where x=9j+7. Empty local subsets cancel, as do full subsets since their
weights are both18j+18. Other prefix/suffix marks have the same definitions.
Both small toggle values1 and3 are available common denominators and never
coincide with R/S marks. The space at weight N uses L=floor(N/9)+1 cuts;
no object of weight at most N requires an index beyond it.

All nonfixed edges again preserve weight, reverse sign and are involutions:
the telescope edges retain all absolute marks; the local four-case identity
has the displayed equal weights; the smallest-toggle argument is unchanged.
Beta's fixed points are exactly positive T and negative P1; alpha's fixed
points are positive L. These exhaust all fixed points because any residual
mark or eligible denominator part is toggled. The finite degree-two graph
argument in product-involution.md therefore proves termination and the
endpoint sign argument proves:

* starting from a packet's T endpoint, the walk ends at P1 or L;
* starting from P1 or L, the reverse walk ends at T and normalizes to a packet;
* reversing that same path proves both inverse identities, disjointness,
  exhaustive packet coverage and exact weight preservation for every N.

rr003_second_product.py is a static implementation with these explicit
constants and interfaces; it does not modify the earlier frozen code,
inspect another partition list, use a rank, or retain a path transcript.
The first theorem's conservative exponential work and quadratic auxiliary
bit bounds apply. Preferred quartic work would require a contract revision
if these walks were used without a sharper bound in the final bijection.
All binding investigation caps remain unchanged.

## Limits, attribution, learning and freeze

Anti-telescoping and the involution principle retain the attribution and
inspection-depth limits recorded in product-involution.md. Novelty of these
elementary applications is unverified. Both scheduled reviews are exhausted;
this second split and the first need separate semantic review in a later
accepted research stage before use as an accepted bridge component.

The two splits supply literal positive initial auxiliary models; they do
not construct all H_(n,r), a matched gap-path decoder, or universal P1-to-gap
algorithms. The precise remaining lemma is to extend these source states
with disjoint exhaustive branch extractions realizing the full three-state
matrix for every n, with intrinsic labels and a decreasing measure. It is
not enough to cite Xia's common analytic recurrence or to add the sizes of
these auxiliary families. No complete-map complexity, Lean certificate or
article exposition has been supplied.

Freeze before weight12 verification; advance to30 only after that pilot.
Generate actual packets, P1 and L by independent paths; test validity,
weight, both identities, collisions and missing images while auditing
reached involution edges. A useful falsifier is a failed normalized inverse,
wrong residue at an endpoint or an unaccounted fixed point.

Decisive obligation supplied: the original residue family now participates
in one fully explicit auxiliary split with a recovered bit and positive
complement. Next step justified: challenge its universal finite-path proof,
then discover the later branch operations. Workflow hypothesis,
**unvalidated**: removing a finite product prefactor by a reversible parity
normalization may reveal the common small denominators needed by an
object-level cancellation. No demonstrated discovery-rate gain is claimed.
