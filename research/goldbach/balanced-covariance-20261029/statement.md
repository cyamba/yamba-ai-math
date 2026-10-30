# BALANCED023: actual covariance, two attempted arithmetic routes

29 October 2026. Actual Mathematician propose stage, one pair8 round.

**Verdict: incomplete.** No estimate (D_{\mathcal Q}=o(M_N^2)), useful one-sided weighted semiprime estimate, or Goldbach breakthrough is proved. The first route reaches a prime-weighted progression discrepancy which the imported Bombieri–Vinogradov statement does not bound with the needed weights. An attempted average of that discrepancy loses a power of the (q)-length. The second route removes prime powers with a proved negligible error and gives an exact signed divisor expansion; its long Möbius correlation remains unbounded at the required scale. The semiprime ledger below identifies the actual weighted target, rather than replacing it by the unweighted pilot.

All statements labelled **proved** have the complete human-readable arguments below. None has a proof-assistant certificate; separate criticism is pending. Novelty is unverified. The persistent Goldbach objective remains incomplete.

## 1. Definitions, support and imported input

The quantifier for the proposed target is all sufficiently large even integers (N), uniformly as (N\to\infty). Put
\[
 L=\log N,\quad I=(N/3,2N/3],\quad y=N^{1/6},\quad z=L^4,
 \quad W=\operatorname{rad}\left(N\prod_{\ell\le z}\ell\right),
 \quad\kappa=W/\varphi(W),
 \quad\mathcal Q=(N^{11/24},N^{13/24}].
\]
Here and below a product indexed by \(\ell\) is over primes. The point function \(\theta(m)\) is \(\log m\) for prime \(m\), zero otherwise. Exactly as in the brief,
\[
 u(n)=\theta(N-n)-\kappa1_{(N-n,W)=1}
                   -\theta(N/2)1_{n=N/2},
 \qquad M_N={\mathfrak S(N)N\over3L},
\]
where \(\mathfrak S(N)\) is the stated binary singular series and \(\mathfrak S(N)\gg1\).

Write \(b_2(r)=1_{P^-(r)>y,\,\Omega(r)=2}\) and \(b_1(r)=1_{r\ {m prime}}\). For \(a\in\{1,2\}\) let
\[
 J_r^2=\mathcal Q\cap(N/(3r),2N/(3r)],\qquad
 J_r^1=J_r^2\cap[r,\infty).
\]
Thus \(\beta(r,q)=\sum_{a=1,2}b_a(r)1_{q\in J_r^a}\). The two branches are disjoint even for repeated prime factors in \(b_2\). For each pair put \(K_{rs}^{ab}=J_r^a\cap J_s^b\). These are the exact coupled intervals, with every open or closed endpoint inherited from their definition.

Every supported index satisfies
\[
 \tfrac13N^{11/24}<r\le\tfrac23N^{13/24},\qquad r>y,
 \quad q>1,\quad r>1.
\]
In particular \(n=rq\) is composite, even when \(q\) is an integer. A nonzero correction atom would require \(n=N/2\) and \(N/2\) prime, which contradicts this compositeness. Only after this argument may we set
\[
 a_r(q)=\theta(N-rq),\quad\chi_r(q)=1_{(N-rq,W)=1},
 \quad v_r(q)=a_r(q)-\kappa\chi_r(q)=u(rq).
\]

**Proved zero rows.** If \((rq,N)>1\), then \(v_r(q)=0\). The model is zero because a common prime divisor of \(rq,N\) divides \(N-rq\) and \(W\). If \(N-rq\) is prime, it is a prime divisor of the even number \(N\) in \([N/3,2N/3)\). For large \(N\) that prime is odd, so its quotient into \(N\) is an even integer at most three, hence two. This would give the already excluded prime \(rq=N/2\). Thus the prime term also vanishes. Consequently rows with \((r,N)>1\), and integer \(q\) with \((q,N)>1\), contribute exactly zero. On every remaining row \((r,W)=1\): \(r\) is \(y\)-rough, \(z<y\), and \((r,N)=1\).

