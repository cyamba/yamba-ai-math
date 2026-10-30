# COFACTORS-015 independent substantive review

29 October 2026. Registry Independent Critic. I read the actual populated counterexample packet, frozen statement, survey, accepted LABELS-005 construction and retuning limitations, and the actual PAIRING-011 comparison definition. I independently checked the new geometry, centers, weighted Cauchy reduction and fixed-order moment. Usage is unknown.

**Verdict:** the raw global-label invariant is **refuted** by the stated witnesses. The integer compression, protected positive-product h=1 block and its undeleted configuration-space norm are **supported**. Candidate 2's exact count/center identities, bounded harmonic test mass, conditional implication from D, and fixed-fourth-power marking lemma are **supported**. D itself is **unverified**, as the author states. One P2 scope clarification is needed for the optional equal-label-deleted eigenvalue when separate factorization states are used; it does not affect the undeleted obstruction or the marking lemma.

Assurance is a complete written-argument audit by a distinct host agent, not formal verification or external peer review. PNT and Mertens remain the stated classical background from the accepted LABELS-005 stage. No polynomial-label operator transport, actual dispersion estimate, full prime-energy extension, Goldbach theorem or novelty determination follows.

## Reviewed versions

| Input | SHA256 |
| --- | --- |
| frozen statement.md | 91bbf0074e34ef26d578a80b4ecf1644db2197748ca1070d38dc8c38686b0212 |
| actual counterexample packet | 300cfbc1445321970aa07e3a6063b63836be37881890557927802c0daa10d16f |
| survey.md | 3ffd07cfbd60b27cec4a650de4888fdcc4343e03563377e8e3ca1427752b27c0 |
| separate pre-mortem.md | 72521afa11ce08c0c7d2ef380eb2da69df2109917381b7f7bffb8fef5b8cbf93 |
| LABELS-005 revision.md | a68d9539081430fcacc79a2da11da3d8057bac21fde0216959ea048c02f4cfbf |
| LABELS-005 parameter-retuning.md | 522cd21ceeda38915d4f468e273f2e0dfbb9f86034108cdbe08643e0bd81115d |
| PAIRING-011 revision.md | 21a75c833070b1436e69d6951dec67aad602f47d061b4e307c3f069aaf7a4f51 |
| finite-results.json | 019cd9e6e0ed1fe006130ae8797bb543b28738e3f62f5283adbf8fa3dde1b11d |
| finite-check-result.json | 9f05bdcc7d4944b7d1a7ab7c73da486801e5ccaf09d2cd46e65708e41637073f |

The pre-mortem was separate framing, not execution of this main critic stage or acceptance of the then-unseen author proof. Frozen inputs were not edited.

## Candidate 1: actual raw paths and exact comparison

The transition rule retains every equality-of-integer-cofactor edge, so each h block is complete. At h=1 the N=16 vertices have distinct selected primes 3,5,11,13 and genuine unit prime complements. Each label exceeds N^alpha throughout the declared alpha interval, since its smallest value 3 exceeds N^(1/3). Four labels require at least three edges in an open walk and four in a closed walk, and the displayed complete block attains both. The small even-N prime-pair lists below 16 confirm the asserted minimum for four raw labels. This is a raw incidence assertion, without a single-dyadic-block requirement. The N=30 witness supplies a four-label path within the stated Y=5 label block. N=8 correctly illustrates the smaller one-edge failure but is explicitly outside the later z>2 convention.

The N=222 rectangular toy also checks directly: the four products are 55,65,85,95 and complements 167,157,137,127. The factors are units modulo 222 and exceed its toy sift cutoff. Neither this toy nor the prime-incidence examples satisfy the source's asymptotic Vaughan/sifting hypotheses. The statement preserves that distinction and makes no factorable-input norm claim from them.

The PNT pigeonhole argument proves unbounded raw block sizes somewhere as N varies. Removing primes below (2X)^alpha and equal pairs is lower order in the ordered prime-pair count. For distinct primes their endpoints are units of their sum, and the labels exceed N^alpha because N<=2X. The average over at most X even sums is unbounded. It gives no prescribed-N prime-pair lower bound.

