# Revision of the switching attempt and model tests

29 October 2026. Registry role: Mathematician, `GOLDBACH-SWITCHING-004`. This revision uses the populated `revise` packet, the separate `review.md`, and the independent finite-check response. The reviewed `statement.md`, `parity-model.md`, and `bilinear-model-test.md` remain unchanged. No further source search or computation was performed in this revision.

## Accepted one-switch calculation

The critic supports the exact least-prime partition and the classical coefficient calculation in the stated fixed-parameter domain:

\[
3/10\le\alpha<1/3,\quad\alpha<d<1/2,\quad d/4\le\beta<d/2.
\]

For the original unweighted counts and A_N=mathfrak S(N)N/log^2N, the initial lower coefficient and summed switching upper coefficient are

\[
L=\frac2d\log\frac{d-\beta}{\beta},\qquad
J=\frac2d\log\frac{\alpha(d-\beta)}{\beta(d-\alpha)}.
\]

The legal upper cutoff is v_r=min(r,sqrt(N^d/r)), with its actual local density retained. It keeps the imported theorem's sieve parameter in [2,3]; no application outside its inspected domain is required. The base mass is li(N), so the stated unweighted normalization is correct. Each switched remainder modulus has r as its unique largest prime factor, permitting the summed ordinary BV remainder control.

The pre-semiprime coefficient is therefore exactly

\[
\boxed{M=L-J=\frac2d\log\frac{d-\alpha}{\alpha}
                  \le4\log(2/3)\le-4/3<0.}
\]

It is independent of beta. The additional valid semiprime upper coefficient K2*I(alpha) is nonnegative, so subtracting it cannot produce a positive lower coefficient. The concrete choice d=49/100, alpha=3/10, beta=1/5 gives M=(200/49)log(19/30)<=-220/147. These analytic sign certificates do not depend on floating-point evaluation.

The exact identities retain q=r through the remaining factor m=1 and all repeated factors. The raw q=1 term is excluded separately from U. Prime summands dividing N are removed globally before using reduced residue classes. Strict cutoff endpoints and the successive sieve-tolerance limit remain as in the frozen statement: fix the tolerance, send N to infinity, then send the tolerance to zero.

**Precisely the refuted assertion:** “This chosen one-switch family, using these declared classical coefficients, yields a positive leading lower coefficient for F_alpha.” The original response attached `refuted` to a sentence describing the true failure; this wording identifies the failed positive assertion explicitly. The certificate does not say that the actual F count is negative, that actual primes fail a conjectured correlation bound, or that every switching or Chen double-sieve identity fails.

## Accepted weighted parity model

The separately root-authored construction specializes the classical Selberg parity example to the exact local density of an odd shifted-prime sieve. On odd n define

\[
w(n)=\prod_{p\mid n}\frac{p-1}{p-2},\qquad
a_\pm(n)=w(n)(1\pm\lambda(n)),\qquad
C_0=1/(2C_2),
\]

and set the weights to zero on even n. The weights are nonnegative real numbers. The plus sequence vanishes whenever Omega(n) is odd, including all primes and all three-factor products.

The critic supports the derived divisor estimate: for every fixed epsilon in (0,1) and every fixed A>0,

\[
\sum_{d\le x^{1-\varepsilon},\ d\text{ odd}}
 \left|\sum_{n\le x,\ d\mid n}a_\pm(n)
                   -\frac{C_0x}{\phi(d)}\right|
 \ll_{A,\varepsilon}x/(\log x)^A.
\]

Thus g(p)=1/(p-1) for odd primes and g(2)=0. Scaling both sequences on [1,x] by li(x)/(C0*x) gives main mass li(x)/phi(d) and retains arbitrary logarithmic savings. Removing n=1 costs a bounded amount in the d=1 sum only. The model has exact zero odd-factor rough population at every cutoff, despite this divisor distribution through every fixed level below 1.

For targets N=2^k, this is the ordinary local divisor-density profile of the shifted-prime sieve. It follows that those general nonnegative weighted divisor-sieve assumptions alone cannot imply a positive weighted odd-factor population. This is stronger than the leading-density-only obstruction from the earlier sparse deletion construction, within its specified weighted setting.

The model is not an indicator of actual reflected primes. It does not assert equidistribution in every nonzero residue class, prime reflection identities, or all additional upper bounds exploiting actual primes. It cannot be assumed to satisfy those properties. Its obstruction is scoped to the divisor-density data that were actually proved.

## A concrete additional bilinear distinction

The separately reviewed supplement tests the model rather than actual prime complements. For its unnormalized plus sequence,

\[
\mu(n)a_+(n)=\mu(n)^2a_+(n)\ge0.
\]

At M=x^(2/5), consider exactly

\[
\mathcal B(x)=\sum_m\left|
 \sum_{M<k\le2M,\ mk\le x}\mu(mk)a_+(mk)\right|.
\]

Retaining prime k in (M,2M] and prime m in (x/(4M),x/(2M)] gives distinct odd factors, products at most x, and individual weights at least 2. PNT therefore gives

\[
\mathcal B(x)\gg x/(\log x)^2.
\]

After the mass-li(x) scaling, the corresponding bound is a constant times li(x)/log^2x. In particular, a bound o(total mass/log^2x) for this concrete expression cannot follow from the proved divisor-density axioms alone. It contains the C=1 Möbius inner structure of the FI comparison, but this calculation does not check every parameter hypothesis of that theorem or every possible choice of M.

This identifies one explicit kind of additional parity-sensitive information that excludes the model. No such upper bound has been proved for actual reflected primes. The model's failure of the test is not evidence that actual primes fail it.

## Independent checks and assurance

The finite worker reports 22,482 exact least-prime switching identities and 7,494 parity identities through even N=5,000, with 48 trial-division cross-checks and zero failures. It preserved m=1, repeated factors, and prime divisors of N. Its symbolic coefficient simplification independently cancels beta, and rational logarithm enclosures plus the analytic bound certify the negative coefficient. The numerical diagnostics agree with those formulas at their recorded tolerance.

These finite checks address arithmetic implementation and coefficient evaluation. They do not establish the infinite sieve remainder control or the parity model's all-log asymptotic by themselves. The mathematical assurance is complete handwritten derivation from the stated inspected classical inputs, plus a separate host-agent substantive review. There is no proof-assistant verification or external human peer review. Numerical effective constants, finite thresholds and novelty remain unverified. The model is a specialization of a classical obstruction, so no priority claim follows from deriving it here.

## Objective and next input

The research goal remains open. This tranche establishes a scoped negative coefficient certificate and an explicit weighted obstruction with a bilinear distinction. It supplies no positive lower margin for the actual F_alpha, no proof of the pointwise cubic sign target, and no Goldbach proof or demonstrated breakthrough.

The next effort must use additional parity-sensitive information about actual primes. Ordinary beta optimization in this one-switch family cannot change its coefficient, and merely increasing ordinary divisor distribution does not remove the weighted model. A different switching identity must justify genuinely additional correction terms, or an analytic method must establish a correlation that excludes the model and meets its actual target-uniform hypotheses.

The root is inspecting the LWW prime-list method in arXiv:2610.20242v1 as a possible distinct bridge. No theorem from that manuscript is validated or imported in this revision. A subsequent bounded bridge attempt must check its precise source statement, parity weights, endpoint control, fixed polynomial roughness and uniformity in the Goldbach target before using it. Neither a related title nor the existence of a prime-list result supplies that missing analytic input.
