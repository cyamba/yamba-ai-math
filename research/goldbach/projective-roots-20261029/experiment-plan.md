# Preregistered determinant-H root checks

29 October 2026. Supplemental preparation for ROOTS-008. Status: preparation only; no checker execution. Read the final frozen author statement and populated packet before instantiating and running its formulas. Preserve all prior frozen research files.

## Three comparisons

1. For even H=2 through 20, u=2 through 30, v=1 through 20 with gcd(u,v)=1 and both coordinates coprime to H, compute canonical c_H in [0,u), d_H, determinant H and first-row primitivity exactly. Check local row kernels at the small prescription primes, including p dividing u, c_H, v or d_H. Use exact projective-line canonical representatives. Include omitted-unit hypotheses and the supplied H=6,S=3 horizontal-line impossibility witness.
2. Enumerate complete residue matrices of determinant H modulo S for odd squarefree S in {3,5,7,15} and even H=2 through 12 coprime to S. Check every prescribed tuple of first-row kernel lines has the same count, total S^3*product(1-1/p^2), and count S*phi(S) per prescription. This exact finite local calculation tests the factor product(1/(p+1)); it does not prove a uniform count in thin real boxes.
3. Count admitted primitive positions directly at even H=2 through 20, S in the same set with gcd(S,H)=1, U in {2,3}, V in {2,3,5}. Use the final author's endpoint convention, provisionally half-open normalized intervals. Test full normalized rectangles and one smaller subrectangle. For ratio intervals [0,1), [0,1/3), [1/3,2/3), [2/3,1) and [1/4,3/4), sum all root prescriptions back to the unweighted ratio count, and sum the three partition pieces back to the full count for every prescription. Any asymptotic main/error comparison is diagnostic only and will be instantiated from the actual statement.

## Execution boundary

The smoke domain uses H<=6, u<=8, v<=8, S in {3,5}, U=V=2 and the full normalized rectangle. The final domain is above. No large prime scan or provider call is part of the stage. Save exact failures, counterexamples, source hash, Python/platform and runtime only after the populated final packet arrives. Complete local uniformity, finite aggregation and matrix identities do not establish the candidate asymptotic or Goldbach.

## Final author instantiation before execution

The frozen statement hash is `42d72d988c7e82e71b2de7a901b5bb17708a7e61053017fc1fbf46c340b89dcf`; its half-open convention matches this plan. Instantiate S=Q*R with horizontal-kernel primes in Q, the CRT rho for all other lines, and the exact canonical-c Mobius count with its finite rounding bound. In comparison 2 also check the author's double-Fourier pair count, its exact j=0 contribution and the retained h=0,j!=0 terms, using H<=6,u<=8,S in {3,5}, V=2, the full/middle-third/empty ratio intervals and every squarefree H divisor. The smoke version uses only H=2. The integer cyclotomic helper is read from frozen RATIOS-007 source hash `498798fd996b211cf5d1f1b3bea47b101fcc720061d9b2133c1a9d5df92e28af`; that file is not edited or executed as a stage. Candidate asymptotic scale comparisons use eta=1/16 as diagnostics only, without accepting a finite implied constant.
