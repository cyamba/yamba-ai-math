# Polynomial cofactors, a protected prime block and a fixed marking moment

29 October 2026. Registry role: Mathematician, GOLDBACH-COFACTORS-015, author stage. Two bounded candidates, pending distinct review and the separate finite experimenter. No mathematical helper code was executed for this stage. TYPEI-013's independent finite stage was completed during the priority pause and its files are separate. Usage is unknown.

Candidate 1 refutes a precise global-label invariant and proves an exact obstruction to an integer-cofactor-only comparison. Candidate 2 proposes direct harmonic cofactor dispersion with an explicit nonzero single-prime center, and proves a fixed-order polynomial-marking large-value lemma. The dispersion estimate is unproved. No original prime margin, Goldbach proof, breakthrough or novelty is claimed.

The accepted LABELS-005 revision and parameter-retuning supplement remain dependencies. Their interpolation, scalar-padding identities and source-range failures are not rediscovered here. The PAIRING-011 comparison is used with its actual complete-pullback definition; no subpolynomial root or moment estimate is extended by substitution.

## Candidate 1: the exact transition rule and its failure

Let N be even, alpha in [3/10,1/3), z=N^alpha>2. A genuine rough squarefree complement q=N-p>1 has at most three prime factors. First retain the unit population (p,N)=1, which also gives (q,N)=1. At most omega(N) original prime values are omitted; positivity of the retained prime-pair count suffices for Goldbach.

A configuration is x=(a,p), with a a selected genuine prime divisor of q, and h(x)=(N-p)/a. Specify the transition before asserting an invariant:

    x -> y if and only if h(x)=h(y), with every such edge retained.   (R)

Its path-label set is the union of selected values a at visited vertices. This is the raw cofactor incidence, including h=1. Its blocks are complete, so local factor capacity does not bound this union.

**Refuted invariant.** At N=16 the four vertices (a,p)=(3,13),(5,11),(11,5),(13,3) have h=1 and unit coordinates. Their prime complements exceed N^alpha throughout the stated interval, because 3^3>16. Traversing them needs three edges; closing the walk needs four edges and has four labels. These lengths are minimal for open and closed walks visiting four different vertices. This is also the smallest even N with four prime-complement labels: for N=4,6,8,10,12,14, the elementary prime-pair lists have at most three labels even before unit removal. A bound by the local value nu(q)=1 already fails on one edge at N=8, with labels 3 and 5. That smaller raw-rule control does not satisfy the later convention z>2; the N=16 four-label counterexample does.

The supplied N=30 path with labels 7,11,13,17 and p=23,19,17,13 is another valid witness. Both are actual prime-incidence examples; expressing p=m*n requires m=1 and violates asymptotic Vaughan m,n>U. A separate finite product-box witness is N=222, m=5, n in {11,13,17,19}, a in {167,157,137,127}. Here N-m*n=a is prime, h=1, both factors are units modulo 222, m is in [5,10), n in [11,22), and all factors exceed the explicit sift cutoff 4. The labels exceed 222^(1/3). This verifies the combinatorial failure on that product-box domain, not the source's asymptotic band/sifting regime.

Nor are raw prime-block sizes bounded by any absolute constant as N varies. By classical PNT, ordered pairs of odd primes in ((2X)^alpha,X] number asymptotically X^2/log^2 X. Their sums occupy at most X even N<=2X. Discard equal pairs, costing O(pi(X)); all remaining endpoints are units of their sum. Some N therefore has unboundedly many labels, all exceeding N^alpha. This is the classical averaged prime-pair fact already used in LABELS-005, not pointwise Goldbach. A rule allowing only previously seen labels deletes actual raw edges. At h=1, keeping only the two diagonal terms changes a two-unit-coefficient square from 4 to 2.

### Exact state, measure and full comparison

Fix Y>=z, selected primes A contained in [Y,4Y] intersect (z,N), each coprime to N, positive weights eta_a, and V>0. A state x=(a,u) has a in A and 0<u<N in any specified product support. Its measure is mu_x=eta_a/V. Factorization multiplicities may instead be represented by separate (a,m,n) states with u=m*n. Define rational lambda_x=(N-u)/a and

    K(x,y)=1_(lambda_x=lambda_y is a positive integer),
    t(x,y)=b*u-a*v,  x=(a,u), y=(b,v).

