# P014: fork transport across forest blocks

**Conjecture, novelty unverified.** Continue the exact height-three target
`[e_(n-4,3,1)] X_inc(P_h)(x;q)`, `n>=7`, with nonnegative first differences
through `floor(|E|/2)`. The [frontier audit](../height-three-unimodality/frontier.md)
and [P013 obstructions](../height-three-forest-surgery/results.md) remain part
of the evidence. No new unresolved theorem has been proved. The user authorized
this next phase after P013 closed; its two-round limit is not retroactively
extended.

Verified repository: `https://github.com/cyamba/yamba-ai-math.git`, branch
`codex/height-three-coefficient-unimodality`, base
`a0c897fb7bcb0d01a9ccff5593c0471424255b96`. P013 is present as uncommitted
work and is preserved along with P012, publication material and Lean proofs.
This is an additive phase, not a harness modification.

## Mathematical reduction and the necessary cross-block step

**Established, inspected primary source:** [Tom v2](https://arxiv.org/html/2311.08020v2),
Definitions 3.1/3.3 and Theorem 3.4 give the complete signed forest expansion;
Lemmas 3.11/3.13 give the tree-list bijection and maximum-insertion coordinates.
These are existing mathematics. General positivity is reported established;
the target's elementary unimodality remains conjectural in our audited record.
This phase does not perform an exhaustive new novelty survey.

Fix component vertex sets `A_1,...,A_m` ordered by minima, and compatible
ordered compositions `alpha_i` of total sorted type `(n-4,3,1)`. Write
`b_v(A)=#{u in A:u<v and {u,v} in E}`. If any nonminimum vertex has `b_v=0`,
the block is empty. Otherwise a tree list on `A` is encoded by digits
`0<=x_v<b_v(A)`: remove maxima successively, or reconstruct in ascending order
by inserting `v` at the end for digit zero, and before the `x_v`-th smaller
neighbor from the right for a positive digit. The inversion number is the sum
of these digits. Add mark coordinates `r_i-1` with capacities `alpha_i[0]-1`.
The complete block polynomial, before epsilon doubling, is

`(-1)^(3-m) q^cross(A) product_(i,v>min A_i) [b_v(A_i)]_q product_i [alpha_i[0]]_q`.

Here `cross(A)` counts graph inversions forced by the component order. No
tree, composition, mark, repeated-part multiplicity or epsilon is discarded.

**Written reduction, not a new unimodality theorem:** a product of chains has
an explicit symmetric-chain decomposition. For an old chain of length `a`
at position `x` and a new coordinate `y` of capacity `b`, put
`j=min(y,a-x)`. The new chain runs
`(0,j),...,(a-j,j),(a-j,j+1),...,(a-j,b)`, with position `x+y-j`.
Carry the old bottom-rank offset through the recursion. Pair epsilon one at
position `t<L` with epsilon zero at `t+1`; the inverse lowers the position.
This reverses sign and preserves effective degree. Bottom/epsilon-zero and
top/epsilon-one endpoints remain. Freeze the coordinate order as ascending
vertex digits component by component, followed by all marks in component order.

The P013 witness's block is `[2]_q^3 [3]_q^2 [4]_q`, with coefficients
`1,6,18,36,53,60,53,36,18,6,1`. Its degree-six first difference is `-7`,
although `6<=|E|/2=7`. Thus **no cancellation confined to this block can
cover all its negative states**, regardless of coordinate order. The witness
itself is a singleton-chain top at rank five in the frozen order. Cross-block
transport is necessary; longer within-block searches cannot remove this deficit.
This algebraic obstruction is written and separately checked, not Lean.

## Proposed universal partial relation: sibling-fork splitting

In one decreasing tree choose siblings `v<u` with common parent `p>u`.
Replace the edges `v--p,u--p` by `v--u`, making `u` a new root. The natural
unit interval property implies that `v--u` is an edge. This splits the tree
into two decreasing trees and can create a composition-sized component that
no original single-edge cut could realize. Keep other components and epsilon.

Split the old composition at any nonempty boundary. Assign its consecutive
blocks `beta,gamma` to the new components in either order with matching
sizes. If global word inversion counts are `I_old,I_new`, retain all bounded
mark solutions

`r_beta+r_gamma = r_old+1+I_old-I_new`.

For the inverse, choose two components, a root `u` in one, a child `v<u` of
that root, and a vertex `p>u` in the other with both graph edges `u--p,v--p`.
Add `u--p` and replace `v--u` by `v--p`. Concatenate the two compositions in
either order. The merged mark is

`r_joined = r_A+r_B-1+I_old-I_new`,

and must satisfy its first-part bound. Cutting and joining with the same
`(u,v,p)` recover the parent forest and the composition boundary. Increasing
parents exclude cycles; component count changes by one; the displayed
equations are inverse weight identities. This proves a symmetric, valid,
type-preserving, sign-reversing, degree-preserving **partial relation**.
It does not prove a collision-free selector, a universal pivot or positive survivors.

For the P013 isolated source `h=(3,6,6,6,7,7,7)`, parents
`(2,5,5,5,7,7,0)`, composition `(3,1,3)`, mark `3`, epsilon `1`, choose
`v=2,u=3,p=5`. The target has parents `(2,3,0,5,7,7,0)`, compositions
`((3),(3,1))`, marks `(3,3)` and epsilon `1`. Its word has inversion one
and effective degree six, matching the negative source and reversing sign.
The inverse explicitly restores the two original edges. This is an example
of the partial relation, not a universal proof.

## Frozen experiment and total boundary

The [program](../../../programs/partition-h3-forest-transport.json) uses the
harness `pair` fleet, root as lead and the separate `frontier_critic` profile.
Two proposal/review rounds, one repair, 16 declared dispatch proxy units;
no nested agents. Research is manually coordinated. Prepared packets and
any offline replay validate protocol only, never mathematical success.

Round one keeps all three P013 primitives and adds the sibling-fork relation.
Four selectors use priorities `(fork,edge,word,mark)` and its reverse, each
first/last lexicographic target. Pair only reciprocal selections. Raw states
are ordered by `(parents,compositions,marks,epsilon)` within degree, and
failures by `(n,h,degree,state)`. Require actual validity, sign, effective
degree, same-primitive inverse membership and collision accounting.

Round two permits one recorded repair: one Tom insertion digit changes by
`+1` for epsilon one or `-1` for epsilon zero, with epsilon toggled and all
other digits, marks, components and compositions fixed. Reconstruction is
valid by the insertion bijection, and degree/sign/inverse follow exactly.
Selectors use `(fork,digit,edge,word,mark)` or its reverse, first/last target.
No other move or parameter repair is allowed in this phase. The coordinate
box/SCD is a mathematical diagnostic, not a substitute for cross-block moves.

Development vectors are fixed as
`(2,4,4,6,7,7,7)`, `(3,6,6,6,7,7,7)`,
`(3,3,4,6,6,7,8,8)`, `(3,5,5,7,7,7,8,8)`.
The third is an additional size-eight boundary case selected before any P014
run; the P013 empty example is retained in its original phase, not silently
replaced there. Explicitly record the exceptional size-eight tableau sector
coverage when the independent comparison completes.

Fresh held-out cases are the first connected height-three vector at each
size 9 and 10 by ascending SHA-256 of `h3-forest-transport-v1:` plus the
comma-separated vector, excluding every frozen P012/P013 and P014 development
case. Freeze their vectors before construction tests. Evaluate them in round
two only, after development-only repair and selector lock. A capped or failed
development case makes the locked selector ineligible for a success claim.

Per round: **600 computation seconds, five million enumeration extensions,
five million candidate charges**. Per case: **120 seconds**. One enumeration
process, sampled peak RSS **2 GiB**, aggregate output-directory artifacts
**250 MiB**. These are the same conservative limits as P013, now explicitly
authorized as a new phase. Counters charge attempted and rejected moves,
inverse checks and grammar-matching traversals. Capped cases stay incomplete;
no replacements or reruns. Sampled RSS is not an OS reservation; the output
guard is not a filesystem quota. No installations or paid compute. Engineering
tests, literature inspection and protocol preparation are accounted separately.

Use the complete existing forest enumeration and independent coloring/tableau
comparisons. If there is no isolated negative, grammar-constrained matching
may diagnose saturation or a verified Hall deficiency; it is never the proof.
The smallest allowed falsifier is a seven-vertex negative lower-half state
isolated in the complete grammar, or a certified grammar Hall deficiency.

## Gates

Write and review a universal covering pivot, collision-free inverse and
positive survivors before substantial Lean. The unresolved theorem additionally
needs a bridge to the actual coloring polynomial, Lean without placeholders or
custom axioms and separate semantic acceptance. A repaired example or finite
success is evidence only. Stop after round two and preserve all failures.

Entrypoint: `python3 -m research.partitions.checks.forest_transport`.
Freeze before searching; keep bulk outputs in ignored `.runs/h3-forest-transport/`.
Run repository unit tests and `scripts/check_repository.py` after functional changes.
