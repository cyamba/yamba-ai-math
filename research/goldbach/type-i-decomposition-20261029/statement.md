# Exact reflected decomposition and an endpoint-uniform Type-I bound

29 October 2026. Registry role: Mathematician, `GOLDBACH-TYPEI-013`, author stage. Two bounded candidates are proved below, pending distinct review: an exact sifted Vaughan/rectangle interface, and the even-H Type-I estimate. The only distribution theorem imported for Type I is the precise primary Mobius BV statement recorded below. ENERGY-012 received its positive main review and corrected-scope revision during this stage; assembly uses that actual revision and its selected-strip or small-radical scope, together with the comparable-threshold check exposed here. No removal of W, actual unweighted prime theorem, Goldbach proof, breakthrough or novelty is claimed.

The pinned Guo source already contains the convolution and common-divisor framework. Its assertion is not used in place of the reductions here. The accepted MOMENTS-010 and PAIRING-011 records keep their eligible-model and original-box restrictions.

## Parameters and target

Let H be even, `L=log H`, `H/L^B<=y<=H/2`, and `y<t<=2y`, with fixed B. Set `U=V0=y^{1/5}`, `Z=exp(L^{3/4})`. Use fixed eligible disjoint bands avoiding H, exponents `0.1<a1<...<aK<0.2`, reciprocal masses V_i, and fixed rho in (0,1). Their masses are uniformly bounded above and below as in MOMENTS-010. All band primes are odd and below Z. Put

\[
 W(w)=\prod_i\omega_i(w)\rho^{\omega_i(w)-1}/V_i,
 \quad F(n)=\mu(H-n)W(H-n)\mathbf1_{1\le n<H},
\]

with a zero factor if omega_i=0. The prime counts omega_i are distinct-prime counts. W and F are bounded for fixed K,rho. Every integer interval uses an explicitly consistent one-sided endpoint convention; varying either endpoint is permitted in the estimates below. No Mobius value at zero or a negative integer is used.

