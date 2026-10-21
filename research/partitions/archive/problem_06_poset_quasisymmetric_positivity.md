# Problem 06: $e$-Positivity and Schur-Positivity in $(P, \omega)$-Partitions & Chromatic Symmetric Functions

* **Source Text:** Richard P. Stanley, *Enumerative Combinatorics, Vol. 1* (Section 3.15) & *Vol. 2* (Section 7.19 & Exercise 7.47).
* **Difficulty:** 7.0 / 10 (Sub-families & Involutions) | 8.5 / 10 (General)
* **Scientific Impact:** 8.5 / 10
* **AI-Agent Tractability:** 9.5 / 10 (Yield Rank #1 — Top Breakthrough Target)

---

## 1. Formal Problem Statement

In *Enumerative Combinatorics*, Stanley introduced the theory of **$(P, \omega)$-partitions** (generalizing MacMahon's plane partitions and ordinary integer partitions to arbitrary labeled posets $(P, \omega)$) and its sister object, the **chromatic symmetric function** $X_G(\mathbf{x})$ of the incomparability graph $G = \operatorname{inc}(P)$:
$$K_{(P, \omega)}(\mathbf{x}) = \sum_{L \in \mathcal{L}(P, \omega)} F_{\operatorname{Des}(L, \omega)}(\mathbf{x}), \qquad X_{\operatorname{inc}(P)}(\mathbf{x}) = \sum_{\kappa : V \to \mathbb{Z}_{>0} \text{ proper}} x_{\kappa(v_1)} x_{\kappa(v_2)} \cdots x_{\kappa(v_n)}$$
Every symmetric function $f(\mathbf{x}) \in \Lambda_n$ can be expanded in the basis of **Schur functions** $\{s_\lambda\}_{\lambda \vdash n}$ or **elementary symmetric functions** $\{e_\lambda\}_{\lambda \vdash n}$:
$$f(\mathbf{x}) = \sum_{\lambda \vdash n} c_\lambda s_\lambda(\mathbf{x}) = \sum_{\lambda \vdash n} d_\lambda e_\lambda(\mathbf{x})$$
Because every $e_\lambda$ is Schur-positive, $e$-positivity ($d_\lambda \ge 0$ for all $\lambda \vdash n$) implies Schur-positivity ($c_\lambda \ge 0$ for all $\lambda \vdash n$).

The famous **Stanley–Stembridge Conjecture (1993)** (and its Shareshian–Wachs $q$-refinement, with recent monumental algebraic geometry breakthroughs by Hikita in late 2024 using probabilistic/representation-theoretic reductions) asks for an explicit **combinatorial interpretation** of the coefficients $d_\lambda \ge 0$ for $(3+1)$-free posets (and unit interval orders), alongside Stanley's broader **$(P, \omega)$-Partition Schur-Positivity Problem**: characterizing which labeled posets $(P, \omega)$ have a symmetric and Schur-positive generating function $K_{(P, \omega)}(\mathbf{x})$.

### Concrete Open Targets for `yamba-ai-math`
1. **Explicit Sign-Reversing Involutions for $e$-Positivity & $s$-Positivity:** Even with algebraic proofs of $e$-positivity for unit interval orders, finding an **explicit, weight-preserving sign-reversing involution** $\iota$ on the signed $P$-tableau expansion (Stanley's acyclic orientation / $P$-tableau formula of Gasharov) whose fixed points directly count $d_\lambda$ (or $c_\lambda$ for $(P,\omega)$-partitions) remains open for major poset families (e.g., general unit interval orders, $(3+1)$-free posets outside melting lollipops, or specific $(P,\omega)$-labeled posets).
2. **Classification & Counterexample Discovery for $(P, \omega)$-Schur-Positivity:** Characterize new infinite families of labeled posets $(P, \omega)$ beyond Skew Ferrers diagrams where $K_{(P, \omega)}(\mathbf{x})$ is symmetric and Schur-positive, or discover the minimal obstructions.

---

## 2. Where to Look: Mathematical Toolkit & Search Areas

1. **Gasharov's $P$-Tableaux & Stembridge's Sign-Reversing Involution:**
   * Gasharov (1996) proved that $X_{\operatorname{inc}(P)}(\mathbf{x})$ is **Schur-positive** for all $(3+1)$-free posets by constructing a brilliant sign-reversing involution on pairs of $P$-tableaux (swapping elements between adjacent columns when a $P$-dominance condition fails). This is the exact blueprint our AI agent can adapt to the **elementary ($e_\lambda$)** basis or to **$(P,\omega)$-partitions**!
2. **Guay-Paquet's Modular Law & Unit Interval Order Dyck Paths:**
   * Every unit interval order on $n$ elements is uniquely encoded by a **Dyck path** (or bounce vector $\mathbf{a} = (a_1, \dots, a_n)$). Furthermore, the **Modular Law** (Guay-Paquet / Abrego–Orellana–Scott) provides linear recurrence relations $X_P - X_{P'} = X_{P''} - X_{P'''}$ when triples of intervals satisfy simple containment conditions.
3. **SAT / SMT Encoding of Sign-Reversing Involutions:**
   * For any fixed poset $P$, the signed combinatorial expansion in the $e_\lambda$ or $s_\lambda$ basis is a finite bipartite graph $G_\lambda = (T^+_\lambda, T^-_\lambda, E)$ between positive-sign tableaux $T^+_\lambda$ and negative-sign tableaux $T^-_\lambda$. Finding a uniform local rule that matches every negative tableau $t^- \in T^-_\lambda$ injectively to a positive tableau $t^+ \in T^+_\lambda$ is a **finite constraint satisfaction problem (Z3/SAT)** that can be solved simultaneously across all posets of size $n \le 8$ to synthesize a universal combinatorial rule!

---

## 3. Agentic Playbook for `yamba-ai-math`

* **Phase 1 (`Explorer-Sage`):** Using `SageMath` (`Posets.UnitIntervalOrders(n)`, `ChromaticSymmetricFunction`, and `StanleySymmetricFunction`), generate the full signed tableau spaces $(T^+_\lambda, T^-_\lambda)$ and exact $e_\lambda / s_\lambda$ expansions for all target posets up to $n = 9$.
* **Phase 2 (`Conjecturer-Symbolic`):** Encode the search for a local tableau-swapping operator $\iota : T^+_\lambda \cup T^-_\lambda \to T^+_\lambda \cup T^-_\lambda$ as a parameterized decision tree over local poset comparisons ($x <_P y$, $x \sim_P y$). Use Z3/evolutionary search to find a rule satisfying:
  1. $\iota(\iota(t)) = t$ (involution),
  2. $\text{sign}(\iota(t)) = -\text{sign}(t)$ whenever $\iota(t) \ne t$,
  3. $\iota(t) = t \implies \text{sign}(t) = +1$ (all fixed points are positive!).
* **Phase 3 (`Formalizer-Lean4`):** Because a sign-reversing involution on finite sets immediately implies positivity via a standard `Finset.sum_involution` lemma in `Mathlib4`, the Lean 4 proof becomes remarkably clean and modular!
* **Phase 4 (`Exposition-TikZ-Scribe`):** Automatically render the poset Hasse diagrams, Dyck path encodings, $P$-tableaux, and red/blue involution matching arrows in TikZ.