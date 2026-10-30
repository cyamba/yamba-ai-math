# GOLDBACH-CHEN-024: actual proposal and signed transfer attempt

29 October 2026. Mathematician, propose stage, one bounded pair round. The exact propose packet and brief were read. This file freezes two mechanisms for the distinct critic. It does not certify the rough-Chen preprint, claim a prime-pair lower bound, or declare a universal sieve obstruction.

**Verdict: incomplete for the original prime margin.** A repaired base application and a genuinely beyond-half signed Type II estimate on an actual suboperator are obtained below, relative to the named imported distribution statements. The exact source one-prime coefficient transfer fails its displayed vector test in a specified interval. A half-level correction is available. The proposed direct semiprime subtraction has a strictly negative coefficient even under an explicitly optimistic switched transfer. The Type II suboperator estimate does not supply the remaining prime-weight or full-residual inequality.

Assurance is a complete written derivation of the deductions, with imported analytic theorems identified, awaiting distinct-role review. It is not proof-assistant certification. Novelty is unverified. No numerical evaluation, source certificate execution, new retrieval, helper, supplementary inference, publication or external message was used.

## 1. Sources, notation and exact target

The pinned source-provenance.json identifies the inspected primary versions. I read rough-chen-v2.tex, Li's text and the actual Lemma 2.1/2.2 page 3 and 4 renders, and Lichtman's text and the Proposition 3.1/6.6 page 9 and 28 renders. Theorems are imported as stated, not inferred from the rough-Chen numerical certificate. The three inputs are Ratliff v2, Zenodo record 20377091; Li, arXiv:2405.05727v4; and Lichtman, arXiv:2309.08522v1.

Write
\[
 \mathcal X_N=2C_2\mathcal S_0(N)N/(\log N)^2,\quad
 C_2=\prod_{p>2}(1-(p-1)^{-2}),\quad
 \mathcal S_0(N)=\prod_{p\mid N,p>2}(p-1)/(p-2).
\]
This is the rough-Chen normalization. It is different from the cubic normalization \(M_N=2C_2\mathcal S_0(N)N/(3\log N)\).

For even \(N\), count primes \(p\) for which \(q=N-p>1\), with \(P^-(q)>N^\alpha\), \(1/4<\alpha<1/3\). Define \(R_\alpha,E_\alpha,H_\alpha\) by \(\Omega(q)=1,2,3\), respectively, counting a representation once, including squares and repeated prime factors. Since \(q<N\), four prime factors greater than \(N^\alpha\) are impossible. Thus, exactly,
\[
 U_\alpha=R_\alpha+E_\alpha+H_\alpha,\qquad
 F_\alpha=U_\alpha-E_\alpha,\qquad
 R_\alpha=F_\alpha-H_\alpha.                         \tag{1}
\]
The required sign is \(F_\alpha>H_\alpha\). A positive \(U_\alpha-H_\alpha\) does not establish it.

Exceptions involving primes dividing \(N\) are retained until bounded: if a prime divisor \(\ell\mid N\) divides \(N-p\), then \(p=\ell\). There are at most \(\omega(N)\) such representations. The excluded cofactor 1 costs at most one. Rough repeated-factor complements have count at most
\[
 \sum_{r>N^\alpha}N/r^2\ll N^{1-\alpha},              \tag{2}
\]
even on summing over all integer \(r\). Hence their deletion in an asymptotic coefficient costs \(o(\mathcal X_N)\); it does not change the exact identity (1). No multiplicity is silently removed.

## 2. Exact imported coefficient classes and repaired base application

Put \(\theta=7/32\), \(\beta=25/224\), \(\eta_0=249/448\), \(u_0=1/500\), and \(\mu_1=25/128\). For Goldbach-size residue \(a=N\), the one-coordinate level is
\[
 v(t)=\min\{(1+t)/2,\ 1-34t/39,\ 57/64-3t/2\}.       \tag{3}
\]
The three-coordinate level \(v(t_1,t_2,t_3)\) is exactly the maximum in Lichtman (6.4), with \(\alpha=1\) and \(\theta=7/32\). We use only its entries \(v(t_1+t_2)\), \(v(t_1)\), and
\[
 w=\psi\left(\min\left\{
 { (5-4\theta)-(3-4\theta)t_3\over8-6\theta},
 {5-\theta-3t_3\over8},1-2t_2\right\},{1+t_1\over2}\right), \tag{4}
\]
where \(\psi(x,y)=x1_{x\ge y}\). The source's strict-versus-weak gate has no effect below, because a positive level margin is retained.

