# Preregistered switching checks

Date: 29 October 2026. Independent experimenter for GOLDBACH-SWITCHING-004. Status at registration: the dependent finite-check stage has not run. Read the completed source survey and await the author's formula and populated packet before execution.

## Three primary comparisons

1. For every even 6 <= N <= 5,000, use exact integer cutoffs for beta in {1/8,1/6,1/5} and alpha in {3/10,8/25,33/100}. Independently compute U from smallest-prime-factor filtering and C_r by enumerating q=r*m with m=1 or no prime factor below r. Check U_alpha=U_beta-sum C_r in all nine cutoff pairs, and F_alpha=U_alpha-E_alpha at the three upper cutoffs. Include q=r, repeated factors, and least factors r dividing N. Cross-check through N=100 using independent trial division.
2. Verify the author's exact coefficient algebra. The proposed legal weakened cutoff is u(t)=min(t,(d-t)/2). The scoped family has d/4 <= beta < d/2, alpha in [3/10,1/3), alpha<d<=1/2. Check the linear-sieve parameter ranges and symbolic cancellation of beta logarithms. Give an exact rational sign certificate using log(x)<=x-1 and (d-alpha)/alpha<=2/3. This verifies coefficient algebra under the stated imported formula; it does not validate an analytic sieve remainder.
3. Independently integrate the legal piecewise upper coefficient by composite Simpson quadrature at 2,000 and 4,000 subdivisions, for d in {7/20,2/5,9/20,49/100,1/2}, the three alpha values, and beta/d in {1/4,1/3,2/5,49/100}. Compare with the closed form. The d=1/2 endpoint is an algebraic boundary check, not a claim that the source distribution theorem holds there. Use exact rational log enclosures for the resulting closed form as an additional certificate on this grid. No beta scan substitutes for the universal symbolic cancellation.

## Failure and resource rules

Preserve any failed exact identity or rational sign check. Numerical comparisons fail on error greater than 1e-8 times max(1,absolute value). All final coefficients must be negative within their certified rational enclosures. A negative coefficient refutes usefulness of exactly this minorant family, not Goldbach or all switching methods. A complete computation does not establish the imported asymptotic theorem or parity input.

Use deterministic standard-library Python and the fixed ranges above, with a small smoke run before the full evaluation. Save runtime, Python/platform, code hash, raw finite counts, worst discrepancies and failures in finite-results.json; save the exact algebraic certificate in coefficient-certificate.json. Token usage and monetary cost are unknown. No external provider or mutable action is part of this stage.
