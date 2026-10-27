# Positive models for the KR1 auxiliary states

**Christopher Yamba with GPT-6.1 Terra mathematical research roles, Yamba AI Math. Research companion, 27 October 2026.**

**Status:** A universal indexed positive cut-word model for the auxiliary KR1 series is supported by a written proof and separate critique. The main direct residue-to-gap KR1 bijection remains unresolved. Lean verifies particular supporting lemmas, not the complete theorem. Novelty is unverified and AI critique is not external peer review.

## Full objective
Find weight-preserving mutually inverse algorithms between partitions into parts in classes 1, 3, 6, 8 modulo nine, and partitions satisfying the KR1 gap rules. Prove universal validity, inverses, weight and termination. The earlier octant construction fails at weight 41 where two distinct source clusters map to `(19,12,6,3,1)` ([corrected PR 15](https://github.com/cyamba/yamba-ai-math/pull/15)); the [PR 16](https://github.com/cyamba/yamba-ai-math/pull/16) restricted sector does not bridge it.

## General theorem
For `d,c>0`, distinct paired nodes `z_i=q^{r_i}+q^{c-r_i}` with `0<r_i<c`, and `D=Phi_{d,c}[z_0,...,z_n]`, define `Phi_{d,c}(z)=product_{j>=0}(1-z q^{dj}+q^{c+2dj})^(-1)`. For every `0<=m<=n`, let `W_n` consist of words over colored particles `alpha,beta` with exactly `n` cuts. Cuts define layers and interrupt adjacent `beta alpha` descents. Writing `b(w)` for intrinsic weight, `comaj(w)` for the forced suffix-descent charge, and `L(w)` for length, the proved expansion is

```tex
(q^d;q^d)_m D =
\sum_{w\in\mathcal W_n}
\frac{q^{b(w)+d\operatorname{comaj}(w)}}
{\prod_{h=m+1}^{L(w)}(1-q^{dh})}.
```

The right side is coefficientwise positive and gives models for all indices of the auxiliary `C_n,A_n,B_n` after specialization and boundary normalization.

### Constructive cancellation
Flatten cuts and particles into one word. Set `delta_1=j_1` and `delta_t=j_t-j_{t-1}-epsilon_{t-1}>=0`. The identity

```tex
d\sum_{t=1}^L j_t=d\operatorname{comaj}(w)+
d\sum_{t=1}^L(L-t+1)\delta_t
```

pairs a negative marker of weight `dh` with exactly one unit of coordinate `delta_(L-h+1)`. Toggle the least eligible marker or coordinate to get a weight-preserving sign-reversing involution. Surviving words have no negative markers and their last `m` gap coordinates locked at zero. Cut-by-cut positivity cannot replace this argument: a zero-cut summand has coefficient minus one at `q^9` for `n>=3`.

## Retained additional results
- Under bounded multiplicities on a residue subfamily, an injection with `max target <= gamma max source + K` for fixed K satisfies `gamma >= log(256)/log(159) = 1.093959803...`. This is not asserted for unrestricted encoding hypotheses.
- Explicit reversible local surgery realizes `1/((1-x)(1-y)(1-x²y)) = 1/((1-y)(1-x²)(1-xy)) + x/((1-x²)(1-xy)(1-x²y))`.
- Pure global color-swap with cyclic routing fails at weight 37. A branch-specific color repair works only for that witness.
- At auxiliary `C_0` and weight eight, preserving colored-particle count is impossible. A global recurrence operator must sometimes create or remove a particle.
- The prior octant map's weight-41 collision is preserved as a regression.

## The still missing bijection
Construct an explicit, reversible weighted decomposition

```tex
\mathscr C_n\longleftrightarrow
\mathscr A_{n+1}\sqcup
(\{3n+3\}\times\mathscr C_{n+1})
\sqcup(\{6n+6\}\times\mathscr C_{n+1})
\sqcup(\{6n+8\}\times\mathscr A_{n+2}).
```

Every output must reveal its branch. Combine it with the other auxiliary recurrences, literal partition endpoints and termination to complete the full KR1 map. Such maps were not found.

## Verification boundary and artifact handoff
The originating research session recorded 36 Lean 4.34.0 Std theorem declarations over four modules, 26 axiom reports, 813 positive-coefficient comparisons across 18 comparisons, larger bounded exact checks, and separate critiques. The Lean declarations certify specified combinatorial and arithmetic lemmas; they do **not** formalize this entire positive-series theorem or the complete KR1 bijection.

The [research folder](../../terra2026/) contains the illustrated PDF, LaTeX source, research and Lean archive, detailed reviews, and verification records. This page is a publication companion to that research archive.

© 2026 Christopher Yamba.