Li Lemma 2.1 applies to the actual modified weights \(\widetilde\lambda_D^\pm(q)\) at the **total** modulus \(q=bc\). Its extracted vector must satisfy
\[
 (D_1,\ldots,D_r)\in\mathcal D_r^{\rm well}(D),\qquad
 D_1\cdots D_{j-1}D_j^2<D\quad(j\le r).              \tag{5}
\]
For \(r\ge3\), the residual is \(c\mid P(p_r)\), and the triple improvement additionally requires \(t_1\le\mu_1\). For \(r=2,1\), the explicit residual is \(c\mid P(N^u)\), with levels \(v(t_1,t_2,u)\), \(v(t_1,u,u)\). The exceptional \(r=0\) assertion is for \(u=u_0\) and level \(19101/32000\). It is not an assertion at arbitrary smoothness \(\beta\).

Li Lemma 2.2 gives the corresponding product-prime congruence error for the same total modified coefficients and vector restrictions. Its displayed prime boxes have exponents \(\epsilon_i\ge\epsilon>0\), \(\sum_i\epsilon_i=1\), and widths \(\Delta=1+(\log N)^{-B}\). An application outside those boxes must justify the endpoint/partition extension. In particular, its statement is not an arbitrary bilinear-coefficient theorem.

Lichtman Theorem 1.7 is different: triply well-factorable coefficients give level \(66/107-\epsilon\) for small residue, and \(153/256-\epsilon\) for \(|a|<x^{1+\epsilon}\). It cannot assign the small-residue level to \(a=N\), or assign triple factorability to modified linear-sieve weights. Proposition 6.6 instead obtains anatomy-dependent modified-weight estimates. These distinctions will matter in Section 5.

### 2.1 Complete anatomy floor, including the zero-, one- and two-factor cases

For \(0<t_3\le t_2\le t_1\le\beta\), one has
\[
 v(t_1,t_2,t_3)\ge\eta_0.                            \tag{6}
\]
If \(t_1+t_2\ge\beta\), put \(x=t_1+t_2\in[\beta,2\beta]\). All three entries of (3) are at least \(\eta_0\): the first at \(x=\beta\), the third at \(x=2\beta\), and the second strictly throughout that interval. If \(t_1+t_2<\beta\), then \(t_2,t_3<\beta/2\). In (4), the first two entries evaluated at \(t_3=\beta/2\), and the third at \(t_2=\beta/2\), are strictly larger than \(\eta_0\). Meanwhile \((1+t_1)/2<\eta_0\). Thus the gate opens and \(w>\eta_0\). This proves (6). Substituting \((t_1,t_2,u_0)\) or \((t_1,u_0,u_0)\) proves the missing-coordinate cases whenever the extracted coordinates are at least \(u_0\).

Here is the exact decomposition that repairs the source's informal zero-factor assertion. For each modulus in the modified lower support, with every prime factor below \(N^\beta\), extract its largest three primes if at least three exceed \(N^{u_0}\). Leave all smaller primes in \(c\); then \(c\mid P(p_3)\), exactly as in Li (i). **Do not** extract arbitrarily many primes and then add an unlicensed restriction \(P^+(c)\le N^{u_0}\) to that clause. If exactly two or one primes exceed \(N^{u_0}\), extract those and use Li (ii) or (iii), with \(u=u_0\). If none do, use the actual \(r=0,u=u_0\) clause. These cases are disjoint and exhaustive. Squarefree support gives uniqueness of the ordered extraction.

The support/vector construction of modified weights is imported from Lichtman Section 6.1, which says these weights inherit the well-factorable support and the same linear-sieve bounds. Use a fixed positive margin: take the working level \(D=N^{\eta_0-\sigma}\), and a finer fixed exponent mesh in the source's modified-vector construction. Every extracted vector inherits (5) from the support; the mesh and strict support margins cost less than \(\sigma/3\). There are finitely many cells, with a number depending on \(\sigma\), not \(N\). Equation (6), \(\beta<\mu_1\), and \(19101/32000>\eta_0\) verify all distribution inequalities with a positive margin. Thus summing Li's estimates over these cells is legitimate. The assertion is not based merely on divisors being smooth.

