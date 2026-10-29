# SR-07. Exact Max-k-SAT histograms, weight enumerators and partition functions at bounded density

**Status: proved conditionally** on the preprint's Theorem C.1 (Boolean tensor contraction),
which is part of the unverified upstream claim. The algebraic identities are **Lean-verified**
in [`GradedCounting.lean`](../lean/EthConsequences/GradedCounting.lean) (`sum_pow_eq`,
`histogram_identity`, `coeff_histogram`, `deformation_identity`, `weight_identity`); the reduction
to Theorem C.1 is checked against its hypotheses below.
**Novelty: not verified.** The preprint states approximate Max-$k$-SAT (Corollary 1.2) and
counts independent sets, colourings and matchings (Corollary 1.3); it does not state the
graded counts below.

Feeds: [ETH-C02](../03-counting/ETH-C02-weighted-counting-q-series.md),
[ETH-C03](../03-counting/ETH-C03-max-sat-histogram.md),
[ETH-C04](../03-counting/ETH-C04-graph-polynomials-and-partition-functions.md).

## The tool

Theorem C.1 contracts a bipartite Boolean tensor network with $O(s)$ wires and degree at most
$s^{9/10}$, with entries in $\mathcal B_{P_0,\ell}=(\mathbb Z/2^{P_0})[V]/(V^\ell)$,
$P_0,\ell\le Cs$, in time $(s+\mathcal L)^{O(1)}2^{O(s/\sqrt{\log s})}$ and polynomial space. The
preprint uses it with $\ell=1$ for $\#k$-SAT. The formal variable $V$ is free for us to use as a
**grading**.

## Corollary A (exact clause histogram at bounded density)

Fix $k$ and $D$. Given a $k$-CNF $F$ with $n$ variables and $m\le Dn$ clauses, the numbers
$h_j=\#\{x:\ x\text{ violates exactly }j\text{ clauses}\}$, $0\le j\le m$, can be computed in
$2^{O_{k,D}(n/\sqrt{\log n})}$ time and polynomial space. In particular the exact Max-$k$-SAT
value $m-\min\{j:h_j>0\}$ and the number of optimal assignments.

*Proof.* Take the preprint's fixed-density network (Appendix C.2: one vertex per clause with its
satisfaction table, equality trees for repeated variables, every edge subdivided by an
equality tensor) and change only the clause tensors: entry $1$ if the clause is satisfied and
$V$ if it is violated. Use $P_0=n+1$ and $\ell=m+1\le s=n+m$. The contraction equals
$\sum_x\prod_e(\text{entry})=\sum_xV^{\mathrm{viol}(x)}=\sum_jh_jV^j$ (`histogram_identity`), and
$0\le h_j\le2^n<2^{n+1}$, so the coefficients modulo $2^{n+1}$ are exact (`coeff_histogram`).
Wires $O_{k}(n+m)=O_{k,D}(n)$, degree $\le\max(k,3)$, entries computable in constant time. $\square$

*Second proof (decision only).* For $m\le Dn$ the preprint's own Corollary 1.2 argument needs no
sampling: a linear-size threshold circuit plus the circuit-to-3-CNF reduction gives exact
Max-$k$-SAT by binary search, and parsimony of the encoding gives the counts $\sum_{j\le J}h_j$.

**Weighted Max-$k$-SAT** with integer weights $w_e\ge0$ and $\sum_ew_e=O(n)$ follows the same way
with entries $V^{w_e}$.

## Corollary B (weight enumerator, Max-Ones, exact-weight #SAT at bounded density)

For $m\le Dn$, the numbers $c_w=\#\{x\in\mathrm{SAT}(F):|x|=w\}$, $0\le w\le n$, in
$2^{O_{k,D}(n/\sqrt{\log n})}$: attach to each variable's equality tree one extra unary vertex
with tensor $(1,V)$, and use $\ell=n+1$ (`weight_identity`). This answers problem YMB-ETH-03 of
the source summaries **for bounded density**; the corrected exponent is
$n/\sqrt{\log n}$, not $n\log\log n/\log n$.

## Corollary C (graph polynomials and partition functions on sparse graphs)

On graphs with $v$ vertices and $O(v)$ edges, in $2^{O(v/\sqrt{\log v})}$:

* all coefficients $i_j(G)$ of the independence polynomial (Corollary B for the 2-CNF
  $\bigwedge_{uw\in E}(\bar x_u\vee\bar x_w)$, Lean bijection in
  [`IndependentSets.lean`](../lean/EthConsequences/IndependentSets.lean)), hence the hard-core
  partition function at every rational activity;
* the $q$-state Potts and Ising partition functions at fixed rational parameters and fixed $q$:
  clear denominators, use local integer tensors on $\lceil\log_2q\rceil$-bit spins, and take
  $P_0=O(v)$ bits;
* the number of proper $q$-colourings for fixed $q$ (already Corollary 1.3 of the preprint).

## What does not follow (open, see [SR-09](SR-09-coverage-map.md))

* **Dense instances.** Exact Max-2-SAT or Max-Cut with $m=\omega(n)$ clauses: the reductions to
  bounded density (sparsification, parity queries) preserve satisfying assignments, not the
  number of violated clauses. No $2^{o(n)}$ exact algorithm is known; the best is
  Williams's $O^*(2^{\omega n/3})$.
* **Weight enumerators at arbitrary density.** The preprint's arbitrary-density network sums
  the original variables inside the variable-group tensors and already uses $V$ for the parity
  lift. A second passive truncated variable in Theorem C.1 would suffice; this extension has not
  been checked.
* **Tutte polynomial at generic points** and the full chromatic polynomial: the random-cluster
  weight $q^{k(A)}$ and colourings with $q=\Theta(v)$ colours are not local with linearly many
  wires.
