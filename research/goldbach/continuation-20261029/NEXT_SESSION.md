# Active Goldbach research checkpoint

29 October 2026. The user requested work on the cloned suggested approach until a solution or breakthrough. **That objective is still active and has not been achieved.** No goal-completion or breakthrough claim is justified. This checkpoint records completed work and a concrete next attempt; it grants no new tool, spending or publication authority.

## Read first

Read `result.md`, `lower-revision.md` and its separate `lower-review.md`. The original suggested approach is in `../orchestrated-prompt.md`, copied byte-identically from branch `origin/research/goldbach-geometry-parity`, revision b69b270947c053d20134431b172b49a7c51286e8. The original main checkout had no Goldbach folder. Only new files were added; pre-existing tracked files and the user's unrelated untracked benchmark configuration were not changed.

## Completed and reviewed

1. `statement.md`: uniform pointwise H bound for alpha=1/3-epsilon, epsilon in [0,1/30], with H<=3+C*S(N)*N/log^2N*(epsilon+1/logN)^2. It is a classical upper-sieve consequence, not a novel Goldbach theorem.
2. `endpoint-lemma.md`: sharp constant-one moving-endpoint transfer and exact divisor switch. The strict cutoff n<N-eta*k matters. Announced prior art overlaps this issue.
3. `local-gap.md`: S(N)*(1-A(N))>>1/logN uniformly, sharp in order along primorial targets with asymptotic constant exp(gamma). This improves a sufficient maximal twisted discrepancy exponent from 3+eta to 2+eta, within the conditional reduction.
4. `lower-revision.md`: endpoint-corrected G=S(N)*(N-B_N)+O_N(N^theta)+small for theta<1/2, relative to inspected unconditional coefficient lemmas and ordinary BV. O_N is the defined signed operator, not an error proved small. One-sided O-open and maximal T2-open remain unproved.
5. `finite-results.json`: 29,994 exact rough identities through N=20,000, 294 trial cross-checks, 628 symbolic divisor swaps, 4,792 numerical Abel checks. Zero failures. These are finite implementation evidence.

All mathematical assurance is handwritten proof plus separate host-agent substantive review, with imported analytic inputs explicitly stated. No new Lean run or external human peer review occurred. Novelty and numerical effective constants are unverified. Sufficiently-large implications do not settle all N without an effective connection.

## Do not repeat the failed shortcuts

The previous sparse-deletion model already blocks leading averages as a pointwise argument. It does not inherit ordinary Mobius inversion or arbitrary-log-saving EH/BV automatically. Subpolynomial roughness cannot be changed to polynomial roughness. A full-endpoint estimate cannot replace the maximum over endpoints. At the strict quarter-root cutoff at most three factors survive, not four. Ordinary BV applies to Lambda, not automatically to Lambda(n)mu(N-n).

The direct signed-operator bound is only O(Nlog^3N), four logarithms above the guaranteed N/logN margin. This is a weakness of that bound, not a measurement of the actual operator. The direct near-cubic lower sieve has parameter s=1/(2alpha)-o(1)<2. The FI route needs an unproved specialized bilinear bound and longer distribution range. Neither route proved the lower estimate.

## Next distinct bounded attempt, not yet executed

Use a program contract with the existing roles and a separate critic. Pursue one explicit weighted Buchstab switching minorant for the original F_alpha count. Begin at beta<1/4, where ordinary BV permits a positive dimension-one lower-sieve coefficient. Write the exact least-factor decomposition U_alpha=U_beta-sum C_r for primes N^beta<r<=N^alpha. At the near-cubic alpha, F_alpha=U_alpha-E_alpha, where E_alpha counts semiprime complements. Apply only actually justified upper bounds for C_r and E_alpha and a lower bound for U_beta. Track singular factors, repeated factors, factor order, moving intervals, all sieve constants and uniformity.

The output must be either a rigorously positive coefficient exceeding the proved contamination coefficient, or an independently checked nonpositive-coefficient certificate for this particular minorant. Do not insert an unproved signed correlation to repair a negative coefficient. A standard parity obstruction is plausible, but must be derived for the actual chosen inequalities. This is a new route to investigate, not a promised breakthrough.

## Harness and engineering provenance

Theorem program `programs/goldbach-uniform-trilinear.json`: 14 fleet proxy units plus 3 supplemental endpoint-author units, completed host work in `host-execution.json`. Pair program `programs/goldbach-pointwise-lower-bound.json`: 8 fleet proxy units plus 3 supplemental root-author units, completed host work in `lower-host-execution.json`. Combined declared host proxy cost 28. These costs are not measured money or inference tokens. No separately billed provider adapter was used.

Manual packets and real saved host responses are under `.runs/goldbach-uniform-002-manual-20261029` and `.runs/goldbach-lower-003-manual-20261029`. Validation replays under the matching `*-validation-20261029` folders completed with research_validated=false. The original manual receipts remain awaiting_execution as packet-preparation evidence; the separate host receipts identify actual work. Do not present replay as fresh research or deterministic code as an LLM proof search.

Repository and contract checks pass; six imported Goldbach unit tests pass. Full tests retain unrelated Windows portability/timing and pre-existing frozen-source issues, recorded in `repository-tests.json`. Setting Python `tempfile.tempdir` to a verified directory under `.runs/` avoids the initial sandbox temp permission errors. Do not widen this research task into fixing unrelated harness or KR1 files. Preserve the frozen proof hashes recorded by the critics. Keep the original imported files byte-identical; their erratum is recorded separately in `revision.md`.
