# SR-06. Explicit constants: where the algorithm starts to beat 2^n, Grover and PPSZ

**Status: empirical** (exact evaluation of the preprint's own cost bound, by
[`galactic_thresholds.py`](../experiments/galactic_thresholds.py); results in
[`galactic_thresholds.json`](../experiments/results/galactic_thresholds.json)). The thresholds
are for the analysed bound, not for an implementation, and polynomial factors are ignored,
which only makes them smaller than the truth.
**Depends on the upstream theorem:** the cost model is the preprint's; the conclusions are
about that model whether or not the theorem holds.

Feeds: [ETH-A06](../01-algorithmic-core/ETH-A06-explicit-constants-and-crossover.md),
[ETH-F02](../06-crypto-and-quantum/ETH-F02-cryptographic-parameter-scaling.md),
[ETH-F03](../06-crypto-and-quantum/ETH-F03-quantum-versus-classical.md).

## Model

Bounded-occurrence 3-CNF on $n$ variables (the setting of the preprint's Section 2). With
$\lambda=\log_2n$, the time is, up to polynomial factors, the product of the three costs of the
preprint's display (2.11),
$$\underbrace{\sum_{j\le q}2^j\binom nj}_{q=\lfloor3nR/Q\rfloor}\ \cdot\
\underbrace{(2D+1)^{2\tau n}}_{D=r^{2Q}}\ \cdot\ \underbrace{2^{2n/r}}_{\text{group}},$$
so the exponent per variable is $e=T(\rho)+2\tau\log_2(2D+1)+2/r$ with $\rho=3R/Q$, where
$T(\rho)=\rho+H(\rho)$ for $\rho\le2/3$ and $T(\rho)=\log_23$ beyond. Constraints: the preprint's (2.17),
with the slightly stronger $12D^2\le n$ in place of $12D^2\le M$, and $2Qr^2\le n$; and the window
condition $c/D=\Pr[\mathrm{Bin}(Q,\frac{r-1}{2r})\notin\mathcal I]\le\tau/(3r)$ (Lemma 4.1 and Step 5),
with the binomial tail computed exactly. (A first version of the script used the slightly
conservative $\tau=3r^2\,\text{tail}/(r-1)$; the effect on the thresholds is negligible.)

## Results

| Parameters | Valid from | Beats $2^n$ ($e<1$) | Beats Grover $2^{n/2}$ | Beats PPSZ $1.30704^n$ |
| --- | --- | --- | --- | --- |
| Preprint's explicit choice (2.19) | $\lambda\ge1.11\times10^{10}$, where $e=1.52$ | $\lambda\approx6.3\times10^{10}$ | $\lambda\approx5.5\times10^{11}$ | $\lambda\approx1.1\times10^{12}$ |
| Best grid choice (same constraints) | | $\lambda\le1.78\times10^{5}$ ($r=20$, $Q=10286$, $R=617$) | $\lambda\le1.78\times10^{6}$ ($r=64$) | $\lambda\le3.98\times10^{6}$ ($r=48$) |
| A finer search | | $\lambda\le1.608\times10^{5}$ ($r=17$, $Q=9835$, $R=595$, $e\approx0.998$) | | |

The "best" rows are upper bounds on the thresholds: they come from parameter searches (the grid
of the script, and a finer search whose parameters the script re-checks as a spot check). So,
within the preprint's own cost model, **the best parameters we found beat exhaustive search from
about $n=2^{1.6\times10^5}$**, Grover's $2^{n/2}$ from about $n=2^{1.8\times10^6}$ and PPSZ (Hertli's
$O(1.30704^n)$) from about $n=2^{4\times10^6}$, and the paper's explicit parameters are not even
admissible below $n=2^{1.1\times10^{10}}$. The crude bound below shows that no choice beats
exhaustive search before $n\approx2^{3\times10^4}$. The Appendix D route is more extreme: at
recursion depth $0$ its parameter inequalities need $\lambda^{4/5}\le\lfloor\lambda/2^{17}\rfloor$, i.e.
$\log_2s\ge2^{85}$; the separate review estimates that deeper recursion levels (depth about
$(\log_2\lambda)/6$) need $\lambda\gtrsim2^{510}$, which we have not re-derived.

A crude lower bound confirms the order of magnitude. For $e<1$ the Taylor term forces
$\rho<0.228$, the window condition forces $R\gtrsim5\sqrt Q$ (the tail must be below
$1/(12rQ\log r)$), so $Q\gtrsim4\,300$, and $12D^2\le n$ then forces $\lambda\gtrsim4Q\log_2r\ge3\times10^4$.
The general $k$-CNF reduction (sparsification and copying, or the parity queries of Section 5)
only increases the effective number of variables.

## Why it matters

* **Concrete security is untouched.** Every instance that fits in the observable universe has
  far fewer than $2^{30000}$ variables (the crude lower bound on the threshold), so the analysed
  bound says nothing about AES, SHA-3, lattice
  or code-based schemes at real parameters; the consequence is asymptotic re-parameterization
  only ([ETH-F02](../06-crypto-and-quantum/ETH-F02-cryptographic-parameter-scaling.md)).
* **Grover.** A $2^{o(n)}$ classical algorithm beats $2^{n/2}$ asymptotically, but with the best
  parameters found only from about $n=2^{1.8\times10^6}$ ([ETH-F03](../06-crypto-and-quantum/ETH-F03-quantum-versus-classical.md)).
* **A target for constant hunting.** The gap between the paper's explicit choice and the best
  choice is a factor of about $4\times10^5$ in $\log_2n$; designs outside the preprint's template
  ([SR-04](SR-04-slab-construction.md)) and better tail bounds are the obvious levers
  ([ETH-A06](../01-algorithmic-core/ETH-A06-explicit-constants-and-crossover.md)).

For comparison, a secondary source (OfficeChai, 2026-10-27, not inspected beyond the article)
reports that an independent Anthropic paper, "A 2^o(n) Time Algorithm for 3-SAT", says its bound
beats brute force only beyond about $10^{10000}$ variables, i.e. about $2^{33000}$.
