---
id: ETH-D08
source: sheet "10 consequences" item 8; preprint Cor. 1.3 and Appendix F.1
category: complexity-consequences
status: audited
---

# ETH-D08: Circuit lower bounds for `E^NP`

* **Established in the preprint.** `E^NP not subset SIZE(O(n))` (via Williams 2013, Thm. 6.1) and the
  quantitative `C_L(n) > c n sqrt(log n)` infinitely often for some `L in E^NP` (Cor. 1.3).
* **Sheet claim refuted as stated.** Nothing about `NC^1`, `TC^0` or `AC^0` follows from the preprint.

## Questions

1. Williams's algorithmic method: a `2^n / n^{omega(1)}` #SAT algorithm for a circuit class `C` gives
   `NEXP not subset C`. Theorem 1 handles CNFs of bounded width only. Does the spectral replacement extend to
   depth-2 circuits of unbounded fan-in with `poly(n)` gates (e.g. ACC^0 layers, threshold of parities)?
2. Can the `n sqrt(log n)` circuit bound be improved to `n (log n)^{1/2 + delta}` by a sharper ETH-type
   algorithm (link to [ETH-B03](../B-exponent-frontier/ETH-B03-polynomial-row-routing.md): an
   `n (log log n)^3 / log n` exponent would give roughly `n log n / (log log n)^3`; heuristic, by analogy with the
   way Cor. 1.3 converts `n / sqrt(log n)` into `n sqrt(log n)`)?
