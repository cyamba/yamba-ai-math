# Independent review of reflected major energy

29 October 2026. Registry role: Independent Critic, `GOLDBACH-ENERGY-012`. This is the actual main critic stage from the populated counterexample packet. The earlier pre-mortem and primary-access records are separate evidence. Assurance is an independently reconstructed mathematical argument plus distinct host-agent review, using the named classical theorem statements and the explicitly declared completed-L structural background. It is not formal verification, external peer review or an audit of the complete proofs of those imported classical theorems. Usage measurements are unavailable.

## Verdict and frozen inputs

**Supported:** Candidate 1, the complete-pullback comparison reduction with its YX^2 prefactor; Candidate 2's energy proof under the precision-dependent selected strip; and its small-radical specialization obtained from the inspected Iwaniec theorem and real-conductor bound. No mathematical repair was found for these statements in their declared ranges and with the stated classical inputs.

**Conditional for general H:** the selected rectangle (10) remains a hypothesis. One fixed width supplies only the precisions it supports. **On rad(H)<=log^C H for fixed C:** the proof discharges that additional rectangle assumption using the classical input, uniformly for all required conductors dividing kH. This includes powers of two and the extra odd factors of k.

**Incomplete:** the general-H selected strip, source-wide validation, the subsequent marked-prime/decomposition/weight-removal assembly, actual-prime parity as an assembled theorem, the original polynomial-roughness/nonzero-center/h=1 margin, Goldbach and novelty. The present analytic estimates do not establish those consequences on their own.

| Reviewed input | SHA256 |
| --- | --- |
| `statement.md` | `eb76660af2f2ccb2ac003fdf835d2b05c325435d7600ed9e7f98448eb32da80b` |
| `survey.md` | `ad158471547feec91691cd1e69aa8f8c9dea51669e5802a740d197cb02e55653` |
| `primary-inputs.md` | `e3780b37583232cda574301f91a6a439070da27b6aee9e0d7a2c692d8d0b3187` |
| `iwaniec-primary-statement.md` | `4de7ed8accc3a0b548f3511ac922c2987361034c0f0169f87b9764038f3125d6` |
| `source-provenance.json` | `a84d275699993eaaa0afbe20fbedfe4005124c215e6aeabce572a3329c7b486e` |
| Separate `pre-mortem.md` | `89e553b15a8856ca83410c62a8ecf7d185d9b0c28cd4a97b3fcf2d01f786977f` |
| `finite-results.json` | `b29a63fbdbf5a33708d828c61e1a448c3eb2f71f5dfcf05123579abef2468dfc` |

I changed none of these files. I independently viewed the original renders of MSTT page 46, Heath-Brown page 1 and Koukoulopoulos page 111 during this main review; Iwaniec page 97 had been independently viewed in this stage's pre-mortem. Exact local source and render hashes are retained in the frozen provenance. The proof uses the actual arithmetic alpha and beta coefficients, not arbitrary bounded arrays.

## Classwise fibers, fixed twists and the two-frequency reduction

The unit reduction is surjective prime by prime, including primes shared by k and H. Its kernel order is the stated phi ratio. The subgroup-character extension construction is valid: adjoining an element of quotient order d requires a d-th root of its character value at the d-th power, which gives a consistent character on the enlarged subgroup. This does not assume cyclic unit groups.

The representatives in (4) have genuinely class-dependent coefficients. Equation (5) applies Cauchy to them before Parseval and is the correct direction. It keeps each extension fixed independently of the base class. The marking phases have separate characters modulo k; hence the marking twist may differ from the long-factor twist. Cauchy on both product sides, their extension sums and the marking expansions have at most the stated coarse k^4 cost. Every later energy and Gram estimate holds a long twist fixed. The principal/quadratic collision from the pre-mortem would refute a mixed-twist argument, but is excluded here.

The normalized product variables lie in a fixed multiplicative box. Their smooth kernel depends on kappa=X/H, which is at most a fixed constant and has no inverse-power derivative loss. The two-dimensional Fourier formula has independent frequencies s and -t on its two product polynomials. Class Cauchy and 2ab<=a^2+b^2 apply after the transform in absolute value; the proof does not assume positivity or convolution structure of this kernel. The transform marginals have fixed logarithmic bounds, so they reduce the main range to the energy in (2) with fixed log costs.