Consequently, with the standard lower linear-sieve function \(f\),
\[
 \liminf_{N\to\infty,\ 2\mid N}{S(\mathcal A_N,N^\beta)\over\mathcal X_N}
 \ge L_0:={e^{-\gamma}\over\beta}f(\eta_0/\beta).     \tag{7}
\]
Here \(\mathcal A_N=\{N-p:p\text{ prime},\ 1<N-p<N\}\). The local density is \(g_N(\ell)=1/(\ell-1)\) for odd \(\ell\nmid N\), zero for \(\ell\mid N\), with the exceptions above. Multiplication of these local factors gives
\(V_N(N^\beta)\sim2e^{-\gamma}C_2\mathcal S_0(N)/(\beta\log N)\), yielding (7). First fix \(\sigma>0\), apply the distribution and sieve theorem, and then let \(\sigma\downarrow0\) using continuity of \(f\). No unproved theorem with an \(N\)-dependent vanishing epsilon is used.

For the corresponding **upper** modified support at total level \(N^{\eta_0-\sigma}\), its largest extracted exponent is at most \(\eta_0/3+o(1)=83/448+o(1)<\mu_1\). If \(t_1\ge\beta\), then \(v(t_1)=(1+t_1)/2\ge\eta_0\). If \(t_1<\beta\), (4) gives \(w\ge\eta_0\): its second entry at \(t_3=\beta\) is exactly \(\eta_0\), and the other entries are larger. The same extraction with \(u_0\) handles \(r=0,1,2\). This verifies the anatomy and residual-smoothness portion of Li's switched upper application in its **stated prime boxes**. It does not silently prove an arbitrary partition extension, or a fixed-factor coefficient identity.

## 3. Mechanism 1: fixed-prime transport and actual semiprime subtraction

The exact Buchstab identity for \(U_\alpha\) is
\[
 U_\alpha=S(\mathcal A_N,N^\beta)
       -\sum_{N^\beta\le\ell<N^\alpha}S((\mathcal A_N)_\ell,\ell), \tag{8}
\]
with strict cutoff conventions matched at the prime boundaries. Changing \(<\) to \(\le\) costs only boundary representations, which must be retained or bounded when a cutoff is a prime.

For \(\ell=N^{t+o(1)}\), an upper residual sieve has actual coefficient
\[
 A_t(q)=\sum_{\substack{\ell d=q\; ;\ \ell\ {m prime}\ {m in\ the\ }t{\rm\ cell}}}
       1_{d\mid P(N^\rho)}\widetilde\lambda^+_{N^{\eta(t)-t}}(d),
 \qquad \rho\le t.                                  \tag{9}
\]
It is not, by notation alone, \(\widetilde\lambda^\pm_{N^{\eta(t)}}(q)\). Li's extracted \(\ell\) is a prime factor of the **modulus**, distinct from the prime factors of the switched product sequence. Since it is the largest factor in (9), (5) requires
\[
 2t<\eta(t).                                        \tag{10}
\]
On the source's claimed decreasing branch \(\eta(t)=57/64-3t/2\), (10) is equivalent to
\[
 t<57/224.                                          \tag{11}
\]
The claimed branch up to \(\alpha\) near 0.2665 exceeds this endpoint. Neither the three-coordinate maximum nor the small-residue theorem repairs a vector already failing (5). Equality requires an additional fixed margin. This disproves that particular direct invocation for those vectors; it does not refute every possible analytic treatment of the branch.

