# Problem 03: Asymptotic Parity & Modular Density Distribution of $p(n)$

* **Source Text:** George E. Andrews & Kimmo Eriksson, *Integer Partitions* (2004), Chapter 10 & Open Problems.
* **Difficulty:** 9.9 / 10
* **Scientific Impact:** 9.5 / 10
* **AI-Agent Tractability:** 3.5 / 10 (Yield Rank #6)

---

## 1. Formal Problem Statement

Let $p(n)$ be the ordinary partition function. **Parkin and Shanks (1967)** conjectured that the parity of $p(n)$ is asymptotically equidistributed:
$$\lim_{X \to \infty} \frac{\#\{1 \le n \le X : p(n) \equiv 0 \pmod 2\}}{X} = \frac{1}{2}$$
Even weaker statements remain shockingly difficult. **Subbarao's Conjecture** (proved for even values by Kolberg/Mirsky, and for odd values in arithmetic progressions by Ono, Radu, and others) states that for every arithmetic progression $r \pmod t$, there exist infinitely many $n \equiv r \pmod t$ such that $p(n)$ is even, and infinitely many such that $p(n)$ is odd.

Currently, the best lower bounds for the number of even or odd values of $p(n)$ for $n \le X$ (due to Bellaïche, Nicolas, Serre, Ahlgren, and Boylan) are of the form:
$$\#\{n \le X : p(n) \text{ is even}\} \gg \sqrt{X}, \qquad \#\{n \le X : p(n) \text{ is odd}\} \gg \frac{\sqrt{X}}{\log \log X}$$
Closing the gap between $\sqrt{X}$ and $X$ for the ordinary partition function $p(n)$ is one of the hardest open problems in number theory.

### Concrete Open Targets for `yamba-ai-math` (Tractable Variants!)
While proving the Parkin–Shanks conjecture for $p(n)$ is beyond current analytic methods, **tractable breakthroughs exist for restricted partition functions and explicit Subbarao-type progressions:**
1. **Explicit Subbarao / Radu Parity Verification for High Moduli:** Prove that for specific restricted partition functions $p_S(n)$ (or $k$-regular partitions $b_k(n)$ modulo 2 or 3), every arithmetic progression $An+B$ (up to a high modulus $A$) contains infinitely many odd and even values, by finding explicit Sturm bounds on modular forms modulo 2.
2. **Sharp Lower Bounds via Nicolas–Serre Hecke Algebras:** Use computer-assisted Hecke algebra nilpotency calculations (following Bellaïche–Nicolas) to improve the exponent or constant in the density of $p(n) \equiv r \pmod m$ for specific small moduli.

---

## 2. Where to Look: Mathematical Toolkit & Search Areas

1. **Sturm's Theorem & Radu's Algorithm for Modular Forms $\pmod \ell$:**
   * Any identity or non-vanishing property of a modular form modulo a prime $\ell$ can be verified completely by checking a finite number of Fourier coefficients up to the **Sturm bound** $B(\Gamma_0(N), k)$. This turns an infinite number-theoretic theorem into a finite computation!
2. **Nicolas–Serre Theory of Nilpotency of Hecke Operators $\pmod 2$:**
   * Let $f(q) = \sum_{n \text{ odd}} p((24n+1)/24) q^n \pmod 2$. The action of Hecke operators $T_p$ ($p \ge 5$ prime) generates a local nilpotent algebra over $\mathbb{F}_2$. Computing the exact index of nilpotency $g(f)$ directly yields explicit asymptotic lower bounds $\#\{n \le X : p(n) \equiv 1 \pmod 2\} \gg \sqrt{X} (\log \log X)^k$.
3. **Glaisher's & Euler's Recurrence Identities Modulo $2^k$:**
   * Use binary quadratic form representations (e.g., $\theta$-series identities modulo $2$) where $p(n) \pmod 2$ is linked to the number of representations of $24n-1$ by specific quadratic forms.

---

## 3. Agentic Playbook for `yamba-ai-math`

* **Phase 1 (`Explorer-Sage`):** Compute $p(n) \pmod 2$ (and restricted variants $b_k(n) \pmod 2$) up to $N = 10^6$ using Fast Fourier Transform / FLINT polynomial inversion in SageMath, storing bitsets for rapid Hecke operator evaluation.
* **Phase 2 (`Conjecturer-Symbolic`):** Apply combinations of Hecke operators $T_{p_1} T_{p_2} \cdots T_{p_r} \pmod 2$ to the generating series to search for lacunary $\theta$-series reductions with provable density bounds, or execute Radu's algorithm to certify non-vanishing in open arithmetic progressions.
* **Phase 3 (`Formalizer-Lean4`):** Formalize the finite Sturm-bound reduction lemma and verify the polynomial congruence certificate in Lean 4.
* **Phase 4 (`Exposition-TikZ-Scribe`):** Generate high-resolution parity Ulam spirals, Hecke transition graphs, and modular fundamental domain diagrams in LaTeX.