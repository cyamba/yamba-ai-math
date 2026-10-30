# Independent review of the moving-sector construction

29 October 2026. Registry role: Independent Critic, `GOLDBACH-SECTORS-006`. This is separate host-agent mathematical review, not formal verification or external peer review. No token or monetary measurements are available.

## Verdict and frozen input

**Supported:** the exact whole-kernel sector conjugacy for the deliberately defined full-pullback centered operator; the coprimality and small-label primitivity checks under their stated hypotheses; the per-sector and aggregate point-count formulas and error bounds; the aggregate relative asymptotic in the stated polynomial-size regime; and the uniform fixed-transition exact-edge bound. The final review also proves the sharper exact-domain bound of at most two partner positions, and at most one when H is even.

**Incomplete:** any target-uniform arithmetic cancellation for the actual Goldbach decomposition, the new major-arc problem, or the source's list-constrained root moments. The construction changes the comparison arcs, and its finite conjugacy does not supply the missing estimates on those arcs. No Goldbach lower bound or demonstrated breakthrough follows. Novelty remains unverified.

The reviewed statement SHA256 is `622e03bca08c00023894cfb98c892c7831a8aef6980cf00775aa6d7aa78291f9`. The reviewed survey SHA256 is `a414c745de82d8ddc3b0d4cfc06791b16d77d9ff53251f2c3ba245b30192b21e`. The populated counterexample packet supplied the completed statement-stage response. I changed neither input.

## Source assurance

