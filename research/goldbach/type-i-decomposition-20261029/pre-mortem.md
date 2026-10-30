# Separate pre-mortem for reflected decomposition and Type I

29 October 2026. Independent Critic, supplemental preparatory dispatch for `GOLDBACH-TYPEI-013`. I read the new brief, initial survey and actual statement-stage packet as framing, with the survey upstream not yet populated, then the pinned Guo convolution/rectangle text at lines 531-636 and reflected specialization of its Type-I argument at lines 2973-3108. This is not a main review or acceptance of the forthcoming author proof. Only this file is owned. Earlier frozen evidence is preserved, and no usage measurements are available.

## Primary BV statement inspected

The root supplied the public author PDF and rendered journal page 115 of Murty-Vatwani, *A remark on a conjecture of Chowla*. I independently viewed that image and checked these local hashes:

| Primary artifact | SHA256 |
| --- | --- |
| `.runs/goldbach-source-inputs-20261029/murty-vatwani-chowla.pdf` | `8c24673584e4bf71975467b39b33b48806a1dce410510a262d4b81d102e6257e` |
| `.runs/goldbach-source-inputs-20261029/murty-vatwani-journal115.png` | `c85318cfbc666f23797b305cb3e07d516ee6235a8b01825e9d8a92b400573009` |

