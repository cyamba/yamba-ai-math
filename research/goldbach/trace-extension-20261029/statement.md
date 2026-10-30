# Trace compression and enlarged determinant-H roots

29 October 2026. Registry role: Mathematician, `GOLDBACH-TRACE-009`, author stage. Two bounded candidates are proved below, pending distinct review: a finite trace-compression bridge with its endpoint-list factor, and a joint count for the enlarged roots. The enlarged count allows prescribed primes dividing H. These results do not prove the remaining trace estimate or a Goldbach lower bound. Novelty is unverified.

The inspected [source definitions and moment statement, sections 4.2-4.6](https://arxiv.org/html/2610.20242v1) distinguish list-weighted endpoint vectors from a trace over all states. We use its finite list definitions to calculate an explicit cost. We do not import its full theorem, its moment conclusion for a different operator, or a variable-H version of its appendix.

## Candidate 1: a true finite trace bridge

Let H be an even positive integer, H>=2. Use the exact sector domains

\[
 \Omega'_c=\{(u,w):U\le u\le16U,\ V\le cu+Hw\le2V\},
 \quad 0\le c<H,
\]

with U,V>=2 and integral positions, and retain all original finite first-coordinate lists and their positive state weights. Let B_c be the coefficient-one centered operator defined with the full-pullback comparison and rescaled cutoff of SECTORS-006, now on **all** primitive positions `(u,w)` in this domain. Retain the specified list symmetrization, damping and good-state projections. Let P_c be the orthogonal diagonal projection onto `(u,H)=1`.

The original enlarged preimage `(u,cu+Hw)` need not be primitive at primes dividing H. This is an artificial enlargement for bounding an operator, not identification with the original arithmetic sequence. No group primes are deleted and no normalization changes: all original group masses and list weights are retained. States with a list prime dividing H simply cannot lie in P_c. The second candidate below accommodates those primes in the enlarged state space.

The sector label remains part of every state, even if two image positions coincide as bare integer pairs. All endpoint families and traces below use that disjoint-union convention.

Define `A_H^unit` as the SECTORS-006 operator on primitive original positions with unit first coordinate. Then its proved finite conjugacy gives

\[
 A_H^{\rm unit}\simeq\bigoplus_{c\pmod H}P_cB_cP_c. \tag{1}
\]

Every entry between retained states agrees: first coordinates and lists are unchanged, the transported good-state ratio is the complement ratio in the image, and the exact and comparison brackets both transform. A further actual-input both-unit restriction is another orthogonal compression, rather than a claim that every enlarged state meets it.

### Schatten contraction, and why a pointwise replacement is different

For any finite weighted Hilbert space, orthogonal projection P, operator B and real p>0,

\[
 \sum_j s_j(PBP)^p\le\sum_j s_j(B)^p. \tag{2}
\]

To prove it, use an orthonormal basis for the weighted space. The singular-value decomposition gives `s_j(T)=inf_{rank F<j}||T-F||`. Compressing any such F preserves its rank bound and cannot increase its error. Thus `s_j(PBP)<=s_j(B)` term by term. In particular, for each integer R>=1, (1)-(2) imply

\[
 \boxed{\operatorname{Tr}((A_H^{\rm unit}(A_H^{\rm unit})^*)^R)
       \le\sum_c\operatorname{Tr}((B_cB_c^*)^R).} \tag{3}
\]

This is a trace inequality. Deleting intermediate projections is not a pointwise diagonal inequality for powers. For example, in Euclidean three-space take

\[
 B=\begin{pmatrix}1&0&1/2\\1&0&-2\\0&0&0\end{pmatrix},
 \qquad P=\operatorname{diag}(1,1,0).
\]

Then for e1 and R=2,

\[
 \langle e_1,((PBP)(PBP)^*)^2e_1\rangle=2
    >25/16=\langle e_1,(BB^*)^2e_1\rangle.
\]

This refutes the pointwise deletion assertion while leaving (3) intact.

### The endpoint-vector factor is explicit

For each position P let u_P be the function equal to one on its admissible list states and zero elsewhere. Such vectors have disjoint supports for different positions. Write `mu_P=||u_P||^2` and `mu_max=max_P mu_P`, with zero if there are no states. For every positive semidefinite K,

\[
 \sum_P\langle u_P,Ku_P\rangle\le\mu_{\max}\operatorname{Tr}K. \tag{4}
\]

Indeed the nonzero `u_P/sqrt(mu_P)` are orthonormal. Equivalently the frame operator `sum_P u_P tensor u_P^*` has eigenvalues mu_P and is at most `mu_max I`. Thus the actual finite consequence for the original root moment is

\[
 \boxed{\sum_P\langle u_P,(A_H^{\rm unit}(A_H^{\rm unit})^*)^Ru_P\rangle
     \le\mu_{\max}\sum_c\operatorname{Tr}((B_cB_c^*)^R).} \tag{5}
\]

This does not insert the number of positions as an additional factor, and it does not pretend u_P is normalized.

For K disjoint prime groups, ordered distinct lists of length m=J+1 dividing the first coordinate u, and state weight `prod_i V_i^{-m}`, let `n_i(u)` be the number of distinct group-i primes dividing u. Exactly

\[
 \mu_P=\prod_{i=1}^K\frac{(n_i(u))_m}{V_i^m}, \tag{6}
\]

where `(n)_m=n(n-1)...(n-m+1)` and the factor is zero if n<m. If all group-i primes exceed p_min,i, then uniformly for u<=16U,

\[
 \mu_{\max}\le\prod_i
       \left(\frac{\log(16U)}{V_i\log p_{\min,i}}\right)^{J+1}. \tag{7}
\]

For the inspected source scales, with `L=log x`, fixed K, `log(16U)=O_K(L)`, `log p_min,i>=L^{0.1}`, group masses bounded below by a positive constant, `J~L^{0.01}` and `R~L^{1/2}`, this gives

\[
 \log\max(1,\mu_{\max})=O_K(L^{0.01}\log L),\qquad
 \max(1,\mu_{\max})^{1/(2R)}=1+o(1). \tag{8}
\]

The finite factor is retained, and only its indicated root is asymptotically harmless. No division by a possibly empty reduced group mass is performed. If other list weights or growing K are chosen, (6)-(7) must be used with their actual values instead.

Let `T_R=sum_c Tr((B_cB_c*)^R)`. A new bound `T_R/(UV)<=L^{-2RE}` would, by (5), give the original normalized endpoint root moment at most `mu_max L^{-2RE}`, with the harmless root cost (8). This is a concrete bridge, not a proof of that new bound. The crude norm conclusion `||A_H^unit||<=T_R^{1/(2R)}` still includes the volume factor `(UV)^{1/(2R)}`; at UV comparable to x this is not automatically harmless. Endpoint pairings need their actual localization and moment argument.

The source endpoint moment is not already an enlarged trace theorem. Even at one position with two list states, the projection onto the vector orthogonal to `(1,1)` has zero quadratic moment on u_P=(1,1), but positive trace at every positive integer power. Thus small endpoint moments alone do not bound the trace required in (5). A separate enlarged trace/path analysis remains necessary.

There is also a less demanding finite route for endpoint pairings, which avoids requiring a full trace. Set `B=direct_sum B_c` and `P=direct_sum P_c`. For f=Pf and g=Pg,

\[
 \langle f,PBPg\rangle=\langle f,Bg\rangle.
\]

Put K=BB*, and write `f=sum_{P in E}alpha_P u_P` on any specified retained endpoint family E. Its Gram matrix with entries `M_{PQ}=<u_P,K^R u_Q>` is positive semidefinite, so its largest eigenvalue is at most `D_E=sum_{P in E}<u_P,K^R u_P>`. Spectral Holder and Cauchy therefore give, for R>=1,

\[
 |\langle f,PBPg\rangle|
 \le\|g\|\|f\|^{1-1/R}
           \left(D_E\sum_{P\in E}|\alpha_P|^2\right)^{1/(2R)}. \tag{8a}
\]

This uses the ambient K^R before restricting its Gram matrix; it makes no invalid comparison of diagonal powers of compressed and uncompressed operators. The sufficient bound `D_E<=mu_max Tr(K^R)` recovers the optional full-trace route. An arithmetic bound on D_E itself could be substantially weaker and would suffice for (8a). Neither such arithmetic bound has been proved here.

## Candidate 2: the enlarged joint root count

### Exact root bijection, including multiple preimages of an original position

An enlarged root is a pair `(c,(u,w))`, with `0<=c<H`, `(u,w)=1`, u>0, and `v=cu+Hw` in the original v interval. Its canonical complement `(r,s)` satisfies `us-wr=1` and `0<=r<u`. Thus r is a unit modulo u and

\[
 G=\begin{pmatrix}u&r\\v&d\end{pmatrix},\qquad
 d=cr+Hs,\qquad \det G=H,\quad vr=-H\pmod u. \tag{9}
\]

Conversely take a triple `(u,v,r)` with `0<=r<u`, `(u,r)=1` and `vr=-H mod u`, and put `d=(H+vr)/u`. Choose integers a,b with `au+br=1` and set

\[
 c=av+bd\pmod H,\quad0\le c<H,\qquad
 w=(v-cu)/H,\quad s=(d-cr)/H. \tag{10}
\]

The determinant relation gives `cu=v mod H` and `cr=d mod H`; hence w,s are integers. Moreover `us-wr=(ud-vr)/H=1`. The sector is unique: two possible c differ by a number annihilating both u and r modulo H, which must be zero by their Bezout identity. This proves a bijection between enlarged roots and these triples. The original pair (u,v) is not required to be primitive or unit modulo H.

For fixed u,v, put g=(H,u). There are no such triples unless `(v,u)=g`. If that equality holds, the number is

\[
 \frac{\phi(u)}{\phi(u/g)}. \tag{11}
\]

Indeed multiplication of unit residues by H has image the residues of gcd g with u; equivalently reduce the resulting unit congruence modulo u/g. The unit reduction map is surjective, with that fiber size. Each r gives a different sector preimage by the bijection. For example H=2,u=4,v=2 has r=1 and r=3, giving respectively sectors 1 and 0. These are two distinct enlarged roots and must both be counted.

### Uniform count, even at prescribed primes dividing H

Let U,V>=2. Use the same half-open intervals I1,I2,I3 as ROOTS-008, inside `[1,16]`, `[1,2]`, `[0,1]`, with lengths L1,L2,L3. Count the triples in (9) with `u/U in I1`, `v/V in I2`, `r/u in I3`, and prescribed first-row kernels `ker(u,r)=ell_p` for p dividing a squarefree S. **No coprimality between S and H is required.** The primitive first row defines each kernel even if the full matrix is singular modulo p. Then, for every fixed eta>0,

\[
 \boxed{N_{\rm ext}=
 \frac{UVL_1L_2L_3}{\zeta(2)\prod_{p\mid S}(p+1)}
 +O_\eta\!\left((\sigma_{-3/4}(H)U^{7/4+\eta}+V)
                                           \log^2(2U)\right).} \tag{12}
\]

The constant depends only on eta. This counts roots with their sector multiplicity, not distinct original pairs. There is no `kappa_b(H)` because no H-unit filter remains. The assertion is an absolute estimate, including empty populations and intervals.

To prove it, split S=QR by the horizontal row kernels. The identical row-primitive argument gives

\[
 Q\mid u,\qquad(u,R)=1,\qquad r=\rho u\pmod R. \tag{13}
\]

This uses `(u,r)=1`, not invertibility of the whole matrix. It remains correct when p divides H, p divides u, rho=0, or prime powers divide u.

Fix such a u and let f be the indicator of the canonical r progression in `[a3*u,b3*u)`, and g the v interval `[a2*V,b2*V)`. Their double Fourier expansion is

\[
 \frac1{u^2}\sum_{h,j\pmod u}
                   \widehat f(h)\widehat g(j)K_u(h,-jH).
\]

The complete sum is over unit r. It imposes precisely `v=-H r^{-1} mod u`, without requiring v or H to be a unit modulo u. The j=0 part is exactly `(T/u) A_u`, where T is the integer v-cardinality and

\[
 A_u=\frac{L_3\phi(u)}R+O(\tau(u)).
\]

For j nonzero, including h=0, the elementary complete bound and

\[
 (h,jH,u)\le(H,u)(j,u)
\]

give the remaining error

\[
 O\!\left(C(u)u^{3/4}(H,u)^{1/4}
                     \sigma_{-3/4}(u)\log^2(2u)\right). \tag{14}
\]

Here C(u) is the reviewed complete-sum factor from RATIOS-007. The normalized Fourier l1 norm of f is O(log(2u)), since R is a unit modulo u. The nonzero v frequencies have weighted norm `O(sigma_{-3/4}(u)log(2u))`, proved by the divisor-weighted geometric sum in ROOTS-008. The zero v-frequency has been retained exactly; the zero r-frequency has not been dropped. Replacing T by `L2*V` costs O(1).

For the sum of (14), use

\[
 \sum_{U\le u\le16U}(H,u)^{1/4}
 \le\sum_{d\mid H}d^{1/4}\#\{u\in[U,16U]:d\mid u\}
 \le31U\sigma_{-3/4}(H). \tag{15}
\]

Only d<=16U can contribute. For those d the count is at most `15U/d+1<=31U/d`. The subpower factors C(u) and `sigma_{-3/4}(u)` are absorbed in any fixed eta. This proves the completed-sum term in (12), without a positive H power or a unit-H assumption.

The A_u error sums to `O(V log^2(2U))`. For the main weighted-u mass, the ROOTS-008 Mobius calculation now has only the R exclusion and no H exclusion:

\[
 \sum_{a_1U\le u<b_1U,\ Q\mid u,\ (u,R)=1}\frac{\phi(u)}u
 =\frac{L_1U}{\zeta(2)}
       \prod_{p\mid R}\frac p{p+1}
       \prod_{p\mid Q}\frac1{p+1}
       +O(2^{\omega(R)}\log(2U)).
\]

Its prefactor is `VL2L3/R`. Thus its error is `O(V*(2^{omega(R)}/R)*log(2U))`, at most `O(V log(2U))`. Its main term is exactly the coefficient in (12). This explicitly retains the R exclusion before absorbing it. The proof applies to every squarefree S, and to all original group primes without deletion or renormalization.

If H<=X^A, S<=exp(C(log X)^0.98), U comparable to X^a and V comparable to X^b, for fixed positive a,b with `b>3a/4`, (12) has absolute error `UV X^{-gamma+o(1)}`, `gamma=min(a,b-3a/4)>0`. The sigma factor in H is uniformly subpower. Fixed positive interval lengths also give relative saving and eventual nonemptiness. Shrinking intervals require their actual main mass to dominate the absolute error. Balanced square-root boxes give exponent 1/8, with unspecified constants and thresholds. The estimate provides no fixed power saving from this method when `b<=3a/4`; that is a limitation of the error, not a counterexample to its main term.

## Real coordinates and the exact remaining trace task

Let `t=r/u`, and extend the root matrix to real t as

\[
 G_H(u,v,t)=\begin{pmatrix}u&ut\\v&vt+H/u\end{pmatrix}.
\]

For an enlarged root, its image matrix `[[u,r],[w,s]]` is unimodular, so every integer image position has unique integral relative coordinates z; primitive image positions correspond to primitive z. In original coordinates `Q=G_H z`. Write `tau=z1+t*z2`. If P,Q both have original preimages in the box, then

\[
 \frac1{16}\le\tau=Q_1/u\le16,\qquad
 z_2=\det(P,Q)/H,\qquad
 |z_2|\le32UV/H,\quad |z_1|\le16+32UV/H. \tag{16}
\]

These bounds apply simultaneously to every endpoint of a path relative to its root. Put `lambda=H/(UV)`, `s0=u/U`, `t0=v/V`. The original box inequalities are precisely

\[
 1\le s_0\tau\le16,\qquad
 1\le t_0\tau+(\lambda/s_0)z_2\le2. \tag{17}
\]

For any z that occurs somewhere in these domains, `|lambda*z2|<=32`. The coefficients and first derivatives of the two boundary functions in the normalized variables `(s0,t0,t)` are therefore `O(1+UV/H)`, without a separate H loss: the potentially large lambda always multiplies z2, while t-derivatives cost only z2. Higher s0 derivatives have the same bounded coefficient on `[1,16]`. This is a concrete geometric control, not an estimate of every discontinuous path weight.

For the intended scales `UV/H=exp(O_K(L^{0.21}))`, relative coordinate heights and each such boundary derivative are subpolynomial in x. Even a fixed-dimensional product repeated O(R) times has exponential scale `exp(O_K(R L^{0.21}))`, still subpolynomial for R of order L^{1/2}. This observation does not bound the entire prime-list/path expansion, its prescribed-modulus products, variation after all discontinuities, or its centered cancellation. Those costs must be summed rather than inferred from individual boundaries.

## Closer prior framing and the remaining obligation

The pinned [Guo source](https://github.com/aster2024/openai-math-followups/blob/a605351dce1a55fb46a494d9cca9b0baa8f2734b/mobius-goldbach-shift/source/main.tex), blob `a114f906cf205f4e50053c7a657f7de55048213c`, already defines labelled lattice-primitive enlarged states, intrinsic complement ratios and endpoint compression at source lines 962-1030. It uses ambient positive powers and then a restricted-root Gram matrix, avoiding any requirement to estimate the full trace on added states. This is closer prior framing for (1) and (8a); the enlargement is not claimed new. Its later geometry also retains the moving determinant term. Its block Type II proposition at lines 1342 onward explicitly assumes H2'. The inspected source assertions, that hypothesis and the claimed analytic transport are not validated or imported here.

The independently derived finite Schatten route is an optional stronger sufficient target. The restricted endpoint Gram route (8a) can instead seek an arithmetic bound on D_E directly. Neither the bound on `T_R/(UV)` nor the required bound on D_E has been established by this stage. Whichever route is used must include all state/list weights, accumulated root-count errors, clean and dirty edge costs, geometric restrictions and memory/distinctness terms. Equation (12) supplies only one arithmetic input for finite prescribed root data. It does not justify the full list/path estimate or identify it with an already proved source theorem. The full-pullback denominator-H prime major term, polynomial-label limitations, nonzero centers and the h=1 prime boundary remain separate. No actual-prime cancellation, Goldbach proof or demonstrated breakthrough is established.
