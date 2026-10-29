# ETH-C04. Graph polynomials and partition functions

| Field | Value |
| --- | --- |
| Category | Counting / statistical physics |
| Source items | "Subexponential evaluation of #P-hard graph polynomials (Tutte, Ising, Potts)"; "Statistical physics and partition functions"; "YMB-ETH-05" (chromatic polynomial) |
| Status | **Partly solved conditionally** (SR-07, Cor. C); Tutte at generic points and full chromatic polynomial **open** |
| Depends on the upstream theorem | Yes |
| Score (I/B/T/L/Lean) | 3 / 3 / 3 / 2 / 3, composite **2.9** |
| Subresults | [SR-07](../subresults/SR-07-graded-counting-bounded-density.md), [SR-09](../subresults/SR-09-coverage-map.md) |

## Covered (graphs with $v$ vertices and $O(v)$ edges, time $2^{O(v/\sqrt{\log v})}$)

* all coefficients of the independence polynomial and the hard-core partition function at
  rational activities;
* $q$-state Potts and Ising partition functions at fixed rational parameters and fixed $q$;
* $P(G,q)$ for each fixed integer $q$ (preprint Cor. 1.3).

## Open

1. **Tutte polynomial at a generic rational point** $(x,y)$ with $(x-1)(y-1)$ not a positive
   integer: the random-cluster weight $q^{k(A)}$ needs the number of components, a global
   quantity. DHMTW's #ETH-based lower bounds ($\exp(o(n))$ for multigraphs,
   $\exp(o(n/\mathrm{polylog}\,n))$ for simple graphs) no longer have a basis, but no $2^{o(m)}$
   algorithm follows.
2. **The full chromatic polynomial** (all coefficients) and the chromatic number: colours up to
   $v$ need $v\log v$ bits ([ETH-C05](ETH-C05-counting-beyond-linear-encodings.md)).
3. **Physics claim to drop**: the source's "penetrating the phase-transition threshold" conflates
   exact exponential-time computation with the approximability transition at the uniqueness
   threshold; nothing about approximation follows.

## Closest work

DHMTW, ACM TALG 10(4) (2014) (level T); Björklund, Husfeldt, Kaski, Koivisto on the Tutte
polynomial in vertex-exponential time (level T, to inspect).

## Smallest falsifier

A linear-wire tensor encoding of $q^{k(A)}$ for non-integer $q$ would solve item 1.

## Resource boundary

One agent for the Tutte question (encodings of connectivity), one critic.