We retain exactly
\[
 F(q)=\sum_r\beta(r,q)v_r(q),\quad
 T_{\mathcal Q}=\sum_{q\in\mathcal Q,\ q\ {m prime}}F(q),\quad
 D_{\mathcal Q}=\sum_{q\in\mathcal Q\cap\mathbb N}q|F(q)|^2.
\]
Weighted Cauchy gives \(|T_{\mathcal Q}|^2\le (\sum_{q\in\mathcal Q,\,q\ {m prime}}1/q)D_{\mathcal Q}\). The reciprocal-prime sum is bounded: the elementary Chebyshev bound \(\pi(x)\ll x/\log x\), followed by partial summation between these fixed powers, suffices. Thus the proposed dispersion target would imply the pilot estimate. Its converse, any branchwise consequence, and any Goldbach implication are not asserted.

The only imported distribution theorem is Koukoulopoulos, *The Distribution of Prime Numbers*, preliminary version, printed p.277/PDF p.288, exact (26.1): for each fixed \(A>0\), the sum over moduli \(d\le Q\le N^{1/2}/L^{A+3}\) of the maximal endpoint and reduced-residue prime-count discrepancy is \(O_A(N/L^{A+1})\). Partial summation gives the corresponding \(\theta\)-discrepancy sum \(O_A(N/L^A)\). No theorem for an extra prime-valued weight is imported.

Primary inspection in this stage: Arneth Gold-40 v1, actual parsed Sections 8, 9.1 and 10.2–10.3, page17 render, and the actual BV page render. Their local files and hashes are in the unchanged `../cubic-signed-20261029/source-provenance.json`. The source PDF has SHA256 `d604a310e193d33698c42e135bff63ce2499b4d0d90c71d9f9a4c08b9b9f3cbd`; its text has SHA256 `359c7aee9867fddce82b6887f8d9e485befe16d107164e2cdec04ebbe9c044d4`. No new retrieval or source-wide certification occurred. The source's Hypothesis8.2 and sufficient dispersion assertion remain open and are not assumptions here. The packet's `audit-theorem` workflow and the repository punctuation rule were read and applied.

## 2. Mechanism 1: retain the four terms and switch the actual prime pair

The exact off-diagonal is
\[
 \sum_{a,b\in\{1,2\}}\ \sum_{r\ne s}b_a(r)b_b(s)
 \sum_{q\in K_{rs}^{ab}\cap\mathbb N}q
 \{a_ra_s-\kappa a_r\chi_s-\kappa\chi_ra_s
                                      +\kappa^2\chi_r\chi_s\}.       \tag{2.1}
\]
Both cross-branch terms \((a,b)=(1,2),(2,1)\) are present. No support is replaced by a rectangle. Repeated factors in \(r\) or \(s\) are retained. The diagonal is not a substitute for (2.1): using only \(\kappa\ll L^4\) and at most \(O(N/q)\) inner indices gives
\[
 D_{\mathcal Q,\mathrm{diag}}\ll N^{37/24}L^8=o(M_N^2).       \tag{2.2}
\]
For completeness, \(\kappa\ll L^4\) follows by bounding the primes at most \(z\) by the telescoping product over all integers \(2\le j\le\lfloor z\rfloor\), and the extra prime divisors of \(N\) above \(z\) by \(\exp(O(L/(z\log z)))\). This deliberately weaker elementary bound suffices for every power error here. Bound (2.2) is bookkeeping already anticipated by the source, not a signed gain.

### Exact integer-q local factors

