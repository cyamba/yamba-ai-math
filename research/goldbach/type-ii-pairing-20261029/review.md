# Independent review of the reflected Type-II difference

29 October 2026. Registry role: Independent Critic, `GOLDBACH-PAIRING-011`. This is the actual main critic stage from the populated counterexample packet. The separate pre-mortem is preparatory evidence, not an earlier acceptance. Assurance is a complete mathematical derivation checked by a distinct host agent, with the previously reviewed MOMENTS-010 and ROOTS-008 dependencies. It is not formal verification, external peer review or validation of a full source theorem. Usage measurements are unavailable.

## Verdict and frozen inputs

**Supported:** Candidate 1, including the positive selected-divisor expansion, signed nonnegative square, coprime determinant equivalence and both absolute/shared overlap estimates; and Candidate 2, the stated xY*L^(-A) bound for Q_all-Q_maj with its explicitly defined complete-pullback comparison. I found no mathematical repair required in these declared domains.

**Incomplete:** a bound for Q_maj itself, its major-energy and character-sum analysis, the remaining decomposition/Type-I/weight-removal interfaces, actual-prime parity and the original polynomial-roughness/nonzero-center/h=1 Goldbach bridge. Neither a Goldbach lower bound nor novelty is established. The difference estimate is not an estimate of either quadratic term separately.

| Reviewed input | SHA256 |
| --- | --- |
| PAIRING-011 `statement.md` | `f93c024abd19699640e90bb5680306432c2bb71600acd77a0b66024a6658645b` |
| PAIRING-011 `survey.md` | `8b787c7854cc46b2511e8e2248b2ace7e394916d591ab67da9a6e5265838d76e` |
| PAIRING-011 separate `pre-mortem.md` | `4e45236b361122a3b062745b9539bf2bf79087a9fe3c3178f126de3a11210eb0` |
| Accepted MOMENTS-010 `revision.md` | `947cc0c9b1fbcb79b9f221246bbc2ecf056dcdd9decf0543b508a3b7ee2931ba` |
| MOMENTS-010 `review.md` | `aedcb031465999ed34dfbee97e50f9f76d3bdb775e83b6bc6bb529acdb229d91` |
| PAIRING-011 `finite-results.json` | `b358e3882f0d5b13d807e0acac1424fd5743424e82084d482f99de4a8fa89981` |

