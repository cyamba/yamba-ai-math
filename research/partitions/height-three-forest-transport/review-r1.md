# P014 first proposal review: block reduction and fork transport

Date: 2026-10-24. Reviewer: separate `frontier_critic` role. This is the
first of at most two P014 proposal/review rounds. Earlier insertion-coordinate
analysis was preflight, not another review round. This review covers the
written proposal and program contract. Computational outcomes are pending;
no implementation execution, enumeration, search, test or Lean run by this
reviewer is asserted. No nested agents were used.

**Verdict: supported conditional relations and written block obstruction;
universal covering construction incomplete.** The insertion-coordinate
bijection, specified symmetric-chain reduction and sibling-fork inverse
are mathematically sound under their stated conditions. The displayed fork
does pair the retained P013 isolate. None establishes a global pivot,
collision-free injection or positive endpoint family. The frozen experiment
may proceed within its declared two-round boundary; it cannot claim success
from the repaired example or the conditional inverse alone.

## Proposal and source boundary

The reviewed [README](README.md) has SHA-256
`32134439f3395b7859e1edb4d94e1f3dea8ed66de4f032695a3176211533ad4e`;
the [P014 contract](../../../programs/partition-h3-forest-transport.json)
has SHA-256
`a7568e09cf202d16e564233a4ab9a57773183d9e173cde849bc676b382125718`.
These identify the written proposal, not an executed program or a frozen
JSON test receipt. The repository base remains
`a0c897fb7bcb0d01a9ccff5593c0471424255b96`, branch
`codex/height-three-coefficient-unimodality`, with P013 preserved as
uncommitted work. This review edits only its own new phase artifact.

