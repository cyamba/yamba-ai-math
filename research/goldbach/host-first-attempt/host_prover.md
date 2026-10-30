# Host prover report: a countermodel for the cube-root Goldbach target

28 October 2026. This is a host-agent mathematical investigation prompted by the Yamba `GOLDBACH-PARITY-001` program. It is not an LLM worker execution inside the Yamba command backend. The proposed theorem below has been independently inspected by another research agent, not peer reviewed by a mathematician or verified in Lean. Its novelty has not been established. It does not settle Goldbach.

## Outcome

The requested pointwise inequality T(N)<0 remains unproved. I attempted to derive it from the negative dyadic mean, prime-density information and rough-semiprime marginals. The attempt fails in a precise way: there is a multiplicatively defined density-one subset A of the primes for which all these average inputs remain true, yet the corresponding signed rough-pair statistic is positive at infinitely many targets.

The result is not a counterexample for the actual primes. It shows that a proof using only these average or one-point inputs cannot distinguish actual primes from a pseudoprime system where the desired conclusion fails. Any successful proof must exploit further structure, such as uniform reflected correlations, a parity-sensitive bilinear bound or another property not preserved in the countermodel.

## Definitions

For a set A of actual prime numbers, define the multiplicative semigroup

  M(A) = {n≥1: every prime factor of n belongs to A}.

For even N≥6, let z_N=⌊N^(1/3)⌋. Define W_A(N) to be the ordered pairs (a,b) with a+b=N, a,b>z_N, a,b∈M(A), and every prime factor of ab greater than z_N. Let

  T_A(N)=Σ_(a,b)∈W_A(N) λ(a).

Every member of W_A(N) is prime or semiprime, because three prime factors each at least z_N+1 would multiply to more than N. Call the numbers of ordered prime–prime and semiprime–semiprime pairs PP_A(N) and SS_A(N). Reflection switches the two mixed types, so

  T_A(N)=SS_A(N)−PP_A(N).                                         (1)

Both summands are at least two. A diagonal pair is counted once. In this countermodel, **filter actual factorization by membership in A**. Merely omitting divisibility tests by deleted primes would let deleted prime factors pass as false survivors and would invalidate the two-factor classification.

## Proposition: negative mean does not force pointwise negativity

There exists a decidable set A⊂ℙ such that:

1. The number of excluded primes satisfies

   #{p≤x:p∉A}=O(x/log²x).

   Hence A has the same prime number theorem and, for each fixed reduced residue class, the same prime-number-theorem asymptotic as ℙ.

2. With the cube-root rough pair definitions above, T_A(N)>0 for infinitely many even N.

3. Its dyadic signed mean is the same as for all primes:

   Σ_(X<N≤2X, N even) T_A(N)
      ~ (3/2)((log 2)²−1) X²/log²X < 0.                           (2)

In particular, an argument based solely on a negative mean of this strength plus the listed one-point prime and rough-semiprime densities cannot prove the pointwise criterion for all large targets.

### Construction

Choose an odd prime r_1≥3 and put N_1=2r_1². At stage j, enumerate the finitely many actual prime pairs p+q=N_j and delete the larger prime from each pair, deleting the unique value once if p=q. Then choose r_(j+1) as the least prime strictly larger than 2N_j, and set N_(j+1)=2r_(j+1)². Let A be the primes remaining after all stages.

This is a finite algorithm at each stage. Membership of a given prime in A is decidable: a stage can only delete primes at least N_j/2, so only finitely many stages can affect a fixed prime.

### Proof of property 2

For every j, r_j is not deleted. Earlier stages remove primes no larger than N_(j−1)<r_j. At stage j, a deleted endpoint is at least N_j/2=r_j²>r_j. At later stages every deleted endpoint is still larger. Thus r_j∈A.

By construction PP_A(N_j)=0: each true prime-pair representation of N_j had at least one endpoint deleted. On the other hand, r_j²∈M(A), is a semiprime, and its two factors exceed ⌊(2r_j²)^(1/3)⌋ because r_j³>2r_j². Therefore (r_j²,r_j²) belongs to W_A(N_j) and contributes to SS_A. By (1), T_A(N_j)=SS_A(N_j)≥1.

### Proof of property 1

A standard Goldbach upper sieve gives, for large even N,

  R(N) ≪ N/log²N · ∏_(p|N,p>2) (p−1)/(p−2).

This is explicitly stated, with a stronger constant, in J. Wu, *Chen's double sieve, Goldbach's conjecture and the twin prime problem*, §1, equations (1.1)–(1.2): https://www.impan.pl/shop/publication/transaction/download/product/82961 . For N_j=2r_j² the product has the single factor (r_j−1)/(r_j−2)≤2. Stage j therefore removes O(N_j/log²N_j) primes.

