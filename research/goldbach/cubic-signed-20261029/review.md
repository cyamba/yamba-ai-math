# CUBIC022 independent mathematical challenge

29 October 2026. Actual fresh Independent Critic, challenge stage, one pair round.

**Verdict: incomplete for the requested constant gap.** The two sector deductions in the frozen proposal are supported by the arguments below, with classical maximal Bombieri-Vinogradov (BV) expressly imported for Claim 1. I found no false estimate in Claims 1 or 2, the rough squareful error, or the exact residual partition. These results do not establish a fixed positive delta, a Goldbach theorem, or an improvement on powers of two. Novelty remains unverified.

Assurance is independent human-readable mathematical review, without proof-assistant certification. A distinct critic identity does not imply statistically independent model errors. No numerical search, new inference supplement, source-wide semantic certification, publication, external message or full-goal completion is part of this stage. Token and monetary usage are unknown. Declared scope remains the eight-unit propose/challenge/revise pair plus two root primary-access units, ten total.

## Frozen assignment and source scope

The actual populated challenge packet was read, including the exact role, brief, output contract and upstream proposal. The reviewed proposal is `statement.md`, SHA256 `9f385113df4b561399311ece472e41affd989ff187a93bdbec66a8d1cccffa5a`; it was not edited by the critic. Definitions are those of its Section 1: even N, L=log N, I=(N/3,2N/3], y=N^(1/6), z=L^4, D=N^(1/2)L^(-B), the complete radical wheel W, its actual prefactor kappa, the reflected-prime weight, and the correction atom.

The local Arneth text passages (7.1)-(8.4) and the supplied page 7 and page 13 renders were inspected. They retain integer k, k=1 and nonrough products, and explicitly leave Hypothesis 8.2 unproved. The primary-input/provenance record preserves the wider root inspection of pages 6, 7, 12, 13 and 17; that root inspection is not represented as a fresh critic inspection of every source page. The classical BV page 277 render was directly inspected: (26.1) has the maximal endpoint and reduced-class sum O_A(x/(log x)^(A+1)), for Q <= sqrt(x)/(log x)^(A+3). Its theorem is imported; this review does not reproduce its classical proof. No source comparison asymptotic or conditional Goldbach implication is used to infer a missing sign.

## One prioritized finding

**F1, critical missing estimate for the full objective; status: unverified.** The target is statement (21), a fixed-delta lower bound, uniform in every sufficiently large even N, for R_nr + R_even + R_outer,odd. The proposal proves no such inequality. Its only general remaining-range bound is O(N L^5), which supplies only a lower bound of the form -C N L^5, rather than the required specified constant below 3/4 times M_N. This is an evidence gap, not a counterexample to the actual-prime inequality and not a refutation of either sector deduction. The precise impact is that the complete requested one-sided gain remains unproved. A falsifiable repair must prove an estimate for these actual three residual operators, with the same wheel, atom, endpoints, weights and all-large-even-N quantifier, strong enough to give (21). A weaker bounded next check is the even rough semiprime sector together with its outer terms; success there alone would still leave the other residuals.

The pointwise obstruction cited by the author is valid. For distinct rough primes p,q with D<p,q<n/D and n=pq, the central set contains just p and q. Hence T(n)=-Phi(log p/log n)-Phi(log q/log n)=-1 exactly. This situation occurs for arbitrarily large admissible even ambient N: take comparable distinct primes and N=2pq-2. Then n is in I, is y-rough, and both inequalities hold eventually for every fixed B>0. This refutes an extension of coefficient suppression to every even rough central product. It does not refute a weighted assertion about the actual u(n), for which this argument supplies no sign.

## Supported deduction 1: tiny-prime product sector

**Status: proved relative to the imported classical BV theorem.** The quantifier is fixed B>=8 and every sufficiently large even N. The asserted conclusion is H_{<=w}=o(M_N), with w=floor(log L/(4 log log L)), G=product_(p<=w) p, and no restriction to squarefree products n.

For squarefree g|G, g>1, and g|n, every divisor h with nonzero mu(h) is uniquely ed with e|g, (d,g)=1. Its large-prime part is d_{>y}, even when n has repeated prime factors. The inner coefficient is sum_(e|g) mu(e) 1_(ed>D). It is zero for d<=D/g and d>D; at d=D it retains the e>1 terms, while at d=D/g none is retained. Therefore the exact surviving support is D/g<d<=D. The progression condition is g d|n, so m=gd, not ed. It follows that

    H_g = sum_(D<m<=gD, g|m, (m/g,g)=1) lambda_g(m) U_m,
    |lambda_g(m)| <= tau(g).

