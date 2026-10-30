# A pointwise upper bound for near-cubic contamination

29 October 2026. Registry role: Mathematician. Input: the completed `survey.md` and its result in the populated statement packet. This is a handwritten derivation using an inspected classical upper-bound sieve. Its separate critic stage is pending. No formal verification, novelty claim, or solution of Goldbach is asserted.

## Claim and definitions

For even integer N, write

\[
\mathfrak S(N)=2C_2\prod_{\substack{\ell\mid N\\\ell>2}}
 \frac{\ell-1}{\ell-2},\qquad
C_2=\prod_{\ell>2}\left(1-\frac1{(\ell-1)^2}\right),
\]

where products indexed by ell are over primes. Let omega(N) denote the number of distinct prime divisors of N, and let omega_{>z}(N) count those exceeding z. For real alpha set z=N^alpha and

\[
H_\alpha(N)=\#\{p\text{ prime}:N-p>1,\ \Omega(N-p)=3,
                         \ P^-(N-p)>z\}.
\]

Prime factors are counted with multiplicity in Omega. The prime p is unrestricted by z. Equivalently, the other summand has a unique sorted factorization N-p=abc with primes z<a<=b<=c. H counts the summand p once, rather than counting permutations of its three factors. A strict comparison with z is equivalent to comparison with floor(z) for integer prime factors.

**Proposition H, status: proved by the argument below, pending independent review.** There are absolute constants C>0 and N0>=16 such that, simultaneously for every even N>=N0 and every real

\[
0\le\varepsilon\le1/30,\qquad \alpha=1/3-\varepsilon,
\]

one has

\[
\boxed{\quad H_\alpha(N)\le\omega_{>N^\alpha}(N)+
 C\mathfrak S(N)\frac{N}{\log^2N}
              \left(\varepsilon+\frac1{\log N}\right)^2.\quad} \tag{H}
\]

The exceptional term omega_{>N^alpha}(N) is at most 3 throughout this range, so it can be replaced by 3, or more weakly by omega(N). C and N0 are effective absolute constants whose numerical values have not been extracted from the classical estimates. In particular, for each fixed epsilon in (0,1/30],

\[
\limsup_{\substack{N\to\infty\\2\mid N}}
 \frac{H_{1/3-\varepsilon}(N)}{\mathfrak S(N)N/\log^2N}
 \le C\varepsilon^2. \tag{H-fixed}
\]

This is a pointwise upper bound, rather than an average over targets. It is a consequence of classical sieve theory. Its priority has not been investigated sufficiently to claim novelty.

## Inspected classical inputs

