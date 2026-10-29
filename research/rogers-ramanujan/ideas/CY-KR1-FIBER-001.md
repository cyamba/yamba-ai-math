# Christopher Yamba intuition: fiber splitting through extra dimensions

ID: CY-KR1-FIBER-001. Received 2026-10-25. Author of intuition:
**Christopher Yamba**. Status: **CONJECTURAL APPROACH; exploration authorized**.
No complete KR1 bijection or novelty claim is established by this record.

## Original wording

> #KR1BIJECTION
>
> Chris idea for resolving the GAP on phase 2
>
> What if we investigate the fiber counts that is - we see that input in domain A T1 and T2 maps to the same output U in codomain B.
>
> But what if we consider the U as an ambiguous image that needs to be split into two distinct images U1 and U2.
> Each of these maps : T1<->U1 and T2<->U2. So we need to figure out how to construct these two
> And then generalise this for all cardinalities of the fibers.
>
> So if T1..TN for count N inputs then we need N outputs that can be systematically constructed from the Ui, i=1..N in B so that we have a complete bijection.
> My first naive intuition would be to consider the squares in T:s in A {4,5} notice the switch places.
> So how can we reflect this on the U?
> Can we just introduce one new dimension at a time in a systematic way and consider each iteration as a unique Ui that maps to Ti?
> For each extra dimension we can see if we find uniqueness and ordered way of placing the numbers (consider it a permutation structure of some sort in multiple dimensions) if there is no solution we add a new dimension and find a ordered way of placing the numbers that folles the rule(s) and produces a

The last sentence was unfinished in the supplied message; it is not silently
completed here. Christopher then explicitly requested trying variations
toward the full bijection. The accompanying sketch is the two-tableau
collision discussed in the preceding session explanation.

## Operational interpretation

Use X,Y for generic source/target sets, avoiding confusion with the fixed
KR1 endpoint names A and B. For a many-to-one coarse move f, study each fiber
f^-1(u), identify the lost order/position data, and encode that data in
distinct valid original target objects of the same weight. Higher-dimensional
tableaux are a proposed construction space in their own right. If they form an
intermediate class, a reversible translation to the required target remains
an obligation; no particular flattening rule is assumed.

Required checks: enough target capacity for each fiber, disjoint allocations
between fibers, an intrinsic inverse, correct weight/statistic, termination,
and exhaustive coverage. Bare labels or permutations of indistinguishable
boxes do not themselves create new unmarked KR1 target partitions.

The pictured tableaux form a separate cancellation problem. Their local
fiber repair can motivate a KR1 construction, but does not itself prove it.

## Christopher's clarification: minimum dimension first, 2026-10-25

Status: **CONJECTURAL; this exact procedure has not been implemented or tested**.
The previous shape-routing and column-carry variants were related explorations,
not a direct test of this dimension-increasing construction.

For a coarse fiber containing m inputs (for example, ten):

1. Work with arrangements of the actual numbered yellow entries, retaining
   the differences between the input permutations.
2. Define admissible generalized tableaux in dimension d, including their
   coordinate orders, label rules, axis conventions and required statistic.
3. First seek some finite d permitting distinct admissible arrangements for
   all m inputs, compatible with the input data. Christopher subsequently
   clarified that existence comes first: minimal d is an optional later goal.
4. Give an exact deterministic selection rule among the available placements
   and assignments. The output must determine its dimension and placement
   intrinsically, so the reverse procedure recovers the particular input.
5. Prove that some finite d always works, and that both algorithms terminate,
   preserve the required statistic, and are mutual inverses.

This would settle the requested bijection only with the remaining global
conditions: outputs from different fibers must be distinct, and the output
class must cover exactly the required Phase 2 target family. If generalized
tableaux are an intermediate class H, also construct the bijection H to that
target. Minimality specifies a choice only after existence is established,
and is not required for a bijection.

### Further clarification: existence first, 2026-10-25

Christopher does not require a unique construction, a unique admissible
placement, or a proof of optimal dimension. The immediate proposed milestone
is existence of at least one uniform procedure whose selected outputs are
distinct and reversible in every case. Many alternative procedures or
placements may work. For the original explicit-bijection objective, an
existence-first argument must ultimately supply an explicit construction.

His suggested starting case is ten colliding inputs separated using ten
additional dimensions. Distinguishable extra axes can store the input choice:
formally, for an indexed fiber, T_i maps to (u,e_i), where e_i is the ith
coordinate unit vector. This elementary encoding separates the ten inputs
in an enlarged decorated class; it does not by itself show that the objects
are admissible generalized tableaux or original target objects. If axes are
identified under symmetry, their ability to distinguish inputs must also be
checked rather than assumed.

Higher-dimensional intermediate objects do not violate the problem. The
outstanding bridge is a reversible statistic-preserving correspondence with
the required original target family, with exact coverage and disjointness
between fibers. Literal geometric flattening is not required. Simply deleting
the distinguishing coordinates would restore the original collision. For
KR1 the endpoints are ordinary partitions; the separate signed-tableau
cancellation task has its own prescribed positive targets and graph-inversion
statistic. Success on an enlarged intermediate family alone settles neither.

This is a clarification and elementary encoding example, not a new proof run
or a claim that the full KR1 bridge has been constructed.

## Further suggested outline: record reversible cube permutations, 2026-10-25

Christopher proposes recording placements of the numbered squares as
reversible operations over a discrete multidimensional cube/tableau,
retaining every assignment and analyzing the possible arrangements for a
general pattern. He calls this a possible "hypergeometric permutation
arrangement." He requested an outline before an attempt.

[Suggested outline: states, operations, assignment ledger, pattern analysis,
intrinsic decoding, and the original-target bridge](CY-KR1-FIBER-001-OUTLINE.md).
Status: **SUGGESTED; UNTESTED**. The ledger must help discover an inverse;
it cannot silently become extra data required by the original target family.

Next investigation: start from this recorded cube/permutation outline;
do not silently replace it with further ordinary shape or column formulas.

## Active investigation

[Fresh isolated attempt and resource contract](../fiber-splitting-20261025/contract.md).
The first variants are reversible shape routing for tableau fibers, and
weight-funded column-multiplicity encoding for the remaining KR1 band.
Results and failures will be recorded separately from this original intuition.

## First checkpoint, 2026-10-25

[Result and next lemma](../fiber-splitting-20261025/RESULT.md).
The related shape-routing and column-encoding variants produced explicit
extensions of the exact reviewed H3 map to
the entire a=4,b=0,y=2, y=3 and y=4 slabs, and funded portions of y=5..17.
Assurance: ordinary proofs with distinct semantic review, conditional on H3;
no Lean certificate or novelty claim. Full KR1 remains open. The pictured
ordinary-tableau fiber also admits an explicit arbitrary-fiber-size repair,
but its naive extension to graph-weighted P-tableaux was refuted.

One proposed Y3 boundary formula was refuted by a collision with retained
f1 third-12 at weight 22, then replaced by six disjoint literal-output
languages. The failed formula and witness remain in the evidence; they are
not erased by the successful revision. Final combined finite checks keep
all 3498 old assignments and add 476 through 40, for 3974 of 5461 total states.
These finite counts do not substitute for the written infinite arguments.
