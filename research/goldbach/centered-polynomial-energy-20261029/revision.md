# Reviewed principal-centered prime energy, original-author revision

29 October 2026. Actual GOLDBACH-CENTERED-018 original-author revision from the populated revise packet. This closes the one authorized Mathematician/Independent Critic/author round. The distinct critic supports both candidates relative to the named classical theorem statements and elementary analysis. This revision accepts its two P2 clarifications: clean prime-support notation, and a half-integer Perron cutoff used throughout. Neither conclusion is enlarged. Usage is unknown.

The frozen author statement SHA256 is 6470a9f07d8b2074bf3fa89a241eb52114ed9e0fd7f6b6426fd897bcdb1a1cf4. The distinct review SHA256 is 3a014cd1b9f78a36b81b05b9e38076e33807f8bd30080145927e54cf1e44caa2. Both remain unchanged. The frozen statement contains four raw carriage-return bytes at intended roman-prime markers; this revision replaces those definitions by explicit prime sets and does not rewrite the frozen evidence.

Assurance is a complete written author argument with a distinct substantive written-argument audit, relative to the precisely inspected classical theorem statements. It is not formal verification, external peer review or an audit of the complete imported published proofs. No new source search, research experiment, extra round, paid call, publication or external message was performed. The proofs below incorporate the two clarifications; the unchanged details and source provenance remain in the frozen statement and review.

## Clean definitions and the two conclusions

Let H=2^ell tend to infinity, L=log H, alpha in [3/10,1/3), delta=1/4, T=sqrt(H/6), Y=H/3 and I=[T,(1+delta)T], including both endpoints. Let eta be fixed, smooth, real, nonzero, between0 and1, and compactly supported in (2,5/2). Define the prime sets

\[
 \mathcal P=\{a:a\text{ is prime},\ H^\alpha<a<H,\ (a,H)=1\},
 \qquad
 \mathcal Q=\{r:r\text{ is prime},\ T\le r\le(1+\delta)T\}.
 \tag{R1}
\]

Put \(V_H=\sum_{a\in\mathcal P}1/a\). All nonzero selected labels have \(2Y<a<(5/2)Y\), so are in \(\mathcal P\) and below H eventually; every prime in \(\mathcal Q\) is odd and an H-unit eventually. The full normalizer satisfies \(V_H=v_\alpha+o(1)\), where \(v_\alpha=\log(1/\alpha)>0\), by the inspected ordinary PNT and the partial-summation argument in the frozen statement. No reciprocal weight occurs in the selected-label counting sum itself.

For chi modulo H, real t and real lambda set

\[
 B_{\chi,\lambda}(t)=\frac1{YV_H}
       \sum_{a\in\mathcal P}\eta(a/Y)e(-\lambda a/Y)\chi(a)a^{it},
 \quad e(x)=\exp(2\pi i x),
\]
\[
 M_\chi(t)=-\frac1T\sum_{r\in\mathcal Q}\chi(r)r^{it},
 \qquad
 N_\chi(t)=\frac1T\sum_{s\in\mathcal Q}(\log s)\chi(s)s^{it}.
 \tag{R2}
\]

Writing B_chi for B_(chi,0) recovers the exact brief. The polynomial sieve forces primality on I because eventually \(H^\alpha<T\) and \((1+\delta)T<H^{2\alpha}\). The brief's own threshold is \(V_0=(T^2)^{1/5}<T\), yielding the exact prime coefficients -1 and log s. The different BOUNDARY-017 threshold \((7T^2/8)^{1/5}\) is also below I and gives the same prime coefficients; equality of the inherited parameters or of the full Vaughan interfaces is not asserted.

For fixed B>0 and T0=L^B define, with chi0 principal,

\[
 E_{\rm np}(\lambda,v)=\frac1{\phi(H)}
    \sum_{\chi\ne\chi_0}\int_{-T0}^{T0}
       |B_{\chi,\lambda}(t)M_\chi(t+v)N_\chi(t+v)|^2\,dt,
\]
\[
 E_0(\lambda,v)=\frac1{\phi(H)}
    \int_{-T0}^{T0}
       |B_{\chi_0,\lambda}(t)M_{\chi_0}(t+v)N_{\chi_0}(t+v)|^2\,dt.
 \tag{R3}
\]

Here phi(H)=H/2. The total energy is exactly \(E_0(\lambda,v)+E_{\rm np}(\lambda,v)\).

