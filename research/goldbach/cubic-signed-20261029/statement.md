# CUBIC022: two cancellations in the actual long signed operator

29 October 2026. Actual Mathematician proposal, one pair round.

**Verdict: incomplete for the constant gap.** Two explicit sectors of the actual operator are \(o(M_N)\). No fixed \(\delta>0\) is proved, including on powers of two. Three remaining operators in (R) retain the missing signed arithmetic. Their required inequality is an open obligation, not a theorem. Novelty of these deductions is unverified.

Assurance: human-readable derivation, not a proof-assistant certificate. Mechanism 1 imports classical Bombieri–Vinogradov in the stated range. Mechanism 2 uses elementary counting, with its needed arguments below. Separate criticism is pending.

## 1. Exact definitions and inspected input

All asymptotics are uniform over sufficiently large even \(N\), with fixed \(B\). Put
\[
 L=\log N,\quad I=(N/3,2N/3]\cap\mathbb N,\quad y=N^{1/6},
 \quad z=L^4,\quad D=N^{1/2}L^{-B}.
\]
The point weight \(\theta(m)\) is \(\log m\) on primes and zero otherwise. Let
\[
 W=\operatorname{rad}\left(N\prod_{p\le z}p\right),\quad
 \kappa=W/\varphi(W),\quad
 u(n)=\theta(N-n)-\kappa1_{(N-n,W)=1}
                   -\theta(N/2)1_{n=N/2}.
\]
The atom is retained. On \(n\in I\), \((n,N)>1\) implies \(u(n)=0\) once \(N\) is large. Indeed any reflected prime on this set is a prime divisor of \(N\) in the central interval; its complementary integer quotient must be two, and the atom cancels it. The model term is zero there.

Define
\[
 \Phi(t)=1-3t^2+2t^3,\quad
 h_{>y}=\prod_{\substack{p\mid h\\p>y}}p,\quad
 C_D(n)=\sum_{\substack{h\mid n\\h>D}}\mu(h)
                  \Phi\left({\log h_{>y}\over\log n}\right).
\]
The exact source operator is
\[
 H_{3,D}(N)=\sum_{n\in I}u(n)C_D(n).                    \tag{1}
\]
This uses precisely the bijection \(n=kh\) in source (8.1), with integer \(k\ge1\). No \(k=1\), product or coupled endpoint is deleted.

We retain
\[
 \mathfrak S(N)=2\prod_{p>2}\left(1-{1\over(p-1)^2}\right)
                   \prod_{\substack{p\mid N\\p>2}}{p-1\over p-2},
 \qquad M_N={\mathfrak S(N)N\over3L},\qquad
 \mathfrak S(N)\gg1.
\]
An elementary bound sufficient for power errors is \(\kappa\ll L^4\): the product for primes at most \(z\) is at most
\(\prod_{2\le j\le\lfloor z\rfloor}(1-1/j)^{-1}\le z\); prime divisors of \(N\) above \(z\) add at most
\(\exp(O(L/(z\log z)))\). Thus \(|u|\ll L^4\). This avoids needing the source's stronger Mertens estimate.

**Imported classical input BV.** For each fixed \(A>0\), prime counts have total maximal endpoint, maximal reduced-class discrepancy from \(\operatorname{li}(t)/\varphi(m)\) bounded by \(O_A(N/L^{A+1})\), over \(m\le Q\le N^{1/2}L^{-A-3}\). Partial summation gives the corresponding \(\theta\) discrepancy \(O_A(N/L^A)\). This statement was inspected in Koukoulopoulos, *The Distribution of Prime Numbers*, preliminary version, printed p.277, (26.1), local render .runs/goldbach-source-inputs-20261029/prime-bv-book277.png. Its classical proof is imported, not re-proved. It agrees with the interface in Arneth (2.1).

For Mechanism 1 fix \(B\ge8\), or a larger admissible source precision. This reserves the factor \(L^{1/4}\) in the moduli below while applying BV with \(A=4\). Mechanism 2 works for any fixed \(B>0\).

Primary scope: Arneth Gold-40 v1, exact input hashes and access provenance in primary-inputs.md and source-provenance.json. The parsed passages (4.1)–(4.5), (5.1)–(5.10), (7.1)–(7.8), (8.1)–(8.4) were read; renders p.7 and p.13 were checked. Source (7.2) follows by summing \(\mu\) over the small-prime part; \(\Phi(t)+\Phi(1-t)=1\) follows by expansion. Neither supplies the desired sign. Source Proposition 6.1 is not imported in the proofs below. No source-wide certification or conditional Goldbach reduction is promoted to a proof.