The product sums have normalization YX and the arc displacement is d(lambda)/Y. Thus (YX)^2/Y=YX^2 is the correct prefactor, with the phi(H) average retained. Arc overlaps are handled by partitioning the union first; enlarging pieces after taking absolute values is legitimate. The number of arcs, extension/marking sums, displacement length and transform bounds have only fixed log-power costs.

For the tails, the three integer factors b,m,n give the pointwise tau_3 coefficient bound regardless of the number K of prime factors inside b, since b has its unique band representation. The inequality tau_3^2<=tau_9 follows prime by prime: every pair of three-part exponent compositions occurs as the row and column sums of a nonnegative three-by-three matrix, and the number of such matrices with total exponent e is the tau_9 coefficient. Summing tau_9 by its divisor representation gives the elementary length-times-log^8 bound. This proves the stated product coefficient norm. Pointwise class Cauchy then gives (9) at all real frequencies, including the low-X/H case through its retained L^B factor. Rapid decay outside the two frequency windows absorbs the tails at every requested fixed precision. This establishes Candidate 1 without assuming an energy estimate or PAIRING-011's difference theorem.

## Elementary means, sparse exceptional values and Gram estimates

Equation (11) follows immediately from orthogonality and at most four terms per unit H-residue. Equation (12) follows from the off-diagonal integral and its harmonic row sum; its extra logarithm is retained later. Equation (13) is the stated disjoint-interval derivative estimate and applies to the selected maxima, however those maxima depend on the coefficients. Splitting alternate intervals gives one-spaced points for each fixed character.

For B^j, disjoint bands give at most (j!)^K representations with repeated primes allowed. The character is evaluated on the product, exactly as required by multiplicativity. Its support lies below H, so the short residue-class estimate and Sobolev bound prove (15). Nonempty Y blocks satisfy log Y bounded above by a constant times L^a_K and below by L^a_K up to a fixed additive term. Therefore log|E|=O(L^(1-a_K)*log L), and fixed a_K>0.1 gives exp(L^0.9) eventually. The exponent gap, not a claim uniform over moving exponents, justifies this threshold. The bulk uses only the MN coefficient-square bound and arbitrary one-spaced samples; it does not require Mobius cancellation.

The Gram estimate (17) is the finite Hilbert duality inequality with a smooth majorant at least one on the coefficient support. Same-character terms retain the unit indicator modulo kH. Its squarefree-divisor expansion, Euler summation and two integrations by parts yield the displayed W*(1+|tau|)^(-2)*log L term plus tau(kH)*(1+|tau|). One-spacing sums the first term to O(W*log L), and the second to O(T0^2*tau(kH)); every relevant W has a fixed positive power of H and absorbs this subpower error.

For distinct base characters the quotient is nonprincipal because the common long twist is fixed. The missing-prime expansion (228) is exact and retains the subpower divisor factor. The inspected ordinary Burgess r=2 statement applies to every primitive nonprincipal modulus; its max-prefix consequence and real partial summation give (18). The stronger Heath-Brown mean-value theorem is not needed. If a prefix exceeds its conductor, complete periods can first be removed, leaving the same sufficient bound.

The three uses have strict power margins. At M>=H^(3/8+eta0), the row ratio is at most H^(-eta0/2+epsilon+o(1))*exp(L^0.9). At W=M^3>=H^(3/5-o(1)) it has a larger margin. At W=N>=H^0.55 it also saves a fixed power. Their coefficient norms are respectively O(1/M), O(L^8/M^3) and O(L^2/N), giving (19). This proof therefore correctly avoids importing a separate Polya-Vinogradov result. It keeps the arithmetic M and N roles throughout.

## Direct MSTT application and small conductors

The original MSTT statement visibly includes the subinterval supremum, arbitrary characters in its modulus range, the factor 1/sqrt(n), and the shared freely chosen precision/modulus exponent. With W_*=D0^R_* and alpha=1/R_*, its local interval is exactly [D0,2D0]. Taking r=1 is allowed. The stated fixed R_* covers |u|<=H^C_t at D0>=H^(1/12), and a larger input precision covers both the conductor ceiling and the desired saving because log W_* is comparable to L.

