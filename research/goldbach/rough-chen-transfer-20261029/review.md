# GOLDBACH-CHEN-024 independent challenge

29 October 2026. Actual Independent Critic challenge, one pair round. The populated challenge packet and its actual proposal JSON were read. Only this review and challenge-result.json are owned by this stage. The frozen proposal has not been edited.

**Verdict: incomplete for the original prime margin.** The signed estimate (21) is supported relative to Lichtman Proposition 3.1, with the endpoint and partial-summation justification supplied below. The ordinary coefficient identity, its cutoff, the half-level branch calculation, and the strictly negative *conditional* semiprime coefficient withstand the mathematical checks. One precise uniformity issue remains in promoting the proposed base coefficient transfer to a proved application of the pinned statements. Neither the modest overall verdict nor support for (21) validates that separate import.

No Goldbach lower bound or fixed positive cubic gap has been established. No authority to complete the full goal belongs to this stage. Novelty remains unverified.

## 1. Evidence and assurance

The frozen statement SHA256 is `09b17b941252a211f3ddc68aea95e5b516a6b58153e461e1e53a42d2566e6f68`, matching the assigned value. Other inspected input hashes are:

| Input | SHA256 |
| --- | --- |
| propose-result.json | `9a212d25bdcb48b747e878fb4b2fc358709eacc81aeaa700c33cca09410ff7a0` |
| brief.md | `7aeddfa2f1f8f3d123b6cd63db7a941c250f62fd87c70da18ed755ed7010b429` |
| source-provenance.json | `3d227f7e5b4e080ba81a4774d1726d71c34bc82fba9d09ce3dda17e3d03785c3` |
| populated challenge.json | `773780fe376775b3efa40998bfaa2da201fa61ca3930b623516183044cf247a3` |

All sixteen pinned source files were checked against the recorded byte lengths and SHA256 values. All sixteen matched. This verifies file identity, not their mathematical truth. I inspected the complete proposed derivations; the pinned rough-Chen TeX's local-factor, distribution, base, branch, switched, conclusion and limitation arguments; Li's actual Lemmas 2.1 and 2.2 in text and the page 3 and 4 renders; and Lichtman's Definitions 1.4 and 2.1, Theorem 1.7, Proposition 3.1, its proof's interval reduction, and Section 6.1/Proposition 6.6, including the page 9 and 28 renders. The imported analytic theorems are used as named primary inputs. Their complete classical proofs have not been re-certified by this review.

Assurance for the elementary deductions below is complete written argument with a distinct assigned reviewer. It is not proof-assistant certification or a claim of statistically independent errors. No numerical certificate, numerical helper, retrieval, extra agent, supplemental mechanism, paid call, publication or external message was used. File reads, existing-render inspection, hashes and output serialization are not a source numerical certificate.

## 2. Prioritized findings

### F1. Critical, open target rather than a refutation of (21)

**Target:** any promotion of the new congruence estimate to the actual complementary-prime lower bound (24), full cubic gap (25), or a positive prime-pair margin.

**Evidence gap:** (21) estimates a discrepancy against the exact reduced-residue numerator `1_(kh,d)=1 / phi(d)` for a restricted rough product and genuinely triply well-factorable modulus coefficients. It supplies no sign-aware minorant/majorant for the actual prime complement, no comparison with the full radical-wheel model, and no bound for the omitted cofactor and nonrough sectors. The full Mobius expansion (22) exceeds its modulus range. The proposed truncated coefficients fail its factorability hypothesis, as proved in Section 6 below. These are actual coefficient failures, not merely a comparison of level exponents.

**Impact:** the original goal remains open. The author explicitly acknowledges this, so this finding preserves that limitation rather than alleging an overclaim of Goldbach. A useful distribution corollary is not yet a lower estimate for the signed operator in the brief.

**Falsifiable repair:** exhibit the actual sign-aware complementary-prime coefficients and their convolution decompositions for every triple splitting, then bound the wheel, atom and omitted sectors with their correct signs. The single-prime support test in Section 6 is a decisive first check of any purported triple-factorability repair.

### F2. High, coefficient-specific uniformity in the base transfer is not explicit

**Target:** the unconditional `proved` label on the coefficient transfer leading to (7), and hence on the use of its specific L0 in (13).

