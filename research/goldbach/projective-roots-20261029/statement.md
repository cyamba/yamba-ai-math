# Joint prescribed projective lines and moving complement ratios

29 October 2026. Registry role: Mathematician, `GOLDBACH-ROOTS-008`, author stage. Two bounded candidate statements are proved below, pending separate review: a finite joint count with an explicit absolute error, and its power-saving consequence in a specified aspect range. This does not attain every aspect ratio allowed by the brief. It uses the separately reviewed elementary complete-sum argument of RATIOS-007, rather than importing a variable-determinant version of the source appendix. No actual-prime, list-moment, Goldbach or novelty claim follows.

## Objects and endpoint convention

Let H>=2 be an integer, U,V>=2 real, and S>=1 squarefree with `(S,H)=1`. The brief takes S odd; the proof below allows the prime 2 as well. For each p dividing S prescribe a line `ell_p` in `P^1(F_p)`. Write

\[
 I_1=[a_1,b_1)\subset[1,16],\quad
 I_2=[a_2,b_2)\subset[1,2],\quad
 I_3=[a_3,b_3)\subset[0,1],\qquad L_i=b_i-a_i.
\]

All counts use these half-open intervals; empty intervals are allowed. Let N count primitive positive integer pairs P=(u,v), with `(uv,H)=1`, satisfying `u/U in I1`, `v/V in I2` and the following conditions. Let c=c_H be the unique integer in `[0,u)` with `vc=-H mod u` and set `d_H=(H+vc)/u`. Require

\[
 c/u\in I_3,\qquad
 \ker(u,c)\pmod p=\ell_p\quad(p\mid S).
\]

The inverse defining c exists because `(u,v)=1`. Since `(u,H)=1`, also `(u,c)=1`. Thus `G_H=[[u,c],[v,d_H]]` has determinant H and primitive first row. Modulo every p dividing S it is invertible, so its first-row kernel is well-defined. No individual-entry unit assumption modulo S is made.

Put

\[
 \tau_H=2^{\omega(H)},\quad \tau_R=2^{\omega(R)},\quad
 \kappa_b(H)=\zeta(2)^{-1}\prod_{\ell\mid H}\frac{\ell-1}{\ell+1}.
\]

## Candidate 1: a uniform finite count

**Proved, pending separate review.** For every fixed eta>0,

\[
 \boxed{N=\frac{UV L_1L_2L_3\kappa_b(H)}
                         {\prod_{p\mid S}(p+1)}
       +O_\eta\!\left(\tau_H
                   (U^{7/4+\eta}+V)\log^2(2U)\right).} \tag{1}
\]

The constant depends only on eta, not H,S, the lines, U,V or the intervals. There is no positive H power or omitted H-divisor cutoff. This is an absolute-error assertion; it is valid even if the population or some interval is empty, or its error exceeds its main term. The absence of an explicit S factor in this coarse absolute error is justified below by retaining the `tau_R` cost before its `1/R` prefactor is used.

### 1. Exact reduction of the line prescriptions

Partition S=QR, where p divides Q precisely when `ell_p=(1:0)`. A nonzero row `(u,c)` has this kernel exactly when `p|u`; then p does not divide c, because `(u,c)=1`. Every other line is uniquely `ell_p=(-rho_p:1)`. It imposes

\[
 p\nmid u,\qquad c=\rho_p u\pmod p.
\]

By CRT choose rho modulo R with these residues. Consequently the whole prescription is exactly

\[
 Q\mid u,\quad (u,R)=1,\quad c=\rho u\pmod R. \tag{2}
\]

This includes `rho_p=0`, when c is nonunit modulo p. It also includes arbitrary powers of p in u at primes dividing Q; only the prescribed divisibility by p is required. The argument never replaces the canonical representative c by a different complement lift modulo S.

### 2. The complete-sum input and the two Fourier norms

The reviewed elementary RATIOS-007 lemma, with its fourth-moment proof reconstructed there, is

\[
 |K_m(h,a)|\le C(m)m^{3/4}(h,a,m)^{1/4},\qquad
 C(m)=\left(2\tau_3(m)m/\phi(m)\right)^{1/4}. \tag{3}
\]

It applies to all m>=2 and all integer frequencies, including even m and nonunit or zero frequencies. Its proof counts the congruence `m|(x1+x2)(y1-x1)(y1-x2)`, uses a linear map with fibers of size at most two and at most `tau_3(m)` allocations, and then divides the fourth moment by a unit-scaling orbit of size `phi(m/(h,a,m))`. For every fixed epsilon>0, both C(m) and `sigma_{-3/4}(m)` are `O_epsilon(m^epsilon)`. No advanced Kloosterman theorem or full source result is a dependency.

Fix an admitted u, so `Q|u` and `(u,HR)=1`. Let f be the indicator of integers