Partial summation against the real sqrt(n) costs O(sqrt(D0)); it does not differentiate the oscillatory n^iu. Thus (20) is valid directly for every required subinterval, without the earlier unsupported full-dyad-to-translated-interval inference. In the actual smooth convolution, M>=H^(1/6) eventually and d<=sqrt(M) leaves M/d>=H^(1/12), exactly its domain.

The identity (275) is true prime by prime with all smooth powers retained. The small-d reciprocal sum is O(log Z). At larger d, the count is O(M/d), including d near 2M, so the Rankin reciprocal tail has no missing endpoint term. The Euler product at exponent 1-1/log Z is at most a constant times log Z: its change from the Mertens product is bounded by (1/log Z)*sum_{p<=Z}(log p)/p=O(1). This proves the displayed exponential decay. Removing the H-unit indicator loses O(M*omega(H)/Z). On the original sifted unit support the imprimitive character agrees with its primitive inducer, since every k prime is below Z. These observations prove (21), including the principal inducer by the actual Mobius input.

For fixed psi the small primitive inducer determines chi, by surjectivity of the unit reduction. Counting conductors gives at most L^(2A1) such characters. The ordinary BN mean value retains the extra logarithm and gives O_K(L^6). The freely chosen small-conductor precision absorbs this count and H/phi(H). No principal zero-free or arbitrary-coefficient cancellation assertion is hidden in this branch.

## Local zero count, logarithmic derivative and Perron

The proof explicitly declares order/growth and Hadamard factorization of the completed primitive L-function as classical structural background. The inspected book theorem supplies the correct entire nonprincipal continuation and functional equation with the conjugate character at 1-s. These are standard inputs, not a full reconstruction of their published proofs. The following deductions are valid relative to that declared background.

In a fixed disk around 2+it, the Euler product bounds L at its center above and below. Functional equation, Stirling and polynomial growth in a fixed strip bound the maximum-to-center ratio of the completed function by exp(O(log(q*(|t|+3)))); the common gamma exponential cancels in that ratio. Jensen then bounds zeros in a smaller fixed disk, including the strip segment with vertical distance at most one. This proves the local zero count uniformly in conductor and height, without using a zero-free assumption.

Subtracting the Hadamard logarithmic derivatives at s and 2+it cancels the constant and genus correction. For zeros farther than one vertically, the difference has inverse-square decay; summing the local counts in successive height strips gives O(log(q*(|t|+3))). Nearby center terms and the gamma-factor difference have that same cost. This yields (22) for the stated strip. Thus the selected zero-free assumption is used only at the subsequent horizontal-separation step, not smuggled into Jensen.

For the Perron rectangle, C2 leaves room for t+v and for the unit-height local count. Every nearby zero is horizontally separated by C1*log L/(2L), and q*<=H*L^A0 gives the stated O(L^2) logarithmic-derivative bound. The inducer is nonprincipal, so there is no pole at one. These hypotheses cover the vertical and horizontal segments.

The half-integer cutpoint argument justifies the endpoint-uniform truncation. One can choose a cutpoint with the same integer sum within bounded distance of y; all such endpoints remain at the same large scale. Here y>=H^(1/6) and T is a fixed log power, so y is much larger than T^2 eventually. Any bounded cutpoint adjustment in the truncated integral is absorbed by the displayed y*L^2/T error. Near the cutpoint the harmonic estimate with Lambda(n)<=log n gives y*L^2/T plus the individual O(log y) endpoint cost; the far tail uses the stated absolutely convergent series. Integer and nearly integer y therefore do not invalidate (23).

The selected strip permits the contour shift to sigma0, with no zero pole. Its vertical integral gives y^(sigma0)*L^3 and the horizontals O(y*L^2/T). The lower bound log y>=L/6 gives the precise C1/12 saving. Passing to an imprimitive character changes only powers of missing primes and costs O(L^2), negligible on this endpoint range. This proves (24).

