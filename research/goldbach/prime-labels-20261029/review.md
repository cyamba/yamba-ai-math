# Independent review of the prime-label adaptations

29 October 2026. Registry role: Independent Critic, `GOLDBACH-LABELS-005`. This is a separate host-agent mathematical audit of the stated adaptations and source-parameter comparisons. It is not formal verification, external peer review, or validation of the full Lue-Wang-Wu manuscript. Usage measurements are unavailable.

## Verdict and reviewed inputs

**Supported:** the support bounds, bounded-label reconstruction identities and stated coefficient costs, repeated-factor corrections, uniform exceptional-count bound, half-weight deweighting, exact quotient expansion, and scalar padding identities.

**Supported as diagnoses of the available source bounds:** the small-K dirty-edge deficit, polynomial-height moment loss, moving-target and primitivity changes, and the separate `parameter-retuning.md` feasibility calculation. These do not establish lower bounds on the actual operator norms and do not exclude a different argument.

**One clarification required:** the collision probability is exactly 1/t_i for equal divisor selections. For arbitrary normalized selection probabilities on the t_i forced divisors, it is at least 1/t_i, and need not equal it. This strengthens rather than removes the collision obstruction.

**Incomplete:** a target-uniform estimate with the correct nonzero center for the adapted signed weights. Neither adaptation supplies a Goldbach lower bound or a demonstrated breakthrough. Novelty and the full original manuscript remain unverified as dependencies.

| Reviewed file | SHA256 |
| --- | --- |
| `statement.md` | `e8ae7df93ac39e8741ed5daa71bc24bf46fb49bcaae77c6aae4d14bd24df515e` |
| `survey.md` | `35394ed75dacc23c4be202f8ba987cb800694f8d7080bddad873f339b7027085` |
| `parameter-retuning.md` | `522cd21ceeda38915d4f468e273f2e0dfbb9f86034108cdbe08643e0bd81115d` |

The statement was supplied through the populated counterexample packet. The parameter calculation is a separate root-authored supplement. I changed neither mathematical input.

## Source inspection and limits

