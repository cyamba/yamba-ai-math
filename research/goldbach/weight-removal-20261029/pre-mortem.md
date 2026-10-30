# Separate pre-mortem: prime-relative weights and assembly

29 October 2026. Independent Critic, separately budgeted preparatory and closest-work preview for `GOLDBACH-WEIGHTS-014`. I read the brief, initial survey and actual statement-stage packet as framing, pinned Guo source lines 3109-3250 and 3436-3512, its introductory reflected/small-radical statements, and LWW Proposition 2.3. This is not the main author or critic stage, and it accepts no forthcoming weight theorem or actual-prime consequence. Only this file is owned. Usage measurements are unavailable.

## Primary prime-BV input

The root supplied the author-provided preliminary book and rendered printed page 277. I independently viewed the render. [Koukoulopoulos, *The Distribution of Prime Numbers*](https://www.dms.umontreal.ca/~koukoulo/documents/publications/primes.pdf), equation (26.1), is a **counting-prime** statement: for fixed A>=0 its endpoint-maximum reduced-class error sum is O_A(x/log^(A+1)x), uniformly for Q<=sqrt(x)/log^(A+3)x. Real partial summation gives the logarithmic prime weights with one fixed log loss; larger fixed precision absorbs it. Differences of interval endpoints are covered.

The local PDF SHA256 is `1445e107bba9c89db6529aeb4bca3ecf01170fc2854a675f5ca6f288c77ea0a8`; the page-render SHA256 recorded in `source-provenance.json` is `e47e69dc9951f29297de3d98d08fb9cacb2e93182553007100838c91f6831cac`. This is exact primary statement inspection, not audit of the book's entire proof. The author-provided preliminary PDF is an unchanged ignored reading input; it is not republished here.

## 1. P1: the local population is the reduced prime residues

At an eligible divisor prime r avoiding H, the condition r|(H-p) requires one reduced prime residue p=H modulo r. Its prime-relative probability is therefore 1/(r-1). Distinct eligible primes give independent reduced-residue conditions by CRT. Neither the integer-divisor probability 1/r nor the root-line probability 1/(r+1) describes this measure.

A finite witness is r=3,H=2. Exactly one of the two reduced residues modulo 3 gives divisibility, so the probability is 1/2. The integer probability would be 1/3 and the root-line probability 1/4. With a single-prime normalizer V=1/3, the weight is three times that indicator, so these populations give means 3/2, 1 and 3/4 respectively. The correct normalizing mean cannot be inferred from the harmonic V alone.

For independent Bernoulli variables with probabilities pi_r=1/(r-1), the exact identity

    E[u*rho^(u-1)]
      =sum_r pi_r * product_{q!=r}(1-(1-rho)*pi_q)

gives the displayed m_j. The eligible band sums of pi_r are log 2+o(1), the difference from their V_i is bounded by a negligible squared-reciprocal sum, and sum pi_r^2=o(1). Each single-band mean consequently tends to 2^(rho-1), giving m_j=2^(K(rho-1))+o(1). For every fixed finite array the means are eventually bounded below by a common positive constant depending only on K,rho. All b copies can be treated at once after a threshold depending on that fixed array.

Decisive author check: derive the mean from the reduced prime-residue model and retain m_j itself when normalizing, rather than substituting the root density or silently treating V_i as the mean.

## 2. P1: pass finite positive remainders to actual primes

The relevant first and mixed moments use only one or two weight copies. In each band, retain the finite Taylor divisor expansion and its positive omitted-order divisor majorant. The reciprocal remainder estimate must use 1/phi(d), not only 1/d; the former works because the band sum of 1/(r-1) tends to log 2<1. Products of bands remain disjoint. Telescoping errors can therefore be dominated by finite positive divisor sums whose reciprocal masses have factorial decay and whose other absolute reciprocal factors are bounded.

With truncation depth O_A(log L), each retained squarefree d is subpolynomial. Its factorization into bands uniquely identifies the coefficient, whose magnitude is a fixed power of log L. All d avoid H, so p=H modulo d is reduced. The primary prime-BV input at global scale H, with a larger fixed precision, can then control the retained coefficients and positive remainders, uniformly in both interval endpoints. There is no prime theorem at the product of an entire band or at the product of all b copies.

The actual remainder passage needs its coefficient and endpoint accounting. An average factorial bound in an abstract local model alone does not prove an arithmetic remainder. Its finite positive expansion must also be summed using BV, or an explicit integer count including all +1 terms. If the proof chooses the quoted counting-prime input and real partial summation directly, no conversion from all von Mangoldt powers is required. If it chooses a von Mangoldt formulation instead, higher prime powers and their finite coefficient sums need a separate O(H^(1/2+o(1))) bound. The few primes dividing H have total logarithmic mass O(L^2) before the finite subpolynomial coefficient sums.

Replacing an interval-length main term by the actual Theta(I) uses an endpoint-uniform PNT estimate at scale H. The final errors are absolute O_A(H*L^(-A)); for arbitrarily thin intervals this is not automatically relative to Theta(I). The requested variance with an o_b(H) error is compatible with that limitation.

Decisive author check: write the first/mixed finite divisor sums and their positive remainder bounds, with moduli and coefficient maxima, before invoking prime BV. Keep the proof to at most two copies per analytic moment.

## 3. P1: the leading variance constant must not depend on b

The pointwise bound W_j<=C_(K,rho) follows from the bounded function u*rho^(u-1), eligible V_i bounded below and fixed K. After the fixed-array threshold, m_j has a lower bound independent of b. Thus X_j=W_j/m_j is bounded by a single C_(K,rho), and X_j^2<=C_(K,rho)*X_j. This gives the required diagonal control without a separate same-copy Taylor expansion involving repeated primes.

Disjoint bands give the exact local mixed mean one for X_j*X_k when j!=k. Actual-prime first and mixed moments then yield, after expansion of the square,

    sum_{p in I} log p * |b^(-1)sum_j X_j(H-p)-1|^2
       <= C_(K,rho)*Theta(I)/b + o_b(H).

The leading C is independent of b; the finite sum of analytic error terms and the threshold may depend on b and its band array. Cauchy must use this same positive prime measure. For a bounded target it gives O(H/sqrt(b))+o_b(H), with the target bound retained. It is invalid to mix a variance on the prime measure with an unproved variance on integer or root points.

The order of limits is essential. For each fixed b, prove the marked normalized correlation tends to zero as H tends to infinity. Then the unmarked limsup is at most C/sqrt(b), and b may tend to infinity afterwards. Pointwise fixed-b errors need not decay for an arbitrary growing b(H): the abstract array e_b(H)=1_{H<=exp(exp(b))} tends to zero for every fixed b, but is one at b(H)=ceil(log log H). This is a concrete falsifier of an automatic growing-family inference. The pinned source's later explicit-rate section proposes extra uniformity and packing; that separate argument is outside the present fixed-b target.

Decisive author check: state a common leading constant, finite-array thresholds and the successive epsilon argument. Do not deduce a log-log rate merely by substituting b=b(H).

## 4. P1: assemble only accepted marked estimates, then remove the prime logarithm safely

The marked-prime cancellation needs the exact Vaughan/Type-I and endpoint rectangle interfaces, the Type-II difference, the actual-coefficient major-energy estimate, dyadic and Mellin losses, cofactor Cauchy scale and both prime-power corrections. A statement packet or a source claim is not acceptance of those dependencies. At this preparation, ENERGY-012 and TYPEI-013 have not received their actual main reviews. The actual accepted revisions and their restrictions must be checked before an unconditional assembled consequence is asserted.

General even H needs exactly the selected strip used in the energy estimate. The independently inspected Iwaniec input can supply that selected strip on rad(H)<=log^C H after the full deduction and energy proof have passed review. That does not extend the small-radical scope to all even H, prove a universal half-plane or remove another unaccepted analytic interface. Powers of two are a subclass, not a proxy for the entire conjecture.

There is a safe short route for final logarithmic unweighting once the full-range bounded-target logarithmic sum is o(H). For |f_H(p)|<=1 and fixed B>2, split at H/L^B. Above that point log p/log H=1+O_B(log L/L), and Chebyshev bounds the number of primes by O(H/L). Below it, bound each sum by O(H/L^B). Thus

    sum_{p<H} f_H(p)
      =(1/L)*sum_{p<H} f_H(p)*log p
         +O_B(H*log L/L^2+H/L^B).

This proves little-o of pi(H) without assuming prefix cancellation for the changing target f_H. Real partial summation is also valid if the proof has the necessary endpoint-uniform estimates for that same fixed H; a theorem only about its terminal sum is not automatically such a prefix estimate. The displayed bounded comparison avoids adding that assumption. Earlier endpoint-uniform bounds are still needed where actually used in decomposition and prime moments.

Decisive author check: give the marked dependency ledger, parameter order and either this bounded-target unweighting or a genuinely endpoint-uniform partial-summation argument.

## 5. P1: closest prior work and the actual Goldbach boundary

The pinned [Guo source](https://github.com/aster2024/openai-math-followups/blob/a605351dce1a55fb46a494d9cca9b0baa8f2734b/mobius-goldbach-shift/source/main.tex), SHA256 `e70d777424852aed92e94b2baf00384c84b4c7fc346bd7dab1085d5652ced95d`, already states the same reflected prime Mobius cancellation under H2' plus a selected strip in Theorem G, and on the small-radical class under H2' with Iwaniec and Burgess in Theorem S. Its positive prime-relative moments, normalized fixed-b variance, successive limits and labelled determinant-H/ambient-Gram architecture are explicit. LWW Proposition 2.3 explicitly fixes b,K and all band exponents before its limit.

Consequently the current work must distinguish checking previously conditional operator and analytic arguments from proving a new conclusion not found in the closest source. A complete independently audited removal of a stated hypothesis could be substantive progress, but novelty and breakthrough classification require that exact comparison and the complete proof. The conditional source conclusion cannot itself certify the missing argument. No full paper or source-wide theorem is validated by this preview.

Even an accepted actual-prime correlation is distinct from Goldbach. For example, at even H=206, the prime p=101 has H-p=105=3*5*7 and mu(H-p)=-1, although its complement is composite. Balanced Mobius signs do not isolate one-prime complements. The original polynomial-roughness margin, nonzero centers and h=1 boundary remain separate. This stage must not replace the user's Goldbach objective by a weaker sign theorem or label it solved.

Decisive author check: state the actual correlation with its exact dependencies and scope, then record a closest-work comparison before any novelty or breakthrough claim. A main verdict remains reserved for the frozen author statement and populated critic packet.