Kevin Ford, *Sieve Methods Lecture Notes, Spring 2023*, [Theorem 2.5 and proof, printed pages 19-21](https://ford126.web.illinois.edu/sieve2023.pdf), gives the upper bound

\[
\#\{1\le n\le x:L_1(n),L_2(n)\text{ prime}\}
 \le K\mathfrak S(L_1,L_2)x/\log^2x
\]

for distinct primitive admissible integer linear forms, with an absolute K for two forms. The theorem allows negative coefficients. The statement and proof explicitly keep coefficient dependence in the singular series. The proof's residue-class remainder and its small-prime exceptions are included in this bound; no unquantified per-coefficient asymptotic is used here.

Terence Tao, [*Mertens' theorems*, Theorem 1, equation (1), and Remark 1](https://terrytao.wordpress.com/2013/12/11/mertens-theorems/), supplies the classical bound A(t)=sum_{ell<=t}(log ell)/ell=log t+O(1). The interval estimate used below is derived explicitly by partial summation, including its error. Neither an unproved prime-tuple lower bound nor a prime-distribution conjecture is an input.

## Proof

If epsilon=0, all three factors would exceed N^(1/3), so H=0. Suppose henceforth 0<epsilon<=1/30. Then alpha>=3/10 and z>2 for N>=16.

For each counted p choose the sorted factorization N-p=abc and put m=ab. All three factors exceed z and their product is less than N. Consequently

\[
z<a,b,c<Y:=N/z^2=N^{1-2\alpha},\quad
m<N/z,\quad x_m:=N/m>z. \tag{1}
\]

The first inequality holds for every one of the three factors, since the other two exceed z. Sorting makes this assignment unique even for repeated factors.

If gcd(m,N)>1, a prime ell dividing that gcd divides both N and abc. It therefore divides p=N-abc. Since p is prime, p=ell and p divides N; moreover ell is a or b and therefore exceeds z. Distinct counted values of p in this exceptional class number at most omega_{>z}(N), globally. If there were four such prime divisors, their product would exceed z^4=N^(4 alpha)>N, which is impossible. Thus the exception is at most 3. We do not sum it separately for each m.

For the remaining p, gcd(m,N)=1. Consider the forms

\[
L_1(t)=t,\qquad L_2(t)=N-mt.
\]

They are distinct, have nonzero integer coefficients, and are primitive because gcd(m,N)=1. Since a,b are odd, m is odd. The number rho(ell) of roots of L_1(t)L_2(t) modulo ell is

\[
\rho(\ell)=\begin{cases}
1,&\ell\mid Nm,\\
2,&\ell\nmid Nm.
\end{cases} \tag{2}
\]

In particular rho(2)=1 and rho(ell)<ell at every prime, so the forms are admissible. If ell divides N, the two roots coincide at zero. If ell divides m, the second form is a nonzero constant modulo ell and the first has one root. There is no common divisor of m and N in this case.

Comparison of the Euler products gives the exact identity

\[
\mathfrak S(L_1,L_2)
 =\mathfrak S(N)\prod_{\ell\mid m}\frac{\ell-1}{\ell-2}
 \le4\mathfrak S(N). \tag{3}
\]

Each prime divisor of m exceeds z>2, there are at most two distinct such divisors, and each displayed ratio is at most 2. If a=b the product contains that prime once, so (3) remains valid.

By Ford's coefficient-uniform bound, the number of possible c for a fixed pair (a,b) is at most

\[
4K\mathfrak S(N)\frac{x_m}{\log^2x_m}
 \le\frac{4K}{(3/10)^2}\mathfrak S(N)
        \frac{N}{ab\log^2N}, \tag{4}
\]

where (1) gives log x_m>alpha log N. We have enlarged the c range to all positive integers c<=x_m and need not require c>=b in the upper bound. Prime outputs equal to a small sieving prime are already handled by the cited theorem. They are not silently discarded.

Sum (4) over its actual permissible (a,b), then enlarge to all ordered prime pairs in (z,Y]. Nonnegative summands permit this enlargement, yielding

\[
H_\alpha(N)\le\omega_{>N^\alpha}(N)+K_1\mathfrak S(N)
 \frac{N}{\log^2N}
 \left(\sum_{z<\ell\le Y}\frac1\ell\right)^2. \tag{5}
\]

The restriction ab<N/z was used before the enlargement, to obtain (4). We do not apply (4) to the extra pairs after discarding that restriction. No factor of 6 is divided out; repeated factors and the chosen sorted representation cause only harmless overcounting in (5).

For completeness, write A(t)=log t+E(t), with |E(t)|<=K_2 for t>=2 by Mertens' first estimate. Stieltjes partial summation on the interval (z,Y] gives

\[
\begin{split}
\sum_{z<\ell\le Y}\frac1\ell
 &=\frac{A(Y)}{\log Y}-\frac{A(z)}{\log z}
       +\int_z^Y\frac{A(t)}{t\log^2t}\,dt\\
 &=\log\frac{\log Y}{\log z}+O(1/\log z)\\
 &=\log\frac{1-2\alpha}{\alpha}+O(1/\log N), \tag{6}
\end{split}
\]

uniformly for 3/10<=alpha<=1/3. The error follows by bounding the two endpoint E terms and the integral by 3K_2/log z. This proof works if z or Y is prime: A(z) includes its endpoint, as appropriate to the strict lower cutoff.

Finally,

\[
0\le\log\frac{1-2\alpha}{\alpha}
 =\log\left(1+\frac{3\varepsilon}{1/3-\varepsilon}\right)
 \le10\varepsilon. \tag{7}
\]

Equations (5)-(7) prove (H), with one absolute constant. Since omega_{>z}(N)<=3 and mathfrak S(N)>=2C_2>0, its normalized exceptional term tends to zero. Taking N to infinity at fixed epsilon gives (H-fixed). This completes the argument.

## Why the remainder and cutoff conventions matter

The stronger assertion H_alpha(N)<=C*epsilon^2*mathfrak S(N)*N/log^2N with no error, uniformly in epsilon depending on N, is false. Let r run through odd primes tending to infinity, N=r^3+3, and

\[
\delta_N=\frac13-\frac{\log r}{\log N},\qquad
\varepsilon_N=2\delta_N,\qquad\alpha_N=1/3-\varepsilon_N.
\]

Then delta_N>0, epsilon_N tends to zero, alpha_N>=3/10 eventually, and r>N^alpha_N. Thus p=3, q=r^3 is counted and H_alpha_N(N)>=1. But epsilon_N=O(1/(N log N)). Even the crude bound mathfrak S(N)<=2C_2(N-1), obtained by extending its finite product to all integers 3 through N, makes C*epsilon_N^2*mathfrak S(N)*N/log^2N tend to zero. A uniform pure-epsilon-squared assertion is therefore refuted. This does not refute (H-fixed), whose epsilon is fixed first, or (H), which retains its lower-scale terms.

The roughness requirement is substantive: it confines the two factored-out primes to a multiplicative interval whose reciprocal-prime mass is O(epsilon+1/log N). Dropping it removes the squared gain. The even-target and coprimality conditions are the ones that make the two linear forms admissible.

## What remains open

For the brief's U_alpha and L_alpha, let F_alpha=(U_alpha-L_alpha)/2. Since alpha>1/4, a rough complement less than N has at most three factors. Therefore F_alpha counts prime and triple-prime complements, and the exact identity is R_z=F_alpha-H_alpha. Its proof is the parity classification and does not provide a lower bound for F_alpha.

Put A_N=mathfrak S(N)N/log^2N. For one fixed epsilon in (0,1/30], a sufficient missing input is

\[
\liminf_{\substack{N\to\infty\\2\mid N}}
 F_{1/3-\varepsilon}(N)/A_N>C\varepsilon^2. \tag{P-open}
\]

Here C is the constant already obtained in (H), rather than one chosen after a purported lower bound. Combining (P-open) with (H-fixed) would give a positive prime-pair count for every sufficiently large even N. **Status of (P-open): conjectural and unproved here.** Chen's nonnegative almost-prime count and the prior negative signed mean do not supply it. There is no justification for assuming a lower-bound constant independent of epsilon, or for optimizing epsilon using an unproved uniform lower estimate.

Dependency map: inspected classical two-form upper sieve + inspected Mertens estimate -> (H); exact parity classification -> R_z=F_alpha-H_alpha; (H) + unproved pointwise parity input (P-open) -> sufficiently-large Goldbach. No arrow in the derivation of (H) uses Goldbach or (P-open).

The narrow next question is whether a noncircular parity-sensitive lower estimate for F_alpha can be obtained with strength larger than the now-controlled O(epsilon^2) contamination. Until that input is proved, this result is technical progress within the proposed approach and is not a solution or claimed breakthrough on Goldbach.
