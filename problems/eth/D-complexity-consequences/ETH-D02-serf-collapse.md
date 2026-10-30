---
id: ETH-D02
source: sheet "Refuting ETH" consequence 2; sheet "10 consequences" item 2
category: complexity-consequences
status: audited, with a precise transfer rule
---

# ETH-D02: Which SERF-complete problems become subexponential

**Transfer rule (established in the preprint, Sec. 1.1.3 and after Cor. 1.1).** A `2^{o(n)}` algorithm for
`k`-SAT transfers to problem `P` only through a reduction from `P` *to* fixed-width SAT that keeps the number of
Boolean variables `O(size parameter)`. SERF-completeness (reductions *from* SAT) is the wrong direction.

| Problem (parameter) | Linear-variable reduction to `k`-SAT? | Status |
| --- | --- | --- |
| #Independent sets, `q`-colourings (fixed `q`), perfect matchings (`v`) | yes (Cor. 1.2) | **established** in preprint |
| Set Splitting, sets of size `<= k` (universe) | yes | **established** (preprint) |
| Max Independent Set / Vertex Cover / Dominating Set on `v` vertices | needs a cardinality constraint | Vertex Cover and MIS: via weighted counting, [ETH-C01](../C-counting-extensions/ETH-C01-weighted-q-series.md) (proof sketch). Dominating Set: open |
| Hamiltonian cycle on bounded-degree graphs (`v`) | successor encodings need `Theta(v log v)` variables | **open** |
| `k`-Set Cover with `n` elements and `m` sets (`m`) | yes when parameter is `m`, cardinality needed | open |

Sheet item "Hamiltonian Cycle ... immediately inherits" is **unverified**; no linear-variable encoding is
known to this program.