\[
 c\in[a_3u,b_3u),\qquad c=\rho u\pmod R.
\]

These are the actual canonical c candidates, an arithmetic progression of step R in `[0,u)`. Regard f on residues modulo u without multiplicity. With `fhat(h)=sum_c f(c)e(-hc/u)`, the fact `(R,u)=1` permutes the Fourier frequencies of this progression and the geometric-series bound gives

\[
 \frac1u\sum_{h\pmod u}|\widehat f(h)|\ll\log(2u). \tag{4}
\]

Indeed its number of terms is at most u, its zero mode divided by u is at most one, and the other modes sum a harmonic series after that permutation. This remains valid for R>u and an empty progression.

Let g count the integers w in any real half-open interval of integer cardinality T, viewed periodically modulo u, with multiplicity when the interval spans periods. Its Fourier transform is the finite sum over those integers. For j nonzero modulo u,

\[
 |\widehat g(j)|\le\frac{u}{2\min(j,u-j)},\qquad
 \frac1u\sum_{1\le j<u}(j,u)^{1/4}|\widehat g(j)|
       \ll\sigma_{-3/4}(u)\log(2u). \tag{5}
\]

To see the weighted bound, majorize `(j,u)^{1/4}` by `sum_{e|u,e|j}e^{1/4}`. For e dividing u the sum over nonzero j divisible by e, after division by u, is `O(e^{-1} log(2u))`. Its coefficient is therefore `e^{-3/4}`, which gives (5). The missing j=0 term is treated exactly, rather than bounded by (5).

### 3. Completion at fixed u, including all H divisors

Expand v-coprimality as `1_(v,H)=1=sum_{b|rad(H),b|v}mu(b)` and put v=bw. Every b and H is a unit modulo u, and b is also a unit modulo S. The inverse relation becomes

\[
 wc=A_b\pmod u,\qquad A_b=-H b^{-1}\pmod u,
 \qquad (A_b,u)=1.
\]

For this b take g to be the w interval `[a_2V/b,b_2V/b)`. Finite Fourier expansion gives its pair count as

\[
 \frac1{u^2}\sum_{h,j\pmod u}
             \widehat f(h)\widehat g(j)K_u(h,jA_b).
\]

The j=0 contribution is exactly `(T/u) A_u`, where

\[
 A_u=\#\{c\in[a_3u,b_3u):c=\rho u\pmod R,\ (c,u)=1\}.
\]

For every j nonzero, including the terms h=0, the complete-frequency gcd is bounded by `(j,u)`, since A_b is a unit. Equations (3)-(5) therefore bound all the remaining terms by

\[
 O\!\left(C(u)u^{3/4}\sigma_{-3/4}(u)\log^2(2u)\right). \tag{6}
\]

This explicitly handles the zero c-frequency with nonzero w-frequency; it has not been dropped or assumed coprime. The relation `wc=A_b` itself makes c and w units modulo u, so it correctly enforces `(u,v)=1` without an additional assumption.

Replace T by `L2*V/b`, with error at most two. Since `A_u/u<=1`, this costs O(1) for each b. It covers empty intervals and arbitrarily large divisors b>2V as well. Summing every squarefree H divisor yields

\[
 N_u=\frac{VL_2}{u}\frac{\phi(H)}H A_u
 +O\!\left(\tau_H C(u)u^{3/4}
                         \sigma_{-3/4}(u)\log^2(2u)\right). \tag{7}
\]

No modulus H is inserted into an unproved arithmetic equidistribution theorem.

### 4. The canonical c mass and the weighted u mass

Because `(R,u)=1`, ordinary Mobius inversion over divisors of u gives

\[
 A_u=\frac{L_3\phi(u)}R+O(\tau(u)). \tag{8}
\]

For each divisor e of u, the two congruences `e|c` and `c=rho*u mod R` form one class modulo eR, with interval count `L3*u/(eR)+O(1)`. This proves (8) even when c or rho is nonunit modulo R. The associated summed error in (7) is

\[
 O\!\left(V\frac{\phi(H)}H
               \sum_{u\le16U}\frac{\tau(u)}u\right)
       =O(V\log^2(2U)). \tag{9}
\]

For completeness set M0=HR and let

\[
 W=\sum_{a_1U\le u<b_1U,\ Q\mid u,\ (u,M_0)=1}\frac{\phi(u)}u.
\]

Expand `phi(u)/u=sum_{d|u}mu(d)/d`. Only d coprime to M0 can contribute. Multiples of `lcm(Q,d)` in the interval that are coprime to M0 number

\[
 \frac{L_1U}{\operatorname{lcm}(Q,d)}\frac{\phi(M_0)}{M_0}
                  +O(2^{\omega(M_0)}).
\]