## 2. Mechanism 1: small-prime cancellation into a controlled shell

For sufficiently large \(N\) set
\[
 w=\left\lfloor{\log L\over4\log\log L}\right\rfloor,\qquad
 G=\prod_{p\le w}p,\qquad Q=GD.
\]
Then \(w\to\infty\), \(w<y\), \(G\le\lfloor w\rfloor!\le L^{1/4}\), and \(3^{\omega(G)}\le3^w=L^{o(1)}\).

**Claim 1 (proved relative to classical BV).**
\[
 H_{\le w}:=\sum_{\substack{n\in I\\(n,G)>1}}u(n)C_D(n)
 =O\left({N\over L^{3-o(1)}}+N^{15/16+o(1)}
                             +N^{3/4+o(1)}\right)=o(M_N). \tag{2}
\]
This is signed cancellation on nonrough products in the original long operator.

### Exact coefficient identity

Fix squarefree \(g\mid G\), \(g>1\), and \(g\mid n\). Every contributing divisor is uniquely \(h=ed\), \(e\mid g\), \((d,g)=1\). Because all primes of \(g\) are at most \(y\),
\[
 C_D(n)=\sum_{\substack{d\mid n\\(d,g)=1}}\mu(d)
 \Phi\left({\log d_{>y}\over\log n}\right)
                  \sum_{e\mid g}\mu(e)1_{ed>D}.          \tag{3}
\]
The inner sum vanishes both for \(d\le D/g\), when no \(ed>D\), and for \(d>D\), when all \(e\mid g\) occur. Only \(D/g<d\le D\) remains, with both endpoints as written.

Put
\[
 U_m=\sum_{\substack{n\in I\\m\mid n}}u(n)
                \Phi\left({\log m_{>y}\over\log n}\right).
\]
In the sum restricted by \(g\mid n\), the modulus is \(m=gd\), not \(ed\). The conditions \(\mu(d)\ne0\) and \((d,g)=1\) make \(m\) squarefree, and \(m_{>y}=d_{>y}\). Therefore
\[
\begin{split}
 H_g&:=\sum_{\substack{n\in I\\g\mid n}}u(n)C_D(n)
 =\sum_{\substack{D<m\le gD\\g\mid m\\(m/g,g)=1}}
                       \lambda_g(m)U_m,\\
 \lambda_g(m)&=\mu(m/g)\sum_{e\mid g}\mu(e)1_{e(m/g)>D},
 \qquad |\lambda_g(m)|\le\tau(g).                       \tag{4}
\end{split}
\]
For a single prime \(p\le w\), this is exactly
\(H_p=\sum_{D<m\le pD,\ p\mid m}\mu(m)U_m\).
Repeated prime factors of \(n\) are permitted: only the divisors \(h\) are squarefree. If \(p\mid N\), the entire \(p\mid n\) sector is zero by the atom-supported identity above.

### Progression and model errors

For \(Q\le N^{1/2}L^{-7}\) we have
\[
 E(Q):=\sum_{\substack{m\le Q\\\mu^2(m)=1}}|U_m|
 \ll {N\over L^4}+{N\over L^3}+N^{15/16+o(1)}
                                  +N^{3/4+o(1)}+L.     \tag{5}
\]
Here are the necessary model and weight details, reconstructed from counting.

Noncoprime rows vanish exactly. On coprime rows, counting one excluded residue for each \(p\mid W,\ p\nmid m\) gives the non-atomic model density on multiples of \(m\):
\[
 g_b(m)={1\over m}\prod_{p\mid(m,W)}{p\over p-1}
       ={1\over\varphi(m)}
          \prod_{\substack{p\mid m\\p\nmid W}}(1-1/p).    \tag{6}
\]
This is generally different from \(1/\varphi(m)\).

Use adjacent Bonferroni orders near \(L/(16\log L)\) for the primes \(p\le z\) not dividing \(m\). The retained small-prime products and their number are at most \(N^{1/4+o(1)}\); the normalized main-density tail is \(N^{-1/16+o(1)}\), by the factorial bound and \(\sum_{p\le z}1/p=O(\log\log z)\). The elementary justification of this reciprocal-prime bound is supplied in Section 3.

