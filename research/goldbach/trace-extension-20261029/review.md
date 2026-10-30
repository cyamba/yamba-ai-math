# Independent review of trace compression and enlarged roots

29 October 2026. Registry role: Independent Critic, `GOLDBACH-TRACE-009`. This is the actual critic stage from the populated counterexample packet. The separate pre-mortem preceded the author statement and is not a prior acceptance of this proof. Assurance is a complete mathematical argument with distinct host-agent review, using the separately reviewed RATIOS-007 complete-sum input and ROOTS-008 elementary counting calculations. It is not formal verification or external peer review. No usage measurements are available.

## Verdict and frozen inputs

**Supported:** the specified finite operator compression; weighted Schatten and endpoint-frame bounds, with their explicit list-fiber factor; the ambient restricted-Gram alternative; the pointwise counterexample; the enlarged-root bijection and multiplicity; the joint absolute-error count for every squarefree S, including primes dividing H; its stated restricted-aspect consequence; and the displayed real-coordinate height and boundary-derivative bounds.

**Incomplete:** the enlarged arithmetic trace estimate, the restricted endpoint-Gram estimate, the complete signed list/path and auxiliary-memory norm chain, its actual-prime transfer, polynomial roughness, and a Goldbach lower bound. None is claimed proved by the frozen statement. There is no demonstrated Goldbach breakthrough or novelty result.

| Reviewed input | SHA256 |
| --- | --- |
| `statement.md` | `44336ee22423b7a63550ff3b49ca394a9e12af1971eb04ac7c8e455a116a4b3d` |
| `survey.md` | `c7ae650b93001fda23496cef1bff04733e0862b73ba516158815a76cebaaf6ad` |
| `goal-bridge-source-audit.md` | `c0d88f11b5a0f027e03e94668a44768c4d74edf6e35f074c80c314a267fd82f6` |
| `source-provenance.json` | `3d341d58198f27acb1883df7d151a962cf1e5a152ce1cd342eea0d0570fc6c88` |
| Pinned Guo `main.tex` local copy | `e70d777424852aed92e94b2baf00384c84b4c7fc346bd7dab1085d5652ced95d` |

I changed none of these inputs. The source audit and provenance are reviewed framing and provenance records, not additional accepted analytic theorems.

## Finite compression, list weights and endpoint Gram matrix

The enlarged operator is defined intrinsically on primitive image positions. Its good-state complement ratio is the image ratio. On the unit-first-coordinate subspace this agrees with the transported ratio from SECTORS-006, and every exact and full-pullback comparison bracket agrees. Hence the identity (1) is an identity of the deliberately specified finite operators, with sector copies kept disjoint. It is not an identification of nonprimitive original preimages with the original arithmetic sequence.

No group containing a prime dividing H is silently replaced by a smaller normalized group. Such a prime can divide the first coordinate of an enlarged state and its list weight remains defined; it cannot occur in the unit-first-coordinate compression. This accounts for those groups without a division by an empty reduced group mass.

The singular-value approximation argument proves s_j(PBP)<=s_j(B), including weighted Hilbert spaces after passage to an orthonormal basis. Taking 2R powers gives (3) for every integer R>=1. It says nothing about a termwise positive replacement in a centered path expansion. In the author's three-dimensional counterexample, BB* is diag(5/4,5,0), whereas the upper two-by-two block of (PBP)(PBP)* is the all-ones matrix. The two claimed diagonal fourth moments are therefore exactly 25/16 and 2. The pointwise inequality is refuted, while the trace inequality survives.

The disjoint-support endpoint vectors form an orthogonal family. Their frame operator has eigenvalues ||u_P||^2, so (4) and then (5) follow with exactly mu_max and no extra number-of-positions factor. For ordered distinct lists of length m, the number of list choices is the falling factorial (n_i)_m, not the unordered binomial count. Formula (6) is exact under its explicitly stated product state weight. Counting distinct prime divisors by log(16U)/log p_min proves (7); fixed K, group masses bounded below, J of order L^0.01 and R of order sqrt(L) give (8). The finite factor must remain before this root is taken. Different weights, growing K or small masses require a new calculation.

