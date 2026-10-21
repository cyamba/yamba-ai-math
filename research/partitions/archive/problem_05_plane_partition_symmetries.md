# Problem 05: Enumeration of Plane Partitions Under Exotic Symmetry & Boundary Classes

* **Source Text:** Richard P. Stanley, *Enumerative Combinatorics, Vol. 2* (1999), Section 7.20 (Plane Partitions) & Exercise 7.101–7.107.
* **Difficulty:** 8.0 / 10
* **Scientific Impact:** 7.5 / 10
* **AI-Agent Tractability:** 7.5 / 10 (Yield Rank #4)

---

## 1. Formal Problem Statement

A **plane partition** $\pi = (\pi_{i,j})_{1 \le i \le r, 1 \le j \le c}$ inside an $r \times c \times t$ box $B(r, c, t)$ is an array of integers $0 \le \pi_{i,j} \le t$ that is weakly decreasing along rows and columns:
$$\pi_{i,j} \ge \pi_{i+1,j} \quad \text{and} \quad \pi_{i,j} \ge \pi_{i,j+1}$$
Equivalently, viewing each entry $\pi_{i,j}$ as a stack of $1 \times 1 \times 1$ unit cubes, $\pi$ corresponds to a **lozenge tiling** of a hexagon with side lengths $(r, c, t, r, c, t)$. MacMahon (1915) proved the famous box formula:
$$\sum_{\pi \subseteq B(r,c,t)} q^{|\pi|} = \prod_{i=1}^r \prod_{j=1}^c \prod_{k=1}^t \frac{1 - q^{i+j+k-1}}{1 - q^{i+j+k-2}}$$
Stanley (1986) classified the **10 symmetry classes** of plane partitions in $B(n,n,n)$ formed by combinations of transposition ($T$), complementation ($C$), and cyclic rotation ($R$), all of which eventually yielded elegant closed-form product formulas (culminating in Andrews, Robbins, Zeilberger, Kuperberg, and Stembridge).

### Concrete Open Targets for `yamba-ai-math`
While the classical 10 symmetry classes in a pure $n \times n \times n$ box are solved, major open conjectures and undiscovered product formulas remain when **dihedral symmetries are combined with non-trivial boundary profiles, punctures (holes), or $q$-weights**:
1. **Dihedral Symmetry Classes of Punctured Hexagons / Cored Plane Partitions:** Discover and prove new exact product formulas (or two-term Pfaffian sums) for cyclically symmetric or self-complementary plane partitions containing a central triangular/hexagonal core removal or fixed diagonal profiles (extending Ciucu–Krattenthaler and Fischer).
2. **Refined $q$-Enumeration of Alternating Sign Matrix (ASM) / TSSCPP Bijective Statistics:** Find new equidistributed multi-statistics between Totally Symmetric Self-Complementary Plane Partitions (TSSCPPs) in $B(2n, 2n, 2n)$ and $n \times n$ Alternating Sign Matrices (ASMs), advancing the open quest for an explicit bijection between TSSCPPs and ASMs.

---

## 2. Where to Look: Mathematical Toolkit & Search Areas

1. **Lindström–Gessel–Viennot (LGV) Non-Intersecting Lattice Paths:**
   * Every plane partition in $B(r,c,t)$ bijects onto a family of non-intersecting lattice paths. Under symmetry constraints, the count reduces to a **determinant** or **Pfaffian** (Stembridge's Theorem) of binomial/hypergeometric entries.
2. **Krattenthaler's `Rate` Heuristics & LLL Prime-Factorization Guessing:**
   * In enumerative combinatorics, if the sequence of counts $A(1), A(2), \dots, A(8)$ for a family of plane partitions factors completely into *small prime numbers* (e.g., primes $\le 2n+1$), there is almost certainly a closed-form hypergeometric product formula! An AI agent can scan thousands of boundary/symmetry configurations and flag any configuration whose counts are "smooth numbers" (small prime factors).
3. ** Kuo's Graphical Condensation (Dodgson Condensation):**
   * Once an agent guesses a closed-form product formula $F(n, k)$ for a family of lozenge tilings / plane partitions, **Kuo condensation** provides an almost completely mechanical inductive proof: one chooses 4 boundary vertices $a,b,c,d$ and verifies the bilinear recurrence $F(\mathcal{G}) F(\mathcal{G} - \{a,b,c,d\}) = F(\mathcal{G}-\{a,b\}) F(\mathcal{G}-\{c,d\}) + F(\mathcal{G}-\{a,d\}) F(\mathcal{G}-\{b,c\})$ purely algebraically!

---

## 3. Agentic Playbook for `yamba-ai-math`

* **Phase 1 (`Explorer-Sage`):** Parameterize a family of plane partitions with boundary defects/symmetries (via Kasteleyn matrices or LGV determinants in SageMath) and compute exact counts $A(n, k)$ for $n \le 10$. Filter exclusively for families where $A(n, k)$ is $P$-smooth (all prime factors $\le 3n$).
* **Phase 2 (`Conjecturer-Symbolic`):** Use rational interpolation and logarithmic prime-exponent linear algebra to guess the exact closed-form ratio of factorials/Pochhammer symbols for $A(n, k)$.
* **Phase 3 (`Formalizer-Lean4`):** Apply Kuo's graphical condensation or LU determinant factorization (Dodgson condensation) so that the inductive step reduces to a polynomial ring identity (`ring` tactic in Lean 4!).
* **Phase 4 (`Exposition-TikZ-Scribe`):** Auto-generate isometric 3D stacked-cube plane partition renderings, dual lozenge tilings, and non-intersecting LGV lattice path diagrams in TikZ.