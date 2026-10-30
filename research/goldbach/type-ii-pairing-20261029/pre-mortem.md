# Separate pre-mortem for the reflected Type-II pairing

29 October 2026. Independent Critic, supplemental preparatory dispatch for `GOLDBACH-PAIRING-011`. I read the brief, survey and actual statement-stage packet as framing, then the pinned Guo source's cofactor square, block definitions and transport, especially lines 1249-1419. The local source SHA256 is `e70d777424852aed92e94b2baf00384c84b4c7fc346bd7dab1085d5652ced95d`, Git blob `a114f906cf205f4e50053c7a657f7de55048213c`. The [pinned source](https://github.com/aster2024/openai-math-followups/blob/a605351dce1a55fb46a494d9cca9b0baa8f2734b/mobius-goldbach-shift/source/main.tex) and [Lue-Wang-Wu Sections 4.6-4.7](https://arxiv.org/html/2610.20242v1#S4.SS6) supply proof text to inspect, not an accepted Type-II theorem.

This is not the main critic stage, acceptance of an unseen author proof, or a complete Type-II/actual-prime/Goldbach verdict. Only this preparatory file is owned. No further classical PDF source was used, and no usage measurements are available. The actual accepted MOMENTS-010 revision and its precise scope must be used later.

## 1. P1: preserve positivity in the original target and in the upper-bound square

The original target uses mu(H-mn) only for H-mn>0. Its selected-prime expansion therefore has positive cofactor h. Cauchy bounds it by a square over positive h; extending that nonnegative square to all nonzero integer h is valid. It does not introduce a Mobius value at a negative argument. The endpoint coefficients of the enlarged square can remain separately supported in m and n.

A small support illustration is H=2, selected a=3 and mn=5: its enlarged cofactor is h=-1 and belongs only to the enlarged upper-bound square, not the positive original target. Zero cofactor requires its own exclusion: H=mn is impossible for H>1 when both variables are units modulo H. If unit support is omitted, H=6,m=2,n=3 gives a zero cofactor even with a selected prime a=5 coprime to H.

Keeping the positive product cutoff inside a signed centered operator instead is a different assertion. Entrywise restriction need not preserve its small norm. For example, the matrix [[1,1],[1,-1]] has norm sqrt(2); the joint cutoff mn<3 on row/column values {1,2} changes it to [[1,1],[1,0]], whose norm is (1+sqrt(5))/2. This is a finite warning about the proposed norm inference, not a counterexample to a correctly enlarged arithmetic square.

The eventual statement must also choose compatible fixed cutoffs. Eta should be real, so expansion of the square has eta(a/Y)eta(b/Y), rather than a missing conjugate. To identify the operator's raw term with Q_all, its common smooth determinant cutoff must equal one on every raw value supported by those etas. With eta supported in [1,4], requiring psi=1 on [-3,3] suffices because det/(HD)=b-a there. MOMENTS-010 permitted an arbitrary fixed smooth compact psi for its norm theorem; that alone does not supply this exact pairing identity. Taking psi identically zero is a smallest logical falsifier of an unrestricted identification with a nonzero raw square.

Decisive next check: the frozen author must define the original positive target, real eta, raw-support plateau of psi, zero-cofactor exclusion and exact all-signed square before invoking the moment.

## 2. P1: the determinant equivalence needs coprime a,b and absolute overlap bounds

For coprime a,b, the determinant equation

    bmn-ars=H(b-a)

implies a|(H-mn) and b|(H-rs) by reduction modulo a,b, then equality of the integer quotients. Positivity is unnecessary. Without coprimality the reverse implication is false even when a,b are units modulo H: H=2, a=b=3 and m=n=r=s=1 satisfy the determinant equation, but both proposed cofactors equal 1/3. Shared-prime terms therefore cannot be silently reinterpreted as integer-cofactor terms.