**Candidate 1, proved and supported by the distinct review:** for every fixed A,B,C>0, uniformly over every real lambda and \(|v|\le L^C\),

\[
 E_{\rm np}(\lambda,v)\ll_{A,B,C,\alpha,\eta} H^{-1}L^{-A}.
 \tag{R4}
\]

In particular this proves the requested v=lambda=0 statement while retaining its exact nonzero principal energy. The extension remains at k=1 with trivial fixed character twists.

**Candidate 2, proved and supported by the distinct review:** only at v=lambda=0, define

\[
 C_\eta(t)=\int_2^{5/2}\eta(u)u^{it}\,du,\qquad
 J_\delta(t)=\int_1^{1+\delta}u^{it}\,du.
 \tag{R5}
\]

For each fixed K>0,

\[
 \frac1{\phi(H)}\int_{-K}^{K}|B_{\chi_0}M_{\chi_0}N_{\chi_0}|^2\,dt
 =\frac8{v_\alpha^2HL^4}
       \int_{-K}^{K}|C_\eta(t)|^2|J_\delta(t)|^4\,dt
       +o_K(H^{-1}L^{-4}).
 \tag{R6}
\]

The limiting integral is positive. Hence the exact growing-height \(E_0(0,0)\) is at least \(c/(HL^4)\). No asymptotic over its growing time range is asserted.

## Preserved arithmetic and analytic proof

The exact imported arithmetic statements remain Iwaniec's original Theorem2 on journal page97, with its nonprincipal-character scope and radical-sensitive zero-free width, and the ordinary quantitative PNT of Koukoulopoulos Theorem8.1, printed page84/PDF95. Their primary-statement inspection and unchanged source hashes are recorded in the frozen author and review. Full published proofs were not audited. No small-sift coefficient theorem, Burgess estimate, Hadamard factorization, functional equation or local-zero-density bound is imported.

A real character modulo \(2^\ell\) is trivial on squares. The bit-lifting argument in the frozen proof shows that every odd residue1 modulo8 is a square, so a real character factors through8. The three nonprincipal sign patterns on (1,3,5,7) are

\[
 \chi_{-4}:(+,-,+,-),\quad
 \chi_8:(+,-,-,+),\quad
 \chi_{-8}:(+,+,-,-).
 \tag{R7}
\]

Their primitive conductors are4,8,8. Induction to H has no missing Euler prime, since2 already divides each conductor. For every real sigma>0 let f(x)=x^(-sigma). Periodic partial summation justifies the convergent L-series and grouping consecutive complete periods. For chi_-4 each block is \(f(4n+1)-f(4n+3)>0\). For chi_8, with x=8n+1, each block is

\[
 [f(x)-f(x+2)]-[f(x+4)-f(x+6)]>0,
 \tag{R8}
\]

since the decrement of f over an interval of length2 strictly decreases as the interval moves right. For chi_-8 the block is \([f(x)-f(x+4)]+[f(x+2)-f(x+6)]>0\). All grouped blocks are absolutely summable. Thus each fixed real L-function is strictly positive for every positive real sigma. This proves the required nonvanishing at1 and excludes every positive real exceptional zero explicitly.

Iwaniec's theorem applies at q=H, rad(H)=2. For each fixed height exponent D its width is at least a constant times \(L^{-3/4}(\log L)^{-3/4}\) up to height L^D. It strictly dominates every fixed \(K_1\log L/L\) eventually. Any exceptional character and zero in the printed region must be real, and (R7)-(R8) exclude them. Therefore all nonprincipal characters, including imprimitive ones, are zero free in

\[
 \sigma\ge1-K_1\log L/L,\qquad |\operatorname{Im}s|\le L^D.
 \tag{R9}
\]

The closed selected rectangle is strictly inside the printed open region. The principal character remains excluded.

The elementary analytic-log derivative route is preserved. If
\(A_\chi(x)=\sum_{n\le x}\chi(n)\), then \(A_\chi(H)=0\) and \(|A_\chi|\le H\). For nonprincipal chi, periodic partial summation gives an analytic continuation to Re(s)>0:

\[
 L(s,\chi)=\sum_{n\le H}\chi(n)n^{-s}
             +s\int_H^\infty A_\chi(x)x^{-s-1}\,dx.
 \tag{R10}
\]