I inspected [Lue-Wang-Wu, equations (4.18)-(4.28) and the root-averaging setup](https://arxiv.org/html/2610.20242v1). The source retains exact transformed domains and counting-space measures in its fixed-shift construction; its root-averaging argument has additional arithmetic hypotheses and a restricted prescribed-modulus range. That inspection does not validate the full manuscript or extend it to moving H. The accepted claims in this review follow from the separate elementary arguments supplied in the statement, rather than an assumed extension of the source's analytic theorem.

## Exact congruence and Fourier identities

If u is coprime to H, the residue c=v*u^(-1) mod H exists uniquely. The proposed map has integral image exactly when v=c*u mod H and has the stated inverse. Its exact image domain is the given parallelogram. Since gcd(u,H)=1,

    gcd(u,c*u+H*w)=gcd(u,H*w)=gcd(u,w),

so primitivity is preserved. The sector index must remain part of the target state: transformed integer positions from different sectors can coincide as bare pairs.

Writing the H inverse branches of multiplication by H on the circle gives the exact Fourier identity (2). The branch average is zero unless H divides the integer frequency; when it does divide, the H branches cancel the individual Jacobian factors. Thus there is no residual 1/H in the nonzero term, and total arc measure is preserved.

For a common first-coordinate divisor D, coprimality of both first coordinates to H implies gcd(D,H)=1. The determinant expansion is

    t = H*det(P',Q')/D + (c'-c)*u*u'/D.

Both displayed quotients are integers because D divides u and u'. The second quotient is a unit modulo H. Hence H divides t exactly for equal sector residues. Since the comparison frequency is t-H*(b-a), the full centered bracket also vanishes across unequal sectors. This conclusion would not follow from the exact-edge condition alone.

Within one sector the determinant, exponential phase and explicitly rescaled smooth cutoff reduce to coefficient one exactly. The complement transformation is correct: if u*s-v*r=1, then (H*r,s-c*r) is an integral determinant-one complement to the image of P. Consequently its complement ratio is H*r_P mod 1. Changes of the original complement alter this ratio only by integers.

First coordinates, all associated lists, and the stated list/damping measures remain unchanged. The pullback is therefore an isometry of the discrete state spaces without inserting an area Jacobian. The good-state projections agree only when defined using the transported ratio H*r_P, as stipulated. List permutations and those projections preserve sectors. The unitary identity, adjoint transformation, finite-moment identities, and maximum-of-block-norm assertion follow. None is a norm estimate.

## The changed arcs are a real arithmetic obligation

The statement correctly defines a new candidate comparison operator. The full pullback of a small arc about zero includes arcs about every j/H. Those with numerator coprime to H have reduced denominator H. For a general rational center the reduced denominators can involve H as well. Equal total measure provides no estimate of prime exponential sums on these new arcs.

A small test makes the distinction explicit. Take H=2, P=(1,1), Q=(1,2), and D=1. These are primitive unit-first-coordinate positions in different sectors, and t=1. A full pullback integral is zero at its odd frequency. Keeping just the branch around zero gives the stated nonzero sine integral; keeping an ordinary small-denominator arc likewise need not give zero. Thus the cross-sector conclusion genuinely requires the full pullback. It is not a property of an arbitrary preexisting major-arc decomposition.

No bound already proved for the original ordinary small-denominator major arcs has been shown to control this comparison. The statement explicitly retains that missing step. Likewise, multiplication by H preserving Haar measure is not arithmetic equidistribution of the actual complement ratios. The source's high moments or root-averaging result cannot be applied solely from the finite conjugacy.

## Coprime input, multiplicative carry, and primitivity

Removing actual prime inputs dividing H costs at most omega(H) counts, and at most omega(H)log H in the stated logarithmic weighting. For von Mangoldt input, each prime base dividing H contributes at most log H over its powers below H. The asserted total bound is valid.

Multiplying an exact Vaughan decomposition by the unit indicator is an algebraic operation: a product is coprime to H exactly when each factor is. Thus the restriction can be carried into the corresponding factor coefficients. This justifies unit factors in that deliberately restricted decomposition; it is not an assertion about arbitrary coefficient arrays or a new analytic estimate for their sums.

For those unit products, every selected divisor of H-mn is coprime to H. Hence both coordinates of P=(D*b*m,s) and Q=(D*a*r,n) are units, and the occupied original sectors have c coprime to H. Their transformed second coordinates need not be units. The statement correctly keeps only a unit-first-coordinate restriction in the transformed block notation.

The primitivity argument is valid under its explicit original small-label hypotheses. A prime ell dividing both coordinates of P would exceed Z because s is Z-rough. It cannot divide D*b, all of whose factors are smaller than Z, so it divides m and is coprime to H. It is also coprime to D, and therefore divides t. The full-pullback bracket implies H divides t, so ell divides t/H. The stipulated cutoff |t/H|<Z forces t=0. Finally b>1 and gcd(b,a*r*s)=1, obtained from the small-label/sift separation and gcd(a,b)=1, rule out t=0. The argument for Q is the same.

There is no circular use of primitivity here: the Fourier support identity itself needs only integral t and unit first coordinates, so it can be used before proving primitive endpoints. Polynomial labels violate the small-label separation used in this proof, as the statement acknowledges. Nor may the compressed unit-first-coordinate identity be applied to an unrestricted abstract state space by claiming its discarded mass is small. For example, a state space supported at the primitive point (2,1) when H=2 has all its mass outside that restriction. The small discarded mass is justified only through the actual prime-input restriction and multiplicative carry.

## Domains, densities and point-count errors

The domain area is 15UV/H and its vertical slice height is V/H. Its smallest containing axis-parallel rectangle has height (V+15cU)/H for c in [0,H), giving exactly the stated area ratio. Negative transformed second coordinates are allowed in the exact domain. Replacing it by a positive rectangle from the source would be a different construction.

For the per-sector count, insert the exact Mobius identity for gcd(u,v)=1. Only g coprime to H can contribute because u is a unit. After scaling, the congruence remains v0=c*u0 mod H. The number of admissible u0 is

    15U*phi(H)/(gH)+O(2^omega(H)),

and each has V/(gH)+O(1) admissible v0. Bounding the latter error by the actual number of integer u0 gives the fixed-g error

    O(2^omega(H)*V/(gH) + U/g + 1).

Summing through B=min(16U,2V) gives the stated logarithmic errors and B term. Extending the reciprocal-square main sum costs O(UV/(HB)). Its Euler product is exactly

    (phi(H)/H)*sum_{(g,H)=1}mu(g)/g^2
      = zeta(2)^(-1)*product_{ell|H}ell/(ell+1).

This proves (7) uniformly in H and c, including the closed-interval endpoint errors. It does not promise a small relative error. In particular the U log(2B) term can dominate the main sector scale in thin boxes.

For both-unit positions, count each scaled interval by its own coprime inclusion-exclusion formula and multiply. Summing its errors gives exactly the two terms involving 2^omega(H) and its square in (8). Its reciprocal-square tail is O(UV/B), and its coefficient is

    (phi(H)/H)^2*sum_{(g,H)=1}mu(g)/g^2
      = zeta(2)^(-1)*product_{ell|H}(ell-1)/(ell+1).

The density relation (phi(H)/H)*kappa_u(H)=kappa_b(H) is correct. It agrees with the number of unit sectors and their transformed areas. H and its prime divisors remain part of the density; it is not the source's fixed parity constant.

If H^delta<=U,V<=H^C, the aggregate error divided by its main term tends to zero. Indeed 2^omega(H)=H^o(1) and kappa_b(H)=H^(-o(1)); these elementary bounds follow by separating finitely many small primes from large primes. Each displayed relative error is then bounded by H^(-delta+o(1)) times a logarithm at worst. This establishes an aggregate position asymptotic. It does not count prescribed list lines, complement-ratio intervals, or high-moment paths, and it is not thin-sector root averaging.

## Fixed-transition exact edges

For a primitive fixed P', all integer solutions to det(P',Q')=D*(b-a) differ by integer multiples of P'. Their first coordinates are separated by P'_1>=U inside an interval of length 15U. The stated bound 17 is therefore safe; the elementary count already gives at most 16 with these closed intervals. Extra list and parallelogram restrictions can only decrease it. The conclusion applies to a fixed label transition and exact determinant. It cannot be summed as an estimate for the major-arc comparison or a complete list operator without controlling their additional terms.

**Stronger reviewed corollary using the exact domain.** Keep the same sector and the exact parallelogram, and write every candidate as Q'=Q0'+jP'. Since T_c^(-1) is linear, its preimage is Q=Q0+jP. The original second coordinates lie in [V,2V] and are separated by v_P>=V. This interval has length V, so at most two integer values of j can occur. If there are two, they are consecutive and v_P=V. When H is even, every allowed first coordinate is odd. Adding P changes first-coordinate parity, so at most one of those consecutive candidates retains the unit-first-coordinate condition. Thus there are at most two partner positions for general H and at most one for even H. This improves the frozen statement's conservative 17 without altering its proof or its scope. It counts positions for fixed D,a,b, not all possible lists or the nonexact comparison term.

## Findings and limits to preserve

No mathematical repair is required for the frozen statement. The following are essential integration limits, rather than errors in the accepted finite results:

1. **P1, changed comparison unresolved.** The new pullback arcs include denominator H and are not an already controlled ordinary major-arc term. Any use in a Goldbach reduction must prove the corresponding prime exponential-sum or centered-operator estimate, including its H dependence. The conjugacy alone supplies no arithmetic cancellation.
2. **P2, root averages are stronger than position counts.** Formula (8) gives an aggregate position asymptotic under its explicit size conditions; formula (7) can have a large relative error in a thin sector. Neither establishes the source's inverse-ratio, prime-line, or high-moment average. Adding modulus H to a theorem outside its range is not justified by either count.
3. **P2, compression and primitivity hypotheses matter.** Preserve the prime-input coprimality carry, unit-first-coordinate restriction, exact domains, full H-fold arc pullback, and original small-label/sift separation. Without them, the elementary counterexamples and failed primitivity reasoning above can occur. The polynomial-label obstacles from the prior tranche remain.
4. **P3, assurance and objective.** The finite identities and elementary quantitative counts are supported by the arguments reviewed here. They do not validate the full source manuscript, establish novelty, or provide a Goldbach lower bound or demonstrated breakthrough. The revision may use the stronger reviewed partner bound of two, or one for even H, but no effective list-constrained norm bound follows from this exact-edge count alone.

The next missing result is a genuine target-uniform centered-operator or root-moment estimate on the exact transformed domains, with the changed arc and list-modulus dependence included. The statement preserves that obligation accurately.
