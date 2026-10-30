# BALANCED023: revision after independent criticism

29 October 2026. Actual original-author revise stage, round 1, stage cost 3 declared proxy units.

**Final round verdict: incomplete.** The critic supports the elementary identities, prime-power error lemma, exact norm equivalence and semiprime accounting. All three substantive gaps remain open: the genuine second-prime-weighted discrepancy with its wheel reference terms, the centered quotient-Möbius norm, and the weighted branch and prefix transfer to the long semiprime contribution. No useful signed covariance bound, weighted semiprime margin, positive Goldbach gap or breakthrough is proved. The failure of these estimates does not refute the eventual dispersion assertion. The user's full Goldbach objective remains incomplete.

This revision adds no mechanism, source, helper or research round. It records the criticism, preserves the supported deductions and restates the semiprime formulas without the frozen proposal's formatting corruption.

## 1. Frozen inputs, correction and assurance

The actual populated revise packet is .runs/goldbach-balanced-023-manual-20261029/packets/revise.json, SHA256 af529bd967f2b2cd523eb0ef82dbb0810e24f4f0f13f80142ee6ffc7a9091e8c. Its upstream is the actual critic result, not an empty handoff. The independent review is review.md, SHA256 4d44ab372a6a71fbeb2ec129026715ed380f51421ae9f5338720df44f8198ddd; challenge-result.json has SHA256 46a8657cc18b895694c5e6c11c1c4a589dbaef3ca4ca22195787f21a307cc2b8.

The proposal remains frozen: statement.md, SHA256 ee40705ea259c3ff2593ddf26d7f3f5d483c0cae3493fd6561fbe4cf1c893fc8, and propose-result.json, SHA256 ccf8d3094b012f84a4fed652d802c3105bf99f5b252342a985f45525ff5419e3. The statement contains six bare carriage-return bytes in Section4 where prime markers were intended. This is a formatting defect, not a mathematical counterexample. The clean full formulas in Section5 below use the explicit marker \(\text{prime}\). The frozen file is not modified.

Assurance is a complete human-readable argument for the elementary claims, with distinct critic reconstruction. There is no formal proof certificate. The actual local source passages and rendered formulas were inspected during propose and challenge as recorded there. The only imported distribution theorem remains Koukoulopoulos, preliminary book, printed277/PDF288, exact (26.1), with its stated range. Neither source Hypothesis8.2 nor the stronger sufficient dispersion test is an assumption. No CHEN024 result, stronger distribution hypothesis or other concurrent work is imported. Novelty is unverified.

## 2. Exact target and supported structure retained

All asymptotic statements in this revision are uniform over sufficiently large even \(N\); \(A>0\) and \(B>0\), when used, are fixed. Put
\[
 L=\log N,\quad I=(N/3,2N/3],\quad y=N^{1/6},\quad z=L^4,
 \quad W=\operatorname{rad}\left(N\prod_{\ell\le z}\ell\right),
 \quad\kappa=W/\varphi(W),\quad
 \mathcal Q=(N^{11/24},N^{13/24}].
\]
The product indexed by \(\ell\) is over primes. Let
\[
 \begin{split}
 u(n)&=\theta(N-n)-\kappa1_{(N-n,W)=1}
                   -\theta(N/2)1_{n=N/2},\\
 \alpha_2(r)&=1_{P^-(r)>y,\ \Omega(r)=2},\\
 \beta(r,q)&=1_{rq\in I}\bigl(\alpha_2(r)
                       +1_{r\text{ prime},\ r\le q}\bigr),\\
 F(q)&=\sum_r\beta(r,q)u(rq),\\
 D_{\mathcal Q}&=\sum_{q\in\mathcal Q\cap\mathbb N}q|F(q)|^2,\qquad
 M_N=\frac{\mathfrak S(N)N}{3L}.
 \end{split}                                                    \tag{R1}
\]
Here \(\theta(m)=\log m\) for prime \(m\), zero otherwise; \(\mathfrak S(N)\) is the conventional binary singular series of the brief, with \(\mathfrak S(N)\gg1\). The unproved target is \(D_{\mathcal Q}=o(M_N^2)\). It would imply the unweighted combined pilot \(T_{\mathcal Q}=o(M_N)\) by weighted Cauchy and the bounded reciprocal-prime sum on this exponent interval. No converse or Goldbach implication is proved.

