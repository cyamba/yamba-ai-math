# Independent mathematical review

29 October 2026. Registry role: Independent Critic. This is separate host-agent semantic review of the two mathematical-author reports. It is not external peer review, a proof-assistant check, or a statistically independent model experiment. No token or monetary measurements are available.

## Verdict

**Supported:** Proposition H, its fixed-epsilon consequence, the counterexample to a uniform pure-epsilon-squared bound without a remainder, the constant-one endpoint transfer lemma, the exact divisor-switch identity, and the endpoint sharpness witness. I found no missing Goldbach assumption or invalid inference in their stated arguments.

**Incomplete:** the overall Goldbach investigation. The parity-sensitive pointwise lower bound remains unproved. Neither accepted result establishes a breakthrough on the conjecture, and novelty is unverified. Proposition H is a classical upper-sieve consequence. The endpoint lemma is an elementary Abel-summation result with announced prior-art overlap.

One error in the inherited brief needs a separate erratum: its quarter-root statement permits four prime factors, although the strict roughness convention makes that impossible.

## Frozen reviewed inputs

The following SHA256 values identify the exact files read. I made no changes to them.

| File | SHA256 |
| --- | --- |
| `statement.md` | `2080964809f35c5b7403940f605fd2f301199e6e7307ca53804fcb33888cab1b` |
| `endpoint-lemma.md` | `6b2933efc684a804cbd5455357e367e054dac70b95282abab8df3dcb9ea7f7fa` |
| `survey.md` | `d177731977b44bf1a6522a6911ea789bf1fae9fcdba801f5ced3de37c69589f1` |

The populated counterexample packet supplied the completed statement-stage response. Review concerned the sharpened exceptional term `omega_{>N^alpha}(N)`, bounded by 3, rather than the earlier weaker `omega(N)` version.

## Proposition H audit

The exact statement is uniform over even N sufficiently large and all epsilon in [0,1/30], with alpha=1/3-epsilon. It bounds the number of prime summands p whose complement is a product of exactly three primes strictly exceeding N^alpha, with repetitions allowed. The numerical absolute constants are not extracted.

