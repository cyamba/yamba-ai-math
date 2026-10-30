# Principal-centered energy for the balanced prime arrays

29 October 2026. Actual registry Mathematician, GOLDBACH-CENTERED-018, propose stage. Two candidates are proved below relative to the explicitly named classical theorem statements, pending the distinct substantive critic. Assurance is an author derivation, not a formal proof or an audit of the published proofs. Usage is unknown. No experiment, paid call, publication, external message or change to frozen 008-017 evidence was performed.

The actual BOUNDARY-017 statement was read as research data, not as an accepted theorem. Its proposed principal obstruction is rederived here for this exact family. The actual ENERGY-012 endpoint Perron argument and its definitions were inspected; the reconstruction below supplies its all-nonprincipal strip directly and avoids importing its small-sift coefficient cancellation, Burgess argument, marking moments or major-comparison conclusion.

## Definitions and classical inputs

Let H=2^ell tend to infinity, L=log H, alpha in [3/10,1/3), delta=1/4, T=sqrt(H/6), Y=H/3, and I=[T,(1+delta)T], with both endpoints included. Let eta be a fixed nonzero real smooth function, 0<=eta<=1, compactly supported in (2,5/2). Write P_I for the primes in I and

\[
 V_H=\sum_{H^\alpha<a<H,\ a\ {m prime},\ (a,H)=1}a^{-1}.
 \tag{1}
\]

The selected labels have 2Y<a<(5/2)Y, hence H/2<a<H. All supported primes are odd and are H-units eventually. The full normalizer (1), rather than a selected-dyad reciprocal mass, is used throughout. There is no 1/a in a selected-label counting sum.

For the stated polynomial factorwise sieve, T>H^alpha and (1+delta)T<H^(2alpha) eventually, because alpha<1/2 and 2alpha>1/2. A composite integer whose prime factors all exceed H^alpha exceeds H^(2alpha). Thus the sift on I forces primality. In the present brief V0=(T^2)^(1/5)<T, so the actual coefficients on the surviving primes are exactly -1 and log s. BOUNDARY-017 instead set V0=(7T^2/8)^(1/5); these are different thresholds, both below I and both giving the same prime coefficient log s. No equality of the two inherited parameters or transfer of the full Vaughan interface is asserted here.

For chi modulo H define

\[
 B_\chi(t)=\frac1{YV_H}\sum_{a\ {m prime}}\eta(a/Y)\chi(a)a^{it},\quad
 M_\chi(t)=-\frac1T\sum_{r\in P_I}\chi(r)r^{it},\quad
 N_\chi(t)=\frac1T\sum_{s\in P_I}(\log s)\chi(s)s^{it}.
 \tag{2}
\]

For fixed B>0 put T0=L^B. With chi0 the principal character, E_np and E0 are exactly

\[
 E_{\rm np}=\frac1{\phi(H)}\sum_{\chi\ne\chi_0}
       \int_{-T0}^{T0}|B_\chi(t)M_\chi(t)N_\chi(t)|^2dt,
 \quad E_0=\frac1{\phi(H)}\int_{-T0}^{T0}|B_{\chi_0}M_{\chi_0}N_{\chi_0}|^2dt.
 \tag{3}
\]

Here phi(H)=H/2 and E_total=E0+E_np is an exact nonnegative decomposition.

The imported number-theoretic statements are:

* **Established, original statement visually inspected:** H. Iwaniec, *On Zeros of Dirichlet's L Series*, Inventiones Mathematicae 23 (1974), 97-104, Theorem 2 on journal page 97. For q>=3, d=rad(q), h=log(q(|t|+3)), its region Re(s)>1-theta has
  theta^(-1)=4*10^4[log d+(h log(2h))^(3/4)]. At most one nonprincipal character modulo q has a zero there; such a character is real and its zero is real and simple. The original local render `.runs/goldbach-source-inputs-20261029/iwaniec-journal97.png` was inspected in this author stage. The PDF SHA256 is `d98fe83def66ce90801760710d21f34458637d32de6ac77d726698220ae25832`; the render hash is `88a60c54861c6a83a57e21186f09eeed080e2b487e4a368f9ea6267629648a61`. [Original journal volume, PDF page104](https://gdz.sub.uni-goettingen.de/download/pdf/PPN356556735_0023/PPN356556735_0023.pdf#page=104). Its full proof was not audited.
* **Established, primary statement inspected in parsed original PDF:** Koukoulopoulos, *The Distribution of Prime Numbers*, author-provided preliminary version, Theorem 8.1, printed page84/PDF95: pi(x)=li(x)+O(x exp(-c sqrt(log x))) for a positive absolute c. [Author-provided book, PDF page95](https://www.dms.umontreal.ca/~koukoulo/documents/publications/primes.pdf#page=95). The local PDF SHA256 is `1445e107bba9c89db6529aeb4bca3ecf01170fc2854a675f5ca6f288c77ea0a8`. The classical proof and numerical constants were not audited or computed. Only ordinary PNT and an eventual positive bound for V_H are needed.

Elementary character orthogonality, periodic partial summation, Euler products on Re(s)>1, Borel-Caratheodory, Cauchy's derivative estimate and Perron's contour kernel are used with their arguments below. No functional-equation, Hadamard-product or uninspected local-zero-density input is needed in this proof. The completed-L passage inspected in ENERGY-012 is therefore not an additional dependency.

PNT and partial summation give

\[
 V_H=\log(1/\alpha)+o(1)=:v_\alpha+o(1).
 \tag{4}
\]

Indeed the endpoint terms pi(x)/x at H and H^alpha are O(1/L); the remaining integral is (1+o(1)) integral_(H^alpha)^H dx/(x log x)=log(1/alpha)+o(1). The relative PNT error is uniformly o(1) on that growing range. Deleting the prime2 changes nothing eventually. In particular V_H stays in a positive compact interval. This derivation does not assume a harmonic-prime theorem with an unrecorded normalization.

## Candidate 1: the nonprincipal saving, with the principal energy retained

**Proved, pending distinct review.** For every fixed A>0 and B>0,

\[
 E_{\rm np}(H)\ll_{A,B,\alpha,\eta} H^{-1}L^{-A}.
 \tag{5}
\]

Thus E_total(H)=E0(H)+O_(A,B,alpha,eta)(H^(-1)L^(-A)), with E0 exactly (3). This is a positive centered-energy statement, not a zero-centered estimate for E_total.

The same proof gives a derived uniform extension inside this candidate. Define

\[
 B_{\chi,\lambda}(t)=\frac1{YV_H}\sum_{a\ {m prime}}
       \eta(a/Y)e(-\lambda a/Y)\chi(a)a^{it},\quad e(x)=e^{2\pi ix},
 \tag{6}
\]

and replace M_chi(t),N_chi(t) in the integrand by M_chi(t+v),N_chi(t+v). For each fixed C>0, (5) is uniform over |v|<=L^C and every real lambda. The sum still excludes chi0 and has k=1 and trivial fixed character twists. The center for this extended family is its exact principal term; only v=lambda=0 has the compact asymptotic in Candidate 2.

### Every real exception is excluded explicitly

A real character is trivial on odd squares. Every odd residue congruent to1 modulo8 is a square modulo2^ell: starting with a root modulo8, if x^2 equals the desired residue modulo2^n, replacing x by x+epsilon*2^(n-1), epsilon in {0,1}, changes its square by epsilon*x*2^n modulo2^(n+1), and so lifts the root. Thus any real character modulo2^ell factors through8. Its three nonprincipal possibilities have the following signs on the odd residues (1,3,5,7):

\[
 \chi_{-4}:(+,-,+,-),\quad
 \chi_8:(+,-,-,+),\quad
 \chi_{-8}:(+,+,-,-).
 \tag{7}
\]

They have primitive conductors4,8,8. There is no missing Euler prime upon induction to H: the only prime dividing H is2 and it already divides each conductor. Hence their L-functions modulo H equal the corresponding fixed primitive L-functions, including at real points by continuation.

For every real sigma>0, put f(x)=x^(-sigma). Periodic partial sums are bounded, so these Dirichlet series converge, and grouping successive complete periods preserves their sum. For chi_-4 every block is f(4n+1)-f(4n+3)>0. With x=8n+1, chi_8 has block

\[
 [f(x)-f(x+2)]-[f(x+4)-f(x+6)]>0,
 \tag{8}
\]

because sigma*u^(-sigma-1) is strictly decreasing. The chi_-8 block is [f(x)-f(x+4)]+[f(x+2)-f(x+6)]>0. Each grouped series is absolutely convergent, as its block is O_sigma((n+1)^(-sigma-1)). Therefore all three L(sigma,chi) are strictly positive for every sigma>0. In particular nonvanishing at1 and throughout a real neighborhood is proved, with no ineffective continuity constant or unproved assertion about a possible exceptional zero.

Apply Iwaniec at the actual modulus q=H. Uniformly for |t|<=L^D, fixed D, h<=2L eventually and d=2. Consequently

\[
 \theta\gg_D L^{-3/4}(\log L)^{-3/4},\qquad
 \frac{\theta}{K\log L/L}\longrightarrow\infty
 \tag{9}
\]

for every fixed K. Any zero allowed in Iwaniec's region would, by that theorem, be a real zero of one of (7); the region has positive real part and (8) excludes it. Thus for every fixed K,D, every nonprincipal chi modulo H has no zero in the closed rectangle

\[
 \sigma\ge1-K\log L/L,\qquad |t|\le L^D
 \tag{10}
\]

for all sufficiently large powers of two. The closure is valid because its width is strictly smaller than the printed open-region width. The principal character is excluded throughout this argument.

### Elementary logarithmic derivative in the narrow rectangle

Here is an alternative to the local-zero-count/Hadamard step of ENERGY-012. For nonprincipal chi modulo H let A_chi(x)=sum_(n<=x)chi(n). Its complete-period sum is0, |A_chi(x)|<=H, and A_chi(H)=0. For Re(s)>0, partial summation gives an analytic continuation

\[
 L(s,\chi)=\sum_{n\le H}\chi(n)n^{-s}
                 +s\int_H^\infty A_\chi(x)x^{-s-1}\,dx.
 \tag{11}
\]

For fixed K,D, on sigma>=1-K log L/L, sigma>=1/2 and |Im(s)|<=L^D+1, the finite sum is bounded by 1+L max(1,H^(1-sigma)), and the integral by |s|H^(1-sigma)/sigma. Thus |L(s,chi)|<=L^O_(K,D)(1), uniformly in chi.

Set w=K log L/L. In the zero-free disk of radius2w centered at z0=1+w+i*tau, an analytic logarithm g=log L exists. Choose its value at z0 by the absolutely convergent Euler logarithm. Then |g(z0)|<=log zeta(1+w)=O(log L), and Re(g)=log|L|<=O_(K,D)(log L) by (11). Borel-Caratheodory bounds |g|=O_(K,D)(log L) in radius7w/4: explicitly its usual inequality follows by applying the Schwarz lemma to the analytic quotient mapping Re(g)<=M into the unit disk, and gives a constant times M+|g(z0)| at any fixed smaller radius. Cauchy's derivative estimate on a disk of radius w/4 around each point at distance<=3w/2 from z0 therefore gives

\[
 |L'/L(s,\chi)|\ll_{K,D}\frac{\log L}{w}\ll_{K,D}L^2
 \tag{12}
\]

for 1-w/2<=Re(s)<=1+1/L. Disks and their boundaries lie in (10); choose its height with a fixed margin. This uses only nonprincipal periodicity and the proved zero-free rectangle. It introduces no principal pole and does not require choosing a height avoiding zeros.

### Endpoint Perron and prime-power corrections

Fix any requested P>0 and frequency ceiling |u|<=L^D. Choose fixed K>=12(P+5) and D2>max(D+2,P+5). Set c=1+1/L, sigma0=1-K log L/(2L), and R=L^D2/2. The disks for (12) at all contour points s-iu lie inside (10) with height L^D2 eventually. For H^(1/6)<=y<=H, truncated Perron for F(s)=-L'/L(s-iu,chi), at a half-integer endpoint with the same integer cutoff, yields

\[
 \sum_{n\le y}\Lambda(n)\chi(n)n^{iu}
 =\frac1{2\pi i}\int_{c-iR}^{c+iR}F(s)\frac{y^s}{s}\,ds
             +O(yL^2/R+L^2).
 \tag{13}
\]

For completeness the kernel obtained by closing the integral of z^s/s has error O(z^c min(1,(R|log z|)^(-1))). With |Lambda(n)chi(n)n^(iu)|<=log n, summing near the endpoint uses |log(y/n)| comparable to |y-n|/y and a harmonic sum; the far tail is bounded by sum_n (log n)n^(-1-1/L)=O(L^2). These give the error in (13). Moving a cutoff by at most one to a half-integer changes its main endpoint factors by a harmless O(L^2) term, or equivalently one first proves the formula for half-integers representing each fixed integer cutoff. This covers either included endpoint of I without a short-interval PNT assumption.

Shift to sigma0. No zero or pole is crossed: chi is nonprincipal and (10) holds. Bound (12) gives vertical contribution O(y^sigma0 L^3) and horizontal contribution O(yL^2/R). Since log y>=L/6,

\[
 \sum_{n\le y}\Lambda(n)\chi(n)n^{iu}
 \ll yL^{3-K/12}+yL^{3-D2}+L^2
 \ll_P yL^{-P}
 \tag{14}
\]

after increasing the eventual threshold. The last L^2 term is negligible uniformly for y>=H^(1/6). Formula (14) is an endpoint bound; subtracting it at the two endpoints of I costs O(T L^(-P)), not a bound relative to an arbitrarily shorter interval.

For every nonprincipal character the primitive inducing conductor is an even power of two, at least4. Induction deletes no additional prime, so (11)-(14) have no omitted imprimitive Euler correction. Prime powers remain in (14). Their total absolute contribution up to y is at most

\[
 \sum_{k\ge2,\ p^k\le y}\log p\ll \sqrt y(\log y)^2.
 \tag{15}
\]

This follows by counting integers p<=y^(1/k), using log p<=log y and at most O(log y) exponents. Removing them and taking the difference of the two endpoints of I gives, for every fixed P,D,

\[
 \sup_{\chi\ne\chi_0,\ |u|\le L^D}|N_\chi(u)|
       \ll_{P,D}L^{-P}+T^{-1/2}L^2\ll_{P,D}L^{-P}.
 \tag{16}
\]

The prime2 never belongs to I eventually. Its character values were zero already; no unsifted or missing-unit term is silently discarded.

### Exact mean values and assembly

All labels in (6) are distinct integers strictly between0 and H and are units. Exact character orthogonality therefore gives, for every real t and lambda,

\[
 \frac1{\phi(H)}\sum_\chi|B_{\chi,\lambda}(t)|^2
 =\frac1{Y^2V_H^2}\sum_{a\ {m prime}}\eta(a/Y)^2
 \le\frac{Y/2+2}{Y^2V_H^2}\ll_\alpha H^{-1}.
 \tag{17}
\]

Both phases disappear on the exact diagonal a=b. There is no residual factor phi(H), 1/a or 1/H in this identity. Also |M_chi(u)|<=(delta T+1)/T for every chi,u.

As a separate normalization check, every product r*s is <=(25/16)T^2=25H/96<H. In M_chi(u)N_chi(u) its coefficient is

\[
 c(n)=-T^{-2}\sum_{r,s\in P_I,\ rs=n}\log s.
 \tag{18}
\]

Unique factorization gives at most two ordered representations. For distinct primes r,s the coefficient is -log(rs)/T^2, and for r=s it is -log r/T^2. Thus (again exactly)

\[
 \phi(H)^{-1}\sum_\chi|M_\chi(u)N_\chi(u)|^2
      =\sum_n|c(n)|^2\ll L^2/T^2\ll L^2/H.
 \tag{19}
\]

The diagonal square has one representation, not two. This check is not needed to improve (17), and no stochastic independence or unproved exceptional-character count is used.

For the extension (6), |t+v|<=L^B+L^C<=L^D with fixed D>max(B,C). Apply (16) only to the nonprincipal terms, use the trivial bound for M, and then enlarge the remaining B sum to all characters in (17). This proves the finite-H bound

\[
 E_{\rm np}(\lambda,v)
 \le 2L^B(\delta+T^{-1})^2
       \frac{Y/2+2}{Y^2V_H^2}
       \sup_{\chi\ne\chi_0,\ |u|\le L^D}|N_\chi(u)|^2
 \ll_{P,B,C,\alpha,\eta} H^{-1}L^{B-2P}.
 \tag{20}
\]

Taking 2P>=A+B proves (5) and its claimed uniform extension. The full V_H^-2 is visible before (4) is applied. No small-sift theorem has been transplanted to these arrays.

The proof has no Siegel-ineffective exceptional-zero step: (7)-(8) exclude the possible exception explicitly. Iwaniec's displayed region and the elementary estimates give effective constants and thresholds in the usual classical sense, as does the classical effective PNT used for the eventual bound on V_H. No numerical threshold or numerical constants are supplied. The finite-H inequality (20), with V_H retained, does not itself need a PNT rate.

## Candidate 2: an explicit principal center on compact time intervals

**Proved, pending distinct review.** This candidate concerns exactly v=lambda=0. For each fixed K>0 define

\[
 C_\eta(t)=\int_2^{5/2}\eta(u)u^{it}\,du,\qquad
 J_\delta(t)=\int_1^{1+\delta}u^{it}\,du.
 \tag{21}
\]

For |t|<=K, ordinary PNT and partial summation give, uniformly on this compact interval,

\[
 Y^{-it}B_{\chi_0}(t)=\frac{C_\eta(t)}{V_H\log Y}+o(L^{-1}),\quad
 T^{-it}M_{\chi_0}(t)=-\frac{J_\delta(t)}{\log T}+o(L^{-1}),\quad
 T^{-it}N_{\chi_0}(t)=J_\delta(t)+o(1).
 \tag{22}
\]

Indeed the normalized test functions eta(u)u^(it) and u^(it) have uniformly bounded size and total variation for |t|<=K. Integrating the PNT error by parts on the fixed scaled supports gives the displayed uniform errors; an included prime endpoint contributes only O(log T/T). Replacing 1/log(Yu),1/log(Tu) by 1/log Y,1/log T costs O(L^(-2)) after normalization. There is no assertion of growing-height uniform PNT here.

As log Y/L tends to1, log T/L tends to1/2 and V_H tends to v_alpha, (22) implies uniformly on this compact interval

\[
 L^2(YT^2)^{-it}B_{\chi_0}(t)M_{\chi_0}(t)N_{\chi_0}(t)
       \longrightarrow-\frac2{v_\alpha}C_\eta(t)J_\delta(t)^2.
 \tag{23}
\]

Consequently its exact compact principal energy has the asymptotic

\[
 \frac1{\phi(H)}\int_{-K}^K|B_{\chi_0}M_{\chi_0}N_{\chi_0}|^2dt
 =\frac8{v_\alpha^2HL^4}
       \int_{-K}^K|C_\eta(t)|^2|J_\delta(t)|^4dt
          +o_K(H^{-1}L^{-4}).
 \tag{24}
\]

The integral is strictly positive: C_eta(0)=integral eta>0 and J_delta(0)=delta>0, and both transforms are continuous. Since K<=L^B eventually, the exact E0 in (3) is therefore >=c_(alpha,eta,K)/(H L^4). Formula (24) describes only the fixed compact part; E0 itself remains the exact growing-height expression (3). No total growing-height asymptotic is asserted. In particular (24) independently refutes the literal all-A zero-centered estimate for E_total for A>4 on this changed polynomial-sifted input.

## Failure cases, review question and remaining arithmetic obligation

The support below H in (17) does real work: if labels a and a+H were allowed together, orthogonality would retain their off-diagonal term and (17) would change. The principal exclusion in (16) does real work: PNT gives N_chi0(0) tending to delta, which falsifies any uniform all-character logarithmic saving. Treating the coincident r=s case in (18) as two ordered representations would be an exact multiplicity error. Positivity of the grouped real L-series and Iwaniec's precise character scope are the load-bearing arithmetic steps for all-nonprincipal uniformity.

The distinct review should check the zero-free-region quantifiers, the analytic-log disk margin in (12), the half-integer endpoint error in (13), and the factor8 in (24). The next bounded proof obligation for this theorem is that substantive review, not an experiment. A proposed extension to a different modulus, nontrivial fixed twists or a different label support must first recheck the real exception, inducing conductor, exact residue multiplicity and center. No numerical observation is used as evidence of a theorem.

This proves a genuine centered energy saving for the stated k=1 family, including the explicitly derived common v and marking-lambda extension. It does not estimate other k, nontrivial fixed character twists, different product rectangles, the full signed fractional comparison, polynomial-sieve Type I, the original pointwise R/E0/H0 or F prime margin, or Goldbach. The one-prime-sum center E0 is not identified with the unknown prime-pair count or with a main term of that full comparison. Multiplicative character orthogonality does not give pointwise additive prime-pair information. The accepted small-sift arrays and these polynomial-sifted prime arrays remain distinct. Closest-work novelty is unverified; no global breakthrough or goal-completion claim follows.
