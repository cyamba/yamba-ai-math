---
id: ETH-D12
source: sheet "Refuting ETH" consequence 8; preprint text after Cor. 1.1
category: complexity-consequences
status: audited
---

# ETH-D12: Why NP is not known to be in SUBEXP

* **Correct.** Subexponential bounds `2^{o(n)}` do not transfer under polynomial-time reductions; that would
  need `2^{n^{o(1)}}`. A reduction producing `N = n^alpha` variables yields `2^{O(n^alpha / sqrt(log n))}`.
* **Corrected arithmetic.** For `N = n log n`: `2^{O(N / sqrt(log N))} = 2^{O(n sqrt(log n))}`, worse than
  brute force (the sheet's version used `/log N`).

## Question

Characterise the problems with reductions to 3-SAT of size `N = n (log n)^{beta}`: they get `2^{o(n)}` iff
`beta < 1/2` (up to `log log` factors). Which classical NP-complete problems have such reductions
(Hamiltonicity with `Theta(n log n)` encodings is just outside)? A sharper SAT algorithm
([ETH-B03](../B-exponent-frontier/ETH-B03-polynomial-row-routing.md)) would move the threshold to `beta < 1`.
