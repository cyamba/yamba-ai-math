# A closed-form failure certificate for one Buchstab switch

29 October 2026. Registry role: Mathematician, `GOLDBACH-SWITCHING-004`. This statement uses the completed source survey in the populated harness packet. It derives an explicit unconditional lower-bound calculation and a strictly negative leading coefficient for that calculation. It does not show that the actual prime-pair or odd-factor count is negative. Separate mathematical review and independent coefficient computation are pending. No novelty or Goldbach breakthrough is claimed.

## Counts, exact switching, and parameter scope

For even N and fixed real gamma>0, let U_gamma(N) count primes p with q=N-p>1 and every prime factor of q strictly greater than N^gamma. At fixed alpha in [3/10,1/3), let E_alpha count those with Omega(q)=2, including squares, and F_alpha count those with odd Omega(q). All rough complements below N have at most three factors, so exactly

\[
F_\alpha(N)=U_\alpha(N)-E_\alpha(N). \tag{1}
\]

For a prime r define

\[
C_r(N)=\#\{p\text{ prime}:q=N-p>1,\ P^-(q)=r\}.
\]

Thus q=r*m for one uniquely determined integer m>=1, and every prime factor of m is at least r. The case m=1 belongs to this count. Equality at r is permitted, so repeated factors such as r^2 and r^3 are retained. For beta<alpha the exact partition by the least prime factor is

\[
U_\alpha(N)=U_\beta(N)
 -\sum_{N^\beta<r\le N^\alpha\atop r\text{ prime}}C_r(N). \tag{2}
\]

The strict lower and inclusive upper endpoints in this prime sum follow directly from strict roughness. No permutations of factors are counted.

Fix parameters

\[
3/10\le\alpha<1/3,\qquad
\alpha<d<1/2,\qquad d/4\le\beta<d/2. \tag{3}
\]

In particular beta<alpha. The ordinary distribution budget is D=N^d, up to harmless integer rounding. Every parameter in (3) is fixed before N tends to infinity. No uniform asymptotic is claimed when d-alpha tends to zero with N.

Use the existing normalization

\[
A_N=\mathfrak S(N)N/\log^2N,\qquad
\mathfrak S(N)=2C_2\prod_{p\mid N,\ p>2}\frac{p-1}{p-2}.
\]

These are the original unweighted prime counts. Their base sieve mass is li(N), rather than N or a von Mangoldt-weighted count.

## Precisely the chosen minorant

Apply the ordinary dimension-one Rosser-Iwaniec lower bound once to U_beta. For each C_r apply an ordinary upper bound to m=q/r, with distribution budget D/r, after weakening its sift cutoff when required to stay within the inspected theorem's domain. Sum these upper bounds and subtract an ordinary two-linear-form upper bound for E_alpha. The inequalities combine with (1)-(2) to give an unconditional lower bound for F_alpha.

For this particular family, the lower coefficient before E_alpha is subtracted is

\[
\boxed{M(d,\alpha,\beta)=\frac{2}{d}
                      \log\frac{d-\alpha}{\alpha}.} \tag{4}
\]

It is independent of beta and is strictly negative throughout (3). Even granting the favorable value E_alpha=0 would leave this coefficient negative. The actual chosen bound also subtracts a nonnegative upper coefficient for E_alpha, making it weaker. This is a failure certificate for the stated inequalities, not an impossibility theorem for all switching arguments or a counterexample to Goldbach.

## Imported sieve statements and their allowed domain

