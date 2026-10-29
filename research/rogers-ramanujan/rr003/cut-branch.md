# RR003 first intrinsic source branch from the cut family

**Proposed proved restricted branch, author-only assurance.** Mechanism B
now has an explicit weight-shifting bijection from K to an intrinsically
recognized subset of P3. Remove the compulsory two from the weight, calling
this normalized family H_(1,1). The map preserves normalized weight. This
is one branch toward

    P3 = H_(1,1) disjoint-union 3+H_(1,2) disjoint-union 6+H_(1,3),

not a proof of the other two branches or all later recursions. H_(1,3) has
the normalized L model in second-product-involution.md, but it has not been
matched to this P3 complement. No complete KR1 algorithm is claimed.

## Actual forward rule and intrinsic statistic

Let (j,D) be any actual K cut. Start with 3j copies of part3. For every
prefix part9i+7 replace it by (9i+4,3). For every prefix part9i+2, necessarily
i>=1, replace it by (9(i-1)+5,6). Leave the suffix4/5 parts and the common
three-divisible parts unchanged. Sort. All output parts lie in P3. Every
replacement preserves its original weight, and the appended threes weigh
9j. The output thus weighs |K|-2=9j+|D|.

Given any P3 partition, let t=count(3), s=count(6), u_i=count(9i+4),
v_i=count(9i+5). Put U_j=sum_(i<j)u_i. The candidate j must satisfy

    3j+U_j <= t <= 3j+U_j+u_j.

These intervals are disjoint: the next lower endpoint is three more than
the present upper endpoint. They also increase without bound. Scan them
until t lies inside one, or in one of their two-integer gaps. In a gap the
object is outside this branch. Otherwise require s>=sum_(i<j)v_i. This is
an intrinsic condition on the input; it does not enumerate partitions.

Set z=t-3j-U_j. Recover the cut by removing all threes and
sum_(i<j)v_i sixes; replace all lower-level 4-parts by 7-parts (+3),
exactly z level-j 4-parts by 7-parts (+3), and all lower-level 5-parts by
prefix2-parts (+6). Retain the other parts. Return the recovered j and D.
The distinguished copies at level j are identical, so no choice of labels
is required. Empty data and equality at either interval endpoint are allowed.

## Universal proof, cost and exact remaining obligation

In a forward image every lower-level4 came from a7, every lower-level5
from a prefix2, and level-j fours split into z former7s and unchanged
suffix4s. Thus t=3j+U_j+z, with 0<=z<=u_j, and
s=original_six_count+sum_(i<j)v_i. The disjoint-interval argument recovers
exactly the original j and z. The inverse count subtractions and residue
replacements restore every multiplicity of D, including zero boundary counts.
Conversely any partition meeting these intrinsic conditions reconstructs
a literal K cut: prefix7 indices are <=j, prefix2 indices1..j, suffix4/5
indices>=j, no literal2/3 remains, and the common parts are unchanged.
Reapplying the forward map restores it exactly. This proves validity,
complete coverage of this specified image and both inverse identities.

The scan terminates by j<=t/3+1. Counting, replacements and sorting fit
O((N+1)^2 log(N+2)) bit work and O((N+1)^2) auxiliary bits. The finite-path
auxiliary product split retains its separate exponential bound; this
polynomial branch does not improve that bound or prove a global-map bound.
The cutoff is on actual weights: pilot K<=12, P3<=10; verification K<=30,
P3<=28, so no sweep above30 is introduced by the two-unit normalization.

The decisive next lemma is a disjoint embedding of normalized L with cost6
into this complement and a literal remaining H_(1,2) branch with cost3,
then compatible analogues for all n. Those branches are not assumed from
the analytic recurrence. A smallest useful falsifier is ambiguous j,
a negative six-count remainder or a collision with the proposed L branch.
The interval gaps and the failed six inequality are exact missing cases.

Modular diagrams, Durfee-style boundary statistics and reversible residue
moves are established methods; Bridges' modular-diagram proof inspected
in recursive-source-seed.md is nearby prior work. This particular expression
was derived here, but novelty is unverified. It has no separate semantic
review. No third mechanism or critic round is introduced.

## A tempting L branch is refuted

A candidate for cost6 normalized L would append 3j+2 threes, replace prefix7
by(4,3), prefix11 by(5,6), suffix8 by(5,3), suffix10 by(next4,6), and retain
common parts. All replacements preserve weight. It loses the cut index:
L cut j=0,D=(6,6,6,8,8,8) and j=1,D=(11,11,11), each normalized weight42,
both map after cost6 to (3,3,3,3,3,5,5,5,6,6,6), weight48.
Both source cuts satisfy the exact L domain. This is an algebraic direct
counterexample, not an enumeration sweep above30. Thus valid output and
weight preservation again do not establish recoverable branch choices.
The failed L proposal is preserved; no implementation is promoted for it.

Decisive obligation proved: the K branch's cut is recovered by an increasing
interval statistic, for arbitrary cut index and increments. Actually refuted:
the displayed simple L conversion. The justified next action is to retain
that intrinsic K statistic and demand a recoverable L cut or revise the
source representation. Workflow hypothesis, **unvalidated**: a monotone
boundary interval can turn a cut parameter into an inverse statistic,
while overlapping intervals expose lost state in a competing conversion.
No higher discovery rate or complete mathematical success follows.