For the finite configuration kernel, summing the N pullback branches produces exactly (2): their individual 1/N measures cancel their surviving branch sum N. Unit labels make the comparison preserve c=(N-u)a^(-1) modulo N. On integer cofactors, substituting u=N-ah and v=N-bk gives

`t=N(b-a)+ab(k-h)`.

The modular condition forces N|(k-h); positive products below N give 0<h,k<N, hence h=k. The surviving phase is zero. Since 0<u,v<N and a,b<=4Y imply |bu-av|<4NY, the stated psi plateau is valid on the entire support. Thus the integer compression is exactly m_arc K, not a newly small centered kernel.

The protected c=1 assertion uses both a<N and 0<u<N: two numbers N-u and a in (0,N) which are congruent modulo N are equal. This rules out fractional c=1 states on that domain. Its weighted raw block is rank one, with eigenvalue S1=sum mu_x, and the difference eigenvalue is (1-m_arc)S1. When S1>0, division by the raw block norm gives precisely 1-m_arc. The arc-cover estimate is O(L^(3A0)/Y), which tends to zero for fixed A0 and polynomial Y. An empty prime-supported block cannot be normalized; no positivity of that unknown block is inferred. On the full positive-u population a nonempty selected label set does supply it, independently of prime-pair counts.

For larger positive-product support, c=1 has the exact layers u=N(1+j)-a with j>=0. Substitution gives both the cutoff argument and the frequency bj-al in (4). If u<CN and a>C, then j<C<a, so the only integer cofactor layer is j=0; the other layers have negative, noninteger cofactors. Their comparison coefficients and support cannot be selected arbitrarily to replace an original input. This extension does not insert negative Mobius arguments into the original target.

## P2 finding: equal-label deletion and factorization multiplicities

**Target:** the optional formula `(1-m_arc)(d-1)mu_x` after deleting equal labels. **Issue:** it is exact in the basic (a,u) h=1 space, where each label gives one vertex. It does not hold for every optional separate (a,m,n) representation with repeated labels.

For a concrete positive-product example take N=38, alpha=3/10, Y=3, unit weights and the three states

`(a,m,n)=(3,5,7), (3,7,5), (5,3,11)`.

All have h=1, all coordinates are units modulo 38, and a>z because `3^10=59049>38^3=54872`; also z>2. Deleting equal-label pairs gives the matrix

`[[0,0,1],[0,0,1],[1,1,0]]`.

Its top eigenvalue is sqrt(2), not d-1=2. The comparison difference multiplies both by 1-m_arc. The constant vector is not an eigenvector after this deletion when label clusters have unequal sizes.

**Impact and repair:** no change to the undeleted rank-one obstruction, compression or positive-cofactor identities is needed. State that the optional deleted formula assumes one vertex per distinct label, or replace it by the appropriate weighted multipartite-block calculation when retaining factorization multiplicity. The original theorem's factorable-Vaughan-input exclusion must remain. This finite matrix does not refute any source operator estimate.

## Candidate 2: the nonzero center and the actual remaining obligation

For squarefree rough q=a h, selecting each genuine prime divisor once gives exactly mu(q)=-mu(h) and nu(q)-1=nu(h). The gcd(a,Nh)=1 condition prevents repetitions, and the h set retains h=1. It follows that (5) is the selected-divisor identity for the unnormalized unit observable. Omitted original prime values dividing N have at most a bounded profile times omega(N), which is o(A_N). Dividing a normalized observable by V_N retains its stated cost and does not change the count vector or D.

The displayed singular factor is correct for the primitive admissible forms a and N-ha: primes dividing h or N have one root and other odd primes have two; h is odd and coprime to even N. For a prime dividing h, its ratio to the base factor is (r-1)/(r-2). This identifies an explicit single-prime intensity, not a theorem that it approximates A_h. Some gamma_h may be zero if their defining sum is empty. Only gamma_1 needs eventual strict positivity.

The real-weight PNT argument for gamma_1 is sufficient. Trivially removing a<=z and the short endpoint N-a<=N/log^4 N costs o(N/log^2 N). On the rest log(N-a)=log N+O(log log N), while the remaining prime count is (1+o(1))N/log N; excluding prime divisors of N is negligible. Thus gamma_1=(1+o(1))A_N without a prime-pair theorem. The three-node identity (8) cancels the terms of degrees one and two in rho and reconstructs gamma_1 with its positive sign.