Every supported \(r>(1/3)N^{11/24}>y\) and \(q>1\), so \(rq\) is composite. The atom could be nonzero only if \(rq=N/2\) were prime; hence it vanishes on this support. If \((rq,N)>1\), the model vanishes. A reflected prime \(m=N-rq\) would be an odd prime divisor of even \(N\) with \(N/3\le m<2N/3\); thus \(N/m\) would be an even integer at most three, hence two. This again makes \(rq=m\) prime, a contradiction. Such rows therefore vanish exactly. Every surviving \(r\) is coprime to \(N\), is \(y\)-rough, and so is coprime to the full actual wheel \(W\).

For branch \(a=2\) use \(b_2(r)=\alpha_2(r)\) and \(J_r^2=\mathcal Q\cap(N/(3r),2N/(3r)]\). For branch \(a=1\) use \(b_1(r)=1_{r\text{ prime}}\) and \(J_r^1=J_r^2\cap[r,\infty)\). Put \(K_{rs}^{ab}=J_r^a\cap J_s^b\), \(a_r(q)=\theta(N-rq)\), \(\chi_r(q)=1_{(N-rq,W)=1}\). The exact off-diagonal is
\[
 \sum_{a,b\in\{1,2\}}\sum_{r\ne s}b_a(r)b_b(s)
 \sum_{q\in K_{rs}^{ab}\cap\mathbb N}q
 [a_ra_s-\kappa a_r\chi_s-\kappa\chi_ra_s+\kappa^2\chi_r\chi_s].
                                                               \tag{R2}
\]
Both branch cross terms, repeated factors and every coupled endpoint remain. The supported negligible diagonal \(O(N^{37/24}L^8)\) does not estimate (R2).

For live \(r,s\), the exact integer-residue normalized wheel factor is
\[
 \prod_{\substack{\ell\mid W\\\ell\mid N(s-r)}}\frac{\ell}{\ell-1}
 \prod_{\substack{\ell\mid W\\\ell\nmid N(s-r)}}
                    \left(1-\frac1{(\ell-1)^2}\right).             \tag{R3}
\]
At one prime the normalized model covariance is \(1/(\ell-1)\) for coincident roots and \(-1/(\ell-1)^2\) for distinct roots. This follows by counting the one or two forbidden residues \(Nr^{-1},Ns^{-1}\); their equality is equivalent to \(\ell\mid N(s-r)\). The global centered wheel covariance is the product in (R3) minus one, not the product of the single-prime covariances. Under unit residues the joint survival probability is one if \(\ell\mid N\), and \(1-\nu_\ell/(\ell-1)\) otherwise, instead of \(1-\nu_\ell/\ell\). These finite CRT identities supply neither a finite-interval wheel asymptotic nor a genuine prime-prime correlation theorem. No prime-q measure is assigned to the integer-q enlargement.

## 3. Critic finding 1: weighted BV and reference terms remain unproved

**Accepted, high severity; unverified arithmetic obligation.** Mechanism1 gives exactly
\[
 s m_1-r m_2=N(s-r),\qquad m_1\equiv N\pmod r,\qquad
 q=(N-m_1)/r\in K_{rs}^{ab}.                                  \tag{R4}
\]
The full modulus \(r\) is retained. In particular, replacing it by \(r/(r,s)\) would add indices. The transformed prime-prime term retains
\[
 \theta(m_1)\,
 \theta\left(\frac{s m_1-N(s-r)}r\right)
\]
with the actual \(q\) weight and coupled support. The second prime has not been removed by switching.

