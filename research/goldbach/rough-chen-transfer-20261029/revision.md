# GOLDBACH-CHEN-024: original-author revision after distinct challenge

29 October 2026. Actual populated revise stage, round 1. The frozen proposal and complete independent review were read; the review SHA256 matches the assigned value. Only revision.md and revise-result.json are written by this stage. No later investigation's primary inputs are imported.

**Final verdict: incomplete for the original prime margin.** The signed congruence estimate survives review relative to Lichtman Proposition 3.1. The base coefficient \(L_0\), and the repaired lower bound using it, are now expressly conditional on the precise lower-level modified-weight family input below. The numerical anatomy, ordinary coefficient identity, vector cutoff, BV branch calculation, conditional negative semiprime coefficient and prime-filter obstruction remain proved at their stated assurance. No novel theorem, substantive Goldbach breakthrough, positive prime margin or fixed cubic gap is claimed.

Assurance is complete written derivation with distinct-role review, relative to named imported analytic results. It is not proof-assistant certification or a new certification of the source proofs. The same two mechanisms are retained. No additional retrieval, numerical helper, supplement, mechanism, round, paid call, publication or external message was used.

## 1. Frozen evidence

| Frozen input | SHA256 |
| --- | --- |
| statement.md | 09b17b941252a211f3ddc68aea95e5b516a6b58153e461e1e53a42d2566e6f68 |
| propose-result.json | 9a212d25bdcb48b747e878fb4b2fc358709eacc81aeaa700c33cca09410ff7a0 |
| review.md | 3abe3e7627c88ab7da16d992bddc174534f9cd137559894d2165d405f0020de9 |
| challenge-result.json | be98ae25323c1a32488f23cbe8aecfa914f959283d51d072148cb47ff63891e2 |
| source-provenance.json | 3d227f7e5b4e080ba81a4774d1726d71c34bc82fba9d09ce3dda17e3d03785c3 |
| populated revise packet | 788c3d4a245b0d64c1d31228a16d3e2efb3b8eab91b56efc1bb1ae89e0ce29df |

The critic reports checking all sixteen pinned primary file identities. This stage checked the frozen hashes above; that earlier wider verification is not presented as a newly performed source-proof audit. The pinned sources remain Ratliff v2, Li arXiv:2405.05727v4, and Lichtman arXiv:2309.08522v1.

## 2. Response to F2: exact conditional base-family import

Put
\[
 \beta=\frac{25}{224},\quad \eta_0=\frac{249}{448},\quad
 u_0=\frac1{500},\quad \rho_0=\frac{19101}{32000},\quad
 D_\sigma=N^{\eta_0-\sigma},
\]
where \(0<\sigma<1/100\) is fixed. The notation \(\widetilde\lambda^-_{D_\sigma}\) means the actual level-\(D_\sigma\) modified lower family used in the sieve, with the source's modified vector construction. It means neither a truncation of weights constructed at \(N^{\rho_0}\) nor arbitrary smooth coefficients. Define
\[
 \Delta_N(q)=\pi(N;q,N)-\pi(N)/\varphi(q).
\]
The exact zero-extracted-factor input needed for the proposed base is:
\[
 \boxed{
 \sum_{\substack{q\le D_\sigma\\q\mid P(N^{u_0})\\(q,N)=1}}
       \widetilde\lambda^-_{D_\sigma}(q)\Delta_N(q)
       \ll_{A,\sigma}\frac{N}{(\log N)^A}
       \quad\text{for every fixed }A>0.}                    \tag{B0}
\]
Here \(P(v)=\prod_{p<v}p\), with the same fixed boundary convention as in the sieve. Uniformity is over sufficiently large even \(N\) for this family and each fixed \(\sigma\). No uniformity as \(\sigma\downarrow0\) is required.

Li Lemma 2.1 begins with \(D=N^\vartheta\). Its un-subscripted \(\widetilde\lambda^\pm\) plausibly retains that parameter in the exceptional \(r=0\) clause. If that is the intended quantified statement for the same modified family, its outer limit \(q\le N^{\rho_0}\) contains \(q\le D_\sigma\), and (B0) follows because those very coefficients vanish outside \(D_\sigma\). That reasoning would use a retained parameter and exact support, not monotonicity of a signed sum.

