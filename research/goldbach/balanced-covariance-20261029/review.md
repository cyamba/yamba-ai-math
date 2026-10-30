# BALANCED023 independent challenge

29 October 2026. Actual Independent Critic challenge stage, one pair8 round, stage cost 2 declared proxy units.

**Verdict: incomplete.** The elementary identities and error lemmas checked below are supported by complete human-readable arguments. Neither permitted mechanism gives a useful signed covariance estimate. The proposed incomplete verdict is justified, but does not itself validate the subsidiary claims; those were checked separately. No contradiction to the eventual dispersion target is proved. Novelty remains unverified, and no full-goal completion decision is made here.

## Frozen inputs and assurance

The actual populated packet is `.runs/goldbach-balanced-023-manual-20261029/packets/challenge.json`, SHA256 `ce8495ed89a7705f31c921d6ba42c62e92d092c16aa4982e7145cf17cc270c40`. Its upstream result equals the actual `propose-result.json` as a parsed JSON object. The latter has SHA256 `ccf8d3094b012f84a4fed652d802c3105bf99f5b252342a985f45525ff5419e3` and passes `harness.runtime.validate_result`.

The reviewed `statement.md` has the assigned frozen SHA256 `ee40705ea259c3ff2593ddf26d7f3f5d483c0cae3493fd6561fbe4cf1c893fc8`. The brief, repository instructions, `audit-theorem` workflow, punctuation rule, CUBIC022 definitions and primary-input provenance were read. All nine files listed in that provenance were checked against their recorded hashes. The actual local Arneth Sections 10.2 and 10.3 were read, and page 17 was visually inspected. The local Koukoulopoulos printed-page-277 render was visually inspected for exact (26.1). These are inspections of the assigned source statements, not certification of the source's full mathematics. No new retrieval occurred.

The formal target is uniform over all sufficiently large even integers N, with the exact I, W, kappa, beta, F, Q and M_N of frozen Section 1:

    D_Q = sum_(integer q in Q) q |F(q)|^2 = o(M_N^2).

The source's open Hypothesis 8.2 and its stronger sufficient dispersion test are not imported hypotheses. Proof assurance below is independent human-readable reconstruction with the classical BV statement expressly imported. No formal proof checker or numerical experiment was run. Schema and hash checks are artifact checks, not mathematical evidence.

## Supported deductions, independently reconstructed

**Support and zero rows, proved.** On either branch, N/(3q)<r<=2N/(3q), so r>(1/3)N^(11/24)>y eventually. Both r and integer q exceed one, hence rq is composite. The atom would require rq=N/2 prime, so it vanishes. If (rq,N)>1, the wheel indicator is zero. A reflected prime m=N-rq must then divide N and satisfy N/3<=m<2N/3. For large N it is odd; the integer N/m is even and lies in (3/2,3], so it is two. That would make rq=m prime, a contradiction. Thus v_r(q)=0 on these indices. Each surviving row has (r,N)=1 and is y-rough. Since z<y eventually, (r,W)=1. Integer q sharing a factor with N also gives zero. The two beta branches remain disjoint, including repeated factors in alpha2.

**Four terms and local measures, proved as identities.** Expanding the square gives the exact coupled support K_rs^(ab), both cross-branch pairs and all four terms

    a_r a_s - kappa a_r chi_s - kappa chi_r a_s + kappa^2 chi_r chi_s.

Nothing licenses discarding either mixed term. The diagonal bound follows directly from at most O(N/q) inner indices and |v_r|=O(L^4): summing O(N L^8) over at most N^(13/24) integer q gives O(N^(37/24)L^8)=o(M_N^2). This is a small diagonal, not off-diagonal cancellation.

For live r,s and ell|W, r and s are invertible modulo ell. The forbidden roots Nr^(-1) and Ns^(-1) coincide exactly when ell|N(s-r). Under uniform integer residues, one or two residues are excluded, so the joint survival probability is 1-nu_ell/ell. The normalized joint factor is therefore ell/(ell-1) for a common root and ell(ell-2)/(ell-1)^2=1-1/(ell-1)^2 otherwise. Each normalized marginal has mean one. Subtracting one from the joint factor proves the single-prime signed covariance 1/(ell-1) or -1/(ell-1)^2. In particular ell=2 divides even N and is always in the common-root case. The global centered wheel covariance is the product of joint factors minus one, not the product of the single-prime covariances; the proposal does not make that mistaken substitution.