Because N_(j+1)>8N_j², the N_j grow faster than geometrically. Only stages with N_j≤2x can remove a prime ≤x. Split these into N_j≤√x and N_j>√x. The former have total O(√x), while the latter have comparable logarithms and geometric total O(x); hence

  #{p≤x:p∉A} ≪ x/log²x.

This is o(x/log x). Subtracting the deleted primes from the usual prime number theorem, and from the prime number theorem in a fixed reduced residue class, proves property 1. □

### Proof of property 3

Write D(t)=#{p≤t:p∉A}. The preceding bound gives D(t)≪t/log²t. Fix X and let z=X^(1/3). Consider true semiprimes q≤2X with both prime factors greater than z that use at least one deleted prime r. Their count is at most

  Q_bad(X) ≤ Σ_(r deleted, z<r≤2X/z) π(2X/r).

For each r in this range, 2X/r≥z, so the standard prime-counting upper bound gives

  π(2X/r) ≪ X/(r log X).

Partial summation using D(t)≪t/log²t gives

  Σ_(r deleted, z<r≤2X/z) 1/r = O(1/log X),
  Q_bad(X)=O(X/log²X).

The number of all z-rough semiprimes ≤2X is O(X/log X), by PNT and prime harmonic summation. Likewise π(2X)=O(X/log X). It follows that, over even X<N≤2X, the total loss of PP pairs is at most D(2X)π(2X)=O(X²/log³X), and the total loss of SS pairs is at most twice Q_bad(X) times the rough-semiprime count, also O(X²/log³X). The actual cutoff z_N≥X^(1/3), so these estimates safely dominate losses for all the moving cutoffs in the block.

Consequently

  Σ_(X<N≤2X, N even) [T_A(N)−T_ℙ(N)] = O(X²/log³X).             (3)

The prime number theorem and the rough-semiprime integral give the previously derived dyadic average

  Σ_(X<N≤2X, N even) T_ℙ(N)
      ~ (3/2)((log 2)²−1) X²/log²X.

Here the rough semiprime marginal is log 2 times the prime marginal: for z=X^(1/3), write each semiprime as rs with r≤s and sum the PNT approximation π(uX/r)−π(r)+1 over primes r∈(z,√(uX)]. Partial summation yields the factor ∫_(1/3)^(1/2) dt/[t(1−t)]=log 2. The normalized prime and rough-semiprime counting measures converge to Lebesgue measure with masses 1 and log 2. Their respective product measures on the band 1<u+v≤2 have area 3/2. For X<N≤2X, replacing N^(1/3) by X^(1/3) changes only numbers with a prime factor in a fixed-multiple interval near X^(1/3); PNT bounds their aggregate effect by O(X²/log³X). This is a special case of the standard rough-number framework surrounding Buchstab's function; see Tao's exposition https://terrytao.wordpress.com/2015/01/04/254a-supplement-4-probabilistic-models-and-heuristics-for-the-primes-optional/ . Equation (3) transfers that negative main term to T_A, proving property 3. Note that this mean calculation is separate from the pointwise conclusion and requires the moving-cutoff estimates; it is not a formal Lean verification. □

## Finite illustrations

Each row independently deletes the larger endpoint of each actual Goldbach pair at N. These individual finite examples illustrate the construction; they are not the globally nested set A from the proposition.

| r | N=2r² | Cutoff | Deleted primes | PP_A | SS_A | T_A |
|---:|---:|---:|---:|---:|---:|---:|
| 3 | 18 | 2 | 2 | 0 | 1 | 1 |
| 5 | 50 | 3 | 4 | 0 | 1 | 1 |
| 7 | 98 | 4 | 3 | 0 | 1 | 1 |
| 11 | 242 | 6 | 8 | 0 | 1 | 1 |
| 13 | 338 | 6 | 9 | 0 | 7 | 7 |

For N=18, deleting 11 and 13 removes 7+11 and 5+13, while 9+9 remains a rough semiprime pair. Mixed 3+15 and 15+3 cancel in the signed sum.

## Remaining theorem obligation

The countermodel retains the actual primality factorization but deliberately removes a sparse, target-dependent set of prime generators. A route to Goldbach must use a property of the complete prime set that this adversarial A fails. Candidate input: a one-sided, N-uniform bound on the reflected prime-versus-rough-semiprime correlation after removing major-arc local factors. Huang and Li provide an existing conditional route using a precisely stated Möbius-twisted distribution hypothesis: https://arxiv.org/abs/2005.03811 . Their theorem is conditional, and no argument here proves the required hypothesis or the pointwise signed bound.

A decisive follow-up is to determine how the countermodel behaves under the **exact** twisted distribution hypotheses in Huang–Li, and under whatever specific centered-divisibility graph estimates are proposed from OpenAI mathematics. If the countermodel satisfies the proposed input, the input is too weak; if it fails, identify and prove the missing uniform estimate for the actual primes. Any such pointwise estimate is genuinely open in this report. No pointwise bound, Goldbach proof or novelty claim is made.