Use the quadratic convention

    Q_K(f)=sum_(x,y)mu_x*mu_y*f(x)*conj(f(y))*K(x,y)
          =sum_(h>=1)|sum_(x:lambda_x=h)mu_x*f(x)|^2.               (1)

Thus f(a,m,n)=alpha_m*beta_n recovers the actual positive raw square, retaining both integer divisibilities. On the unrestricted selected-label/product support let

    J(x,y)=Psi(t/(NY))*integral_(theta:N*theta in M1)
                          e(theta*(t-N*(b-a))) dtheta,

where Psi is real even and 1 on [-4,4]. The complete pullback gives exactly

    J(x,y)=1_(N|t)*Psi(t/(NY))
                    *integral_M1 e(phi*(t/N-b+a)) dphi.            (2)

Write m_arc=|M1|. The kernel is Hermitian. There is no extra 1/N. Indeed each branch has measure 1/N and the surviving branch sum has value N. For positive products and a,b<=4Y, the plateau is 1 on this whole support. These are definitions and exact identities, not a polynomial-label saving.

**Proved integer-compression identity, pending review.** If x,y have integer cofactors h,k, then

    t=N*(b-a)+a*b*(k-h).

Since gcd(ab,N)=1, (2) forces N|(k-h). Also 0<h,k<N. Therefore k=h, the phase vanishes, and, with I the integer-cofactor states,

    1_I J 1_I = m_arc*K.                                         (3)

Restricting the comparison to actual integer cofactors changes the unrestricted comparison; the raw rank-one block has not become a small centered block.

There is a stronger protected boundary. The modular cofactor c(x)=(N-u)*a^(-1) mod N is preserved by (2). Since 0<N-u,a<N, its sector c=1 is exactly N-u=a, hence h=1. It contains no fractional-cofactor states on this positive-product support and is invariant for both kernels. On it J=m_arc*K. In the weighted counting Hilbert space the constant block vector has raw eigenvalue S1=sum_(h=1)mu_x and difference eigenvalue (1-m_arc)*S1. Normalizing this raw block to norm1 leaves difference norm exactly1-m_arc. The elementary arc-cover bound m_arc=O(L^(3A0)/Y) tends to zero for polynomial Y. If equal labels a=b are deleted, an equal-weight d-vertex block has eigenvalue (1-m_arc)*(d-1)*mu_x instead, so the distinct-label path still matters.

This is a norm statement for this explicit configuration space. A vector restricted to a+u=N need not factor as a permissible Vaughan coefficient array. It is not a norm lower bound for the different accepted subpolynomial operator, or an impossibility theorem for every corrected mechanism. If u is restricted to primes, the block size is the unknown prime-pair count. If all positive u are allowed, the block exists independently of that count; these populations are not exchanged.

For larger product support the c=1 sector has the exact layers u=N*(1+j)-a, j>=0. If u<CN and a>C, only j=0 has an integer cofactor, because lambda=1-N*j/a, gcd(a,N)=1 and 0<=j<a. For x=(a,j), y=(b,l), the comparison entry is

    Psi((b*(1+j)-a*(1+l))/Y)
                       *integral_M1 e(phi*(b*j-a*l)) dphi.         (4)

The j>=1 layers have negative N-u and generally fractional lambda. They are auxiliary comparison states, never negative Mobius arguments in the original target. Introducing them requires an actual support extension with linked coefficients. An arbitrarily chosen vector in a new layer cannot replace the original input. Equations (3)-(4) identify the first obstruction without inventing a bounded global birth rule.

## Candidate 2: harmonic dispersion and a fixed marking moment

This corrected direction uses direct cofactor dispersion with a nonzero center, rather than a long path with a falsely bounded union of labels. Its algebraic reduction and marking lemma are proved below. The original-target dispersion estimate is explicitly unverified.

### Prime-sensitive center and bounded harmonic test mass

Let H_N consist of squarefree h>=1, coprime to N, with all prime factors>z, at most two factors, and h<N/z; include h=1. Define exact unit counts

    A_h=#{a prime>z : a*h<=N-2, (a,N*h)=1,
                         N-a*h is prime>1}.

Every record has rough squarefree q=a*h. In particular A_1=R_unit. Selecting each genuine prime factor once proves the unnormalized LABELS-005 observable identity

    Z_rho^unit=-sum_(h in H_N)mu(h)*rho^(nu(h))*A_h.                (5)

