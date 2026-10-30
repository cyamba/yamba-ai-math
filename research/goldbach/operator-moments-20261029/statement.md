# Audit of the auxiliary moment and reflected root replacement

29 October 2026. Registry role: Mathematician, `GOLDBACH-MOMENTS-010`, author stage. This is an independent reconstruction of the finite operator argument and its reflected arithmetic replacement, pending distinct hostile review and exact checks. The two candidate conclusions below concern explicitly defined auxiliary operators. They do not assume H2', validate the full source theorem, estimate the prime major part, or establish Goldbach. Novelty is unverified.

Primary reference: [Lue-Wang-Wu v1, sections 4.2-4.5](https://arxiv.org/html/2610.20242v1). The pinned Guo source already gives conditional transport and enlarged-state/ambient-Gram framing; that conditional assertion is not a dependency. The elementary root-count dependency is the separately reviewed ROOTS-008 result in its actual aspect range. TRACE-009 supplies the finite ambient-Gram identity, not an arithmetic moment estimate.

## Parameters, eligibility and exact normalization

Put L=log x. Fix K, rho in (0,1), and distinct exponents `0.1<a1<...<aK<0.2`, all before taking x to infinity. Write

\[
 m=J+1,\quad J=\lfloor L^{0.01}\rfloor,\quad
 R=\lceil\sqrt L/2\rceil,\quad N_{\rm mem}=\lceil L^2\rceil.
\]

The original band i is `exp(L^{a_i})<p<=exp(2L^{a_i})`. For a reflected target H comparable to x, let Pi_i contain the primes in that band not dividing H and set `V_i=sum_{p in Pi_i}1/p`. If V_i^0 denotes the full-band mass, then

\[
 0\le V_i^0-V_i\le
   \frac{\log H}{\exp(L^{a_i})L^{a_i}}. \tag{1}
\]

Indeed each omitted prime uses at least `L^{a_i}` of the logarithmic divisor budget log H and contributes at most `exp(-L^{a_i})`. Mertens' prime harmonic estimate gives `V_i^0=log 2+o(1)`. Thus the eligible masses converge uniformly to log 2 and lie in a fixed compact subinterval of (0,1) eventually. Bounds using the number of band primes only improve upon deletion. The proofs below use just these mass bounds, band sizes, disjointness and the explicitly defined good tests, so they allow these H-dependent subsets.

Let `c_V=prod_i(V_i^0/V_i)=1+O_K(L^{0.9}exp(-L^{0.1}))`. On unit endpoint states the index set already excludes band primes dividing H. If the same good projection is used, changing old to eligible normalizers multiplies the state weight by `c_V^m` and the one-edge operator by c_V. Hence its order-2R endpoint moment is multiplied by exactly `c_V^{m+2R}=1+o(1)`, not by an uncontrolled additive error. This comparison does not identify differently defined good projections. The construction below defines and keeps its eligible good tests throughout; eventual removal of them is a separate obligation.

Take a nonempty selected-product block Y and shared-product block d0, with `log Y` between a positive multiple of `L^{0.1}` and `O_K(L^{0.2})`, and `log(d0Y)=O_K(L^{0.21})`. Integer position rectangles and canonical-ratio partitions use a consistent half-open convention. Fix a smooth product cutoff eta supported in [1,4], a fixed smooth compactly supported psi, and

\[
 \mathfrak M=\bigcup_{q\le L^{A_0},\ (a,q)=1}
 \{\theta:\|\theta-a/q\|\le2L^{A_0}/Y\}.
\]

Constants attached to these fixed cutoffs are retained in the implied constants. A request for precision chooses A0 and then K; neither grows with x.

## Finite independent-line and memory models

Fix a real root `(u,v,t)` in `[U,16U] times [V,2V] times [0,1]`, where eventually `U=d0YM`, `V=N`, `MN` is comparable to x and H is comparable to x. Put

\[
 G_H(u,v,t)=\begin{pmatrix}u&ut\\v&vt+H/u\end{pmatrix},\qquad
 \tau(z)=z_1+tz_2.
\]

Use primitive integer z in a finite box of height `C R d0Y` and the strip `U/u<=tau(z)<=16U/u`; choose fixed C large enough for all actual paths. Let chi(z) be the original-box position indicator `G_H z in Omega`. Additional retained position-only projections can be included in chi. They are kept, not deleted from a signed path expansion. Every retained position has positive tau, and tau-ratios lie in [1/16,16]. For any integral complement w_z with `det(z,w_z)=1`, define

\[
 \beta_z=\tau(w_z)/\tau(z)\pmod1.
\]

It does not depend on the complement. For each eligible prime p independently choose a uniform line ell_p in `P^1(F_p)`. Active lists are ordered distinct m-tuples in each group. In the physical line model they obey `ell_p=[z]_p` for every active entry, and have state measure `prod_i V_i^{-m}`. The endpoint vector is one at z=e1 on all admissible lists and zero elsewhere. List symmetrization S averages the m! permutations in each group; it is an orthogonal projection.

A complete list at z is good if both following tests hold. First, for every D in [d0,2d0) obtained by omitting one entry per group,

\[
 \|hD\beta_z\|>Y^{-0.7}\quad(1\le h\le Y^{0.2}). \tag{2}
\]

Second, for every nonempty group set I, with i*=max I, let Z range over products of one eligible prime from each group in `I minus {i*}`, and D over all such omissions. For `T_f=prod_{i notin I}p_i`, with weight `prod_{i notin I}(p_i V_i)^{-1}`, require, outside choices of total weight at most `exp(-L^{a_i*}/4)`,

\[
 \|(DZ-D'Z')T_f\beta_z\|
       \ge100\exp(-L^{a_{i*}})\quad(DZ\ne D'Z'). \tag{3}
\]

These tests are list-permutation invariant. Their bad-ratio measure is `O_K(exp(-cL^{0.1}))`: (2) costs at most `2m^K Y^{-1/2}`; for (3), the number of DZ values is `exp(o(L^{a_i*}))`, because all Z groups have smaller fixed exponents than a_i*. Each unequal difference times T_f is a nonzero integer and preserves Haar measure. A union bound followed by Markov at the displayed threshold proves the claim. These arguments remain uniform for eligible subsets and their bounded positive masses.

For an edge, retain J shared entries in each group, omit their old unshared product b, and select a new unshared product a with no prime from the old complete lists. Put `D=product(shared entries)` and retain `d0<=D<2d0` and `D|det(z,z')`. The geometric centered kernel, without its damping, is

\[
 k(z,z';D,a,b)=\frac{d_0}{D}\eta(a/Y)\eta(b/Y)
 \psi\!\left(\frac{\det(z,z')}{DY}\right)
 \left\{\mathbf1_{\det(z,z')/D=b-a}
 -\int_{\mathfrak M}e(\theta(\det(z,z')/D-b+a))\,d\theta\right\}. \tag{4}
\]

Operationally the physical edge sums each new unshared prime in group i with weight 1/V_i and sums target positions with counting measure, retaining the shared ordered prefix. It also has damping `rho^{(omega_ell(z)+omega_ell(z')-2Km)/2}`, goodness, position projections and S at both ends. The state weight `prod_i V_i^{-m}` is used for its Hilbert inner product; it is not applied a second time to these operational sums. Alternate edges use its weighted adjoint. Let M_R(u,v,t) be its order-2R endpoint moment averaged over the independent ell_p. This definition uses all-ones endpoint list fibers, not trace closure of an individual basis list state.

For j=0,...,2R set `q0=q_(2R)=sqrt(rho)`, interior `qj=rho`, `eps_j=1-qj`, and

\[
 b'_p=1-\frac{\sum_j\epsilon_j}{p+1},\qquad
 \nu_i(p)=\frac1{V_i(p+1)b'_p},\quad
 s_i=\sum_{p\in\Pi_i}\nu_i(p),\quad
 \Delta=\max_{i,p}\nu_i(p). \tag{5}
\]

For large x, b'_p>0, `p V_i nu_i(p)=1+O(R/p)`, `s_i=1+O_K(R/p_min)` and `Delta<<_K exp(-L^{0.1})`. The product of b'_p lies in (0,1].

The auxiliary space has counting measure on z, active-list measure `prod_i nu_i^{tensor m}`, and, for each group, a symmetric ordered memory tuple of k_i pairs `(p,ell)` with measure `lambda_i^{tensor k_i}/k_i!`, where `lambda_i(p,ell)=nu_i(p)`. Auxiliary active lists range over all ordered m-tuples, allowing repetitions, as does the underlying memory alphabet. Kernels enforce distinct complete active lists and the cross-edge exclusion just stated. The memory cap is `sum_i k_i<=N_mem` at both arguments. Equivalently a memory occupation vector n_a has measure `prod_a nu(a)^{n_a}/n_a!`; this equivalent form will make the adjoints explicit.

The full alphabet mass is `sum_p(p+1)nu_i(p)`, which can be very large. It is **not** s_i. Only the compatible slice `{(p,[z]_p)}` at a fixed z has mass s_i. All exponential factors below use that slice; incompatible memory coordinates are retained unchanged.

Choose theta in (0,1) with `theta^2>sqrt(rho)`. The following are operational definitions, with the stated sums part of the operator rather than a second application of its state measure.

* G_j fixes z and the active lists. In each group remove any subset of compatible existing memory coordinates, where compatibility means `ell=[z]_p`. If d are removed and h compatible coordinates remain, its factor is `(-eps_j/theta)^d (qj/theta^2)^h`. Append an ordered l-tuple of `(p,[z]_p)` with factor `(1/l!)*prod(-eps_j V_i nu_i(p)/theta)`. Sum all choices. Indices distinguish repeated existing coordinates.
* E_j retains (4), all endpoint projections/S/good tests, the shared D restrictions and the complete-list/cross-edge exclusions. Choose a subset S0 of departing groups to store their old unshared entry as `(p,[z]_p)`; discard the other departing entries. For a group in I, fill the new unshared slot by removing a compatible memory coordinate present **before** this edge, with factor 1/V_i. For a group outside I select a fresh prime with measure nu_i. A coordinate appended on this edge cannot also fill a slot on this edge. Multiply by `theta^{h_s+h_t}`, where h_s counts compatible memory coordinates before the edge at z and h_t counts compatible memory coordinates after it at z'. Sum these choices. On alternating edges transpose/conjugate the geometric kernel and retain these same memory rules.

The global distinctness restriction, imposed on the final expansion rather than the individual operator spaces, concerns all prime **introduction variables**: initial active entries, fresh E selections, and G appends. Transferring an already stored coordinate introduces no new prime variable. Let b be one at `z=e1` and empty memory, independently of active lists. Then `||b||^2=prod_i s_i^m=1+o(1)`.

## Candidate 1: model moment bound

**Author proof, pending independent review.** For each fixed E0>0 one can choose A0 and then sufficiently large fixed K so that, uniformly in the above real root and retained position projections,

\[
 |M_R(u,v,t)|\ll L^{-2R(E_0+4)}. \tag{6}
\]

The proof below supplies the needed signed bounds. It does not assume smallness of a norm after arbitrary choice restrictions.

### G_j and the coarse edge estimate

Choose fixed v0>1 with `sqrt(rho)/theta^2+1/(theta v0)<1`, and use Schur weight `w=v0^{sum k_i}`. In one compatible memory type of occupation n, the G_j row sum is a binomial removal sum and an exponential append sum. In group i it is at most

\[
 \exp(v_0\epsilon_j V_i s_i/\theta)
 \left(q_j/\theta^2+\epsilon_j/(\theta v_0)\right)^{h_i}. \tag{7}
\]

For the adjoint it is at most

\[
 \exp(v_0\epsilon_j s_i/\theta)
 \left(q_j/\theta^2+\epsilon_j V_i/(\theta v_0)\right)^{h_i}. \tag{8}
\]

To verify the adjoint, multiply a transition from n to n-d+l by the ratio `(nu^n/n!)/(nu^{n-d+l}/(n-d+l)!)`. The result reverses removal and append, interchanging the factors V_i in precisely (7)-(8). Thus neither factorials nor repeated coordinates are omitted. Both parentheses are at most one. Incompatible coordinates are unchanged. Taking products proves two-sided weighted Schur bounds `||G_j||<=C_(K,rho)`; the memory cap only reduces their absolute sums.

For E_j, fix z and choose an integral w_z with determinant one. A target of determinant j1 is uniquely `z'=j1*w_z+h*z`, and the tau-ratio strip leaves O(1) h for each j1. The raw determinant is fixed. In the comparison term there are O(Y) possible j1/D, and `|M|<<L^{3A0}/Y`. Memory transfers cost at most `N_mem^K` coordinate choices; remaining prime measure sums and V_i factors are bounded. Reversing the operation uses the same factorial identities and gives the same bound for the adjoint. Consequently for a fixed C*=C*(K,A0,rho),

\[
 R_w(E_j),C_w(E_j),\|E_j\|\le L^{C_*}. \tag{9}
\]

It also holds after arbitrary choice multipliers of modulus at most one **that preserve symmetry in existing memory coordinates**. This is an absolute estimate and does not retain the signed small bound below under those modifications.

### Clean edges: signed Fourier bound with endpoint multipliers

A clean edge has no active/memory transfers. Partition positions into slope cells of length d0Y for `z2/tau(z)`, with only O(1) neighboring interactions. Fix shared lists and their common projective lines and the unchanged memory. A good primitive z* in the block gives the lattice

\[
 \Lambda_D=\{h z_*+lD w_*:h,l\in\mathbb Z\},\quad
 \alpha=D\beta_{z_*},\quad |l|\ll Y,\quad h+l\alpha\asymp1.
\]

Its scaled lattice `(l/Y,h+l alpha)` has covolume 1/Y. A vector shorter than Y^{-0.8} would have `0<|l|<Y^{0.2}` and `||l alpha||<Y^{-0.7}`, contradicting (2). A shortest-vector basis therefore has parameters A',B' with `A'B'` comparable to Y and both between `Y^{0.1}` and `Y^{0.9}`. Completing the shortest vector and reducing the other along it proves these box bounds directly. The resulting integral basis matrix B_D has determinant D, so the reduced determinant is `det(k,l)`.

For an unshared product a, `m(a)=prod_i nu_i(p_i)<<_K 1/Y` on eta(a/Y). Conversion of this measure to counting measure gives bounded endpoint factors `eta(a/Y)sqrt(Ym(a))`. Extend by zero to the product box times all integer a. The remaining signed kernel is

\[
 \frac1Y\psi(\det(k,l)/Y)
          \int_{\mathbb T\setminus\mathfrak M}
                   e(\theta(\det(k,l)-b+a))\,d\theta. \tag{10}
\]

Goodness, complete-list restrictions, primitivity, chi and compatible-memory theta factors are bounded endpoint multipliers. They can remain on either side of (10). This is a proved norm compression, not pointwise removal from a signed sum.

Fourier transformation in a reduces (10) to determinant matrices at frequencies outside M. Fourier inversion of psi reduces them to `xi=theta+v/Y`. For `|v|<=L^{A0}/2`, Dirichlet approximation at denominator cutoff `ceil(Y/L^{A0})` supplies coprime c,d with

\[
 L^{A_0}<d\le\lceil Y/L^{A_0}\rceil,\qquad |\xi-c/d|\le d^{-2}.
\]

A smaller denominator would put theta in M by its displayed width. The rectangular exponential matrix T=(e(xi hk)) has Gram row-sum bound

\[
 \|T\|^2\ll(A'/d+1)(B'+d\log(2d)).
\]

In blocks of at most d/2 consecutive differences, the approximated residues are separated by at least 1/(2d), which proves this harmonic sum bound including the zero difference. After a column permutation the determinant matrix is T tensor its conjugate transpose. Dividing its norm by Y therefore gives

\[
 \ll 1/d+Y^{-0.1}\log(2Y)+d\log(2d)/Y
 \ll_K L^{0.2-A_0}+Y^{-0.1}\log Y. \tag{11}
\]

The discarded v range is bounded by the rapid Fourier decay of psi and the trivial O(Y) matrix norm. A collision between old and new unshared primes, temporarily allowed in (10), costs at most Delta in both Schur directions: condition on that one equality and use the determinant target count of (9). Its correction is `O_K((1+L^{3A0})Delta)`. Summing the bounded neighboring cells and list averages proves the clean bound (11), uniformly in memory and chi.

### Dirty raw edges: both directions of Schur

Fix the departing-storage set S0 and receiving-memory set I. If I is nonempty choose i*=max I and one pre-existing receiving coordinate `(p*,ell*)` in that group; there are at most N_mem choices. Put `P_full=Db` and `a=p* Z T_f`. Cross-edge exclusion makes p* coprime to the entire old list. In the raw part,

\[
 j_1=P_{\rm full}-Dp_*ZT_f\not\equiv0\pmod {p_*}.
\]

The target line at p* determines `h=h* mod p*` in `z'=j1*w_z+h*z`; h* depends on P_full,p*,ell*,z, not the omitted D or Z. The tau strip gives

\[
 \left\|DZT_f\beta_z-
       (P_{\rm full}\beta_z+h_*)/p_*\right\|\le16/p_*.
\]

The nu-product for fresh T_f choices is uniformly comparable to its reciprocal-prime weight. Except for mass `O_K(exp(-cL^{0.1}))`, (3) separates different DZ by more than the diameter 32/p*. Thus at most one DZ is possible. Its factorization recovers D and Z separately: all Z primes taken from memory are excluded from the old complete lists. The old list average therefore permits at most one omission tuple, of mass m^{-K}. For this tuple, the determinant leaves O(1) targets. Once the target is fixed, repeated compatible memory entries cost only a constant per selected group, since `h theta^{h-1}` is bounded. Exceptional T_f choices use the crude N_mem^K bound. The resulting receiving-direction bound is

\[
 \epsilon_K=C_{K,\rho}
       (N_{\rm mem}m^{-K}+N_{\rm mem}^{K}e^{-cL^{0.1}}). \tag{12}
\]

When I is empty the row bound is O_(K,rho)(1). In the adjoint, S0 and I exchange their roles. The occupation-measure ratio transfers the same V_i factors in the reverse direction, which stay bounded. Thus fixed dirty parts have row/column bounds `(epsilon_K,O(1))`, `(O(1),epsilon_K)`, or `(epsilon_K,epsilon_K)`. Weighted Schur gives

\[
 \|E_j^{\rm dirty,raw}\|\ll\sqrt{\epsilon_K}
 \ll L^{1-0.005K}+O_A(L^{-A}). \tag{13}
\]

The small scalar exceptional mass alone is not used as an operator norm; it enters this explicitly uniform two-sided count.

### Dirty comparison and the uniform edge norm

A received memory coordinate fixes one line modulo p* with p* not dividing D. In the adapted lattice box above this is a nonzero linear congruence. Counting one variable after fixing the other gives

\[
 \#\{(h,l):a_0h+b_0l=0\pmod {p_*}\}
 \ll A'B'/p_*+\max(A',B')
 \ll Y(p_*^{-1}+Y^{-0.1}).
\]

Multiply by `|M|<<L^{3A0}/Y` and the N_mem^K transfer choices. In one direction this bounds the row by a polynomial in L times `p_min^{-1}+Y^{-0.1}`. The other direction has (9). When only S0 is nonempty, reverse the edge. Hence

\[
 \|E_j^{\rm dirty,comp}\|
 \le L^{C_\dagger}(p_{\min}^{-1}+Y^{-0.1})^{1/2}
       =O_A(L^{-A}) \tag{14}
\]

for every fixed A, with C_dagger fixed after K,A0. Combining (11),(13),(14), choose `A0>G+3` and `K>200(G+3)`. For sufficiently large x,

\[
 \|E_j\|\le L^{-G},\qquad\|G_j\|\le C_{K,\rho}. \tag{15}
\]

The hypotheses used for (15) are precisely the retained shared/cross-list restrictions, good tests, symmetric memory space and endpoint projections above. No extension to arbitrary signed choice restrictions is asserted.

### Local prime identity and the memory tail

For a physical path let A_p be the indices where p is active. Its exact independent-line average is

\[
 \frac1{p+1}\sum_\ell
 \prod_{j\in A_p}\mathbf1_{\ell=[z_j]_p}
 \prod_{j\notin A_p}(1-\epsilon_j\mathbf1_{\ell=[z_j]_p}). \tag{16}
\]

Here is a termwise construction of the memory expansion. If A_p is empty, either no p is introduced, giving b'_p, or a single ghost is appended at a and removed at c>a. Its contribution divided by b'_p is

\[
 \frac{\epsilon_a\epsilon_c}{(p+1)b'_p}
 \mathbf1_{[z_a]_p=[z_c]_p}
 \prod_{a<j<c}(1-\epsilon_j\mathbf1_{[z_j]_p=[z_a]_p}).
\]

Their sum is (16)/b'_p, by expansion grouped by the first and last selected deficit. If A_p is nonempty, it must use one common line. Each maximal consecutive active interval gives one factor 1/V_i; each gap is a required storage and later recovery of the existing p. The prefix before the first interval is either fresh introduction or a ghost append at h before it. Its branches sum by `prod(1-x_j)=1-sum_h x_h prod_{h<j}(1-x_j)`; the suffix has the reverse identity. Thus p is introduced exactly once, with coefficient `1/((p+1)b'_p)` and the required interval normalizers.

Along an inactive retained coordinate the two edge theta factors cancel the G factor to q_j. A G append contributes `-epsilon_j V_i` after cancellation; its removal contributes `-epsilon_j`. These give exactly the prefix, suffix and ghost weights just listed. The l! orders of distinct G introductions cancel the 1/l! append weight. Transfers do not create a new introduction. Multiplying these per-prime correspondences proves the untruncated signed identity

\[
 M_R=\left(\prod_p b'_p\right)
       \langle b,G_0E_0G_1\cdots E_{2R-1}G_{2R}b\rangle_{\rm distinct}.
                                                               \tag{17}
\]

For the memory tail, E appends at most 2KR coordinates over a whole path. Exceeding N_mem requires at least `N_mem-2KR` G introductions. Mark each such introduction by an extra factor 2. For a ghost absent from active lists, summing its two lifetime endpoints telescopes in the later endpoint and costs at most `C_rho R/p`. Hence all ghost choices cost at most `prod_p(1+C_rho R/p)<=exp(C_(K,rho)R)`. There are O_K(J+R) active primes, each with at most O(R^2) lifetime endpoint choices. Physical path/list absolute mass is at most `exp(O_K(L^{0.73}))`, as counted below. Removing the extra marks bounds the cut error by

\[
 2^{-N_{\rm mem}+2KR}
 \exp(O_{K,\rho}(L^{0.73}+(J+R)\log(2R)+R))
        \ll_A L^{-2AR}. \tag{18}
\]

This argument applies to the globally distinct expansion, where each introduction has a different prime. It is not an assertion that unrestricted repeated ghosts have a product bound of this form.

### Distinctness: high rank uses atoms, low rank keeps signed norms

After the cap, reserve a finite ordered introduction-index set B for the initial Km entries, each possible fresh E slot, and the first N_mem append slots of every G/group. Its size is polynomial in L. Let B_act be its actually used indices. The exact inclusion-exclusion identity is

\[
 \mathbf1_{\text{all introduction primes distinct}}
 =\sum_{\mathcal C}\prod_{C\in\mathcal C}
      (-1)^{|C|-1}(|C|-1)!\,\mathbf1_{C\subset B_{act},\ p_a\text{ equal on }C},
                                                               \tag{19}
\]

over disjoint clusters of size at least two. It follows by summing cycle signs within each equal-prime class. Rank r is `sum_C(|C|-1)`, involves at most 2r indices, and the sum of absolute cluster weights at rank r is at most `|B|^{2r}`: a canonical ordered decomposition into r transpositions determines each permutation.

A fresh E prime prescribed to a previously known value has row bound at most `Delta L^{C*}`. Prescribing s coordinates of a G append tuple costs at most `(C_K Delta)^s`, uniformly in old data: its factorial exponential series is bounded by `sum_{l>=s}C^l Delta^s s_i^{l-s}/l!`. Initial prime atoms have the same Delta bound. Iterating (9) gives the rank-r contribution at most `L^{C*(2R+1)}(C_K Delta)^r` before cluster counting. Put

\[
 r_0=\left\lceil C_0\frac{2R\log L}{L^{0.1}}\right\rceil,
 \quad C_0>2(C_*+E_0+7).
\]

Since `C_K |B|^2 Delta<=exp(-L^{0.1}/2)`, the sum of ranks r>=r0 is `O(L^{-2R(E0+4)})`.

For r<r0, impose each equality cluster by circle orthogonality and attach its phases to the introduction events, including zero when a reserved append index is not used. Each phase has modulus one. For a G append tuple replace the phase multiplier by its average over permutations of that new tuple: all subsequent operators are symmetric in existing memory coordinates, so this changes neither the summed matrix element nor its membership indicators. The modified G has its same absolute Schur bound. Modified E factors need only (9). At most 2r E factors are modified; all others keep (15). Initial phases do not increase ||b||. Thus the rank-r signed term is at most

\[
 C_{K,\rho}^{2R+1}\|b\|^2
       L^{-G(2R-2r)+2C_*r}.
\]

Summing `|B|^{2r}` up to r0 costs `L^{o(R)}` because r0/R tends to zero. Taking `G=E0+5` gives `L^{-2RG+o(R)}<<L^{-2R(E0+4)}`. Together with the high ranks, (18), and `prod b'_p<=1`, this proves (6). The phase insertion uses coarse bounds where necessary, rather than assuming the signed norm survives an arbitrary equality restriction.

## Candidate 2: reflected arithmetic replacement

**Author proof, pending independent review.** In the symmetric Type-II setup below, the normalized ambient selected-root moment is the ROOTS-008 density times the independent-line integral, up to `O_A(L^{-2AR})`. Combining it with Candidate 1 gives the corresponding small ambient selected-root moment, with the actual eligible normalizers.

At the bilinear input, both coefficients have the same sifted support and fixed polynomial-log bound, with `M,N>=x^delta`, `MN` comparable to x. The summand depends on m,n through their product, apart from the separate coefficient factors. Exchanging m,n and their coefficient arrays preserves these assumptions, conjugations and selected-product cutoffs. We therefore orient M<=N **at this input**. This is not a claim of symmetry for arbitrary later auxiliary formulas. With `U=d0YM,V=N`, `d0Y=x^{o(1)}`, the finite error of ROOTS-008 divided by UV is at most `x^{-delta/4+o(1)}` after choosing its arbitrary eta small. In particular the needed aspect restriction holds. Fix a smaller positive c_delta, for example delta/8, for all subsequent counts.

Let B be the direct-sum ambient coefficient-one operator on primitive image states, with the eligible groups, original-box chi and intrinsic good tests just defined. For each primitive both-unit original root P in Omega let u_P be its all-ones list fiber in its unique unit sector. Define

\[
 D_{\rm unit}=\sum_{P\in\Omega,\ (P_1,P_2)=1,\ (P_1P_2,H)=1}
                 \langle u_P,(BB^*)^R u_P\rangle.
\]

This uses the ambient power before endpoint restriction. Intermediate original preimages are not required to be units. Only the selected root has those filters. Thus no root-dependent unit projection has been inserted at every step.

Expand this **physical** order-2R moment into relative positions, active lists and list permutations before introducing any Fock memory. Every intermediate image state is primitive. The root determinant-H basis is unimodular in the sector lattice, so relative z are integral primitive and all active eligible-prime conditions are prescribed lines in the first row of the canonical root matrix. The ROOTS-008 unit-root theorem applies because all eligible primes are coprime to H. The original root population has local density kappa_b(H), not the enlarged 1/zeta(2).

For these physical paths, coordinate height is at most `C R d0Y`, by TRACE-009 geometry and H comparable to MN. Hence the logarithm of the number of position paths is `O(R log(Rd0Y))`. Naively choosing every active list at each of 2R+1 positions and all permutations costs logarithm at most

\[
 O_K(Rm L^{0.2}+Rm\log m).
\]

All fixed cutoff factors, d0/D, normalizers and centered bracket choices cost at most `exp(O_K(R+m))` in absolute coefficients. Thus total pre-damping physical coefficient mass is `exp(O_K(L^{0.73}))`. This bound is deliberately coarse and allows repeated physical primes.

For primes not present in any active list, their path damping lies in [0,1]. Its deficit has independent-line mean at most `(2R+1)/(p+1)`. Truncate the product between consecutive Bonferroni bounds of degrees `B0-1,B0`, where `B0=ceil(L^{0.76})`. The mean difference is at most

\[
 \frac{(C_K(2R+1))^{B_0}}{B_0!}
     \le\exp(-cL^{0.76}\log L), \tag{20}
\]

which absorbs the pre-damping `exp(O_K(L^{0.73}))` mass. Active-prime factors are kept exactly. Each unused-prime deficit is supported on at most 2R+1 projective lines. Enumerating all B0 selected primes and these line values has total raw coefficient/choice mass at most `exp(O_K(L^{0.96}))`, not the smaller pre-damping mass. Every retained prescribed modulus obeys

\[
 \log S\ll_K RmL^{0.2}+B_0L^{0.2}=O_K(L^{0.96}), \tag{21}
\]

inside the ROOTS-008 range. This includes the positive Bonferroni remainder when used to upper-bound an absolute error. Its mean main mass uses the factorial (20); its additive counting discrepancy uses the larger raw retained-term mass. No L^2 memory indices enter (21): that expansion is made only in the independent-line model after arithmetic replacement.

For the real boundaries write root coordinates `s=u/U,t0=v/V,t=r/u`. The original-box conditions for each path position are

\[
 1\le s\tau(z)\le16,\qquad
 1\le t_0\tau(z)+(H/(UVs))z_2\le2.
\]

On potentially contributing boundaries tau is bounded below by 1/16. Their transverse s or t0 derivatives are bounded below accordingly; other derivatives and the number of relative positions are `exp(o(L))`. Also `|(H/(UV))z2|` is bounded on contributing box positions. Choose complements w_z of size O(|z|). The intrinsic ratio has derivative `d beta_z/dt=1/tau(z)^2` before reduction modulo one. All integer frequencies and translates in (2)-(3), including all choices defining their weighted exceptional condition, number `exp(o(L))` and have size `exp(o(L))`. Consequently goodness is constant between that many t-boundary values. This statement is uniform for eligible groups; their positive masses are fixed as the root coordinates vary.

Partition the normalized root box into cubes of side `h=x^{-c_delta/8}`. The total main volume of cubes meeting any effective boundary is `x^{-c_delta/8+o(1)}`, using the transverse derivatives and the above counts. On other cubes every physical indicator is constant. Apply ROOTS-008 to each cube and retained line assignment. There are `O(x^{3c_delta/8})` cubes and `exp(o(L))` retained terms, so the normalized total discrepancy is `x^{-5c_delta/8+o(1)}`. Boundary-cube counting errors are already included in that sum. The main boundary mass is bounded by `x^{-c_delta/8+o(1)}`. Together with (20), both are `O_A(L^{-2AR})` for every fixed A, since R is of order sqrt(L).

This proves the explicit replacement

\[
 \boxed{\frac{D_{\rm unit}}{UV}
 =\kappa_b(H)\int_1^{16}\!\int_1^2\!\int_0^1
          M_R(Us,Vt_0,t)\,dt\,dt_0\,ds
       +O_A(L^{-2AR}).} \tag{22}
\]

Both the endpoint-list closure and root population are those defining D_unit, not a full trace. With A chosen above E0+4, (6) and the bounded measure mass give `D_unit/(UV)<<L^{-2R(E0+4)}`. Its use in a pairing is the finite ambient-Gram inequality of TRACE-009 with the actual coefficient family and list-fiber norms. No full-trace estimate is inferred.

## Assurance and remaining boundaries

Claims (6) and (22) are author proofs of this specified auxiliary chain, with every load-bearing estimate exposed for separate review. They are not accepted merely because the original source states analogous formulas. A critic should especially check the two-sided dirty-edge count, the symmetric introduction-index phase step, and the accumulated damping/boundary discrepancy sum. Any failed step invalidates the combined moment conclusion and must remain visible.

This report does not prove removal of good restrictions in an actual reflected prime pairing, a prime exponential-sum bound on the new denominator-H comparison arcs, H1/selected zero-free hypotheses, or the full Guo/LWW analytic transfer. Even acceptance of these auxiliary claims would leave the original polynomial-cutoff label support, nonzero parity centers, h=1 prime boundary and lower-margin problem. No actual-prime parity theorem, Goldbach proof, demonstrated breakthrough or novelty is claimed.