**Evidence gap:** Li's exceptional r=0 display uses u=1/500 and an outer modulus limit N^(19101/32000). The actual base uses the *different level-dependent weights* tilde-lambda^-_D with D=N^(249/448-sigma). A signed estimate for tilde-lambda^- at the maximal construction level does not imply the same estimate for the lower-level construction by discarding terms: these are different coefficient sequences. The proposal writes no coefficient-indexed r=0 estimate and gives no proof of that family uniformity. The needed statement is specifically

    sum_(q<=D, q|P(N^(1/500)), (q,N)=1)
      tilde-lambda^-_D(q) [pi(N;q,N)-pi(N)/phi(q)]
      <<_A N/(log N)^A,

uniformly for the actual fixed D exponent below the stated maximum, and with the same modified family used in the lower sieve. Likewise, the exact modified-support/vector construction has to be the imported construction, rather than a change to arbitrary smooth coefficients. The pinned Section 6.1 gives the support/factorization framework and refers elsewhere for its precise modified definition; its word “essentially” is not a new coefficient identity.

There is a plausible narrow reading that resolves this issue: Li first quantifies D=N^vartheta, and its un-subscripted tilde-lambda retains that family parameter in the r=0 clause. Under that reading, applying the r=0 conclusion to tilde-lambda_D and using its support q<=D is legitimate. This would be an explicit uniform-family import, not monotonicity of a signed error. I have no counterexample to this reading or to the base bound. I do not refute the primary theorem. The frozen proof should state this exact import and its retained parameter rather than claim it has newly verified it from the numerical level inequality alone.

**Impact:** the anatomy inequalities and disjoint r=0/1/2/3 grouping are supported, but the source-to-*actual-coefficient* conclusion (7) remains conditional on this precise import as currently documented. The BV branch error estimate itself is unaffected; the lower bound (13) with this L0 inherits the base qualification. The negative formal coefficient calculation does not require unconditional validity of (7).

**Falsifiable repair:** write and justify the displayed coefficient-indexed r=0 uniform statement from the original D-parametrized lemma/construction. If that scope cannot be established within the pinned inputs, label (7), and therefore (13) with that base, conditional. For the already conditional switched application, also identify the exact modified upper support giving t1<=D-exponent/3; the ordinary upper-support cubic condition is not by itself a proof about arbitrary modified weights.

### F3. Low, exact formulas need a clean restatement in revision

**Target:** the literal formulas containing the prime indicator, especially (20), (22) and the cell condition in (9).

**Evidence:** the frozen Markdown contains bare carriage-return corruption in some intended `\rm` markers. The intended formulas can be reconstructed from the surrounding definitions, but the literal rendering is damaged.

**Impact:** no mathematical counterexample follows. This is a reproducibility and readability defect in otherwise identifiable coefficients.

**Repair:** preserve the frozen file and restate the affected formulas cleanly in the revision, using `\text{prime}` or an explicit indicator definition.

## 3. Base anatomy and fixed-factor transport audit

For theta=7/32 and beta=25/224, the one-coordinate function is exactly

    v(t)=min((1+t)/2, 1-34t/39, 57/64-3t/2).

The Goldbach-size residue uses alpha=1 in Lichtman's functions; it does not get the small-residue 66/107 level. On beta<=x<=2beta, the first entry is at least eta0=249/448 by its left endpoint, the third by its right endpoint, and the second is larger throughout. If t1+t2<beta with t1>=t2>=t3, then t2,t3<beta/2. The three entries in w at that limiting pair exceed eta0: the second exceeds it by 75/3584, and the other two are larger as well. Its gate threshold (1+t1)/2 is below eta0. This proves (6). It also proves the missing-coordinate numerical inequalities for (t1,t2,u0) and (t1,u0,u0) when the extracted exponents are at least u0=1/500. The strict/weak gate distinction does not change these applications with a fixed working-level margin.

The proposed grouping is the correct one. With at least three primes above N^u0, extract exactly the three largest. The residual then has all prime factors below the third largest, precisely c|P(p3); it need not be u0-smooth. With exactly two or one primes above N^u0, extract those and use c|P(N^u0). With none, use the exceptional u0 clause. Squarefree support makes the ordered extraction unique. The side inequality beta<25/128 holds. Fixed exponent cells above u0 can be made compatible with the source vector mesh and a fixed sigma margin, provided the actual imported modified construction is retained. This is not an estimate for arbitrary coefficients supported on smooth integers. F2 identifies the remaining coefficient-family qualification, not a failure of these elementary inequalities.

