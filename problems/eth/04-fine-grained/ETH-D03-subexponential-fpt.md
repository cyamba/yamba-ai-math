# ETH-D03. Subexponential FPT algorithms from linear kernels

| Field | Value |
| --- | --- |
| Category | Fine-grained / parameterized |
| Source items | "Subexponential FPT and W[1] acceleration"; "Destruction of tight $2^{\Omega(k)}$ lower bounds" |
| Status | **Vertex Cover solved conditionally**; general picture open |
| Depends on the upstream theorem | Yes |
| Score (I/B/T/L/Lean) | 3 / 2 / 4 / 2 / 3, composite **2.8** |
| Subresults | [SR-09](../subresults/SR-09-coverage-map.md) |

## Statement

Vertex Cover parameterized by $k$ is solvable in $2^{O(k\log\log k/\sqrt{\log k})}+\mathrm{poly}(n)$:
kernelize to at most $2k$ vertices (Chen, Kanj, Jia, J. Algorithms 41 (2001), via
Nemhauser–Trotter), then solve the 2-CNF plus an $O(k)$-gate counter with Theorem 1.1. The same
works for every problem with a kernel of $O(k)$ **variables** in a fixed-width SAT encoding.
Under ETH, Vertex Cover had no $2^{o(k)}$ algorithm (Cygan et al., *Parameterized
Algorithms*, Ch. 14).

## Corrections

The exponent is not $p\log\log p/\log p$, and k-Clique, Dominating Set (general) and other
W[1]- or W[2]-hard problems gain nothing: reductions go from SAT to them
([SR-08](../subresults/SR-08-corrections-to-gemini-summaries.md), row 14).

## Open parts

1. A census: which problems in the Cygan et al. ETH chapter have linear-variable kernels
   (Vertex Cover; Dominating Set on bounded-degree graphs; Max Leaf Spanning Tree?), and which
   have only quadratic kernels (Feedback Vertex Set, Cluster Editing) and stay open.
2. Can the algebraic method run directly on a kernel with $O(k)$ vertices but $\Theta(k^2)$ edges
   faster than through SAT, e.g. Cluster Editing?

## Resource boundary

One agent; census plus one or two worked encodings; Lean for the Vertex Cover reduction via
[`IndependentSets.lean`](../lean/EthConsequences/IndependentSets.lean).