The ambient-Gram alternative is also valid. For K=BB*, positivity gives <f,Kf> <= ||f||^(2-2/R)<f,K^R f>^(1/R). Cauchy bounds the pairing by ||g|| sqrt(<f,Kf>), and the positive Gram matrix bounds <f,K^R f> by D_E sum|alpha_P|^2. This proves (8a), treating f=0 separately. It uses the ambient power before restricting the endpoint family; it does not commit the false pointwise compression step. A small endpoint root moment does not bound a full trace: the projection onto (1,-1) annihilates the root vector (1,1) but has trace one. The full-trace target is a sufficient alternative, not a necessary replacement for the source Gram argument.

## Enlarged roots and multiplicity

For a primitive image root, us-wr=1 makes r a unit modulo u. The determinant-H matrix then satisfies vr=-H modulo u. Conversely, a permitted triple gives integral d=(H+vr)/u. If au+br=1, the stated c=av+bd modulo H satisfies cu=v and cr=d modulo H, so w and s are integral and us-wr=1. Bezout also proves uniqueness of c. This establishes the bijection without assuming either H or v is a unit modulo u.

Writing g=gcd(H,u), a unit-r solution requires gcd(v,u)=g. If so, reduction modulo u/g fixes one unit residue for r. The reduction map on units is surjective, with fiber phi(u)/phi(u/g), including g=u. The H=2,u=4,v=2 example has the stated two sectors. Different r cannot describe the same enlarged root because that primitive image root has a unique canonical complement. Counting only distinct original pairs would therefore give the wrong population.

The first row (u,r) is primitive at every prime, including primes dividing H even though the entire matrix can be singular there. Its horizontal kernel requires p|u. A nonhorizontal kernel (-rho:1) requires p not dividing u and r=rho*u modulo p. CRT proves (13) for squarefree S=QR, with no coprimality condition between S and H. This is the correct distinction from ROOTS-008's H-unit-filtered root population.

## The enlarged absolute-error count

At fixed admitted u, the r progression lies in [0,u) and R is a unit modulo u. Its normalized Fourier l1 norm is O(log(2u)), also when R>u and it is empty or a singleton. The v interval is periodized with multiplicities; complete periods cancel in each nonzero frequency, however large V/u is.

Double Fourier inversion imposes exactly v=-H*r^(-1) modulo u. Its zero v frequency is exactly (T/u)A_u. Mobius inversion over divisors of u gives A_u=L3*phi(u)/R+O(tau(u)), because these divisors are coprime to R. No zero r frequency has been discarded.

For j nonzero, the reviewed elementary complete bound applies to K_u(h,-jH), including zero h, zero -jH, even u and nonunit coefficients. Prime valuations prove gcd(h,jH,u)<=gcd(H,u)*gcd(j,u). The divisor-weighted geometric sum bounds the nonzero v Fourier norm by O(sigma_(-3/4)(u)log(2u)). This yields (14). Its subpower factors can be absorbed in any prescribed eta by allocating a smaller exponent to each. Divisor majorization then gives (15): only d<=16U contribute and their multiple count is at most 31U/d. This is why the surviving H dependence is sigma_(-3/4)(H), not H^(1/4) or an omitted H divisor count.

Replacing T by L2*V costs O(1) per u since A_u/u<=1. The A_u error is bounded by V sum tau(u)/u=O(Vlog(2U)^2). To check the remaining weighted-u mass directly, expand phi(u)/u=sum_{d|u}mu(d)/d. Only d coprime to R survive; count multiples of lcm(Q,d) coprime to R with error O(2^omega(R)). Their harmonic d sum gives the displayed O(2^omega(R)log(2U)) error. Extending the main series costs O(1), uniformly in Q: its absolute tail coefficient gcd(Q,d)/(Q*d^2) is at most 1/d^2.

The Euler factors relative to 1/zeta(2) are p/(p+1) at R primes and 1/(p+1) at Q primes. Multiplication by the outside 1/R converts the former to 1/(p+1). The mass error has the same prefactor, so its cost is 2^omega(R)/R<=1, including p=2. This proves exactly the density and uniform absolute error (12). There is no kappa_b(H) because the H-unit filters have been removed. The calculation supports every squarefree S, not merely S coprime to H.

Half-open canonical intervals prevent double counting r=u and retain all integer endpoint errors. Empty intervals and large Q or R do not create a relative asymptotic: their main mass can be smaller than the absolute error. Under the specified H<=X^A and subpolynomial S, both sigma_(-3/4)(H) and the inverse prescribed-line density are X^o(1). Dividing the finite error by UV gives U^(3/4+eta)/V and 1/U, hence the asserted gamma=min(a,b-3a/4), with arbitrary exponent slack. Fixed positive interval lengths give the stated restricted-aspect relative result. The balanced exponent 1/8 follows. No all-aspect or arbitrary shrinking-interval relative estimate is supplied or refuted.