For the upper anatomy calculation, eta0/3=83/448<25/128. If the actual modified upper construction has that largest-extracted-factor restriction, its displayed inequalities work: for t1>=beta the one-coordinate entry is (1+t1)/2>=eta0; otherwise the second entry in w at t3=beta is exactly eta0 and the other entries are larger. The r=0/1/2 residual classes still have to be the ones just described. This verifies the numerical anatomy part, conditional on the stated exact modified support, not the full switched endpoint transport.

For a fixed largest modulus prime ell=N^t, the actual shifted residual weight in (9) is not the total modified weight merely because both are sieve weights. Li's vector condition requires ell^2<D. On eta(t)=57/64-3t/2, this is exactly t<57/224, with a fixed strict margin required in an application. Above that threshold the direct specified vector invocation fails. No assertion about all alternative decompositions follows.

The ordinary identity (12) is correct. For squarefree d with P^+(d)<ell, prepend ell to its decreasing prime list. The lower support's separate condition is ell^2<D; each remaining even-index condition becomes the upper support's odd-index cubic condition at level D/ell. The Mobius sign changes by minus one. For d=1 and ell^2>=D the lower coefficient vanishes whereas the proposed right side is -1, giving the promised smallest counterexample to extension. None of this proves an identical formula for the modified weights.

At total level N^(1/2-sigma), ordinary upper residual weights are legitimately controlled by classical absolute BV at the fixed prime endpoint N. A squarefree total modulus has only O_beta(1) possible large prime factors ell>=N^beta, since its size is at most N^(1/2-sigma); bounded ordinary weights therefore give a bounded aggregated coefficient. The error sum uses the supremum over reduced residue classes in BV, so growth of residue N is harmless here. Removing representations containing a prime factor of N costs at most omega(N); each such representation has p equal to that factor. Endpoint cutoffs and repeated large factors have the asserted power-saving elementary bounds. No different-modified-weight identity is needed for this BV statement.

The branch integrals in (13) are correct. For beta<=t<=1/8, rho=t and s=(1/2-t)/t; changing variables gives 2 exp(-gamma) times the integral of F from 3 to 87/25. For 1/8<=t<=alpha, rho=(1/2-t)/3 and F(3)=2 exp(gamma)/3; the integrand is 2/[t(1/2-t)] and its integral is 4 log(3alpha/(1/2-alpha)). Fixed positive margins followed by continuity give the claimed limiting branch coefficient. Its combination with the proposed L0 is qualified by F2. In (14), the claimed loss is nonnegative only on the expressly restricted t<25/96 subinterval; beyond it BV covers the smaller claimed source level. The proposal states this restriction and does not establish the neighboring modified coefficients by that calculation.

## 4. Exact conditional semiprime coefficient calculation

The exact identity U_alpha=R_alpha+E_alpha+H_alpha is valid for q>1 and alpha in (1/4,1/3), because four prime factors greater than N^alpha have product greater than N. It includes repeated factors. The ordinary harmonic masses in (15) are correct for the ordered-once chambers. The inner triple integral is

    integral_(v=t)^((1-t)/2) dv/[v(1-t-v)]
       = log((1-2t)/t)/(1-t).

The lower endpoint restrictions on the largest prime and repeated-factor diagonals contribute a lower logarithmic order or the bound N^(1-alpha), respectively. These are raw product masses; no correlation with a prime complement has been inferred from them.

For (16), the factor 2/eta0 is the formal upper linear-sieve constant: the raw product count is (N/log N)Bj, V_N(N^(1/2)) is 4 exp(-gamma) C2 S0(N)/log N, and F(2eta0)=exp(gamma)/eta0. Dividing their product by X_N=2 C2 S0(N) N/(log N)^2 gives 2Bj/eta0. Validity of the required switched coefficient estimates and full product-domain partition remains an explicit additional assumption. Li's displayed boxes have exponents summing to one and logarithmically short widths; they are not by themselves a proof for every product below N. Its printed main numerator is a coprimality condition with N, rather than the general (product,q)=1 numerator. Any extension must retain or justify changing it. When the prime factors in the product are all above N^alpha and the actual upper modulus support has largest prime below N^(83/448+o(1)), coprimality of product and q is automatic; products sharing a large prime with N form a negligible exceptional sector. This observation does not prove the missing box-to-full-domain extension or the upper-support import.

