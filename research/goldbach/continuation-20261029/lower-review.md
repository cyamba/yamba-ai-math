# Separate review of the pointwise lower-bound attempts

29 October 2026. Registry role: Independent Critic, `GOLDBACH-LOWER-003`. This is handwritten mathematical review by a distinct host agent. It is not formal verification, external peer review, or independent provider validation. No usage measurements are available.

## Verdict and frozen inputs

**Supported, relative to the stated imported unconditional coefficient estimates and ordinary Bombieri-Vinogradov:** the endpoint-corrected decomposition (8), the squarefree-bias upper bound, the one-sided conditional closure, and the quantitative diagnoses of the two failed unconditional routes.

**Supported:** the supplemental root-authored local-factor proposition, including its sharp order and primorial asymptotic constant. It improves the sufficient maximal twisted discrepancy saving from exponent 3+eta to exponent 2+eta.

**Incomplete:** the actual Goldbach lower bound. Neither the signed operator estimate nor the specialized twisted or bilinear estimate has been proved. The accepted material is a reduction and an improvement to its sufficient hypothesis, not a Goldbach breakthrough. Novelty remains unverified.

| Reviewed file | SHA256 |
| --- | --- |
| `lower-proposal.md` | `a86f3edd4832a302dc44f4d61c033c243b53fa9ab82786fc1b86200aaa6560b7` |
| `local-gap.md` | `991a9e861577e9b5549b60e0140925a67b3f0f03ef569f5f4cc63d89a423b1b2` |

The first input is the frozen proposal supplied in the populated challenge packet. The second is a separately authored supplement. I changed neither input.

## Inspected sources and assurance boundary