The inspected [Wu, Lemma 2.2 and equation (2.6), printed page 220](https://www.impan.pl/shop/en/publication/transaction/download/product/82961), supplies lower and upper formulas with well-factorisable remainder weights of order 1, hence magnitude at most 1, and requires the sift cutoff z to satisfy 2<=z<=sqrt(Q) when the distribution budget is Q. Its functions satisfy

\[
F(s)=2e^\gamma/s\quad(2\le s\le3),\qquad
f(s)=2e^\gamma\log(s-1)/s\quad(2\le s\le4).
\]

These intervals follow from the source's differential definitions. No application of its lemma below s=2 is made. The lemma uses finitely many remainder-weight families depending on its approximation tolerance. The coefficient limits here mean: fix that tolerance, let N tend to infinity, then let the tolerance tend to zero. Its remainder errors are controlled by ordinary [Ford, Theorem 3.4](https://ford126.web.illinois.edu/sieve2023.pdf), since d<1/2 is fixed. The exact partition (2) is also the elementary least-prime argument in Ford Lemma 3.8.

## Local densities and exceptional primes

First remove the prime summands p dividing N. There are at most omega(N)=O(log N) such summands in the entire problem. For the remaining sequence, a prime ell dividing a complement q cannot divide N: otherwise it would divide p as well, contrary to the removal. Thus the admissible sifting primes exclude prime divisors of N. For ell not dividing N, the local density among prime summands is

\[
g_N(\ell)=1/(\ell-1).
\]

The factor 2 divides N, so its sifting density is zero. With products over primes strictly less than v, put

\[
V_N(v)=\prod_{\ell<v,\ \ell\nmid N}
                  \left(1-\frac1{\ell-1}\right).
\]

This profile satisfies the uniform dimension-one product condition in Wu: deleting primes dividing N only decreases the product of inverse factors compared with the full odd-prime profile. Mertens and the twin-prime Euler product give, for v=N^u with u in any fixed compact subinterval of (0,1),

\[
V_N(v)=(e^{-\gamma}+o(1))\frac{\mathfrak S(N)}{u\log N}, \tag{5}
\]

uniformly over even N. To see the potentially important target dependence, the exact finite factorization is

\[
V_N(v)=2\prod_{\ell<v}(1-1/\ell)
 \prod_{2<\ell<v}\left(1-\frac1{(\ell-1)^2}\right)
 \prod_{2<\ell<v,\ \ell\mid N}\frac{\ell-1}{\ell-2}.
\]

Prime divisors of N at least v contribute a ratio 1+o(1) between this partial local product and the complete singular series: there are O_u(1) such divisors and each omitted factor is 1+O(1/v). This justifies (5) for a moving target N, not just a fixed local-factor pattern.

Removing p|N from progression counts costs at most O(omega(N)) per modulus. Summing that crude error over moduli at most D contributes O(D log N)=o(A_N), even after the fixed number of sieve weight families. One may therefore use the usual reduced-residue BV errors and retain a global O(log N) count exception. If r divides N, the only possible prime p with r dividing q is p=r, already removed. Such r are never treated as reduced-residue progression moduli.

The sequence q=N-p includes q=1 if N-1 is prime; it must be excluded from U_beta, at a cost at most 1. It is included in a raw sifted sequence only for this subtraction. In C_r the remaining factor m=1 is retained, as required. Prime factors equal to r are not crossed out, since that switch sieves only primes strictly less than its cutoff v<=r. The prime-equals-sieving-prime and local-factor exceptions are therefore explicit.

## The lower coefficient at beta

For squarefree k coprime to N, the unsifted complement sequence has progression count pi(N;k,N), with main mass li(N)/phi(k), after the preceding harmless removals. Take sift cutoff floor(N^beta)+1, which imposes exactly the strict prime-factor condition >N^beta. Its ratio to N^beta tends to one. Since beta<d/2, the condition on the lower-sieve cutoff is satisfied eventually. Since d/4<=beta, the parameter d/beta lies in (2,4]. Thus

\[
\liminf_{2\mid N,\ N\to\infty}\frac{U_\beta(N)}{A_N}
 \ge L(d,\beta):=\frac{e^{-\gamma}}{\beta}f(d/\beta)
 =\frac{2}{d}\log\frac{d-\beta}{\beta}. \tag{6}
\]

The coefficient includes both li(N)~N/log N and the density (5). Ordinary BV controls the lower-sieve remainders through D; the dependence of the residue N mod k on N is permitted by its reduced-residue maximum.

## A legal upper bound for each switch

For r not dividing N write t=log r/log N and D_r=D/r. Among p with p congruent to N modulo r, the unsifted main mass is li(N)/phi(r). For squarefree k with prime factors less than r and coprime to N, divisibility of m=(N-p)/r by k is the reduced progression p congruent to N modulo rk, with local density 1/phi(k). The sequence must exclude all prime factors of m strictly less than r to count C_r exactly. For an upper bound it is legitimate to sieve fewer of those factors.

Use the explicit legal cutoff

\[
v_r=\min\{r,\sqrt{D_r}\}.
\]

Its exponent is u(t)=min(t,(d-t)/2)>0, and its actual sieve parameter is

\[
s'_r=\frac{d-t}{u(t)}\in[2,3]. \tag{7}
\]

The lower endpoint beta>=d/4 ensures the upper limit 3 in (7). When t<=d/3, keep v_r=r. When t>=d/3, weaken to sqrt(D_r), giving parameter exactly 2. This explicit split avoids applying Wu's lemma to a parameter below 2. Its changed density V_N(v_r) must be used; substituting V_N(r) in the second range would be invalid.

Since s'_r F(s'_r)=2e^gamma, equations (5) and (7) give the leading per-r bound