Fix two live rows \(r,s\). For \(\ell\mid W\), the forbidden roots in the variable \(q\bmod\ell\) are \(Nr^{-1}\) and \(Ns^{-1}\). They coincide exactly when \(\ell\mid N(s-r)\). Let \(\nu_\ell\) be one in that case and two otherwise. Under the *uniform integer residue measure* modulo \(W\), CRT proves
\[
 {1\over W}\sum_{t\bmod W}\chi_r(t)\chi_s(t)
       =\prod_{\ell\mid W}(1-\nu_\ell/\ell),\qquad
 {1\over W}\sum_{t\bmod W}\kappa\chi_r(t)=1.             \tag{2.3}
\]
Thus the joint normalized model factor is
\[
 \kappa^2\prod_{\ell\mid W}(1-\nu_\ell/\ell)
 =\prod_{\substack{\ell\mid W\\\ell\mid N(s-r)}}
          {\ell\over\ell-1}
  \prod_{\substack{\ell\mid W\\\ell\nmid N(s-r)}}
          \left(1-{1\over(\ell-1)^2}\right).             \tag{2.4}
\]
This is not the product of the two marginal means. At a single prime, put \(B_{\ell,r}=\ell(\ell-1)^{-1}1_{t\ne Nr^{-1}}\). Directly averaging its one or two forbidden residues gives the exact signed local covariance
\[
 \mathbb E[(B_{\ell,r}-1)(B_{\ell,s}-1)]
 =\begin{cases}1/(\ell-1),&\ell\mid N(s-r),\\
                -1/(\ell-1)^2,&\ell\nmid N(s-r).
   \end{cases}                                            \tag{2.5}
\]
These formulas are finite wheel identities, not prime-prime correlation estimates. In particular \(W\) can greatly exceed the available interval length, so a complete-residue identity is not automatically an asymptotic on \(K_{rs}^{ab}\).

For comparison of measures only, uniform *unit residues* at \(\ell\) would give joint survival probability one when \(\ell\mid N\), and \(1-\nu_\ell/(\ell-1)\) when \(\ell\nmid N\). The corresponding marginal probabilities are one and \(1-1/(\ell-1)\). They differ from (2.3). This calculation assigns no distribution theorem or prime density to the integer-q sum.

One can also retain the full finite-interval wheel exactly. Expand both indicators over \(d,e\mid W\). Their congruences have a solution precisely when \((d,e)\mid N(s-r)\), then one residue modulo \([d,e]\). Hence
\[
 \sum_{q\in K\cap\mathbb N}q\chi_r(q)\chi_s(q)
 =\sum_{\substack{d,e\mid W\\(d,e)\mid N(s-r)}}\mu(d)\mu(e)
       \sum_{\substack{q\in K\cap\mathbb N\\q\equiv t_{d,e}\pmod{[d,e]}}}q. \tag{2.6}
\]
No error from this expansion is asserted small: summing a unit lattice error over all wheel divisors would not justify that assertion.

### The attempted distribution step, including its actual averaging loss

For \(m_1=N-rq,m_2=N-sq\), exactly
\[
       s m_1-r m_2=N(s-r),\qquad
       m_1\equiv N\pmod r,\quad q=(N-m_1)/r\in K_{rs}^{ab}.  \tag{2.7}
\]
The congruence modulo \(r\), not just modulo \(r/(r,s)\), is needed to retain integer \(q\). Substitution into the first term of (2.1) gives
\[
 \sum_{\substack{m_1\equiv N\pmod r\\(N-m_1)/r\in K_{rs}^{ab}}}
 {N-m_1\over r}\,\theta(m_1)
 \theta\left({s m_1-N(s-r)\over r}\right).               \tag{2.8}
\]
So the switch has not removed the second genuine-prime condition. The mixed terms have exactly the same transformed support and the indicated wheel indicator instead of the second prime.

Here is a concrete attempt to average using the available BV theorem. Restrict to any dyadic interval \(X<q\le2X\) in \(\mathcal Q\) with \(N/X\le N^{1/2}/L^{A+3}\). All relevant \(r,s\) then lie in a constant multiple of \(R=N/X\). The constant is harmless, so impose the BV cutoff on that multiple as well. Group the first and second terms of (2.1) as
\[
       \sum_{q\in K}q\theta(N-rq)v_s(q).                  \tag{2.9}
\]
The other two terms remain \(-\kappa\sum_{q\in K}q\chi_r(q)v_s(q)\), with no change of model. Let \(\Delta(r)\) be the maximal reduced-class endpoint \(\theta\)-discrepancy up to \(N\). Abel summation of (2.9) along the progression bounds its error relative to the corresponding constant-density lattice sum by
\[
 \bigl(\|qv_s(q)\|_\infty+
        \operatorname{Var}_{q\in K\cap\mathbb N}(qv_s(q))\bigr)
                   O(\Delta(r)+r/\varphi(r)).             \tag{2.10}
\]
This follows from the discrete identity \(\sum f_j e_j=f_b E_b+\sum_{j<b}(f_j-f_{j+1})E_j\), where \(E_j\) is the progression error up to index \(j\). The term \(r/\varphi(r)\) allows the endpoint difference between the continuous and integer lattice reference. This is a valid partial summation bound for the actual second-prime weight.

