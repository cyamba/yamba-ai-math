# ETH-E03. Space: subexponential time with small space

| Field | Value |
| --- | --- |
| Category | Space complexity |
| Source items | "Polynomial-space (PSPACE) compression of exact exponential algorithms" |
| Status | **Open** (refinement); the source's framing corrected |
| Depends on the upstream theorem | Yes |
| Score (I/B/T/L/Lean) | 2 / 2 / 3 / 2 / 2, composite **2.2** |
| Subresults | none |

## Statement

Theorem 1.1 runs in polynomial space; the Lean formalization bounds visited cells by
$(L+1)^{O_k(1)}$. Polynomial space was always available for $2^n$ search, so the novelty is
subexponential time **with** polynomial space ([SR-08](../subresults/SR-08-corrections-to-gemini-summaries.md),
row 19).

## Tasks

1. Determine the exponent $c$ in the $n^{c}$ space bound of the overview algorithm (the
   truncated polynomial arithmetic needs $O(J)$ coefficients of $O(nR\log n)$ bits) and of the
   tensor route.
2. Time–space trade-off: can space $O(n)$ or $n\,\mathrm{polylog}(n)$ be reached with the same
   exponent?
3. Branching programs: does the algorithm yield subexponential-size branching programs for
   3-SAT (non-uniformly)?

## Resource boundary

One agent; analysis only.
