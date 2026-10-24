# P013 round-two proposal: one parent-edge surgery

**Conjectural construction, partial relation proved only.** Round one is
preserved in the ignored `r1.json` and `r1-source/`. Checked word surgery
repairs the old mark-step isolate but leaves new isolated negatives. No
held-out case has been evaluated. The sole allowed repair adds the following
primitive to the two existing primitives; none is removed or redefined.

Delete one parent edge of a component with composition `alpha`. Its two
decreasing subtrees must receive two nonempty consecutive blocks `beta,gamma`
of `alpha`, in either order, with the correct vertex counts. Retain every
other component and epsilon. If `r` was the old mark and the global inversion
numbers are `I_old,I_new`, enumerate precisely the bounded integer solutions

`r_beta+r_gamma = r+1+I_old-I_new`,

`1<=r_beta<=beta_1`, `1<=r_gamma<=gamma_1`.

Conversely, add a single parent edge from a root `u` to a vertex `v>u` in a
different component, where `{u,v}` is a graph edge. Concatenate those two
compositions in either order. The merged mark is uniquely forced to be

`r_joined = r_A+r_B-1+I_old-I_new`.

Keep the candidate only if this lies in the permitted first-part interval.
All inversion numbers refer to the entire reordered canonical forest word;
no locality of their change is assumed. This is a structural grammar with
scalar compensation, not unrestricted degreewise matching.

## Conditional argument and limits

**Written proof; not Lean or a proof of the conjecture.** Cutting an edge of
a decreasing tree leaves two decreasing trees. A cross-component edge from
a root to a larger vertex preserves the unique-larger-parent condition and
cannot create a cycle, so joining is valid. Cutting precisely the added edge
recovers the original parent forest. Concatenation and the indicated
composition boundary are inverse, including their order. The displayed
equations are inverse rearrangements of the full weight identity, and the
split enumerates every original mark pair in the bounds. The unchanged
composition multiset preserves type, tree count changes by one, and epsilon
is fixed, so total sign reverses. Thus the **neighbor relation** is symmetric,
valid, sign reversing and degree preserving.

The edge and composition boundary are witnesses for a legal inverse; they
are not extra labels in the signed space. Several witnesses can reach the
same state, and several sources can reach the same destination. This proof
does not establish inverse recovery of a deterministic selector or a
collision-free injection. The four selectors are priority `(mark,word,edge)`
or `(edge,word,mark)`, with first/last lexicographic target and reciprocal
selection required. Grammar-constrained matching remains diagnostic only.

The canonical-word change may be large; the scalar equation can have no
allowed mark. No argument yet guarantees a move for every negative state,
a universally recoverable pivot, or positive survivors. Those are the
decisive proof obligations. This tests an added relation, not a new proof
of an established positivity theorem. The accepted unresolved target and
all resource limits remain unchanged. A second failure ends this phase;
no third grammar repair or substantial Lean work is authorized here.