There is a concrete coefficient repair below this threshold for the **ordinary** weights, whose definition is printed in Lichtman Section 6.1. If \(d\) is squarefree, \(P^+(d)<\ell\), and \(\ell^2<D\), then
\[
 \lambda_D^-(\ell d)=-\lambda_{D/\ell}^+(d).          \tag{12}
\]
Indeed, place \(\ell\) first in the decreasing prime list. The extra lower-support condition is \(\ell^2<D\). Its even indexed conditions become exactly the odd indexed upper-support conditions for \(d\), at level \(D/\ell\); the Mobius signs differ by minus one. This proves (12), including \(d=1\). If \(\ell^2\ge D\), the left side is zero even at \(d=1\), while the right side is \(-1\). Thus the extension across (10) is genuinely false for these ordinary coefficients. The pinned texts do not state the corresponding exact identity for the modified weights. Their well-factorability alone does not prove it.

A legitimate alternative, valid also above (11), is to cap the **total** branch modulus at \(N^{1/2-\sigma}\) and use ordinary upper weights at residual level \(N^{1/2-\sigma}/\ell\). The classical Bombieri-Vinogradov statement is printed as Lichtman (1.2). For each total squarefree modulus, the number of candidate prime divisors \(\ell\ge N^\beta\) is at most \((1/2)/\beta+O(1)\). The aggregated coefficient is therefore uniformly bounded. BV's absolute error sum at the fixed prime endpoint \(N\) controls (9) with these ordinary weights, without (5), triple factorability, or a modified-weight identity. The exact residual prime threshold may be weakened from \(\ell\) to \(N^\rho\) for an upper bound, with \(\rho=\min\{t,(1/2-\sigma-t)/3\}\). Coprimality exceptions obey (2) and the prime-divisor-of-\(N\) bound above. A cutoff that equals a prime contributes at most \(O(N^{1-\beta})\) boundary representations, which is negligible here.

This gives the following **proved repaired lower estimate**, relative to BV and (7):
\[
 \liminf{U_\alpha\over\mathcal X_N}\ge L_0-H_{1/2}(\alpha),\quad
 H_{1/2}(\alpha)=2e^{-\gamma}\int_3^{87/25}F(s)\,ds
                 +4\log{3\alpha\over1/2-\alpha}.     \tag{13}
\]
To derive it, for \(\beta\le t\le1/8\) use \(\rho=t\) and integrate
\(e^{-\gamma}t^{-2}F((1/2-t)/t)\); the substitution \(s=1/(2t)-1\) gives the first term. For \(1/8\le t\le\alpha\), use \(\rho=(1/2-t)/3\), \(F(3)=2e^\gamma/3\), and integrate \(2/[t(1/2-t)]\). Its lower endpoint contributes the factor 3. As with (7), take fixed positive margins first and then a continuity limit. This correction is weaker than the source formula. It preserves the actual coefficients rather than pretending that (9) is a total modified weight.

The precise price of capping a purported valid source branch at half level on any interval \([a,b]\subset(57/224,\alpha]\) is the nonnegative loss
\[
 \Delta H[a,b]=\int_a^b\left\{
 {2\over t(1/2-t)}-{2\over t(57/64-5t/2)}\right\}dt, \tag{14}
\]
where the second integrand is retained only when its claimed total level exceeds \(1/2\), namely \(t<25/96\). For \(t\ge25/96\), ordinary BV already covers the smaller source level, so there is no need to enlarge that loss. Formula (14) is an exact repair cost, not a claim that the uncorrected neighboring modified coefficients are already justified.

### 3.1 Carrying out the semiprime subtraction, with its actual failed sign

The ordered-once semiprime harmonic mass and triple harmonic mass are
\[
 B_2(\alpha)=\int_\alpha^{1/2}{dt\over t(1-t)}
            =\log{1-\alpha\over\alpha},\qquad
 B_3(\alpha)=\int_\alpha^{1/3}{\log((1-2t)/t)\over t(1-t)}dt. \tag{15}
\]
The first follows by writing a semiprime as \(rs\), \(r\le s\), and summing \(N/(r\log(N/r))\) over \(r\) using the prime number theorem. The lower endpoint \(s\ge r\) changes the raw product count only by \(O(N/(\log N)^2)\), one logarithm below its \(N/\log N\) scale. For triples, integrate \(dv/[v(1-t-v)]\) from \(t\) to \((1-t)/2\), giving the displayed inner logarithm. Repeated factors are included in the exact counts and have the error (2). These are harmonic masses, not asymptotics for the correlated prime complements.