The expected repair is an error estimate on the actual shared-prime subarray of the raw square, followed by the comparison array separately. For raw terms, fixed selected products a,b permit Cauchy over the actual integer cofactor and a divisor-square bound. The full signed cofactor range has length O(H/Y); H/X can cost a fixed power of log x and must be retained. The divisor-square proof uses gcd(a,H)=1 to ensure a divisor of H-a*h is coprime to a, then the usual largest-factor deletion and residue count. The endpoint product range remains positive even though h may have either sign. Its nonzero values are O(H), so an O((H/Y)log^3 H) bound is consistent with the full interval and subpolynomial Y.

For comparison terms, the full pullback gives H|(bk-a*l). Because a,b are units modulo H, fixing k permits one residue class for l modulo H in an interval of length O(H), hence O(1) choices; the reverse degree is also O(1). This supports an absolute divisor-square estimate by 2*tau(k)*tau(l)<=tau(k)^2+tau(l)^2. The comparison arc multiplier is O(L^(3A0)/Y). Counting selected-product pairs with a common band prime costs O(Y^2*sum_p p^(-2)), exponentially small in the minimum band scale. These are concrete counts to prove at their actual coefficient bounds, not positivity of the comparison form.

The original selected-divisor expansion has a separate square-overlap error: a selected p dividing h makes p^2 divide H-mn. Since p avoids H, there is either no solution when p divides m or one residue class of n modulo p^2. With both dyadic lengths a fixed power of x and p^2=x^o(1), the residual endpoint term is absorbed. The rho-weighted number of selected choices is uniformly bounded for fixed K,rho and V_i bounded below. That weighted counting step must appear if an unweighted square-divisibility count is used.

Decisive next check: expand the two cofactor sums before dropping their integer divisibility conditions, and keep separate raw/comparison overlap bounds including H/X losses.

## 3. P2: complex endpoint coefficients and the Hilbert norm need exact identification

With the inner product conjugate-linear in its first argument, the correct endpoint coefficient is

    f(Db*m,s)=conj(alpha_m)*beta_s.

For Q=(Da*r,n), this gives conj(f(P))*f(Q)=alpha_m*conj(alpha_r)*beta_n*conj(beta_s), exactly the expanded cofactor-square coefficient. Omitting the alpha conjugation reverses it in general: alpha_m=i and alpha_r=beta_n=beta_s=1 give i as the required coefficient and -i from the incorrect choice.

Sifting above Z while all band primes are below Z makes the complete band-prime part of Db*m exactly Db. Thus f is independent of list ordering on its endpoint support. For fixed ordered full prime product G, count endpoints by O(UV/G), with U=d0YM,V=N. Summing the actual ordered state normalization uses

    product_i V_i^(-m) * sum_ordered_lists 1/G <= 1.

This follows by dropping distinctness into the nonnegative product harmonic sums. It gives ||f||^2<=C*UV*L^(4C) when each coefficient array is bounded by L^C. Its logarithmic exponent is independent of K,J. A factorial or an extra list-count bound here would spoil the intended normalization.

Automatic primitivity must be established for comparison endpoints too. With coprime a,b and the small-band/sift separation, gcd(b,a*r*s)=1 and b>1 force t=bmn-ars!=0. A common prime of Db*m and s exceeds Z and avoids H. Since H|t and |t/H|=O(Y)=o(Z), it would divide a nonzero integer smaller than Z, a contradiction. The same proof applies at the other endpoint. The full H-fold pullback, not just the raw determinant equation, is needed for its comparison congruence.

Decisive next check: define f from the position's complete band part, prove both endpoint supports and primitivity, then calculate its norm in the exact list Hilbert measure.

## 4. P1: keep the H lattice block and ambient Gram power

For unit first coordinates the congruence H|det(P,Q) is exactly equality of their unit slope classes modulo H. Every such class must remain a separately labelled index-H lattice. The real slope changes across an allowed edge by O(H/(d0Y*M^2)), so cells at this width have bounded neighboring interaction.

