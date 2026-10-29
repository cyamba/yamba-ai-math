# ETH-F03. Quantum versus classical: Grover and the new algorithm

| Field | Value |
| --- | --- |
| Category | Quantum |
| Source items | "Quantum vs classical speedup: shrinkage of Grover's quadratic advantage on structured NP search" |
| Status | **Asymptotic statement correct; crossover computed** (SR-06); quantum speedup of the new algorithm open |
| Depends on the upstream theorem | Yes |
| Score (I/B/T/L/Lean) | 2 / 2 / 3 / 1 / 1, composite **2.0** |
| Subresults | [SR-06](../subresults/SR-06-galactic-thresholds.md) |

## Statement

A deterministic $2^{o(n)}$ algorithm beats Grover's $O(2^{n/2})$ search (Grover, STOC 1996) for
large $n$, but in the preprint's cost model only beyond $n\approx2^{1.8\times10^6}$ (SR-06).

## Task

Is there a quantum algorithm for 3-SAT in time $2^{(1-\Omega(1))E(n)}$ where $E(n)$ is the
classical exponent? The algorithm is an exact sum over three enumerations (Taylor data,
measurement tuples, group assignments). Quantum amplitude estimation gives quadratic speedups
for approximate sums; exact sums of $N$ bounded terms need $\Omega(N)$ queries in the worst case
(parity), so a speedup must use structure, e.g. Grover search for a satisfying assignment within
one group given the measurements.

## Resource boundary

One agent; a short analysis note.
