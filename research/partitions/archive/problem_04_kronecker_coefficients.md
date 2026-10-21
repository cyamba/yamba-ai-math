# Problem 04: Combinatorial Interpretation & Positivity of Kronecker Coefficients

* **Source Text:** Richard P. Stanley, *Enumerative Combinatorics, Vol. 2* (1999), Chapter 7 (Symmetric Functions), Exercise 7.78–7.84 & Open Problems.
* **Difficulty:** 9.8 / 10 (General) | 7.5 / 10 (Restricted Shapes)
* **Scientific Impact:** 10.0 / 10
* **AI-Agent Tractability:** 6.0 / 10 (Yield Rank #5)

---

## 1. Formal Problem Statement

For three partitions $\lambda, \mu, \nu \vdash n$, the **Kronecker coefficient** $g(\lambda, \mu, \nu)$ is the multiplicity of the irreducible representation $V_\nu$ inside the tensor product $V_\lambda \otimes V_\mu$ of irreducible representations of the symmetric group $\mathfrak{S}_n$. Equivalently, via the Frobenius characteristic map and Schur functions $s_\lambda$:
$$s_\lambda * s_\mu = \sum_{\nu \vdash n} g(\lambda, \mu, \nu) s_\nu, \qquad g(\lambda, \mu, \nu) = \frac{1}{n!} \sum_{w \in \mathfrak{S}_n} \chi^\lambda(w) \chi^\mu(w) \chi^\nu(w)$$
Unlike the Littlewood–Richardson coefficients $c^\nu_{\lambda \mu}$ (which have an explicit positive combinatorial rule via semistandard tableaux and Knutson–Tao honeycombs), **no general positive combinatorial interpretation** (counting a set of combinatorial objects without signs) is known for $g(\lambda, \mu, \nu)$ (Stanley's Problem 10 in *Positivity Problems in Algebraic Combinatorics*).

Furthermore, **Saxl's Conjecture (2012)** asserts that for the staircase partition $\rho_k = (k, k-1, \dots, 2, 1) \vdash \binom{k+1}{2}$, the tensor square $V_{\rho_k} \otimes V_{\rho_k}$ contains *every* irreducible representation $V_\nu$ of $\mathfrak{S}_n$, i.e.:
$$g(\rho_k, \rho_k, \nu) > 0 \quad \forall \nu \vdash \binom{k+1}{2}$$

### Concrete Open Targets for `yamba-ai-math`
1. **Explicit Combinatorial Rule for New Restricted Triple Families:** Extend Blasiak's (2017) rule for one hook shape and Remmel–Whitehead's rules for two-row shapes to an explicit positive tableau/lattice-point counting rule when $\lambda, \mu$ are **two-row-plus-hook shapes** or **near-rectangular shapes**.
2. **Polyhedral / Saturation Rules for Saxl's Conjecture Subfamilies:** Prove $g(\rho_k, \rho_k, \nu) > 0$ for an infinite family of shapes $\nu$ not yet covered by Ikenmeyer–Pak–Panova or Bessenrodt–Bowman–Sutton (e.g., specific 4-row or hook-augmented shapes) by constructing explicit non-vanishing character or standard Young tableau (SYT) witnesses.

---

## 2. Where to Look: Mathematical Toolkit & Search Areas

1. **Blasiak's Colored Yamanouchi Words & Barred Tableaux:**
   * Jonah Blasiak solved the case where one partition is a hook $(n-d, 1^d)$ using colored tableaux and super-alphabet insertion (Haiman's mixed insertion). Extending these local insertion/jeu-de-taquin rules is the prime combinatorial avenue.
2. **Kirillov–Klyachko Quantum Marginal Polytopes & Eigenvalue Cones:**
   * In Geometric Complexity Theory (Mulmuley–Sohoni), reduced Kronecker coefficients $\bar{g}(\lambda, \mu, \nu)$ stabilize as the first part grows. They are governed by integer points in polyhedral cones (Hive-like polytopes) modulo quasi-polynomial Chamber structures.
3. **Comparable Partitions & Dominance Order Semigroups:**
   * Use the **Semigroup Property** of Kronecker coefficients (Christandl–Harrow–Mitchison): if $g(\lambda^{(1)}, \mu^{(1)}, \nu^{(1)}) > 0$ and $g(\lambda^{(2)}, \mu^{(2)}, \nu^{(2)}) > 0$, then $g(\lambda^{(1)}+\lambda^{(2)}, \mu^{(1)}+\mu^{(2)}, \nu^{(1)}+\nu^{(2)}) > 0$. This allows an AI agent to prove positivity for infinite families by finding a finite **Hilbert basis** of atomic positive triples!

---

## 3. Agentic Playbook for `yamba-ai-math`

* **Phase 1 (`Explorer-Sage`):** Using `SymmetricFunctions(QQ).s().kronecker_product()` in SageMath, compute exact databases of $g(\lambda, \mu, \nu)$ and reduced Kronecker coefficients $\bar{g}(\alpha, \beta, \gamma)$ for restricted row lengths $\ell(\lambda), \ell(\mu), \ell(\nu) \le 3$.
* **Phase 2 (`Conjecturer-Symbolic`):**
  * *Track A (Semigroup / Saxl):* Decompose target partitions $\nu$ into sums of small base partitions where $g > 0$ via Integer Linear Programming (Z3/Gurobi) to construct an inductive Hilbert-basis proof of positivity.
  * *Track B (Ehrhart Quasi-polynomials):* Fit piecewise quasi-polynomials to $\bar{g}(k\alpha, k\beta, k\gamma)$ and extract the bounding inequalities of the Kronecker cone facets.
* **Phase 3 (`Formalizer-Lean4`):** Formalize the semigroup decomposition lemma and verify the base-case character inner products in Lean 4.
* **Phase 4 (`Exposition-TikZ-Scribe`):** Render 3D chamber complex slices, Young diagram decompositions, and colored Yamanouchi tableaux in TikZ.