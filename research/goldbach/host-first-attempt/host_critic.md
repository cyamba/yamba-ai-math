# Independent hostile test: cube-root parity statistic

Host-agent research, 28 October 2026. This is a mathematical countermodel for broad proof templates, not a counterexample to Goldbach and not a result about the actual primes. The construction was derived independently by two host workers, but has not been checked by a human mathematician or a proof assistant. Priority is unknown. The program uses a standard uniform upper sieve as an explicit external input, not an assumed lower bound.

## Question under attack

For even N and z_N=⌊N^(1/3)⌋, the ordered statistic on actual rough pairs satisfies T(N)=SS(N)−PP(N). Proving T(N)<0 for every sufficiently large even N would imply Goldbach. A negative average of T and the prime number theorem for all fixed residue classes do not control one target. The question is how sharp a counterexample can be made while retaining prime-factor structure.

## Countermodel proposition

There is a subset A of the actual primes, with D(x)=#{p≤x:p prime, p∉A}=O(x/log²x), for which:

1. A has the same leading prime number theorem in every fixed reduced residue class as the full primes.
2. Its cube-root-rough prime and semiprime pair statistics have the same leading dyadic averages as those of the full primes.
3. There are infinitely many even N with PP_A(N)=0 and SS_A(N)≥1. Thus the model's signed statistic T_A(N)=SS_A(N)−PP_A(N) is positive at those N, despite the same negative leading average.

**Precise model.** An A-prime is an ordinary prime belonging to A. An A-semiprime is the product of exactly two A-primes, counting multiplicity. Pair counts use a+b=N, both entries >z_N, every constituent prime factor in A and >z_N, and ordered pairs; the diagonal is counted once. The signed statistic uses (−1)^k for a product of k A-primes. This semigroup restriction is necessary: if one merely removes deleted primes from a sieve applied to all integers, deleted factors can pass the sieve and the two-factor classification no longer follows.

### Proof

Let N_0 be any fixed integer. Inductively choose an odd prime r_j>2N_{j−1} and put N_j=2r_j². For every ordinary prime-prime representation p+q=N_j, delete the larger endpoint max(p,q). Let A be the original primes minus all these deleted endpoints.

All deletions at stage j lie in [N_j/2,N_j]. Since r_j> N_{j−1}, no earlier deletion removes r_j; current deletions are at least r_j²>r_j, and later deletions are still larger. Thus every r_j remains in A. Conversely every ordinary prime representation of N_j has an endpoint deleted at stage j, so PP_A(N_j)=0. Because r_j³>2r_j², r_j>z_{N_j}; consequently (r_j²,r_j²) is a valid ordered diagonal semiprime pair, giving SS_A(N_j)≥1 and T_A(N_j)>0.

For the deletion bound use the standard upper-sieve estimate

R(N) ≪ [N/log²N] ∏_{p|N,p>2}(p−1)/(p−2),

where R is the ordered prime-pair count. Wu quotes Selberg's version as (1.2), https://www.impan.pl/shop/publication/transaction/download/product/82961 . For N_j=2r_j² the product is (r_j−1)/(r_j−2)=O(1), hence at most O(N_j/log²N_j) primes are deleted at stage j. If a stage contributes a deleted prime ≤x, then N_j≤2x. The N_j grow faster than a fixed geometric sequence; summing their bounds gives D(x)=O(x/log²x). For a clean bound, split the stages at N_j=√x: the earlier contributions total O(√x), and for the later ones all logs are comparable to log x while the geometric sum is O(x). The prime number theorem in a fixed reduced residue class then yields statement 1.

Fix a large dyadic X and write z_min=⌊X^(1/3)⌋. The number of ordinary cube-root-rough semiprimes m≤2X lost when requiring their prime factors to belong to A is at most

Σ_{p∉A, p≥z_min} π(2X/p),

with p≤2X/z_min implicit. Since 2X/p≥z_min and D(t)=O(t/log²t), Chebyshev's prime upper bound and partial summation give

Σ_{p∉A, z_min≤p≤2X/z_min} 1/p = O(1/log X),
number lost = O(X/log²X).

There are O(X/log X) rough semiprimes up to 2X, so pairs affected by deleting a factor have total O(X²/log³X). Pairs affected by deleting an A-prime have the same or smaller order. Therefore the original and model PP and SS sums over X≤N≤2X differ by o(X²/log²X). In particular the model has the same leading negative mean,

Σ_{even X≤N≤2X} T_A(N) ~ (3/2)[(log 2)²−1] X²/log²X,

while T_A(N_j)>0 for infinitely many targets. The mean uses the separately established rough-semiprime marginal asymptotic and standard PNT; this construction does not prove that marginal formula. □

### Stronger average information still survives

Let J_A(N)=Σ_{a+b=N; a,b∈A}log a log b. Summing the nonnegative difference J(N)−J_A(N) over N≤X counts each pair containing a deleted prime at most twice, so

Σ_{N≤X}|J(N)−J_A(N)| ≪ D(X)π(X)log²X ≪ X²/log X=o(X²).

Tolev's quoted mean-absolute Goldbach formula has error o(X²), https://www.impan.pl/shop/en/publication/transaction/download/product/83974 , so the A-model also has the same leading weighted Goldbach asymptotic for almost every even target. It does *not* inherit all of Tolev's arbitrary logarithmic-power error bounds. The model preserves principal singular-series behavior in this average sense, not necessarily all correlated input or a Bombieri–Vinogradov/Elliott–Halberstam distribution theorem.

## What this falsifies

Any abstract lemma that concludes T(N)<0 for each large N from only (i) prime PNT and fixed-modulus equidistribution, (ii) prime/rough-semiprime marginal asymptotics, (iii) the exact reflection identity, and (iv) the negative averaged T, is false. Even allowing natural semiprimes as products of modeled primes and a weighted almost-all Goldbach asymptotic is insufficient. This is an explicit failure of that *class of hypotheses*, not of a valid method using stronger N-uniform pair correlations, divisor identities, exact prime arithmetic or the Möbius-twisted hypotheses of Huang–Li. It does not demonstrate that those additional hypotheses fail for A; that would need separate proof.

A new pointwise lemma must therefore identify a property of the full prime indicator absent in this deletion model and must show how that property excludes N_j-style holes. One option is the maximal-in-y twisted arithmetic progression estimate in Huang–Li, https://arxiv.org/abs/2005.03811, but whether any OpenAI divisibility-graph theorem supplies that estimate is open. A subsequent preprint alleges an endpoint omission in the original argument and claims a repair under the full maximal hypothesis: https://zenodo.org/records/21939906. Both criticism and repair require independent checking. An overlapping recent programme involving cubic minorants is https://zenodo.org/records/23477014.

## Adversarial checks

`host_critic_check.py` uses direct integer factorization and verifies the identity and mixed-term reflection for every even 6≤N≤2000. It also checks the progression obstruction and quarter-root tie examples, and makes a finite model at N=98=2·7² by deleting the larger endpoints of all prime representations. The code separately restricts both modeled prime factors to A. See `host_critic_results.txt` and the script for output, Python version and precise scope. These exact finite checks are not a proof of the infinite proposition.

## Additional prior art found during this attempt

Bahboui, [Toward a Goldbach Proof: An Explicit Conditional Reduction](https://www.preprints.org/manuscript/202610.0809), posted 10 October 2026, explicitly discusses a Chen–Liouville discriminator and higher-odd-factor contamination. The preprint does not claim an unconditional Goldbach proof; its claims have not been independently verified here. Its overlap reinforces that no priority claim is made for the algebraic bridge.