Zero coefficients can be included for nonsquarefree m; the nonzero ones have squarefree m because mu(m/g) is nonzero and (m/g,g)=1. For g=p prime, lambda_p(m)=mu(m) on the shell. No product, multiplicity or k=1 term is lost.

Rows with (m,N)>1 vanish exactly. To see the only possible prime exception, if p=N-n is prime and divides N, the central interval makes N/p an integer between 3/2 and 3. For large even N its only possible value is 2: the value 3 would force N=3p even and hence p=2. The correction atom cancels the value 2. The wheel term also vanishes on these rows. On coprime rows the non-atomic model density is exactly

    g_b(m)=(1/m) product_(p|(m,W)) (1-1/p)^(-1)
          =(1/phi(m)) product_(p|m, p not|W) (1-1/p).

Thus the author does not replace the actual model by an incorrect progression density. The squarefree reciprocal-totient sum is O(log(2x)): expand r/phi(r)=sum_(e|r) mu(e)^2/phi(e), then use convergence of sum_e mu(e)^2/(e phi(e)). Consequently sum_(m<=Q,p|m) mu(m)^2/phi(m)=O(L/p), and the summed density mismatch is O(L sum_(p>z) p^(-2))=O(L^(-3)). Multiplication by the interval length costs O(N/L^3).

For completeness, the model truncation is within its asserted elementary range. Adjacent Bonferroni orders K~L/(16 log L) for p<=z retain squarefree products at most z^(K+1)=N^(1/4+o(1)), with at most that many products. The Bernoulli main-density remainder is bounded by (sum_(p<=z) 1/p)^(K+1)/(K+1)! = N^(-1/16+o(1)). Apply the bounds to the positive count with the large prime divisors F of N already excluded, then expand the F-filter. Since 2^omega(F)=N^o(1), its exact expansion only multiplies the lattice error by N^o(1). Each compatible congruence has at most one lattice error. Multiplication by kappa<=O(L^4) is absorbed in the power errors. This proves the asserted interval error

    O((N/m) N^(-1/16+o(1)) + N^(1/4+o(1))).

Summing over m<=Q costs N^(15/16+o(1))+N^(3/4+o(1)). BV with A=4 supplies O(N/L^4) for the prime discrepancy. On coprime rows its reduced residue is exactly N mod m. Reflection and partial summation preserve the coupled interval: the polynomial weight is bounded in [0,1] and has variation at most one. The atom has at most its m=1 contribution among coprime rows, of size O(L). This verifies (5), including all errors used in it.

Finally G<=w!<=L^(1/4), Q=GD<=sqrt(N)L^(-31/4)<=sqrt(N)L^(-7) when B>=8. Product inclusion-exclusion has total coefficient cost sum_(g|G) tau(g)=3^omega(G)<=3^w=L^o(1). Therefore

    |H_{<=w}| << N/L^(3-o(1))
                  + N^(15/16+o(1)) + N^(3/4+o(1)) = o(M_N),

using S(N)>>1. An extension to a prime p near y would instead expose pD near N^(2/3)L^(-B); the imported BV range does not justify it. The remaining nonrough interval is correctly retained.

## Supported deduction 2: odd rough central strip

**Status: proved by the elementary argument, for every fixed B>0 and sufficiently large even N.** On squarefree y-rough n, h_{>y}=h and mu(n/h)=mu(n)mu(h). The open central set D<h<n/D is invariant under h -> n/h once D^2<n. Its complementary long outer set includes equality h=n/D, so d=n/h<=D there. The exact average under the involution is

    T(n)=(1/2) sum_(central h) mu(h)
                     [Phi(t_h)+mu(n)Phi(1-t_h)].

For mu(n)=-1 the bracket is 2Phi(t_h)-1. There are at most 32 divisors, because six factors greater than N^(1/6) have product greater than N. With c_n=log D/log n, the derivative bound |Phi'|<=3/2 gives

    |T(n)| <= 48(1/2-c_n) = O_B(log L/L).

All endpoints and the logarithmic loss have the stated direction. This coefficient bound alone would be insufficient with a crude O(N L^4) mass; the proposal supplies a valid bound for the actual mass.

Here are the load-bearing sieve details for that mass. Take q=exp(L/(log L)^2) and even K=2 floor((log L)^2/32). Then z<q<y eventually and q^K<=N^(1/16). Upper Bonferroni at this even order is valid for the positive actual and model counts. If nu_p is the number of excluded residues, nu_p<=2. The total lattice error is at most sum_(e<=q^K) 2^omega(e)<=sum_(e<=q^K) tau(e)=N^(1/16+o(1)). The difference of the truncated main density from the full product is at most

    (sum_(p<=q) nu_p/p)^(K+1)/(K+1)! <<_J L^(-J)

