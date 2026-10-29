# SR-09. Coverage map: which ETH-hard problems become subexponential

**Status: proved conditionally** on the preprint's Theorem 1.1 (and Theorem D.1 where marked
D.1). Each positive entry gives a reduction to fixed-width SAT with $O(n)$ variables; the
negative entries record that **no such reduction is known** (open), not that none exists.
Bibliographic facts were checked by our citation pass of 2026-10-29 at statement level
(inspection level T or A, as recorded in the
[reading list](../../../references/reading-list.md#exponential-time-hypothesis-consequences));
none is a proof audit.
**Novelty:** most positive entries are routine once Theorem 1.1 is granted; the value is the
map, the corrected exponents and the explicit open boundary.

Feeds: [ETH-D01](../04-fine-grained/ETH-D01-ipz-constants-and-serf.md),
[ETH-D02](../04-fine-grained/ETH-D02-seth-nseth-gapeth-survivors.md),
[ETH-D03](../04-fine-grained/ETH-D03-subexponential-fpt.md),
[ETH-C05](../03-counting/ETH-C05-counting-beyond-linear-encodings.md),
[ETH-A08](../01-algorithmic-core/ETH-A08-width-dependence-and-uw-seth.md),
[ETH-F01](../06-crypto-and-quantum/ETH-F01-inverting-local-functions.md).

**Principle.** $2^{o(N)}$ algorithms transfer only through reductions whose output has
$O(N)$ variables (Impagliazzo, Paturi, Zane, JCSS 63 (2001), SERF reductions). Write
$\rho(N)=N\log\log N/\sqrt{\log N}$; Theorem 1.1 gives $2^{O_k(\rho(N))}$ for $k$-CNF on $N$
variables (any number of clauses) and $2^{O_{k,D}(N/\sqrt{\log N})}$ at density $\le D$.

## Covered

| Problem (input size) | Encoding with $O(n)$ variables | Time |
| --- | --- | --- |
| $k$-SAT, #$k$-SAT, $k$ fixed | itself | $2^{O_k(\rho(n))}$ |
| Maximum independent set, maximum clique, minimum vertex cover, any graph ($v$ vertices) | 2-CNF $\bigwedge_{uw}(\bar x_u\vee\bar x_w)$ (complement graph for clique) plus a linear-size counting circuit (adder tree, $O(v)$ gates) and Tseitin encoding | $2^{O(\rho(v))}$ |
| #IS, proper $q$-colourings ($q$ fixed), perfect matchings (sparse) | preprint Cor. 1.3 | $2^{o(v)}$, $2^{o(v+e)}$ |
| Independence polynomial, Potts/Ising at fixed rational parameters, graphs with $O(v)$ edges | graded contraction, [SR-07](SR-07-graded-counting-bounded-density.md) (D.1) | $2^{O(v/\sqrt{\log v})}$ |
| Exact Max-$k$-SAT and its histogram, $m\le Dn$ | [SR-07](SR-07-graded-counting-bounded-density.md) | $2^{O_{k,D}(n/\sqrt{\log n})}$ |
| Dominating set, max degree $\Delta$ fixed | width-$(\Delta+1)$ clause per vertex plus counter | $2^{O_\Delta(\rho(v))}$ |
| Set Splitting, sets of size $\le k$ | preprint §1.1.3 (Cygan, Dell, Lokshtanov, Marx, Nederlof, Okamoto, Paturi, Saurabh, Wahlström, observation 3.6) | $2^{O_k(\rho(n))}$ |
| Circuit-SAT, fan-in 2, $s=O(n)$ gates | Tseitin | $2^{O(\rho(n))}$; gives $\mathrm E^{\mathrm{NP}}\not\subseteq\mathrm{SIZE}(O(n))$ (preprint Cor. C.1) |
| Inverting maps with output locality $d$ (Goldreich's PRG, any stretch) | preprint Cor. C.2 | $2^{O_d(\rho(n))}\mathrm{poly}(m)$ |
| **Sparse noisy linear equations / sparse LPN with $m=O(n)$ samples**: find $x\in\mathbb F_2^n$, $e$ with $\lvert e\rvert\le\eta m$, $Ax+e=b$, rows of $A$ of weight $k$ | variables $x,e$ ($n+m$); each row is a $(k+1)$-XOR, $2^k$ clauses; counter for $\lvert e\rvert$ | $2^{O_{k,\eta,m/n}(n/\sqrt{\log n})}$ |
| **Vertex Cover parameterized by $k$** | kernel with $\le2k$ vertices (Chen, Kanj, Jia, J. Algorithms 41 (2001), via Nemhauser–Trotter), then the IS row | $2^{O(\rho(k))}+\mathrm{poly}(n)$ |

## The clause-width frontier

Combine counting sparsification with the tensor route. Sparsification writes a $k$-CNF as at
most $2^{\varepsilon n}$ disjoint $k$-CNFs with at most $c(k,\varepsilon)n$ clauses each, with
$c(k,\varepsilon)=(k/\varepsilon)^{O(k)}$ (Calabro, Impagliazzo, Paturi, CCC 2006; the counting version
is Dell, Husfeldt, Marx, Taslaman, Wahlén, Appendix A). Each leaf is a network with
$s\le k\,c(k,\varepsilon)n+O(n)$ wires, so the exponent is
$$\varepsilon n+O\!\left(\frac{k\,(k/\varepsilon)^{O(k)}\,n}{\sqrt{\log n}}\right).$$
Choosing $\varepsilon=1/\log\log n$ gives $o(n)$ whenever
$$k(n)\ \le\ c\,\frac{\log\log n}{\log\log\log n}$$
for a small absolute $c$. So $k(n)$-SAT is subexponential up to width
$\Theta(\log\log n/\log\log\log n)$ (conditional on D.1 with absolute constants for $s$ wires,
which is how Theorem D.1 is stated). The source summary's threshold
$k\le\frac{1-\varepsilon}c\log_2\log_2n$ (YMB-ETH-06) omits the $\log\log\log n$ coming from
the $(k/\varepsilon)^{O(k)}$ sparsification constant. Unbounded-width CNF-SAT with
$\mathrm{poly}(n)$ clauses is untouched, so the lower bounds that follow from "CNF-SAT has no
$2^{(1-\delta)n}$ algorithm" (Fréchet distance, diameter approximation, treewidth-parameterized
IS and DS; preprint §1.1.3) keep their justification.

## Not covered: no $O(n)$-variable encoding is known (open)

| Problem | Obstruction |
| --- | --- |
| Hamiltonian cycle/path, even max degree 3 | Only SERF-*hard* (IPZ). The edge-set witness has $O(n)$ bits but "single cycle" is a global connectivity condition; known encodings use $\Theta(n\log n)$ variables. |
| Chromatic number ($q$ unbounded), full chromatic polynomial | $n\lceil\log_2q\rceil$ variables, $\Theta(n\log n)$ for $q=\Theta(n)$; best known $2^n\mathrm{poly}(n)$ (Björklund, Husfeldt, Koivisto, SICOMP 2009). |
| Exact Max-2-SAT / Max-Cut, $m=\omega(n)$ | Violation counts are not preserved by sparsification; best known $O^*(2^{\omega n/3})$ (Williams 2005). |
| Permanent of a dense $n\times n$ 0/1 matrix, perfect matchings in dense graphs | Witness is a permutation ($n\log n$ bits); the counting target needs #SAT of a superlinear encoding. |
| TSP, Subset Sum, Knapsack ($n$ numbers of $b$ bits) | Arithmetic on $\Theta(nb)$ bits. |
| Tutte polynomial at generic $(x,y)$ | Random-cluster weight $q^{k(A)}$ counts components (global). |
| Planar problems below $2^{o(\sqrt n)}$ | Planar inputs give nothing better than $2^{O(n/\sqrt{\log n})}$. |
| $k$-Clique in $n^{o(k)}$, other W[1]-hardness | Reductions run from SAT to these problems, not back. |

Each row of the second table is a candidate fleet problem in
[ETH-C05](../03-counting/ETH-C05-counting-beyond-linear-encodings.md) or
[ETH-D07](../04-fine-grained/ETH-D07-reduction-blowup-boundary.md): either a linear encoding
(which would make the problem subexponential) or a barrier showing why the algebraic method
needs more than encodings.