The omitted p|N terms have a bounded profile times omega(N)=o(A_N), where A_N=S(N)N/log^2 N and S(N) is the Goldbach singular series from LABELS-005. They do not remove the h=1 atom or invalidate positivity obtained from R_unit.

For the normalized one-group weight W_rho=nu*rho^(nu-1)/V_N, divide the signed observables and their centers by V_N. Counts A_h and the dispersion Delta_N below remain unnormalized; the explicit observable cost is 1/V_N.

For h in H_N set

    S_h(N)=S(N)*product_(r|h)(r-1)/(r-2),
    gamma_h=S_h(N)*sum_(a prime>z, a*h<=N-2, (a,N*h)=1)
                                          1/log(N-a*h).          (6)

This is a computable positive single-prime intensity, not a proved approximation to A_h. It contains no second primality indicator. The local singular factor is exactly the product for the primitive admissible forms a and N-h*a: primes dividing h or N have one root and other odd primes have two. Exclusions a|h are explicit. Classical PNT gives

    gamma_1=(1+o(1))*S(N)N/log^2 N=(1+o(1))*A_N.                  (7)

To check the real weight in (7), remove a<=z and N-a<=N/log^4 N by trivial counts. The latter contribution is at most N/(log^4 N*log2). On the rest log(N-a)=log N+O(log log N), and removing primes a|N costs O(omega(N)). PNT then yields (7) without a prime-pair theorem.

Define G_rho=-sum_h mu(h)*rho^(nu(h))*gamma_h. Since nu(h) is0,1 or2,

    -3*G_(1/4)+3*G_(1/2)-G_(3/4)=gamma_1.                        (8)

These centers have a positive prime reconstruction, rather than simultaneous zero centers.

Use ell^2(H_N,h) with squared norm sum_h h*|v_h|^2. With S_z=sum_(z<r<N/z,r prime)1/r and C_N=1+S_z+S_z^2/2,

    sum_(h in H_N)1/h<=C_N,
    |Z_rho^unit-G_rho|^2<=C_N*Delta_N,
    Delta_N=sum_(h in H_N)h*|A_h-gamma_h|^2.                       (9)

The first inequality enlarges the one-prime reciprocal sum and the distinct two-prime sum. The second is weighted Cauchy, since |mu(h)*rho^nu(h)|<=1. Mertens gives S_z=log((1-alpha)/alpha)+O(1/log N), uniformly here, so C_N is bounded. The unit mass at h=1 is retained. The original raw square is still exactly <A,diag(1/h)A>_h, not the new weighted norm; no original quadratic form is silently changed.

**Unverified analytic obligation D.** For some fixed sigma in (0,1), prove pointwise for all sufficiently large even N in the original target domain that

    Delta_N<=(1-sigma)^2*gamma_1^2.                               (D)

It would give A_1>=sigma*gamma_1>0, because h=1 is one summand. The stronger Delta_N=o(A_N^2) would give all three correctly centered signed bounds through (9). Neither is established. In particular D already controls the unknown prime boundary; inferring it from bulk mixing or the marking lemma would be circular. The proved connection is bounded harmonic test mass and an explicit nonzero center, not a proof of D. This is not scalar external padding.

### Proved polynomial-marking large-value lemma

Let Y in[N^alpha,N], choose any prime subset A_Y of[Y,4Y] whose labels are units modulo N, and take V>=v_->0 and |eta_a|<=C_eta. Fix a Dirichlet character psi modulo kN and real lambda. For chi modulo N put

    c_a=eta_a*e(-lambda*a/Y)/(Y*V),
    B_(chi*psi)(t)=sum_(a in A_Y)c_a*chi(a)*psi(a)*a^(it).

The twist psi is fixed across chi. Let C0=C_eta/v_-, C_sq=4*C0^2 and D0=24*C_sq^4. At most 4Y integer labels occur, so sum_a|c_a|^2<=C_sq/Y. The fourth power has coefficients d_u satisfying

    u<=W=(4Y)^4,
    sum_u|d_u|^2<=24*(sum_a|c_a|^2)^4<=D0/Y^4.                    (10)

Prime factorization gives at most 4!=24 ordered representations of u, including repetitions: the exact number is 4!/product_r multiplicity(r)!. Character evaluation occurs once at u, not at its fourth power. Complete multiplicativity of the fixed twist and positive Cauchy give (10).