On each fixed logarithmic-width strip of (R9), with a fixed polylogarithmic height, this bounds |L| by a fixed power of L. Set \(w=K_1\log L/L\). The disk of radius2w about \(z_0=1+w+i\tau\) is zero free, with left edge1-w and a fixed height margin. Choose its analytic logarithm g to agree at z0 with the Euler logarithm. Then \(|g(z_0)|\le\log\zeta(1+w)=O(\log L)\), while \(\operatorname{Re}g\le O(\log L)\) on the disk by (R10).

Borel-Caratheodory bounds g by O(log L) in radius7w/4. Explicitly, for h=g-g(z0) and \(A=\sup\operatorname{Re}g-\operatorname{Re}g(z0)>0\), the quotient h/(2A-h) maps to the unit disk and vanishes at the center. Schwarz gives \(|h|\le2Ar/(2w-r)\) at radius r<2w. The A=0 case is constant by the maximum principle. Cauchy's estimate in radius w/4 around points at distance at most3w/2 from z0 gives

\[
 |L'/L(s,\chi)|\ll \log L/w\ll L^2
 \tag{R11}
\]

on \(1-w/2\le\operatorname{Re}s\le1+1/L\), uniformly at the required contour heights. No zero-avoiding choice of contour height is needed.

## Corrected half-integer endpoint argument

This section replaces the frozen statement's stronger unsupported shift-back aside. A half-integer cutoff is used throughout the Perron formula and contour shift; no contour endpoint factor is shifted back by a claimed O(L^2).

For an integer cutoff m put \(y^*=m+1/2\). Then n<=m and n<y* are exactly the same integer set. For the actual included interval I use

\[
 m_+=\lfloor(1+\delta)T\rfloor,\qquad
 m_-=\lceil T\rceil-1,\qquad y_\pm^*=m_\pm+1/2.
 \tag{R12}
\]

Thus the difference of the cutoff sums at \(y_+^*,y_-^*\) counts exactly the integers in the included interval I, even if either real endpoint is an integer. Both half-integers are comparable to T and lie in \([H^{1/6},H]\) eventually.

Fix P,D>0, choose \(K_1\ge12(P+5)\), \(D_2>\max(D+2,P+5)\), and put
\(c=1+1/L\), \(\sigma_0=1-K_1\log L/(2L)\), \(R=L^{D_2}/2\).
For \(|u|\le L^D\) and either half-integer in (R12), Perron's formula is