Now grant exactly the optimistic inputs specified in the proposal, including its formal H_src and switched bounds. Let C(alpha)=L0-H_src-(2/eta0)(B2+B3). Since f<=1, gamma>1/2 and exp(1/2)>3/2,

    L0 < 448/75.

On the first source branch, s=(1-t)/(2t) lies between 3 and 199/50<4, and F(s)>=2 exp(gamma)/s gives an integrand at least 4/[t(1-t)]. On the other formal branches eta(t)<=(1+t)/2 gives the same lower bound. Consequently, for alpha>1/4,

    H_src >= 4 log(199/75),
    B2 > log 2,   B3 >= 0.

For x>1, log x>2(x-1)/(x+1); its difference has derivative (x-1)^2/[x(x+1)^2]>0 and vanishes at 1. Therefore

    H_src + (2/eta0)B2
       > 496/137 + 1792/747
       = 448/75 + 353328/7675425.

Indeed the common denominator is 137*747*75=7675425, and the numerator of the difference is 27788400+18412800-45847872=353328. Thus C(alpha)<-353328/7675425 throughout the stated interval. This independently reconstructs (18) without a numerical helper. It is a proved inequality for the specified *conditional coefficient expression*. It does not establish the optimistic input inequalities, refute their primary sources, or rule out every refined signed sieve.

## 5. Detailed audit of the actual signed estimate (21)

This is the strongest new arithmetic assertion in the proposal, and it survives the following checks relative to Lichtman Proposition 3.1.

Set x=N/3, a=N, and the proposition's residue exponent to 1+epsilon. Then a<x^(1+epsilon) eventually. Its small variable n is the prime cofactor k, not the Mobius variable h. On a dyadic rectangle meeting kh in (x,2x], the small scale K is at least a constant times N^(1/6) and at most N^(1/3-epsilon), so x^epsilon<=K<=x^(1/3+epsilon) eventually. The large scale H has KH asymptotic to x up to fixed factors. The condition h>D is harmless as part of the large coefficient; indeed on this suboperator h is eventually larger than N^(2/3+epsilon)/3 and hence larger than D. No size hypothesis is obtained by switching k and h.

The small coefficient is alpha_k=1_(k prime), with the stated endpoint restrictions, and the large coefficient is beta_h=mu(h)1_(h>D,P^-(h)>y). Both are 1-bounded. The small coefficient is supported on P^-(k)=k>y=N^(1/6)>z0=x^(1/(log log x)^3). Definition 2.1 explicitly admits the prime indicator and requires uniformity also under the auxiliary coprimality condition (k,d)=1. No SW property of the large Mobius coefficient is needed. Common prime factors between k and h are allowed by the proposition. When mu(h) is nonzero, roughness makes h squarefree and h_(>y)=h, so the coupled weight is exactly the one in (20); when mu(h)=0 the replacement changes nothing.

There is a small uniformity argument implicit in the author's partial summation that can be supplied without assuming SW for arbitrary coupled weights. For each dyadic prime interval and each endpoint T in it, the truncated prime indicator remains SW, uniformly in T, including the auxiliary coprimality condition. One may use the usual endpoint-uniform prime SW estimate and subtract its two endpoint sums; all endpoints are comparable to K. Equivalently, the proof of Proposition 3.1 explicitly passes in (5.19) to arbitrary intervals I_N and I_M. Large-variable truncation is allowed because beta is arbitrary. Thus the bilinear discrepancy bound holds uniformly for partial rectangles while retaining kh in I. No assertion that the joint function mu(h)Phi is SW is required. If one instead used a Mellin decomposition, any twists would need their own uniform SW constants; that unneeded alternative has not been silently invoked here.