The exceptional display does not explicitly write this family quantifier. Lichtman Section 6.1 describes the support framework and refers elsewhere for the precise modified construction. Within the pinned inputs I do not establish that the exceptional assertion covers this particular lower-level family. Thus (B0) is the precise additional import, **unverified here**. An estimate for the different family \(\widetilde\lambda^-_{N^{\rho_0}}\) cannot be shortened or assigned new coefficients to prove it.

This qualification supersedes the unconditional proved label on proposal (7), and on the use of that particular \(L_0\) in (13). It does not refute Li's lemma or claim that (B0) is false.

### 2.1 Numerical anatomy retained, coefficient conclusion qualified

The complete elementary anatomy proof in frozen Section 2.1 and review Section 3 remains proved. With \(\theta=7/32\),
\[
 v(t)=\min\{(1+t)/2,\ 1-34t/39,\ 57/64-3t/2\},
\]
and the exact three-coordinate maximum from Lichtman (6.4) satisfies
\[
 v(t_1,t_2,t_3)\ge\eta_0
       \quad(0<t_3\le t_2\le t_1\le\beta).                  \tag{R1}
\]
If \(t_1+t_2\ge\beta\), the entry \(v(t_1+t_2)\) gives the bound by its three endpoint comparisons on \([\beta,2\beta]\). Otherwise \(t_2,t_3<\beta/2\); the auxiliary minimum's three entries exceed \(\eta_0\), and its gate threshold \((1+t_1)/2\) is below \(\eta_0\). This also proves the missing-coordinate inequalities at \((t_1,t_2,u_0)\) and \((t_1,u_0,u_0)\) when the extracted coordinates are at least \(u_0\).

The disjoint grouping is correct: extract exactly the three largest primes if at least three exceed \(N^{u_0}\), leaving \(c\mid P(p_3)\); with exactly two or one, leave \(c\mid P(N^{u_0})\); with none, use (B0). Squarefree support gives uniqueness. No extra \(u_0\)-smoothness restriction is introduced into the three-factor clause. The actual imported construction must be retained, and each extracted vector must satisfy
\[
 D_1\cdots D_{j-1}D_j^2<D_\sigma\quad\text{for every }j.     \tag{R2}
\]
Its fixed positive margin and fixed mesh allow summing the stated \(r=1,2,3\) estimates. The missing zero-factor instance is precisely (B0).

Consequently, conditional on (B0) for that same standard modified lower-sieve construction, the other stated Li estimates, local factors and continuity argument give
\[
 \liminf_{\substack{N\to\infty\\2\mid N}}
 \frac{S(\mathcal A_N,N^\beta)}{\mathcal X_N}
 \ge L_0=\frac{e^{-\gamma}}{\beta}f(\eta_0/\beta).            \tag{R3}
\]
Here
\[
 \mathcal X_N=2C_2\mathcal S_0(N)N/(\log N)^2,\quad
 C_2=\prod_{p>2}(1-(p-1)^{-2}),\quad
 \mathcal S_0(N)=\prod_{\substack{p\mid N\\p>2}}\frac{p-1}{p-2}.
\]
The full proof of this conditional implication is the frozen base derivation, with the family qualification (B0): the local product is \(2e^{-\gamma}C_2\mathcal S_0(N)/(\beta\log N)\), the exceptional primes dividing \(N\) are bounded, and fixed \(\sigma\) limits precede continuity as \(\sigma\downarrow0\).

The switched upper application has a separate construction requirement. Its actual upper modified family must restrict its largest extracted exponent to \(t_1\le(\eta_0-\sigma)/3\), up to the construction's mesh loss absorbed in a fixed margin. The ordinary condition \(p_1^3<D_\sigma\) alone does not prove this for arbitrary modified weights. Conditional on that actual property, the numerical upper anatomy comparisons are correct: \(t_1\ge\beta\) uses \(v(t_1)=(1+t_1)/2\), while \(t_1<\beta\) uses the auxiliary minimum at \(t_3=\beta\), whose second entry equals \(\eta_0\). Its zero-factor family input and the full product-domain extension are not established from the ordinary support either. The switched contaminant bounds therefore remain conditional.

