# ETH-A06. Explicit constants and the crossover with exhaustive search and PPSZ

| Field | Value |
| --- | --- |
| Category | Algorithmic core |
| Source items | "YMB-ETH-04" (explicit crossover constant $C_3$ vs PPSZ) |
| Status | **Partially solved** (SR-06); improvements open |
| Depends on the upstream theorem | No (evaluates the preprint's cost model) |
| Score (I/B/T/L/Lean) | 3 / 2 / 5 / 3 / 2, composite **3.0** |
| Subresults | [SR-06](../subresults/SR-06-galactic-thresholds.md) |

## Task

Determine, for the preprint's algorithms with the best admissible parameters, the least $n$ at
which the running-time bound beats $2^n$, Grover's $2^{n/2}$ and Hertli's PPSZ bound
$O(1.30704^n)$; then lower these thresholds by better designs or bookkeeping.

## Known (SR-06)

Bounded-occurrence 3-CNF, the preprint's three costs, exact binomial tails:

| Parameters | Beats $2^n$ | Beats $2^{n/2}$ | Beats $1.30704^n$ |
| --- | --- | --- | --- |
| Preprint (2.12) | $\log_2n\approx6.3\times10^{10}$ | $5.5\times10^{11}$ | $1.1\times10^{12}$ |
| Best found | $1.6\times10^5$ | $\lesssim1.8\times10^6$ | $\lesssim4.0\times10^6$ |

Appendix C as written needs $\log_2s\ge2^{85}$. The source summary's form $2^{C_3n/\log_2n}$ is
wrong ([SR-08](../subresults/SR-08-corrections-to-gemini-summaries.md), row 5).

## Open parts

1. Optimize Appendix C's constants ($\varepsilon=2^{-17}$, $r=64$, $\Delta=s^{9/10}$) and report its
   threshold.
2. Use the slab or MILP-optimal point-dependent designs ([ETH-A03](ETH-A03-point-dependent-designs.md))
   inside the cost model: they shrink the measurement term for moderate $Q$.
3. Account for the general $k$-CNF reduction (sparsification, parity queries) to state thresholds
   for arbitrary 3-CNFs.
4. Compare with the independent Anthropic paper's reported crossover near $10^{10000}$ variables
   (secondary source, not inspected).

## Smallest falsifier

A parameter choice satisfying all constraints with exponent below 1 at $\log_2n<3\times10^4$
would contradict SR-06's crude lower bound for this cost model.

## Resource boundary

One agent with the existing script; a few CPU-hours.
