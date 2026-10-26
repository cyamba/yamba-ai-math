# From a 2D Corner Obstruction to 3D and d-Dimensional Ferrers Diagram Bijections: Tableau Positivity and the Kanade–Russell $I_1$ Identity

**Author:** Christopher Yamba ([www.christopheryamba.com](https://www.christopheryamba.com))
**Original collaborator:** Antigravity (Google DeepMind)
**Revision 2:** October 26, 2026. Original record timestamp: `2026-10-24T22:42:00Z` (`2026-10-25T00:42:00+02:00`).
**Status:** Research preprint with corrected constructions, finite computational evidence, and explicit remaining proof obligations.

## Abstract and motivating geometric idea

Christopher Yamba proposed exploring a third Ferrers coordinate when a planar corner slide creates an illegal column descent, and extending this viewpoint to higher dimensions. This motivates the local rotations and partition-coordinate experiments recorded here. The extra coordinate is useful bookkeeping; a comparable prefix $C=(c_1,\ldots,c_p)$ satisfies $c_i<_P b$ for each $i$, but this does **not** assert a chain $c_1>_P\cdots>_P c_p$.

The paper proves a local fiber-injectivity statement, conditional tableau rotations, a general hook-slide argument, a signed-array cascade, and a corrected beta-rearrangement bijection. Python enumeration verifies the full routing and selected Dual Jacobi–Trudi cancellations for all 42 natural unit interval orders at $n=5$ and all 132 at $n=6$. For Kanade–Russell $I_1$ (KR1), the general construction remains open: the implementation uses a finite apex lookup table and its advertised round trips hold only over the checked range $0\le N\le40$. A concrete failure at $N=41$ refutes extending the current rules to all weights.

## 1. Tableau conventions, local fibers, and the corrected rotation map

For a poset $P=([n],<_P)$, a tableau has strict $P$-chains along rows and no adjacent column descent. Its graph-inversion weight is

$$\operatorname{inv}_G(T)=\#\{(x,y)\in E(\operatorname{inc}(P)):x<y,\ \operatorname{row}_T(y)<\operatorname{row}_T(x)\}.$$

**Local fiber lemma (machine-checked).** If $a<_P b$ and $\forall z,\ z<_P b\Rightarrow a\not<_P z$, comparable-prefix insertion of $b$ into the singleton tail can be inverted using `extractFirst (r a)`. Hence `bubbleInsert` is injective when restricted to this local fiber, even in posets of arbitrary height. The predicate is sufficient; the lemma does not say every collision-free tableau satisfies it.

For $T=((u,v),(a,b),(c))\in\mathcal T_P(2,2,1)$, write

$$W(T):\Longleftrightarrow a<_P c<_P b\quad\text{and}\quad c\not<_P v.$$

The comparable-prefix slide $B$ has a collision precisely between the witness $T$ and $T'=((u,v),(a,c),(b))$; both map to $((u,v),(a),(c),(b))$.

**Conditional rotation lemma (machine-checked).** If $T$ is valid, $a<_P c$, $v<_P b$, and $c\not<_P v$, then

$$\operatorname{promote32}(T)=((u,v,b),(a,c))$$

is valid and has the same graph-inversion weight. These are the explicit hypotheses of `promote32_tableau_valid` and `promote32_tableau_graph_inversions`; they do not prove the complete routing map below.

**Corrected finite construction.** Define four ordered candidates

$$\begin{aligned}
R_1(T)&=((u,v,b),(a,c)),&R_2(T)&=((a,c,b),(u,v)),\\
R_3(T)&=((u,a,v),(c,b)),&R_4(T)&=((u,c,b),(a,v)).
\end{aligned}$$

Set $A_i(T)$ to mean **both** $R_i(T)\in\mathcal T_P(3,2)$ and $\operatorname{inv}_G(R_i(T))=\operatorname{inv}_G(T)$. Then

$$\Phi_{221}(T)=\begin{cases}
B(T),&\neg W(T),\\
R_{i_*(T)}(T),&W(T),\quad i_*(T)=\min\{i\in\{1,2,3,4\}:A_i(T)\}.
\end{cases}$$

The two output shapes distinguish the disjoint-union sectors. Exact enumeration checks existence of an accepted candidate, validity, equal weight and global injectivity for all 42 Hessenberg vectors at $n=5$. Equal weight of an accepted candidate is enforced by the definition; existence and injectivity are separate finite checks. No Lean theorem for the complete map or an arbitrary-size extension is claimed.

**Counterexample to the previous formula.** At $h=(2,2,4,5,5)$, $T=((1,4),(2,5),(3))$ is valid and has weight 1. The earlier second-branch inequalities select $R_2(T)=((2,3,5),(1,4))$, which has weight 2. The corrected predicate rejects it and selects $R_4(T)=((1,3,5),(2,4))$, of weight 1. The implementation and displayed definition now use the same acceptance rule.

## 2. Hook slides and corrected beta-rearrangement bijection

**General hook-slide argument (written proof).** For any finite poset and $T=((u_1,\ldots,u_k),(c_1),\ldots,(c_r))$, remove an arm entry $u_m$, $2\le m\le k$, and insert it after the longest singleton prefix whose entries satisfy $c_i<_P u_m$. The remaining arm is a strict chain. Inserting after the prefix preserves column non-descent, and the moved entry passes only comparable entries, so graph-inversion weight is unchanged. Lean proves the arm-length-three endpoint and middle cases with arbitrary singleton tails, rather than this entire arbitrary-$k$ statement.

**Beta-rearrangement theorem (written proof).** The determinant-term bijection is algebraic; its application to $X_G$ here assumes a natural unit interval order. Let $\lambda\vdash n$ and pad it by zeros to length $n$. Under the zero-based determinant convention, the row-to-column permutation $\sigma$ defines

$$\beta_{\sigma(i)}=\mu'_i-i+\sigma(i),\qquad 0\le i<n.$$

Nonvanishing determinant terms contributing $e_\lambda$ correspond bijectively to distinct rearrangements $\beta$ of this padded vector with pairwise distinct keys $\kappa_j=\beta_j-j$. Sort these keys decreasingly:

$$\kappa_{\tau(0)}>\cdots>\kappa_{\tau(n-1)}.$$

The correct recovery is

$$\sigma=\tau,\qquad \mu'_i=\kappa_{\tau(i)}+i,\qquad \operatorname{sgn}(\sigma)=(-1)^{\operatorname{inv}(\tau)}.$$

Indeed, the forward construction gives $\kappa_{\sigma(i)}=\mu'_i-i$, a strictly decreasing sequence, so its sorting order is exactly $\sigma$. Conversely, distinct integer keys have successive gaps at least one, and $\kappa_j\ge-(n-1)$, so the recovered $\mu'_i$ are weakly decreasing and nonnegative. Their sum is

$$\sum_i\mu'_i=\sum_j(\beta_j-j)+\sum_i i=\sum_j\beta_j=n.$$

Thus these columns define a unique partition of $n$. With $\sigma=\tau$, the reconstructed exponent is $\mu'_i-i+\tau(i)=\beta_{\tau(i)}$, recovering the original vector. In the other direction, sorting recovers the original permutation and columns. These are mutual inverses, preserving determinant multiplicity and sign. This argument is not yet formalized in Lean; explicit round-trip tests supplement it.

For the review counterexample $n=3$, $\beta=(0,0,3)$, the keys are $(0,-1,1)$ and $\tau=\sigma=(2,0,1)$, with $\mu'=(1,1,1)$. The incorrect inverse permutation $(1,2,0)$ produces exponents $(2,2,-1)$, a vanishing term.

**Finite cancellations.** Combining the routing with hook moves cancels all 323 negative tableaux for $[e_{4,1}]X_G$ at $n=5$, leaving 259 survivors matching the polynomial degree by degree. At $n=6$, exact checks cover:

- $\Phi_{2211}$: 2,592 source tableaux, 330 routed to shape $(3,2,1)$.
- `six_sector_e33_injection`: 801 negative tableaux cancelled and 207 survivors.
- `eight_sector_e51_injection`: 3,980 negative tableaux cancelled and 2,820 survivors.

The $n=6$ algorithm processes tableaux in the implementation's fixed enumeration order, selecting a valid equal-weight candidate not already used in the target sector. The conditional Lean rotation `promote321` is only one candidate: validity requires $a<_P c_2$, $v<_P b$, $c_2\not<_P v$; its weight theorem additionally requires $c_1<_P c_2$. Complete algorithmic coverage and injectivity here are finite Python checks, not consequences of that one Lean lemma.

## 3. Universal signed-array cascade

The Lean theorem `cascade_split_preserves_all` states the specified local toggle

$$((p,[]),(q,b::as))\longleftrightarrow((q,as),(p,[b]))$$

proves equivalences of the bundled shape and goodness predicates, and equality of graph-inversion weight. Row-chain validity follows separately from unchanged entries and pairwise chains under its stated hypotheses, with nonempty `as` and a strict chain `b::as`. This local result does not itself supply a global sign-reversing involution for arbitrary height.

The cascade gives equivalences of signed-array predicates, not a construction of a globally good tableau; both local configurations fail the full `Good` predicate.

## 4. KR1 coordinate identities, finite rules, and a failed extension

For $Q(a,b)=a^2+3ab+3b^2$, the Lean certificate proves arithmetic identities including

$$Q(3c+r,b)=r^2+3r(b+2c)+3Q(b,c),\qquad Q(3c,b)=3Q(b,c).$$

For $(a,b)=(3,0)$, write $d_3=\mu_0$, $d_2=\mu_1-\mu_0=3q_2+r_2$, $r_2\in\{0,1,2\}$, and $d_1=\mu_2-\mu_1$. Then

$$\operatorname{wt}(C)=(9+2r_2)+6q_2+3d_3+d_1.$$

This is an octant parameterization of **cluster coordinates**, and a weight identity. Equal weight does not establish membership, image disjointness or an inverse on the target column partitions.

**Cone conjecture.** In column-weight multiplicities $(10^z,9^y,8^x,6^{c_6},3^{c_3},1^{c_1})$, the proposed family with $y\in\{1,2\}$, $x+z\ge1$, $0\le z\le3$, and $c_6+c_3+c_1\ge1$ if $x=0$, is conjectured valid in $\mathcal U$ and disjoint from the lower-sector image. The suite checks 3,744 finite states. A complete all-parameter proof of terminal conditions and exclusion from the full lower-sector image remains required.

**Finite KR1 correspondence.** The implemented operators `step_six`, `step_three`, `step_one` and their proposed inverses reduce 3,709 higher-sector states through weight 40 to 85 cluster-coordinate apexes (three special-sector apexes and 82 explicit table assignments). Together with lower sectors, the checked round-trip correspondence covers 5,461 states for $0\le N\le40$. The `OCTANT_APEX_PAIRS` constant is an explicit finite table assigning apexes: the construction is not lookup-free. The special $(a=3,b=0)$ rules pass an additional check through $N=60$ (4,491 states), which is still finite evidence.

**Refuted all-weight extension of the current rules.** At $N=41$, a cluster with a known apex already fails round-trip recovery:

$$C=(5,0,(0,1,2,6,7),())\ \longmapsto\ U=(19,12,6,3,1),$$

but `decompose_full(U)` returns $(2,2,(5,5),(0,1))$. The higher-sector map overlaps the lower-sector image. Thus extending these current rules to all weights is false, rather than merely unverified. The valid finite results and weight identities remain useful.

## 5. Assurance levels and next research targets

| Claim | Assurance and boundary |
| --- | --- |
| Local fiber lemma, conditional rotations, specified cascade, KR1 arithmetic identities | Supplementary Lean statements under explicit hypotheses |
| General hook-slide argument; corrected beta-rearrangement theorem | Written mathematical arguments; beta round-trip computation additionally checks finite cases |
| Complete tableau routing and selected DJT cancellation | Exact finite enumeration at $n=5,6$ |
| KR1 full round trips | Exact finite enumeration only for $0\le N\le40$ |
| Cone family and unrestricted KR1 sector construction | General cone statement remains conjectural; current full-map all-weight extension is refuted at $N=41$ |

Promising next steps are to classify image signatures so higher-sector operators cannot enter the lower-sector image, construct an explicit inverse for the tableau routing, and prove candidate coverage under the natural unit interval assumptions. A general apex rule must replace or justify the finite table. These are research goals, not established conclusions.

## 6. Supplementary Lean 4 Formal Verification Index

Lean was unavailable locally. GitHub CI subsequently rebuilt the unchanged Lean 4.34.0 certificate (73 theorem reports); the fresh source-bound record is [lean_std_ci_2026-10-26.json](../evidence/lean_std_ci_2026-10-26.json).

The existing verification record reports 19 theorems in [`research/partitions/lean/MultidimensionalFerrers.lean`](../lean/MultidimensionalFerrers.lean) verified with Lean 4.34.0 (`Std` only, zero external dependencies, zero `sorry`, standard axioms `{propext, Quot.sound, Classical.choice}` recorded in [`research/partitions/lean/verification.json`](../lean/verification.json)):

| Lean 4 Theorem | Statement Summary |
| :--- | :--- |
| `MultidimensionalFerrers.bubble_injective_local_fiber` | Non-3-chain local fiber injectivity of `bubbleInsert` in posets of arbitrary height. |
| `MultidimensionalFerrers.promote32_tableau_valid` | 3D rotation `((u,v),(a,b),(c)) ↦ ((u,v,b),(a,c))` preserves `Tableau` validity under its explicit hypotheses. |
| `MultidimensionalFerrers.promote32_tableau_graph_inversions` | 3D rotation `promote32` preserves `tableauGraphInversions` under its explicit hypotheses. |
| `MultidimensionalFerrers.collision_witness_promoted_valid` | Resolves the height-3 collision witness `[[1,2],[3,5],[4]] ↦ [[1,2,5],[3,4]]`. |
| `MultidimensionalFerrers.promote321_tableau_valid` | $n=6$ 3D rotation `((u,v),(a,b),(c1),(c2)) ↦ ((u,v,b),(a,c2),(c1))` preserves `Tableau` validity under its explicit hypotheses. |
| `MultidimensionalFerrers.promote321_tableau_graph_inversions` | $n=6$ 3D rotation `promote321` preserves `tableauGraphInversions` under its explicit hypotheses. |
| `MultidimensionalFerrers.hookBubbleEnd_tableau_valid` | Endpoint hook slide `(3,1^r) → (2,1^{r+1})` preserves `Tableau` validity under its explicit hypotheses. |
| `MultidimensionalFerrers.hookBubbleEnd_tableau_graph_inversions` | Endpoint hook slide preserves `tableauGraphInversions` under its explicit hypotheses. |
| `MultidimensionalFerrers.hookBubbleMid_tableau_valid` | Interior hook slide (`m = 2`) `(3,1^r) → (2,1^{r+1})` preserves `Tableau` validity under its explicit hypotheses. |
| `MultidimensionalFerrers.hookBubbleMid_tableau_graph_inversions` | Interior hook slide preserves `tableauGraphInversions` under its explicit hypotheses. |
| `MultidimensionalFerrers.cascade_split_preserves_all` | Universal $k$-D first-column cascade `(0, k) ↔ (k-1, 1)` in `SignedArrays`. |
| `MultidimensionalFerrers.kr1_scale3_self_similarity` | $Q(3c+r, b) = r^2 + 3r(b+2c) + 3\,Q(b, c)$. |
| `MultidimensionalFerrers.kr1_scale3_divisible` | $Q(3c, b) = 3\,Q(b, c)$. |
| `MultidimensionalFerrers.kr1_head_offset_identity` | $Q(a, b) = 3b(b+1) + a^2 + 3(a-1)b$ for $a \ge 1$. |
| `MultidimensionalFerrers.kr1_a3_core_weight` | $3(b+2) + 3(b+1) + 3b(b+1) = Q(3, b)$. |
| `MultidimensionalFerrers.kr1_a3_b0_octant_weight` | $(9 + 2r_2) + 6q_2 + 3d_3 + d_1 = Q(3, 0) + 3d_3 + 2(3q_2 + r_2) + d_1$. |
| `MultidimensionalFerrers.kr1_a3_b0_6d_cone_routing_weight` | $10 + 9 + 9 + 8 + 6(q_2-4) + 3(d_3-1) + d_1 = Q(3, 0) + 3d_3 + 6q_2 + d_1$ for $q_2\ge4,d_3\ge1$. |
| `MultidimensionalFerrers.kr1_higher_octant_weight` | $(W_{\mathrm{base}} + 2r_2) + 6q_2 + 3d_3 + d_1 = W_{\mathrm{base}} + 3d_3 + 2(3q_2 + r_2) + d_1$. |
| `MultidimensionalFerrers.kr1_a4_a5_a6_apex_weights` | Apex weights $(8,8) \mapsto Q(4,0)$, $(15,9,1) \mapsto Q(5,0)$, $(18,10,8) \mapsto Q(6,0) = 3Q(0,2)$. |

---


## 7. Revision and artifact provenance

A public correction notice accompanies this edition: [ERRATA_2026-10-26.md](ERRATA_2026-10-26.md).

Christopher Yamba's original geometric proposal motivated this investigation; novelty of the constructions has not been established by a systematic prior-work audit. Revision 2 corrects the rotation selection and determinant permutation recovery while preserving valid local lemmas and finite results. The original timestamp records provenance, not a claim that these corrections or checks existed then.

Current hashes and revision metadata are in [`AUTHORSHIP_TIMESTAMP_ATTESTATION.json`](AUTHORSHIP_TIMESTAMP_ATTESTATION.json). Embedded hash copies are omitted to prevent stale or circular attestations. Publication remains subject to review of these corrected claims.
