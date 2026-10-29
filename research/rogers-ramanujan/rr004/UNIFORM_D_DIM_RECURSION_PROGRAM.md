# Phase 2 Research Program: Uniform $d$-Dimensional Recursive Bijection ($a \to \infty$) for Kanade–Russell $I_1$ and General-$n$ Dual Jacobi–Trudi Cancellation

**Originating Insight:** Christopher Yamba's 3D and $d$-dimensional Ferrers diagram principle (sliding along descending higher-dimensional axes and decomposing multi-scale partition families into $d$-dimensional Ferrers octants).

---

## 1. Objective of Phase 2

In Phase 1 (committed on `feat/multidimensional-ferrers-bijections`), we established:
1. The **3D rotation $\Phi_{221}$**, the **universal interior hook slides $\Psi_{\mathrm{hook}}^{(m)}$**, the **$n$-dimensional $\beta$-rearrangement theorem**, and the **complete 6-sector Dual Jacobi–Trudi injection for $[e_{4,1}] X_G$ at $n=5$** (verified in Lean 4 `MultidimensionalFerrers.lean` and `multidimensional_ferrers.py`).
2. The **6D Ferrers Cone Theorem** in $(10^z, 9^y, 8^x, 6^{c_6}, 3^{c_3}, 1^{c_1})$, the **universal $(a=3, b=0, \forall \mu)$ bijection** (`reconstruct_a3_b0` / `decompose_a3_b0`, verified through $N = 35$), and the **complete round-trip KR1 bijection $\mathcal{B} \leftrightarrow \mathcal{U} \leftrightarrow \mathcal{C} \leftrightarrow \mathcal{A}$ through weight $N = 26$** (`rr004_multidim_cones.py`).

**Phase 2** pursues the full infinite-dimensional generalization ($a \to \infty$ and $n \to \infty$) across two tracks:
- **Track 2A (Uniform Recursive $d$-Dimensional KR1 Bijection for All $a, b \ge 0$):** Turn the scale-3 self-similarity identity
  $$Q(3c + r, b) = r^2 + 3r(b + 2c) + 3\,Q(b, c) \qquad (r \in \{0, 1, 2\})$$
  (machine-checked in `MultidimensionalFerrers.kr1_scale3_self_similarity`) into a **single uniform recursive operator** $\mathcal{R}_3 : \mathcal{C}_{c, b} \times \text{ResidueCone}_r \to \mathcal{U}$ that constructs and inverts $\mathcal{C} \leftrightarrow \mathcal{U}$ for arbitrary $a \ge 0, b \ge 0$ without finite-weight cutoffs.
- **Track 2B (General-$n$ Multi-Sector Dual Jacobi–Trudi Cancellation on $\beta$-Rearrangements):** Combine the $n$-dimensional $\beta$-rearrangement space $\mathrm{Perm}(\lambda_1, \dots, \lambda_k, 0^{n-k})$ (Theorem 1.3) with the universal $(0, k) \leftrightarrow (k-1, 1)$ cascade (`MultidimensionalFerrers.cascade_split_preserves_all`) and 3D Ferrers rotations to cancel negative Dual Jacobi–Trudi sectors for general $n$.

---

## 2. Mathematical Architecture of Track 2A ($a \to \infty$ Scale-3 Recursion)

### 2.1 The Scale-3 Dilation Operator $D_3 : \mathcal{U} \to \mathcal{U}_{3\text{-div}}$

By `kr1_scale3_divisible`, $Q(3c, b) = 3\,Q(b, c)$, where the roles of $(a, b) = (3c, b)$ and $(b', a') = (b, c)$ swap under scale-3 dilation!
More generally, for a cluster state $C = (a, b, \mu, \nu)$ with $a = 3c + r$ ($r \in \{0, 1, 2\}$):
1. **Group the $3c$ single clusters into $c$ triples** $T_k = (\mu_{3k}, \mu_{3k+1}, \mu_{3k+2})$ for $0 \le k < c$, leaving $r \in \{0, 1, 2\}$ residual head singles.
2. **Mod-3 Difference Coordinates on Each Triple:** Write the differences within triple $T_k$ as
   $$d_{3k+3} = \mu_{3k} - \mu_{3k-1}, \qquad d_{3k+2} = 3q_{2,k} + r_{2,k}, \qquad d_{3k+1} = \mu_{3k+2} - \mu_{3k+1}.$$
   Then the weight contribution of triple $T_k$ splits into:
   - A **3-divisible core** of weight $3 \cdot \text{wt}_{\text{sub}}$, which combines with the $b$ two-clusters $\nu$ into an effective lower-rank state $\widetilde{C} \in \mathcal{C}$ of rank $(a', b') \approx (b, c)$ scaled by $3$, plus
   - A **6D Ferrers cone head** determined by the residue vector $(r, r_{2,0}, \dots, r_{2,c-1}) \in \{0, 1, 2\}^{c+1}$ and the $+1$ carry steps $d_{3k+1}$.

### 2.2 Concrete Milestones for Track 2A

1. **Milestone 2A.1 — Uniform $(a = 3, \forall b \ge 0, \forall \mu, \forall \nu)$ Bijection:**
   Unify `reconstruct_a3_b0`, `reconstruct_a3_b1`, and the universal $b \ge 2$ core $(3(b+2), 3(b+1), 3b^{2+\Delta_b}, \dots, 3^{2+\Delta_1})$ into a single closed-form forward and inverse map for **all** $a = 3, b \ge 0$ and all $(\mu, \nu)$, verified through weight $N = 40$.
2. **Milestone 2A.2 — Uniform $(a = 4, \forall b \ge 0)$ and $(a = 5, \forall b \ge 0)$ Bijections:**
   Extend the $(a-1)$-column head decomposition $Q(a, b) = 3b(b+1) + a^2 + 3(a-1)b$ (`kr1_head_offset_identity`) to all $b \ge 0$ for $a \in \{4, 5\}$, verified through weight $N = 40$.
3. **Milestone 2A.3 — Recursive Scale-3 Lift for $a \ge 6$:**
   Implement the recursive scale-3 reduction $(3c + r, b) \to (b, c)$ and verify the complete round-trip bijection $\mathcal{B} \leftrightarrow \mathcal{U} \leftrightarrow \mathcal{C} \leftrightarrow \mathcal{A}$ through weight $N = 40$ (where $a = 6$ enters at $N = 36$).

---

## 3. Mathematical Architecture of Track 2B (General-$n$ Multi-Sector DJT Cancellation)

1. **Milestone 2B.1 — $\beta$-Rearrangement Adjacent Transposition Graph:**
   For any $\lambda \vdash n$, organize the valid rearrangements $\beta \in \mathrm{Perm}(\hat{\lambda})$ (with distinct shifted keys $\kappa_j(\beta) = \beta_j - j$) into a bipartite graph of positive-sign and negative-sign sectors connected by adjacent swaps $(j, j+1)$ and 3D Ferrers rotations.
2. **Milestone 2B.2 — Complete Multi-Sector Cancellation at $n = 6$:**
   Extend `six_sector_e41_injection` from $n = 5$ to all non-trivial two-row and three-row elementary coefficients $[e_\lambda] X_G$ across all 132 Hessenberg vectors at $n = 6$.
3. **Milestone 2B.3 — Lean 4 Formalization of Phase 2 Theorems:**
   Formalize the general-$a$ recursive weight decomposition and multi-sector survivor theorems in Lean 4 (`MultidimensionalFerrersPhase2.lean`) and open the Phase 2 Pull Request.