## 3. Clean formulas and retained mechanism 1

For a fixed logarithmic cell \(J_t\) of the largest modulus prime, the clean formula intended by frozen (9) is
\[
 A_t(q)=
 \sum_{\substack{\ell d=q\\\ell\in\mathbb P\cap J_t}}
   \mathbf1_{\{d\mid P(N^\rho)\}}\,
   \widetilde\lambda^+_{N^{\eta(t)-t}}(d),\qquad \rho\le t.  \tag{R4}
\]
It is not automatically a total-modulus modified weight.

The fixed largest factor \(\ell=N^{t+o(1)}\) must obey \(2t<\eta(t)\) to fit (R2). For \(\eta(t)=57/64-3t/2\), this is exactly \(t<57/224\), with a fixed margin required. Above this threshold the specified vector invocation fails. For ordinary weights and squarefree \(d\) with \(P^+(d)<\ell\),
\[
 \lambda_D^-(\ell d)=-\lambda_{D/\ell}^+(d)
                         \quad\text{if }\ell^2<D.            \tag{R5}
\]
Prepending \(\ell\) converts the lower support's remaining even indexed conditions into the upper support's odd indexed conditions at \(D/\ell\), and changes the Mobius sign. At \(d=1,\ell^2\ge D\), the left side is zero while the proposed right side is \(-1\). Thus extension fails. No corresponding modified identity is assumed.

The half-level branch statement remains proved relative to classical BV, independently of (B0). At total level \(N^{1/2-\sigma}\), each total modulus has only \(O_\beta(1)\) candidate prime divisors \(\ell\ge N^\beta\); ordinary weights are bounded. Hence the aggregated coefficient is bounded, and the absolute BV sum at endpoint \(N\) controls its error. BV's reduced-residue supremum handles residue growth. The upper branch has normalized limsup at most
\[
 H_{1/2}(\alpha)=
 2e^{-\gamma}\int_3^{87/25}F(s)\,ds
       +4\log\frac{3\alpha}{1/2-\alpha}.                    \tag{R6}
\]
Choose \(\rho=t\) up to \(1/8\), then \(\rho=(1/2-t)/3\). The substitution \(s=1/(2t)-1\) gives the first term; the second integrand is \(2/[t(1/2-t)]\). Fixed positive margins followed by continuity give (R6). The exceptional and endpoint bounds remain those proved in the frozen proof and checked in review.

Its combination with this base is now explicitly conditional on (B0) and the actual base construction:
\[
 \liminf U_\alpha/\mathcal X_N\ge L_0-H_{1/2}(\alpha).       \tag{R7}
\]
The branch estimate itself is unaffected by the base qualification. The nonnegative correction cost on \([a,b]\subset(57/224,\alpha]\) is more cleanly written
\[
 \int_{[a,b]\cap(-\infty,25/96)}
 \left\{\frac2{t(1/2-t)}
            -\frac2{t(57/64-5t/2)}\right\}\,dt,              \tag{R8}
\]
and is zero outside that clipped interval, where BV covers the smaller claimed level. This does not justify neighboring modified coefficients.

### 3.1 The failed semiprime sign remains a conditional calculation

For \(1/4<\alpha<1/3\), exact counting with multiplicity retained gives
\[
 U_\alpha=R_\alpha+E_\alpha+H_\alpha,\quad
 F_\alpha=U_\alpha-E_\alpha,\quad R_\alpha=F_\alpha-H_\alpha.
                                                               \tag{R9}
\]
The ordered-once harmonic masses are
\[
 B_2=\log((1-\alpha)/\alpha),\qquad
 B_3=\int_\alpha^{1/3}
             \frac{\log((1-2t)/t)}{t(1-t)}\,dt.
\]
They are not correlated prime-complement asymptotics.

