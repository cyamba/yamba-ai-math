# ETH-A05. Approximate parity interpolation: Chebyshev, Krawtchouk and Padé alternatives

| Field | Value |
| --- | --- |
| Category | Algorithmic core |
| Source items | "Problem 6 (YAMBA-378-06): sharpening via Chebyshev/Padé spectral approximants" |
| Status | **Mostly negative** (analysis below); the 2-adic version is Appendix D |
| Depends on the upstream theorem | No |
| Score (I/B/T/L/Lean) | 2 / 2 / 4 / 2 / 2, composite **2.4** |
| Subresults | [SR-01](../subresults/SR-01-isoperimetric-rank-barrier.md), [SR-03](../subresults/SR-03-point-dependent-rank-barrier.md) |

## Task

The source suggests replacing the exact interpolation $f(j)=(-1)^j$ on $\mathcal I$ by an
approximation with small error $|\varepsilon_j|\le2^{-\Theta(v\log v)}$, relying on the final answer
being an integer.

## Analysis

* **Real approximation does not reduce measurements.** The measurement count is a rank
  ($c\ge\operatorname{rank}(I-M_0)$ for one matrix, $c_t\ge\operatorname{rank}N_t$ per node). An
  eigenvalue $1-\varepsilon_j\ne1$ is still a nonzero eigenvalue of $I-M_0$: every approximately
  fixed direction must be measured or its error carried. Carrying it perturbs $H(0)$ by up to
  $2^n\cdot\mathrm{poly}\cdot\max|\varepsilon_j|$, so the error must be below $2^{-n}$, which
  costs degree $\Omega(\sqrt{Qn})$ and destroys the Taylor savings.
* **The 2-adic version works**: Appendix D keeps exactness modulo $2^{p_t}$ and lets terms of
  high 2-adic valuation vanish. Approximation in the 2-adic metric is exactly what the tensor
  route does ([ETH-A04](ETH-A04-tensor-mode-counting-barrier.md)).

## Open question

Formalize the first bullet: a lower bound on any scheme that uses real approximate parity
polynomials with an integer-rounding finish (a "robust" version of SR-01).

## Closest work

Paturi's degree bounds for approximating symmetric functions (STOC 1992, level T); probabilistic
degree of parity (Srinivasan, Tripathi, Venkitesh 2019, level T).

## Smallest falsifier

A scheme with error $2^{-n}$ and replacement degree $o(\sqrt{Q\log(1/\varepsilon)})$ would contradict
the probabilistic-degree lower bound; none is expected.

## Resource boundary

One agent, one critic; a short note.