I inspected [Ford, Sieve Methods Lecture Notes, Theorem 2.5 and its proof, printed pages 19-21](https://ford126.web.illinois.edu/sieve2023.pdf). Its two-form bound permits nonzero integer coefficients, including a negative coefficient, and retains coefficient dependence in the singular series; its implicit constants depend only on the number of forms. The proof's residue-class errors and small-prime exceptions are already included. I also inspected [Tao, Mertens' theorems, Theorem 1, equation (1)](https://terrytao.wordpress.com/2013/12/11/mertens-theorems/), which supplies the bounded error in the log-weighted prime harmonic sum. These are the established imported inputs; I did not audit every result in either source.

The following load-bearing steps check out:

1. A counted p has one sorted factorization N-p=abc. Every factor lies strictly between z=N^alpha and Y=N/z^2. With m=ab, the actual permissible pairs satisfy m<N/z and x_m=N/m>z. This restriction is used before enlarging the nonnegative reciprocal-pair sum. The argument does not mistakenly apply the logarithmic lower bound to extra pairs introduced afterward.
2. If a prime ell divides both m and N, it divides the prime p=N-abc, so p=ell. Hence exceptional p are distinct prime divisors of N exceeding z. Four such distinct divisors would have product greater than N^(4alpha)>N; there are at most three, globally. The exception is not multiplied by the number of factorizations or sieve moduli.
3. In the coprime case, t and N-mt are primitive and admissible. At 2 there is one root, since m is odd and N even. At an odd ell dividing Nm there is one root, and otherwise there are two. Their singular series is exactly S(N) times the product of (ell-1)/(ell-2) over distinct prime divisors of m. There are at most two such divisors, each odd, so its ratio to S(N) is at most 4. Repeated factors reduce, rather than increase, this number of local factors.
4. The uniform two-form sieve applies to all c<=N/m. The enlargement drops c>=b and roughness of c only in an upper bound. It counts prime values near the endpoints rather than silently discarding small prime outputs. Since log(N/m)>alpha log N, its denominator has the required uniform lower bound.
5. The displayed Stieltjes summation identity follows from A(t)=log t+O(1). Its endpoint and integral errors are O(1/log z), uniformly even when the interval shrinks. The strict lower prime cutoff is implemented correctly by subtracting A(z). The resulting reciprocal-prime mass is O(epsilon+1/log N), with an absolute constant on alpha in [0.3,1/3]. Squaring it proves the claimed bound, including its uniform lower-scale term.

The counterexample to removing that lower-scale term is valid. For odd primes r tending to infinity, N=r^3+3 is even, q=r^3 has three repeated prime factors, and p=3 is permitted because only the complement is required to be rough. The prescribed epsilon_N places r strictly above the roughness cutoff while epsilon_N=O(1/(N log N)). Even the report's crude S(N)=O(N) bound makes the proposed pure-epsilon-squared upper bound tend to zero, contradicting H>=1. This refutes the bound uniform in epsilon(N); it does not refute the fixed-epsilon limit.

## Endpoint argument audit

For each admitted k, the strict integer cutoff is M_k=max(0,ceil(N-eta*k)-1). Its admitted weights w_k(n)=log(k/(N-n)) are negative and increasing. Discrete Abel summation bounds the weighted discrepancy by

    max_{j<=M_k}|E_k(j)| * (-w_k(M_k) + w_k(M_k)-w_k(1))
      = log((N-1)/k) * max_{j<=M_k}|E_k(j)|.

This verifies the constant one for arbitrary complex f and arbitrary coefficients after taking absolute values. The empty sum, M_k=1, k=1, and strict-boundary cases are handled. No prime cancellation is assumed. The prime-weighted corollary is correctly conditional on maximal endpoint discrepancy and pays one logarithm.

The divisor switch also checks out. For squarefree h=N-n, the bijection k=h/d gives mu(d)=mu(h)mu(k), and d>eta is exactly n<N-eta*k. For nonsquarefree h, both sides vanish because of their explicit ordinary Mobius factors. The outer bound k<(N-1)/eta is necessary, and no noncoprime contribution is deleted from the exact identity. The transfer lemma subsequently controls only the coprime part, as disclosed.

The witness N=10, k=3, eta=2, f(1)=f(8)=1 has full discrepancy zero in both reduced residues. Its moving weighted discrepancy is -(log 3)/2, with moving maximal discrepancy 1/2 and weight bound log 3. It attains the single-modulus bound exactly. Thus full-endpoint information alone cannot prove this general transfer lemma.

## Prioritized findings and remaining obligations

1. **P2, inherited input error, status refuted.** The original `orchestrated-prompt.md` says that at alpha=1/4 rough numbers may have four factors. Under its strict prime-factor condition P^-(q)>floor(N^alpha), every factor is actually greater than N^alpha. Four factors at alpha=1/4 would have product greater than N. For q<N, at most three factors survive. The four-cell P/S model is still nonexhaustive because triples can survive. Preserve the imported file and add a dated erratum with this exact correction. This error does not invalidate Proposition H or the endpoint lemma.
2. **P1, objective still incomplete, status conjecture.** Neither an upper bound for H nor maximal-discrepancy transfer provides the lower bound for F_alpha=(U_alpha-L_alpha)/2. The remaining condition `P-open` is sufficient but itself stronger than mere existence of a Goldbach representation, since it supplies a positive lower bound at the prime-pair scale after subtracting contamination. A new lower-bound attempt must identify an actual parity-sensitive input and prove it uniformly in the target. A negative average, Chen's unsigned count, or the statement of a twisted distribution conjecture does not fill this gap. This is a scope limitation already acknowledged by both authors, not an error in the two accepted propositions.
3. **P3, quantitative and priority limits, status unverified.** Effective numerical values of C and N0 have not been extracted, and no finite connection to the remaining initial range is available. No sufficiently broad closest-work comparison establishes novelty of Proposition H. The endpoint repair has announced prior-art overlap. Keep these claims as checked technical progress within the programme; do not promote them to a Goldbach breakthrough or a new result of established priority. A quantitative implementation would first need an explicit upper-sieve constant and a separately proved lower margin.

No mathematical revision is required for the accepted propositions. The narrowest defensible outcome is the pointwise contamination upper bound, the sharp finite transfer lemma, and the corrected strict-cutoff interpretation. The next decisive research check is a noncircular lower estimate for F_alpha whose proven margin exceeds the controlled contamination, or a concrete counterexample to a proposed such estimate. The independent finite experiment is useful for implementation and endpoint errors, but its results were not used to establish these infinite statements.