For an explicitly covered dyadic interval \(X<q\le2X\), all relevant \(r,s\) are \(O(R)\), \(R=N/X\). Require their entire constant multiple of \(R\) to be at most \(\sqrt N/L^{A+3}\). Imported BV, after partial summation, gives \(\sum_r\Delta(r)\ll_A N/L^A\) for the maximal reduced-class \(\theta\)-discrepancy. Applied to the actual remaining sequence
\[
 f_s(q)=q\,[\theta(N-sq)-\kappa\chi_s(q)],
\]
discrete Abel summation bounds each progression error by
\[
 O\bigl((\|f_s\|_\infty+\operatorname{Var}f_s)
                              (\Delta(r)+r/\varphi(r))\bigr).     \tag{R5}
\]
The available bounds are \(\|f_s\|_\infty\ll XL^4\) and \(\operatorname{Var}f_s\ll X^2L^4\). Summing on the actual branch supports, and bounding their zero-one coefficients by one only at this explicit estimation step, gives
\[
 O\left(X^2R L^4\left(\frac N{L^A}+RL^4\right)\right)
       =O\left(\frac{N^2X}{L^{A-4}}+N^2L^8\right).                \tag{R6}
\]
The critic independently checked this bound. It is an insufficient upper bound, not an assertion that the actual discrepancy is that large. Fixed \(A\) cannot make this available expression \(o(N^2/L^2)\), and the complete support also permits \(r\) up to \((2/3)N^{13/24}\), above the imported cutoff.

The gap consists of two linked tasks: a negligible estimate for the genuine second-prime-weighted discrepancy on its exact supports, and a matching evaluation of the correctly centered finite-interval wheel reference terms. Proving only one, or computing complete-period factors (R3), does not finish this route. Smooth partial summation weights cannot replace \(f_s\); uniform prime counts in an unweighted progression do not bound this additional arithmetic weight. No repair of either task is supplied by this revision.

## 4. Critic finding 2: retain the prime-power equivalence, leave the Möbius norm open

**Accepted, high severity; unverified cancellation obligation.** Mechanism2 has a supported elementary lemma, which is preserved with its exact two-way conclusion. Let
\[
 F_\Lambda(q)=\sum_r\beta(r,q)
       [\Lambda(N-rq)-\kappa\chi_r(q)],\qquad
 E(q)=F_\Lambda(q)-F(q)\ge0.
\]
Then
\[
 \sum_{q\in\mathcal Q\cap\mathbb N}E(q)\ll\sqrt N L^2,\qquad
 \sum_{q\in\mathcal Q\cap\mathbb N}qE(q)^2
                      \ll N^{3/2}L^3=o(M_N^2).                 \tag{R7}
\]
Here is the complete counting argument. \(\Lambda-\theta\) is nonnegative, at most \(L\), and supported on proper prime powers \(p^k\), \(k\ge2\). There are \(O(\sqrt N L)\) such integers below \(N\), using \(N^{1/k}\le\sqrt N\) for at most \(L/\log2\) exponents. For each \(n=N-p^k\in I\), its part supported on primes greater than \(y\) has at most five prime-factor slots with multiplicity: six would have product greater than \(y^6=N>n\). Every supported \(r\mid n\) is obtained by choosing one or two of those slots, so there are at most \(5+\binom52=15\), and certainly at most twenty, possibilities. This overcount includes repeated factors. Each such \(r\) determines \(q=n/r\). This proves the first bound. The pointwise bound \(E(q)\ll (N/q)L\) now gives
\[
 \sum_q qE(q)^2
       \le \bigl(\sup_q qE(q)\bigr)\sum_q E(q)
       \ll NL\sqrt N L^2.
\]
Since \(M_N\gg N/L\), both error scales are negligible as claimed.

For the norm \(\|G\|_q^2=\sum_{q\in\mathcal Q\cap\mathbb N}q|G(q)|^2\), the reverse triangle inequality gives
\[
 \bigl|\|F_\Lambda\|_q-\|F\|_q\bigr|
       \le\|E\|_q=O(N^{3/4}L^{3/2})=o(M_N).
\]
Consequently, exactly and in both directions,
\[
 D_{\mathcal Q}=o(M_N^2)
 \quad\Longleftrightarrow\quad
 \sum_{q\in\mathcal Q\cap\mathbb N}q|F_\Lambda(q)|^2=o(M_N^2).
                                                               \tag{R8}
\]
The equivalence does not establish either side. It removes only proper prime powers, not the surviving prime correlation.

