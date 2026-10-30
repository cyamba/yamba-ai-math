# Reviewed cofactor scope and repeated-label correction

29 October 2026. Registry role: Mathematician, GOLDBACH-COFACTORS-015, actual revision stage. I read the populated revise packet, the separate substantive review and the distinct experimenter's final output. The frozen statement, review and finite artifacts are unchanged. This revision performs no new experiment or source search. Usage is unknown.

The frozen statement SHA256 is `91bbf0074e34ef26d578a80b4ecf1644db2197748ca1070d38dc8c38686b0212`. The main review SHA256 is `250fee54d7d3e8dffad68fc86aeda699b09f874bbbf23913ac0c16adf54b66dd`. Its verdict supports both candidates in their stated narrow scope, with one P2 correction to the optional equal-label-deleted eigenvalue. The following text supplies that correction and makes the related support qualifications explicit.

## The P2 correction

The undeleted h=1 block has kernel 1 between all its configurations. With positive state measure mu_x its raw integral operator is rank one, and the constant vector has eigenvalue

    S1=sum_(x:h=1)mu_x.

The comparison on this block is m_arc times the raw operator, so the difference eigenvalue is `(1-m_arc)S1`. This assertion allows repeated labels and factorization multiplicities. It was supported by the main review and remains unchanged.

The frozen statement's optional formula after deleting all pairs with equal selected label must be read more narrowly:

**Corrected formula.** If the block consists of d basic vertices `(a,u)` with d distinct labels and the same positive weight w, then the equal-label-deleted operator has top eigenvalue `(d-1)w`, and its raw-minus-comparison top eigenvalue is `(1-m_arc)(d-1)w`.

On this basic h=1 space, u=N-a is fixed by the label, so one vertex per label is automatic. The matrix is w times the complete graph without loops. Its constant vector has eigenvalue `(d-1)w`; vectors orthogonal to the constant vector have eigenvalue `-w`. This is the precise scope of the optional d-1 formula. It is not a formula for the number of arbitrary `(a,m,n)` states.

For clarity, the correct general representation is a weighted multipartite block. Partition configurations into label clusters L_a, and put

    s_a=sum_(x in L_a)mu_x.

After equal-label deletion, all within-cluster entries vanish. The operator kills every vector whose weighted sum within each cluster is zero. In the orthonormal cluster basis `1_(L_a)/sqrt(s_a)`, its remaining matrix is

    C_ab=sqrt(s_a*s_b) for a!=b, and C_aa=0.                      (R1)

To prove the entry formula, apply the deleted integral operator to one basis vector: on another cluster its value is the weighted sum over the first cluster, namely sqrt(s_b). Taking the weighted inner product with the second normalized indicator gives sqrt(s_a*s_b). Consequently its eigenvalues depend on the cluster masses, not just the total number of configurations. The comparison difference on this protected block is exactly `(1-m_arc)C`.

The critic's actual finite witness is N=38, alpha=3/10, Y=3, with unit-weight states

    (a,m,n)=(3,5,7),(3,7,5),(5,3,11).

All have h=1. Their labels satisfy the rough cutoff exactly, since `3^10=59049>38^3=54872`, and all coordinates are units modulo 38. The two first configurations have label 3 and the third has label 5. Equal-label deletion therefore gives

    [[0,0,1],
     [0,0,1],
     [1,1,0]].

The cluster masses are 2 and 1, so (R1) is `[[0,sqrt(2)],[sqrt(2),0]]`. Its top eigenvalue and norm are sqrt(2), with squared norm 2. The raw-minus-comparison squared norm is `2(1-m_arc)^2`, rather than the erroneous `4(1-m_arc)^2` obtained by treating three configurations as three distinct labels. The separate experimenter reproduced this control before its one smoke and one final run. It corrects the optional deleted formula without changing the undeleted rank-one obstruction.

## Accepted connection and its support

**Proved with the stated distinct host-agent review:** retaining every raw equal-integer-cofactor edge does not bound the union of selected polynomial labels by local factor capacity. The N=16 four-label path is a statement about raw prime incidence without a single-dyad requirement. N=30, with labels 7,11,13,17, also fits one label window Y=5. The N=8 two-label control is outside the later z>2 convention. These distinctions remain explicit. The PNT averaging argument proves large blocks somewhere as N varies, not a prescribed-N prime lower bound.

The prime-incidence examples use a factor1 when written as Vaughan products. The separate N=222 product-box example has only its declared finite cutoff and rectangle support. None is an asymptotic factorable-Vaughan counterexample. The exact configuration-space norm statements are likewise not lower bounds for the accepted subpolynomial source operator.

