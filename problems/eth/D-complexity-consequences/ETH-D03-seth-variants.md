---
id: ETH-D03
source: sheet "Refuting ETH" consequence 3; sheet "10 consequences" item 5
category: complexity-consequences
status: audited
---

# ETH-D03: SETH, NSETH, Gap-ETH and unbounded-width SETH

* **Correct.** SETH, NSETH, Gap-ETH and their randomized forms are refuted for fixed width (preprint
  Sec. 1.1.1), because testing `#F > 0` decides SAT and UNSAT in `2^{o(n)}` for every fixed `k`.
* **Survives.** The hypothesis "CNF-SAT with unbounded width has no `2^{(1-delta) n} poly(n,m)` algorithm"
  (used for Frechet distance, diameter approximation, treewidth-parameterized Independent Set and Dominating
  Set) is untouched: Theorem 1's constants depend on `k` ([ETH-B05](../B-exponent-frontier/ETH-B05-width-threshold.md)).
* **Sheet nuance confirmed.** Problems reducing from CNF-SAT with `k = omega(1)` keep their lower bounds only
  under this unbounded-width hypothesis (the sheet calls it UW-SETH).

## Open

1. Is there a `2^{(1-delta)n} poly(m)` algorithm for CNF-SAT of width `k = O(log n)` or `O(log m)`? Theorem 1
   says nothing; this is now the cleanest "SETH" question.
2. Does NSETH's role (barriers for deterministic fine-grained reductions, Carmosino et al. 2016) carry over to a
   width-unbounded NSETH?