## Geometry and the first remaining arithmetic obligation

The image root matrix is unimodular, so relative integer coordinates exist uniquely and preserve image primitivity. In original coordinates Q=G_H z, determinant expansion gives z2=det(P,Q)/H. The box bounds imply (16), and direct substitution gives (17). With lambda=H/(UV), any occurring z has |lambda*z2|<=32. Derivatives in t cost z2, while derivatives of lambda*z2/s0 remain bounded; tau and z1 have the displayed O(1+UV/H) control. Thus the claimed first derivatives and higher s0 derivatives are bounded as stated. This does not imply a bounded-variation estimate for an arbitrary product of all discontinuous path restrictions.

The first new arithmetic trace/path obligation can be stated concretely. Expand the actual T_R, or the sufficient selected-root D_E, with all weighted list states. Specify its endpoint closures, active prime lists, memory/distinctness conditions, signed centered edges and root-relative positions. For each summand identify its exact finite prescribed-line modulus and real root region. Then prove that the sum of the absolute coefficients times the accumulated counting and boundary-partition errors from the appropriate root theorem is smaller than UV*L^(-2RE). Formula (12) is one fixed-data input, not that summed estimate. For D_E, the retained unit endpoint root population additionally requires its actual filters, as in ROOTS-008; its density cannot simply be replaced by the enlarged density. For a full trace, closure of a basis list state must be retained rather than replaced by an all-ones endpoint fiber.

After that arithmetic replacement one still needs the small bound for the resulting signed model moment, including clean and dirty edge norms and memory/ghost operations at the actual weights. Neither individual subpolynomial coordinate bounds nor a finite compression proves these cancellations. In particular, mu_max is harmless only after its specified root, whereas the unlocalized volume factor (UV)^(1/(2R)) is large at UV comparable to x. The author explicitly preserves all these gaps.

## Source provenance and prioritized findings

I inspected the locally pinned [Guo source](https://github.com/aster2024/openai-math-followups/blob/a605351dce1a55fb46a494d9cca9b0baa8f2734b/mobius-goldbach-shift/source/main.tex), including input lines 124-146, enlargement and intrinsic-ratio lines 962-1030, and the geometry/root/Type-II chain at lines 1249-1394. Its declared H2' assumes the correctness of LWW's specified operator and moment arguments. It already uses labelled lattice-primitive enlargement and ambient positive-power restricted Gram matrices, and explicitly says a full trace on added nonunit states is unnecessary. Its root/path and Type-II transport are conditional assertions, not imported validation of those arguments here. The recorded exact source copy has Git blob `a114f906cf205f4e50053c7a657f7de55048213c`. Source identity and inspected text establish provenance, not correctness of its entire analytic chain.

No mathematical repair is required for the frozen limited claims. Three integration findings must remain visible:

1. **P1, arithmetic moment remains incomplete.** The first missing load-bearing step is the weighted signed path replacement and ensuing model edge/memory bound described above. Decisive next check: write the exact finite T_R or D_E expansion, bound its total discrepancy cost and prove its signed model bound with every projection and normalization present. A root count or a citation to H2' does not discharge it.
2. **P2, do not conflate endpoint, trace or root populations.** Keep mu_max, the Gram-family coefficients, endpoint closures and unit filters explicit. The two-state annihilated endpoint example decisively rules out recovering a full trace merely from small indicator-endpoint moments. Full-trace enlarged roots have density 1/zeta(2); retained unit endpoint roots have their own filtered density. Preserve the absolute-error and aspect restrictions of (12).
3. **P1, source and Goldbach bridge remain unproved.** Guo already supplies closer enlargement/Gram framing. Neither the present finite specialization nor that conditional source establishes the full changed denominator-H prime major term, actual-prime reflected correlation, polynomial-label margins or Goldbach lower bound. Keep novelty unverified and do not mark the user's Goldbach objective complete from these results. A decisive substantive advance would require a proved uniform estimate for the actual required prime/operator correlation with its dependencies resolved.

The accepted outcome is a valid finite bridge and an enlarged unweighted counting theorem with explicit costs. It leaves the actual arithmetic cancellation task open.