I changed none of these inputs. The pinned Guo source and [Lue-Wang-Wu Sections 4.6-4.7](https://arxiv.org/html/2610.20242v1#S4.SS6) were inspected for the relevant support, localization and reassembly interfaces. Their full transport conclusion is not an assumed theorem. Classical zero-free results are not needed for this difference estimate.

## Positive support, cofactor integrality and raw overlap

For a squarefree positive w, selecting one eligible divisor in each group gives the stated Mobius sign and rho factor. For nonsquarefree w, every term retaining (a,h)=1 has a square remaining in h and hence vanishes, so the restricted expansion remains exact. Removing that restriction creates only selected p with p^2|w. The pointwise majorization (65) bounds the sum of their absolute selected weights by the bounded W(w); it is therefore legitimate to use a count of bad pairs rather than count selected tuples again.

Every band p is below Z while m is Z-rough, so m is invertible modulo p^2. The condition p^2|H-mn is one residue of n. Since p^2=x^o(1)<N, its endpoint error is absorbed in O(N/p^2). Summing primes gives the claimed O(x*L^(2C)/p_min) expansion error, also after the bounded eta cutoff. Only positive w occurs in this argument. Cauchy then uses h>=1 and h<=H/Y; adding negative-h squares is nonnegative enlargement. Unit support excludes h=0. No Mobius function at a negative integer and no joint positive-product mask enters the signed operator.

Expanding the enlarged square gives exactly (4). Reducing b(H-mn)=a(H-rs) modulo a,b proves the reverse implication from (5) only when gcd(a,b)=1. The displayed H=2,a=b=3,m=n=r=s=1 witness has determinant equality and noninteger quotient 1/3, correctly refuting the stronger shared-prime assertion. Shared raw terms are bounded from their actual integer-cofactor definition throughout.

The progression estimate (6) is valid uniformly in H's residue. The inequality tau(k)^2<=tau_4(k) and deletion of a largest factor dominate its sum by the displayed tau_3 divisor sum. Only divisors d coprime to a contribute because gcd(a,H)=1. CRT counts k with error O(1); the resulting x^(3/4)*L^2 error is dominated by (x/a)*L^3 uniformly over selected subpolynomial a. Cauchy over the common integer h then gives (7), using only positive product arguments k,l<=4x. This improves on a full cofactor-interval enlargement: even when H/x is logarithmic, the count retains scale x and has no unnecessary H/x factor.

The number of selected product pairs is at most the number of integer pairs in [Y,4Y]. Shared primes cost O(Y^2*sum_{p>=p_min}p^(-2)); for an admitted p the individual multiple count is O(Y/p), including its endpoint. Unique product representation prevents an extra band-tuple multiplicity. The coefficient bound, fixed normalizers and the preceding Cauchy estimate give (8).

## Complete-pullback comparison and its absolute bounds

The H inverse branches each have Jacobian 1/H. Their root-of-unity sum cancels all branches unless H divides t, and otherwise cancels that Jacobian. This gives (1), with no residual factor 1/H. In particular the comparison retains the exact congruence used by the lattice construction and primitivity proof.

For each a,b, the comparison congruence determines l modulo H when k is fixed because a is a unit modulo H. There are O(1) l in its allowed range and conversely O(1) k. The positive product supports lie below 4x and H>=x; this degree bound can also be seen directly from their length, independently of enlarging the cutoff interval. Applying 2*tau(k)*tau(l)<=tau(k)^2+tau(l)^2 and the ordinary divisor-square sum gives the claimed O(x*L^3) count. Multiplication by the comparison arc size and the same pair counts proves (9). It applies separately to shared a,b without assigning them false quotient integrality.

The cutoffs now satisfy the exact identification requirements from the pre-mortem. Eta is real and nonnegative. Psi is real, even and one on [-4,4]; the raw value (b-a)/Y is in [-3,3]. Thus the common raw cutoff does not alter Q_all. The comparison need not be nonnegative; all overlap/removal bounds use its absolute value.

## Accepted moment scope and endpoint identification

The MOMENTS-010 revision explicitly repairs the unequal-state-space normalizer issue. This proof uses eligible groups at every ambient intermediate state from the outset and makes no full-band versus eligible ambient-power equality. Both coefficient arrays have the stipulated symmetric support, sifting and bound hypotheses, so they may be exchanged before the construction to orient M<=N. The scalar quadratic forms are unchanged by that exchange. This does not assert that arbitrary later analytic roles may be swapped.

The extension to x<=H<=x*L^B is justified by the checks in line 164. Eligibility still loses only exponentially small reciprocal mass. ROOTS-008 is uniform for polynomial H; its actual restricted aspect saving holds with U=d0YM,V=N after orientation. Relative heights are O(1+UV/H)=O(d0Y), and the H/(UV) coefficient is always multiplied by a bounded contributing z2. The accepted boundary partition and prescribed-modulus budgets therefore remain subpolynomial with the same fixed-power discrepancy margin. There is no missing positive H power in (11). The slightly larger H range changes fixed thresholds and logarithmic constants, not the moment's proof mechanism.

The endpoint coefficient f has the correct alpha conjugation for an inner product conjugate-linear in its first entry. Equation (12) follows exactly. Since the long variables are Z-rough and every band prime lies below Z, the complete band part of Dbm is exactly Db. Thus f is independent of the ordering of its full active lists, and its damping exponent is zero. Its H-unit support follows from that of the long coefficients and eligible band products.

Comparison endpoints are primitive for the same reason as raw endpoints. A common prime ell of Dbm and s exceeds Z, avoids Db and H, and divides t. The disjointness of a,b and the sifting give gcd(b,a*r*s)=1, so b>1 forces t!=0. Both kernels give H|t and |t/H|<=C_psi*Y<Z. Thus ell would divide a smaller nonzero integer. Reversing the roles proves the other endpoint case. This proof is independent of the sign of the common cofactor and of the sign of t.

For fixed ordered full list product G, its available positions are O(UV/G). The quotient support is at least M, so the endpoint rounding term is absorbed uniformly. Dropping distinctness into the positive product harmonic sum gives the exact norm bound (13); no logarithmic exponent depending on K or J is introduced. The list state weight and the fresh-edge factor are distinct and correctly counted once each.

## H blocks, cells and the ambient Gram estimate

Unit endpoints share a sector exactly when H divides their determinant. The cutoff gives the stated real-slope locality, with only a bounded number of neighboring cells in each sector. Choose a primitive point in an occupied labelled lattice. Determinants with other points are multiples of H of magnitude O(UV). For a fixed determinant the difference of solutions is an integer multiple of that lattice-primitive point; the positive first-coordinate interval permits O(1) shifts. Hence there are O(1+UV/H)=O(d0Y) endpoints per block and per cell. Counting unrestricted integer determinants instead would have lost an H factor; the proof does not do that.

The restricted coefficient-space matrix formed from the ambient positive power is positive semidefinite. Its diagonal sum bounds its largest eigenvalue without normalizing u_P. Cell occupancy then bounds the coefficient norm by C*d0Y*sup|f|^2. Spectral Holder is applied in the ambient space, followed by Holder over the localized endpoint vectors; their supports are disjoint and their neighbor supports have bounded overlap. Every selected root enters the diagonal sum once, so it is at most D_unit. No number-of-sectors factor and no full trace is inserted.

Substituting the actual Hilbert norm and (11) yields (14), with the explicit (d0Y)^(1/(2R)) factor. Its logarithm is O_K(L^(0.21-0.5)), so it is bounded. This is a valid endpoint Gram argument, not the false pointwise deletion of intermediate unit or domain projections from powers.

## The separate positive bad-edge replacement

The bad-state argument does not use a signed high moment as a positive absolute estimate. First bound the endpoint coefficients by their suprema. In this nonnegative upper bound one may drop their remaining quotient support and the target's unit/plane-primitivity restrictions, keeping a unit primitive source root and a primitive target in its ambient lattice. Dropping physical damping also enlarges the form because every admissible active list has at least Km band primes at its position and the damping is at most one. This explains why no uncontrolled arithmetic cutoff from an arbitrary coefficient array enters the replacement.

A single edge then has exactly J+2 distinct eligible primes per group in its list union. Its finite relative target/prime choices have exp(o(L)) size and prescribed modulus log S=O_K(L^0.21). Absolute raw and comparison kernel coefficients depend on the integer relative data, not the real root coordinates. The remaining box and intrinsic source-bad conditions have precisely the controlled boundaries from MOMENTS-010. Applying ROOTS-008 on those cells therefore gives a normalized power error, stronger than any fixed L^(-D). No memory cap or high-moment Bonferroni expansion is needed after this positive damping bound.

In the independent model the line probability and list normalization sum to at most one as in (257). For each fixed source list the bad-ratio measure is exponentially small. The uniform target count is O(1) for the raw reduced determinant and O(Y) for the comparison reduced determinant, with comparison multiplier O(L^(3A0)/Y). This count may depend on the ratio, but its uniform bound permits integration over the bad set without assuming independence from it. Reversing the symmetric joint edge gives the same argument for a bad target. With the coefficient suprema this proves (15), including the needed positive row/column counts, as a separate arithmetic lemma.

## Exact shared-list reassembly and precision

The outside list averages disappear in <f,K0*f> because f is list-order invariant. The inner-product state normalization is product V_i^(-(J+1)); the one-edge fresh selections contribute another product V_i^(-1). After division by d0 the geometric factor is 1/D. Equation (16) is therefore exact.

The J shared slots in each group are ordered harmonic draws of total mass one. All dyadic D blocks partition their product exactly once. For fixed coprime a,b, the actual kernel enforces only their collision avoidance, the endpoint coefficient support and the automatic primitivity already proved. Thus summing those ordered draws gives exactly w(a,b) in (17), with no extra J!, J+1 or per-block unit mass assumption. Complete-list permutations and the distinguished unshared last entry are already accounted for by the ordered state space and invariant endpoint vector.

A union bound for repeated shared slots and the two forbidden endpoint primes gives (18). Its loss is exponentially small compared with every fixed logarithmic precision. Equations (8)-(9) justify replacing w by one in absolute value and independently restoring shared a,b with their actual raw cofactor conditions. The number of dyadic D blocks is O_K(L); each block has pairing scale UV=d0Yx, so division by d0 leaves xY. The specified precision order E>A+4C+3, D>A+3, then moment and operator parameters, absorbs that dyadic sum and all fixed cutoff factors. This proves (10).

## Finite coverage and integration findings

I inspected the independent experimenter's actual completed result. Its reported bounded exact checks cover signed squares and Cauchy, integer cofactor/equivalence and conjugation identities, branch normalization and comparison degrees, limited geometry, and scalar ordered harmonic/factorial accounting. Its geometric sample contains only 25 endpoint pairs and maximum cell distance zero. Some toy complete J=2 padding masses vanish; separate per-group factorial cases are nonzero. The full physical kernel identity (17), localization asymptotics, primitivity at large Z, positive one-edge replacement and Type-II estimate are explicitly outside its coverage. Those computations are useful finite evidence, not proofs of the asymptotic claims above. I did not rerun them or broaden their stated coverage.

No repair is required for the frozen main claims. Preserve three scope conditions in the revision:

1. **P1, difference versus major term.** The accepted conclusion is (10) for the specified comparison. Its first remaining analytic obligation is a bound for Q_maj with the actual coefficient arrays and every character/Mellin normalization. Nothing here estimates it, establishes actual-prime parity or proves Goldbach.
2. **P2, keep the positive one-edge argument and common eligible space explicit.** Its safe support enlargements occur only after taking a nonnegative absolute upper bound. They do not authorize arbitrary entrywise restrictions of a signed operator or replacement of projected powers by ambient diagonal powers. Retain the corrected MOMENTS-010 scope, original-box boundaries and selected-root endpoint closure.
3. **P2, exact support and ordered weights are essential.** Preserve the real eta, psi plateau, unit support, coprime determinant equivalence, shared raw cofactor conditions, 1/D and V_i powers, and all ordered tuple factors. The existing shared-prime, zero-cofactor, conjugation and factorial witnesses show that these are load-bearing hypotheses, not optional presentation choices.

The specified Type-II raw-minus-comparison bound passes this substantive review. Its closest source framing is already known, novelty remains unverified, and the user's full Goldbach objective remains open.
