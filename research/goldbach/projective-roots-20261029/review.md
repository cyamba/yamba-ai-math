# Independent review of the joint projective-root count

29 October 2026. Registry role: Independent Critic, `GOLDBACH-ROOTS-008`. This is the actual critic stage following the populated statement packet. The separate `pre-mortem.md` was written before reading this proof and is not an earlier acceptance of it. Assurance here is complete elementary argument plus distinct host-agent review, without formal verification or external peer review. Usage measurements are unavailable.

## Verdict and frozen input

**Supported:** Candidate 1, the finite absolute-error formula uniform in H, S, prescribed lines and intervals; and Candidate 2, its power-saving consequence in the explicitly restricted aspect range b>3a/4.

The proof retains the zero completed frequencies, all squarefree H divisors, canonical complement representatives, nonunit row entries at prescribed primes, and the R-dependent exclusion cost before absorbing it. I found no missing positive power of H, hidden loss in S, or endpoint error invalidating the stated estimates.

**Incomplete:** the broader all-aspect power-saving target in the brief, relative asymptotics for arbitrary shrinking intervals, and any prime-weighted/list-moment/operator application or Goldbach lower bound. Those are not asserted by the frozen statement. No demonstrated Goldbach breakthrough or novelty follows.

The reviewed statement SHA256 is `42d72d988c7e82e71b2de7a901b5bb17708a7e61053017fc1fbf46c340b89dcf`. The reviewed survey SHA256 is `93d2cda5df7055243759b4116b9b54592cf6f05b876863f2b86ac9d554b5132e`. I changed neither input. The optional next-operator framing was not used as a dependency.

## Exact CRT reduction, including nonunit entries

The canonical c exists because v is invertible modulo u. It is also coprime to u because H is invertible there. Thus the first row (u,c) is primitive, and determinant H makes the matrix invertible at every prescribed prime.

For the horizontal kernel (1:0), the exact condition is p|u; c is automatically nonzero modulo p. Every other projective line has one representation (-rho_p:1), and its condition is c=rho_p*u modulo p together with p not dividing u. Otherwise both row entries would vanish. This proves the Q/R reduction, including rho_p=0, p=2 when allowed, and arbitrary powers of Q primes in u. No complement lift is altered to make a congruence convenient.

The horizontal case is indispensable. The preparatory example H=2, u=3, v=5 has canonical c=2 and determinant-H complement d_H=4. Its first-row kernel modulo 3 is horizontal, although u is not a unit modulo 3. The proof correctly keeps that case. Conversely, omitting (S,H)=1 would invalidate the universal line density: at H=3,S=3 the required u-unit condition makes the horizontal line impossible. These are witnesses to hypotheses the actual proof retains, not counterexamples to it.

## Canonical c Fourier completion

For a fixed admitted u, gcd(R,u)=1. Its candidate c values form one arithmetic progression inside [0,u), with no repeated residue modulo u. Multiplication of the Fourier frequency by R permutes the residue frequencies. The geometric-series bound therefore gives normalized Fourier l1 norm O(log(2u)), even if R>u and the progression is empty or a singleton. Its zero mode divided by u is at most one. This estimate has no S-dependent coefficient.

The w interval may span many periods. Its nonzero Fourier modes still satisfy the usual geometric bound because whole periods cancel. Weighting by gcd(j,u)^(1/4) costs the stated sigma_(-3/4)(u): after majorizing by a sum over divisors e of gcd(j,u), write j=e*l and sum the harmonic series on the reduced interval. The normalized cost is O(e^(-1)log(2u)), giving e^(-3/4) after its weight. The zero w-frequency is not included in this estimate.

The complete-sum input is the already separately reviewed RATIOS-007 lemma, valid at even moduli and zero or nonunit frequencies. Its finite fourth-moment/orbit proof is a dependency, rather than acceptance of a variable-H LWW theorem. The subpower factors C(u) and sigma_(-3/4)(u) can be combined within the requested arbitrary eta by choosing each exponent sufficiently small.

## Fixed-u relation and every H divisor

Expanding v-coprimality over b|rad(H) is exact. Every b is a unit modulo u, and the relation becomes w*c=A_b with A_b=-H*b^(-1) a unit modulo u. It enforces both c and w invertible modulo u, hence the primitive-position condition, without an additional discarded population.

Two finite Fourier inversions give the displayed double frequency sum with K_u(h,j*A_b). For j=0, summing over h yields exactly (T/u)*A_u by orthogonality, with A_u counting the unit c candidates. For every j!=0, including h=0, the common-frequency gcd is bounded by gcd(j,u). Applying the complete bound and the two Fourier norms proves (6). No zero-c-frequency term is dropped.

Replacing the integer w-cardinality T by L2*V/b costs O(1), since A_u/u<=1. This also handles b>2V, where the actual interval is empty, and every intermediate short interval. Summing all tau_H radical divisors gives phi(H)/H in the main term and exactly the displayed tau_H error factor. There is no unproved congruence estimate with modulus H and no omitted large-divisor tail.

## Both mass computations and the local density

