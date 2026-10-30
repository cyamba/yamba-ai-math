---
id: ETH-D04
source: sheet "10 consequences" item 5; preprint Sec. 1.1.3
category: complexity-consequences
status: audited
---

# ETH-D04: Fine-grained lower bounds that survive

| Lower bound | Original hypothesis | Still supported by |
| --- | --- | --- |
| LCS, regular-expression matching (quadratic) | SETH | **OVC** (Orthogonal Vectors Conjecture) |
| Edit distance (quadratic) | SETH | OVC via later reductions (to check per paper) |
| Frechet distance, diameter approximation | SETH | unbounded-width CNF-SAT hypothesis |
| IS / DS parameterized by treewidth (`(2-eps)^tw`, `(3-eps)^tw`) | SETH | unbounded-width CNF-SAT hypothesis |
| Hitting Set, Set Splitting (CDL16 sharp bounds) | SETH | Set Splitting with bounded set size now has subexponential algorithms; check which variants survive |
| Subset Sum pseudopolynomial (ABHS19) | SETH | open |

**Task.** For each entry record the weakest surviving hypothesis with a primary source (inspection level A).
The sheet's claim that ETH-based `n^{Omega(log n)}` hardness for dense `k`-subgraph and approximate Nash is
lost is **correct in kind** (those used ETH or stronger), but each needs its reduction checked for
variable blow-up: a quasi-polynomial lower bound derived from 3-SAT with `N = poly(n)` variables needs
`2^{Omega(N)}` hardness, which is gone, while `2^{N^{eps}}` hardness may survive.
