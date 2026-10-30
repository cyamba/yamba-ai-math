# Constructive unimodality: recorded failed attempts

This ledger preserves refuted constructions, not counterexamples to the
height-three coefficient conjecture. Earlier corner-slide counterexamples,
the written two-sector cardinality obstruction and the established height-two
Lean theorem retain their original assurance boundaries in the
[partition evidence](README.md).

## P014: fork transport and insertion-digit repair

Recorded 2026-10-24 before starting P015. **Refuted:** cancellation by one
accepted direct edge of the complete frozen P014 grammar, including its sole
repair. The grammar contained mark, checked word, single-edge, sibling-fork
and insertion-digit operations. All four fixed selectors also failed.

For `h=(3,5,5,7,7,7,8,8)`, two negative degree-three states have common
parents `(3,5,4,6,7,0,8,0)`, marks `(1,1)`, epsilon zero and compositions
`((1,3),(4))` or `((3,1),(4))`. Their complete neighbor union contains only
one positive state: parents `(3,5,4,0,7,0,8,0)`, compositions
`((3),(4),(1))`, marks `(1,1,1)`, epsilon zero. Thus Hall's necessary
inequality fails, `2>1`.

Assurance: [written exhaustive argument](height-three-forest-transport/obstruction.md),
exact complete-neighborhood computation, and
[separate semantic review](height-three-forest-transport/review-r2.md).
**Not Lean.** The graph's independently coloring-checked coefficient is
`q^5(1+q)^4`; this is no unimodality counterexample. A future larger or
composite neighbor relation is not refuted by the certificate.

Valid partial fork inverses survive. The exact block calculation
`[2]_q^3[3]_q^2[4]_q` with degree-six first difference `-7`, below the
global midpoint seven, proves that purely within-block moves cannot suffice.
The remaining obligation is recoverable transport of component membership
that does not collapse the two composition orders.

[Results](height-three-forest-transport/results.md),
[compact evidence](height-three-forest-transport/evidence.json) and
[execution ledger](height-three-forest-transport/execution.json) preserve
source hashes, failures, the unrun held-out cases and the extra preliminary
review's workflow-cost deviation. P015 does not overwrite or upgrade them.

Earlier phase outcomes remain in
[P012](height-three-unimodality/results.md) and
[P013](height-three-forest-surgery/results.md).
