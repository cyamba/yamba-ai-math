# Separate pre-mortem for the reflected-energy interface

29 October 2026. Independent Critic, separately budgeted preparatory dispatch for `GOLDBACH-ENERGY-012`. I read its brief, initial survey and actual statement-stage packet as framing; the survey upstream result was not yet populated. I inspected pinned Guo source lines 1707-2404, including the fiber, Mellin, Perron, sparse Gram and small-conductor arguments. This file is neither an author statement nor a main verdict on that chain. It does not assume that PAIRING-011 has passed its later main review. Ownership is this file only; earlier frozen access records and proof files remain unchanged. Usage is unknown.

## New primary inspection: Iwaniec's exact statement

During this preparation the root supplied the successfully retrieved original volume and rendered journal page 97. I independently viewed that image and checked the hashes:

| Local primary artifact | SHA256 |
| --- | --- |
| `.runs/goldbach-source-inputs-20261029/iwaniec-volume23.pdf` | `d98fe83def66ce90801760710d21f34458637d32de6ac77d726698220ae25832` |
| `.runs/goldbach-source-inputs-20261029/iwaniec-journal97.png` | `88a60c54861c6a83a57e21186f09eeed080e2b487e4a368f9ea6267629648a61` |

The [original Goettingen scan](https://gdz.sub.uni-goettingen.de/download/pdf/PPN356556735_0023/PPN356556735_0023.pdf), PDF page 104, visibly defines q>=3, d=rad(q), ell=log(q*(|t|+3)) and

    theta^(-1)=4*10^4*(log d+(ell*log(2ell))^(3/4)).

Its Theorem 2 allows at most one nonprincipal character modulo q and zero in Re(s)>1-theta; a possible character is real and its zero is real and simple. This is now **primary theorem-statement inspection**, not inspection of the full original proof. The earlier access-limited records describe the earlier attempt and are not silently rewritten.

The small-radical specialization can consequently be checked against that exact input. If rad(H)<=L^C, k<=L^A0 and q*|kH, then rad(q*)<=L^(A0+C). A primitive real character has odd conductor exponents at most one and 2-part at most eight, hence q*<=8*rad(kH). Taking A1>A0+C excludes all such real primitive conductors above L^A1 eventually. At fixed height |t|<=L^C2, ell<=2L eventually, uniformly in the required conductors. Thus the printed theta is bounded below by a constant times L^(-3/4)*(log L)^(-3/4), which strictly dominates C1*log L/L for every fixed C1. The desired closed strip is strictly inside the printed open region, and the possible real exception is outside its large-conductor range. This verifies the selected-strip deduction on the stated small-radical class, including H=2^m, from the inspected classical input. It does not give a general universal zero-free half-plane or generalized RH.

## 1. P1: eliminate class-dependent fiber coefficients before using fixed twists

Reduction from units modulo kH to units modulo H is surjective, also when k and H share primes. The kernel has size phi(kH)/phi(H)=k*product_{p|k,p not dividing H}(1-1/p)<=k. Each character of that kernel extends to the finite ambient unit group. These group facts support the proposed fiber expansion.

The coefficients of that expansion depend on the residue class modulo H. They cannot be treated as fixed coefficients of one global character twist. The indicated Cauchy inequality in the residue-class variable is a valid way to remove them, at a fixed power of k. Only after that step can orthogonality produce energies with a fixed extended twist psi. The two additional additive phases in marking products need their own characters modulo k, so the marking twist psi_2 can differ from the common long-factor twist psi.

The subsequent sparse Gram family must keep psi fixed. Mixing extensions across character-frequency pairs can invalidate its character split: modulo 3, take chi_1 principal and psi_1 quadratic, while chi_2 is quadratic and psi_2 principal. The two products chi_i*psi_i are identical although the chi_i differ. Their Gram entry is principal, not a nonprincipal character sum, and spacing known separately for each chi does not control their combined frequencies. This is a minimal witness to an unsafe mixed-twist argument, not a failure of the correctly fixed-twist route.

Decisive author check: write the classwise Cauchy/Parseval inequalities with all twist indices retained, then run every energy argument separately for each fixed twist and account for their k-power sum.

## 2. P1: the natural Mellin scale and its prefactor must be explicit

The two product variables are bmn and ars, of scale YX. Their normalized values w=bmn/(HY), w'=ars/(HY) lie at scale kappa=X/H, with L^(-B)<=kappa<=1 up to fixed constants. The logarithmic variables of w/kappa and w'/kappa stay in a fixed box. The phase derivatives cost fixed powers of L^A0, not a factor of H/X. This makes the proposed two-variable Fourier/Mellin separation plausible with polylogarithmic frequencies and rapidly decaying tails.

Its cutoff is a two-product kernel and need not be a positive convolution. A correct proof should take its transform, bound the absolute transformed coefficients and apply Cauchy to the resulting two product polynomials. Their two frequencies can differ by the second transform variable. Energy must therefore hold on the enlarged frequency window, or after an explicitly permitted fixed shift; no new arbitrary coefficients may be inserted into the small-conductor Mobius factor.

Each normalized product polynomial has the YMN normalization and the arc displacement has measure d(lambda)/Y. Therefore the comparison scale is YX^2 times the averaged energy, before the fixed logarithmic costs. Energy O(L^(-A)/H) suffices for O(HY L^(-D)) because X<=H, after absorbing those costs. Dropping the 1/Y, using scale X in place of X/H in the transformed smooth kernel, or losing an unrecorded frequency shift would change the conclusion.

Decisive author check: give one exact inverse-transform formula, its two frequency arguments, the tail estimate and the resulting YX^2 prefactor.

## 3. P1: Perron must use the selected large-conductor strip, not a principal or ordinary narrow region

For a primitive nonprincipal inducing character, the proposed contour can work. The selected strip provides horizontal distance at least C1*log L/(2L) from nearby zeros on sigma>=1-C1*log L/(2L), and the local zero count gives a polynomial logarithmic-derivative bound. The contour height must leave room for the twist and the local zero-count neighborhood. Integer or near-integer Perron endpoints require the O(log y) term as well as the usual y*log^2(y)/T error. Imprimitive corrections cost prime powers at primes dividing the modulus; they are O(L^2) and negligible only because y>=H^(1/6).

The long-prime-factor convolution uses endpoint sums with endpoints at least V0=X^(1/5)>=H^(1/6) eventually. Its ratio-two intervals contain at most one power of each fixed prime, so dropping the small-prime and H-unit restrictions costs O(Z+L) per cofactor, then O((Z+L)/V0) after normalization. This preserves short intervals by differencing endpoint bounds rather than demanding a prime theorem relative to their individual lengths.

A principal inducing character has a pole at one and cannot receive this contour cancellation estimate. It belongs in the separate low-conductor Mobius treatment. Also, a conventional width c/log q* at q* comparable to H gives only a fixed exponential factor at these endpoint lengths; it cannot replace the selected C1*log L/L width when arbitrary fixed log savings are required. General H remains conditional on that selected strip. The small-radical deduction above addresses only its specified class.

Decisive author check: retain the pole exclusion, contour margins and endpoint/imprimitive losses before deriving the normalized N-polynomial bound.

## 4. P2: sparse Gram energies have viable margins only at the stated lengths

The proposed short-polynomial power j=floor(L/log(16Y)) has support at most H. Disjoint prime bands imply at most (j!)^K representations of a fixed product, even with repeated primes. Sobolev at one-spaced frequency points and the short residue-class mean value then give the displayed subexponential exceptional-family size. The strict fixed inequality a_K>1/10 is needed to absorb its log L factor into exp(L^0.9); thresholds can depend on the fixed band exponents.

For the sparse Gram argument, same-character entries require the smooth majorant and both integration-by-parts decay and the Euler-summation error. Their row is O(X'*log L+T0^2*tau(kH)). Distinct fixed-twist characters have a nonprincipal quotient; partial summation and the exact imprimitive divisor expansion permit the inspected ordinary Burgess r=2 input or Polya-Vinogradov, with the missing-prime factor retained.

At M>=H^(3/8+eta0), Burgess gives the fixed margin M^(-1/2)*H^(3/16+epsilon)<=H^(-eta0/2+epsilon). For the third M moment polynomial, M^3>=H^(3/5-o(1)) leaves a power over the H^(1/2+o(1)) Polya-Vinogradov cost. In the complementary M case, MN>=H/L^B forces N>=H^(5/8-eta0-o(1)), comfortably above H^(1/2+2eta0) at eta0=1/40. These margins absorb the exceptional-family subexponential factor. The arithmetic M and N roles must remain identified: the energy proof uses mu on M and the long-prime convolution on N, and needs no unsupported swapping of those roles.

Decisive author check: prove the exact Gram bounds, including same-character errors and imprimitive factors, at all three coefficient norms before applying the final Holder step. The stronger Heath-Brown mean-value theorem has extra length/spacing hypotheses; the ordinary r=2 interval bound is the needed imported statement here.

## 5. P2: use the actual MSTT interval statement directly

The root supplied the exact primary statement of published MSTT Lemma 3.9(ii), page 46, from [the journal PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/6DF08E2A3EFABB2DD0DA6CDA38649B18/S2050508623000288a.pdf/div-class-title-higher-uniformity-of-arithmetic-functions-in-short-intervals-i-all-intervals-div.pdf). I use that supplied theorem statement here; I did not independently audit its full contour proof. Its hypotheses include alpha in (0,1], modulus at most log^A X, frequency at most X, and a supremum over subintervals of [X^alpha,2X^alpha], for the coefficient mu(r*ell)/sqrt(ell), 1<=r<=X.

At a dyadic length D0, choose X_*=D0^R_* and alpha=1/R_*, with fixed sufficiently large R_* and r=1. The input then covers the desired local interval directly. Its logarithmic precision can cover both the conductor ceiling and the desired saving. Frequencies up to x^C_t are covered if D0>=x^(delta/2) and R_*>2C_t/delta, with extra margin after convolution. Multiplication by the real sqrt(ell) and partial summation removes the coefficient without differentiating ell^it. The already present supremum over subintervals makes the source's translated-prefix detour unnecessary. Full-dyad estimates alone would not justify arbitrary translated dyadic intervals by a naive binary decomposition of an arithmetic function; use the stronger actual primary hypothesis instead.

The identity mu(n)R_Z(n)=sum_{d|n,P^+(d)<=Z}mu(n/d) is exact prime by prime. For d<=M^(1/2), apply the local estimate at M/d with enough fixed rescaling margin and absorb the smooth reciprocal sum O(log Z). For larger smooth d, Rankin at exponent 1/log Z gives reciprocal tail O(log Z*exp(-c*log M/log Z)); at Z=exp(L^(3/4)) this is exp(-cL^(1/4)) times a polynomial. The count of multiples is O(M/d) even for d near M, so no omitted +1 tail is needed. Removing the H-unit restriction on sifted support costs O(M*omega(H)/Z). All of these claims have concrete elementary reductions; the imported MSTT estimate is the remaining primary theorem input.

The Mobius coefficient is essential. An arbitrary bounded array can align with a fixed character and phase instead of cancelling; a principal positive sifted array also cannot be assigned every log saving merely by relabeling it. For fixed psi, the inducing primitive character determines chi, so the low-conductor character count is polynomial in L. This again relies on holding psi fixed as in item 1.

Decisive author check: state the exact MSTT parameter substitution, interval supremum, real-weight partial summation and smooth-tail bound, and retain the arithmetic coefficient hypothesis.

The preliminary deductions support a viable conditional architecture and now confirm the specific small-radical zero-free input from its original printed statement. They do not prove the forthcoming energy theorem, the complete major-comparison reduction, actual-prime parity or a Goldbach lower bound. A main review must inspect the actual frozen proof, its independent checks and all fixed parameter dependencies.