I inspected the relevant statements and parameter displays in [Lue-Wang-Wu, arXiv:2610.20242v1](https://arxiv.org/html/2610.20242v1): the auxiliary groups and weight in section 2.3; the fixed-shift determinant relation; the active-list and moment parameters; the dirty-edge bounds (4.48)-(4.51); the moment-to-pairing calculation through (4.68); and the root-averaging input range and appendix error (A.5). These are source descriptions and algebraic parameter checks, not a completed audit of its theorem or full analytic proof chain. The report correctly declines to import a moving-target, polynomial-label theorem from these statements.

## Bounded genuine labels: exact algebra

The original source groups have primes at most exp(2L^a), a<1/5. For each fixed alpha>0 this is below exp(alpha*L)=N^alpha eventually, so no group prime divides an admitted rough complement. Its required-group weight is therefore zero on that population.

After moving K disjoint required groups above N^alpha, a nonzero term requires at least K distinct prime divisors, whose product is strictly greater than N^(K*alpha). Since q<N, support is empty when K*alpha>=1, including equality. The observation does not rule out bounded K. The proposed single group covering every prime above the cutoff and below N does cover every factor of the admitted q.

For squarefree complements the profiles h_rho(k)=k*rho^(k-1), k=1,2,3, give the displayed three vectors at rho=1/4,1/2,3/4. Direct substitution verifies

    3*h_(1/4)-3*h_(1/2)+h_(3/4) = (1,0,0),
    (17/3)*h_(1/4)-(25/3)*h_(1/2)+(11/3)*h_(3/4) = (1,0,1).

The Mobius signs then give Z_rho=-R+2rho*E0-3rho^2*H0 and the exact signed reconstructions (A4)-(A5). Their l1 costs are 7 and 53/3 for these fixed nodes and coefficients. They are not asserted to be optimal over other choices of nodes, and no such optimality was established here.

The unsigned distinct-factor table is also correct. Prime squares produce a false positive for the bare odd indicator, while distinct r^2*s triples produce a false negative. Prime cubes have nu=1 and still receive the correct bare odd value. Ordinary mu kills every nonsquarefree input instead, so (A5) counts squarefree odd complements and must add nonsquarefree odd triples to recover F. The prime reconstruction (A4) needs no such correction.

Every nonsquarefree admitted q has r^2|q for a repeated prime r>N^alpha. Since p determines q uniquely, counting all such integer multiples bounds its population by N/(z-1), as stated. Its ratio to A_N tends to zero because S(N) is bounded below and N^(-alpha)log(N)^2 tends to zero. The same argument controls the difference of rough mu and lambda sums. It does not assert equality of the functions.

The three displayed suprema are 1, 1 and 27/16, so the coefficient-weighted bound for the bare odd interpolation is 323/16. The source-normalized W_rho divides these costs by the explicitly retained V_N, whose limiting value log(1/alpha)>0 is correct. At rho=1/2, the profile (1,1,3/4) gives both identities in (A7) exactly. The earlier reviewed H bound controls the squarefree triple error in the fixed-epsilon asymptotic regime; it does not estimate the signed sum itself.

## Centering, quotient boundaries, and norm propagation

The stated formal center has the signs and factors dictated by the exact three cells. At the limiting cubic boundary it is generally nonzero, since the semiprime coefficient tends to log 2. Those averaged coefficients are not promoted to a target-uniform theorem.

The simultaneous-zero-center contradiction is sound. If all three Z sums were uniformly o(A_N), (A4) would force R=o(A_N). PNT gives a positive average prime-pair count at order X^2/log(X)^2. Removing representations with the complement at most N^alpha changes that average only by O(pi(X)*pi(X^alpha)), which is lower order. Expanding the nonnegative singular-series divisor product gives exactly the bound sum_{even N<=X}S(N)<=X: the full reciprocal divisor product is C2^(-1), cancelling its prefactor. Consequently sum A_N is O(X^2/log(X)^2), and the asserted uniform little-o conclusion would contradict the positive average. It is therefore invalid to copy simultaneous zero cancellation to these adapted weights.

For correctly chosen centers with prime reconstruction equal to 1, errors bounded individually by eta*A_N propagate with l1 cost 7. Thus eta<1/7 is indeed sufficient for positivity. This elementary implication does not prove the centers or error estimates.

The quotient expansion (A8) checks term by term. On squarefree q, selecting each prime r|q once gives mu(q)=-mu(q/r) and exponent nu(q/r)=nu(q)-1. The factor nu(q) arises from the number of selections. Nonsquarefree inputs vanish through the explicit squarefree condition. The quotient h=1 contributes exactly -R; prime and squarefree-semiprime quotients reproduce the other two terms of (A3). Thus a theorem restricted to long quotients cannot silently discard h=1. On a macroscopic prime-complement interval, its selected prime label is itself macroscopic.

The finite divisor expansion terminates after three distinct factors, but its two-label moduli already exceed N^(2alpha)>=N^(3/5). The fact that its algebra terminates does not put its progression errors inside ordinary BV. No new progression or character-Mellin estimate for these terms is supplied.

## Source bounds and the concrete retuning attempt

The source's dirty-edge error has a first displayed term proportional to L^2*(J+1)^(-K). Its large-K Schur calculation produces the stated L^(1-0.005K) term at J+1 comparable to L^0.01. Substituting K<=3 does not yield a negative logarithmic exponent. This is a failure to certify decay with the displayed estimate, not evidence that the actual norm grows or cannot decay.

At the published moment order 2R comparable to sqrt L, a complete product of K(J+1) polynomial labels has log height at least K(J+1)alpha*L. Since the source leaves a height factor to the power 1/(2R), the resulting factor is at least exp(c*K*alpha*(J+1)*sqrt L). It exceeds every fixed power of L even for constant J. The author correctly identifies the surviving factor rather than omitting it during moment extraction.

The supplement's retuning calculation is a valid narrower comparison. To fit the displayed positive dirty-edge budget term within L^(-G), its inequality requires J+1 at least a constant times L^(2(G+C+1)/K). Increasing J while keeping the published R makes the height factor worse. Keeping that height loss within a fixed logarithmic power would require R at least a constant multiple of K*alpha*(J+1)*L/log L, outside the cited moment statement. This calculation imposes requirements on a use of those particular upper bounds, not necessary conditions on an unknown better norm estimate.

There is an independent earlier range failure. The root-averaging proof prescribes squarefree moduli only through exp(O_K(L^0.98)); a single polynomial label p>N^alpha exceeds this range eventually for every fixed K and fixed implied constant. Retuning J or R does not reverse alpha*L>C*L^0.98. The appendix's error depending on S^5 cannot be replaced by a larger-range theorem by assertion. A new root-averaging estimate would be needed before a retuned moment argument could use it.

The source also uses its auxiliary primes below the sift threshold to identify the auxiliary part and prove primitive positions. Polynomial labels exceed that threshold, so the same coprimality conclusions do not follow from the old sifted support. The reflected equality gives bmn-ars=N(b-a), with the displayed sign, replacing the fixed-shift determinant. The small-determinant primitivity argument therefore needs a new moving-target treatment. The audit does not assert that every such treatment is impossible.

## External padding and its exact limitations

Since D is squarefree and uses only group primes below z, it is coprime to every admitted q. Thus W(Dq)=C_D, mu(Dq)=mu(D)mu(q), and lambda(Dq)=lambda(D)lambda(q) are exact, including nonsquarefree q for the Mobius identity. The padded signed sum is just the stated nonzero scalar times the original sum. A q-independent average remains one scalar times that sum; if the scalar is zero, the average contains no recoverable information and cannot be divided by zero. Its center must transform by the same scalar.

For one forced divisor in each group, all algebraic selections of the required labels give a=b=D. Discarding shared-label terms would discard the entire construction. For t forced labels, equal independent selections collide with probability 1/t. For arbitrary normalized probabilities pi_j supported on those labels, the collision probability is sum pi_j^2>=1/t; for example probabilities 3/4 and 1/4 give 5/8 rather than 1/2. This is the requested wording correction. It preserves the collision obstruction under the source's potentially nonuniform prime-selection measures.

At t_i=J+1 and fixed rho, the displayed inverse-normalizer logarithm is correct and has leading order K*J*|log rho|. With J comparable to L^0.01 its inverse exceeds every fixed logarithmic power. This cost cannot simply be suppressed when checking a theorem with fixed bounded endpoint multipliers. Taking rho to depend on J would itself leave the source's stated fixed-rho regime and require uniform estimates; no impossibility for such a newly proved extension is claimed.

Finally n= Dq gives n+D*p=D*N. The padded polynomial in p has common divisor D, and removing it returns the original reflected form. As a sequence on multiples of D, its mass is the original prime mass and its roughness is imposed after dividing by D. Neither becomes the unrestricted mass or roughness at ambient size D*N. The report correctly keeps these changes explicit.

## Findings and required revision

1. **P3, collision precision.** Amend the exact probability 1/t_i to specify equal divisor selections. For arbitrary normalized choices state the lower bound sum pi_j^2>=1/t_i. The two-label probability example above is a concrete counterexample to an unqualified exact-probability statement.
2. **P2, source-range integration.** Include the separately reviewed root-averaging range obstruction and retuning calculation in the final synthesis. Raising J or R is a concrete attempted repair whose use of the existing estimates fails; it is not a theorem excluding a newly proved small-K or polynomial-modulus argument.
3. **P1, analytic objective incomplete.** Exact coverage, reconstruction, deweighting and padding do not prove the correctly centered target-uniform signed estimates. Preserve the nonzero-center issue, the h=1 boundary, and the lack of a moving-target theorem. No actual Goldbach lower margin or breakthrough is established.
4. **P3, assurance and scope.** Retain the fixed-parameter order of limits and all norm/normalizer costs. Do not describe an increasing term in an available upper bound as a lower bound on the actual operator. This audit inspects only the indicated primary sections and does not certify the full preprint, every adaptation, or priority.

Apart from the collision wording and integrating the separate supplement, no mathematical repair to the stated identities is needed. A next substantive advance must establish a new arithmetic estimate in the missing range, rather than invert a zero normalization, delete a nonzero center, or drop the original prime-complement boundary.