Since 4alpha>1, Y^4>=N. Exact character orthogonality and Cauchy within each residue class, containing at most W/N+1 integers, imply uniformly in t,lambda

    sum_(chi mod N)|B_(chi*psi)(t)|^8
      <=phi(N)*(W/N+1)*sum_u|d_u|^2
      <=D0*(4^4+1)=:C_*.                                        (11)

This remains valid when W>N; no prime-distribution theorem is used at W. For F_chi=B_(chi*psi)^4 its derivative coefficients are i*log(u)*d_u, so the analogous bound for sum_chi|F'_chi|^2 has the extra factor(log W)^2.

Let P be any family (chi,t), |t|<=T, one-spaced when chi agrees. Disjoint radius-one-half intervals and the derivative identity for |F_chi|^2 give sum_P|F_chi(t)|^2<=I0+2*sqrt(I0*I1), with summed integrals of |F|^2 and |F'|^2 on[-T-1,T+1]. Apply (11) pointwise to both integrals. For E contained in P with |B|>L^(-A_s),

    |E|<=C_*(2T+2)*(1+2*log W)*L^(8A_s).                         (12)

For T=L^B1 this is O(L^(8A_s+B1+1)), since log W=O(L). This is a proved polynomial inequality, pending review, not an actual-prime distribution theorem. It replaces the subpolynomial regime's subexponential exceptional-count bound by a fixed logarithmic power for this marking component. No actual norm or prime-margin improvement follows automatically.

For genuine labels the normalizer may be the full mass V_N=sum_(z<a<N,(a,N)=1)1/a, which LABELS-005 records tends to log(1/alpha)>0. Each dyad then meets the stated lower bound on V. There are O(log N) dyads, and their smooth-partition costs remain. A boundary block with Y>=c*z for a fixed c>0 also has Y^4>=N eventually, because 4alpha-1>=1/5; the same proof then applies after that fixed threshold. Thus a smooth partition's lowest fixed-factor boundary blocks are not silently dropped. If a single-dyad reciprocal mass is used instead, its inverse powers enter C0 and cannot be discarded.

### Exact budget and remaining support obstruction

The fourth-power proof has four marking slots and at most eight slots in its squared-coefficient argument. Orthogonality in (11) is exact, with height W<=4^4*N^4 and no CRT discrepancy error. It does not assert bounded label births along a long operator path.

A direct quadratic expansion of Delta_N retains two selected labels at a time and their common integer h. A dyadic pair may require rad(a*b)<=16Y^2; globally a*b<=N^2/h^2. Encoding the at most two factors of h as prescriptions adds them explicitly. These polynomial ranges already exceed the accepted exp(O(L^0.98)) root input. No such discrepancy estimate is supplied. A hypothetical 2R-edge raw path can still contain 2R different selected labels besides the factors of h and require height h*(4Y)^(2R). The failed global-three inference is not reused.

The new analytic task is D, or another explicitly sufficient correctly centered prime-boundary estimate, with the exact comparison (2)-(4), fractional states and all coefficients retained. The marking lemma controls one large-value component only. Polynomial roughness of N-m*n is not a product of a coefficient in m and one in n, so it cannot be inserted into ENERGY-012's arithmetic arrays by assertion. TYPEI-013's finite Taylor moduli likewise stop being subpolynomial when its small bands are replaced by genuine labels and can contain the prime-boundary main term. Neither missing interface follows from (12).

## Assurance and next check

The proved claims are the specified raw-path failure, comparison compression and protected block, its stated configuration-space eigenvalue, the nonzero-center algebra and harmonic Cauchy reduction, and the fixed-fourth-power marking bound. These have complete author arguments using elementary algebra, exact character orthogonality, positive Cauchy, factorization, calculus, and the classical PNT/Mertens background already present in LABELS-005. They await distinct semantic review and finite reproduction. No formal checker, external peer review, new source-wide theorem or novelty check was performed.

Small decisive falsifiers are the N=8/16/30 raw paths with their stated domains, an integer positive-state pair contradicting (3), a fractional positive c=1 state with a<N, or a repeated-prime fourth-power coefficient violating 24. The reviewer should check support versus factorable Vaughan input, normalizer V and the distinction between (12) and D. A finite null search would not establish D. The original polynomial-rough prime margin and Goldbach remain open; no independently checked breakthrough is asserted.
