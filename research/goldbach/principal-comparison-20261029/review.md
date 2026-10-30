# PRINCIPAL-019 distinct substantive challenge

29 October 2026. Actual Independent Critic for the populated `GOLDBACH-PRINCIPAL-019` challenge stage. I read the frozen author statement and upstream result, the actual accepted CENTERED-018 revision and distinct review, and the BOUNDARY-017 coefficient/comparison interface. No unaccepted RECOMBINE-020 result is used. Usage is unknown.

**Verdict: supported relative to the actual accepted CENTERED-018 theorem and its precisely named classical inputs.** Both candidates are supported: the actual label-independent comparison has the displayed exact square representation, and its central term has coefficient `2 J_eta/9` with the stated error and nonprincipal saving. Its actual fractional comparison consequently has the stated positive lower bound. One P2 coordinate clarification below should be made explicit in the bounded revision; it changes no formula, constant or result.

Assurance is a complete written-argument audit by a distinct host agent, not formal verification, external peer review, or a new audit of the imported published proofs. No mathematical helper, experiment, supplement, new source search, paid inference, publication or external message was performed. The original pointwise prime margin, Goldbach, novelty and substantive-breakthrough classification remain unestablished.

## Reviewed versions

| Input | SHA256 |
| --- | --- |
| frozen PRINCIPAL-019 statement.md | 046701bca199227e1ec4c37e79b8dc911ca1ca0dfc314667c85500bb1bb0510d |
| actual populated challenge packet | 268e6b6812a768960317b554f17fc70a0ca6615a6fa5d704c57ace9ca4e6381d |
| accepted CENTERED-018 revision.md | a45b012cbd701675ce6746f060bedd7777f5075ca8cb96ab3fd903b5d40407d3 |
| distinct CENTERED-018 review.md | 3a014cd1b9f78a36b81b05b9e38076e33807f8bd30080145927e54cf1e44caa2 |

The frozen author and dependencies remain unchanged. The imported all-precision estimate is exactly the accepted k=1, trivial-fixed-twist, arbitrary-real-lambda/common-v estimate for the changed prime arrays on powers of two. The ordinary effective PNT has the theorem-statement assurance recorded there. Neither an administrative completion record nor an unreviewed later claim replaces either input.

## Prioritized finding

**P2, coordinate clarification for the principal/nonprincipal central split.** Target: statement (5), (12), (18) and (24), and the phrase "the nonprincipal part of Q_0." The total character-summed integrand and the residue-square integrand are periodic in phi, but an individual character square in (5) need not be. On changing phi to phi+1, a triple acquires `e(amn/H)`, which varies between residue classes. Therefore the principal/nonprincipal split is defined here using the signed central lift `-Lambda/Y<=phi<=Lambda/Y`, not an arbitrary representative of the wrapped arc in `[0,1)`.

The actual rescaling in (11)-(12) already uses this correct signed lift, so this is no load-bearing defect. The summed integrand is periodic because orthogonality retains only pairs with `amn=brs mod H`; the additional factor is then one. Equivalently, each residue-class amplitude in (7) acquires one common unit phase, so its square is periodic. **Repair:** state explicitly before (11) that the central character decomposition uses this signed lift and that the individual character parts are coordinate-dependent. A direct check is the extra factor `e((amn-brs)/H)` on an individual character's cross terms: it is generally nontrivial before the character sum, and exactly one on the retained residue pairs. This clarification leaves Q_0, its coefficient and the fractional lower bound unchanged.

No other corrective finding is needed. The following proof checks establish the load-bearing claims and their limits.

## Candidate 1: the actual positivity identity

### Support, coefficient ordering and independent-label swap

The actual support has `T^2<=mn,rs<=25T^2/16=25H/96<H`, while every active label is in `(2H/3,5H/6)` and below 4Y. Thus `|bmn-ars|<4HY` on every contributing pair. The real even cutoff is identically one on this entire Cartesian support before it is removed. There is no remaining coupled determinant cutoff.

The original coefficient is exactly `eta(a/Y)eta(b/Y)alpha_m conj(alpha_r)beta_n conj(beta_s)/V_H^2`. Swapping the independently summed labels a and b preserves both this coefficient and all supports, because the arrays are independent of the label. The congruence becomes `amn=brs mod H`, and the phase becomes

`phi*(a(mn/H-1)-b(rs/H-1))`.

All factors are units modulo H. Multiplicative character orthogonality therefore inserts exactly `phi(H)^-1 sum_chi chi(amn)conj(chi(brs))`. Factoring the two finite sums gives precisely statement (5), with one amplitude and its complex conjugate. There is no extra branch Jacobian, factor H, reciprocal label, or changed ordering of the long coefficients. The negative alpha and positive logarithmic beta are retained. Equal labels, equal products and the one ordered representation of a square are all included.

The same finite identity follows by grouping the congruence into its unit residue classes, giving (7) without a residual factor phi(H). In this expression every residue square is itself periodic. The nonnegative pointwise integrand proves `Q_M>=0` for every measurable comparison set and proves monotonicity under set inclusion, with any consistent circle representatives. These are **proved** properties of this actual input class.

