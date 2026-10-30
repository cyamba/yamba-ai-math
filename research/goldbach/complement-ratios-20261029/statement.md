# Uniform averaging of the moving complement ratio

29 October 2026. Registry role: Mathematician, `GOLDBACH-RATIOS-007`. This gives a complete limited arithmetic argument, pending separate review. It reconstructs the elementary complete-sum input suggested by the inspected [Lue-Wang-Wu appendix, equation (A.2)](https://arxiv.org/html/2610.20242v1), without importing that paper's full theorem or root-averaging claim. It proves cancellation for unweighted primitive positions, not for a prime-complement sequence, prescribed prime lists, or high path moments. No Goldbach proof, demonstrated breakthrough, or novelty claim is made.

## Definitions and two candidate results

Let H>=2 be an integer and U,V>=2 be real. For a primitive integer position P=(u,v), choose an integral complement (c,d) satisfying u*d-v*c=1 and put r_P=c/u modulo 1. Thus c is congruent to -v^(-1) modulo u. The choice of complement changes r_P by an integer only.

Let P(H;U,V) consist of positions with U<=u<=16U, V<=v<=2V, gcd(u,v)=1 and gcd(uv,H)=1. Write N0 for its cardinality and, for nonzero integer k,

\[
S(H,k;U,V)=\sum_{P\in\mathcal P(H;U,V)}e(kH r_P).
\]

All interval endpoints are interpreted literally; the estimates include integer-rounding errors. Let tau_H=2^omega(H), tau(n) be the divisor count and sigma_s(n)=sum_{d|n}d^s. Set

\[
\kappa_b(H)=\frac1{\zeta(2)}\prod_{\ell\mid H}\frac{\ell-1}{\ell+1}.
\]

The first candidate is a finite complete-sum bound with an explicit divisor factor. The second is its interval-completion consequence, including a discrepancy estimate with a nonempty moving-H range.

## 1. Elementary complete Kloosterman estimate

For m>=2 and integer h,a put

\[
K_m(h,a)=\sum_{x\ ({\rm mod}\ m),\ (x,m)=1}
                     e((hx+a x^{-1})/m),\qquad
C(m)=\left(2\tau_3(m)\frac{m}{\phi(m)}\right)^{1/4}.
\]

Here tau3 is the number of ordered factorizations into three positive integers. Then

\[
\boxed{|K_m(h,a)|\le C(m)m^{3/4}\gcd(h,a,m)^{1/4}.} \tag{1}
\]

In particular, for every fixed eta>0, C(m)<<_eta m^eta. Formula (1) permits even m, zero frequencies, and frequencies sharing factors with m.

**Proof.** Additive orthogonality gives

\[
\sum_{h,a\ ({\rm mod}\ m)}|K_m(h,a)|^4=m^2 T_m,
\]

where T_m counts unit quadruples x1,x2,y1,y2 with x1+x2=y1+y2 and x1^(-1)+x2^(-1)=y1^(-1)+y2^(-1) modulo m. Substitute y2=x1+x2-y1. Clearing the unit denominators shows

\[
m\mid(x1+x2)(y1-x1)(y1-x2).
\]

The linear map from (x1,x2,y1) to those three factors has kernel of size at most two: its kernel is (t,-t,t), with 2t=0 modulo m. Every residue triple whose product is divisible by m admits a factor allocation d1*d2*d3=m with di dividing its i-th entry. For each allocation there are m^2 residue triples, since their number is product(m/di). A union bound therefore gives

\[
T_m\le2m^2\tau_3(m),\qquad
\sum_{h,a}|K_m(h,a)|^4\le2m^4\tau_3(m). \tag{2}
\]

For a unit s modulo m, changing x to s*x gives K_m(h*s,a*s^(-1))=K_m(h,a). Put g=gcd(h,a,m). The stabilizer of this pair is s=1 modulo m/g. Indeed the two congruences on s-1 are equivalent to that one condition. Reduction of units modulo m onto units modulo m/g is surjective, prime by prime, so the orbit has size phi(m/g). Using its contribution to (2),

\[
|K_m(h,a)|^4\le\frac{2m^4\tau_3(m)}{\phi(m/g)}
 \le 2m^3g\tau_3(m)\frac m{\phi(m)}.
\]

The last inequality uses (m/g)/phi(m/g)<=m/phi(m). This is (1). The subpower bound for C(m) follows from the elementary divisor bounds and the analogous bound for m/phi(m), by separating finitely many small primes. This proof uses no external Kloosterman theorem. □

## 2. Interval completion with the moving multiplier

For a fixed admitted u, let c_u(k)=sum_{x mod u,(x,u)=1}e(kx/u), the Ramanujan sum. The fixed-u formula is

\[
\boxed{S_u=\frac Vu\frac{\phi(H)}H c_u(k)
 +O\!\left(\tau_H C(u)u^{3/4}\gcd(k,u)^{1/4}\log(2u)\right).} \tag{3}
\]

Its implied constant is absolute. In (3), S_u sums over the v interval with gcd(v,uH)=1 and phase e(-kH*v^(-1)/u). No assumption that k is a unit is made, and H need not be small.

### Completion proof and large H divisors

Expand 1_(v,H)=1=sum_{d|rad(H),d|v}mu(d) and put v=d*w. Since gcd(u,H)=1, every such d and H is a unit modulo u, and the inverse coefficient is

\[
a_d=-kH d^{-1}\pmod u,\qquad
\gcd(a_d,u)=\gcd(k,u). \tag{4}
\]

The w interval is [V/d,2V/d]. For any integer interval of length L, finite Fourier expansion modulo u gives its inverse sum as

\[
\frac L u c_u(a_d)+\frac1u
 \sum_{h=1}^{u-1}K_u(h,a_d)
                         \sum_{w\text{ in interval}}e(-hw/u).
\]

The usual geometric-series inequality gives

\[
\frac1u\sum_{h=1}^{u-1}
 \left|\sum_w e(-hw/u)\right|\ll\log(2u),
\]

because the h term is at most u/(2*min(h,u-h)). This is valid for short, empty or many-period intervals. Applying (1), using gcd(h,a_d,u)<=gcd(k,u), bounds the nonzero-frequency part uniformly by C(u)u^(3/4)gcd(k,u)^(1/4)log(2u).

The integer length differs from V/d by at most two. Its zero-frequency correction is O(|c_u(a_d)|/u)=O(1), absorbed by the displayed error. In particular divisors d>2V, whose interval is empty, are included legitimately: their proposed main term is bounded by V/d<1, and that rounding error accounts for it. There is no unrecorded truncation of the H divisors.

Multiplication of the Ramanujan frequency by a unit, or by -1, leaves its value unchanged. Thus c_u(a_d)=c_u(k). Finally sum mu(d)/d over all divisors of rad(H), obtaining phi(H)/H. Summing the errors over their tau_H choices proves (3). □

### Sum over u, including common frequency factors

For every fixed eta>0, summation of (3) yields

\[
\boxed{\begin{split}
S(H,k;U,V)
&=V\frac{\phi(H)}H
 \sum_{U\le u\le16U,\ (u,H)=1}\frac{c_u(k)}u\\
&\quad+O_\eta\!\left(\tau_H\sigma_{-3/4}(|k|)
                        U^{7/4+\eta}\log(2U)\right).
\end{split}} \tag{5}
\]

To justify the frequency factor, gcd(k,u)^(1/4)<=sum_{d|k,d|u}d^(1/4). A divisor d<=16U has at most 15U/d+1<=31U/d multiples in the u interval. Therefore

\[
\sum_{U\le u\le16U}\gcd(k,u)^{1/4}
 \le31U\sigma_{-3/4}(|k|).
\]

Together with C(u)<<_eta U^eta this proves the error in (5). The coprimality restriction in that error sum can be discarded in an upper bound.

The Ramanujan identity c_u(k)=sum_{d|gcd(u,k)}d*mu(u/d), obtained by expanding the unit indicator, also gives

\[
\sum_{U\le u\le16U}\frac{|c_u(k)|}u\ll\tau(|k|).
\]

For each d|k, the remaining harmonic sum is over an interval [U/d,16U/d] and is bounded by an absolute constant; when d>U its upper endpoint is at most 16. Consequently

\[
\boxed{|S(H,k;U,V)|\ll_\eta
 V\tau(|k|)+\tau_H\sigma_{-3/4}(|k|)
                         U^{7/4+\eta}\log(2U).} \tag{6}
\]

The explicit main term in (5) should not be silently discarded at fixed u. For example, if u divides k its complete inverse frequency is zero and c_u(k)=phi(u). Formula (6) sums such possibilities through their actual divisor cost rather than assuming gcd(k,u)=1.

## Correct primitive both-unit mass

Independently of the sector statement, an elementary count gives

\[
\boxed{N_0=15UV\kappa_b(H)
         +O\bigl(\tau_H(U+V)\log(2U)\bigr).} \tag{7}
\]

**Proof.** At fixed u coprime to H, counting integers v coprime to uH by inclusion-exclusion gives

\[
V\frac{\phi(u)}u\frac{\phi(H)}H
                     +O\bigl(\tau_H\tau(u)\bigr).
\]

The sum of these errors over u is O(tau_H*U*log(2U)). For the main sum expand phi(u)/u=sum_{d|u}mu(d)/d. Only d coprime to H occur. The number of its multiples in [U,16U] that are coprime to H is 15U*phi(H)/(dH)+O(tau_H), so

\[
\sum_{U\le u\le16U,\ (u,H)=1}\frac{\phi(u)}u
 =15U\frac{\phi(H)}H
       \sum_{(d,H)=1}\frac{\mu(d)}{d^2}
                           +O(\tau_H\log(2U)).
\]

Extending the reciprocal-square series costs O(1) here. Its Euler product, multiplied by (phi(H)/H)^2, is exactly kappa_b(H). Multiplication by V*phi(H)/H proves (7). □

This retains the target-dependent local density. In particular it is not the fixed odd-parity constant from a fixed-shift model.

## A nonempty polynomial saving range

Suppose H tends to infinity and, up to fixed multiplicative constants,

\[
U=H^a,\qquad V=H^b,\qquad a,b>0,\quad b>3a/4.
\]

For any fixed A>0, uniformly over 1<=|k|<=H^A, the elementary divisor bounds make tau_H, tau(|k|), sigma_(-3/4)(|k|), and kappa_b(H)^(-1) all H^o(1). Equations (5)-(7), choosing eta sufficiently small, give

\[
\boxed{\frac{|S(H,k;U,V)|}{N_0}
 \ll H^{-\gamma+o(1)},\qquad
\gamma=\min\{a,\ b-3a/4\}>0.} \tag{8}
\]

The notation means a bound H^(-gamma+delta) for every fixed delta>0, with constants depending on the fixed parameters and delta. The divisor bounds are uniform for polynomially bounded k; there is no claim uniform over arbitrary enormous k. The count error in (7) is relatively smaller in this range, and N0 is positive eventually.

For the balanced example U,V comparable to sqrt(H), gamma=1/8. Thus genuine unweighted complement-ratio cancellation is obtained uniformly in the large multiplier H, rather than treating H as an additional large residue modulus. The estimate does not cover every highly unbalanced box; its displayed error explains the limit b>3a/4.

## A proved discrepancy consequence

Let x_P=H*r_P modulo1 and define the normalized interval discrepancy

\[
\mathcal D=\sup_I\left|\frac1{N_0}\#\{P:x_P\in I\}-|I|\right|.
\]

For every integer J>=2 with N0>0,

\[
\boxed{\mathcal D\ll J^{-1/2}
       +\sum_{1\le k<J}\frac{|S(H,k;U,V)|}{kN_0}.} \tag{9}
\]

Here I ranges over circular intervals with a consistent half-open convention. A short proof makes the smoothing cost explicit. The Fejer kernel F_J(t)=J^(-1)*(sin(pi*J*t)/sin(pi*t))^2 is nonnegative, has integral1 and Fourier support |k|<J. Outside distance delta from zero its integral is O(1/(J*delta)), by the bound F_J(t)<=1/(4J*||t||^2). Take delta=J^(-1/2), treating bounded small J by the trivial discrepancy bound. Enlarge I by delta and convolve its indicator with F_J. Dividing by one minus that tail gives a trigonometric majorant of 1_I, with constant coefficient |I|+O(J^(-1/2)) and nonzero coefficients O(1/|k|). If enlargement fills the circle, use the constant1. A minorant comes from one minus a majorant of the complementary interval. Averaging those finite polynomials over x_P and using their Fourier coefficients proves (9). No unproved discrepancy theorem is an input.

In the polynomial range of (8), choose J comparable to H^(2gamma). The frequency range in (8) permits this for a fixed exponent A>=2gamma, and the harmonic factor log J is absorbed in H^o(1). Therefore

\[
\mathcal D\ll H^{-\gamma+o(1)}. \tag{10}
\]

In particular the balanced sqrt(H) example allows J comparable to H^(1/4) and discrepancy H^(-1/8+o(1)). This is an asymptotic estimate with unspecified effective constants, not a numerical claim at any finite H.

For a right-continuous periodic function g of bounded variation, the elementary Stieltjes/Koksma bound gives

\[
\left|\frac1{N_0}\sum_P g(x_P)-\int_0^1g(t)\,dt\right|
                         \ll\operatorname{Var}(g)\mathcal D. \tag{11}
\]

One proof writes g as its constant plus the cumulative signed derivative measure, interchanges its integral with the finite empirical measure minus Lebesgue measure, and bounds each interval mass by D. The total variation of that derivative is Var(g). Complex-valued g follows by the same absolute-measure argument. A trigonometric polynomial can alternatively be averaged directly using (5), retaining its exact Fourier-coefficient costs.

Combining (7), (10) and (11) averages g with the correct leading mass 15UV*kappa_b(H). If g depends on H, its variation must be multiplied into the error explicitly. Bounded variation independent of H is permitted; variation growing faster than the proved saving is not automatically covered.

## Scope of the arithmetic advance

This is an actual elementary cancellation and discrepancy bound for the unprescribed moving complement ratio over primitive both-unit integer positions. It avoids an artificial congruence modulus H by using the unit multiplier in (4) and paying its explicit divisor count instead. The proof rederives its complete-sum input and all completion, frequency and density costs. Separate review and finite verification must still check it.

The measure has no actual-prime indicator, prescribed prime-list line constraints, selected endpoint coefficients or high operator moments. Neither (10) nor the bounded-variation statement certifies that those more complicated test functions have bounded variation, allowed frequencies, or suitable norm costs. The changed large-denominator major-arc prime estimate from SECTORS-006 is untouched. Polynomial-label support, nonzero centers and the h=1 prime boundary from LABELS-005 remain.

Consequently no prime-correlation lower bound, original F margin, Goldbach proof or demonstrated breakthrough follows yet. The separate closest-work.md inspection records the stronger classical Weil bound and related inverse-distribution literature. The elementary proof here is a scoped specialization of established methodology, not a new general inverse-distribution theorem; no advanced Weil estimate is required by its argument. The exact filtered consequences of those external results have not been audited here.

The next meaningful extension would need a joint estimate with the actual prescribed list arithmetic or endpoint structure, with all modulus and variation costs stated, rather than treating generic Fourier equidistribution as the missing Goldbach estimate.
