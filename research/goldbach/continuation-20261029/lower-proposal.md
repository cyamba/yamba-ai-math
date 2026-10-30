# Two pointwise lower-bound attempts

29 October 2026. Registry role: Mathematician, program `GOLDBACH-LOWER-003`. This proposal continues the actual lower-bound attempt after the accepted contamination bound. It proves reductions and quantifies where the attempted unconditional estimates fail. It does not supply the missing estimate or a Goldbach breakthrough. The separate critic has not yet reviewed this proposal.

## Shared notation and inspected inputs

Keep H_alpha, F_alpha and A_N=mathfrak S(N)N/log^2N from `statement.md`. For fixed 0<epsilon<=1/30, alpha=1/3-epsilon, the reviewed result gives limsup H_alpha/A_N<=C*epsilon^2. The desired original input is liminf F_alpha/A_N>C*epsilon^2, uniformly over sufficiently large even targets.

The analytic inputs inspected for this attempt are:

* [Ford, *Sieve Methods*, Theorem 3.4, printed page 35](https://ford126.web.illinois.edu/sieve2023.pdf): ordinary Bombieri-Vinogradov with endpoint and reduced-residue maxima up to x^(1/2)/(log x)^B. Passing from its prime-counting form to the von Mangoldt form costs logarithms, which arbitrary logarithmic saving absorbs. The same notes, section 3.1, record the dimension-one sifting limit beta(1)=2.
* [Huang-Li v2, Lemmas 1 and 3, sections 3.1 and 3.3-3.4](https://arxiv.org/html/2005.03811): unconditional Möbius/phi coefficient evaluations and squarefree-complement mass. Their statements and relevant calculations were inspected here; this is not a full independent audit of every supporting reference. I use their unconditional coefficient estimates and reproduce the reduction below. I do not import their missing-cutoff rearrangement or assume their twisted-distribution conjecture.
* [Friedlander-Iwaniec, *Asymptotic sieve for primes*, Theorem 1 and hypotheses (R), (B), pages 1043-1045](https://arxiv.org/pdf/math/9811186): prime detection requires its specified bilinear input in addition to distribution. This is an implication with analytic hypotheses, not a theorem proving those hypotheses for reflected primes.

All source-derived distribution inputs below are distinguished from the estimates still to be proved. No purported unconditional lower bound is inferred from the mere existence of these theorem statements.

## Attempt 1: retain one signed moving-endpoint operator

This route bypasses the stronger near-cubic F target and aims directly at ordinary binary Goldbach. A proof of its final operator estimate need not prove the original rough-pair criterion or a fixed positive prime-pair-scale margin for F.

Fix once and for all 0<theta<1/2, for example theta=49/100, and set Q=N^theta. Let

\[
G(N)=\sum_{\substack{p+q=N\\p,q\text{ prime}}}\log p\log q,
\qquad f_N(n)=\Lambda(n)\mu(N-n),\qquad
B_N=\sum_{1\le n<N}f_N(n).
\]

For each k coprime to N, set M_k=max(0,ceil(N-Qk)-1), w_k(n)=log(k/(N-n)), and

\[
\Delta_k(N)=
 \sum_{\substack{1\le n\le M_k\\n\equiv N\ (k)}} f_N(n)w_k(n)
 -\frac1{\phi(k)}\sum_{1\le n\le M_k}f_N(n)w_k(n).
\]

Define the **signed operator**, preserving cancellation between moduli,

\[
\mathcal O_N(Q)=
 \sum_{\substack{1\le k<(N-1)/Q\\(k,N)=1}}\mu(k)\Delta_k(N). \tag{1}
\]

This definition uses ordinary Möbius and von Mangoldt functions, not a modified prime-deletion model. It is an arithmetic progression discrepancy with a particular moving cutoff and weight, rather than a renamed prime-pair count.

### Exact divisor split

Let

\[
W(N)=\sum_{1\le n<N}\Lambda(n)\mu^2(N-n)\Lambda(N-n),
\]

and split its divisor identity at d<=Q into S1 and S2. Then W=S1+S2 exactly. The squarefree factor forces N-n to be prime whenever its von Mangoldt factor is nonzero. The remaining discrepancy between W and G comes from first-coordinate prime powers. There are O(N^(1/2)log N) such powers, each product of logarithmic weights is O(log^2N), so

\[
G(N)=S_1+S_2+O(N^{1/2}\log^3N). \tag{2}
\]

By the corrected finite divisor switch in `endpoint-lemma.md`,

\[
S_2=\sum_{k<(N-1)/Q}\mu(k)
 \sum_{\substack{1\le n<N-Qk\\n\equiv N\ (k)}}
 f_N(n)\log\frac{k}{N-n}. \tag{3}
\]

No endpoint is replaced by N. If gcd(k,N)>1, any n with nonzero Lambda(n) in that class is a prime power with base p dividing N. For each fixed k the sum of those Lambda weights is at most omega(N)log N=O(log^2N), and the logarithmic weight is O(log N). Thus the full noncoprime part of (3) is

\[
O((N/Q)\log^3N). \tag{4}
\]

It is negligible compared with N/log^A N for each fixed A, because theta>0.

### The short-divisor term is actually accessible

For every fixed A>0, ordinary Bombieri-Vinogradov and the inspected unconditional coefficient evaluation give

\[
S_1=\mathfrak S(N)N+O_{A,\theta}(N/\log^A N). \tag{5}
\]

Here is the dependence check rather than an invocation of a conditional EH theorem. Expand mu^2(h)=sum_{b^2|h}mu(b) and truncate b at B=(log N)^(A+4). The tail is bounded by O(N log^4N/B): use the exact count of positive h<N divisible by lcm(b^2,d), the inequality |mu(d)log d|<=log N, and gcd(b^2,d)=gcd(b,d) on squarefree d. Expanding gcd(b,d)=sum_{r|b,r|d}phi(r) bounds the reciprocal sum by O((log N)(log B+1)/B), which is more than sufficient.

For b<=B, d<=Q, the modulus lcm(b^2,d) is at most QB^2. The noncoprime classes contribute O(QB log^3N), again negligible. For each fixed b and modulus r, squarefree d with lcm(b^2,d)=r has at most tau(b)<=b choices, so the total multiplicity for r is at most O(B^2). Therefore the absolute error of replacing the remaining prime progression sums by N/phi(r) is at most

\[
O\!\left(B^2\log N\sum_{r\le QB^2}
 \max_{(a,r)=1}|\psi(N;r,a)-N/\phi(r)|\right).
\]

Any fixed power of log N here is absorbed by choosing the saving in Bombieri-Vinogradov sufficiently large. Its modulus condition holds eventually because theta<1/2 is fixed, even after all these logarithmic factors. The resulting main coefficient is exactly the one evaluated by Huang-Li Lemma 3. This proves (5) from unconditional imported inputs. No reflected Möbius distribution was used in this part.

### Evaluate the transferred global coefficient with its endpoint

Subtracting the centered sums in (1) from the coprime part of (3) leaves exactly

\[
\sum_{n<N}f_N(n)K_N(N-n),\qquad
K_N(h)=\sum_{\substack{k<h/Q\\(k,N)=1}}
 \frac{\mu(k)}{\phi(k)}\log\frac{k}{h}. \tag{6}
\]

Choose 0<rho<1-theta. For h>=QN^rho put R_h=ceil(h/Q)-1, so k<h/Q is k<=R_h exactly. The identity

\[
K_N(h)=-\sum_{\substack{k\le R_h\\(k,N)=1}}
 \frac{\mu(k)}{\phi(k)}\log\frac{R_h}{k}
 -\log\frac{h}{R_h}\sum_{\substack{k\le R_h\\(k,N)=1}}
 \frac{\mu(k)}{\phi(k)}
\]

and the two inspected estimates in Huang-Li Lemma 1 give, uniformly in this range,

\[
K_N(h)=-\mathfrak S(N)+O_\rho(\log N\exp(-c_\rho\sqrt{\log N})). \tag{7}
\]

Their comparability hypothesis log N<<log R holds since R_h>=N^rho/2 eventually. The strict endpoint has not been lost. For h<QN^rho, the crude bound sum_{k<=T}1/phi(k)=O(log(2T)) gives |K_N(h)|=O(log^2N). The short h interval therefore contributes at most O(N^(theta+rho)log^3N), including the replacement of K by -mathfrak S(N), since mathfrak S(N)=O(log N). This is negligible at every fixed logarithmic saving. Using (2)-(7) yields the valid reduction

\[
\boxed{G(N)=\mathfrak S(N)(N-B_N)+\mathcal O_N(Q)
                   +O_{A,\theta}(N/\log^A N).} \tag{8}
\]

Its assurance is a handwritten derivation from the explicitly inspected unconditional coefficient estimates and ordinary BV. The separate critic must check its details. It is not an independent proof of those imported coefficient estimates.

### Obtain a genuine unconditional bias upper bound

Since mu(h)<=mu^2(h),

\[
B_N\le\sum_{n<N}\Lambda(n)\mu^2(N-n)
 =\mathcal A(N)N+O_A(N/\log^A N),\quad
\mathcal A(N)=\prod_{\substack{\ell\nmid N\\\ell>2}}
             \left(1-\frac1{\ell(\ell-1)}\right). \tag{9}
\]

This estimate is unconditional. For a direct range check, expand the squarefree indicator, truncate b at T=N^beta with any fixed 0<beta<1/4, and apply ordinary BV to the coprime square moduli b^2<=N^(2beta). The remaining tail is at most N log N/T by counting h=N-n in positive multiples of b^2. The noncoprime part is O(T log^2N). Extending the main sum in mu(b)/phi(b^2) to infinity has a power-saving error and gives the displayed Euler product. These facts reproduce the calculation inspected in Huang-Li section 3.3.

Put delta_N=1-mathcal A(N). This gap is target dependent and can tend to zero. It is not an absolute positive constant. For sufficiently large N the least prime ell not dividing N is at most 2log N, as follows from the prime number theorem for the primorial product. Since N is even, this ell exceeds 2, giving

\[
\delta_N\ge\frac1{\ell(\ell-1)}
 \ge\frac1{2\log N(2\log N-1)}. \tag{10}
\]

The same bound is explicitly used in the inspected Huang-Li corollary proof. Taking A=4, or any fixed A>2, keeps the error in (8)-(9) below this guaranteed margin, after accounting for mathfrak S(N)=O(log N) by requesting one extra logarithm in (9).

### The one-sided signed estimate that would finish this route

For one fixed theta<1/2 and one fixed kappa>0, the following is sufficient:

\[
\boxed{\mathcal O_N(N^\theta)\ge
 -(1-\kappa)\mathfrak S(N)\delta_N N
 \quad\text{for every sufficiently large even }N.} \tag{O-open}
\]

Indeed, (8)-(10) would imply

\[
G(N)\ge\kappa\mathfrak S(N)\delta_N N+O(N/\log^4N)>0.
\]

The stronger absolute maximal twisted EH hypothesis is unnecessary for this logical reduction; the one-sided signed combination (O-open) is enough. **Status of (O-open): unproved.** Its definition is explicit, and its reduction does not assume Goldbach, but no cancellation bound for this operator has been obtained here.

The reviewed endpoint lemma quantitatively explains a stronger sufficient input. If

\[
\sum_{\substack{k<N^{1-\theta}\\(k,N)=1}}
 \max_{j<N}\left|
 \sum_{\substack{n\le j\\n\equiv N\ (k)}}f_N(n)
 -\frac1{\phi(k)}\sum_{n\le j}f_N(n)\right|
 \ll N/(\log N)^{3+\eta} \tag{T-open}
\]

for some fixed eta>0, then |mathcal O_N(Q)|=O(N/(log N)^(2+eta)). By (10), this is smaller than the required margin, so it would imply (O-open), for example with kappa=1/2 eventually. This needs only one logarithmic saving exponent at one polynomial level, but it remains a reflected Möbius-twisted estimate, not ordinary BV.

**Actual failed estimate.** Applying absolute values with only |mu|<=1 and ordinary prime bounds yields at best the simple bound

\[
|\mathcal O_N(Q)|\ll N\log^3N.
\]

To see the quantitative loss, a progression has at most N/k+1 candidate n, each Lambda weight is at most log N; the centered global term is bounded using sum_{k<=K}1/phi(k)=O(log K), and the endpoint transfer pays another log N. The worst-case margin in (O-open) is guaranteed only at order N/log^2N. This argument therefore misses at least five logarithms, and contains no one-sided improvement. Replacing mu(N-n) by an arbitrary bounded weight in ordinary BV is invalid.

There is also a power-level deficit: Q=N^theta is below N^(1/2), whereas the switched moduli in (1) extend to N^(1-theta), above N^(1/2). At theta=49/100 these are levels 0.49 and 0.51 respectively. Ordinary BV does not control even the sequence f_N, regardless of that further level mismatch. Choosing theta>1/2 to shorten the twisted side makes (5) require an unproved ordinary distribution input instead. No inspected unconditional theorem supplies the needed combination.

## Attempt 2: a direct rough lower sieve and its bilinear replacement

Try to lower-bound the total rough-complement mass before distinguishing its odd factors. Use the nonnegative weighted sequence a_h=Lambda(N-h), 1<=h<N. For squarefree d coprime to N,

\[
\sum_{\substack{h<N\\d\mid h}}a_h
 =\psi(N;d,N)
 =\frac{N}{\phi(d)}+r_d,
\]

up to the harmless strict endpoint convention. Residues with gcd(d,N)>1 involve prime powers with base dividing N and can be split off. The local density for primes ell not dividing N is 1/(ell-1), a dimension-one sieve. Ordinary BV controls summed remainders through

\[
D=N^{1/2}/(\log N)^B.
\]

For z=N^alpha, the sifting parameter is

\[
s=\frac{\log D}{\log z}
 =\frac{1}{2\alpha}-o(1)\in[3/2,5/3]-o(1)
\quad(3/10\le\alpha\le1/3). \tag{11}
\]

The dimension-one lower-sieve threshold is 2, as recorded in the inspected Ford section 3.1. Thus the available ordinary distribution does not even give a positive universal lower-sieve coefficient for the entire rough set at this cutoff. It cannot yield the stronger odd-factor lower margin F_alpha from those sieve inputs alone. To cross this particular threshold one would need D>z^2=N^(2alpha), namely level greater than 0.6 to nearly 2/3 rather than 1/2. The level deficit is a factor N^(2alpha-1/2), between N^0.1 and nearly N^(1/6), before logarithmic losses. This is a failure of this attempted lower-sieve argument, not a proof that no arithmetic method can work.

One may instead try the Friedlander-Iwaniec bilinear prime-detecting sieve on a_h=Lambda(N-h)mu^2(h). Its Theorem 1 requires a distribution parameter D>N^(2/3), along with an additional bilinear bound. Substitution into its actual axiom (B) produces expressions of the form

\[
\sum_m\left|\sum_{\substack{M<k\le2M\\mk<N}}
 \gamma(k,C)\mu(mk)\Lambda(N-mk)\right|,
\qquad\gamma(k,C)=\sum_{\substack{d\mid k\\d\le C}}\mu(d). \tag{12}
\]

The squarefree indicator is redundant inside (12), since mu(mk) vanishes otherwise. The required ranges are Delta^(-1)*sqrt(D)<M<delta^(-1)*sqrt(N), 1<=C<=N/D, with the source's strong logarithmic saving and absolute outer sum. This is an explicit reflected-prime bilinear correlation. Ordinary BV neither provides its pointwise cancellation nor reaches the initial D>N^(2/3) requirement. The source theorem does not assert (12) for this sequence.

There is an additional uniformity obligation: as N varies, the local density function changes at prime divisors of N. A theorem whose implicit constants depend on a fixed density function cannot simply be applied uniformly to all N without checking those constants and Euler products. This proposal does not claim to have done so. Even granting that routine local-factor work, the analytic distribution and bilinear inputs remain missing.

The prior deletion countermodel can refute arguments using only properties it was proved to preserve. It cannot be used here as a shortcut to the failure or truth of (T-open) or (12), since its transplanted divisor identity and quantitative distributions were not proved. Likewise, almost-all results or a subpolynomial roughness theorem cannot be promoted to these target-uniform polynomial-cutoff hypotheses.

## Outcome and strongest preserved claim

The valid progress in this tranche is the endpoint-corrected reduction (8), the target-dependent one-sided sufficient bound (O-open), and precise failures of the two attempted unconditional estimates. Equations (O-open), (T-open), the original F lower margin, and the specialized bilinear axiom remain **unproved**. No new estimate across that gap has been established, so this is not a breakthrough on Goldbach.

The narrow next mathematical target is to prove a one-sided bound for the explicit signed operator (1) that beats its target-dependent squarefree gap, or to find a genuine arithmetic mechanism giving an odd-factor rough lower margin. Renaming these expressions, invoking a conditional theorem, or running further finite scans would not accomplish that task.
