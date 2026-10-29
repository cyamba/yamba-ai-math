# KR1 sector notebook — Phase 2

New local attempt, 25 October 2026 Stockholm. All new arguments and executable
transcriptions initially have author-only assurance. RR006/RR007 remain closed.

## Frozen families before the first pilot

1. **H1 implementation, version 1.** This transcribes the *reviewed prior*
   restricted paper construction; it is not a newly claimed all-sector map.
   Keep f1 (A3 plus corrected b1 cycle), g2, g3 and their alternating paths
   distinct. The source domain is all a<=2 plus a3,b0. New implementation,
   image test and literal endpoint coverage must pass this attempt's checks.
2. **External Phase 2 sector tables, version 1.** AST-extract only the named
   functions in test_complete_n26.py and verify_a3_b0_universal.py; never import
   their top-level executions or absolute imports. Test a3,b1, a4,b0, a5,b0
   exactly as written. The supplied claim through26 is neither an all-b rule
   nor a universal proof. Record first literal/weight/injectivity failures;
   do not repair cases from a finite table or silently merge assignments.
3. **Bounded-phase reduction, version 1.** For a3,b and
   mu=(x,x+y,x+y+z), put B=b+1 and x=Bq+k, 0<=k<B. The child is
   C'=(1,B,(z),(q,q+nu1,...,q+nub)). Its exact excess is
   wt(C)-wt(C')=2+2y+3k. This is an exact C-side reduction with an
   intrinsic inverse, *not* a U map. It exposes the missing bounded phase.

## Initial structural clues and obstructions

The external a3,b1 branch merges d3 and nu1 into the same number of threes;
its asserted continuous parameter encoding is suspect beyond its finite
cutoff. The a4 table has branches discarding d2 residues or d4 contributions;
the a5 fallback discards most riggings. Exact smallest falsifiers remain to
be measured, without treating these observations alone as executed results.

The bounded-phase reduction suggests a weight-two orbit above a1,B. A naive
target D_B plus 8/10 markers and a 3(k+1) column collides with g2: arbitrary
q raises the top multiplicity into its old mixed-marker language. Thus an
intrinsic contour normalization is required. A new child dimension or an
extra geometric coordinate does not itself supply that parser.

At N<=40, a3,b2 first appears at39; a4,b1 at31; a5,b1 has minimum43
and is outside the authorized numerical boundary. Any claimed all-b result
therefore requires a proof that tests through40 cannot supply.