Sum the error against 1/d through d<=16U. Extending the main reciprocal-square series costs O(1), since `(Q,d)/(Qd^2)<=1/d^2`. Therefore

\[
 W=L_1U\zeta(2)^{-1}
       \prod_{p\mid HR}\frac p{p+1}
       \prod_{p\mid Q}\frac1{p+1}
       +O(\tau_H\tau_R\log(2U)). \tag{10}
\]

Here the local product follows directly from

\[
 \frac{\phi(M_0)}{M_0Q}
 \sum_{(d,M_0)=1}\frac{\mu(d)(Q,d)}{d^2}.
\]

The prime factors of Q are disjoint from HR, so a Q prime changes its Euler factor from `1-1/p^2` to `1-1/p`, and the outside 1/Q supplies the remaining 1/p. This is why its factor is `1/(p+1)`, including the cases p divides u.

The prefactor multiplying W in (7)-(8) is `VL2L3*phi(H)/(HR)`. Thus its error is explicitly

\[
 O\!\left(\frac VR\frac{\phi(H)}H
                    \tau_H\tau_R\log(2U)\right). \tag{11}
\]

The cost of excluding R is present. Only now use `tau_R/R=prod_{p|R}(2/p)<=1` to absorb it into `O(V tau_H log(2U))`. There is no unsupported claim that this exclusion was free. Multiplying the main factors in (10) by `phi(H)/(HR)` gives exactly

\[
 \frac{\kappa_b(H)}{\prod_{p\mid S}(p+1)}.
\]

Finally sum (6)-(7) over u. The elementary subpower bounds for `C(u) sigma_{-3/4}(u)` give, for every fixed eta>0, the error `O_eta(tau_H U^{7/4+eta}log^2(2U))`. Combining it with (9) and (11) proves (1). Its treatment of prime powers in u, all H divisors, nonunit row entries and all line types is explicit.

## Candidate 2: a power-saving joint range

**Proved consequence of (1), pending separate review.** Let X tend to infinity, `2<=H<=X^A`, and `S<=exp(C(log X)^0.98)` with fixed positive A,C and `(S,H)=1`. Suppose U and V are comparable, up to fixed positive constants, to `X^a` and `X^b`, with fixed `a,b>0` and

\[
 b>3a/4,\qquad \gamma=\min\{a,b-3a/4\}>0.
\]

Uniformly in the prescribed lines and the three intervals,

\[
 N=\frac{UV L_1L_2L_3\kappa_b(H)}{\prod_{p\mid S}(p+1)}
                   +O\!\left(UV X^{-\gamma+o(1)}\right). \tag{12}
\]

As usual this means any fixed positive slack in the exponent, with constants depending on that slack and the fixed parameters. Indeed `tau_H=X^{o(1)}` uniformly for H<=X^A. Choose eta small enough for any requested slack in (1). The product `prod_{p|S}(p+1)` and `kappa_b(H)^{-1}` are also `X^{o(1)}`. For fixed positive interval lengths the main term is `UV X^{-o(1)}`, so (12) is a relative power saving and the population is eventually nonempty. For shrinking or empty intervals it remains an absolute estimate without a promised relative error or division by the population.

In balanced boxes U,V comparable to `X^a`, gamma is a/4. In the Goldbach-sized example H comparable to X and U,V comparable to sqrt(X), it is 1/8. These conclusions have unspecified asymptotic constants and thresholds, rather than numerical certification at any finite X.

## Exact limitation and next obligation

The finite formula (1) holds for every aspect ratio, but its normalized error contains `U^{3/4+eta}/V`. If `b<=3a/4`, it does not provide the negative power requested for all boxes in the brief. This is a precise failure of this absolute-completion estimate to certify that broader claim, not a counterexample to the proposed main term or a lower bound for the actual error. No all-aspect theorem has been proved here. A transposed inverse relation would introduce a moving real phase involving `H/(uv)`; controlling it uniformly without a positive H cost would require a further argument. No such argument is imported from determinant-one appendix (A.5).

The proof establishes a joint prescribed-line and ratio count over unweighted primitive positions. It does not assert equidistribution in every individual thin projective line with a relative error, sum high moments over growing lists, or bound the resulting centered operator with actual prime coefficients. The changed denominator-H major part from SECTORS-006, actual-prime correlations, polynomial-rough nonzero centers and the h=1 prime boundary remain open.

RATIOS-007 and its inspected closest work already document stronger classical Weil input and inverse-distribution methodology. This derivation is a scoped specialization, with novelty unverified. The full Lue-Wang-Wu theorem and a variable-H version of its appendix are not assumed. The next concrete use would need to insert (12), with its aspect restriction and every prescription-density and error cost, into an actual list/path-moment expansion and check that the accumulated error is smaller than the required centered main scale. No Goldbach lower bound, solution or demonstrated breakthrough follows from the present result.