Under uniform unit residues, a root is zero when ell|N and excludes no unit; otherwise the nu_ell roots are nonzero and exclude nu_ell of ell-1 units. This gives exactly the proposal's different unit-residue probabilities. CRT multiplies these finite local probabilities. For the finite interval identity, expanding chi_r and chi_s over d,e|W gives compatible congruences precisely when (d,e)|N(s-r), and then one residue modulo [d,e]. This verifies (2.6). No approximation by complete periods, prime-prime correlation, or small lattice error follows from it.

**The switched relation and available BV bound, proved conditional only on imported BV.** Substituting m_1=N-rq and m_2=N-sq gives s m_1-r m_2=N(s-r). The full condition m_1=N modulo r is necessary and sufficient for integer q=(N-m_1)/r; using a weaker modulus would add indices. Equation (2.8) retains this condition and the second prime weight. On live rows the class N modulo r is reduced.

For a dyadic X<q<=2X, the supports have r,s=O(R), R=N/X. Require their full constant multiple of R to be at most sqrt(N)/L^(A+3), as the proposal does. Exact book (26.1) gives total maximal prime-count error O_A(N/L^(A+1)); partial summation against log gives total theta error O_A(N/L^A), with harmless lower-end constants. For each r, the cumulative discrepancy from the discrete progression reference r/phi(r) is O(Delta(r)+r/phi(r)). The additional lattice term accounts for integer endpoint rounding. Applying the discrete Abel identity to f(q)=q v_s(q) gives (2.10), including the actual nonsmooth second-prime weight. Its supremum is O(XL^4), and the available variation bound is O(X^2 L^4), since there are O(X) differences of size O(XL^4). There are O(R) possible s. Bounding the retained zero-one branch coefficients by one at this explicit estimation step gives

    X^2 R L^4 [N/L^A + R L^4]
      = O(N^2 X/L^(A-4) + N^2 L^8).

Thus (2.11) is a valid upper bound on the absolute progression-error sum for the covered dyadic portion. It is not a bound of the desired size. The calculation does not claim that every progression error actually attains this size.

**Prime-power replacement and equivalence, proved.** Let R_0(q)=F_Lambda(q)-F(q), using R_0 here to avoid confusing it with the dyadic R. The atom has already vanished and the model cancels, so R_0 is nonnegative and supported on reflected proper prime powers. There are O(sqrt(N)L) such powers below N: for every 2<=k<=L/log 2 there are at most N^(1/k)<=sqrt(N) possible bases. For each n=N-p^k in I, n<N. Six prime factors greater than y, counted with multiplicity, would have product greater than y^6=N. There are therefore at most five such factor slots. Every supported prime or rough semiprime divisor r is obtained by choosing one or two of those slots. At most 5+binom(5,2)=15 choices suffice as an overcount, including repeated factors; the stated constant twenty is valid. Each r fixes integer q=n/r. Hence sum_q R_0(q)=O(sqrt(N)L^2).

For fixed q, there are at most O(N/q) inner integers, each contributing at most L, so q R_0(q)=O(NL). Nonnegativity now gives

    sum_q q R_0(q)^2 <= [sup_q q R_0(q)] sum_q R_0(q)
                         = O(N^(3/2)L^3).

Because M_N is bounded below by a positive constant times N/L, both stated errors are little-o at the claimed scales. In the Hilbert norm ||G||^2=sum_q q|G(q)|^2, the reverse triangle inequality yields | ||F_Lambda||-||F|| |<=||R_0||=o(M_N). This proves both directions of (3.2), uniformly over even N. It does not imply that either norm is itself o(M_N).

**Signed divisor identity, proved as algebra.** Prime factorization proves log m=sum_(e|m) Lambda(e). Möbius inversion gives Lambda(m)=sum_(d|m) mu(d)log(m/d). Splitting at d<=H and d>H proves (3.3). In the latter sum set k=m/d. Its exact conditions are k|m and m/k>H. Since m<2N/3, k<2N/(3H); the opposite reflected endpoint and both beta branches remain in beta. The integer k=1 is included with log 1=0. The Möbius quotient retains its own squarefree or zero value. Thus (3.4) is exact without a coprimality restriction on k. Equation (3.5) is precisely the original dispersion obligation after the proved prime-power equivalence, not an estimate of its left side.