The pointwise bound \(|v_s|\ll L^4\) gives \(\|qv_s\|_\infty\ll XL^4\), but its variation is only bounded here by \(O(X^2L^4)\): there are \(O(X)\) successive differences, each at most \(O(XL^4)\). Summing (2.10) over the *actual* \(r,s\) supports, bounding their zero-one coefficients by one, and using imported BV gives the rigorous but insufficient bound
\[
 \mathrm{error}\ll X^2R L^4
       \left({N\over L^A}+R L^4\right)
 \ll {N^2 X\over L^{A-4}}+N^2L^8.                       \tag{2.11}
\]
The elementary bound \(r/\varphi(r)\ll L^4\) is sufficient for the displayed lattice term. No fixed logarithmic precision \(A\) removes the power \(X\) from the first term. The coefficients \(b_a,b_b\), all branch restrictions and coupled intervals were kept until this explicit failed averaging bound; they were not silently replaced by a distribution hypothesis.

Moreover the whole support is not in the BV range: \(r\) can be as large as \((2/3)N^{13/24}\). Reversing the roles of \(r\) and \(s\) leaves a second prime-valued weight, and does not fix this. Summing first in \(r\) instead introduces \(b_a(r)\), a prime or filtered-semiprime quotient weight, and sometimes a modulus \(q>\sqrt N\). The imported theorem does not include these weights or moduli.

**First failed arithmetic inequality of this route.** The weighted progression errors in (2.10), summed with \(b_a(r)b_b(s)\) and the exact supports, would need to be negligible at scale \(M_N^2\), together with a matching evaluation of their wheel reference terms. Estimate (2.11) does not prove that. Replacing the variation in (2.10) by a smooth, constant-sized variation would discard the actual second-prime sequence. Local formulas (2.3)–(2.6) do not authorize that replacement. No assertion that the eventual covariance target is false follows from this failure.

## 3. Mechanism 2: an exact signed divisor expansion of the remaining prime weight

This attempt keeps the actual \(\beta\), rather than replacing it by a comparison density. Let \(\Lambda\) be the von Mangoldt function and define
\[
 F_\Lambda(q)=\sum_r\beta(r,q)
       [\Lambda(N-rq)-\kappa\chi_r(q)],\qquad
 R(q)=F_\Lambda(q)-F(q)\ge0.
\]

**Proved arithmetic error lemma.** Uniformly over even \(N\),
\[
 \sum_{q\in\mathcal Q\cap\mathbb N}qR(q)^2
             \ll N^{3/2}L^3=o(M_N^2),\qquad
 \sum_{q\in\mathcal Q\cap\mathbb N}R(q)\ll N^{1/2}L^2=o(M_N). \tag{3.1}
\]
Indeed \(\Lambda-\theta\) is supported on \(p^k\), \(k\ge2\), with value \(\log p\le L\). There are \(O(N^{1/2}L)\) such integers below \(N\), by summing the elementary upper bound \(N^{1/k}\) for \(2\le k\le L/\log2\). For a fixed \(n=N-p^k\in I\), any supported \(r\mid n\) is a prime or semiprime all of whose prime factors exceed \(y\). The part of \(n\) supported on such primes has at most five prime factors with multiplicity, since \(y^6=N>n\). There are consequently at most a fixed constant, say twenty, possible divisors \(r\) of the required one- or two-factor forms. Repeated factors cause no difficulty: choosing one or two factors from five labelled prime-factor slots overcounts all such divisors. For each divisor \(r\), \(q=n/r\) is fixed. Therefore \(\sum_qR(q)\ll N^{1/2}L^2\). Also \(R(q)\ll (N/q)L\) by counting all inner indices. Multiplying this last bound by \(qR(q)\) and summing proves the first inequality in (3.1).

