# Independent review of the switching certificate and parity model

29 October 2026. Registry role: Independent Critic, `GOLDBACH-SWITCHING-004`. This is separate host-agent mathematical review. It is not external peer review, formal verification, or a test with an independent model provider. No usage measurements are available.

## Verdict and reviewed versions

**Supported:** the exact least-prime partition, the legal one-switch coefficient calculation, and its negative closed-form certificate in the declared fixed-parameter domain.

**Supported:** the root-authored weighted parity model, its divisor-density normalization, and its summed arbitrary-log-saving error through every fixed level x^(1-epsilon).

**Supported:** the supplemental bilinear test, restricted to the stated expression and parameter M=x^(2/5). It identifies extra information absent from the model rather than supplying that information for actual primes.

**Incomplete:** a positive odd-factor lower bound for the actual prime-complement sequence or a Goldbach solution. None of these supported statements is a demonstrated breakthrough on Goldbach. Priority is unverified. No mathematical correction is required for the frozen inputs.

| Frozen input | SHA256 |
| --- | --- |
| `statement.md` | `3faf6a11ff9189f7e8251d9187abaf0ead8069110951bc541ee004eca678ff53` |
| `parity-model.md` | `8cfc0eabfbae699fbec0d10328277cac82bd37b97aafac6d9ab5d8d76f7f0e14` |
| `survey.md` | `652497f283067950e0700577fecc88d7bbaf052f134e7ca4d67ab1d8b2f03473` |
| `bilinear-model-test.md` | `483a8ec93b95e09d26217187effd86c44aa0b95ce46ba3880e380d945bd1a36a` |

The populated counterexample packet supplied the completed statement response. The parity model and its bilinear corollary were separately root-authored supplements. I changed none of these files.

## Primary-source checks