With \(H=N^{1/24}\), \(m=N-rq\), let \(S_H(q)\) and \(V_H(q)\) be the divisor sums over \(d\mid m\) with \(d\le H\) and \(d>H\), respectively, of \(\beta(r,q)\mu(d)\log(m/d)\), summed also over \(r\); let \(B_0(q)=\sum_r\beta(r,q)\chi_r(q)\). Elementary Möbius inversion gives
\[
 F_\Lambda(q)=S_H(q)+V_H(q)-\kappa B_0(q),                        \tag{R9}
\]
and exactly
\[
 V_H(q)=\sum_{k<2N/(3H)}\log k
   \sum_{\substack{r:\ k\mid N-rq\\(N-rq)/k>H}}
       \beta(r,q)\mu\left(\frac{N-rq}k\right).                  \tag{R10}
\]
The strict upper bound uses \(N-rq<2N/3\); the other reflected endpoint remains in \(\beta\). Integer \(k=1\) is present with its true zero factor \(\log1\); no additional coprimality or prime restriction is made. This algebra is supported, but the necessary estimate
\[
 \sum_{q\in\mathcal Q\cap\mathbb N}q
   |V_H(q)-(\kappa B_0(q)-S_H(q))|^2=o(M_N^2)                  \tag{R11}
\]
remains unproved. It is a reformulation of the target after (R8), not a second signed gain. Neither deleting the long sum nor bounding its Möbius coefficients absolutely establishes (R11). The current prime-count BV input supplies no assertion about the actual quotient-Möbius sequence in (R10).

## 5. Critic finding 3 and the clean complete semiprime formulas

**Accepted, medium severity; unverified transfer obligation.** The following formulas correct only the six damaged prime markers in the frozen statement and preserve the independently checked mathematical content.

Fix \(B>0\), put \(D=\sqrt N/L^B\), and define
\[
 \Phi(t)=1-3t^2+2t^3,\qquad
 h_{>y}=\prod_{\substack{\ell\mid h\\\ell>y}}\ell,\qquad
 C_D(n)=\sum_{\substack{h\mid n\\h>D}}\mu(h)
              \Phi\left(\frac{\log h_{>y}}{\log n}\right).
                                                               \tag{R12}
\]
The actual full long operator is \(\sum_{n\in I}u(n)C_D(n)\). Eventually \(D<\sqrt{N/3}\). Thus whenever \(n=pq\in I\), with \(p\le q\) prime, \(q\ge\sqrt n>D\).

For distinct rough primes \(y<p<q\), set \(t=\log p/\log(pq)\). Among \(1,p,q,pq\), the first is below \(D\), \(q>D\), and \(pq\) has \(\Phi(1)=0\). Direct expansion gives \(\Phi(t)+\Phi(1-t)=1\), so the exact coefficient is
\[
 C_D(pq)=-1_{p>D}\Phi(t)-\Phi(1-t)
   =\begin{cases}
       -(3t^2-2t^3),&p\le D,\\
       -1,&p>D.
     \end{cases}                                               \tag{R13}
\]
In particular \(p=D\) belongs to the first case because the long cutoff is \(h>D\). For the square \(n=p^2\in I\), roughness and \(p>D\) give instead
\[
 C_D(p^2)=-\Phi(1/2)=-\tfrac12.                                \tag{R14}
\]
Indeed the divisor \(p^2\) has Möbius value zero, so there is only one contributing prime divisor \(p\), with no doubling. This is the square coefficient of the actual full long operator; a squarefree-only residual would have a separate squareful error ledger.