Every eligible one-prime or two-prime h has factors below N/z. Enlarging the distinct pair sum gives reciprocal mass at most `1+S_z+S_z^2/2`. The stated Mertens estimate is uniform on alpha in [3/10,1/3), so this bound is uniformly finite. Weighted Cauchy in the actual h-weighted norm gives (9) directly. For the unweighted incidence vector A its raw square is `sum_h A_h^2=<A,diag(1/h)A>_h`; general eta/f inputs use their corresponding weighted fiber vector. This identity does not equate the original square to the new dispersion norm.

D is a sufficient but unproved arithmetic estimate. Its h=1 term alone implies `|A_1-gamma_1|<=(1-sigma)gamma_1`, hence the advertised positive prime margin. This makes the boundary difficulty explicit: D already directly estimates the unknown prime-pair count. The stronger little-o dispersion would control the correctly centered signed tests, but neither version follows from the harmonic mass bound or from the marking moment. This review accepts the reduction and conditional implication only.

## Fixed-fourth-power polynomial-marking lemma

The coefficient calculation is valid with repetitions. Prime factorization gives at most 4! ordered representations of a degree-four product; the exact multiplicity is 4! divided by the repeated-prime factorials. Cauchy inside each such fiber and |psi|<=1 give (10). A fixed twist may vanish on some labels dividing k; this only reduces the bound. It remains fixed across chi, which is essential.

Exact character orthogonality modulo N followed by Cauchy within each residue class yields (11) with at most W/N+1 integers in a class. Since Y^4>=N, multiplication by phi(N) and the coefficient norm D0/Y^4 gives the claimed constant D0(4^4+1), including W>N. No distribution theorem at a polynomial modulus is hidden in this count. The derivative has coefficient log u times the old one, so its squared norm costs at most (log W)^2.

For one-spaced times at a fixed character, radius-one-half intervals have disjoint interiors. Integrating the identity for the derivative of |B^4|^2 gives the stated `I0+2 sqrt(I0 I1)` bound. Applying the two pointwise character bounds to these integrals proves (12), with the enlarged interval length 2T+2. The exceptional threshold contributes L^(8A_s). For T=L^B1 and Y<=N, log W=O(L), so the claimed logarithmic-power count follows. The same proof handles fixed-factor lower boundary blocks once Y^4>=N, and any small dyadic normalizer must retain its inverse powers.

This is an elementary marking-component estimate with four slots and polynomial support height. It neither bounds long-path label births nor supplies the changed arithmetic energy. The author correctly retains the polynomial prescribed-modulus budget, fractional support linkage, nonfactorable roughness and prime-boundary dispersion as missing inputs. The subpolynomial root and Type-I estimates cannot be extended to them by substitution. Novelty remains unknown.

## Finite evidence

The actual final finite output arrived before this review was frozen and was inspected. It reports one smoke and one bounded final run, with 35,906 and 1,156,448 checks respectively and no failures. Its checker SHA256 is `51a27ad91e31fec1023a01ec588d6064586440e15a56ba4b32dca328300067f4`. These are inspected saved results, not a rerun by this critic.

Coverage includes the declared N<=100 incidence domain, fixed N=8/16/30/222 witnesses, 1,133,221 positive-state sector pairs, 633 integer-cofactor pairs, exact larger-layer arguments and rational weighted rank-one modes. The separate experimenter reproduced the critic's N=38 repeated-label matrix control. Count/center reconstruction uses actual finite rough incidence but a designated rational toy center; it does not evaluate the analytic gamma_h. Thirty marking configurations use exact complete characters, Gaussian coefficients and t=lambda=0. Their repeated-prime, coefficient and residue-Cauchy tests do not certify the continuous derivative or one-spaced sampling argument.

The finite evidence is consistent with the scoped proof and the P2 correction. It cannot establish D, analytic gamma asymptotics, an asymptotic factorable-input norm obstruction, a polynomial-root extension, a prime margin, novelty or Goldbach.
