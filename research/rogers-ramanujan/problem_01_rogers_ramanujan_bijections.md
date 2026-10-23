# Problem 01: Algorithmic Bijective Proofs for Rogers-Ramanujan-Type Identities

* **Source Text:** George E. Andrews & Kimmo Eriksson, *Integer Partitions* (2004), Chapter 8 & Epilogue.
* **Difficulty:** 7.5 / 10
* **Scientific Impact:** 8.0 / 10
* **AI-Agent Tractability:** 9.0 / 10 (Yield Rank #2)

---

## 1. Formal Problem Statement

Let $\mathcal{P}(n)$ denote the set of integer partitions of $n$. A **Rogers-Ramanujan-type identity** asserts that for all $n \ge 0$, two restricted subsets of partitions $\mathcal{A}(n), \mathcal{B}(n) \subseteq \mathcal{P}(n)$ have equal cardinality:
$$|\mathcal{A}(n)| = |\mathcal{B}(n)|$$
Typically:
* $\mathcal{A}(n)$ is defined by **difference conditions** between parts at distance $d$ (e.g., $\lambda_i - \lambda_{i+d} \ge c$, plus boundary conditions on the smallest parts).
* $\mathcal{B}(n)$ is defined by **congruence conditions** on the parts modulo some integer $M$ (e.g., $\lambda_i \equiv r_1, r_2, \dots \pmod M$).

For the classical Rogers-Ramanujan identities ($M=5$, $d=1$, $c=2$), analytic proofs via the Jacobi Triple Product and Watson's $q$-analogue of Whipple's theorem are straightforward, whereas constructing an explicit, natural, weight-preserving **combinatorial bijection**
$$\Phi_n : \mathcal{A}(n) \stackrel{\sim}{\longrightarrow} \mathcal{B}(n)$$
required the Garsia–Milne involution principle (1981) or Pak/Boulet-Pak direct Dyson-map iterations.

### Concrete Open Targets for `yamba-ai-math`
1. **Direct (Involution-Free) Bijections for Higher-Modulus Identities:** Construct an explicit, local Ferrers-diagram or Durfee-square surgical bijection $\Phi_n$ for the **Göllnitz–Gordon identities** (modulus 8), **Schur's 1926 Partition Theorem** (modulus 6), or the **Andrews–Gordon identities** ($M = 2k+1$) that avoids the non-constructive cancellation loops of the Garsia–Milne involution principle.
2. **Bijective Resolution of Kanade–Russell Conjectures:** Provide an explicit bijective map and refined multi-statistic generating function for the **Kanade–Russell (2015) modulo 9 and modulo 12 identities**, where analytic and bijective machinery remain actively contested.

---

## 2. Where to Look: Mathematical Toolkit & Search Areas

To equip our AI agents to synthesize $\Phi_n$, the harness should search and combine primitives from the following five areas:

1. **Bressoud's & Pak's Iterative Dyson Maps:**
   * Look at how two-row arrays and iterated Dyson rank transformations peel hooks off Ferrers diagrams and reassemble them into congruence-restricted parts.
2. **2-Modular & $k$-Modular Ferrers Diagrams:**
   * Represent parts not as rows of $1 \times 1$ boxes, but as rows of $2$-ominoes or residue-weighted boxes (Corteel–Lovejoy overpartition frameworks).
3. **Cylindric Partitions & Crystal Base Theory:**
   * Connect difference conditions to energy functions on affine crystals $B(\Lambda)$ of $\widehat{\mathfrak{sl}}_n$ (Kang, Misra, Miwa). Bijections often become transparent when translated into paths in crystal graphs.
4. **Sylvester's & Franklin's Involution Templates:**
   * Generalize the slope-intersection geometry of Franklin's pentagonal number involution (moving the smallest part vs. rightmost diagonal) to steeper slopes ($2$-hooks, $3$-hooks).
5. **Symbolic Cellular Automata / Local Rewrite Systems:**
   * Frame a bijection as a confluent term-rewriting system (or 2D cellular automaton) on the integer sequence $(\lambda_1, \lambda_2, \dots, \lambda_k)$ that preserves $\sum \lambda_i = n$ while monotonically decreasing a "difference-violation energy" until the partition lands in $\mathcal{B}(n)$.

---

## 3. Agentic Playbook for `yamba-ai-math`

* **Phase 1 (`Explorer-Sage`):** Enumerate $\mathcal{A}(n)$ and $\mathcal{B}(n)$ for $1 \le n \le 30$. Compute all known statistics on every partition (length $\ell(\lambda)$, Durfee square size $d(\lambda)$, largest part $\lambda_1$, number of odd parts, Dyson rank, 2-core).
* **Phase 2 (`Conjecturer-Symbolic`):** Search for **preserved joint statistics** $(s_1, s_2)$ such that $|\{\lambda \in \mathcal{A}(n) : s(\lambda) = v\}| = |\{\mu \in \mathcal{B}(n) : s'(\mu) = v\}|$. Once a refined statistic match is found, the bipartite matching space for $\Phi_n$ shrinks dramatically (often to singleton or size-2 buckets!).
* **Phase 3 (`Formalizer-Lean4`):** Define $\mathcal{A}(n)$ and $\mathcal{B}(n)$ as `Finset (Nat.Partition n)` in Lean 4, implement $\Phi_n$, prove $\Phi_n(\lambda) \in \mathcal{B}(n)$ and $\Psi_n(\Phi_n(\lambda)) = \lambda$.
* **Phase 4 (`Exposition-TikZ-Scribe`):** Auto-generate side-by-side shaded Ferrers diagrams showing the Durfee square dissection and hook shifts for $n=15$.