The [author's public PDF](https://mrammurty-ai.github.io/chowla.pdf), Proposition 3, visibly states that every A>0 admits B>0 such that

    sum_{q<=sqrt(X)/(log X)^B} max_{a mod q} max_{Y<=X}
       |sum_{n<=Y,n=a mod q} mu(n)| << X/(log X)^A.

It includes all residue classes as printed, not only reduced classes, and is attributed there to Corollary 1 of Siebert-Wolke. This is primary statement inspection in Murty-Vatwani, not independent inspection of the original cited proof. The intended narrower reduced-class use and differences of two endpoints are permitted. The old Queens URL's failed access is superseded by this new primary evidence, without rewriting earlier records.

## 1. P1: exact convolution and both prime-power corrections

The stated Vaughan identity is algebraically sound. Using log=1*Lambda, the difference of the second and third terms is mu_{<=U}*1*Lambda_{>V}; adding the final mu_{>U} term gives mu*1*Lambda_{>V}=Lambda_{>V}. The remaining Lambda_{<=V} restores Lambda exactly. On a dyad above y>V the latter short term is absent. Complete multiplicativity of the Z-rough indicator then gives the displayed T1,T2,T3, with the actual c_V(n)=sum_{ell|n,ell>V}Lambda(ell). For T2, the coefficient at q=d*ell is bounded by sum_{ell|q}Lambda(ell)=log q after absolute values.

The passage to prime-only sums needs two different corrections. Removing R_Z on the von Mangoldt sum costs prime powers with base at most Z; a ratio-two interval has at most one power of each fixed prime. Removing the remaining higher powers is still necessary. For instance, with Z=2 and F supported at 9, a von Mangoldt sum has log 3 while the prime-only sum is zero. This is a finite witness to dropping only the first correction. The proposed O(Z)+O(sqrt(y)*log^2 y) bounds are compatible with bounded F and partial dyads.

Decisive author check: write the convolution before any asymptotic estimate, retain both errors, and keep the positive shifted argument in F. Neither correction is supplied by a later Type-II result.

## 2. P1: expose product boundaries without changing the analytic coefficient roles

For a rectangle with MN comparable to y, count a product boundary strip using the shorter variable only as the counting variable. The sum of O(delta*y/m+1) over it is O(delta*y+sqrt(y)), with fixed coefficient losses. This does not require exchanging the arithmetic roles of the Mobius and long-prime-factor coefficients. Smoothing only the prime-variable product cutoff and Mellin inversion give common phases m^(iv)n^(iv). The positivity endpoint and mu(H-mn)W(H-mn) remain in the bounded target and are not differentiated.

The actual coefficients needed by ENERGY-012 remain mu(m)R_Z(m)m^(iv) and c_V(n)R_Z(n)n^(iv), with their permitted unit factors. A symmetric exchange used for an auxiliary Type-II difference does not establish the analytic energy theorem with arbitrary arrays or reversed arithmetic roles. The frequency range from the smoothing, for example L^(2B_s), and the transform's fixed log-power integration loss must be chosen before fixing the later energy height. Reusing an earlier smaller phase window would be a genuine range gap.

Unit removal is quantitative. A common factor of a sifted variable and H exceeds Z; counting those multiples gives O(MN*omega(H)/Z), with the explicit coefficient log factor. In Type I the outer q<=y^(2/5) has the same divisor budget and a smaller-power endpoint contribution. All these errors remain negligible after fixed logarithmic integration losses. An entrywise positive-product mask must not be inserted into a signed operator on the assertion that its norm is unchanged; PAIRING-011 handles the original target's positivity through its separate nonnegative cofactor enlargement.

Decisive author check: expose both product endpoints, calculate the strip and Mellin losses, and state the exact phase window and coefficient roles passed to the later accepted inputs.

## 3. P1: use finite expansions and count every positive remainder

Keep k odd before expanding its remaining small-prime exclusion. A finite Bonferroni polynomial of depth C_I*log L involves only odd squarefree r<=Z^(C_I*log L+1)=H^o(1). The positive omitted-order divisor sum has factorial reciprocal mass, since sum_{p<=Z}1/p=O(log L). It is not legitimate to use the entire primorial as a modulus and appeal to BV.

The single-band Taylor identity for u*rho^(u-1)/V is correct with coefficient (j+1)(rho-1)^j/V on divisors having j+1 prime factors. Its remainder is bounded by (R+1)(1-rho)^R/V times the positive order-R+1 divisor sum. The same identity covers u=0 and all smaller u by zero terms. Its reciprocal remainder mass is O(1/R!), and its retained absolute reciprocal mass is bounded, including the 1/phi(d) variant because the eligible band sums are eventually below one. Multiplying K bands needs a telescoping positive-error argument; a truncated polynomial should not be assigned the pointwise uniform bound of the original W.

For r|k and d|H-qk, a common prime of r,d would divide H, impossible because every d prime is eligible. For the other terms q is coprime to d by roughness. With parity retained, these conditions give at most O(y/(q*r*d)+1) solutions. Reciprocal masses control the main terms of every finite remainder. The total absolute coefficient counts of retained r,d are H^o(1), so all +1 terms are at most y^(2/5+o(1)), before fixed logarithmic losses. This is the finite endpoint count needed in addition to factorial means.

Decisive author check: display the positive remainder majorants, both reciprocal and absolute coefficient masses, and their CRT counts. Do not infer an arithmetic truncation error solely from an independent-model mean.

## 4. P1: extract g, retain smooth prime powers and keep parity

Set g=gcd(r,H), with r odd squarefree, q Z-rough and coprime to H, and d disjoint from r. Then g is odd squarefree, d and g are coprime, and the exact local identity is

    mu(d*g*v)=mu(d*g)
       *sum_{b|v, all prime factors of b divide d*g} mu(v/b).

Arbitrary powers in b are essential. For dg=3 and v=9, the full supported b set {1,3,9} gives mu(27)=0, whereas retaining only squarefree b={1,3} gives one. This is a minimal useful finite falsifier of that tempting truncation.

Writing H-q*r*j=d*g*b*t gives

    t = (H/g)*(d*b)^(-1) mod (q*r/g).

The inverse exists: d avoids q,r; every prime of g has been removed from squarefree r and is absent from q; b uses only d,g primes. Also H/g is coprime to q*r/g. There is no need to impose gcd(g,db)=1. Without extracting g, a direct appeal to a reduced-class estimate would have the wrong hypothesis; for example H=30,q=7,r=3 has H-q*r=9 in a nonreduced class modulo 21. The inspected BV statement is stronger, but the present proof should retain its transparent g-specific factorization and scales rather than silently changing routes.

Since H is even and q,r,d,g,b are odd, odd j is equivalent to odd t. Combining this parity with the odd-modulus congruence produces a reduced class modulo 2*q*r/g. Omitting the 2 admits even t and even j that the original k-rough support forbids. Translated or reversed positive t intervals are differences of two endpoints; they do not alter the modulus or inverse.

Decisive author check: prove the displayed identity and inverse prime by prime, explicitly retain all supported b powers, and write the odd CRT class before applying BV.

## 5. P1: the BV scale and both large-b Rankin costs must remain separate

For d*g*b<=y^(1/20), the containing scale Y0=(H+3y)/(d*g*b) is at least y^(19/20), with log Y0 comparable to L. The largest reduced modulus is y^(2/5+o(1)), whereas sqrt(Y0) is at least y^(19/40). The positive exponent gap is 3/40, enough for every fixed BV log loss. This must be applied at each fixed g,d,b and its actual Y0, then summed with its reciprocal factor 1/(d*g*b). Grouping q*r/g is particularly safe because q has primes above Z and r/g primes at most Z; any more general divisor multiplicity can be bounded by the stated tau-weighted Cauchy argument. Applying one common BV scale before extracting g would obscure the actual coefficient and level accounting.

The weighted BV bound follows from ordinary BV and Cauchy using the trivial error E(Y0;m)<=Y0/m+1 and sum tau(m)^2/m=O(log^4 Y0), at a sufficiently larger fixed precision. The remaining sums in g,d,b cost only fixed powers of L when their true reciprocal weights are retained.

If d*g*b>y^(1/20), retained d*g=H^o(1) implies b>y^(1/25) eventually. The supported prime set of d*g has only O_{K,A}(log L) distinct primes. For each fixed positive exponent eta its Euler factors (1-p^(-eta))^(-1) are bounded individually, so their product is L^O(1). Rankin at 1/2 therefore gives reciprocal tail O(y^(-1/50)*L^O(1)), while Rankin at 1/20 bounds the number of supported b up to H+3y by y^(1/20)*L^O(1), using H/y<=L^B. Counting the equation absolutely gives O(y/(d*b*q*r)+1). Its reciprocal part has the power saving; its endpoint part totals y^(9/20+o(1)). These are different estimates. Applying the Euler product to every prime below Z instead of the O(log L) supported primes would invalidate its polynomial bound.

The log k factor in T1 should be restored by real-weight partial summation only after a bound uniform in both endpoints, costing one fixed logarithmic power. This is precisely where the max-over-endpoints in the inspected BV input is useful.

Decisive author check: retain every g's scale, divisor multiplicity and reciprocal factor, then prove both Rankin estimates and all endpoint counts. The exponent margin alone does not establish the truncated Type-I sum.

These checks identify a viable bounded route and exact failure witnesses for omitted hypotheses. They do not accept a Type-I theorem before its frozen author proof and main packet, or establish any weighted prime Mobius consequence, removal of W, polynomial-roughness margin or Goldbach result. The ENERGY-012 main critic packet takes priority when supplied.
