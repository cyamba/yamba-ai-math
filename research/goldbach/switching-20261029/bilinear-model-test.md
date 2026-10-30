# An explicit bilinear test distinguishes the parity model

29 October 2026. Root-authored supplement to `parity-model.md`, submitted for separate review. This is a test of that model, not a bound for actual shifted primes and not a Goldbach breakthrough.

Let a_+(n)=w(n)(1+lambda(n)) be the unnormalized plus model defined there. The exact identity

\[
\mu(n)a_+(n)=\mu(n)^2a_+(n)\ge0
\]

holds: if n is nonsquarefree both sides vanish; if n is squarefree then mu(n)=lambda(n), so either a_+(n)=0 or mu(n)=1.

Fix M=x^(2/5), and consider the concrete expression

\[
\mathcal B(x)=\sum_{m\ge1}\left|
       \sum_{\substack{M<k\le2M\\mk\le x}}
                       \mu(mk)a_+(mk)\right|.
\]

Every summand of the inner sum is nonnegative. Retain only prime k in (M,2M] and prime m in (x/(4M),x/(2M)]. Then mk<=x, both primes are odd and distinct for sufficiently large x, and mu(mk)a_+(mk)=2w(mk)>=2. The prime number theorem gives

\[
\#\{M<k\le2M:k\text{ prime}\}\gg\frac{M}{\log x},
\quad
\#\{x/(4M)<m\le x/(2M):m\text{ prime}\}
                      \gg\frac{x}{M\log x}.
\]

Consequently

\[
\boxed{\mathcal B(x)\gg x/(\log x)^2.}
\]

This test does not have arbitrary logarithmic saving despite the model's arbitrarily strong divisor-sum distribution. After scaling the model to mass li(x), the same conclusion is a lower bound by a constant times li(x)/log(x)^2. Thus a bilinear axiom demanding o(total_mass/log(x)^2) for this expression cannot be deduced from the divisor-density axioms alone.

This expression is the C=1 case of the Mobius-weighted inner structure discussed in the Friedlander-Iwaniec comparison, since gamma(k,1)=1. Application of their full theorem still requires all of its parameter and uniformity conditions. No assertion that the actual prime-complement sequence fails this test is made. The calculation shows exactly one kind of additional correlation information capable of excluding the model, rather than merely calling it a parity obstruction.
