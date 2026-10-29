# ETH-F01. Inverting local functions: Goldreich's PRG and sparse LPN

| Field | Value |
| --- | --- |
| Category | Cryptography |
| Source items | "Cryptographic immunity at fixed parameters vs asymptotic re-parameterization"; "Cryptographic parameter scaling" |
| Status | **Conditional consequences proved** (preprint Cor. D.2; SR-09 for sparse LPN); open beyond |
| Depends on the upstream theorem | Yes |
| Score (I/B/T/L/Lean) | 3 / 2 / 4 / 2 / 2, composite **2.7** |
| Subresults | [SR-09](../subresults/SR-09-coverage-map.md), [SR-06](../subresults/SR-06-galactic-thresholds.md) |

## Statements

* Preprint Cor. D.2: maps $\{0,1\}^n\to\{0,1\}^m$ with output locality $d$ (Goldreich's candidate
  one-way functions and PRGs, any stretch) are invertible, with exact preimage counts, in
  $2^{O_d(\rho(n))}\mathrm{poly}(m)$.
* SR-09: **sparse noisy linear equations** (rows of weight $k$, noise rate $\eta$, $m\le Cn$
  samples): solve the CNF on the $n+m$ variables $x,e$ with a linear-size counter for $|e|$ in
  $2^{O_{k,\eta,C}(n/\sqrt{\log n})}$, and count all consistent solutions. With more samples one may
  keep any $Cn$ of them; this recovers the secret exactly when those samples determine it (sparse
  rows leave a fraction about $e^{-kC}$ of variables uncovered, so exact recovery needs $C$ to
  grow slowly).
* Concrete parameters are untouched: the algorithm beats exhaustive search only for
  $n\gtrsim2^{160000}$ (SR-06).

## Not covered

Dense LPN, dense MQ and syndrome decoding with dense parity checks: their constraints are not
fixed-width with $O(n)$ clauses after encoding (SR-08 row 17).

## Open parts

1. Fine-grained crypto built on fixed-width SAT or on ETH (if any) loses its asymptotic basis; list
   such constructions.
2. Does the deformation method say anything new about *average-case* local PRGs at polynomial
   stretch beyond the generic $2^{o(n)}$ (e.g. distinguishing in less time than inverting)?

## Closest work

Applebaum, Computational Complexity 25 (2016) (survey, level T); Alekhnovich, FOCS 2003 (level T,
attribution of sparse LPN not verified).

## Resource boundary

One agent; documentation and one worked reduction in Lean if cheap.
