# Result: limited moving-multiplier arithmetic averaging

29 October 2026. `GOLDBACH-RATIOS-007`. A complete elementary argument and separate substantive review establish the limited unweighted averaging estimate below. It is a scoped use of classical methodology, with novelty unverified. It does not solve Goldbach or establish a substantive demonstrated breakthrough towards its prime-correlation bound. The user objective remains active.

## Accepted estimate

For primitive positions P=(u,v) with U<=u<=16U, V<=v<=2V, U,V>=2 and gcd(uv,H)=1, let r_P=c/u modulo1 where u*d-v*c=1. Write N0 for their count, tau_H=2^omega(H), and S(H,k)=sum_P e(k*H*r_P) for nonzero integer k. The [accepted revision](revision.md), using the frozen [complete proof](statement.md), gives for every fixed eta>0

    |S(H,k)| <<_eta V*tau(|k|)
        + tau_H*sigma_(-3/4)(|k|)*U^(7/4+eta)*log(2U),

    N0 = 15UV*kappa_b(H)
        + O(tau_H*(U+V)*log(2U)),

    kappa_b(H) = zeta(2)^(-1)*product_(ell|H)(ell-1)/(ell+1).

The proof reconstructs its elementary complete Kloosterman3/4 bound by fourth moments and unit-scaling orbits. Interval completion retains every divisor of rad(H), short and empty intervals, endpoint rounding, nonunit Fourier frequencies and the Ramanujan main term. The key limited gain is gcd(k*H*d^(-1),u)=gcd(k,u) on the admitted coprime support. The target H therefore costs its divisor count rather than a new full congruence modulus in this calculation.

If U is comparable to H^a and V to H^b for fixed positive a,b with b>3a/4, then uniformly for nonzero |k|<=H^A at every fixed A,

    |S(H,k)|/N0 << H^(-gamma+o(1)),
    gamma = min(a,b-3a/4)>0.

A proved finite Fejer-majorant argument gives interval discrepancy of the same asymptotic power. In balanced boxes U,V comparable to sqrt(H), this is H^(-1/8+o(1)). Constants and the eventual threshold are not numerically extracted. This statement averages all admitted integer positions; it carries no prime weights or prescribed line/path restrictions.

For a periodic bounded-variation test function g, normalized error is controlled by Var(g) times discrepancy. Replacing the actual population N0 by leading mass M=15UV*kappa_b(H) requires both costs

    N0*Var(g)*discrepancy + |N0-M|*|integral(g)|.

The second term matters even for H-dependent constants of zero variation. Empty finite populations are kept unnormalized. The [separate critic](review.md) supports the stated proof and required this integration clarification.

## Assurance, checks and priority

Assurance is a complete self-contained elementary derivation plus a distinct host-agent substantive review. No proof assistant or external human peer verification was performed. The full external LWW theorem is not used as a validated dependency. [Closest-work inspection](closest-work.md) identifies established modular-inverse methodology and a stronger classical Weil bound; this calculation is not presented as a new general inverse-distribution theorem.

The [exact finite checks](finite-results.json) passed17 fourth moments at moduli2 through18,2,108 unit-orbit cases,2,695 collision eliminations,29,240 kernel-map inputs,1,960 interval expansions,132 Fourier completions,470 empty divisor intervals,133 nonunit-frequency cases and300 complement-phase groupings. The60 finite position domains include six empty populations;960 mass checks passed. Numerical error-scale comparisons remain diagnostics. Finite checks support identities and boundary handling, not the infinite analytic estimate.

All six actual host stages are retained under `.runs/goldbach-ratios-007-manual-20261029`. Nominal dispatch proxy cost14, checker preparation2 and closest-work inspection2 total18 within20. Actual inference usage and money are unknown. Offline replay checks response protocol only, with research_validated=false and no fresh inference. Manual preparation receipts remain distinct from actual completed host records.

Repository contracts pass. The full116-test suite retains10 failures and3 errors in existing unrelated Windows, timing and frozen-evidence paths, so it is not green; [repository-tests.json](repository-tests.json) records the current run. The new finite arithmetic checkers passed their declared executions. Original imported Goldbach files remain unchanged.

## Remaining actual research task

This resolves a limited unweighted complement-ratio average. It supplies no joint prescribed-prime-line average, high path-moment estimate, actual-prime cancellation, denominator-H major-arc prime estimate, or positive Goldbach margin. In particular arbitrary weights cannot be attached to an equidistribution statement without their own joint bound.

The next actual program is [ROOTS-008](../projective-roots-20261029/brief.md): derive or refute the joint ratio/projective-line count for determinantH matrices, tracking the true S and H dependence. Its author stage has started and its independent finite checker is preparing. This stronger statement is not assumed from the present estimate or from the source's determinant1 result. Even success would leave the prime/operator obligations explicit. The Goldbach objective remains active and unachieved.
