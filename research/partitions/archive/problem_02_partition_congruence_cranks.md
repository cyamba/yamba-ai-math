# Problem 02: Combinatorial Cranks & Statistics for General Partition Congruences

* **Source Text:** George E. Andrews & Kimmo Eriksson, *Integer Partitions* (2004), Chapters 5, 10 & Epilogue.
* **Difficulty:** 8.0 / 10
* **Scientific Impact:** 8.5 / 10
* **AI-Agent Tractability:** 8.0 / 10 (Yield Rank #3)

---

## 1. Formal Problem Statement

Ramanujan discovered and proved the three classic partition congruences:
$$p(5n+4) \equiv 0 \pmod 5, \qquad p(7n+5) \equiv 0 \pmod 7, \qquad p(11n+6) \equiv 0 \pmod{11}$$
To explain the $\pmod 5$ and $\pmod 7$ congruences combinatorially, Freeman Dyson (1944) introduced the **rank** of a partition:
$$\operatorname{rank}(\lambda) = \lambda_1 - \ell(\lambda)$$
(largest part minus number of parts), which splits the partitions of $5n+4$ (resp. $7n+5$) into $5$ (resp. $7$) equinumerous residue classes $\pmod 5$ (resp. $\pmod 7$). Because Dyson's rank fails for $11n+6 \pmod{11}$, Dyson conjectured the existence of a **crank**, later found by Andrews and Garvan (1988):
$$\operatorname{crank}(\lambda) = \begin{cases} \lambda_1 & \text{if } \omega(\lambda) = 0 \\ \mu(\lambda) - \omega(\lambda) & \text{if } \omega(\lambda) > 0 \end{cases}$$
where $\omega(\lambda)$ is the number of $1$s in $\lambda$, and $\mu(\lambda)$ is the number of parts strictly larger than $\omega(\lambda)$.

While Ono (2000) and Ahlgren–Ono proved via modular forms and Galois representations that congruences $p(An+B) \equiv 0 \pmod M$ exist for every prime $M \ge 5$, these proofs are purely existential/analytic.

### Concrete Open Targets for `yamba-ai-math`
1. **Explicit Combinatorial Cranks for Higher Prime Congruences & $k$-Regular Partitions:** Discover an explicit combinatorial statistic $C(\lambda) \in \mathbb{Z}$ (built from part multiplicities, Durfee squares, and Frobenius symbols) that divides the partitions of known Ramanujan-type congruences—either for $p(An+B) \pmod{13, 17, 19}$ or for **$k$-colored partitions / overpartitions $\overline{p}(An+B) \pmod{M}$**—into $M$ equinumerous (or cyclic shift-symmetric) residue classes.
2. **Exact Inequalities Between Crank and Rank Moments:** Discover and prove new sharp inequalities or modular identities between higher moments of the Dyson rank $N(m, t, n)$ and Andrews–Garvan crank $M(m, t, n)$ modulo small primes.

---

## 2. Where to Look: Mathematical Toolkit & Search Areas

1. **Garvan's Vector Partitions ($V$-Partitions) & $k$-Cranks:**
   * Study how the Andrews–Garvan crank is the weight of a triple of partitions $(\pi_1, \pi_2, \pi_3)$. Generalizing to $k$-tuples of restricted partitions provides a rich algebraic grammar for new cranks.
2. **Frobenius Symbols & $M_2$-Rank / $bg$-Rank:**
   * Berkovich and Garvan introduced the $bg$-rank (using alternating sums of Frobenius arm and leg lengths) and $M_2$-rank for partitions without repeated odd parts. These statistics are deeply modular and easily computable on Ferrers diagrams.
3. **Hecke Operators on $q$-Series & Mock Modular Forms:**
   * Look at two-variable generating functions $C(z; q) = \sum_{n \ge 0} \sum_{\lambda \vdash n} z^{\operatorname{stat}(\lambda)} q^n$. When $z = \zeta_M$ (an $M$-th root of unity), the series should vanish along the arithmetic progression $An+B$.
4. **Symbolic Regression over Partition ASTs (Abstract Syntax Trees):**
   * Define a domain-specific language (DSL) of partition primitives: `max_part(p)`, `num_parts(p)`, `count_ones(p)`, `durfee_size(p)`, `frobenius_arm(p, i)`, `conjugate(p)`. Use genetic programming / LLM-guided tree search to evolve formulas $f(\lambda)$ that minimize the variance of residue bucket sizes modulo $M$.

---

## 3. Agentic Playbook for `yamba-ai-math`

* **Phase 1 (`Explorer-Sage`):** Select a family of congruences (e.g., overpartitions $\overline{p}(n)$, $k$-regular partitions $b_k(n)$, or Andrews' singular overpartitions) and compute the full partition tables for the first 15 values of $n$ in the arithmetic progression $An+B$.
* **Phase 2 (`Conjecturer-Symbolic`):** Run an evolutionary search over the Partition-DSL ASTs. Score each candidate statistic $S(\lambda)$ by the Shannon entropy / chi-squared uniformity of the buckets $\{ \lambda \vdash (An+B) : S(\lambda) \equiv r \pmod M \}$ across $n=0, 1, \dots, 12$.
* **Phase 3 (`RedTeam-Falsifier`):** When a zero-variance (exact equinumerous) statistic $S^*(\lambda)$ is found, test it at $n=13, 14, 15$ and construct its bivariate generating function $\sum z^{S^*(\lambda)} q^{|\lambda|}$ to verify division by the cyclotomic polynomial $\Phi_M(z)$.
* **Phase 4 (`Formalizer-Lean4` & `Exposition-TikZ-Scribe`):** Formalize the statistic $S^*$, verify the finite partition congruence buckets in Lean 4, and render color-coded residue tables and Frobenius diagram decompositions in LaTeX.