Treat \(F=\prod_{p\mid N,\ p>z}p\) exactly. It has \(\tau(F)=2^{\omega(F)}=N^{o(1)}\) divisors. Apply Bonferroni first to the positive \(F\)-sieved count, and expand the \(F\)-filter afterwards; no inequality is multiplied by a signed \(\mu(f)\). Compatible lattices have error at most one each. Thus, for any real interval \(J\subset(N/3,2N/3]\), the model error is
\[
 O\left({N\over m}N^{-1/16+o(1)}+N^{1/4+o(1)}\right).
\]
The factor \(\kappa\ll L^4\) is absorbed in \(N^{o(1)}\). Summing over \(m\le Q\) gives the two power errors in (5).

For the density mismatch, \(1-\prod(1-x_i)\le\sum x_i\) gives
\[
 \sum_{\substack{m\le Q\\\mu^2(m)=1\\(m,N)=1}}
 \left|{1\over\varphi(m)}-g_b(m)\right|
 \ll L\sum_{p>z}p^{-2}\ll L^{-3}.                       \tag{7}
\]
Indeed \(\sum_{r\le x}\mu^2(r)/\varphi(r)\ll\log(2x)\), so the sum with \(p\mid m\) is \(O(L/p)\). The former estimate follows from
\(m/\varphi(m)=\sum_{e\mid m}\mu^2(e)/\varphi(e)\) and convergence of
\(\sum_e\mu^2(e)/(e\varphi(e))\), whose Euler factors have increments \(1/(p(p-1))\).

BV with \(A=4\) bounds the actual reflected-prime interval discrepancies by \(O(N/L^4)\). The polynomial weight in \(U_m\) is in \([0,1]\) and monotone on \(I\), so partial summation costs an absolute constant and retains the exact endpoints. On a coprime row the atom can occur only for \(m=1\) when \(N/2\) is prime, at cost \(O(L)\). This proves (5). Restricting its absolute error sums to \(p\mid m\) or the sets in (4) is legitimate.

Finally inclusion–exclusion on the product variable gives
\[
 1_{(n,G)>1}=-\sum_{\substack{g\mid G\\g>1}}\mu(g)1_{g\mid n},
 \qquad
 |H_{\le w}|\le \sum_{g\mid G}\tau(g)E(Q)
                   =3^{\omega(G)}E(Q).
\]
Since \(Q\le N^{1/2}L^{1/4-B}\le N^{1/2}L^{-7}\), this proves (2).

The real assumption is logarithmic size of \(G\). A single prime \(p\) approaching \(y\) yields a shell up to \(pD\), potentially \(N^{2/3}L^{-B}\); (5) does not cover it. Thus (2) does not remove all nonrough products. The shell support is an exact obstruction to that proposed extension, not a counterexample to an eventual prime theorem.

## 3. Mechanism 2: odd squarefree rough central-strip pairing

For squarefree \(y\)-rough \(n\in I\) define
\[
 {\cal C}(n)=\{h\mid n:D<h<n/D\},\qquad
 T(n)=\sum_{h\in{\cal C}(n)}\mu(h)\Phi(\log h/\log n).
\]
Eventually \(D^2<n\). The map \(h\mapsto n/h\) is an involution of this exact open central set. The remaining long outer set is \(h\ge n/D\), equivalently \(d=n/h\le D\); equality belongs to the outer set.

**Claim 2 (proved, elementary).**
\[
 E_{\rm odd}:=\sum_{\substack{n\in I\\P^-(n)>y\\\mu(n)=-1}}u(n)T(n)
 =O_B\left({\mathfrak S(N)N(\log L)^5\over L^2}
                                  +\log L\right)=o(M_N). \tag{8}
\]
Here \(\mu(n)=-1\) includes squarefreeness.

### Exact involution and derivative loss