Let f(k,h)=Phi(log h/log(kh)). On each relevant rectangle, logarithms of k,h and kh are comparable to log N. The quantities |f|, K|f_k|, H|f_h| and KH|f_kh| are bounded uniformly. Exact two-variable partial summation therefore bounds the weighted discrepancy by a constant times the supremum of the partial-rectangle discrepancy: the boundary terms and the two first-derivative and mixed-derivative integrals all have bounded total mass. The product interval remains a permitted fixed I subset [x,2x]. In particular, no approximation to Phi, discretization error, Mellin tail or uncontrolled endpoint strip is present. The O((log N)^2) dyadic rectangles cost only logarithms and are covered by choosing the theorem's logarithmic accuracy A+3 first. This supplies the missing expanded argument for the full coupled polynomial, without weakening it to a separable coefficient.

At theta=7/32 the admissible level exponent is

    min(66/107, (5-(1+epsilon)*7/32)/8) - 50epsilon
      = 153/256 - (50+7/256)epsilon.

The proposed exponent 153/256-100epsilon has a fixed spare margin. Since Q is expressed with N whereas the proposition uses x=N/3, the constant rescaling is absorbed for large N by that fixed exponent margin. For 0<epsilon<1/2000 it remains strictly above 1/2. Nothing uses the small-residue 66/107 level for residue N.

The modulus sequence must be genuinely triply well-factorable for every splitting of Q into three factors, with the bounded factors required by Definition 1.4. That is an assumption of (21), not a conclusion about Mobius or modified sieve weights. Restriction to (d,N)=1 preserves the property: in each convolution representation multiply each factor at d_i by 1_(d_i,N)=1, and use 1_(d,N)=1=product_i 1_(d_i,N)=1 for d=d1d2d3. The main numerator remains exactly 1_(kh,d)=1. Thus the resulting bound is exactly (21) for its actual signed coefficients and residue.

**Supported scope:** a beyond-half signed congruence-error estimate for this one restricted suboperator against an assumed admissible modulus sequence, relative to the imported Proposition 3.1. It is not an estimate for the original wheel model or prime weight. It is not a substantive Goldbach breakthrough by itself.

## 6. Prime-filter and omitted-sector audit

For m=N-kh in [N/3,2N/3), set Z=sqrt(2N/3). For sufficiently large N every prime in this interval exceeds Z, and every composite there has a prime factor at most Z. Consequently the exact identity intended by (22) is

    1_(m prime) = sum_(d|m, d|product_(r prime,r<=Z) r) mu(d).

This is valid also for prime powers: the squarefree Mobius divisor sum is zero once one small prime divides m. Its actual moduli extend to m, and cannot all be put below Q from (21).

For the naive truncated b_d=mu(d)1_(d<=Q)1_(P^+(d)<=Z), choose a prime r in (Q^(1/3),2Q^(1/3)]. For large N this interval is below both Q and Z, so b_r=-1. In the balanced splitting Q=Q^(1/3)Q^(1/3)Q^(1/3), every Dirichlet convolution of three factors supported at most Q^(1/3) has coefficient zero at r: a factorization of a prime must put r into one factor. This contradicts b_r=-1, regardless of signs or cancellation at composite arguments. For coprime restriction, the number of primes in the interval grows, while N has at most 3 log N/log Q=O_epsilon(1) prime divisors of that size; a prime not dividing N can be selected. This proves the claimed factorability counterexample. Bertrand plus the prime number theorem here are classical imports, not a numerical search.

Phi is nonnegative on [0,1], but mu(h) has both signs. A prime upper bound cannot be multiplied indiscriminately by this coefficient to obtain a signed lower bound. Splitting its two signs produces bounded permissible large coefficients for Proposition 3.1; it still supplies no suitable prime minorant and majorant. Logarithmic prime weights, the exact radical W, kappa, and the atom at kh=N/2 would then still have to be transported. None was replaced by 1/phi(d) in the accepted congruence calculation.

The cofactor k=1 is present in (19). Its rough contribution vanishes because Phi(1)=0, while its nonrough part need not vanish. The remaining nonrough, even rough and outer odd sectors recorded in the previous cubic revision remain unresolved and have not been discarded here. Repeated factors in kh are permitted in (21), and the exact counting identities retain them; the power-saving deletions occur only in the specified asymptotic contamination coefficients.

The narrow defensible outcome is therefore the supported Type II corollary, the elementary coefficient obstruction and conditional failed semiprime sign, with F2 made explicit in any revised base claim. The first decisive next mathematical check is an actual sign-aware complementary-prime coefficient transport passing the balanced prime test. This challenge neither grants another round nor authorizes any change of the original objective, resource contract or publication status.
