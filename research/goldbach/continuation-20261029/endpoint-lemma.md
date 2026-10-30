# Exact transfer with a moving endpoint

29 October 2026. Supplemental mathematical-author statement for `GOLDBACH-UNIFORM-002`.

**Claim status: proved by the handwritten elementary argument below, pending the separate substantive critic.** No proof assistant was run. This is a finite Abel-summation lemma and a corrected divisor-switch identity. It does not prove an Elliott–Halberstam hypothesis or Goldbach. No novelty claim is made: [Moya's primary record](https://zenodo.org/records/21939906) announces a repair of the same cutoff issue, although its PDF was inaccessible to the survey worker. The original rearrangement and maximal hypothesis were inspected in [Huang–Li v2, section 3.2](https://arxiv.org/html/2005.03811).

## Definitions and strict integer endpoints

Let \(N\ge3\) be an integer, let \(1<\eta<N-1\) be real, and let \(f:\{1,\ldots,N-1\}\to\mathbb C\) be arbitrary. For a positive integer \(k\) coprime to \(N\), put

\[
g_k(n)=f(n)\left(\mathbf1_{n\equiv N\pmod{k}}-\frac1{\phi(k)}\right),
\qquad E_k(j)=\sum_{n=1}^jg_k(n),\qquad E_k(0)=0.
\]

Write

\[
M_k=\max\{0,\lceil N-\eta k\rceil-1\},\qquad
w_k(n)=\log\frac{k}{N-n}.
\]

The admissible integers \(1\le n<N-\eta k\) are exactly \(1\le n\le M_k\). This convention handles both integral and nonintegral \(\eta k\), including strict equality at the boundary.

For the lemma, restrict to

\[
\mathcal K=\{k\in\mathbb N:1\le k<(N-1)/\eta,\ (k,N)=1\}.
\]

Each such \(k\) has \(1\le M_k\le N-2\). Terms with \(M_k=0\), if included in an extended sum, contribute zero.

## Lemma 1: transfer with constant one

For arbitrary complex coefficients \(c_k\),

\[
\begin{split}
&\left|\sum_{k\in\mathcal K}c_k
 \left(\sum_{\substack{1\le n<N-\eta k\\n\equiv N\ (k)}}
       f(n)\log\frac{k}{N-n}
 -\frac1{\phi(k)}\sum_{1\le n<N-\eta k}
       f(n)\log\frac{k}{N-n}\right)\right|\\
&\quad\le\sum_{k\in\mathcal K}|c_k|\log\frac{N-1}{k}
                 \max_{0\le j\le M_k}|E_k(j)|\\
&\quad\le\log(N-1)\sum_{k\in\mathcal K}|c_k|
                 \max_{0\le j<N}|E_k(j)|.
\end{split}
\]

In particular, \(|c_k|\le1\) gives a bound by \(\log(N-1)\) times the sum of maximal discrepancies, with no unspecified constant.

**Proof.** Fix \(k\in\mathcal K\) and abbreviate \(M=M_k\), \(w=w_k\), \(E=E_k\). Since \(N-n>\eta k>k\) throughout the interval, \(w(n)<0\). Since \(N-n\) decreases with \(n\), \(w(n)\) increases with \(n\). Discrete Abel summation gives the exact identity

\[
\sum_{n=1}^Mg_k(n)w(n)
 =E(M)w(M)+\sum_{j=1}^{M-1}E(j)\bigl(w(j)-w(j+1)\bigr).
\]

Taking absolute values and setting \(D_k=\max_{0\le j\le M}|E(j)|\),

\[
\begin{split}
\left|\sum_{n=1}^Mg_k(n)w(n)\right|
&\le D_k\left[-w(M)+\sum_{j=1}^{M-1}\bigl(w(j+1)-w(j)\bigr)\right]\\
&=D_k[-w(1)]
 =D_k\log\frac{N-1}{k}.
\end{split}
\]

The difference of the two weighted sums in the statement is exactly the sum on this left side. Sum over \(k\), use the triangle inequality, and note \(\log((N-1)/k)\le\log(N-1)\). This also covers \(M=1\), where the intermediate sum is empty. The \(k=1\) discrepancy is identically zero because \(\phi(1)=1\). This proves the result. □

The argument does not require \(f\) to be real, nonnegative, multiplicative or supported on primes. It does not require cancellation between different moduli.

## Corollary 2: what the maximal twisted input would supply

Take \(f(n)=\Lambda(n)\mu(N-n)\), \(c_k=\mu(k)\), \(\eta=N^\theta\), with fixed \(0<\theta<1\). For sufficiently large \(N\), the hypotheses on \(\eta\) hold. If, for every \(B>0\),

\[
\sum_{\substack{k<N^{1-\theta}\\(k,N)=1}}
       \max_{0\le j<N}|E_k(j)|\ll_B\frac{N}{(\log N)^B},
\]

then the coprime part of the moving weighted AP replacement has error

\[
O_B\left(\frac{N}{(\log N)^{B-1}}\right).
\]

**Proof.** The modulus set in Lemma 1 is a subset of \(k<N^{1-\theta}\), and \(|\mu(k)|\le1\). Apply the lemma. Taking \(B=A+1\) provides \(O_A(N/(\log N)^A)\). □

This corollary establishes only the transfer implication. It assumes the maximal twisted estimate and does not prove it. It also does not estimate the remaining global main term or the noncoprime-modulus part of a full analytic proof.

## Lemma 3: exact divisor-switch identity

Let \(\Lambda\) and \(\mu\) be the ordinary von Mangoldt and Möbius functions on the positive integers. Under the same \(N,\eta\), define

\[
S_2(N,\eta)=\sum_{n=1}^{N-1}\Lambda(n)\mu^2(N-n)
               \sum_{\substack{d\mid N-n\\d>\eta}}\mu(d)\log(1/d).
\]

Then, exactly,

\[
S_2(N,\eta)=\sum_{1\le k<(N-1)/\eta}\mu(k)
      \sum_{\substack{1\le n<N-\eta k\\n\equiv N\pmod{k}}}
       \Lambda(n)\mu(N-n)\log\frac{k}{N-n}.
\]

**Proof.** For each \(n\), put \(h=N-n\ge1\). If \(h\) is nonsquarefree, \(\mu^2(h)=\mu(h)=0\), so both contributions vanish. If \(h\) is squarefree, the divisor bijection \(k=h/d\) gives \(\mu(d)=\mu(h)\mu(k)\). Moreover

\[
d>\eta\iff k<h/\eta\iff n<N-\eta k,
\qquad \log(1/d)=\log(k/h).
\]

The condition \(k\mid h\) is \(n\equiv N\pmod{k}\). Since \(1\le h\le N-1\), every admitted \(k\) satisfies \(k<(N-1)/\eta\). Conversely, every pair \((k,n)\) on the right determines the integer divisor \(d=h/k>\eta\) on the left. All sums are finite, so their order can be interchanged. This proves the identity, with no coprimality restriction discarded. □

To apply Lemma 1, split the exact outer sum into \((k,N)=1\) and \((k,N)>1\). Only the former is controlled by that lemma. The second part remains an explicit separate obligation rather than an assumed error.

## A full-endpoint counterexample

This is an arbitrary-sequence test of the transfer argument, not a prime model or a Goldbach counterexample. Set \(N=10\), \(k=3\), \(\eta=2\), and

\[
f(1)=f(8)=1,\qquad f(n)=0\quad(n\notin\{1,8\}).
\]

Here \(\phi(3)=2\), \(N\equiv1\pmod3\), and \(M_3=3\). At the full endpoint \(j=9\),

\[
E_3(9)=1-\frac{2}{2}=0.
\]

Indeed both reduced residue classes modulo 3 have zero full-endpoint discrepancy: each contains one unit of mass, and the global mass is two. Nevertheless,

\[
E_3(3)=1-\frac12=\frac12,
\]

and the moving weighted discrepancy is

\[
\sum_{n=1}^{3}g_3(n)\log\frac{3}{10-n}
 =\frac12\log\frac39=-\frac12\log3\ne0.
\]

In this example Lemma 1's single-modulus bound is attained exactly:

\[
\left|\text{moving weighted discrepancy}\right|
 =\log\frac{9}{3}\max_{0\le j\le3}|E_3(j)|
 =\frac12\log3.
\]

Thus even complete cancellation at the full endpoint for every reduced residue of this modulus cannot replace maximal endpoint information in a general transfer lemma. This does not rule out a separate arithmetic argument that controls the omitted tail for a special sequence.

## Exact limits of the result

The elementary transfer lemma is proved without an analytic conjecture. Its prime-weighted corollary is conditional on an open discrepancy estimate. The divisor switch corrects a finite identity and preserves an explicit noncoprime remainder. None supplies a pointwise lower bound for prime pairs, a proof of the signed cubic criterion, or a Goldbach breakthrough. Its purpose is to prevent a false simplification of the proposed analytic input.