Try switching both contaminations and upper-sieving the complementary prime, at total level \(\eta_0\) and threshold \(N^{1/2}\). The linear-sieve parameter is \(2\eta_0<3\). If the required switched boxes and their endpoint/partition extension are justified for the exact upper modified coefficients, this procedure would give
\[
 E_\alpha\le(2B_2(\alpha)/\eta_0+o(1))\mathcal X_N,\quad
 H_\alpha\le(2B_3(\alpha)/\eta_0+o(1))\mathcal X_N.    \tag{16}
\]
The constant is forced by \(F(s)=2e^\gamma/s\) and the same local product; it is not a prime-pair asymptotic. Li's stated \(k=2\) and \(k=3\) boxes are both eligible after Section 2's anatomy check. A passage from those boxes to all \(rs<N\) or \(rst<N\), with residue still \(N\), is an extra transport step, not silently supplied by writing “smoothing.” I do not promote the full (16) to an established bound on the basis of the displayed lemmas alone.

Even grant (16) and, optimistically, grant the source's stronger uncorrected branch bound \(H_{\rm src}\). Then the actual prospective prime margin would be
\[
 {R_\alpha\over\mathcal X_N}\ \ge\
 L_0-H_{\rm src}(\alpha)-{2\over\eta_0}B_2(\alpha)
                    -{2\over\eta_0}B_3(\alpha)+o(1). \tag{17}
\]
This is the attempted semiprime subtraction. Its right-side coefficient is strictly negative for every \(1/4<\alpha<1/3\), by the following exact inequalities, with no numerical certificate:

* \(f(s)\le1\), \(\gamma>1/2\), and \(e^{1/2}>3/2\) give \(L_0<448/75\).
* On the first source branch the upper integrand is at least \(4/[t(1-t)]\), because \(F(s)\ge2e^\gamma/s\) in its stated \(3\le s<4\) range. On its remaining branches the integrand is exactly \(2/[t(\eta(t)-t)]\), and \(\eta(t)\le(1+t)/2\), so the same lower bound holds. Hence
  \(H_{\rm src}(\alpha)\ge4\log(\alpha(1-\beta)/(\beta(1-\alpha)))\ge4\log(199/75)\).
* \(B_2(\alpha)>\log2\), \(B_3(\alpha)\ge0\), and \(\log x>2(x-1)/(x+1)\) for \(x>1\), give
\[
 H_{\rm src}+{2\over\eta_0}B_2
 >{496\over137}+{1792\over747}
 ={448\over75}+{353328\over7675425}.                 \tag{18}
\]

Thus even this optimistic candidate has coefficient less than \(-353328/7675425\). The failed requirement is the strictly positive sign of the **whole** coefficient in (17), including the negative semiprime term. An improved exact-P3 constant by itself cannot repair this calculation. This is only a failure of the displayed direct linear-sieve subtraction; it is not a no-go for all stronger distribution, correlated or non-linear weights, or Goldbach itself.

## 4. Mechanism 2: the actual cubic short-prime-cofactor operator

Retain the brief's exact definitions
\[
 I=(N/3,2N/3],\quad y=N^{1/6},\quad z=(\log N)^4,
 \quad W=\operatorname{rad}\left(N\prod_{p\le z}p\right),\quad
 \kappa=W/\varphi(W),\quad D=N^{1/2}(\log N)^{-B},
\]
\[
 u(n)=\theta(N-n)-\kappa1_{(N-n,W)=1}
             -\theta(N/2)1_{n=N/2},\quad
 \Phi(t)=1-3t^2+2t^3,
\]
\[
 H_{3,D}=\sum_{k\ge1}\sum_{h>D,\ kh\in I}
       \mu(h)\Phi\left({\log h_{>y}\over\log(kh)}\right)u(kh).
                                                               \tag{19}
\]
No cofactor, including 1, is dropped from (19). Define one suboperator by restricting to \(k\) prime, \(y<k\le N^{1/3-\epsilon}\), and \(P^-(h)>y\). On it, \(\mu(h)\ne0\) implies \(h_{>y}=h\), so its signed coefficient is exactly
\[
 a(k,h)=1_{k\ {m prime},\ y<k\le N^{1/3-\epsilon}}
        1_{h>D,\ P^-(h)>y}\mu(h)
        \Phi\left({\log h\over\log(kh)}\right).       \tag{20}
\]
It is a literal piece of (19). Common prime factors of \(k\) and \(h\), hence repeated factors of \(kh\), are allowed. This definition does not assume the rest of \(C_D\) has been transported.