An occupied cell in a fixed labelled lattice has O(d0Y) primitive endpoints. Choose one lattice-primitive P0 in it. Determinants with every other endpoint are multiples of H and have magnitude O(H*d0Y). For a fixed determinant, two solutions differ by an integral multiple of P0 because P0 is primitive in that lattice. Their first-coordinate interval permits O(1) multiples. The number of determinant multiples is O(d0Y). Using all integer determinants instead would introduce an unnecessary H loss. For the entire labelled block, the stronger count O(1+UV/H) is also available; in the present range UV/H=d0Y*X/H tends to infinity and is at most d0Y.

For each cell use K=B*B^* in the ambient enlarged space and the selected unit endpoint vectors. The positive matrix with entries <u_P,K^R*u_Q> has largest eigenvalue at most the sum of its diagonal entries on that cell. Spectral Holder is applied before selecting those endpoint roots. Sum the resulting pairing inequalities by Holder over cells and labelled blocks, using disjoint f supports and bounded overlap of neighboring g supports. The total diagonal sum is the selected-root moment from MOMENTS-010, not a full trace and not a moment with intermediate unit projections. No factor equal to the number of slope classes appears.

Together with the endpoint norm, this leaves the explicit loss (d0Y)^(1/(2R)), bounded at the accepted parameters. Pointwise deletion of intermediate projections from powers is false, as recorded in TRACE-009, and cannot replace this argument.

Decisive next check: keep the actual label/cell partition in the coefficient-space Gram calculation and account for each selected root exactly once.

## 5. P1: bad-state removal and ordered reassembly require their own positive estimates

A high signed moment does not by itself bound an absolute form supported on bad roots. The source proposes a separate one-edge route, which must now be reconstructed. First dominate arbitrary endpoint coefficients by their suprema. In the independent-line model a one-edge list union has J+2 distinct primes per group, giving total normalized harmonic-line mass at most one. For fixed lists the source bad-ratio measure is exponentially small. A uniform absolute count leaves O(1) raw targets and O(Y) comparison targets, the latter multiplied by O(L^(3A0)/Y). Integration over bad ratios then bounds the positive one-edge model. Reverse the edge for target-bad terms. The one-edge arithmetic replacement must include those bad-test boundaries and its own accumulated counting error; it is not obtained from the signed high-moment statement alone.

The remaining artificial shared-list average has an exact scalar identity. Dividing a block pairing by d0 changes d0/D to 1/D. Its state and one-edge normalizers give, in each group,

    (1/D)*V_i^(-(J+2))
      = product_shared_slots (1/(p*V_i)) * V_i^(-2),

where the displayed D on the left denotes that group's shared product, or the identity is multiplied over groups. The J shared slots are ordered harmonic draws. They are distinct and avoid the two unshared endpoint primes with probability w(a,b); the union bound gives 1-w=O_K(m^2*max_p(1/(p*V_i))). Summing all dyadic D blocks counts each ordered tuple once. It inserts neither J! nor J+1, and the mass of an individual block is not assumed to be one. Endpoint list invariance permits removing the list symmetrizations in the scalar pairing.

To replace w by one, multiply this collision loss by separately proved absolute raw and comparison bounds. Restoring shared a,b terms requires their own estimates from item 2. Each block pairing has scale d0Y*X, hence division by d0 has scale Y*X; the O_K(L) dyadic sum consumes a fixed precision loss. H*Y is a permitted final relaxation in the declared range, with any H/X logarithmic cost explicitly absorbed. The proof must state the parameter order so its final logarithmic exponent does not grow with K or J.

Decisive next check: prove the positive one-edge replacement, then write the exact ordered tuple reassembly before applying any collision estimate. The source's H2'-conditional paragraph is not a replacement for either proof.

These are preparatory obligations and narrow finite witnesses. A later main review must inspect the frozen actual statement and packet, the accepted MOMENTS-010 revision, and the exact checks. No Type-II difference theorem, major comparison estimate, actual-prime cancellation or Goldbach result is accepted by this pre-mortem.
