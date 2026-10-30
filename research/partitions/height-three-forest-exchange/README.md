# P015: recoverable vertex exchanges across forest components

**Target: conjecture. Novelty: unverified.** For every natural unit interval
poset of height exactly three on `n>=7` vertices, let
`c_h(q)=[e_(n-4,3,1)] X_inc(P_h)(x;q)` and `M=|E|`. The proposed universal
result is `[q^d] (1-q)c_h(q)>=0` for `0<=d<=floor(M/2)`.
This continues the user's instruction to record the failed attempt and work
on the next hurdle. The [failure ledger](../failed-attempts.md) closes P014;
its evidence, the height-two Lean formalization and publication material are
preserved byte for byte. See the [pre-scaffolding inventory](upstream.json).

Verified repository: `https://github.com/cyamba/yamba-ai-math.git`, branch
`codex/height-three-coefficient-unimodality`, base
`a0c897fb7bcb0d01a9ccff5593c0471424255b96`. Existing P013/P014 work is
uncommitted. This is an additive research phase, not a harness change.

## Inherited complete space and novelty boundary

The [frontier audit](../height-three-unimodality/frontier.md) remains the
bounded literature comparison. General positivity is reported established;
it does not establish the elementary first-difference target. The audit and
independent general-proof rebuild remain incomplete. This phase does not
certify that the selected target or a local exchange lemma is new.