\[
\frac{\operatorname{li}(N)}{\phi(r)}V_N(v_r)F(s'_r)
 =(1+o(1))\frac{2\mathfrak S(N)N}
                  {r\log^2N\,(d-t)}. \tag{8}
\]

Here phi(r)=r-1 can be replaced by r with a uniform o(1), since r>N^beta. The sieve approximation error is handled by the stated successive limits. The local-density approximation is uniform on this fixed parameter interval, since d-alpha>0.

Accumulated errors do not require a hidden distribution theorem for products of primes. The upper-sieve remainder for r has moduli rk with rk<=D, and every prime factor of k is strictly less than v_r<=r. Therefore r is the unique largest prime factor of rk. Each resulting modulus can arise from at most one switching prime r; the remaining k is then determined. For each of the fixed sieve-weight families, whose coefficients have magnitude at most 1, the sum of absolute errors is bounded by the ordinary BV absolute error over moduli at most D. The finitely many families multiply it by a tolerance-dependent constant only. The removals p|N cost O(D log N) as above.

Using PNT or prime harmonic partial summation in the nonnegative main sum, and enlarging past the finitely many r|N only after obtaining the bounds for admissible r, yields

\[
\limsup_{2\mid N,\ N\to\infty}
 \frac{\sum_{N^\beta<r\le N^\alpha}C_r(N)}{A_N}
 \le J(d,\beta,\alpha):=
 2\int_\beta^\alpha\frac{dt}{t(d-t)}.
\]

The terms removed for p|N are o(A_N). Evaluating the elementary integral,

\[
J(d,\beta,\alpha)=\frac{2}{d}
 \log\frac{\alpha(d-\beta)}{\beta(d-\alpha)}. \tag{9}
\]

Equivalently this is the survey's formal effective integral e^-gamma*integral F((d-t)/t)dt/t^2, but (8) derived it using only legal parameters. No theorem below s=2 is needed.

## Completing an actual minorant for F

The certificate already follows from (6)-(9), before subtracting E_alpha. To make a fully specified lower bound for F, an ordinary prime-two-form estimate also bounds that subtraction at the same scale. Let K2>0 be any valid absolute constant in the inspected [Ford Theorem 2.5](https://ford126.web.illinois.edu/sieve2023.pdf), for two primitive admissible linear forms and their singular series. Its numerical value is not needed for the sign certificate.

A semiprime complement has the unique sorted form q=r*s, z=N^alpha<r<=s, with r<=sqrt N. If r divides N, the prime summand must be p=r, giving at most three exceptions globally. Otherwise the forms s and N-r*s are primitive and admissible. Their singular series is exactly mathfrak S(N)*(r-1)/(r-2), which is (1+o(1))*mathfrak S(N) uniformly in r>z. Applying the coefficient-uniform two-form bound with x=N/r gives

\[
\limsup_{2\mid N,\ N\to\infty}\frac{E_\alpha(N)}{A_N}
 \le K_2 I(\alpha),\qquad
I(\alpha)=\int_\alpha^{1/2}\frac{dt}{t(1-t)^2}
 =2-\frac1{1-\alpha}-\log\frac{\alpha}{1-\alpha}>0. \tag{10}
\]

This upper bound enlarges the s interval only after using log(N/r)>=(1/2)log N, and includes squares r=s. Its finite exception disappears after division by A_N. All coefficients in (10) are nonnegative. Combining the exact identities and actual inequalities therefore gives the valid unconditional minorant calculation

\[
\liminf_{2\mid N,\ N\to\infty}\frac{F_\alpha(N)}{A_N}
 \ge L(d,\beta)-J(d,\beta,\alpha)-K_2 I(\alpha)
 =M(d,\alpha,\beta)-K_2 I(\alpha). \tag{11}
\]

It is a weak lower bound, since F_alpha>=0 already. Its purpose here is to assess the proposed switching mechanism with the exact allowed classical coefficients. No unknown K2 can rescue its negative sign.

## Exact failure certificate and optimization within this family

Subtract (9) from (6). The beta factors cancel exactly, proving (4). Since d<1/2 and alpha>=3/10,

\[
0<\frac{d-\alpha}{\alpha}<\frac23,
\qquad
M(d,\alpha,\beta)\le4\log(2/3)\le-\frac43<0. \tag{12}
\]

The last inequality is the elementary bound log x<=x-1. Equation (12) is an analytic rational sign certificate, independent of floating-point quadrature. Since K2 I(alpha)>=0, the coefficient in (11) is strictly more negative. It cannot dominate the nonnegative contamination upper coefficient C*epsilon^2 from the prior tranche.

A concrete rational choice is

\[
d=49/100,\quad\alpha=3/10,\quad\beta=1/5.
\]

For it,

\[
L=\frac{200}{49}\log\frac{29}{20},\quad
J=\frac{200}{49}\log\frac{87}{38},\quad
M=\frac{200}{49}\log\frac{19}{30}
 \le-\frac{220}{147}<0,
\]

and I(alpha)=4/7+log(7/3)>0. These formulas are ready for independent exact simplification and numerical illustration, but the sign does not depend on their numerical evaluation.

No beta search in (3) changes M. Partitioning the switching interval merely partitions the same integral (9). Among the stated legal cutoffs, the chosen v_r is the largest allowed one. Choosing a smaller fixed-polynomial cutoff with parameter exceeding 3 does not improve the leading standard upper coefficient: the differential definitions imply sF(s)>=2e^gamma for s>=2, so its factor F(s)/log v is no smaller than 2e^gamma/log D_r. A cutoff giving parameter between 2 and 3 gives equality in that comparison. Using a smaller distribution budget on a subinterval only reduces d-t and worsens (8).

The most favorable relaxed edge of the fixed-parameter family has d tending to 1/2 from below and alpha=3/10, yet its coefficient still tends to 4log(2/3)<0. This limiting comparison does not assert a distribution theorem beyond the usual BV range. It is not a claim of optimality over more elaborate Chen double-sieve improvements, two-switch identities, or other analytic inputs.

## Outcome and next mathematical obligation

**Proved, pending separate critic:** the exact switching identities, legal coefficient derivation and strictly negative coefficient certificate for the precisely chosen one-switch minorant. **Unproved:** any positive lower margin for the actual F_alpha, the pointwise signed cubic target, or Goldbach. Finite checks can catch endpoint and normalization errors but do not prove these asymptotic statements.

The failed calculation identifies a specific improvement target. A method modifying this same starting family would need a rigorous gain exceeding at least 4/3 of A_N even before paying for semiprime subtraction, rather than a tiny parameter adjustment. A next distinct possibility is to derive the additional correction terms of a genuinely different double-sieve/switching identity and check its actual distribution hypotheses for the moving target. That would require a new bounded contract and review; no such correction or improved lower coefficient is claimed here.