**Semiprime coefficients and q weight, proved as accounting.** For fixed B>0, eventually D<sqrt(N/3), hence q>D for every prime p<=q with pq in I. For distinct rough p<q, the only nonzero Möbius divisors are 1,p,q,pq; 1 is below D and pq has Phi(1)=0. With t=log p/log(pq), the coefficient is -1_(p>D)Phi(t)-Phi(1-t). Polynomial expansion gives Phi(t)+Phi(1-t)=1 and Phi(1-t)=3t^2-2t^3. This proves (4.1), including the lower case at p=D because h>D is strict. For p=q the divisor p^2 has Möbius value zero and p>D, leaving -Phi(1/2)=-1/2 with no doubling. This is the square's coefficient in the full long operator; the squarefree residual would omit the square and require its separate error ledger.

On prime q in Q the product bound forces p>y, and p<=q gives unique ordering. Equations (4.3) and (4.4) therefore have the correct weights, sign, support and square term. Weighted Cauchy uses sqrt(q)F_(2,w)(q) and 1/sqrt(q), so the enlarged energy weight really is q. For composite integer q this is only the specified enlargement with the extended coefficient formula, not an assertion of semiprime support.

## Prioritized substantive findings

1. **High severity, unverified: the genuine four-term covariance remains unbounded.** Target: the desired negligibility after (2.10), including its matching wheel reference terms. Concrete gap: the verified BV average is O(N^2 X/L^(A-4)+N^2 L^8), with X a fixed positive power of N. No fixed A makes that available bound o(N^2/L^2), and the r support can also reach (2/3)N^(13/24), beyond the imported BV range. Exact finite-wheel averages do not estimate the prime-prime term or the incomplete-period wheel sums. Impact: there is no useful signed estimate even on the covered portion. Repair or decisive proof obligation: establish a negligible actual second-prime-weighted discrepancy together with its correctly centered wheel terms on an explicitly stated dyadic support, or replace that step by another proved bound within the authorized mechanism. Merely replacing the variation by a smooth variation, applying prime-q local factors, or invoking BV above its cutoff would not repair it. This is a gap already acknowledged by the proposal, not a refutation of the eventual target.

2. **High severity, unverified: the quotient-Möbius route has no load-bearing cancellation inequality.** Target: (3.5). Concrete gap: (3.3)-(3.4) give an exact decomposition and bijective divisor switch, but no estimate of V_H against kappa B-S_H. The proved O(N^(3/2)L^3) correction removes only proper prime powers; it does not diminish the surviving prime correlation. Impact: this route does not establish a second independent signed gain or improve the covariance target. Repair or decisive proof obligation: prove the actual centered weighted norm in (3.5), or a specified useful signed consequence of (3.4), with the unchanged quotient, endpoints and both branches. The current BV input is about prime counts and supplies no such quotient-Möbius assertion.

3. **Medium severity, unverified: the pilot has no automatic weighted branchwise transfer.** Target: any use of hypothetical unweighted combined pilot control to bound the original even rough semiprime term. Concrete gap: F_1+F_2 can cancel without control of either signed branch. Within the prime branch, w_D is g(t)=3t^2-2t^3 below D and one above D, with a generally constant jump Phi(t_D) at D. Direct differentiation gives g'(p)=6t(1-t)log q/[p(log(pq))^2]. Discrete partial summation thus requires the actual prime-branch prefix sums and the cutoff value, with the square separately carrying weight 1/2. A final unweighted total gives none of these bounds for signed summands. Impact: even a future proof of the unweighted combined pilot would leave this transfer, complementary q ranges and the remaining long-operator sectors unresolved. Repair or decisive proof obligation: prove the weighted prime-branch energy in (4.4), or sufficient prefix estimates with all variation and endpoint terms, and retain the separate residual ledger. No abstract countermodel or finite witness is being asserted as a counterexample to the actual primes.

## Narrow defensible result and handoff

The supported result is a package of exact support, covariance, local-wheel, divisor and semiprime-weight identities, a negligible diagonal, a negligible prime-power replacement, and a valid but insufficient BV error bound. There is no supported useful covariance gain, weighted semiprime margin, fixed positive Goldbach gap or solution of Hypothesis 8.2. The narrowest next check is finding 1's actual weighted discrepancy on one specified balanced dyadic interval, with its reference terms; that is a proof obligation for an authorized continuation, not authorization for an extra round here.

This stage used only the assigned critic role. No supplement, additional agent, numerical helper, new retrieval, paid call, external message or publication was performed. Token and monetary usage are unknown. Frozen inputs and other contributors' files were preserved. Only `review.md` and `challenge-result.json` are owned outputs of this stage.
