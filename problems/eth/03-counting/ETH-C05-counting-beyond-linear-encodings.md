# ETH-C05. Beyond linear encodings: chromatic number, Hamiltonicity, dense permanents

| Field | Value |
| --- | --- |
| Category | Counting / frontier |
| Source items | "SERF hierarchy collapse" (overstated for Hamiltonian cycle); "Hamiltonian Cycle on sparse graphs" |
| Status | **Open** |
| Depends on the upstream theorem | Yes for motivation; the problems stand alone |
| Score (I/B/T/L/Lean) | 5 / 4 / 1 / 3 / 2, composite **3.4** |
| Subresults | [SR-09](../subresults/SR-09-coverage-map.md#not-covered-no-on-variable-encoding-is-known-open) |

## Task

For each problem below, either give a $2^{o(n)}$ algorithm (if Theorem 1.1 holds) or explain why
the algebraic method needs more than an encoding into fixed-width SAT:

1. **Hamiltonian cycle** on $n$-vertex graphs of maximum degree 3 (ETH-hard via a linear
   reduction; only SERF-hard per IPZ);
2. **chromatic number** (best known $2^n\mathrm{poly}(n)$, Björklund–Husfeldt–Koivisto);
3. **permanent of a dense $n\times n$ 0/1 matrix** (Ryser's $O(2^nn)$ and its sub-$2^n$
   refinements, which save only a $2^{o(n)}$ factor; exact best bound to be inspected);
4. **TSP** and **Subset Sum** with $n$ items.

## Two routes

* **Encodings.** A Hamiltonicity certificate checkable by a circuit with $O(n)$ gates would put
  Hamiltonian cycle on bounded-degree graphs into SERF. Known encodings need $n\log n$ position
  bits; a negative result here (a lower bound on nondeterministic circuit size for single-cycle
  verification) would be informative.
* **Direct algebra.** Ryser's formula writes the permanent as $\sum_x\prod_{i=1}^n L_i(x)$ with
  linear forms $L_i$: a product of total degree $n$, so the Taylor cost is fine, but every
  $L_i$ reads all variables. One deformed form per *factor* (not per occurrence) needs
  measurements spanning the row space of $A$ off each group: about $n(1-1/r)$ measurements,
  far too many. A low-rank-plus-local structure for generic matrices would be required; a
  rigidity-type barrier is plausible.

## Closest work

IPZ 2001 (Hamiltonian circuit SERF-hard, level T); Björklund, Husfeldt, Koivisto, SICOMP 39
(2009) (level T); Björklund's permanent algorithms (level T, to inspect).

## Smallest falsifier

For the direct-algebra route on permanents: show that any design for $\sum_x\prod_iL_i(x)$ with
dense generic $L_i$ needs $\Omega(n)$ measurements at some node (a matrix-rigidity statement).

## Resource boundary

Two agents (encodings and nondeterministic circuit lower bounds; algebraic rigidity), one
critic; one iteration to produce precise statements.