By the triangle inequality in the weighted square norm, (3.1) proves the exact equivalence
\[
 \sum_q q|F(q)|^2=o(M_N^2)
 \quad\Longleftrightarrow\quad
 \sum_q q|F_\Lambda(q)|^2=o(M_N^2).                       \tag{3.2}
\]
This removes only prime powers. It is not a favourable bound on the prime-prime off-diagonal, nor a new margin.

For every integer \(m>1\), elementary Möbius inversion proves
\[
 \Lambda(m)=\sum_{d\mid m}\mu(d)\log(m/d).
\]
To check the identity without an imported theorem, write \(\log m=\sum_{e\mid m}\Lambda(e)\), which follows by prime factorization, and invert the divisor sum. Set \(H=N^{1/24}\) and define, with \(m=N-rq\),
\[
 \begin{split}
 S_H(q)&=\sum_r\beta(r,q)\sum_{\substack{d\mid m\\d\le H}}
                                  \mu(d)\log(m/d),\\
 V_H(q)&=\sum_r\beta(r,q)\sum_{\substack{d\mid m\\d>H}}
                                  \mu(d)\log(m/d),\\
 B(q)&=\sum_r\beta(r,q)\chi_r(q).
 \end{split}
\]
Then, with no omitted divisor or changed endpoint,
\[
 F_\Lambda(q)=S_H(q)+V_H(q)-\kappa B(q),                 \tag{3.3}
\]
and the attempted long-divisor switch is exactly
\[
 V_H(q)=\sum_{k<2N/(3H)}\log k
   \sum_{\substack{r:\ k\mid N-rq\\(N-rq)/k>H}}
        \beta(r,q)\mu\left({N-rq\over k}\right).         \tag{3.4}
\]
The strict upper bound is correct because \(m=N-rq<2N/3\); the lower reflected endpoint \(m\ge N/3\) remains in \(\beta\). The \(k=1\) term is present and has its actual zero factor \(\log1\). No coprimality, squarefree quotient or prime status has been imposed on \(k\); the Möbius function itself supplies its actual value.

This is a concrete signed divisor decomposition accessing both branches, including the even rough semiprime branch. It does not evaluate its long part. The necessary arithmetic obligation after this switch is
\[
 \sum_{q\in\mathcal Q\cap\mathbb N}q
       |V_H(q)-(\kappa B(q)-S_H(q))|^2=o(M_N^2).         \tag{3.5}
\]
No estimate of (3.5) is obtained. Short \(d\) alone do not approximate \(\Lambda\) here: deleting \(V_H\) would require exactly a new assertion about the signed Möbius values on the quotient in (3.4). Taking absolute values there removes their cancellation before centering. The hypotheses of BV concern prime counts, not this quotient-Möbius sequence, and do not supply (3.5). Equations (3.3)–(3.5) record the failed second attempt and do not constitute an additional successful theorem candidate.

## 4. Exact connection to the actual long semiprime contribution

This is necessary accounting for a potential signed gain, not a substitute estimate. Fix \(B>0\), \(D=N^{1/2}L^{-B}\), and
\[
 \Phi(t)=1-3t^2+2t^3,\qquad
 C_D(n)=\sum_{h\mid n,\ h>D}\mu(h)
                \Phi\left({\log h_{>y}\over\log n}\right).
\]
The original long operator is \(\sum_{n\in I}u(n)C_D(n)\). Eventually \(D<\sqrt{N/3}\), so for every \(n=pq\in I\), \(p\le q\) prime, \(q>D\).

For distinct rough primes \(p<q\), let \(t=\log p/\log(pq)\). The divisors with nonzero Möbius coefficient are \(1,p,q,pq\). The last has weight \(\Phi(1)=0\), and \(q>D\). Thus the complete long coefficient is
\[
 C_D(pq)=-1_{p>D}\Phi(t)-\Phi(1-t)
 =\begin{cases}-(3t^2-2t^3),&p\le D,\\-1,&p>D.
 \end{cases}                                            \tag{4.1}
\]
Equality \(p=D\) belongs to the first case, since the long cutoff is strict. The identity \(\Phi(t)+\Phi(1-t)=1\) follows by polynomial expansion. For the square \(n=p^2\), \(\mu(p^2)=0\), there is only the divisor \(p>D\) with nonzero long contribution, and
\[
                    C_D(p^2)=-\Phi(1/2)=-1/2.            \tag{4.2}
\]
This is the square coefficient of the actual long operator after squarefree removal, even though a squarefree-only residual would omit it. No repeated factor is doubled.