This reasoning does not prove positive semidefiniteness of the general label-dependent configuration kernel. A joint cofactor mask would change which label carries a coefficient after the swap; a nonconstant Psi outside the plateau would remain a coupled factor. Neither can be discarded from the square derivation. In particular the argument does not apply directly to an arbitrary fractional-sector vector. The author correctly obtains its later actual fractional bound indirectly from the complete form.

## Candidate 2: central transport, density and exact constant

### Torus arc and exact normalization

For large H, `Lambda/Y<1/2`. Use the signed lift of the central torus arc, of total measure `2Lambda/Y`. With `phi=lambda/Y`, the Jacobian is exactly `dphi=dlambda/Y`. The own-triple amplitude in (5) divided by `Y V_H X` is exactly P_chi in (11). Squaring and combining the Jacobian with the outside `1/(phi(H)V_H^2)` gives

`Q_0=Y X^2*(1/phi(H))*sum_chi integral_[-Lambda,Lambda] |P_chi(lambda)|^2 dlambda`.

This proves (12). The full reciprocal mass V_H remains inside P_chi. The label sum itself is an unweighted prime sum with eta; no reciprocal a is inserted. There is no additional 1/H in this already pulled-back comparison.

The major set contains this central arc as a set of the circle; possible wrapped or overlapping arc descriptions do not duplicate its measure. The elementary cover bound `m_arc<<L^(3A0)/Y` is sufficient for the later integer estimate, and no noncentral-arc asymptotic is used.

### Common-product transform and the retained nonprincipal contribution

On every triple, `q=amn/(YX)` lies in `[2,125/32]` and `X/H=1/6`. Hence its own-triple phase factors exactly as

`e(lambda*q/6)*e(-lambda*a/Y)`.

A fixed cutoff w equal to one on the q support therefore gives the log-Fourier identity (13), with inversion factor `1/(2pi)`, common frequency t in all three factors, and the unit phase `(YX)^(-it)`. It is the actual CENTERED-018 family with v=0 and arbitrary marking lambda. No separate long frequencies or changed twist enter.

The transform has a uniform pointwise bound from its compact support. Repeated integration by parts gives `C_j(1+|lambda|)^j(1+|t|)^(-j)`, and its L1 norm is at most `C(1+|lambda|)^2`. For `R=L^B`, weighted Cauchy bounds the retained normalized nonprincipal square by the actual energy times `O((1+Lambda)^2)`. Integrating over lambda costs a further `O(Lambda)`. The accepted estimate can pay this fixed `L^(3A0)` loss by choosing its requested precision higher. B is a fixed exponent chosen before H grows, so its uniform frequency hypothesis is respected.

### Tail mean preserving 1/H

For every real lambda,t, the exact normalized all-character B mean has only the diagonal a=b: the labels are distinct H-units below H. Thus

`(1/phi(H))*sum_chi |B_chi,lambda(t)|^2 = (Y^2 V_H^2)^-1 sum_a eta(a/Y)^2 << 1/(H V_H^2)`.

Trivially `|M_chi|<<1` and `|N_chi|<<L` at all frequencies. In the Hilbert norm of the normalized character sum, Minkowski therefore bounds the tail by

`C L/(sqrt(H) V_H) * integral_(|t|>R) |Fhat_lambda(t)| dt`.

For `|lambda|<=Lambda`, the last integral is at most `C_j(1+Lambda)^j R^(1-j)`. Since B>A0, its logarithmic exponent is `B-j(B-A0)`, which can be made arbitrarily negative by a fixed j. Squaring and integrating over lambda retains the essential 1/H. Enlarging a nonprincipal sum to all characters in this upper bound is legitimate and introduces no extra factor phi(H).

Combining the retained and tail pieces, and paying the cross term with the elementary square inequality, gives an arbitrarily strong `H^-1 L^-D` bound for the normalized nonprincipal P mean integrated in lambda. Multiplication by `YX^2` then yields `Q_0,np=O_D(HY L^-D)`, as in (18). This is a **proved** transport of the actual accepted theorem on the signed central lift. No other k, fixed twist, arithmetic array or arc is covered by it.

### Effective PNT on the growing lambda interval

At the principal character all supported integers are units. In the actual triple sum, prime a has density `da/log a`, prime m has density `dm/log m`, and the logarithmic beta makes the n density exactly `dn`. After `a=Yu`, `m=Tr`, `n=Ts`, the scale factors cancel the normalization `Y X=Y T^2`. This gives exactly the negative density D_H in (19), including the two denominators `log(Yu)log(Tr)` and the absence of a third logarithm. The continuum phase is `lambda*u*(rs/6-1)`.

