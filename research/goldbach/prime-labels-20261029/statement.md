# Two constructive prime-label adaptations

29 October 2026. Registry role: Mathematician, `GOLDBACH-LABELS-005`. Input: the completed survey in the populated statement packet. This report constructs bounded-label reconstruction and external padding explicitly, then identifies the exact estimates that the inspected source does not supply. It derives several finite identities and bounds, but no new parity-sensitive estimate for actual primes. Separate review and finite algebra checks are pending. Goldbach and the active breakthrough objective remain open.

## Source scope and target

The inspected primary source is [Lue-Wang-Wu, arXiv:2610.20242v1](https://arxiv.org/html/2610.20242v1), particularly equations (2.12)-(2.17), Propositions 2.3, 4.2 and 4.5, equations (4.48)-(4.51), and the moment-transfer calculation (4.63)-(4.68). Inspection of these statements and parameter calculations does not validate the manuscript's full theorem or analytic source chain. Its stated shift is 2, its auxiliary groups are subpolynomial, and its proof chooses a sufficiently large fixed number of groups for the requested precision. None is a stated theorem for the moving Goldbach target and polynomial roughness.

For even N, fix alpha in [3/10,1/3), z=N^alpha, and count prime summands p with q=N-p>1 and P^-(q)>z. Such q has at most three prime factors, including multiplicity. Use U, F and H as in the preceding tranches, and A_N=mathfrak S(N)N/log^2N. The reviewed bound gives limsup H/A_N<=C*epsilon^2 when alpha=1/3-epsilon with epsilon fixed. A positive F margin larger than this is still missing.

Let nu(q) be the number of distinct prime factors, distinguished from Omega(q). The source uses distinct group counts. Ordinary mu(q) removes nonsquarefree inputs; lambda(q) counts multiplicity. All identities below keep those distinctions explicit.

## Attempt A: bounded genuine polynomial labels

### Support and a construction that repairs coverage

The original source groups lie between exp((log N)^a) and exp(2(log N)^a), with fixed a<1/5. For sufficiently large N every such prime is below z, so their divisor weight is zero on the entire target rough population. Relocating K disjoint required groups above z makes the weight zero whenever K*alpha>=1: a nonzero weight requires K distinct divisors, whose product exceeds N^(K*alpha)>=N. The equality case is excluded too because every selected prime strictly exceeds N^alpha. In the present range this excludes K>=4.

This support observation alone does not rule out bounded labels. Define one polynomial group

\[
\mathcal P_N=\{r\text{ prime}:z<r<N\},\quad
V_N=\sum_{r\in\mathcal P_N}\frac1r
       =\log(1/\alpha)+o(1)>0.
\]

It covers every prime factor of each admitted q. For 0<rho<1 put

\[
h_\rho(q)=\nu(q)\rho^{\nu(q)-1},\qquad
W_\rho(q)=h_\rho(q)/V_N.
\]

This has exactly the one-group algebraic form of the source weight, but its prime range is different and no source estimate is transferred by definition. For an empty group count define h=0; the admitted q>1 have nu>=1.

On squarefree q, the possible factor count k=Omega(q)=nu(q) is 1, 2 or 3. At rho=1/4,1/2,3/4 the profiles are respectively (1,1/2,3/16), (1,1,3/4), and (1,3/2,27/16). Exact interpolation gives

\[
3h_{1/4}(q)-3h_{1/2}(q)+h_{3/4}(q)
   =\mathbf1_{k=1}, \tag{A1}
\]

and

\[
\Phi(q):=\frac{17}{3}h_{1/4}(q)-\frac{25}{3}h_{1/2}(q)
                           +\frac{11}{3}h_{3/4}(q)
   =(k-2)^2=\mathbf1_{k\text{ odd}}. \tag{A2}
\]

Thus bounded genuine labels can reconstruct the relevant factor types exactly; they need not approximate every admitted q by a many-group average.

Define the actual signed counts

\[
Z_\rho(N)=\sum_{p,\ q=N-p>1,\ P^-(q)>z}\mu(q)h_\rho(q),
\]

where p is prime. Let R be the prime-complement count, E0 the squarefree semiprime count and H0 the squarefree triple count. Then exactly

\[
Z_\rho=-R+2\rho E_0-3\rho^2H_0. \tag{A3}
\]

The signed prime reconstruction is particularly simple:

\[
\boxed{R=-3Z_{1/4}+3Z_{1/2}-Z_{3/4}.} \tag{A4}
\]

It needs no repeated-factor correction, since mu kills nonsquarefree composites and every prime is squarefree. Its coefficient l1 cost is 7. Likewise the squarefree odd-factor count is

\[
F_0=-\frac{17}{3}Z_{1/4}+\frac{25}{3}Z_{1/2}
                              -\frac{11}{3}Z_{3/4}. \tag{A5}
\]

The l1 cost in (A5) is 53/3. These are identities, not estimates for the Z terms.

### Repeated factors and norm costs

For the bare unsigned Phi(nu), as opposed to its mu-weighted use, the full type table is:

| Complement type | Omega | nu | Phi(nu) | True odd indicator |
| --- | --- | --- | --- | --- |
| r | 1 | 1 | 1 | 1 |
| r^2 | 2 | 1 | 1 | 0 |
| r*s, r!=s | 2 | 2 | 0 | 0 |
| r^3 | 3 | 1 | 1 | 1 |
| r^2*s, r!=s | 3 | 2 | 0 | 1 |
| r*s*t, distinct | 3 | 3 | 1 | 1 |

Consequently the bare Phi sum equals F plus the prime-square complement count minus the distinct r^2*s complement count. In (A5) all nonsquarefree odd triples instead have to be added to obtain F. Neither formula silently identifies nu with Omega.

There is a uniform elementary bound for the entire exceptional population:

\[
Q_{\rm ns}(N):=\#\{p:q=N-p\text{ admitted and nonsquarefree}\}
 \le\sum_{r>z}\left\lfloor\frac{N}{r^2}\right\rfloor
 \le\frac{N}{z-1}=O(N^{1-\alpha})=o(A_N). \tag{A6}
\]

Here the sum can be enlarged from primes r to integers, and the roughness forces every repeated prime above z. This also bounds the difference between rough mu and lambda correlations by O(N^(1-alpha)). Thus their replacement is justified at the prime-pair scale here, without pretending they agree exactly on repeated factors.

The three h profiles have supremum norms at most 1, 1, and 27/16 on the admitted population. The coefficient-weighted supremum cost for the bare interpolation (A2) is at most

\[
17/3+25/3+(11/3)(27/16)=323/16.
\]

The W norms have the additional known factor 1/V_N, which remains bounded for fixed alpha. No factorial approximation error is present: the degree-three divisor expansion terminates on these factor types.

A useful one-weight approximation is also exact. Let B_mu be the rough mu sum, and let Y_rho=sum mu(q)^2*h_rho(q) over admitted prime summands. At rho=1/2,

\[
Z_{1/2}=B_\mu+H_0/4,\qquad
Y_{1/2}=U_0-H_0/4. \tag{A7}
\]

Here U0 is the squarefree rough count. The already reviewed H bound controls these deweighting errors by O(epsilon^2*A_N) in the fixed-epsilon limit. This repairs the weight-approximation part of the adaptation at bounded K. It does not bound the signed sum itself.

### Centering cannot be copied as zero

The exact cells in (A3) are the required starting point for any center. For example, the formal rough-type mean coefficients 1, c2(alpha), c3(alpha) would give

\[
b_\rho(\alpha)=-1+2\rho c_2(\alpha)-3\rho^2c_3(\alpha),
\quad c_2(\alpha)=\log((1-\alpha)/\alpha),
\]

with the classical nonnegative triple Buchstab coefficient c3. These describe the familiar averaged comparison, not a proved pointwise formula for Z_rho at the moving target. At the limiting cubic boundary c3 tends to zero and c2 tends to log 2, so even this reference center is not zero for general rho. Choosing a rho to cancel an average would not prove pointwise cancellation.

There is also a direct consistency test independent of the triple coefficient. If all three Z sums in (A4) had uniform estimates o(A_N), then R=o(A_N). But PNT gives a positive average prime-pair count of order X^2/log^2X over even N<=X; excluding q<=N^alpha changes it only by a lower-order contribution. Moreover sum_{even N<=X}mathfrak S(N)<=X, by expanding its nonnegative divisor product and summing multiples. Thus uniform o(A_N) would imply an averaged o(X^2/log^2X) count, a contradiction. One cannot copy simultaneous zero cancellation for these adapted weights.

A correctly centered quantitative target could instead ask for

\[
Z_\rho=b_\rho(\alpha)A_N+\mathcal E_\rho(N)
\quad(\rho=1/4,1/2,3/4),
\]

where the proposed centers obey -3*b_1/4+3*b_1/2-b_3/4=1 and each |mathcal E_rho|<=eta*A_N with eta<1/7. Then (A4) would give R>0. This implication is elementary; the estimates and their pointwise centers are **unproved**, not conclusions imported from LWW. No estimate for them has been obtained by reconstruction alone.

### The actual source estimates fail to transfer at this K

Expanding h_rho by the source's finite binomial identity gives terms counting one, two, and three distinct group divisors. The two-divisor terms already involve moduli r*s>N^(2alpha)>=N^(3/5), and the three-divisor terms involve moduli above N^(3alpha). Ordinary BV cannot evaluate these using its square-root range. The truncation at three gives exact algebra, but does not make those progression errors small. It is precisely an analytic, not a coverage, deficit.

There is an exact quotient boundary that an attempted replacement estimate must preserve. Expanding one selected genuine prime divisor gives

\[
Z_\rho(N)=-\sum_{r\in\mathcal P_N}
 \sum_{\substack{h\ge1,\ rh<N\\
 N-rh\text{ prime},\ P^-(rh)>z,\mu^2(rh)=1}}
                    \mu(h)\rho^{\nu(h)}. \tag{A8}
\]

For squarefree rh, mu(rh)=-mu(h) and nu(rh)=nu(h)+1, and selecting each prime factor once reproduces the original multiplicity nu(q). The component h=1 is exactly -R. The components with h prime and h a squarefree semiprime give the other two terms of (A3). Thus any long-quotient character-Mellin cancellation result whose variable must exceed a positive power of N leaves h=1 untouched. On a macroscopic q interval, this component has selected label r of size N, rather than a subpolynomial product Y. Dropping that boundary would drop the original prime-complement count itself. This is a structural diagnosis of the attempted adaptation, not a proof that every new boundary argument must fail.

The inspected source's dirty-edge argument gives a bound containing L^(1-0.005*K), with L=log N, before choosing K>200*(G+3) to obtain a desired edge saving L^(-G); see equations (4.48)-(4.51). With K<=3 that available bound supplies no decaying logarithmic factor. This is not a lower bound for the actual operator norm or a proof that a different small-K argument is impossible. It is the exact failure of this attempted substitution into the inspected proof.

There is a second explicit cost. The source takes J=floor(L^0.01) additional-list entries and moment order 2R comparable to L^(1/2). Its moment-to-pairing estimate still contains the factor (d0*Y)^(1/(2R)), made bounded there using log(d0*Y)=O_K(L^0.21). If every list prime is genuinely above N^alpha, then the complete product of K*(J+1) distinct list primes instead has logarithm at least K*(J+1)*alpha*L. The leftover factor is at least exp(c*K*alpha*L^0.51), so the substituted upper estimate cannot absorb it with any fixed logarithmic saving. Shortening genuine lists to fit Omega<=3 removes the source's growing-J dirty-edge saving and has not been justified by a replacement moment bound.

Finally the source's prime groups lie below its sift threshold Z=exp(L^0.24). This is used to identify auxiliary parts and prove primitive position vectors. Polynomial labels exceed Z, so the source's sifted coefficient support no longer guarantees those coprimality identities. For the reflected bilinear relation

\[
(N-mn)/a=(N-rs)/b
\]

the determinant condition is b*m*n-a*r*s=N*(b-a), rather than the fixed-shift coefficient in the source. Even small labels therefore do not preserve its small-determinant argument for primitive positions automatically. This moving-target condition requires a separate proof, not deletion of exceptional terms by assertion.

The strongest straightforward actual-prime bound remains of the full count scale: ordinary BV and a legal weakened upper sieve give limsup U/A_N<=4, as in the preceding switching calculation. Thus |Z_1/4| and |Z_1/2| are O(A_N), and |Z_3/4| is O(A_N) with its displayed norm factor. These absolute bounds have no required one-sided margin. Attempt A repairs exact coverage and deweighting but fails at the source's small-K, polynomial-height, and moving-target analytic estimates.

## Attempt B: externally pad the complement

Take the original small source groups, all below z for sufficiently large N, and a squarefree D made from t_i>=1 distinct primes in group i, with no other prime factors. Because q is z-rough, gcd(D,q)=1 automatically. Put T=sum_i t_i and

\[
C_D=\prod_i\frac{t_i\rho^{t_i-1}}{V_i}>0.
\]

Every group divisor count of Dq is exactly t_i, so the transfer formulas are

\[
\boxed{W(Dq)=C_D,\qquad
\mu(Dq)=(-1)^T\mu(q),\qquad
\lambda(Dq)=(-1)^T\lambda(q).} \tag{B1}
\]

The mu identity remains valid when q is nonsquarefree, since both sides then vanish. Consequently the padded signed correlation is exactly

\[
\sum_{p,q\text{ admitted}}\mu(Dq)W(Dq)
       =\mu(D)C_D\,B_\mu(N), \tag{B2}
\]

and likewise for lambda. Dividing by the nonzero scalar recovers the original unresolved correlation, not a new cancellation gain. The correct center in the padded coordinates must be multiplied by the same scalar; padding cannot turn a nonzero original rough bias into a justified zero center.

For any q-independent finite averaging coefficients c_D, the average of (B2) is M*B_mu, where M=sum_D c_D*mu(D)*C_D. If M is nonzero, division again returns B_mu. If M=0, the padded average vanishes identically and contains no information about B_mu; it cannot be normalized by zero. All lambda formulas have the same conclusion. A q-dependent choice would be a new arithmetic weight requiring its own proof.

### Normalization and forced collisions

If exactly one prime is placed in every group, C_D=product V_i^(-1), a known constant-scale factor at fixed K. But every selection of one required label from each padded group then selects the same product D. In the source's squared expression, the two selected products satisfy a=b=D and share all their primes. A step discarding shared-label terms as negligible would discard the entire padded mass. Its original shared-prime lemma is not a statement about these artificially forced divisors.

With t_i labels in group i, independent selections from that fixed group collide with probability exactly 1/t_i. The pertinent probability is not O(1/r) for a prime r: divisibility by every chosen prime has been forced. Taking t_i=J+1 may reduce that collision probability but introduces the inverse-normalizer cost

\[
\log(1/C_D)=K\{J|\log\rho|-\log(J+1)+O(1)\}
\]

when all groups have that count. For J asymptotic to L^0.01 this grows at order L^0.01 for fixed K,rho; the normalization exceeds every fixed power of log N. The source's bounded endpoint-multiplier hypotheses cannot simply ignore it. This is an additional obstruction to this particular padding transfer, not a no-go for every abstract auxiliary-list construction.

### The reflected linear form and ambient scale

Writing n=Dq gives n+D*p=D*N. As a polynomial in the original prime variable p, the padded complement is -D*p+D*N, whose coefficient and constant have gcd D>1. It is nonprimitive and always divisible by the prescribed labels. Removing that common divisor gives q=N-p, exactly the original primitive reflected form, with its moving constant N and negative slope. It does not give the source's fixed shift p+2.

As a sequence on n<=D*N, the prime variable is N-n/D and n is restricted to multiples of D. Its mass is the original prime-count mass, not the unrestricted prime mass at the enlarged ambient scale D*N. Its roughness condition is P^-(n/D)>z, not P^-(n)>z, which would be destroyed by the inserted small primes. A theorem at ambient size D*N with an unadjusted error can lose a factor D relative to the original target. Local density, residue, coefficient-size and primitive-position hypotheses must all be rebuilt before any moment theorem could apply.

These exact changes do not imply that the source theorem is false. They show why it has not been applied to this construction. Equations (B1)-(B2) prove that the padding operation alone supplies no new estimate; any gain must come from an additional actual-prime correlation theorem for the new restricted linear-form sequence, and peeling D shows the unresolved correlation it must address.

## Outcome, assurance, and remaining estimate

**Proved by the complete algebra above, pending separate review:** bounded one-group prime and odd-factor reconstructions with stated norm costs; the O(N^(1-alpha)) repeated-factor bound; the rho=1/2 deweighting identities; exact padding and averaging identities; forced-collision and normalization costs. The source parameter substitutions identify explicit failures of the inspected estimates, rather than merely restating an open hypothesis.

**Unproved:** a correctly centered, target-uniform one-sided polynomial-roughness bound for the adapted Z sums, a positive F margin beating H, or a bilinear/moment theorem that supplies either. The inspected manuscript does not state the needed bounded-K, polynomial-label, moving-target theorem, and its full original theorem remains unverified as a dependency here. No cancellation estimate was inferred from zero padding averages or an impossible zero-bias assumption.

This is a constructive adaptation audit, not a Goldbach proof, demonstrated breakthrough, or novelty claim. A next advance must replace the missing small-K/moving-target correlation estimate with a complete argument. Label insertion, interpolation, parameter renaming, or further finite identity checks cannot supply that analytic estimate by themselves.