Define the actual positive coefficient \(w_D(p,q)=-C_D(pq)\) by (4.1), and set \(w_D(p,p)=1/2\). On prime \(q\in\mathcal Q\), any \(p\le q\) with \(pq\in I\) automatically exceeds \(y\). Unique ordering therefore gives the exact balanced semiprime part
\[
 H_{2,\mathcal Q}
 =-\sum_{\substack{q\in\mathcal Q\\q\ {m prime}}}
          \sum_{\substack{p\le q\\p\ {m prime}\\pq\in I}}
                    w_D(p,q)u(pq).                      \tag{4.3}
\]
With the same formula for integer \(q\) define \(F_{2,w}(q)\) by the inner sum. Its correct dispersion weight is again \(q\):
\[
 |H_{2,\mathcal Q}|^2
 \le\left(\sum_{\substack{q\in\mathcal Q\\q\ {m prime}}}{1\over q}\right)
       \sum_{q\in\mathcal Q\cap\mathbb N}q|F_{2,w}(q)|^2. \tag{4.4}
\]
The integer-q version of \(F_{2,w}\) retains its actual coefficients; it has no claim to semiprime support when \(q\) is composite.

The weight cannot be removed silently. For fixed \(q\), on the distinct-prime part it is \(g(t)=3t^2-2t^3\) for \(p\le D\), then one for \(p>D\). Its derivative below \(D\) is \(6t(1-t)\log q/[p(\log(pq))^2]\), and the jump at \(D\) is \(1-g(t_D)=\Phi(t_D)\). This jump is generally of constant size. Discrete partial summation would therefore require control of prime-branch *prefix* sums \(\sum_{p\le x,\,p<q,\,pq\in I}u(pq)\), including the cutoff at \(D\), followed by the square term (4.2). A bound for only their final unweighted sum does not provide that control.

Nor does a bound for \(F_1(q)+F_2(q)\) give a bound for either branch or its weighted prefix sums: the two signed branch sums can cancel. No abstract countermodel is used to assert a fact about the actual primes. This simply identifies the additional statements a transfer would require. The ranges with largest prime outside \(\mathcal Q\), other even rough factor counts, nonrough products and the odd outer residual remain outside (4.3). Thus even a proof of (4.4) with an \(o(M_N^2)\) right-hand energy would not finish Hypothesis8.2 or Goldbach.

## 5. Handoff

The two attempted mechanisms were actual four-term distribution/divisor switching, and an exact signed divisor expansion of the genuine prime weight. The proved deductions are exact support and zero-row identities, finite-wheel local covariances, the negligible prime-power replacement (3.1), and the complete semiprime coefficient and weighted transfer ledger. They carry no asserted positive Goldbach gap. The load-bearing covariance inequality remains unproved; the explicit failures are (2.10)–(2.11) and (3.5).

A bounded next proof obligation would be to control the second-prime-weighted progression discrepancy in (2.10) on even one actual dyadic balanced range, with the exact branch coefficients and matching wheel terms, or to prove a signed estimate for the actual quotient-Möbius sum (3.4). A local-density computation alone is not that obligation. No finite experiment was run, and a finite witness would not refute an eventual asymptotic assertion.

Review questions: verify the live-row coprimality with the full wheel, distinguish the two local measures, check the retained congruence modulo \(r\) in (2.8), audit the weighted BV variation loss, check the at-most-five large-prime-factor counting in (3.1), and check \(p=D\), \(p=q\), and the varying semiprime weight in (4.1)–(4.4).

Resource boundary: one actual propose/challenge/revise pair8 proxy-unit round; this is its propose stage. No supplement, helper calculation, numerical search, external retrieval, paid call, external message or publication was performed. Token and monetary usage are unknown. Nothing in these deductions marks the full user objective complete.