I inspected [Huang-Li v2, Lemmas 1 and 3, section 3.1, and the squarefree-mass argument in section 3.3](https://arxiv.org/html/2005.03811). Lemma 1 states the two Mobius/phi coefficient estimates with an absolute exponential saving under polynomial comparability of the cutoff and target. Lemma 3 gives the truncated squarefree coefficient uniformly for even targets. These are unconditional imported estimates; the review does not re-prove their full analytic source chain. The source's erroneous full-endpoint divisor swap is not used.

I also inspected [Ford, Theorem 3.4 and the discussion of beta(1)=2](https://ford126.web.illinois.edu/sieve2023.pdf), and [Friedlander-Iwaniec, hypotheses (R), (R1), (B), (B1)-(B3), and Theorem 1](https://arxiv.org/pdf/math/9811186). Ordinary BV is an endpoint-maximal, reduced-residue estimate for primes, with square-root distribution up to logarithms. FI additionally requires a long distribution range and a distinct absolute-outer-sum Mobius bilinear estimate. Neither source supplies that specialized twisted input for reflected primes.

For the supplement I checked the proof directly using standard PNT and Mertens product estimates. The cited [Mertens account](https://terrytao.wordpress.com/2013/12/11/mertens-theorems/) was inspected during the preceding separate review. No numerical constants or finite threshold were verified.

## The short-divisor estimate checks out

This was the potentially dangerous step, because a naive summation over all divisors could lose a power of N. Let B be the polylogarithmic squarefree-expansion cutoff and Q=N^theta, with fixed theta<1/2. For squarefree d,

    1/lcm(b^2,d) = gcd(b,d)/(b^2*d).

There is no uncontrolled additive counting error: the number of positive h<N divisible by this lcm is at most N/lcm. The absolute truncation tail is therefore at most

    N log(N)^2 * sum_{b>B} b^(-2)
        * sum_{d<=Q, d squarefree} gcd(b,d)/d.

The identity gcd(b,d)=sum_{r|b,r|d}phi(r) gives

    sum_{d<=Q, d squarefree} gcd(b,d)/d
      <= (1+log Q) * sum_{r|b} phi(r)/r
      <= (1+log Q)*tau(b).

The elementary divisor estimate sum_{b>B}tau(b)/b^2 is O((log B+1)/B). It follows, for example, by writing b=rs, splitting r<=B and r>B, and summing the reciprocal-square tail in s. Thus the tail is

    O(N log(N)^3*(log B+1)/B),

which is bounded by the proposal's looser O(N log(N)^4/B). With B=(log N)^(A+4), it is O_A(N/(log N)^A). This uses no prime correlation estimate.

For b<=B, every progression modulus is r=lcm(b^2,d)<=QB^2. For fixed b and r, all primes outside b occurring in d are fixed by r, while each prime dividing b can be present in squarefree d or absent. The number of possible d is at most 2^omega(b)<=tau(b)<=b. Summing over b gives an O(B^2) multiplicity bound. Multiplying the ordinary BV error by B^2 log N costs only a fixed logarithmic power. For each chosen saving, QB^2 is eventually below the corresponding BV range, since theta<1/2 is fixed. The residue N mod r may depend on N, but BV's reduced-residue maximum permits that dependence.

If a modulus has a common prime divisor with N, a nonzero von Mangoldt term in that progression is a prime power with base dividing N. Its total weight per progression is O(log(N)^2). Multiplying by log d and the O(QB) pairs gives the stated O(QB log(N)^3), which is negligible compared with every fixed N/log(N)^A. Strict versus inclusive endpoint differences obey the same harmless power-saving bounds. The resulting main coefficient is precisely the one in the inspected Huang-Li Lemma 3, with the correct sign mu(d)log(1/d).

## The long term retains the correct sign and endpoint

The squarefree-complement divisor identity gives W=S1+S2 exactly. W differs from the prime-prime weighted count G only through prime powers in its first coordinate; O(sqrt(N) log(N)^3) is a valid upper bound for that difference.

The corrected switch keeps n<N-Qk. The noncoprime k part is O((N/Q)log(N)^3): for each k only prime-power bases dividing N can contribute, and the admitted logarithmic weights have magnitude at most log N. The coprime part equals the signed discrepancy operator plus its centered global sum.

For h=N-n, the centered coefficient uses k<h/Q exactly. Taking R_h=ceil(h/Q)-1 implements this strict condition, and

    log(k/h) = -log(R_h/k) - log(h/R_h)

produces the two coefficient sums in the proposal. When h>=Q*N^rho, R_h>=N^rho/2 eventually, so the inspected uniform coefficient estimates apply. Their error, even after all displayed log factors and summing |f_N(n)|<=log N, is smaller than N/log(N)^A for every fixed A. For h<Q*N^rho, with theta+rho<1, the O(log(N)^2) coefficient bound gives a contribution O(N^(theta+rho)log(N)^3), again negligible at every fixed logarithmic saving. The replacement by -S(N) in this short range is covered too.

Consequently the derived sign is

    G(N) = S(N)*(N-B_N) + O_N(Q) + O_{A,theta}(N/log(N)^A).

In particular the operator enters with a plus sign. The decomposition assumes no twisted-distribution conjecture. It isolates the missing long correlation rather than estimating it.

## Squarefree bias and the supplemental sharper margin

The inequality mu(h)<=mu(h)^2 yields the required upper bound for B_N. Truncating the squarefree expansion at N^beta, beta<1/4, gives coprime square moduli within ordinary BV, a tail O(N log N/N^beta), and noncoprime prime-power terms O(N^beta log(N)^2). Its main coefficient is the Euler product A(N). Requesting arbitrarily strong fixed logarithmic saving makes multiplication by S(N)=O(log N) harmless.

The proposal's separate lower bound delta_N>=c/log(N)^2 is valid, and delta_N is not bounded below by a positive absolute constant. The supplement correctly retains S(N) with the gap and proves the sharper bound

    S(N)*delta_N >= c/log N.

To check its uniformity, put y=4log N. PNT gives total prime log mass below y at least 3log N eventually, while prime divisors of N have log mass at most log N. Missing primes below y therefore have total log mass at least y/2 and number at least y/(2log y). If s is the sum of 1/[p(p-1)] over all missing odd primes, then s<=1/2 and delta_N>=1-exp(-s)>=s/2. These missing primes give delta_N>=c/(y log y).

If one of them lies below sqrt y, its single factor gives delta_N>=1/y, and S(N)>=2C2 completes the estimate. If none does, all primes below sqrt y divide N, so Mertens gives S(N)>=c log y. Multiplication by the preceding gap estimate again gives c/y. These cases are exhaustive and use no Goldbach representation.

For primorial N_y, the exact Euler-factor identity in the supplement and Mertens give S(N_y)~exp(gamma)log y. PNT and partial summation give the missing reciprocal-prime-square tail asymptotic 1/(y log y), hence delta_{N_y}~1/(y log y). Since log N_y~y, the product is exp(gamma)/log N_y asymptotically. The order 1/log N is therefore sharp uniformly over even targets, up to its unspecified lower constant.

It follows that a maximal twisted discrepancy bound O(N/log(N)^(2+eta)), eta>0, would suffice: the reviewed Abel lemma pays one log, leaving an operator o(N/log N). This is below the uniform local margin. The weaker exponent 2+eta is a conditional sufficient hypothesis, not an estimate established here.

## Findings and required revision

1. **P1, main objective incomplete.** No estimate for O-open, T-open, T2-open, or the FI bilinear expression is proved. A one-sided bound on one signed combination is logically enough, but it still carries the unresolved pointwise parity correlation. Defining it as a progression discrepancy does not make it an available analytic input. Preserve the explicit conditional status and do not announce a Goldbach breakthrough.
2. **P2, quantitative refinement for the revision.** The frozen proposal's 3+eta discrepancy exponent and its five-log comparison use the coarser separate bound on delta_N. The supported supplement improves the sufficient exponent to 2+eta by proving S(N)delta_N>=c/log N. In the final revision replace the old threshold by this one, and describe the crude O(N log(N)^3) comparison as a four-log gap relative to this guaranteed margin. This is a comparison of available bounds, not a lower bound for the actual size of the operator.
3. **P3, assurance and finite-connection limits.** Keep the decomposition explicitly relative to the imported coefficient lemmas, the proof's fixed theta and rho, and arbitrary-log-saving ordinary BV. Their constants, a numerical local-gap constant, and a finite verification threshold are not extracted. The primorial sharpness is a complete asymptotic argument, but no claim of novel priority follows from it. These limitations affect any announcement or effective all-N closure, not the stated sufficiently-large conditional implication.

No correction to the mathematical derivation is required beyond integrating the supported quantitative supplement and retaining these scope limits. For route 2, the available lower-sieve parameter remains below 2, and FI still requires both distribution beyond 2/3 and its specialized bilinear estimate. The extra uniformity in N for a changing density function remains an explicit additional obligation. No source inspected here proves those conditions for the reflected-prime sequence.

The decisive next step is an actual one-sided estimate for the signed moving-endpoint operator, or another parity-sensitive mechanism giving a proven pointwise lower margin. Further restatement of the condition or finite agreement cannot supply that step.
