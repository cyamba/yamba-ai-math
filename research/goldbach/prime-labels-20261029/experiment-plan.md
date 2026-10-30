# Preregistered prime-label algebra checks

29 October 2026. Independent experimenter for LABELS-005. Status: prepared before the dependent final run. This stage tests finite algebra and support, not the source manuscript's analytic theorem.

## Three comparisons

1. Evaluate the source weight exactly using distinct group-prime divisors, disjoint finite prime groups and rho in {1/2,2/3,3/4}. Check vanishing on rough integers when every group prime is at or below the rough cutoff. Check empty support whenever K required group primes exceed z and z^K>=N. Include repeated-prime examples distinguishing distinct omega from Omega. Use rational reciprocal-prime normalizations and preserve explicit support witnesses.
2. On every multiplicity vector of total degree 1, 2 or 3 over a three-prime alphabet, check the author's stated bounded-label reconstruction. Test any squarefree-only reconstruction separately on squarefree and repeated types. Use Fraction arithmetic for polynomial coefficients and provide the first excluded repeated-factor failure rather than silently treating distinct support size as Omega.
3. Check exact Mobius and Liouville padding on finite squarefree D and rough q, W(Dq)=W(D) under group-prime separation, and normalized/zero-normalizer mixtures on all {-1,0,1} coefficient sequences over a fixed four-element complement set. Find the smallest Mobius counterexample after removing coprimality and a counterexample showing coprimality alone does not ensure label separation. A zero mixture must be shown compatible with a nonzero original correlation.

After reading the final statement and before execution, comparison 2 is instantiated with the author's rho values {1/4,1/2,3/4} and formulas A1 through A7: bare interpolation, signed cell counts, mu-weighted R/F0 reconstruction, repeated-factor corrections, half-weight deweighting and norm costs 7, 53/3 and 323/16. A separate rho grid {1/2,2/3,3/4} remains a diagnostic comparison only.

## Scope and rules

Use only deterministic standard-library Python, exact rational arithmetic and small finite sets. Read the final author's statement before selecting its reconstruction formula, and run after the populated finite-check packet arrives. A small smoke run precedes the final run. Save all failures, exact witnesses, code hash, Python/platform and actual wall time in finite-results.json. Unknown inference usage and monetary cost remain unknown. Finite support and identity checks do not prove analytic cancellation, target-uniformity or Goldbach.