[Tom v2](https://arxiv.org/html/2311.08020v2), Definitions 3.1/3.3 and
Theorem 3.4, supplies the complete signed model. Lemmas 3.11/3.13 supply
tree-list recovery and maximum-insertion coordinates. These are established
mathematics, not new results of P014. The source was inspected during this
continuous investigation. The general-positivity and elementary-unimodality
distinction in the retained frontier audit remains applicable. Novelty of
the target and of any successful fork construction remains unverified;
neither a new exhaustive survey nor a theorem claim is supported here.

## Within-block bijection and symmetric-chain reduction

Fix component vertex sets in minima order and compatible ordered
compositions. Inter-component inversions are then constant. For each
nonminimum vertex `v` in a component `A`, set

\[
 b_v=|\{u\in A:u<v,\{u,v\}\in E\}|.
\]

Deleting maxima leaves the relative order of all smaller vertices
unchanged. The coordinate `x_v` counts the smaller neighbors after `v`.
In the inverse construction, zero inserts `v` at the end and positive
`k<b_v` inserts it immediately before the `k`-th smaller neighbor from
the right. Excluding insertion before the earliest neighbor is essential;
the range is `0,...,b_v-1`, not `0,...,b_v`. The valid-tree-list bijection
and insertion lemma give exact recovery and inversion sum `sum_v x_v`.
Different trees are retained as distinct coordinate vectors.

If a nonminimum vertex has `b_v=0`, the block is empty; it cannot be turned
into a zero-capacity coordinate. Singletons contribute no tree coordinates.
Adding the mark coordinates `r_i-1` gives precisely the proposed shifted
product of chains, with raw sign fixed by the number of components.
The empty product has one coordinate vector. Composition assignments and
equal-part multiplicities remain those of the raw signed space.

The rectangle recursion is a genuine decomposition, not merely a path
through some points. Given `(x,y)` in `[0,a] x [0,b]`, set

\[
 j=\min(y,a-x),\qquad t=x+y-j.
\]

If `y<=a-x`, the point is on the horizontal segment of chain `j`; otherwise
it is on its vertical segment. The common corner is counted once. The
inverse from chain label and position is

\[
 (x,y)=
 \begin{cases}
 (t,j),&t\le a-j,\\
 (a-j,t-a+2j),&t>a-j.
 \end{cases}
\]

For an old symmetric chain with bottom rank `R` in a product of total
capacity `S`, its length is `a=S-2R`. The new bottom rank is `R+j`, and
the new top is `(S+b)-(R+j)`. Carrying this offset proves symmetry after
each recursion. Chain identifiers and offsets must be retained for exact
recovery; a rank alone does not determine a coordinate vector.

For a resulting chain of length `L`, epsilon one at position `t<L`
pairs with epsilon zero at `t+1`. Its inverse lowers the position.
The coordinate rank rises by one while epsilon falls by one, so effective
degree is unchanged and sign reverses. Equal degree keeps the pair inside
or outside the lower-half restriction together. Bottom/epsilon-zero and
top/epsilon-one remain, including both distinct endpoints when `L=0`.
This is a universal interior involution, not a positivity proof.

The explicit negative endpoint deficit is correct. On the P013 one-tree
block with composition `(3,1,3)`, the unsigned polynomial is
`[2]_q^3 [3]_q^2 [4]_q`, with coefficients
`1,6,18,36,53,60,53,36,18,6,1`. The doubled degree-six count is
`53-60=-7`, below the global midpoint seven. Every symmetric-chain
decomposition has seven singleton chains at rank five, so coordinate
reordering cannot eliminate this aggregate deficit. In the frozen order,
the displayed witness has capacities `(0,1,1,2,3,1,2)` and coordinates
`(0,0,0,2,0,1,2)`; the final chain has bottom rank five and length zero.
The cross-block obligation is therefore proved, not inferred from a
failed finite selector. The SCD remains an analytic diagnostic in this
experiment and must not be reported as an active tested primitive.

## Sibling-fork validity, inverse and weight

In a decreasing tree, let `v<u` have the common parent `p>u`. The proposed
new edge exists: `v<u<p` and `{v,p}` imply `{v,u}` in a natural unit
interval graph. This use of the graph assumption is necessary. Removing
`u->p` and changing `v->p` to `v->u` collects the former descendant
subtrees of `u` and `v` into one component rooted at `u`; the remainder
stays connected to the old root. Both components are decreasing trees.

Conversely, `u` must be a root of one component and `v` its **direct**
child. For `p>u` in a different component, require both graph edges
`{u,p}` and `{v,p}`. Adding those two parent edges and deleting `v->u`
joins the components and recovers siblings with parent `p`. Increasing
parents and the component separation exclude cycles. Reusing the same
triple `(u,v,p)` reverses the operation exactly.

Every nonempty composition boundary, both assignments to the two vertex
sets, and all bounded mark solutions must be retained. The equation

\[
 r_A+r_B=r+1+I_{\rm old}-I_{\rm new}
\]

is exactly the global weight identity, and the joined-mark equation is
its inverse rearrangement. It can have no bounded solution; graph
validity does not guarantee degree-preserving transport. Epsilon must
stay fixed for fork surgery: the component-count change already reverses
the raw sign, and toggling epsilon would reverse it a second time.
All other component payloads remain unchanged, but their relative word
positions can change when minima reorder, so inversion changes must be
computed on the entire forest word.

These facts prove a symmetric, valid, type-preserving, sign-reversing,
degree-preserving **partial relation**. The chosen fork, composition
boundary and mark pair are inverse witnesses, not extra labels in the
signed objects. Several witnesses or sources can share a destination.
Thus a deterministic selector needs a separate inverse and collision
argument; no universal existence or pivot follows from this lemma.

The numerical pairing checks exactly. In the P013 source choose
`v=2,u=3,p=5`. The target parent vector
`(2,3,0,5,7,7,0)` has components `{1,2,3}` and `{4,5,6,7}`, with
canonical words `1,2,3` and `4,5,7,6`. Its only inversion is `{6,7}`.
Use the boundary `(3,1)|(3)` with reversed assignment: the first component
receives `(3)` and the second `(3,1)`. The required mark sum is
`3+1+3-1=6`, forcing marks `(3,3)` in their allowed intervals. Hence the
target degree is `1+2+2+1=6`, and its sign is positive, opposite the
source. Using only the first composition boundary would miss this pair.
The inverse with root `3`, child `2` and other-component vertex `5`
restores the exact source.

## Prioritized obligations before interpreting computation

1. Freeze the JSON protocol, four development vectors, two held-out
   vectors, selector priorities and ordering before search. The new
   size-eight development case is additional P014 coverage; P013's empty
   case stays preserved in its original record. Its exceptional tableau
   sector must be explicitly checked rather than presumed nonempty.
2. Implement the complete raw signed space and candidate relation. Count
   attempted and rejected forks, inverse triples, composition assignments,
   mark tests, inverse-membership checks and grammar diagnostics. Validate
   actual parent forests and global degree; do not replace inverse
   membership with an assumption that the witness data will be recovered.
3. Keep reciprocal-selector failures and collisions separate from a
   full-grammar isolate or certified Hall deficiency. Sibling forks may
   have no eligible sibling pair or size-compatible boundary, and mark
   bounds may fail. No covering lemma rules out these structural failures.
4. If development justifies the sole round-two repair, a one-unit Tom
   digit change with epsilon toggle is valid and reversible by the
   insertion bijection. It remains within the same block and cannot by
   itself remove its `-7` deficit; it may expose a state that admits a
   cross-block move. No other repair or parameter tuning is allowed.
5. Lock the development-chosen selector before held-out work. A failed or
   capped development case makes it ineligible for success; caps remain
   incomplete and receive no replacements or reruns. Two review rounds,
   one repair, one enumeration process and the declared per-round
   600 seconds, five million extensions, five million candidate charges,
   120 seconds per case, sampled 2 GiB RSS and 250 MiB output-directory
   boundaries remain binding. Protocol preparation and engineering checks
   are separately accounted work, not missing research receipts.

The next decisive check is complete bounded testing of the fork relation
on the frozen development space, retaining the smallest full-grammar
failure if one occurs. No computational result is supplied by this review.
A universal covering pivot with positive survivors and a collision-free
inverse remains the mathematical gate before substantial Lean work. The
unresolved target also requires the actual coloring bridge and separate
semantic acceptance; this proposal does not satisfy that final gate.