The primary distribution input is the inspected [Murty-Vatwani Proposition 3, journal page 115](https://mrammurty-ai.github.io/chowla.pdf): each P>0 admits B_P with

\[
 \sum_{m\le T^{1/2}(\log T)^{-B_P}}
 \max_{a\ ({\rm mod}\ m)}\max_{z\le T}
       |\sum_{n\le z,\ n=a\ ({\rm mod}\ m)}\mu(n)|
          \ll_P T(\log T)^{-P}. \tag{1}
\]

We use only its narrower reduced-class consequence and interval differences. The theorem statement was downloaded, rendered and independently inspected as recorded in `primary-inputs.md` and `source-provenance.json`. It is reproduced there from Siebert-Wolke (1971); that original proof and the complete Murty-Vatwani paper were not audited. This assurance qualification is retained.

## Candidate 1: convolution, prime corrections and rectangles

**Proved, pending review.** The exact convolution below gives T1-T2+T3 and both prime-power corrections. Its rectangular pieces have precisely the Mobius and long-prime-factor coefficients needed by the later energy argument, with controlled Mellin phases and endpoint losses.

Write `mu_<=U` and `Lambda_<=V0` for the corresponding truncated arithmetic functions. From `log=1*Lambda` and `mu*1=delta_1`,

\[
 \Lambda=\Lambda_{\le V0}+\mu_{\le U}*\log
       -\mu_{\le U}*\Lambda_{\le V0}*1
       +\mu_{>U}*\Lambda_{>V0}*1. \tag{2}
\]

Indeed the second minus third term is `mu_<=U*1*Lambda_>V0`; adding the last gives `mu*1*Lambda_>V0=Lambda_>V0`. No asymptotic estimate enters (2).

The indicator R_Z is completely multiplicative. On n>y>V0 the first term vanishes. Multiplication by `R_Z(n)F(n)1_(y<n<=t)` gives exactly T1-T2+T3, where

\[
 T_1=\sum_{d\le U}\mu(d)R_Z(d)
       \sum_{y<dk\le t}R_Z(k)(\log k)F(dk),
\]
\[
 T_2=\sum_{d\le U,\ell\le V0}\mu(d)\Lambda(\ell)R_Z(d\ell)
       \sum_{y<d\ell k\le t}R_Z(k)F(d\ell k),
\]
\[
 T_3=\sum_{m>U,n>V0,\ y<mn\le t}
       \mu(m)R_Z(m)c_{V0}(n)R_Z(n)F(mn),
 \quad c_{V0}(n)=\sum_{\ell|n,\ell>V0}\Lambda(\ell). \tag{3}
\]

Here `0<=c_V0(n)<=log n`. For T2, grouping q=d*ell gives q<=y^{2/5}, with coefficient of absolute value at most `sum_{ell|q}Lambda(ell)=log q`. T1 has q<=y^{1/5}. Both retain R_Z(q).

To pass to prime-only sums there are two corrections. Removing R_Z from the von Mangoldt sum costs at most `||F|| sum_{p<=Z}log p=O(||F|| Z)`, because a partial ratio-two interval contains at most one power of each fixed prime. Removing the remaining higher powers costs `O(||F|| sqrt(y)log^2(2y))`, by counting bases up to sqrt(2y) and exponents. Hence

\[
 \sum_{y<p\le t}(\log p)F(p)
       =T_1-T_2+T_3+O(\|F\|_\infty[Z+\sqrt y\log^2(2y)]). \tag{4}
\]

The second correction is still necessary after the first: Z=2 and a test supported at 9 leave a von Mangoldt contribution log 3 and no prime contribution. The positive shifted endpoint stays in F throughout (2)-(4).

### Product strips and the actual coefficient roles

Dyadic localization of T3 gives O(L^2) rectangles with `M,N>=y^{1/5}/2`, `MN` comparable to y, `m>U`, `n>V0` retained by subintervals. On each rectangle the arithmetic arrays before a common phase are exactly

\[
 \alpha_m=\mu(m)R_Z(m),\qquad
 \beta_n=c_{V0}(n)R_Z(n). \tag{5}
\]

For a relative product strip of width epsilon*y at either endpoint, count using the shorter variable only as a counting variable. If that length is A=min(M,N), then

\[
 \#\{|mn-s|\le C\epsilon y\}
       \ll\sum_{a\asymp A}(\epsilon y/a+1)
       \ll\epsilon y+\sqrt y. \tag{6}
\]

This does not exchange the Mobius and long-prime-factor roles. Coefficients and F cost one fixed L power, uniformly in the dyad endpoint t.

Choose `epsilon=L^{-B_s}` and a smooth approximation to `1_(y<mn<=t)` as a function of mn/y, with errors supported in those two strips. Its logarithmic-variable transform has L1 norm at most a fixed power, for example `O(epsilon^{-2})`. Mellin inversion gives common phases `m^{iv}n^{iv}` and a harmless `y^{-iv}`. Derivatives of the smooth cutoff of order r cost `O_r(epsilon^{-r})`, so truncating at

\[
 |v|\le\epsilon^{-2}=L^{2B_s} \tag{7}
\]

leaves an arbitrarily small fixed logarithmic error by choosing r sufficiently large. The total strip error over rectangles is `O(L^3(epsilon y+sqrt y))`; the transform and rectangle sums contribute only fixed logarithmic integration losses. F, its shifted positivity cutoff and its arithmetic factors are never differentiated.

Removing pairs where m or n shares a prime with H costs `O(yL*omega(H)/Z)` per collection of supported rectangles, up to the fixed logarithmic sums. Such a prime exceeds Z; the number of multiples in a dyad is `O(M/p)` or `O(N/p)` when it can occur, including endpoints. This remains negligible after (7)'s fixed logarithmic loss. Thus the rectangular coefficients delivered to energy are

\[
 \mu(m)R_Z(m)\mathbf1_{(m,H)=1}m^{iv},\qquad
 c_{V0}(n)R_Z(n)\mathbf1_{(n,H)=1}n^{iv}. \tag{8}
\]

They are units modulo kH for k<=L^{A0}. The phase ceiling (7) must be fixed before the later energy height and zero-free constants; it cannot be replaced by an earlier smaller ceiling. An auxiliary symmetric Type-II difference may exchange both arrays to orient M<=N, but the energy proof retains the roles in (8).

There is one exact threshold bookkeeping point: on these rectangles `V0=y^{1/5}` while `X_rect=MN` is merely comparable to y. A nonempty rectangle has `y/4<X_rect<=2y<=H`. Thus V0 is within fixed positive factors of `X_rect^{1/5}`, and V0>=H^{1/6} eventually. This is not an equality obtained by renaming the variable.

Here is the explicit extension of the accepted ENERGY-012 proof. Its beta coefficient still satisfies `0<=c_V0(n)<=log n`, so every ordinary, bulk and sparse Gram coefficient norm is unchanged. Its exact divisor convolution now restricts the prime-power factor to ell>y^{1/5}; its inner intervals remain ratio at most two, with endpoints at least this V0. The upper endpoints obey 2N<=H eventually because M>=H^{1/5-o(1)} and X_rect<=H. The same endpoint Perron bound applies, and removing inner small-prime/unit restrictions still costs `O((Z+L)/V0)`, negligible at every fixed logarithmic precision. The remaining harmonic-cofactor and exceptional-energy arguments use only the length hypotheses `M,N>=H^{1/5-o(1)}` and these coefficient norms. The small-conductor Mobius argument is unchanged. Therefore the energy proof is uniform for this comparable threshold with the same precision scheme, rather than a different arithmetic array. Choose its fixed phase/lower-product parameter at least max(B+1,B_s) before its heights and zero-free constants, to cover `X_rect>=H/(4L^B)` and (7).

All rectangles keep the same global L=log H, marking bands, W and integer J,R. Since `log X_rect=L+O(log L)`, the logarithm used to express their asymptotic bounds is comparable with ratio tending to one. For PAIRING-011/MOMENTS-010 the proof uses `J` of order `L^0.01`, `R` of order sqrt L, positive fixed masses, the strict band-exponent gaps, and prime-log bounds within fixed constant factors of L^{a_i}; it does not require a new rounding of J,R or new bands at each rectangle. Keeping their good tests at the common global L gives the same clean/dirty estimates and the physical budgets `O(L^0.73)` and `O(L^0.96)`. ROOTS-008's modulus range and power discrepancy remain available because log X_rect is comparable to L. This checks the common-logarithm interface without changing W between rectangles.

In particular the comparison arcs are defined once with denominators at most L^{A0}, using this common global L in both the difference and energy arguments. This applies the proved bounds with their checked scale hypotheses; it does not assert equality between comparison operators built from two different arc cutoffs.

## Candidate 2: endpoint-uniform even-H Type I

**Proved relative to (1), pending review.** For each fixed A and every outer sequence with `|a_q|<=CL`, supported on Z-rough q<=Q=y^{2/5},

\[
 \sum_q a_q\sum_{s<qk\le t}R_Z(k)
       \mu(H-qk)W(H-qk)\mathbf1_{qk<H}
             \ll_A yL^{-A} \tag{9}
\]

uniformly for both dyad endpoints `y<=s<t<=2y`. Consequently T1 and T2 in (3) have this bound. The proof uses finite divisor expansions and the actual scale for each extracted common divisor.

### Unit removal and finite positive truncation errors

First discard q sharing a prime with H. Such a prime exceeds Z. Using `#k<=y/q+1`, the total is at most

\[
 C L\sum_{p|H,p>Z}\sum_{q\le Q,p|q}(y/q+1)
       \ll y L^2\omega(H)/Z+Q L\omega(H)/Z,
\]

which has every requested logarithmic saving. This estimate is absolute and includes the endpoint counts. Thereafter `(q,H)=1`, q is odd, and only odd k need be retained before expanding its remaining sifting.

For the odd primes p<=Z, let R_I=ceil(C_I log L) and form the truncated inclusion-exclusion polynomial P_I(k) through order R_I. Its coefficients are mu(r) for odd squarefree r with `omega(r)<=R_I`, `P+(r)<=Z`. The pointwise error is bounded positively by

\[
 E_I(k)=\sum_{r|k,\ r\ {m odd\ squarefree},\omega(r)=R_I+1,\ P^+(r)\le Z}1.
\]

The binomial identity `sum_{j<=R}(-1)^j binom(u,j)=(-1)^R binom(u-1,R)` for u>0 proves the error bound, including the case u<=R. Its reciprocal coefficient mass is at most `S_Z^{R_I+1}/(R_I+1)!`, where `S_Z=sum_{3<=p<=Z}1/p=O(log L)`. With C_I large this is smaller than any requested fixed L power. The retained absolute reciprocal mass is `O(log Z)`, and every retained or error r is at most `Z^{R_I+1}=H^{o(1)}`. Their total absolute coefficient count is H^{o(1)}.

For one band put u=omega_i(w), and R_W=ceil(C_W log L). The finite identity is

\[
 \frac{u\rho^{u-1}}{V_i}
  =\frac1{V_i}\sum_{j=0}^{R_W-1}(j+1)(\rho-1)^j
        \sum_{d|w,\ d\ {m squarefree\ in}\ \Pi_i,\omega(d)=j+1}1
           +E_i(w),
\]
\[
 |E_i(w)|\le\frac{(R_W+1)(1-\rho)^{R_W}}{V_i}
       \sum_{d|w,\ d\ {m squarefree\ in}\ \Pi_i,\omega(d)=R_W+1}1. \tag{10}
\]

Taylor's remainder for `(1-z)^{u-1}` proves this for u>=R_W+1; smaller u is an exact finite polynomial, and u=0 is zero. Let A_i be the absolute retained polynomial and B_i the positive remainder bound. Both with weights 1/d and 1/phi(d), the A_i coefficient mass is bounded, and B_i mass is `O(1/R_W!)`: use the band reciprocal sums, and their 1/(p-1) analogues, bounded above by one eventually. Telescope the K products, using bounded true W_i and A_i on earlier factors. This gives a retained divisor polynomial `P_W(w)=sum_{d|w}c_d` and positive finite remainder E_W with

\[
 \sum_d|c_d|/d\ll_{K,\rho}1,\qquad
 \sum_d e_d/d\ll_{K,\rho}1/R_W!, \tag{11}
\]

and the same bounds with phi(d). Each d is odd squarefree, eligible and coprime to H, with O_K(R_W+1) prime factors and size H^{o(1)}. The total absolute coefficient counts, including e_d, are H^{o(1)}. The truncated polynomial is not assigned the pointwise bound of true W.

Indeed the combined error is bounded by `C_K E_I(k)+A_I(k)E_W(H-qk)`, where A_I is the absolute odd-sieve polynomial. If r divides k and d divides H-qk, a common prime of r,d would divide H, impossible for an eligible d prime. Otherwise `(r,d)=1`, `(q,d)=1`, and with oddness retained these conditions form one class modulo 2rd. Thus their number is

\[
 O(y/(qrd)+1). \tag{12}
\]

Use (12) on each positive remainder. The main errors are controlled by (11), the factorial odd-sieve tail, `sum_r1/r<<log Z` and `sum_q |a_q|/q<<L^2`. The total of all +1 terms is at most `y^{2/5+o(1)}` times fixed logarithmic factors. Choosing C_I,C_W first in terms of A makes all these errors `O_A(yL^{-A})`. The full primorial is never a modulus.

### Exact common-divisor extraction and parity

It remains to estimate retained terms with r|k, d|H-qk. Put `k=rj`, `g=(r,H)`. Then g is odd squarefree, `(d,g)=1`, and `dg|H-qrj`. For squarefree `A=dg`, prime-by-prime calculation proves

\[
 \mu(Av)=\mu(A)\sum_{b|v,\ p|b\Rightarrow p|A}\mu(v/b). \tag{13}
\]

All prime powers in b are allowed. At a prime in A the local sum is one at exponent zero and zero at every positive exponent after multiplication by mu(p); outside A it is the usual Mobius factor. For example A=3,v=9 needs b=9; forcing b squarefree would give one instead of mu(27)=0.

Write

\[
 H-qrj=dgbt,\quad t>0,\qquad
 t\equiv(H/g)(db)^{-1}\pmod{qr/g}. \tag{14}
\]

The inverse exists: d avoids q and r; g avoids q because q is Z-rough, and avoids r/g because r is squarefree; b is supported on primes of dg. Also `H/g` is coprime to `qr/g`, since `(q,H)=1` and `(r/g,H)=1`. No condition `(g,db)=1` is imposed or needed. H=78,q=11,r=3,d=5,b=3,j=t=1 is a valid example with b sharing g.

Since H is even and q,r,d,g,b are odd, j odd is equivalent to t odd. Combine the reduced odd-modulus class in (14) with `t=1 mod 2`, obtaining a **reduced** class modulo

\[
 m_0=2qr/g. \tag{15}
\]

It would be incorrect simply to use the even residue H/g modulo this doubled modulus. The positive t interval is translated and reversed from the original dyad endpoints, and is contained in `[1,Y0]` with

\[
 Y0=(H+3y)/(dgb). \tag{16}
\]

Both endpoints are retained; (1) applies to their difference. The sign reversal in H-qrj has not changed the modulus or reducedness.

For a finite parity witness, H=32,q=r=g=b=1,d=3,j=2,t=10 satisfies H-qrj=dgbt and the undoubled class, with d coprime to H, but j and t are even. It must be excluded from the retained odd-k sum.

### Small dgb: each g has its own BV scale

For `dgb<=y^{1/20}`, (16) gives `Y0>=y^{19/20}`, with log Y0 comparable to L. Every reduced modulus (15) is at most `y^{2/5+o(1)}`, whereas

\[
 Y0^{1/2}\ge y^{19/40},\qquad 19/40-2/5=3/40>0.
\]

Thus the BV level with every fixed logarithmic loss is available. Apply it separately at each fixed g,d,b and this Y0 before summing their factors.

Grouping q,r by m0 has coefficient at most `CL tau(m0)`. In fact the rough/small-prime factorization is unique here: q contains only primes above Z and r/g only primes at most Z. We retain the more robust divisor bound. Let E(Y0;m) be the reduced endpoint maximum from (1). Its trivial bound is `O(Y0/m+1)`. Cauchy and `sum tau(m)^2/m<<log^4(2Y0)` give

\[
 (\sum_{m\le Q_0}\tau(m)E(Y0;m))^2
 \le(\sum E)(\sum\tau(m)^2E)
       \ll_P (Y0L^{-P})(Y0L^4).
\]

Here Q0<=sqrt(Y0) times any required negative logarithmic power; the +1 divisor sum is absorbed as well. With a sufficiently high fixed BV precision and the outer coefficient L, the result is `O_A(Y0 L^{-A'})` for any fixed A'. Multiply by |c_d| and sum only afterward. The true reciprocal factors give

\[
 \sum_d|c_d|/d\ll1,\quad
 \sum_{g|\operatorname{rad}(H)}1/g\ll\log L,\quad
 \sum_{b:\ p|b\Rightarrow p|dg}1/b
       \le\prod_{p\le Z}(1-1/p)^{-1}\ll\log Z.
\]

Consequently the head is bounded by `(H+3y)L^{-A'}` times fixed logarithmic powers, hence by `yL^{-A}` since H/y<=L^B. No common-scale BV bound has discarded the g,d,b denominators.

### Large dgb: reciprocal and endpoint tails

Retained dg is H^{o(1)}. Thus `dgb>y^{1/20}` forces `b>y^{1/25}` eventually. Its prime support has only `O_(K,A)(log L)` odd primes, namely those dividing dg. For every fixed eta>0,

\[
 \prod_{p|dg}(1-p^{-\eta})^{-1}=L^{O_{K,A,\eta}(1)}.
\]

Rankin at 1/2 and 1/20 respectively gives

\[
 \sum_{b>y^{1/25},\ p|b\Rightarrow p|dg}1/b
       \ll y^{-1/50}L^{O(1)},\qquad
 \#\{b\le H+3y:p|b\Rightarrow p|dg\}
       \ll y^{1/20}L^{O(1)}. \tag{17}
\]

These Euler products are over the O(log L) supported primes, not every prime up to Z. The absolute count of (14), including oddness, is

\[
 O(y/(dbqr)+1). \tag{18}
\]

Indeed `gcd(dgb,qr)=g`, so the t spacing is qr/g while its interval length is O(y/(dgb)). The reciprocal part of (18), after summing q,r,d with their harmonic masses, is `O(y^{49/50}L^{O(1)})`. The endpoint part uses Q=y^{2/5}, H^{o(1)} total retained r and d coefficients, and the second bound in (17). It is `y^{9/20+o(1)}`. Both have every fixed logarithmic saving. This proves (9), with all endpoint counts retained.

### Restoring log k and the actual Type-I terms

The estimate (9) is uniform in both product endpoints and in every outer sequence of size O(L). For T1 use `log k=log(qk)-log q`. The second term is covered by the outer sequence `mu(q)log q`. Restore the first by real-weight partial summation in the product n=qk, using the endpoint-uniform bound and derivative 1/n of log n. It costs one fixed L power, absorbed by choosing precision higher. No phase or shifted Mobius target is differentiated. T2 is covered directly by its grouped coefficient bound log q. This completes Candidate 2.

## Assembly in the reviewed analytic scope and the next boundary

Candidates 1 and 2 do not assume an energy bound in their proofs. The actual ENERGY-012 revision is now available with positive distinct review; its general-H selected strip remains an assumption, while its fixed small-radical class supplies that strip from the named classical inputs. Combining it, with the explicitly checked comparable threshold above, and accepted PAIRING-011 gives for each rectangular selected-product piece `Q_all<<HY L^{-P}` and hence `|T_Y|<<H L^{-P/2}` by the signed cofactor Cauchy estimate. This is a proposed corollary of the current candidates and accepted dependencies, pending this stage's review; it does not use an unreviewed source-wide theorem.

For explicit precision order, choose B_s>A+10 for the strips, then P>2(A+B+2B_s+5). This absorbs H/y<=L^B, O(L^2) rectangles, O_K(L) selected-product blocks and the O(L^{2B_s}) Mellin integral. Choose PAIRING-011's operator parameters for that P, then ENERGY-012's height and selected-strip constants at the required precision and enlarged fixed phase ceiling. All are fixed before H tends to infinity. Equations (3)-(4), overlap errors and Type I then give

\[
 \sum_{y<p\le t}(\log p)\mu(H-p)W(H-p)
                      \ll_A yL^{-A}, \tag{19}
\]

with the same explicit selected-strip condition for general H, or from the named classical inputs on the fixed small-radical class. The comparable-threshold extension and this assembly require the present stage's distinct review. It is the weighted target W, not the actual unweighted Mobius-prime sum. The original positive F remains the input to Cauchy, and no nonfactorable positive-product mask was put in the signed operator.

This stage does not remove W, assert a rate uniform in a later number of marking families, impose polynomial roughness, or prove a prime Goldbach margin. The h=1 boundary and nonzero centers remain. The BV theorem statement is imported with its exact primary assurance; original source-wide transport and novelty are not established. The written arguments and their finite witnesses must undergo distinct semantic review and the preregistered bounded convolution/class checks before acceptance.