Keep exactly the optimistic analytic inputs from the proposal: the base \(L_0\), the stronger uncorrected source branch \(H_{\mathrm{src}}\), and switched upper bounds \(E_\alpha/\mathcal X_N\le2B_2/\eta_0+o(1)\), \(H_\alpha/\mathcal X_N\le2B_3/\eta_0+o(1)\). These include the actual upper modified support, its coefficient-specific distribution and zero-factor instance, and the full product-domain extension. They remain unproved here. Li's printed switched numerator also uses coprimality with \(N\). On the claimed upper support all modulus primes would be smaller than product primes, giving automatic product-modulus coprimality; products sharing a prime with \(N\) are negligible exceptions. This still does not prove the missing extension of the short boxes to all products below \(N\).

Under exactly those assumptions the prospective prime coefficient is
\[
 C(\alpha)=L_0-H_{\mathrm{src}}-\frac2{\eta_0}(B_2+B_3).
\]
Its negativity is proved independently of their truth. Since \(f\le1\), \(\gamma>1/2\), and \(e^{1/2}>3/2\), \(L_0<448/75\). The source integrands are at least \(4/[t(1-t)]\), hence \(H_{\mathrm{src}}\ge4\log(199/75)\). Also \(B_2>\log2\), \(B_3\ge0\), and \(\log x>2(x-1)/(x+1)\) for \(x>1\). The latter follows by differentiating the difference. Therefore
\[
 H_{\mathrm{src}}+\frac2{\eta_0}B_2
 >\frac{496}{137}+\frac{1792}{747}
  =\frac{448}{75}+\frac{353328}{7675425},
\]
so
\[
 C(\alpha)<-\frac{353328}{7675425}
                   \quad(1/4<\alpha<1/3).                 \tag{R10}
\]
This is a proved inequality for the specified conditional expression. It neither establishes its analytic inputs nor excludes other stronger signed arithmetic. Positive prime-plus-\(P_2\) counts do not give (R9)'s desired sign.

## 4. Accepted signed theorem with its literal coupled weight

Retain the exact cubic definitions
\[
 \begin{gathered}
 I=(N/3,2N/3],\quad y=N^{1/6},\quad z=(\log N)^4,\quad
 D=N^{1/2}(\log N)^{-B},\\
 W=\operatorname{rad}\left(N\prod_{p\le z}p\right),\quad
 \kappa=W/\varphi(W),\quad \Phi(t)=1-3t^2+2t^3,\\
 u(n)=\theta(N-n)-\kappa\mathbf1_{\{(N-n,W)=1\}}
                    -\theta(N/2)\mathbf1_{\{n=N/2\}}.
 \end{gathered}
\]
Here \(B>0\) is fixed, and \(\theta(m)=\log m\) on primes and zero otherwise. The unchanged full operator is
\[
 H_{3,D}=\sum_{k\ge1}\sum_{\substack{h>D\\kh\in I}}
     \mu(h)\Phi\left(\frac{\log h_{>y}}{\log(kh)}\right)u(kh).
                                                               \tag{R11}
\]
For fixed \(0<\epsilon<1/2000\), the clean version of proposal (20) is
\[
 a(k,h)=
 \mathbf1_{\{k\in\mathbb P,\ y<k\le N^{1/3-\epsilon}\}}\,
 \mathbf1_{\{h>D,\ P^-(h)>y\}}\,\mu(h)
       \Phi\left(\frac{\log h}{\log(kh)}\right).              \tag{R12}
\]
When \(\mu(h)\ne0\), roughness and squarefreeness give \(h_{>y}=h\). When \(\mu(h)=0\), both coefficients vanish. Thus (R12) is literally a suboperator of (R11), including common factors of \(k,h\) and repeated factors of \(kh\).

**Proved relative to Lichtman Proposition 3.1 and its endpoint-uniform interval formulation:** for every \(A>0\), every sufficiently large even \(N\), and every genuinely triply well-factorable sequence \(\lambda_d\) of level
\[
 Q=N^{153/256-100\epsilon},
\]
supported on \((d,N)=1\),
\[
 \left|\sum_{d\le Q}\lambda_d
 \sum_{\substack{k,h\\kh\in I}}a(k,h)
 \left(\mathbf1_{\{kh\equiv N\pmod d\}}
       -\frac{\mathbf1_{\{(kh,d)=1\}}}{\varphi(d)}\right)\right|
 \ll_{A,\epsilon,B}\frac{N}{(\log N)^A}.                     \tag{R13}
\]
Triple factorability has its exact Definition 1.4 meaning: convolution by three 1-bounded sequences for every splitting of \(Q\), with the specified factor supports. It is assumed for the modulus sequence, not proved for arbitrary Mobius or modified sieve coefficients. No version of (B0) is needed.

