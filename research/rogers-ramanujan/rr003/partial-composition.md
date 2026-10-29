# RR003 restricted residue–gap composition

**Proposed proved restricted bijection; author-only assurance.** The code
rr003_partial.py composes the unit-normalized Stockhofe endpoint, the final
a<=2 column embedding, and the direct gap–cluster merge. The complete KR1
bijection remains unresolved. Both scheduled critic reviews preceded these
final extensions, so none is represented as a separately accepted bridge.
Novelty is unverified; the endpoint constructions are attributed in their
respective proof records. Lean certification and article exposition remain
subsequent obligations, not purported executions.

The literal gap domain consists of all gap partitions whose intrinsic split
into close pairs and singles has **at most two singles**. There may be
arbitrarily many pairs, arbitrary increments, and unbounded weight. Close
pairs are disjoint by the distance-two rule. The literal residue domain
consists exactly of those residue partitions whose explicit Stockhofe
column image is recognized by the final a<=2 inverse. Membership is an
algorithm on the input itself, with no enumeration, rank or hidden lookup.
Neither restricted domain is asserted to be the whole family.

Forward residue-to-gap: run residue_to_columns, then decompose_columns,
then cluster_to_gap. Inverse gap-to-residue: run gap_to_cluster, then
reconstruct_columns, then columns_to_residue. Unsupported valid objects
raise OutsideRestrictedDomain. Malformed objects remain ordinary validation
failures. Empty input is supported in both directions.

Every component has a written weight-universal argument in
endpoint-stockhofe.md, round-2-revision.md and endpoint-cluster-merge.md.
Their stated domain and codomain interfaces match exactly. Composing their
validity, weight, termination and inverse identities therefore gives all
those properties for this restricted map at the same **author-only** proof
assurance. Its conservative work is O((N+1)^2 log(N+2)) bit operations and
auxiliary space O((N+1)^2) bits in unary weight N; no complexity-target
revision is needed. A finite end-to-end run will check both actual domains,
weights, collisions, missing restricted images and both inverse identities.
These finite checks are exposure, not universal proof or independent review.

A precise omitted gap object is (1,3,5), weight nine: it has three singles,
C=(3,0,(0,0,0),()). A precise omitted residue object is (3,6), weight nine:
its Stockhofe columns are U=(6,3), outside this embedding's image. These are
witnesses of incomplete coverage, not claims that a complete map is impossible.
The independent restricted small-charge map in recursive-repair.md can map
some objects outside this image; it is a different partial construction and
is not silently combined with this one, since their assignments can conflict.

Decisive remaining lemma: extend or replace the U–C construction with a
single disjoint exhaustive decomposition for arbitrary a, recovering a,b
intrinsically from U. Alternatively mechanism B needs an object-level
source branch adapter as specified in recursive-transfer-obligation.md.
Nothing about the composition changes that governing objective.

Workflow hypothesis, **unvalidated**: checking an explicit partial composition
on the actual endpoints can expose interface errors hidden by intermediate
round trips. It does not establish a higher discovery rate or a general
harness improvement.