[Tom v2](https://arxiv.org/html/2311.08020v2), Definitions 3.1/3.3,
Theorem 3.4 and Lemma 3.11, supplies the existing signed forest expansion
and canonical tree-word bijection. Those statements were inspected again
for this phase. The new candidate is transport in that existing space,
not a new expansion. No inspected statement is claimed to prove this target;
an exhaustive comparison of label-exchange constructions is still missing.

Retain every larger-parent forest with at most three components, every
compatible **ordered** composition tuple whose parts sort to `(n-4,3,1)`,
all marks `1<=r_i<=alpha_i[0]`, and both epsilon values. Components are
ordered by their minima. The doubled sign and degree are

`sign=(-1)^(3-number_of_components+epsilon)` and
`D=inv_G(concatenated canonical words)+sum(r_i-1)+epsilon`.

Enumerate the full coefficient before restricting doubled states to the
lower half. Reuse the exact forest enumeration and polynomial comparisons;
retain the n=8 exceptional determinant evidence, including its 32 tableaux,
from P014. Comparing a new forest census with a saved independent coloring
value is labelled reuse, not a fresh coloring calculation.

## Proposed partial inverse: move labels and their component payloads

Choose labels `a<b` in **different** tree components. Apply the transposition
`tau=(a b)` to every vertex and parent in the forest, fixing root marker zero.
Carry the entire ordered composition and mark of component `A` to `tau(A)`.
Reorder components by their new minima, and toggle epsilon. Reject the
candidate if any nonzero parent is not a larger graph neighbor, or if the
full effective degree changes. Round one permits only `b=a+1`.

**Written conditional argument, awaiting separate review:** a valid relabelled
forest has the same component sizes, composition parts and marks. Thus it
has the same type and the opposite doubled sign. Payload transport through
the component sets preserves composition order even when the sorted list of
components changes. Applying the same transposition twice restores every
parent, payload and epsilon exactly. Actual validity and equality of degree
are symmetric under this inverse. Consequently each fixed transposition is
a sign-reversing, degree-preserving partial involution. This does not prove
that different transpositions, or the union with earlier primitives, admit
a covering collision-free pivot.

The retained P014 Hall states have parents `(3,5,4,6,7,0,8,0)`, marks
`(1,1)`, epsilon zero, and compositions `((1,3),(4))` or `((3,1),(4))`.
The candidate `tau=(2 3)` gives parents `(2,4,5,6,7,0,8,0)`, carries those
respective compositions unchanged, and sets epsilon one. The resulting
component words `1246`, `3578` have inversions `34,56`, so degree remains
three. The positive targets are distinct, and the same exchange recovers
the sources. This hand calculation motivates the rule; it is not a covering
theorem or a successful held-out test.

## An adjacent-label statistic that exposes the obstruction

Assume `b=a+1`, a valid exchange, and that component order is unchanged
under the transported component sets. Within each component the relabelling
preserves all relative label comparisons, so the canonical word changes
from `w` to `tau(w)`. Let `s=1` when `a` is before `b` in `w`, and `s=-1`
otherwise. Let `B` count labels strictly between their positions in `w` of
either kind:

1. `k<a` with `h(k)=a`;
2. `k>b` with `h(a)<k<=h(b)`.

Writing `e=1` if `{a,b}` is a graph edge, and zero otherwise, the exact
inversion change is `I(tau(w))-I(w)=s*(e-B)`.
Indeed all pairs not incident to `a,b` are unchanged. The pair `a,b`
contributes `s*e`. A lower distinguishing neighbor has adjacency to `a`
but not `b`; an upper one has adjacency to `b` but not `a`, by the natural
unit interval condition. Each lying between the two positions contributes
`-s`; all others contribute zero. This exhausts the inversion pairs.

For adjacent true twins (`e=1`, identical other neighbors), `B=0`, so the
change is exactly `s`. They pair whenever `s=2*epsilon-1`. Labels 2 and 3
in the retained example are such twins. Non-twins, reordering component
minima and longer exchanges still require the full actual-statistic check.
This formula and partial relation are elementary written proof obligations,
not asserted novel results or Lean certificates.

## Frozen tests, one repair and resources

Before any research enumeration, freeze `protocol.json` and source bindings.
Development uses the four nonempty P014 cases, in increasing size/vector order:
`(2,4,4,6,7,7,7)`, `(3,6,6,6,7,7,7)`,
`(3,3,4,6,6,7,8,8)`, `(3,5,5,7,7,7,8,8)`.
They are disclosed development data, not independent new evidence.
New held-out vectors are the SHA-256-minimal connected height-three vectors
at n=9 and n=10 under prefix `h3-forest-exchange-v1:`, excluding every
P012/P013/P014 development and frozen held-out vector. Freeze the actual
vectors before construction tests. No held-out outcomes may select a repair.

The grammar includes all five final P014 groups (mark, word, edge, fork,
digit) and the new exchange group. Test four deterministic selectors:
priority `(exchange,fork,edge,word,digit,mark)` or its reverse, each with
first/last lexicographic target. Sort raw states by
`(parents,compositions,marks,epsilon)` within degree. Require reciprocal
selection, inverse recovery, actual signed-space membership and collision
freedom. Retain minimal failures by `n,h,D,state`.

The **only permitted repair** is to allow any pair `a<b` in the same
transposition rule, instead of only adjacent labels. It changes no payload
transport, statistic filter or earlier primitive. If round-one development
has a perfect reciprocal selector, leave the grammar unchanged; otherwise
record this repair before the second execution. Freeze a selector only after
all development cases complete, choosing least total unpaired negatives,
then least selector ID. Run fresh held-out cases only if that total is zero;
otherwise keep them unrun. Grammar matching is diagnostic, restricted to
the frozen union, and never a universal or unrestricted positivity argument.

The smallest immediate falsifier is an unpaired negative on the retained
eight-vertex vector. A selector failure refutes that selector; a negative
isolate or a verified complete-neighborhood Hall deficiency refutes the
whole direct-edge grammar. Repairing the old two-state subset does not
establish coverage of the rest of that signed space.

Use root as lead and one separate critic, no nested agents or extra critic
preflight. Two formal proposal/review rounds, at most one repair; six formal
stages cost 16 declared dispatch proxies. No provider tokens or money are
inferred from this tally. Each round has 600 computation seconds, five
million extensions and five million candidate charges; each case has 120
seconds. One enumeration process, sampled RSS 2 GiB and aggregate output
directory 250 MiB. Charge attempted/rejected exchanges, inverse checks and
matching traversals as well as accepted moves. Capped cases remain incomplete
and are never replaced or silently rerun. Stop at either budget or round limit.
No installs, new dependencies or paid compute.

Engineering unit tests, input hashing, protocol generation, primary-source
reading and semantic review are recorded separately from research counters.
Memory is sampled high-water RSS, not an OS reservation; the output guard
is not a filesystem quota. Preserve historical source snapshots and receipt
hashes. Substantial Lean work remains gated on a credible universal covering
argument, the actual-coloring bridge and separate semantic acceptance.
