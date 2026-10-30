---
id: ETH-D05
source: sheet "Refuting ETH" consequence 5; sheet "10 consequences" item 3
category: complexity-consequences
status: audited, open items
---

# ETH-D05: Parameterized complexity after ETH

* **Correct.** ETH-based lower bounds of the form `2^{o(k)} poly(n)` impossible (Vertex Cover, Feedback Vertex
  Set, ...) and `f(k) n^{o(k)}` impossible (Clique, via Chen et al. 2006) lose their justification.
* **Corrected exponent.** Problems with a polynomial kernel of `O(k)` Boolean variables and a parsimonious
  fixed-width CNF encoding run in `poly(n) 2^{O(k log log k / sqrt(log k))}`.
* **New algorithms (sketch).** k-Vertex Cover in `poly(n) + 2^{o(k)}`, via kernel plus weight enumerator
  ([ETH-C01](../C-counting-extensions/ETH-C01-weighted-q-series.md)).

## Open

1. **Clique.** The `n^{o(k)}` lower bound used a reduction from 3-SAT with `N = O(k log n)`-ish variables
   per group (Chen et al.); with `sqrt(log)` savings, does `k`-Clique get an `n^{o(k)}` algorithm? Not
   from Theorem 1 directly: encoding `k`-Clique needs `k log n` variables, giving `2^{O(k log n / sqrt(log(k log n)))}`
   `= n^{O(k / sqrt(log(k log n)))}`, which **is** `n^{o(k)}` when `k log n -> infinity`. Check the encoding
   (one-hot per group needs `kn` variables; binary per group needs `k log n` variables and `O(k^2 n^2)`
   clauses of width `O(log n)`, which is unbounded width). So: open, hinges on [ETH-B05](../B-exponent-frontier/ETH-B05-width-threshold.md).
2. Planar and bounded-genus parameterized problems with `2^{O(sqrt k)}` algorithms: no transfer
   (see [ETH-D07](ETH-D07-planar-lower-bounds.md)).
