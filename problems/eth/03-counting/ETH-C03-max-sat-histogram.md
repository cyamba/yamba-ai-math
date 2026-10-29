# ETH-C03. The exact Max-k-SAT clause histogram, and dense Max-2-SAT

| Field | Value |
| --- | --- |
| Category | Counting / optimization |
| Source items | "YMB-ETH-07: polynomial-space Max-3-SAT via the algebraic certificate"; preprint Cor. 1.2 |
| Status | **Solved conditionally at bounded density** (SR-07, Cor. A); **dense case open and important** |
| Depends on the upstream theorem | Yes |
| Score (I/B/T/L/Lean) | 4 / 4 / 2 / 3 / 3, composite **3.4** |
| Subresults | [SR-07](../subresults/SR-07-graded-counting-bounded-density.md); Lean `Graded.histogram_identity`, `deformation_identity` |

## Statement

For $m\le Dn$ the full histogram $h_j=\#\{x:\mathrm{viol}(x)=j\}$, hence exact Max-$k$-SAT and the
number of optima, is computable in $2^{O_{k,D}(n/\sqrt{\log n})}$ (SR-07). The source's identity
$\sum_x\prod_e(1+t(\Phi_e-1))=\sum_jh_j(1-t)^j$ is correct (Lean `deformation_identity`), but
its algorithmic use through the general reduction fails: sparsification and variable copying
preserve satisfying assignments, not violation counts.

## The open problem

**Exact Max-2-SAT (or Max-Cut) on $n$ variables with $m=\omega(n)$ clauses in $2^{o(n)}$ time.**
The best known is Williams's $O^*(2^{\omega n/3})$ with exponential space (TCS 2005, level T). The
preprint's Corollary 1.2 gives only an additive $\varepsilon m$ approximation. Possible routes:

1. A sparsification that preserves the number of violated clauses approximately enough for an
   exact finish (e.g. a sparse "certificate" of the optimum plus exact local search).
2. Apply the deformation directly to dense quadratic forms: the product
   $\prod_{e}V^{[\text{violated}]}$ has degree $m$, not $O(n)$, so Taylor recovery is too costly;
   a degree-reduction analogous to the parity lift for counting violations mod $2^\ell$ is needed.

## Closest work

Williams, "A new algorithm for optimal 2-constraint satisfaction and its implications", TCS
348 (2005) (level T); preprint Cor. 1.2 (level T; R039).

## Smallest falsifier

A fine-grained reduction showing that $2^{o(n)}$ dense Max-Cut implies a $2^{o(N)}$ algorithm for
a problem believed harder (e.g. $\#$Max-2-SAT with large weights) would indicate a barrier.

## Resource boundary

Two agents (degree reduction for violation counts; literature on dense Max-CSP), one critic.