for every fixed J. The elementary Chebyshev bound from central binomial coefficients yields sum_(p<=q) 1/p=O(log log q)=O(log L), sufficient for this tail. The harmonic-series expansion gives P_q^(-1)>=sum_(m<=q)1/m, hence P_q<<1/log q, without a PNT input.

For rough n and prime N-n in the central interval, both numbers avoid primes <=q. There is one excluded residue when p|N and two otherwise. Their local product, including p=2, is bounded by O(S(N) P_q^2). Missing prime divisors of N above q only reduce its ratio to the complete positive singular series. Multiplication by the actual theta weight costs at most L. This gives O(S(N)N(log L)^4/L), with the smaller errors in (15).

For the model upper bound, dropping only the filter for p|N above z is legitimate because the remaining count is positive; its original prefactor kappa is retained. The retained root product is exactly P_q V_N(z). Direct factor multiplication gives

    kappa V_N(z)
      = S(N) product_(p>z,p not|N) (1-(p-1)^(-2))^(-1)
      << S(N).

In particular a divisor p|N above z contributes p/(p-1) on both sides; it has not disappeared. For p<=z,p not|N, the two forbidden roots give (1-1/p)(1-1/(p-1)); for p|N they coincide. These are the correct mixed densities, not products of two independently imposed sieves. Kappa multiplies the tail and lattice errors only, with kappa<<L^4, giving (17). The atom costs at most L. Combining these positive bounds gives (12) for the actual |u|. Multiplication by O_B(log L/L) proves

    E_odd = O_B(S(N)N(log L)^5/L^2 + log L) = o(M_N).

## Exact remainder and error ledger

**Status: proved as a support identity and coarse bound.** On rough squareful n, at most five prime factors with multiplicity imply |C_D(n)|<=32. The number of these n is at most N sum_(p>y) p^(-2)=O(N^(5/6)); |u|<<L^4 gives the claimed entire long contribution O(N^(5/6)L^4)=o(M_N). This is a separate long-operator bound; it does not silently validate the full-minorant removal in source (8.3).

Every n in I belongs to exactly one of: a tiny-prime product; a remaining nonrough product w<P^-(n)<=y; a rough squareful product; a rough squarefree even product; or a rough squarefree odd product. The last sector splits into its open central and closed outer divisor sets. Complementing the outer divisors gives exactly the author's R_outer,odd, using Phi(1-t)=1-Phi(t). Thus (19) follows without overlap or omitted endpoints. All nonrough squareful products remain in R_nr unless already in the tiny-prime sector. The k=1 term is present: its rough weight Phi(1) is truly zero, whereas the nonrough k=1 weight generally is not zero and remains included. The coarse residual estimate follows from |u|<<L^4, 0<=Phi<=1 and sum_(n<=N)tau(n)<<N log N. It cannot resolve F1.

The narrowest defensible conclusion is the three negligible terms in (19), with the exact three residuals still open. No claimed estimate of the frozen proposal is refuted in this review. The even central coefficient suppression extension described in F1 is refuted algebraically, and is already disclaimed by the author.

## Frozen input hashes

SHA256 hashes checked against the actual local files:

| Input | SHA256 |
| --- | --- |
| statement.md | 9f385113df4b561399311ece472e41affd989ff187a93bdbec66a8d1cccffa5a |
| .runs/goldbach-cubic-022-manual-20261029/packets/challenge.json | de4f7ea132511f06db43bd3fe775a9aee6620b87980529fca20aedbc99886463 |
| brief.md | 24829eaeb70a3edf6e8b04e420b6c610e83c61b8fdd8c714dcdee644d63719e3 |
| primary-inputs.md | 37dccdda7a451c58f3ed17b04c495f362846593d4d6e301c7d5bfdbfe2ec5bad |
| source-provenance.json | d9f5054a3f1d8048b2e47c9aa7b8ebe0fe868491b5e8bf9fb8b5df1ef2608114 |
| .runs/goldbach-source-inputs-20261029/arneth-gold40.pdf | d604a310e193d33698c42e135bff63ce2499b4d0d90c71d9f9a4c08b9b9f3cbd |
| .runs/goldbach-source-inputs-20261029/arneth-gold40.txt | 359c7aee9867fddce82b6887f8d9e485befe16d107164e2cdec04ebbe9c044d4 |
| .runs/goldbach-source-inputs-20261029/prime-bv-book277.png | e47e69dc9951f29297de3d98d08fb9cacb2e93182553007100838c91f6831cac |

The remaining Arneth render hashes stay in the unchanged source-provenance record. Output hashes are reported to the parent after writing, to avoid a self-referential file hash.