I inspected [Wu, Lemma 2.2, definitions and equation (2.6), printed pages 219-220](https://www.impan.pl/shop/en/publication/transaction/download/product/82961). Its stated cutoff range is 2<=z<=sqrt(Q). Its remainder coefficients have order 1, which means their absolute values are at most 1 by the preceding definition. Their number depends only on the fixed approximation tolerance. Its differential definitions give the functions used by the author on the stated intervals.

I also inspected [Ford, the ordinary BV statement and the classical Selberg examples in section 1.7.4](https://ford126.web.illinois.edu/sieve2023.pdf). The classical Liouville summatory estimate used by the model is explicitly recorded there. Ford's coefficient-uniform two-linear-form upper bound was inspected during the earlier separate review. These source checks do not constitute a full audit of either source's entire proof chain. The algebra, error accumulation, and model construction below were checked directly.

## Exact partition and exceptional cases

For fixed N, each complement q>1 has a unique least prime factor. Thus changing the strict rough cutoff from N^beta to N^alpha subtracts exactly those least factors r satisfying N^beta<r<=N^alpha. Writing q=r*m is unique and permits m=1. The condition that all remaining factors are at least r retains equality, so repeated factors, squares and cubes are correctly included. There is no permutation multiplicity.

At alpha in [0.3,1/3), four factors all strictly above N^alpha would have product greater than N. Consequently a rough complement has one, two or three factors, and F_alpha=U_alpha-E_alpha is exact. The raw lower-sieve sequence includes q=1 at most once and subtracts it explicitly. It is not erroneously removed from the switched m sequence, where m=1 is needed.

Removing prime summands p dividing N globally costs at most omega(N), after which no prime factor of q divides N. A switch with r|N would force p=r and is already in that removed class. For the semiprime subtraction, such exceptions have p>N^alpha and number at most three, by the product argument from the prior reviewed tranche. All these count errors are negligible on A_N=S(N)N/log(N)^2.

## Legal sieve parameters and normalization

The local density at an allowed odd prime ell is 1/(ell-1); primes dividing N, including 2, are excluded. The exact factorization of V_N(v) in the statement is correct. Mertens and the convergent twin-prime product give its coefficient e^(-gamma)*S(N)/log v. Target dependence is controlled: for v=N^u with fixed u bounded below, only O_u(1) prime divisors of N can exceed v, and each omitted singular factor is 1+O(1/v). The profile's product condition is uniform because deleting factors dividing N can only decrease the inverse-density product.

The unweighted base mass is li(N), so li(N)~N/log N combines with V_N to produce precisely the normalization A_N. Replacing the base mass by N would lose a logarithm; the author does not make that error.

For the lower sieve, beta in [d/4,d/2) yields s=d/beta in (2,4]. The explicit strict cutoff floor(N^beta)+1 is asymptotically unchanged and remains in the allowed range for fixed beta<d/2. Thus the lower coefficient is

    L(d,beta) = (2/d)*log((d-beta)/beta).

For a switch r with t=log r/log N, the available distribution budget is D_r=N^d/r. The chosen cutoff v_r=min(r,sqrt(D_r)) is legal. Its exponent u=min(t,(d-t)/2) is positive on the declared fixed interval, and its sieve parameter is in [2,3]: use t>=beta>=d/4 for the upper endpoint, and the explicit weakening for t>d/3. The calculation uses V_N(v_r), as it must, rather than retaining V_N(r) after weakening.

For all relevant squarefree k, the prime factors of k are strictly less than v_r<=r. Hence k is coprime to r and its main progression term is li(N)/[phi(r)phi(k)]. One can take the sifting-prime set to exclude r; no assumption at that unused prime is needed. The upper function satisfies sF(s)=2exp(gamma) on [2,3], so the per-r leading expression is exactly the one giving the factor 2/(d-t).

All parameters are fixed before taking N to infinity. The lower bound on d-alpha is used for uniformity of the density approximation. The source's approximation tolerance is fixed first, so the number of remainder families is fixed; only after N tends to infinity is the tolerance sent to zero. No moving-parameter uniformity is silently inferred.

## Summed remainder errors and coefficient certificate

For an upper-sieve remainder, the global progression modulus is r*k<=D. Since every prime factor of k is strictly smaller than r, the switch prime r is the unique largest prime factor of the resulting modulus. A modulus therefore arises from at most one r, and then k is determined. The absolute sum of remainders for each order-1 coefficient family is bounded by the ordinary BV absolute sum through D. There is no hidden multiplicity growing with the number of switching primes. The lower sieve uses the same ordinary remainder theorem directly. Because d<1/2 is fixed, every required fixed logarithmic saving is available below the BV range eventually. Removing p|N contributes at most O(D log N) by the crude per-modulus count, which is negligible.

Prime harmonic summation in the nonnegative upper main terms then gives

    J(d,beta,alpha) = 2*integral_beta^alpha dt/[t(d-t)]
      = (2/d)*log(alpha*(d-beta)/(beta*(d-alpha))).

Subtracting J from L cancels beta exactly:

    M(d,alpha,beta) = (2/d)*log((d-alpha)/alpha).

Throughout the declared domain, (d-alpha)/alpha<2/3 and 2/d>4. The logarithm is negative, so multiplying by the larger positive factor makes the result more negative. Thus M<=4log(2/3)<=-4/3. The inequality direction and the rational sign certificate are correct. The displayed rational example and its I(alpha) specialization also simplify correctly.

The semiprime upper coefficient is nonnegative. Its integral follows from the sorted least factor r<=sqrt N and the two-form bound, and direct antidifferentiation gives

    integral_alpha^(1/2) dt/[t(1-t)^2]
      = 2-1/(1-alpha)-log(alpha/(1-alpha)).

It includes repeated factors. Subtracting any valid nonnegative K2*I(alpha) makes the chosen lower bound worse. A negative lower-bound coefficient is compatible with F_alpha>=0 and says nothing negative about the actual count. It certifies failure only of this precisely specified combination of standard inequalities. The remarks about partitioning its integral and using smaller legal cutoffs remain within that same family; they do not cover Chen double-sieve improvements or every switching identity.

## Weighted parity model audit

For odd n, the expansion w(n)=sum_{e|n}h(e) is correct because the local sum is 1+1/(p-2)=(p-1)/(p-2), with h supported on odd squarefree e. The bound h(e)<=tau_3(e)/e holds prime by prime, including equality at p=3. Expanding tau_3 into three factors yields the stated logarithmic head sum; its elementary summatory bound and partial summation yield the reciprocal tail. The Euler product sum h(e)/e=C2^(-1) follows from

    1+1/[p(p-2)] = (1-1/(p-1)^2)^(-1).

The positivity bound sum_{n<=T}w(n)<<T follows by counting odd multiples after the same expansion. Its partial summation gives sum_{d<=T}w(d)/d<<log(2T).

For arbitrary odd d, including powers, the identity for w(dm) correctly excludes from the new divisor expansion all primes already dividing d. The remaining m may still contain those primes. Counting its odd residual multiples gives Y/(2e)+O(1), Y=x/d. The Euler-factor ratio at p|d equals p/(p-1). Consequently the main term is exactly C0*x/phi(d), with C0=1/(2C2), and the uniform error O(w(d)log(2x)^3) is valid. Summed through D=x^(1-epsilon), this error is O(Dlog(2x)^3), smaller than x/log(x)^A for every fixed A and epsilon>0.

For the twist, complete multiplicativity gives lambda(d)lambda(e), and lambda(e)=mu(e) on the squarefree support of h. The odd summatory relation L_odd(t)=L(t)+L(t/2) has the correct plus sign. Splitting e at sqrt Y is legitimate: the first part uses the classical Liouville summatory bound at arguments at least sqrt Y, and the second is at most Y times the reciprocal h tail, namely O(sqrt Y log(2Y)^2). For d<=x^(1-epsilon), Y>=x^epsilon uniformly, so this power-saving tail is smaller than every fixed requested logarithmic saving. Multiplication by w(d) and summation with sum w(d)/d<<log x loses just one logarithm, as stated.

These arguments establish the summed arbitrary-log-saving divisor estimate for both signs. Scaling by li(x)/(C0*x) gives the stated prime-counting mass and preserves all such savings. Removing n=1 affects only the divisor sum d=1 by a bounded amount. The plus sequence is nonnegative and zero at every odd-Omega input, regardless of roughness. For targets N=2^k, its zero-residue divisor densities match the shifted-prime sieve profile. None of this establishes a model of actual reflected primes or equidistribution in all reduced residues, which the report correctly disclaims.

## Supplemental bilinear test

For the plus model, mu(n)*a_plus(n)=mu(n)^2*a_plus(n)>=0 exactly: either the integer is nonsquarefree, its odd parity kills the plus weight, or it is squarefree with even parity and mu(n)=1. Thus no cancellation is lost by restricting the bilinear sum to a subset of its terms.

With M=x^(2/5), retain prime k in (M,2M] and prime m in (x/(4M),x/(2M)]. Their products are at most x and the two primes are distinct for sufficiently large x, since their exponent ranges differ. Each product contributes at least 2. PNT supplies a number of pairs bounded below by a constant times x/log(x)^2. This proves the displayed bilinear lower bound; scaling to li(x) mass gives li(x)/log(x)^2. Its C=1 Mobius inner structure is the asserted one. The calculation does not assert that this particular M belongs to every parameter range of the full FI theorem, nor does it assert failure for actual primes. It does prove that a suitably small bound for this concrete bilinear expression cannot be deduced from the model's divisor-density data alone.

## Findings and limits to preserve

There are no required mathematical repairs for the frozen statements. The following boundaries are essential when integrating them:

1. **P1, objective incomplete.** The coefficient certificate refutes the adequacy of one declared minorant; it supplies no positive lower margin for actual F_alpha. The model obstruction applies to general nonnegative weighted divisor-sieve inputs. Neither is a proof of Goldbach or an impossibility theorem for all Goldbach methods.
2. **P2, additional hypotheses must be checked separately.** The model does not retain actual-prime reflection, all-residue AP equidistribution, or the two-linear-form bounds used in the actual-prime subtraction. The bilinear supplement shows one explicit distinction. It cannot be promoted to a statement that actual primes fail that test, or that a full FI application has been verified.
3. **P3, parameter and assurance scope.** Preserve fixed alpha,d,beta, the successive tolerance limit, the exact strict cutoffs, and the all-log model estimate's fixed epsilon. Numerical effective constants, finite thresholds and novelty are unverified. No finite check can establish the infinite obstruction or asymptotic coefficient calculation on its own.

The decisive next research step must introduce an actual additional arithmetic estimate or a different switching identity with its true remainder hypotheses. Changing beta within this family, or merely increasing ordinary divisor distribution in the general weighted setting, does not provide the required odd-parity lower bound.