### 4.1 Actual signed beyond-half estimate

Fix \(0<\epsilon<1/2000\), \(A>0\), and
\[
 Q=N^{153/256-100\epsilon}.
\]
For **any genuinely triply well-factorable sequence** \(\lambda_d\) of level \(Q\), supported on \((d,N)=1\), one has
\[
 \left|\sum_{d\le Q}\lambda_d
   \sum_{k,h:\ kh\in I}a(k,h)
       \left(1_{kh\equiv N\pmod d}
             -{1_{(kh,d)=1}\over\varphi(d)}\right)\right|
 \ll_{A,\epsilon,B} {N\over(\log N)^A}.              \tag{21}
\]
This is a signed arithmetic estimate for the actual coefficient (20), not a comparison of sieve constants. It follows from Lichtman Proposition 3.1, as follows.

Set its product scale to \(x=N/3\), residue \(a=N\), and residue-growth exponent to \(1+\epsilon\). For large \(N\), \(N<x^{1+\epsilon}\). Split \(k,h\) into dyadic rectangles \(K<k\le2K\), \(H<h\le2H\), intersected with \(kh\in[x,2x]\); then \(KH\asymp x\). The small factor is \(k\), with
\[
 x^\epsilon<K\ll N^{1/3-\epsilon}<x^{1/3+\epsilon}.
\]
Its coefficient is the prime indicator on the dyadic interval, so it satisfies the imported Siegel-Walfisz condition (Lichtman Definition 2.1), and its primes exceed \(y>x^{1/(\log\log x)^3}\). The large-factor sequence
\(\beta_h=\mu(h)1_{h>D,P^-(h)>y}\) is 1-bounded; that sequence is not required to satisfy Siegel-Walfisz. Thus no unproved SW assertion for the combined \(\mu(h)\Phi\) coefficient is made. The level in Proposition 3.1 is
\[
 \min\left\{66/107,\ (5-(1+\epsilon)7/32)/8\right\}-50\epsilon
 =153/256-(50+7/256)\epsilon.
\]
Our exponent has a fixed spare margin and absorbs the constant change from \(N\) to \(x\). It is greater than \(1/2\) for the specified epsilon range. The modulus coefficients meet the theorem's exact triple-factorability hypothesis by assumption, rather than by a claim about arbitrary Mobius or modified sieve coefficients.

Initially apply the proposition without \(\Phi\). On a rectangle the smooth function \(\Phi(\log h/\log(kh))\), and its first and mixed derivatives multiplied by \(K,H,KH\), are uniformly bounded. Two-variable partial summation therefore inserts it at bounded cost. The threshold \(h>D\) is part of the large sequence, and the product interval is explicitly allowed by the proposition. There are \(O((\log N)^2)\) rectangles, absorbed by first asking the theorem for \(A+3\). This proves (21), with every sign and coprimality factor retained. Restricting an already triply well-factorable sequence to \((d,N)=1\) preserves that property, because the coprimality indicator factors over each convolution factor in its definition.

The claim is limited to (20); it neither includes all cofactor sizes nor estimates the original wheel model. The full \(k=1\) contribution is still present in (19): it vanishes on the rough part since \(\Phi(1)=0\), but can be nonzero on the nonrough part. No such term is discarded.

## 5. The first failed transport back to the signed prime weight

To turn (21) into a lower bound for the prime part of (19), one needs actual complementary-prime sieve coefficients to which (21) applies, with the correct sign orientation. On (20), \(\Phi\ge0\), but \(\mu(h)\) has both signs. A lower estimate therefore needs a prime minorant on \(\mu(h)=+1\) and a prime majorant on \(\mu(h)=-1\). Multiplying a single majorant by \(\mu(h)\) is invalid. The separate parity indicators are admissible large-factor sequences in Proposition 3.1; this observation does not manufacture admissible prime-sieve weights.

