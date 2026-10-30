# Preregistered auxiliary-moment combinatorics

29 October 2026. Supplemental preparation for MOMENTS-010. Status: preparation only; no execution. The final frozen author definitions and populated finite-check packet must be read before running. Prior frozen files are preserved.

## Three comparisons

1. Check the exact per-prime factor in source (4.37), its inactive interval expansion, active common-line case, prefix/suffix telescoping and normalization by the number of maximal active runs. Use path lengths 3 and 5, every realizable equality pattern of projective labels, every active mask, p in {3,5,11}, and rho in {1/4,4/9}. Both square roots are rational, so endpoint q=sqrt(rho) and interior q=rho are exact Fractions. Check the stated theta cancellations. Keep endpoint and active-run normalization negative controls.
2. For index sets of size 0 through 6, enumerate set partitions and permutation cycles independently. Verify distinct-prime inclusion-exclusion (4.55) on every equality pattern and every active mask, with the active-status condition retained. Verify cycle multiplicities, signs, rank counts and the rank-weight bound (4.56). Include the smallest inactive-index omission witness. No permutation domain exceeds size 6.
3. For ordered tuple lengths 0 through 6 over {2,3,5}, including repetitions, use two positive rational prime-weight vectors and exact Gaussian-rational phase factors. Verify tuple symmetrization with three symmetric test functions, the bound on the averaged phase, factorial/multiplicity measures, and active-list versus memory-tuple total masses. Specified coordinates beyond the tuple length give zero. Include a nonsymmetric-test counterexample. This checks finite algebra; it does not certify a G/E operator norm from a few matrices.

The prime-tuple masses in comparison 3 are for appended pairs constrained to the current line. Separately check the full pair-memory alphabet {(p,line):p in {2,3}} through length 3, including repeats and a symmetric test depending on both coordinates. Its total mass is lambda(X)^l/l!, with lambda(X)=sum_p(p+1)nu(p), whereas the fixed-line appended mass uses s=sum_p nu(p). Keep this distinction explicit rather than silently normalizing the full memory alphabet.

## Domains and assurance

The smoke run uses path length 3, one rho and one p, index sets through size 3 and tuples through length 3. The bounded final domains are above. Source (4.61) is the phase-factor/equality setup; its following displayed symmetrization identity is checked separately from any analytic phase-inserted norm claim. Exact source formulas will be instantiated from the final author statement before execution. Save code hash, Python/platform, runtime, exact failures and negative controls only after the stage is dispatched. No asymptotic moment, source analytic theorem or Goldbach result follows from these checks.

## Frozen author instantiation

The final author hash is `0e0e38bdb4f3b000bd67f385d5c32da1bb59fbd22790d1ddb31a8d10ead3e7ca`. Its q/b-prime/nu definitions, per-prime identity (16), active-run normalizers, local theta cancellations, distinctness identity (19), rank weights, tuple symmetry and full-pair versus compatible-slice measures match the prepared formulas. Coverage remains limited to these finite identities. The complete operational G/E histories, adjoint Schur estimates, memory-tail argument, analytic norm/moment bounds and reflected replacement (22) are not tested by inventing a finite norm experiment.