### 4.1 Complete reduction and the critic's uniform Abel argument

Set \(x=N/3\), residue \(a=N\), and residue exponent \(1+\epsilon\); eventually \(N<x^{1+\epsilon}\). Each dyadic rectangle \(K<k\le2K,\ H<h\le2H\) meeting \(kh\in(x,2x]\) has \(KH\asymp x\). The small factor is \(k\), with \(K\gg N^{1/6}\) and \(K\le N^{1/3-\epsilon}\), so eventually \(x^\epsilon\le K\le x^{1/3+\epsilon}\). Its coefficient is the prime indicator with the stated endpoints, is 1-bounded, satisfies the imported Siegel-Walfisz condition including its auxiliary coprimality condition, and is supported above \(y>x^{1/(\log\log x)^3}\). The large coefficient is
\[
 \beta_h=\mu(h)\mathbf1_{\{h>D,\ P^-(h)>y\}},
\]
which is 1-bounded and need not satisfy SW. No SW property of a coupled \(\mu(h)\Phi\) sequence is used.

The proposition's admissible level is
\[
 \min\left\{\frac{66}{107},\frac{5-(1+\epsilon)7/32}{8}\right\}
       -50\epsilon
   =\frac{153}{256}-(50+7/256)\epsilon.
\]
Our level has fixed spare margin, absorbs the constant change \(N=3x\), and exceeds \(1/2\) for the stated epsilon range. It uses the Goldbach-size-residue exponent.

The needed partial-rectangle bound is uniform in both endpoints. Truncating the prime indicator at a dyadic endpoint preserves SW uniformly: subtract the endpoint-uniform prime estimates, including the auxiliary coprimality restriction, at two endpoints comparable to \(K\). Equivalently, the proof of Proposition 3.1 explicitly reduces in (5.19) to arbitrary subintervals \(I_N,I_M\). The large-factor truncation is permitted because that sequence is arbitrary and bounded. This is the precise interval uniformity checked by the critic; no new coupled-weight SW or Mellin-twist assumption is inserted.

Let \(E(s,t)\) be the unweighted discrepancy, including the outer \(\lambda_d\) sum, on \(K<k\le s,\ H<h\le t\), retaining \(kh\in I\) and the same small and large coefficients. Ask the theorem for accuracy \(A+3\). Then
\[
 \sup_{s,t}|E(s,t)|\ll N(\log N)^{-A-3}.                    \tag{R14}
\]
For \(f(k,h)=\Phi(\log h/\log(kh))\), all relevant logarithms are comparable to \(\log N\), and
\[
 |f|+K|f_k|+H|f_h|+KH|f_{kh}|\ll1.                         \tag{R15}
\]
Exact two-variable Abel summation expresses the weighted discrepancy as
\[
 \begin{split}
 &f(K_2,H_2)E(K_2,H_2)
 -\int_K^{K_2}f_k(s,H_2)E(s,H_2)\,ds\\
 &-\int_H^{H_2}f_h(K_2,t)E(K_2,t)\,dt
 +\int_K^{K_2}\int_H^{H_2}f_{kh}(s,t)E(s,t)\,dt\,ds .
 \end{split}                                               \tag{R16}
\]
The absolute coefficient mass in (R16) is bounded by (R15). Hence (R14) controls the full literal \(\Phi\) at bounded cost. The product interval stays fixed and permitted. There is no approximation, dropped strip or Mellin tail. Summing \(O((\log N)^2)\) rectangles proves (R13).

Restriction of \(\lambda\) to \((d,N)=1\) preserves triple factorability: restrict each convolution factor to arguments coprime to \(N\); their product is coprime exactly when every factor is. The main numerator therefore remains exactly \(\mathbf1_{\{(kh,d)=1\}}\). All signs, support conditions and endpoints are retained.

## 5. Response to F1: the prime filter and full residuals remain open

