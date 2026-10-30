# A parity model with the exact odd-prime sieve density

29 October 2026. Supplemental root-authored mathematical argument, pending separate review. This specializes the classical Selberg parity example to the local density 1/(p-1) of a shifted-prime sieve. It is not a model of the actual primes, a counterexample to Goldbach, or a novelty claim. The classical example and the Liouville summatory estimate are described in [Ford, section 1.7.4](https://ford126.web.illinois.edu/sieve2023.pdf).

## Statement and scope

Let C_2 be the twin-prime Euler product and C_0=1/(2C_2). For odd n set

\[
w(n)=\prod_{p\mid n}\frac{p-1}{p-2},
\]

with w(1)=1, and put w(n)=0 for even n. Let lambda(n)=(-1)^Omega(n), with ordinary prime-factor multiplicity. Define a_+(n)=w(n)(1+lambda(n)) and a_-(n)=w(n)(1-lambda(n)). Both are nonnegative, and a_+ is zero whenever Omega(n) is odd, including every prime and every product of three primes.

For each fixed epsilon in (0,1) and A>0, the following holds as x tends to infinity:

\[
\sum_{\substack{d\le x^{1-\epsilon}\\d\text{ odd}}}
 \left|\sum_{\substack{n\le x\\d\mid n}}a_\pm(n)
                   -\frac{C_0x}{\phi(d)}\right|
 \ll_{A,\epsilon}\frac{x}{(\log x)^A}.
\tag{1}
\]

Even d have identically zero divisor sums, so g(p)=1/(p-1) for odd primes and g(2)=0. If a mass li(x) is desired, multiply both sequences on [1,x] by li(x)/(C_0x). Then (1) has main term li(x)/phi(d) and retains every logarithmic saving. These are positive real weights, not asserted indicator functions.

For the Goldbach target family N=2^k, these are exactly the ordinary local divisor densities used for prime complements: g(d)=1/phi(d) for odd squarefree d, and zero for even d. Nevertheless the plus model has identically zero odd-Omega rough population at every cutoff. Thus the divisor-density assumptions alone, even with distribution through x^(1-epsilon), cannot imply a positive weighted odd-Omega population for all nonnegative sequences. This is a scoped obstruction to arguments using only those data, not to methods exploiting additional arithmetic of actual primes, correlation hypotheses, or extra bilinear information.

## Elementary coefficient bounds

Define a nonnegative multiplicative function h by h(p)=1/(p-2) for odd primes, h(p^j)=0 for j>=2, and h(2^j)=0 for j>=1. Then for odd n,

\[
w(n)=\sum_{e\mid n}h(e).
\]

The inequality h(e)<=tau_3(e)/e gives

\[
\sum_{e\le Y}h(e)\ll(\log(2Y))^3,
\qquad
\sum_{e>Y}\frac{h(e)}e\ll\frac{(\log(2Y))^2}{Y}.
\tag{2}
\]

The first follows by expanding tau_3 into triples and the harmonic sum. For the second, sum_{e<=T}tau_3(e)<=T(1+log T)^2 and partial summation, or dyadic summation, gives sum_{e>Y}tau_3(e)/e^2<<log(2Y)^2/Y. Also

\[
\sum_e\frac{h(e)}e
 =\prod_{p>2}\left(1+\frac1{p(p-2)}\right)=C_2^{-1}.
\tag{3}
\]

In particular, by positivity,

\[
\sum_{n\le T}w(n)\ll T,
\qquad
\sum_{d\le T}\frac{w(d)}d\ll\log(2T).
\tag{4}
\]

Here even terms are zero. The first bound follows by expanding w and counting odd multiples; the second follows by partial summation. All implied constants in (2)-(4) are absolute.

## Divisor sums of the untwisted weight

Fix odd d, not necessarily squarefree, and put Y=x/d. The factorization identity

\[
w(dm)=w(d)\mathbf1_{m\text{ odd}}
                  \sum_{\substack{e\mid m\\(e,d)=1}}h(e)
\]

is checked prime by prime. Therefore

\[
\begin{split}
W_d(x)&:=\sum_{n\le x,d\mid n}w(n)\\
&=w(d)\sum_{\substack{e\le Y\\(e,d)=1}}h(e)
                    \left(\frac{Y}{2e}+O(1)\right)\\
&=\frac{w(d)Y}{2}
       \prod_{\substack{p>2\\p\nmid d}}
             \left(1+\frac1{p(p-2)}\right)
       +O(w(d)(\log(2Y))^3).
\end{split}
\]

Extending the main sum uses the second bound in (2). At each prime dividing d,

\[
\frac{(p-1)/(p-2)}{1+1/[p(p-2)]}=\frac p{p-1}.
\]

Consequently

\[
W_d(x)=\frac{C_0x}{\phi(d)}
                     +O(w(d)(\log(2x))^3).
\tag{5}
\]

By (4), the sum of these error bounds through d<=D is O(D log(2x)^3). For D=x^(1-epsilon) this is smaller than x/log(x)^A for every fixed A, eventually.

## Divisor sums of the parity twist

The standard classical estimate for L(t)=sum_{n<=t}lambda(n) gives L(t)<<_B t/log(2t)^B for every fixed B>0. Its odd-part version obeys the same bound, because

\[
L_{\rm odd}(t)=L(t)+L(t/2).
\]

Complete multiplicativity of lambda and the expansion above yield

\[
\begin{split}
J_d(x)&:=\sum_{n\le x,d\mid n}w(n)\lambda(n)\\
&=\lambda(d)w(d)
 \sum_{\substack{e\le Y\\(e,d)=1}}\mu(e)h(e)L_{\rm odd}(Y/e).
\end{split}
\]

For e<=sqrt(Y), apply the classical bound and (3), giving O_B(Y/log(2Y)^B) before the factor w(d). For e>sqrt(Y), use |L_odd(t)|<=t and (2), giving O(sqrt(Y)log(2Y)^2). Since d<=x^(1-epsilon) implies Y>=x^epsilon, this second bound is also O_{B,epsilon}(Y/log(x)^B) for sufficiently large x. Thus, uniformly over the admitted d,

\[
|J_d(x)|\ll_{B,\epsilon}
             \frac{w(d)x}{d(\log x)^B}.
\]

Summing and using (4) gives

\[
\sum_{d\le x^{1-\epsilon},\ d\text{ odd}}|J_d(x)|
                \ll_{B,\epsilon}\frac{x}{(\log x)^{B-1}}.
\tag{6}
\]

Choose B>A+1. Combining (5)-(6) proves (1) for both signs. Removing n=1, if complements must exceed 1, changes only the d=1 sum by a bounded amount. None of this uses an arithmetic progression cancellation theorem for shifted primes.

## Exact limitation

The model matches divisor sums centered at the sieve main term; it does not assert equidistribution in every nonzero residue class. It does not retain the requirement that the first reflected coordinate be an actual prime, ordinary prime-indicator identities in that coordinate, or a Friedlander-Iwaniec bilinear axiom. Additional upper bounds derived from such extra structure must be checked separately before claiming that this model meets them.

The valid conclusion is that improving ordinary divisibility distribution alone cannot repair an odd-parity lower bound in the general nonnegative weighted-sieve setting. It does not establish an impossibility theorem for all Goldbach arguments or prove the missing operator estimate false for actual primes. This is a specialization of a classical obstruction; its priority has not been investigated.