The complete-pullback comparison, with unit labels a<N and positive products 0<u<N, preserves `c=(N-u)a^(-1) mod N`. Its integer-cofactor compression is exactly `m_arc*K`; its c=1 sector is exactly h=1. The associated undeleted normalized difference eigenvalue is 1-m_arc **when that block is nonempty**. An empty block cannot be normalized. In particular, restricting u to primes does not establish that the prime-supported block is nonempty at every N. On the full positive-u population, a nonempty selected label set supplies such a block independently of prime-pair counts. These ambient populations are not interchangeable.

The explicit larger-support layers `u=N(1+j)-a` and their comparison kernel retain the fractional states. Adding them requires a proved support extension with the actual coefficients; arbitrary added-layer vectors do not replace a factorable input. The positive raw square and the full comparison remain distinct objects. The protected-block observation is a precise obstruction to one proposed construction, not a universal parity impossibility claim.

## The nonzero center and harmonic dispersion remain scoped

The exact count vector A_h in the frozen statement is the **unweighted** genuine-divisor incidence on the unit, squarefree rough population. Its h=1 entry is the unknown count R_unit. For it,

    Z_rho^unit=-sum_h mu(h)*rho^(nu(h))*A_h,
    sum_h A_h^2=<A,diag(1/h)A>_h.

A general eta/f configuration input instead has its weighted fiber amplitude `C_h=sum_(x:h)mu_x*f(x)`, and the corresponding raw square is `sum_h|C_h|^2=<C,diag(1/h)C>_h`. It is not obtained by replacing that weighted vector by A. Neither raw square is the new centered dispersion norm.

The model gamma_h is an explicitly defined nonnegative single-prime intensity; some entries may be zero because the defining sum is empty. The classical PNT argument gives eventual strict positivity only where needed, namely `gamma_1=(1+o(1))*A_N`. It is not a joint prime-pair theorem. The three-node nonzero center reconstruction and bounded harmonic test mass were supported by the review, as was the weighted Cauchy reduction.

**Unverified:** the dispersion estimate D. Its h=1 summand already bounds `|R_unit-gamma_1|^2`, so D would imply the desired positive prime margin. It is not inferred from the harmonic mass bound, a rational toy center, or the marking lemma. Dividing normalized observables by the actual V_N retains its reciprocal cost. Removing h=1, choosing a zero center, or suppressing an empty prime-supported block would change the problem.

## Fixed marking lemma and independent evidence

**Proved at the reviewed written-argument assurance:** for one genuine prime-label group, fixed twist across chi, bounded marking coefficients, positive lower normalizer and polynomial marking scale, the fixed fourth-power representation bound and classwise character Cauchy give the bounded unnormalized eighth moment. Repetitions are allowed, their multiplicity is at most 24, and characters are evaluated at the product once. The derivative and one-spaced calculus argument then gives the logarithmic-power exceptional-count bound. Its support height is polynomial; no root-averaging or prime-distribution theorem at that height is used by this lemma.

The full normalizer may exceed 1; the proof requires its positive lower bound, not a memory-model mass restriction. Boundary dyads and inverse powers of any alternative small normalizer retain their stated costs. This remains a marking-component estimate. It does not prove a full polynomial-label energy transport, a centered operator contraction, a permissible roughness factorization, or D.

The distinct finite output reports one smoke and one bounded final run, with 35,906 and 1,156,448 exact checks and no failures. Final body runtime was 0.539671 seconds; its checker hash is `51a27ad91e31fec1023a01ec588d6064586440e15a56ba4b32dca328300067f4`. These saved outputs were inspected, not rerun in revision. Their domain includes the declared finite incidence, positive sector/compression, rank-one and repeated-label matrix cases. Center checks use a designated rational toy center rather than analytic gamma_h. Marking checks use finite complete characters and t=lambda=0; they do not computationally certify the continuous derivative or one-spaced argument.

Assurance is a complete author derivation with distinct host-agent substantive review and separate bounded finite reproduction. It is not proof-assistant verification, external peer review or a new audit of the PNT/Mertens proofs. No new experiment, mathematical helper execution or supplemental round occurred in this revision.

Polynomial-modulus root discrepancy, actual fractional-state coefficient linkage, polynomial roughness/Type I transport, D and the original prime margin remain open. Closest-work novelty and Goldbach are unestablished. The accepted output is an exact construction failure, a corrected local operator connection and a useful marking inequality, not an independently established breakthrough or a Goldbach proof.