Define
\[
 w_D(p,q)=
 \begin{cases}
  3\left(\dfrac{\log p}{\log(pq)}\right)^2
       -2\left(\dfrac{\log p}{\log(pq)}\right)^3,&p<q,\ p\le D,\\
  1,&p<q,\ p>D,\\
  \tfrac12,&p=q.
 \end{cases}                                                   \tag{R15}
\]
For prime \(q\in\mathcal Q\), \(p\le q\), \(pq\in I\), the lower product bound forces \(p>(1/3)N^{11/24}>y\). Unique ordering, including the square once, therefore gives the full balanced semiprime contribution
\[
 H_{2,\mathcal Q}
   =-\sum_{\substack{q\in\mathcal Q\\q\text{ prime}}}
        \sum_{\substack{p\le q\\p\text{ prime}\\pq\in I}}
                          w_D(p,q)u(pq).                       \tag{R16}
\]
For each integer \(q\in\mathcal Q\), use exactly the formula (R15) to define
\[
 F_{2,w}(q)=
        \sum_{\substack{p\le q\\p\text{ prime}\\pq\in I}}
                          w_D(p,q)u(pq).                       \tag{R17}
\]
For composite integer \(q\), this is a specified coefficient extension; it asserts no semiprime support or Möbius coefficient identity for the resulting product. Weighted Cauchy gives
\[
 |H_{2,\mathcal Q}|^2
 \le
 \left(\sum_{\substack{q\in\mathcal Q\\q\text{ prime}}}\frac1q\right)
 \sum_{\substack{q\in\mathcal Q\\q\text{ prime}}}
                         q|F_{2,w}(q)|^2
 \le
 \left(\sum_{\substack{q\in\mathcal Q\\q\text{ prime}}}\frac1q\right)
 \sum_{q\in\mathcal Q\cap\mathbb N}q|F_{2,w}(q)|^2.               \tag{R18}
\]
All six prime markers in the two outer and inner restrictions of (R16), the inner restriction of (R17), and the three prime restrictions in (R18) are written with the explicit text command. The exact Cauchy weight in the enlarged energy is \(q\), not a prime-density weight.

For fixed \(q\), on the distinct-prime part the coefficient is \(g(t)=3t^2-2t^3\) below \(D\), and one above \(D\). Below the cutoff,
\[
 \frac{d}{dp}g\left(\frac{\log p}{\log(pq)}\right)
       =\frac{6t(1-t)\log q}{p(\log(pq))^2};
\]
at \(D\) its right jump is \(\Phi(t_D)\). Thus discrete partial summation needs the genuine prime-branch prefix sums
\[
 S_q(x)=
   \sum_{\substack{p\le x,\ p<q\\p\text{ prime}\\pq\in I}}u(pq),
                                                               \tag{R19}
\]
their cutoff values and the square atom with coefficient \(1/2\). An estimate only for a final unweighted sum does not supply these signed prefix estimates. Nor does an estimate for the combined signed sum \(F_1+F_2\) control either branch separately, since they may cancel. No abstract example or finite witness is being asserted as a counterexample to actual prime asymptotics.

The weighted energy in (R18), or sufficient actual prefix estimates for (R19) with every variation and endpoint term, is still unproved. Largest-prime ranges outside \(\mathcal Q\), higher even rough factor classes, nonrough products and the odd outer residual also remain. Hence the semiprime ledger establishes the exact relevance of a potential signed gain without claiming that combined pilot control settles the long operator.

## 6. Final disposition

The narrow supported result comprises exact support and four-term identities, the distinct finite wheel measures, a valid but insufficient BV weighted-error bound, the negligible prime-power correction and exact norm equivalence, the signed divisor identities, and the semiprime coefficients with their true weights and endpoints. None supplies a useful signed covariance gain.

The three critique findings remain explicit open obligations. The next bounded proof task would have to estimate a genuine weighted discrepancy with its wheel reference on an actual dyadic support, or the actual centered quotient-Möbius norm; any semiprime transfer also needs its weighted branch or prefix statement. These are possible future tasks, not an extra round authorized here.

No new retrieval, numerical experiment, helper, additional agent, paid call, external communication or publication was performed in this revision. Only revision.md and revise-result.json are owned outputs. Frozen proposal and critic artifacts remain unchanged. One pair8 proxy-unit round accounts for propose3, challenge2 and revise3; token and monetary usage remain unknown. The full user objective remains active and incomplete.