Here the exact coefficient obstacle can be proved, not merely suspected. Put \(Z=\sqrt{2N/3}\). Since \(N-kh\in[N/3,2N/3)\), for large \(N\) the exact prime indicator is
\[
 1_{N-kh\ {m prime}}=
       \sum_{\substack{d\mid N-kh\ ;\ d\mid\prod_{r\le Z}r}}\mu(d). \tag{22}
\]
Every composite in the interval has a prime factor at most \(Z\), while every prime in the interval exceeds \(Z\); the complete divisor sum is therefore respectively 0 and 1. The exact expansion has moduli up to \(2N/3\), beyond \(Q\). Truncating to \(d\le Q\) produces the coefficient
\[
 b_d=\mu(d)1_{d\le Q}1_{P^+(d)\le Z},               \tag{23}
\]
which is **not triply well-factorable of level \(Q\)**. To prove this, choose any prime \(r\) with \(Q^{1/3}<r\le2Q^{1/3}\); Bertrand's theorem provides one for large \(Q\), and \(2Q^{1/3}<\min(Q,Z)\). Then \(b_r=-1\). For the balanced split \(Q=Q^{1/3}Q^{1/3}Q^{1/3}\), every convolution of three sequences supported up to \(Q^{1/3}\) has coefficient 0 at the prime \(r\), since a factorization of a prime must put the prime into one factor. This contradiction proves the assertion. Coprimality to \(N\) can also be respected: the prime number theorem gives \(\gg Q^{1/3}/\log N\) primes in that interval, whereas \(N\) has at most \(3\log N/\log Q=O_\epsilon(1)\) prime factors exceeding \(Q^{1/3}\). Hence some such prime does not divide \(N\).

Thus neither (22) nor its naive truncation is licensed by (21). The modified linear-sieve weights are not generally triply well-factorable either (Lichtman explicitly says so on page 6); one would need a new factorization/decomposition argument for the actual weights or a sharper theorem for their class. Replacing them by another class without an exact signed majorant/minorant transport would change the problem.

The first unresolved signed conclusion is a bound of the form
\[
 \sum_{k,h:\ kh\in I}a(k,h)
 \left[\theta(N-kh)-\kappa1_{(N-kh,W)=1}
                   -\theta(N/2)1_{kh=N/2}\right]
       \ge -(c+o(1))M_N,                             \tag{24}
\]
with a useful explicit fixed \(c\), accompanied by bounds for all remaining cofactors and nonrough products. Equation (21) does not prove (24). Even (24) alone would not prove the required
\[
 H_{3,D}\ge-(3/4-\delta+o(1))M_N\quad(\delta>0).      \tag{25}
\]
The earlier cubic residual partition in cubic-signed-20261029/revision.md remains intact: nonrough, even rough, and outer odd residuals are not set to zero. The wheel density and the correction atom in (24) are retained exactly, rather than replaced by \(1/\varphi(d)\).

## 6. Frozen handoff and smallest decisive checks

The new deductions offered for review are (6), the repaired source-to-base application (7), the ordinary concatenation identity and its precise vector failure (10)-(12), the actual BV repair (13)-(14), the strict negative sign for the attempted semiprime subtraction (17)-(18), and the signed stronger-distribution suboperator estimate (21) with its exact failure to transport through (22)-(23). These use only the two mechanisms above. None establishes Goldbach or the cubic fixed gap.

The next proof obligation within mechanism 1 is an exact theorem for (9), including its shifted coefficients and any fixed factors outside (5), plus a semiprime estimate stronger than the direct subtraction tested here. For mechanism 2 it is a valid sign-aware complementary-prime majorant/minorant transport for the literal coefficient (20), in an actually covered modulus class, followed by all omitted-sector bounds. A smallest falsifier for a claimed triple-factorability transport is the single prime coefficient in the balanced splitting argument. A smallest falsifier for extending (12) past (10) is \(d=1\).

The independent critic should particularly inspect the exact r=0/1/2/3 extraction in Section 2, the modified versus ordinary coefficient distinction, the factor-count bound in the BV correction, and the variable roles and uniformity in the Type II use. No claim is made that the preprint's entire theorem is refuted; the identified source application and the present signed mechanisms have the precise limitations recorded here.
