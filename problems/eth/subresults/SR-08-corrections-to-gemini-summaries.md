# SR-08. Corrections ledger for the two source summaries

**Status: established** against the inspected preprint (inspection level T for the cited
sections; see [SOURCE.md](../SOURCE.md)) and, where marked, against Lean in
[`lean/`](../lean/) or exact computation.

The problem list in this folder was seeded by two AI-generated summaries supplied with the
request ("Refuting the Exponential Time Hypothesis" and "Make a list of the 10 most influential
and impactful consequences ...", both Gemini, 2026-10-27/28). They are useful as a map of
consequences, but several statements are wrong or overstated. Each row gives the claim, the
verdict and the corrected statement. Problem files cite this ledger instead of repeating the
errors.

## Running time and mechanism

| # | Claim in the summaries | Verdict | Correct statement |
| --- | --- | --- | --- |
| 1 | Time $2^{O(n/\log n)}$, or $2^{O_k(n\log\log n/\log n)}$ | **Wrong** | Preprint Thm 1.1: $(n+m)^{O_k(1)}2^{O_k(n\log\log n/\sqrt{\log n})}$; $2^{O_{k,D}(n/\sqrt{\log n})}$ when $m\le Dn$; Lean scope: $n(\log\log n)^2/\sqrt{\log n}$ ([378.md](https://github.com/openai/math/blob/main/lean/docs/378.md)). Every downstream bound with $n/\log n$ must be redone with $n/\sqrt{\log n}$. |
| 2 | Pipeline: "partition clauses into $O(n/\log n)$ clusters of size $\Theta(\log n)$, replace cluster indicators by low-rank spectral polynomials, evaluate at poly($n$) points" | **Wrong mechanism** | Groups $r\asymp\sqrt{\log n}/(\log\log n)^2$, nodes $Q\asymp\log n/\log\log n$, replacement degree $R\asymp\sqrt{\log n}$, Taylor jets at each node from fixed Boolean substitutions, measurement separation, Hermite interpolation ([SOURCE.md](../SOURCE.md)); or recursive tensor contraction (Appendix D). |
| 3 | $Z_F(t)=\sum_x\prod_r(1+t(\Psi_r(x)-1))$ "decomposes over an induced separator of size $O(n/\log n)$" (YMB-ETH-01) | **Wrong** | This polynomial is the clause-violation generating function ([`deformation_identity`](../lean/EthConsequences/GradedCounting.lean)); at $t=1$ it is $\#F$ trivially and it separates nothing. |
| 4 | Extra $\log\log n$ in Lean comes from IPZ branching and is removed by "buffered clause-width compression" (YMB-ETH-02) | **Unsupported** | Preprint: the rational-interpolation route gives $(\log\log n)^2$, the tensor-contraction route (Appendix D) gives $\log\log n$ in general and none at bounded density. |
| 5 | "Crossover constant $C_3$ with $2^{C_3n/\log_2n}$" vs PPSZ (YMB-ETH-04) | **Wrong form** | The exponent has the form $n\,(\log\log n)^a/\sqrt{\log n}$. Explicit thresholds: [SR-06](SR-06-galactic-thresholds.md) (beats $2^n$ only for $n\gtrsim2^{160000}$). |

## Lemma-level identities

| # | Claim | Verdict | Correct statement |
| --- | --- | --- | --- |
| 6 | Recurrence $S(k,b)+S(k-1,b)=1+(-2)^b\binom{k-1}b$ for $S(k,b)=\sum_{j\le b}(-2)^j\binom kj$ (YAMBA-378-01) | **False** ($b=1$, $k=2$: left side $S(2,1)+S(1,1)=-3-1=-4$, right side $1-2=-1$) | $S(k+1,b)=-S(k,b)+2(-2)^b\binom kb$ (Lean `S_succ`). |
| 7 | Defect $f_{a,b}(a+k)-(-1)^{a+k}=(-1)^a(-2)^{b+1}\binom{k-1}b$ for all $k$ | **False** ($b=1,k=3$: actual $-4$, claimed $8$) | $(-1)^kS(k,b)-1=(-1)^{b+1}2^{b+1}\sum_{m<k}(-1)^m\binom mb$ and $\lvert\cdot\rvert\le2^{b+1}\binom{k-1}b$ (Lean `defect_eq`, `abs_defect_le`). |
| 8 | Hermite weights: "$\mathrm{lcm}(1,\dots,Q)^{2J}$ clears all denominators" (YAMBA-378-04) | **Correct but weak** | $\mathrm{lcm}(1,\dots,Q)^{J-1-r}w_{t,r}\in\mathbb Z$ (proof from the residue formula, checked exactly for $Q\le7$, $J\le5$); see [ETH-B04](../02-algebraic-identities/ETH-B04-hermite-weights-and-bit-lengths.md). |
| 9 | Minc's permanent identity is part of the proof (YAMBA-378-05) | **Not in the preprint** | The preprint's Taylor data come from Boolean differences (Lemma 3.3, Lean `boolean_differences`); permanents enter only through Curticapean's perfect-matching reduction. The identity is classical and the problem is kept as a side exercise. |
| 10 | $\{0,\pm1\}$ eigenbasis with squared norms $2^{w}$ and $\binom Qj d_-^jd_+^{Q-j}$ vectors with $j$ antisymmetric factors (YAMBA-378-03) | **Correct** | Matches preprint Section 2.7, Step 2. |

## Consequences

| # | Claim | Verdict | Correct statement |
| --- | --- | --- | --- |
| 11 | ETH, #ETH, SETH, Gap-ETH, NSETH refuted for fixed width; $s_k=0$ for all $k$ | **Correct, conditional** | As stated in preprint Section 1.1.1, if Theorem 1.1 holds. |
| 12 | Planar/geometric bounds move from $2^{\Omega(\sqrt n)}$ to $2^{O(\sqrt n/\log n)}$ | **Wrong** | Only the ETH-based *justification* of $2^{\Omega(\sqrt n)}$ disappears. No $2^{o(\sqrt n)}$ planar algorithm follows; the new algorithm on planar inputs costs $2^{O(n/\sqrt{\log n})}$, worse than the known $2^{O(\sqrt n)}$ ([ETH-D05](../04-fine-grained/ETH-D05-planar-and-geometric-problems.md)). |
| 13 | Every SERF-complete problem, including **Hamiltonian Cycle** on sparse graphs, becomes $2^{o(n)}$ | **Overstated** | IPZ prove Hamiltonian Circuit only SERF-*hard*; no $O(n)$-variable SAT encoding of Hamiltonicity is known (connectivity is global). Independent Set, Vertex Cover, $q$-Colourability ($q$ fixed), Set Splitting do follow ([SR-09](SR-09-coverage-map.md)). |
| 14 | FPT: any problem with an $O(p)$-variable reduction gets $2^{O(p\log\log p/\log p)}n^{O(1)}$; tight $2^{\Omega(k)}$ bounds "destroyed" | **Exponent wrong, scope overstated** | $2^{O(p\log\log p/\sqrt{\log p})}$, and only for problems with linear-variable SAT encodings of a kernel, e.g. Vertex Cover ([SR-09](SR-09-coverage-map.md)). Other ETH-based lower bounds lose their justification without gaining algorithms. |
| 15 | Tutte polynomial, chromatic polynomial, Ising/Potts on sparse graphs all subexponential | **Partly wrong** | Potts/Ising at fixed rational parameters and fixed $q$, independence polynomial: yes on sparse graphs ([SR-07](SR-07-graded-counting-bounded-density.md)). Full chromatic polynomial and Tutte polynomial at generic points: open. |
| 16 | "Spectral replacement" yields lower bounds against $\mathrm{NC}^1$ and $\mathrm{TC}^0$ | **Unsupported** | The preprint proves $\mathrm E^{\mathrm{NP}}\not\subseteq\mathrm{SIZE}(O(n))$ and $C_L(n)>c\,n\sqrt{\log n}$ (Cor. 1.4) via Williams's method; nothing about $\mathrm{NC}^1$ or $\mathrm{TC}^0$ follows. |
| 17 | MQ and syndrome-decoding parameters must be rescaled to $n=\Theta(\lambda\log\lambda)$ | **Wrong for dense schemes** | Dense quadratic systems and dense parity checks are not fixed-width CNFs with $O(n)$ clauses; the theorem does not apply to them. Sparse local primitives (Goldreich's PRG, sparse LPN with linearly many samples) are affected asymptotically ([ETH-F01](../06-crypto-and-quantum/ETH-F01-inverting-local-functions.md)), and nothing changes at concrete sizes ([SR-06](SR-06-galactic-thresholds.md)). |
| 18 | Classical algorithm beats Grover's $2^{n/2}$ "for every $\alpha>0$" | **Asymptotically correct, galactically late** | True for $2^{o(n)}$, but the crossover is near $n=2^{1.8\times10^6}$ ([SR-06](SR-06-galactic-thresholds.md)). |
| 19 | "Polynomial-space compression of exact exponential algorithms" | **Misleading** | Polynomial space was always available for $2^n$ search; what is new is subexponential time **with** polynomial space. |
| 20 | Technical notes by Ryan O'Donnell and Shiva Kintali exist | **Correct** | Kintali (2026-10-26) and O'Donnell (2026-10-28) expositions found by the literature check; inspection level T. |

