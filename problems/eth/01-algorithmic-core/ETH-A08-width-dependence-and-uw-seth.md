# ETH-A08. Dependence on the clause width and the unbounded-width frontier

| Field | Value |
| --- | --- |
| Category | Algorithmic core / fine-grained |
| Source items | "YMB-ETH-06: the UW-SETH phase transition $k(n)$"; "Refutation of fixed-width SETH vs re-anchoring to UW-SETH" |
| Status | **Partially solved conditionally** (SR-09); frontier open |
| Depends on the upstream theorem | Yes |
| Score (I/B/T/L/Lean) | 3 / 3 / 3 / 3 / 2, composite **2.9** |
| Subresults | [SR-09](../subresults/SR-09-coverage-map.md#the-clause-width-frontier) |

## Task

Find the largest width $k(n)$ for which $k(n)$-SAT (any number of clauses) is solvable in
$2^{o(n)}$, and whether CNF-SAT with unbounded width and $\mathrm{poly}(n)$ clauses admits
$2^{(1-\delta)n}$ time.

## Known

Conditional on Theorem C.1 and the Calabro–Impagliazzo–Paturi sparsification constant
$(k/\varepsilon)^{O(k)}$: $k(n)\le c\log\log n/\log\log\log n$ suffices (SR-09). The source
summary's $k\le\frac{1-\varepsilon}c\log\log n$ omits the $\log\log\log n$ (SR-08 context). Lower
bounds that depend only on unbounded-width CNF-SAT (Fréchet distance, diameter approximation,
treewidth-parameterized IS and DS) keep their justification.

## Open parts

1. Remove the $\log\log\log n$: a sparsification with $c(k,\varepsilon)=2^{O(k)}\varepsilon^{-O(1)}$ for
   counting would give $k(n)=\Theta(\log\log n)$. Is such sparsification possible? (Known
   sparsification lower bounds should be checked first.)
2. Can the tensor route take clauses of width $k$ with cost depending on $k$ only through the
   number of wires $km$, avoiding sparsification for moderately dense inputs?
3. Formulate the right hypothesis replacing SETH for width $\omega(\log\log n)$.

## Closest work

Impagliazzo, Paturi, Zane, JCSS 2001; Calabro, Impagliazzo, Paturi, CCC 2006 (level T);
preprint Lemma A.1 and Section 5.4 (level T, read in full; reading list R039).

## Smallest falsifier

A family of $k$-CNFs with $k=\omega(\log\log n)$ on which every leaf of every sparsification has
$2^{\Omega(k)}$ clauses per variable would block route 1.

## Resource boundary

One theory agent, one critic; one iteration.