For A_u, inclusion-exclusion over divisors e of u is legal because e is coprime to R. The constraints e|c and c=rho*u modulo R are one class modulo eR. Counting that class in the actual half-open canonical interval gives L3*u/(eR)+O(1). Thus A_u=L3*phi(u)/R+O(tau(u)), uniformly even when rho or c is nonunit modulo R. The summed error in (9) is bounded by the elementary sum of tau(u)/u and costs O(Vlog(2U)^2).

For the remaining weighted u mass, write M0=HR. A divisor d arising from phi(u)/u is coprime to M0. Multiples of lcm(Q,d) can then be counted with the coprime density phi(M0)/M0 and error O(2^omega(M0)). Since Q is coprime to HR, this gives exactly tau_H*tau_R times the harmonic d sum. Extending the main series costs O(1): the absolute coefficient (Q,d)/(Q*d^2) is at most 1/d^2, including when Q exceeds the u range.

The Euler product in (10) checks prime by prime. An HR prime changes the base reciprocal-square factor to p/(p+1). A Q prime has its outside 1/p and replaces 1-1/p^2 by 1-1/p, giving 1/(p+1). Prime powers in u were never removed by these calculations.

Crucially, the weighted-mass error is multiplied by V*L2*L3*phi(H)/(H*R). Its R cost is therefore tau_R/R, bounded by one because R is squarefree and each factor is 2/p<=1. This remains true at p=2. Absorbing this factor only at this stage is valid. It would have been invalid to claim the coprimality exclusion itself had no cost.

The resulting main coefficient is precisely kappa_b(H) divided by product_{p|S}(p+1): H primes acquire their second unit factor, R primes acquire the outside 1/R, and Q primes already have the line factor. This derives the line density for the actual canonical-root count instead of merely copying a complete matrix density. Summing the completed-sum errors over u contributes the stated U^(7/4+eta) term. The remaining mass errors are dominated by the stated V term. Formula (1) follows with constants depending only on eta and with no positive power of H or S.

## Endpoint and uniformity checks

All three real intervals are used half-open. In particular c=u never enters the canonical interval, c=0 is correctly excluded by the unit relation for u>=2, and every integer endpoint correction is included in the cardinality or coprime-count errors. Empty intervals give an absolute estimate with zero main length; no division by a zero population occurs.

Large Q can leave no admitted u, and large R can leave very few c candidates. The absolute formula can still be true with its coarse error larger than its main term. Independence of S in that error is not a relative estimate for every line at every finite size. The proof's Fourier and prefactor bounds explain why it is nevertheless a valid absolute estimate.

Under H<=X^A, its radical-divisor factor is uniformly X^o(1). Dividing the finite error by UV gives the exponents -a and 3a/4-b, with eta absorbed in any fixed requested slack. This proves Candidate 2 for b>3a/4. The prescribed density is X^(-o(1)) in the declared subpolynomial S range, since product(p+1)<=S*2^omega(S)<=S^2; the inverse H density is likewise subpower. Fixed positive interval lengths therefore give the stated relative power saving and eventual nonemptiness. The balanced example has exponent a/4, hence 1/8 at a=b=1/2.

For a general shrinking-interval family, a relative conclusion needs the explicit main mass to dominate the absolute error. Equivalently, the product of interval lengths times kappa_b(H)/product(p+1) must dominate the error divided by UV. The statement appropriately promises only an absolute estimate otherwise. The preparatory gap interval [0,1/(32U)) is a concrete reason: no canonical ratio lies there, although its continuum main term is positive. This is compatible with the accepted absolute error and contradicts an unqualified relative assertion, which the author does not make.

When b<=3a/4, the displayed completion error supplies no fixed negative power. This is a failure of this particular error bound to prove the full brief's all-aspect target. It neither refutes the candidate main term nor lower-bounds the actual error. The proposed transposed route has a moving real phase, and its uniform treatment is not supplied here.

## Findings and integration limits

No mathematical repair is required for the frozen statement. The following scope conditions must remain in the revision:

1. **P1, broader target remains open.** The proof establishes a joint unweighted root count in a useful restricted aspect range, not the original all-aspect power-saving target. Keep that unresolved part explicit rather than marking it refuted.
2. **P2, absolute versus relative error.** Preserve (S,H)=1, the Q/R line split, every H divisor, half-open endpoints and the prefactor that absorbs tau_R. Relative estimates require a sufficiently large prescribed interval main mass; empty and very thin populations remain unnormalized.
3. **P1, operator and prime obligations remain.** No prescribed growing-list moment, selected-endpoint norm estimate, changed denominator-H prime major term, or actual-prime correlation bound follows from the finite count alone. The optional next-operator framing is not evidence for any of those estimates.
4. **P3, assurance and priority.** The elementary complete-sum input and inverse-distribution methodology are established prior tools. This audit supports the presented specialization, not a full source-theorem extension, a novel general result, a Goldbach lower bound or a demonstrated breakthrough.

The exact-density and uniform absolute-error derivation pass this separate review. A later use must propagate its actual error through the full list/path expansion and show that accumulation is smaller than the needed centered scale; that step is not part of the accepted result.