\[
 \sum_{n<y^*}\Lambda(n)\chi(n)n^{iu}
 =\frac1{2\pi i}\int_{c-iR}^{c+iR}
       -\frac{L'}L(s-iu,\chi)\frac{(y^*)^s}{s}\,ds
       +O(y^*L^2/R+L^2).
 \tag{R13}
\]

The elementary truncated kernel error is bounded by a constant times
\((y^*/n)^c\min(1,(R|\log(y^*/n)|)^{-1})\). Its sum against \(\Lambda(n)\le\log n\) is bounded by the displayed error: near y* use the harmonic sum of the nonzero half-integer distances, and in the far tail use \(\sum_n(\log n)n^{-1-1/L}=O(L^2)\).

Shift this same integral, retaining y* in every factor, to sigma0. All points s-iu, and the disks needed for (R11), stay inside (R9) with height L^D2 eventually. No zero or principal pole is crossed. The vertical contribution is \(O((y^*)^{\sigma_0}L^3)\); the horizontal sides and truncation contribute \(O(y^*L^2/R+L^2)\). Since \(\log y^*\ge L/6\), the choices above give

\[
 \left|\sum_{n<y^*}\Lambda(n)\chi(n)n^{iu}\right|
       \ll_{P,D}y^*L^{-P}.
 \tag{R14}
\]

Applying (R14) at \(y_+^*,y_-^*\), each comparable to T, gives O(T L^(-P)) for the full log-prime-power interval sum. No estimate relative to a much shorter interval is asserted. Every nonprincipal inducing conductor is a power of two at least4, so induction supplies no omitted Euler correction. Removing higher prime powers costs \(O(\sqrt T L^2)\): up to a cutoff y the elementary absolute bound is \(\sum_{k\ge2,p^k\le y}\log p\ll\sqrt y(\log y)^2\). Prime2 is absent from I eventually and was already annihilated by the character. Consequently

\[
 \sup_{\chi\ne\chi_0,\ |u|\le L^D}|N_\chi(u)|
       \ll_{P,D}L^{-P}+T^{-1/2}L^2
       \ll_{P,D}L^{-P}.
 \tag{R15}
\]

This completes the requested endpoint clarification without any new hypothesis or research input.

## Exact energy normalization and compact center

The exact below-H orthogonality identity is unchanged:

\[
 \frac1{\phi(H)}\sum_\chi |B_{\chi,\lambda}(t)|^2
       =\frac1{Y^2V_H^2}\sum_{a\in\mathcal P}\eta(a/Y)^2
       \le\frac{Y/2+2}{Y^2V_H^2}.
 \tag{R16}
\]

Only a=b survives, and both marking and Mellin phases cancel. Also
\(|M_\chi(u)|\le\delta+1/T\). Choose fixed \(D>\max(B,C)\), so \(|t+v|\le L^D\) in (R3). Apply (R15) only to nonprincipal characters, then enlarge just the remaining B mean to all characters:

\[
 E_{\rm np}(\lambda,v)
 \le2L^B(\delta+T^{-1})^2
       \frac{Y/2+2}{Y^2V_H^2}
       \sup_{\chi\ne\chi_0,\ |u|\le L^D}|N_\chi(u)|^2
       \ll H^{-1}L^{B-2P}.
 \tag{R17}
\]

Taking 2P>=A+B proves (R4), uniformly in every real lambda. The separate product-support check is also preserved: rs<=25H/96<H, two ordered representations occur for distinct primes and one for a square. Its coefficients are -log(rs)/T^2 in the first case and -log r/T^2 in the second. Its exact character-averaged squared norm is therefore O(L^2/H). No independence assumption or exceptional-value count is used.

The effectivity qualification is unchanged. The real exception is excluded explicitly, so there is no Siegel-ineffective step. The imported displayed region, elementary inequalities and classical effective ordinary PNT give effective thresholds in the usual classical sense. No numerical threshold or constant was computed. In (R17) the explicit V_H^-2 may be retained without a PNT rate.

For v=lambda=0, ordinary PNT and partial summation on the fixed scaled supports give, uniformly for each fixed |t|<=K,

\[
 Y^{-it}B_{\chi_0}(t)=\frac{C_\eta(t)}{V_H\log Y}+o(L^{-1}),\quad
 T^{-it}M_{\chi_0}(t)=-\frac{J_\delta(t)}{\log T}+o(L^{-1}),\quad
 T^{-it}N_{\chi_0}(t)=J_\delta(t)+o(1).
 \tag{R18}
\]

The test functions have bounded variation uniformly on this compact time range; prime endpoints cost at most O(log T/T). As log Y~L, log T~L/2, V_H tends to v_alpha, the L^2-scaled dephased product tends uniformly to \(-2C_\eta J_\delta^2/v_\alpha\). Squaring gives factor4 and phi(H)^(-1)=2/H gives factor8 in (R6). Its integral is positive because \(C_\eta(0)>0\), \(J_\delta(0)=\delta>0\), and both are continuous. Only fixed compact time intervals are treated asymptotically. The entire growing-height E0 remains its exact definition.

## Final status and boundaries

The two critic clarifications are resolved in the new revision. Candidate1 and Candidate2 are proved at the stated assurance level and supported by the distinct written review. The positive compact principal contribution refutes the literal all-precision zero-centered total-energy extension on these changed polynomial arrays for A>4. It does not refute the accepted small-sift energy theorem.

The assumptions doing substantive work remain the power-of-two modulus and its explicit real-character patterns, the exact prime arrays, and the selected-label support below H. Including chi0 in (R15) fails because N_chi0(0) tends to delta. Allowing two labels separated by H changes the exact mean (R16). A repeated prime product has one ordered representation, not two. These are precise failure cases of unjustified extensions.

The result supplies the stated centered k=1 energy estimate and only its explicitly proved common-v/arbitrary-lambda extension. It does not establish other k, nontrivial fixed twists, other product rectangles, full signed fractional comparison or polynomial transport, polynomial-sieve Type I, identification of E0 with an original prime-pair main term, the pointwise original R/E0/H0 or F prime margin, or Goldbach. Multiplicative character orthogonality does not establish a pointwise additive prime count. The accepted small-sift arrays remain distinct from the polynomial prime arrays. Closest-work novelty, global breakthrough classification and goal completion remain unverified or unauthorized. The next missing mathematical result is the full comparison/transport and original prime-margin interface, outside this bounded round.
