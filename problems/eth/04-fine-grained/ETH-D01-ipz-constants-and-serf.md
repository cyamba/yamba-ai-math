# ETH-D01. The IPZ constants $s_k$ and the SERF class

| Field | Value |
| --- | --- |
| Category | Fine-grained complexity |
| Source items | "Total collapse of the IPZ sequence"; "Subexponential collapse of the entire SERF-complete class"; "SERF hierarchy collapse" |
| Status | **Conditional consequence; map done** (SR-09); refinements open |
| Depends on the upstream theorem | Yes |
| Score (I/B/T/L/Lean) | 3 / 1 / 4 / 3 / 3, composite **2.6** |
| Subresults | [SR-09](../subresults/SR-09-coverage-map.md) |

## Statement

Impagliazzo and Paturi define $s_k=\inf\{\delta:k\text{-SAT}\in\mathrm{DTIME}(2^{\delta n})\}$ (JCSS
2001); ETH is $s_3>0$. If Theorem 1.1 holds then $s_k=0$ for every fixed $k$. Problems complete
for SNP under SERF reductions (IPZ, JCSS 2001: $k$-SAT, $k$-Colorability; size-constrained:
Independent Set, Vertex Cover, Clique, $k$-Set Cover) inherit $2^{o(n)}$ algorithms through
reductions with linearly many variables.

## Corrections

* IPZ's abstract lists the problems as SNP-complete, while the body distinguishes
  size-constrained SNP; Hamiltonian circuit is only SERF-hard (SR-08 row 13).
* $s_k$ is non-decreasing and, under ETH, increases infinitely often; it is not shown to increase
  at every $k$ (citation check).

## Open parts

1. Make the SERF membership of each named problem explicit with the parameter used (vertices,
   edges, universe size) and the resulting exponent; SR-09 does this for the main ones.
2. Is $k$-Set Cover with universe size $n$ and **arbitrarily many** sets covered? (The witness is
   a set of sets, not linear in $n$.)

## Resource boundary

One agent; documentation-level.