Squarefreeness gives \(\mu(n/h)=\mu(n)\mu(h)\), and roughness gives \(h_{>y}=h\). Consequently
\[
 T(n)={1\over2}\sum_{h\in{\cal C}(n)}\mu(h)
       [\Phi(t_h)+\mu(n)\Phi(1-t_h)],
 \qquad t_h={\log h\over\log n}.                         \tag{9}
\]
Write \(c_n=\log D/\log n<1/2\). In this set \(c_n<t_h<1-c_n\).
Since \(|\Phi'(t)|=6t(1-t)\le3/2\) and \(\Phi(1/2)=1/2\),
\[
 |2\Phi(t_h)-1|\le3(1/2-c_n).
\]
For odd parity, (9) gives
\[
 |T(n)|\le {3\over2}2^{\omega(n)}(1/2-c_n)
          \le48(1/2-c_n)=O_B(\log L/L).                 \tag{10}
\]
Every \(y\)-rough integer below \(N\) has at most five prime factors with multiplicity, and
\[
 1/2-c_n={B\log L+\tfrac12\log(n/N)\over\log n}.
\]
This expression is positive on \(I\) once \(N\) is large.

For even parity, however,
\[
 T(n)={1\over2}\sum_{h\in{\cal C}(n)}\mu(h).              \tag{11}
\]
A rough squarefree semiprime \(n=pq\) with \(D<p,q<n/D\) has \(T(n)=-1\). This is an algebraic failure case for suppression of every central coefficient, not a finite counterexample to the eventual weighted assertion.

### Actual rough absolute-mass bound

We prove the deliberately weak bound
\[
 \sum_{\substack{n\in I\\P^-(n)>y}}|u(n)|
 \ll {\mathfrak S(N)N(\log L)^4\over L}+L.               \tag{12}
\]
Put
\[
 q=\exp\left({L\over(\log L)^2}\right),\qquad
 K=2\left\lfloor{(\log L)^2\over32}\right\rfloor .
\]
Eventually \(z<q<y\). Apply the even upper Bonferroni sum at order \(K\) to at most two excluded residues per prime \(p\le q\). Retained squarefree moduli satisfy \(e\le q^K=N^{1/16+o(1)}\). The combined lattice error is at most
\[
 \sum_{e\le q^K}2^{\omega(e)}
 \le\sum_{e\le q^K}\tau(e)\ll q^K\log(2q^K)=N^{1/16+o(1)}.
\]
The discrepancy between the truncated main density and the full local product is at most
\[
 {(\sum_{p\le q}\nu_p/p)^{K+1}\over(K+1)!}\ll_J L^{-J}
                                                        \tag{13}
\]
for each fixed \(J\), because \(\nu_p\le2\), \(K\asymp(\log L)^2\) and
\(\sum_{p\le q}1/p=O(\log\log q)=O(\log L)\).

The reciprocal-prime bound needs no PNT. Primes in \((m,2m]\) divide \(\binom{2m}{m}\le4^m\); dyadic summation gives \(\sum_{p\le x}\log p\ll x\). Splitting at \(\sqrt x\) gives \(\pi(x)\ll x/\log x\), and partial summation gives the bound above. Also, for \(P_q=\prod_{p\le q}(1-1/p)\),
\(P_q^{-1}\ge\sum_{m\le q}1/m\gg\log q\).

For the actual sequence, rough \(n\) and prime \(N-n\) force both numbers to avoid primes at most \(q\). Their local exclusion number is \(\nu_p=1\) for \(p\mid N\), and two otherwise. Multiplication of the local factors, including \(p=2\), yields
\[
 \prod_{p\le q}(1-\nu_p/p)
       \ll\mathfrak S(N)P_q^2
       \ll{\mathfrak S(N)\over(\log q)^2}.               \tag{14}
\]
The omitted tail of \(\prod_{p>2}(1-(p-1)^{-2})\) is bounded away from zero uniformly. Multiplying the sifted count by \(\theta(N-n)\le L\) and taking \(J=12\) in (13) gives
\[
 \sum_{P^-(n)>y}\theta(N-n)
 \ll {\mathfrak S(N)N(\log L)^4\over L}
       +N/L^{11}+N^{1/16+o(1)}L.                       \tag{15}
\]

For the non-atomic model an upper bound can drop the large prime divisors \(p>z\) of \(N\) from the filter, while retaining the actual prefactor \(\kappa\). Sieve \(n\) by \(p\le q\) and \(N-n\) by \(p\le z\). The local density is exactly
\[
 P_q V_N(z),\qquad
 V_N(z)=\prod_{\substack{p\le z\\p\nmid N}}\left(1-{1\over p-1}\right).
\]
Direct local multiplication gives the identity in source (6.3):
\[
 \kappa V_N(z)=\mathfrak S(N)
   \prod_{\substack{p>z\\p\nmid N}}
      \left(1-{1\over(p-1)^2}\right)^{-1}
 \ll\mathfrak S(N).                                   \tag{16}
\]
Every prime divisor of \(N\) still in \(\kappa\) is thus accounted for. No distribution theorem for those factors is invoked. The same Bonferroni orders and moduli give
\[
 \sum_{P^-(n)>y}\kappa1_{(N-n,W)=1}
 \ll {\mathfrak S(N)N(\log L)^2\over L}
       +N/L^8+N^{1/16+o(1)}.                           \tag{17}
\]
Only the errors use \(\kappa\ll L^4\). The correction atom costs at most \(L\). Equations (15)–(17), with \(|u|\le a+b\), prove (12). Combining (10) and (12) proves (8).

Squarefreeness, roughness and odd parity each do real work. For a squarefree nonrough \(n=ab\), where \(a\) is its small-prime part, complementary large-prime logarithms sum to \(\log b/\log n\), not one. The central-strip difference can then contain an additional \(O(\log a/\log n)\). No smallness of that term is proved here. Nonrough squareful products also lack the Möbius complement relation.

## 4. Complete remainder ledger and first failed estimate

An elementary error ledger accompanies Mechanism 2. For \(y\)-rough squareful \(n<N\), \(|C_D(n)|\le2^{\omega(n)}\le32\), and there are at most \(N\sum_{p>y}p^{-2}\ll N^{5/6}\) such \(n\). Their entire original long contribution satisfies
\[
 E_{\rm sf,long}=O(N^{5/6}L^4)=o(M_N).                  \tag{18}
\]
This bounds the long coefficient itself on this rough squareful set. It does not discard squareful nonrough products. It is separate from the full-minorant squarefree-removal term in source (8.3), which would still need its own closure ledger.

The three remaining actual operators are
\[
\begin{aligned}
 R_{\rm nr}&=\sum_{\substack{n\in I\\w<P^-(n)\le y}}u(n)C_D(n),\\
 R_{\rm even}&=\sum_{\substack{n\in I\\P^-(n)>y\\\mu(n)=1}}u(n)C_D(n),\\
 R_{\rm outer,odd}&=
 \sum_{\substack{n\in I\\P^-(n)>y\\\mu(n)=-1}}
 u(n)\mu(n)\sum_{\substack{d\mid n\\d\le D}}\mu(d)
              \left[1-\Phi\left({\log d\over\log n}\right)\right].
\end{aligned}                                                    \tag{R}
\]
The last identity uses \(d=n/h\) on \(h\ge n/D\) and exact \(\Phi\) symmetry. It includes equality and every integer cofactor. The \(k=1\), \(h=n\) term is included, with its true zero polynomial weight on rough squarefree products. The nonrough residual includes \(k=1\) with its generally nonzero true weight, and all remaining squareful nonrough products.

The exact support identity is
\[
 H_{3,D}=H_{\le w}+E_{\rm sf,long}+E_{\rm odd}
                     +R_{\rm nr}+R_{\rm even}+R_{\rm outer,odd}.   \tag{19}
\]
Thus the three proved error terms are \(o(M_N)\), uniformly over even \(N\). No residual is asserted negligible, and no extra gain on powers of two is proved.

For quantitative remaining-range accounting with only the arguments here,
\(\sum_{n\le N}\tau(n)\ll N\log N\), \(0\le\Phi\le1\), and \(|u|\ll L^4\) give
\[
 |R_{\rm nr}|+|R_{\rm even}|+|R_{\rm outer,odd}|\ll NL^5.          \tag{20}
\]
This is far larger than \(M_N\). It records the absence of a useful remainder estimate; it is not substituted for the requested signed lower bound.

The first failed load-bearing inequality is, for some fixed \(\delta>0\) and all sufficiently large even \(N\),
\[
 R_{\rm nr}+R_{\rm even}+R_{\rm outer,odd}
          \ge-\left({3\over4}-\delta+o(1)\right)M_N.              \tag{21}
\]
No proof of (21) is obtained. Writing this obligation is not a new result or a breakthrough. Centering supplies no sign by itself.

A tractable next obligation is an actual weighted estimate for the even-parity semiprime central sector (11), together with its outer semiprime terms, retaining the wheel and reflected-prime weight. Its explicit coefficient \(-1\) falsifies a pointwise suppression mechanism. It does not refute the eventual weighted assertion; arithmetic information is still required.

No result from 014, 018, 019 or 021 is transported to an unsupported weight or range. The source comparison asymptotic, short-operator closure and original prime minorant would need their own assurance before a claimed Goldbach implication; no such closure is claimed here.

## 5. Handoff and boundary

Exactly two mechanisms were attempted: small-prime Möbius cancellation into controlled modulus shells, and odd-parity complementary pairing in the actual central strip. Both yield deductions about the signed operator (1); neither proves the \(3/4\) gap. The rough squareful bound is an elementary error ledger for the second mechanism.

Review questions: check the modulus \(gd\) in (4), the growing-\(w\) precision reserve, the positive-count treatment of divisors of \(N\), every endpoint in (9) and (19), and the mixed model normalization (16). The unresolved arithmetic is precisely (21), with all three residuals present.

No numerical search, supplementary agent, paid call, external message, publication or full-goal completion is part of this proposal. Resource scope remains one actual propose/challenge/revise pair round, eight proxy units, plus two root primary-access units. Token and monetary usage are unknown.