The effective ordinary PNT and real partial summation apply separately to each fixed-factor interval. On these scaled supports, the phase has variation `O(1+|lambda|)` in each variable with the others fixed. Smooth eta has fixed variation, and hard long endpoints add bounded jumps. Telescope the three replacements; the remaining normalized true prime masses and density masses are bounded. For `|lambda|<=L^A0`, the variation, possible logarithms and endpoint costs are fixed logarithmic powers or negative powers of T,Y. They are dominated by `exp(-c' sqrt L)`. Consequently (20) holds at every fixed logarithmic precision, uniformly on this entire growing interval. No arithmetic progression PNT, short-interval theorem or target-specific prime-triple asymptotic is hidden here.

Both the actual principal amplitude and its density are `O(1/(V_H L^2))`, by absolute coefficient sums. Therefore a uniform error in (20) can be squared and integrated after paying the interval length, with an arbitrarily small fixed logarithmic error. The outer exact principal prefactor `YX^2/phi(H)` is retained when this error is converted to a comparison error.

### Integrable decay before logarithm expansion

For `r,s in [1,5/4]`, put `kappa=rs/6-1`. It lies in `[-5/6,-71/96]` and is bounded away from zero. Integration by parts in u has no boundary terms because eta is smooth and compactly supported. It proves arbitrary fixed polynomial decay in lambda for A and for D_H, the latter with its full `1/(V_H L^2)` factor. No smoothness of the hard r,s boundaries is needed for this step.

Uniformly on the scaled box,

`L^2/(log(Yu)log(Tr))=2+O(1/L)`.

All fixed positive-order u derivatives of the error are also `O(1/L)`, since `log(Yu)=L+O(1)` and `log(Tr)=L/2+O(1)`. Applying the same u integration by parts to the difference proves the weighted error in (22), rather than an unweighted error that would accumulate over the growing lambda interval. Its square and cross term are integrable. This proves

`integral_R |D_H(lambda)|^2 dlambda = 4 J_eta/(V_H^2 L^4)+O(1/(V_H^2 L^5))`.

For every fixed desired tail precision, increasing the fixed derivative order makes the tails past `Lambda=L^A0` smaller than that precision. This uses A0>0, as assumed. The same fact applies to A, so `J_eta` is finite. It is strictly positive because A is continuous and `A(0)=(integral eta)*delta^2>0`.

It follows that the exact-density comparison representation (24) is valid with an all-precision `O_D(HY L^-D)` error. On powers of two `phi(H)=H/2` exactly, while `X=H/6`; hence

`YX^2/phi(H)=HY/18`.

Multiplying by the density coefficient 4 gives `4/18=2/9`. This verifies the coefficient, normalization and `O(1/L)` relative error in (10). The exact V_H remains visible throughout, so no convergence-rate substitution for that normalizer is needed.

## The actual fractional lower bound and its limits

Every positive integer cofactor on this support is one: an active label exceeds `2H/3`, whereas a positive complement is below H. The protected c=1 sector contains exactly h=1, with no fractional states. Its cross terms with the complement vanish in the original full-pullback kernel. The integer compression equals `m_arc` times the raw h=1 block, giving exactly (26) for the full major set, with the actual restricted fractional input.

For each ordered pair m,n there is at most one possible label `a=H-mn`. Absolute values and PNT give

`|C_1| <= V_H^-1 * #P_I * sum_(n in P_I) log n << H/(V_H L)`.

No lower bound or nonemptiness is asserted. Combining its square with `m_arc<<L^(3A0)/Y` makes the integer major part at most `H^2 L^(3A0-2)/(V_H^2 Y)`. Relative to `HY/(V_H^2 L^4)`, this is `O(L^(3A0+2)/H)=o(1)` because Y=H/3.

Complete-form monotonicity now gives `Q_M1>=Q_0`. Subtracting the negligible integer compression proves precisely the lower bound (28), with coefficient `2J_eta/9+o(1)`, for this actual fractional comparison. This is a **proved** update of the earlier unknown-sign status on this specific input. It does not prove a positive-semidefinite fractional kernel or a full-major asymptotic. The other major arcs are used only through set inclusion.

The central density uses three separate prime sums and has no additive prime-triple constraint. Its positive value therefore cannot establish `C_1!=0` at a prescribed H. In particular the actual boundary equation would require `a/Y=3-mn/(2T^2)` in `[71/32,5/2]`; a smooth eta supported strictly below 71/32 is allowed by the hypotheses and has no boundary configurations at all, while its continuum `J_eta` is still positive. This is a direct support check of the distinction, not an extra estimate for the raw-minus-major remainder.

For every input in this stage, m and n are primes greater than one, so the original Vaughan variable `p=mn` is composite, including a square on the diagonal. No prime-plus-prime Goldbach count is reconstructed here. Neither the positive comparison nor its fractional lower bound estimates `|C_1|^2-Q_M1` sufficiently for an original-target conclusion. Polynomial-sieve Type I, other-k or other-array transport, the pointwise correctly centered rough prime margin, novelty, breakthrough classification and Goldbach remain **unverified**.

The narrowest accepted statement is the actual-input square identity plus the central asymptotic and its actual fractional lower-bound consequence, all at the stated assurance. A next analytic claim must control its own raw-minus-full-major remainder and original-target decomposition without assuming them. No full-goal-completion decision is made in this stage.
