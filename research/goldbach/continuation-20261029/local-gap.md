# The uniform size of the local-factor margin

29 October 2026. Supplemental mathematical-author argument by the root agent for `GOLDBACH-LOWER-003`, submitted to the separate critic. **Status: handwritten proof pending separate review.** It uses the classical prime number theorem and Mertens' product estimate. It supplies no cancellation for the signed operator and establishes no Goldbach breakthrough or novelty.

For even N define

\[
\mathfrak S(N)=2C_2\prod_{\substack{p\mid N\\p>2}}\frac{p-1}{p-2},
\qquad
\mathcal A(N)=\prod_{\substack{p\nmid N\\p>2}}
       \left(1-\frac1{p(p-1)}\right),\qquad
\delta_N=1-\mathcal A(N).
\]

Here all p are prime and C_2 is the twin-prime Euler product from `statement.md`. The lower proposal bounded delta_N alone by a constant times 1/log(N)^2. Keeping the singular series with it gives a sharper uniform margin.

## Proposition

There are absolute constants c>0 and N0 such that every even N>=N0 satisfies

\[
\boxed{\mathfrak S(N)\delta_N\ge \frac{c}{\log N}.} \tag{1}
\]

This order is sharp: along the primorial targets N_y=product_{p<=y}p,

\[
\mathfrak S(N_y)\delta_{N_y}\sim\frac{e^\gamma}{\log N_y}.
\tag{2}
\]

No numerical c or N0 is extracted here. The estimate is an elementary consequence of established prime asymptotics, not a new prime-distribution theorem.

## Proof of the uniform lower bound

Put y=4 log N. The prime number theorem in the form theta(y)=sum_{p<=y}log p~y gives theta(y)>=3 log N for all sufficiently large N. The distinct prime divisors of N have total logarithm log(rad N)<=log N. Consequently

\[
\sum_{\substack{p\le y\\p\nmid N}}\log p\ge2\log N,
\qquad
\#\{p\le y:p\nmid N\}\ge\frac{y}{2\log y}.
\tag{3}
\]

Because N is even, all these missing primes exceed 2. Let

\[
s_N=\sum_{\substack{p\nmid N\\p>2}}\frac1{p(p-1)}.
\]

The sum is at most sum_{m>=3}1/[m(m-1)]=1/2. Since 1-u<=exp(-u), absolute convergence of the product gives

\[
\delta_N\ge1-e^{-s_N}\ge s_N/2.
\]

Every term from (3) is at least 1/[y(y-1)], so

\[
\delta_N\ge\frac1{4(y-1)\log y}\gg\frac1{y\log y}.
\tag{4}
\]

Now separate two exhaustive cases.

If some missing prime p satisfies p<=sqrt(y), the corresponding single Euler factor gives delta_N>=1/[p(p-1)]>=1/y. As S(N)>=2C_2, this already yields S(N)delta_N>=2C_2/y.

Otherwise every prime p<=sqrt(y) divides N. For odd primes p, (p-1)/(p-2)>=(1-1/p)^(-1). Thus Mertens' product estimate gives

\[
\begin{split}
\mathfrak S(N)
&\ge2C_2\prod_{2<p\le\sqrt y}\left(1-\frac1p\right)^{-1}\\
&=C_2\prod_{p\le\sqrt y}\left(1-\frac1p\right)^{-1}
 \gg\log y.
\end{split}
\]

Combining this with (4) again gives S(N)delta_N>>1/y. Since y=4 log N, both cases prove (1). The argument uses no representation of N by primes.

## Sharpness along primorials

Take N_y=product_{p<=y}p. Then log N_y=theta(y)~y. The exact factor identity

\[
\frac{p-1}{p-2}
 =\left(1-\frac1p\right)^{-1}
  \left(1-\frac1{(p-1)^2}\right)^{-1}
\quad(p>2)
\]

and Mertens' product asymptotic imply

\[
\mathfrak S(N_y)\sim e^\gamma\log y.
\]

The missing primes are exactly p>y. Partial summation using the prime number theorem yields

\[
\sum_{p>y}\frac1{p(p-1)}
 \sim\sum_{p>y}\frac1{p^2}
 \sim\frac1{y\log y}.
\]

This sum tends to zero, so one minus the product of its factors is asymptotic to the sum. Hence delta_{N_y}~1/[y log y], and multiplying proves (2). In particular no absolute positive constant lower bound for S(N)delta_N is possible. The uniform order 1/log N is optimal up to constants.

## Conditional consequence for the operator attempt

Assume the endpoint-corrected decomposition in `lower-proposal.md` is justified at its stated assurance level. Its operator is controlled by the already reviewed finite Abel lemma:

\[
|\mathcal O_N(N^\theta)|
 \le\log(N-1)\sum_{\substack{k<N^{1-\theta}\\(k,N)=1}}
                 \max_{j<N}|E_k(j)|.
\]

Therefore, for one fixed 0<theta<1/2 and eta>0, the still-unproved estimate

\[
\sum_{\substack{k<N^{1-\theta}\\(k,N)=1}}
 \max_{j<N}|E_k(j)|
 =O\left(\frac{N}{(\log N)^{2+\eta}}\right)
\tag{T2-open}
\]

would make the operator o(N/log N), smaller than the guaranteed margin S(N)delta_N*N. It would give the one-sided sufficient condition with, for example, kappa=1/2 eventually. The analytic remainders must also be o(N/log N), which the proposal's arbitrary logarithmic saving would supply if its reduction passes review.

This improves the sufficient fixed logarithmic saving exponent from 3+eta to 2+eta by retaining the product of the local factors. **T2-open remains unproved.** This does not improve the known distribution level, eliminate the reflected Mobius twist, or construct a Goldbach representation. It is a refinement of a conditional reduction.

The established inputs are standard PNT and Mertens estimates, also used in the inspected [Huang-Li corollary calculation](https://arxiv.org/html/2005.03811) and [Tao's account of Mertens' theorems](https://terrytao.wordpress.com/2013/12/11/mertens-theorems/). Priority has not been investigated. No claim of novelty follows from this derivation.
