# Final pass: recurrence branch constraints

Status: exact algebra and counterexamples, author argument; no complete
recurrence bijection. Novelty unverified. This note uses Xia v1
https://arxiv.org/html/2609.08816v1 (3.1)–(3.9) and the positive word model
in [general_positive_divided_differences.md](general_positive_divided_differences.md).

## Exact positive row

For Xia's product-side sequences, define B_n=C_n+q^(3n+2) A_(n+1).
Equation (3.1) is equivalent to the positive row

    C_n = A_(n+1) + q^(3n+3) B_(n+1) + q^(6n+6) C_(n+1)
        = A_(n+1)
          + q^(3n+3) C_(n+1)
          + q^(6n+6) C_(n+1)
          + q^(6n+8) A_(n+2).

This is an identity of generating functions established within Xia's claimed
analytic argument; it is not here promoted to a bijection. The problem is to
split each C_n positive word intrinsically into the four disjoint positive
branches with explicit inverses. The established all-n positivity does not
itself give this split.

The common tail changes with n: for `T_n=product_{j>n,3∤j}(1-q^(3j))^-1`,
`T_n/T_(n+1)=(1-q^(3n+3))^-1` if 3∤(n+1), and 1 otherwise. When
3|(n+1), the locked terminal delta count increases instead. A word operation
must therefore handle the periodic change in state and cannot rely solely on
extracting an extra common part 3n+3.

## Constraint for color-preserving cut insertion

A C_n particle of color α or β in layer i has base, respectively,
`3n+4+3i` or `6n+5-3i`. A_(n+1) bases are
`3n+2+3i` and `6n+7-3i`. Insert a new cut anywhere in a C_n word, preserving
all particle colors and relative order. For a particle to the left of the
inserted cut, its layer is unchanged; for one to the right, its layer rises
by one. Hence its A_(n+1)-minus-C_n base change is

    α left: -2;  β left: +2;  α right: +1;  β right: -1.

Writing D_L=#α_left−#β_left and D_R=#α_right−#β_right, the total base
change is `-2 D_L+D_R`, congruent to total color imbalance
`D_L+D_R (mod 3)`. Index/gap changes, including the weight of the new cut,
are multiples of 9; common-tail changes are multiples of 3. Therefore any
weight-preserving map in this restricted model requires total color imbalance
divisible by 3. This is not a no-go theorem for color-changing moves,
particle creation/deletion, or nonlocal transfer.

The necessity of color change is already forced by the complete row at n=0,
weight 4: the C0 object `(4)` consists of one α particle. The sole possible
RHS object is in A1, cut 0, layer-1 β particle of weight 4. The q³ C1 and
q⁶ C1 branches have empty-word weights 3 and 6 and their first particle has
weight at least 7; q⁸ A2 starts at weight 8. Thus no full recurrence map
preserving colored-particle labels can exist, regardless of index transfer.

A natural color swap and prepend-zero-cut sends old layer i to i+1 and swaps
α,β. Its A_(n+1)-minus-C_n base change is `+3(n−2i)` per old α and the
negative of this per old β. It works without base repair at n=0, giving the
known no-literal-3 P3→A1 subfamily, but generally needs imbalance-dependent
compensation and may disrupt locked suffix gaps.

## Particle count must change

The recurrence cannot be realized by word cyclic rotation, boundary transfer,
complement, or any other operation that preserves the number of α/β
particles, even allowing arbitrary changes of cut indices, colors, and
common-tail particles. At n=0 and total weight 8, C0 has exactly one object
with one colored particle: the β particle 5 and the common part 3. The only
other C0 object is `(4,4)`, with two colored particles.

On the RHS, A1 has no one-particle object of weight 8: its possible node
particle weights start 4,5,7; common parts start at 6; each positive cut
index costs at least 9. The q³C1 branch has no one-particle object below 10;
the q⁶C1 branch has none below 13; and q⁸A2's empty object has zero colored
particles while every nonempty object has positive weight. Consequently the
source one-particle object has no one-particle destination. A valid global
recurrence bijection must sometimes create or remove colored particles and
transfer their weight to branch charges or common parts. This is an exact
small counterexample, independent of the analytic sum-product identity.

No forward/inverse map overcoming these constraints is supplied. Existing
RR003 H11/K branches and the two collision counterexamples are recorded in
[recurrence-experiments.md](recurrence-experiments.md).