The actual N coefficient has the exact divisor convolution (25). Its inner intervals are ratio at most two, with endpoints at least V0 and at most 2N<=H eventually. Removing the small-prime and H-unit factors costs O(Z+L), because at most one power of each prime occurs in such an interval. After normalization the total loss is O((Z+L)/V0), negligible since V0>=H^(1/6). Differencing endpoint estimates, then summing the harmonic cofactors, proves (26) even for arbitrarily short supported intervals. No relative prime theorem at those short lengths is claimed.

## Energy assembly, constants and small radicals

The complement of E is covered by (16). On the large-conductor part of E, (26) and (19) give the first-case bound immediately. In the other case M<H^(3/8+eta0), the product lower bound forces N>=H^(5/8-eta0)/L^B and hence the long-N regime. Holder with exponents 3 and 3/2 gives (27), with the displayed L^6 reserve more than sufficient. Dividing by phi(H) costs O(log L/H). The proposed A_s and D_N therefore leave strict margins for (2). Both sparse families and small conductors are included.

The parameter order is noncircular. The operator/arc data and required energy precision are fixed before A_s,D_N and then C1,C2. The transform's frequency scale does not depend on the zero-free constants. The free MSTT precision is chosen afterwards. The proof expressly makes the general-H conclusion conditional on the resulting selected strip, rather than deriving all precisions from one fixed width.

For the small-radical class, the original Iwaniec page has exactly the transcribed 3/4 width and possible real-character exception. Every required q* dividing kH has radical at most L^(A0+C), size at most H*L^A0 and ell<=2L at the fixed height. The resulting width strictly dominates C1*log L/L. An odd-prime real primitive character factors modulo that prime because the higher kernel has odd order; at two it factors through eight. Thus a real primitive conductor is at most eight times its radical. Choosing A1>A0+C excludes every possible real primitive exception above the cutoff eventually. The desired closed rectangle lies strictly inside Iwaniec's open region. Conductors one and two stay in the MSTT branch. This checks every q* dividing kH, including extra k primes, and proves the claimed small-radical specialization from the named classical inputs.

## Finite evidence and remaining integration conditions

I inspected the experimenter's completed exact results. They cover unit reductions and extensions, fiber reconstruction and Cauchy/Parseval identities, scalar prefactor examples, smooth convolution, discrete real-weight summation and repeated-prime coefficient bounds. The rational-arc numerator coverage is only one, and the sampled product prefactors use Gaussian coefficients and multiplicative toy phases. These checks do not evaluate the actual arithmetic energy, the continuous transform, zero-free regions, local zeros, Perron, Gram asymptotics or the final energy. I did not rerun them or treat their agreement as analytic proof.

No repair is required for the frozen candidates. Preserve three findings in integration:

1. **P1, general-H status and precision.** The general energy remains conditional on its explicitly selected large-conductor rectangle. The small-radical classical deduction has the stated fixed-C scope and cannot be promoted to every H. One fixed width supplies only its permitted precisions.
2. **P2, fixed twists and arithmetic inputs.** Classwise Cauchy must precede Parseval, each sparse family fixes psi, and the principal/small-conductor branch uses the actual sifted Mobius coefficients. Keep the MSTT interval supremum, real-weight conversion, endpoint errors, exact YX^2 normalization and the declared completed-L structural background. The formal threshold here is V0=X^(1/5). A Vaughan rectangle can instead inherit V0=y^(1/5) with X only comparable to y. The proof appears stable under that fixed-factor change, but a later application must explicitly derive the comparable-threshold extension from its uses of beta<=log n, V0 comparable to X^(1/5), endpoints above H^(1/6) and the negligible (Z+L)/V0 cost. This review does not silently enlarge the frozen theorem's exact threshold. Removing any of these conditions would change the proof rather than merely simplify notation.
3. **P1, assembled prime and Goldbach consequences remain separate.** The accepted analytic result estimates the specified comparison and energy. Decomposition/Type-I, marked-prime assembly, weight removal and logarithmic unweighting must use their actual reviewed scopes before an actual-prime theorem is recorded. Even that correlation does not isolate prime complements or prove the original Goldbach lower margin. Closest-prior and novelty review also remain separate.

The conditional energy chain and its classical small-radical specialization pass this review. There is no first load-bearing failure within the declared proof; the first unresolved steps toward the user's full goal are the remaining assembly interfaces and the distinct prime-complement margin.