The clean identity intended by proposal (22) uses \(m=N-kh\in[N/3,2N/3)\), \(Z=\sqrt{2N/3}\), and \(P_{\le}(Z)=\prod_{r\in\mathbb P,\ r\le Z}r\):
\[
 \mathbf1_{\{m\in\mathbb P\}}
       =\sum_{\substack{d\mid m\\d\mid P_{\le}(Z)}}\mu(d).    \tag{R17}
\]
For large \(N\), interval primes exceed \(Z\), and every interval composite has a prime factor at most \(Z\). The complete squarefree divisor sum is respectively 1 and 0, including prime powers. This proves (R17).

Its actual moduli extend beyond \(Q\). The naive truncated sequence
\[
 b_d=\mu(d)\mathbf1_{\{d\le Q\}}\mathbf1_{\{P^+(d)\le Z\}}
\]
is not triply well-factorable at level \(Q\): choose a prime \(r\in(Q^{1/3},2Q^{1/3}]\). For large \(N\), \(r<\min(Q,Z)\), so \(b_r=-1\), whereas every convolution for the balanced three-factor split has coefficient zero at \(r\). If coprimality to \(N\) is required, the prime number theorem gives an increasing number of candidates, while \(N\) has at most \(3\log N/\log Q=O_\epsilon(1)\) prime factors exceeding \(Q^{1/3}\). Thus \(r\nmid N\) can be chosen. More generally, the balanced split forces a truly triply well-factorable sequence to vanish at every argument with a prime factor exceeding \(Q^{1/3}\).

This disproves that exact filter transport. It does not refute a signed average on the actual coupled supports. Since \(\Phi\ge0\) but \(\mu(h)\) has both signs, a signed lower estimate requires a prime minorant on \(\mu(h)=+1\) and a majorant on \(\mu(h)=-1\). Both parity indicators are admissible large-factor sequences; no suitable complementary-prime filters have been constructed. Multiplying a single upper bound by \(\mu(h)\) is invalid.

Thus (R13) has not established a useful fixed-constant lower estimate for
\[
 \sum_{\substack{k,h\\kh\in I}}a(k,h)
 \left[\theta(N-kh)-\kappa\mathbf1_{\{(N-kh,W)=1\}}
              -\theta(N/2)\mathbf1_{\{kh=N/2\}}\right].      \tag{R18}
\]
It does not replace the radical-wheel model by the reduced-residue main numerator or remove the correction atom. The \(k=1\) term of (R11) is retained: its rough part vanishes because \(\Phi(1)=0\), while its nonrough part need not vanish.

All omitted cofactor ranges and nonrough products remain in the full operator. The nonrough, even rough and outer odd residuals in the earlier cubic revision are unchanged. Repeated factors remain in exact identities and in (R13). The original target
\[
 H_{3,D}\ge-\left(\frac34-\delta+o(1)\right)M_N
 \quad\text{for one fixed }\delta>0,\qquad
 M_N=\frac{2C_2\mathcal S_0(N)N}{3\log N}                    \tag{R19}
\]
remains unproved, as does \(F_\alpha>H_\alpha\). The quantifier remains every sufficiently large even \(N\), not an average or a selected family.

## 6. Final claim status

F1 is accepted and unresolved: prime-weight transport, wheel, atom and omitted sectors remain necessary. F2 is accepted as a qualification: (B0) is the exact family input not established from the pinned statements, so the base and its \(L_0\) combination are conditional; the elementary anatomy and ordinary BV branch are unaffected. F3 is repaired by (R4), (R12) and (R17), while preserving the frozen proposal.

The retained checked stronger-distribution result is (R13), on its exact restricted support and assumed genuinely triply well-factorable modulus class, relative to Lichtman Proposition 3.1. It is a signed congruence corollary, not a Goldbach lower bound or claimed novel breakthrough. The ordinary/vector deductions and conditional negative coefficient are also retained.

The next mathematical obligation is a sign-aware complementary-prime filter passing the balanced support test, followed by the unchanged residual estimates. A separate source-scope obligation is (B0). Neither grants another round. Pair stages cost eight declared proxy units, plus root primary-access preparation two, ten total. Token and monetary usage remain unknown. The persistent user objective remains incomplete.
