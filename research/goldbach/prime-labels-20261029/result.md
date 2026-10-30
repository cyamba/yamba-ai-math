# Result of the prime-label and padding attempts

29 October 2026. `GOLDBACH-LABELS-005`, one executed host-agent theorem round. The binary Goldbach objective is active and unachieved. No correctly centered target-uniform parity estimate, Goldbach proof or substantive demonstrated breakthrough was obtained. The selected external manuscript is unverified as a dependency, and novelty of the technical observations is unverified.

## Supported mathematical findings

For q=N-p>1 with every prime factor>N^alpha and alpha in [0.3,1/3), the factor count is at most3. Original subpolynomial source labels vanish on this population. K disjoint required polynomial groups have empty support when K*alpha>=1. One group containing every factor repairs coverage. Write h_rho(q)=nu(q)*rho^(nu(q)-1), nu counting distinct prime factors, and sum Z_rho= sum mu(q)h_rho(q) over the indicated prime complements. The reviewed exact identities are

    Z_rho = -R + 2*rho*E0 - 3*rho^2*H0,
    R = -3*Z_(1/4) + 3*Z_(1/2) - Z_(3/4),
    F0 = -(17/3)*Z_(1/4) + (25/3)*Z_(1/2) - (11/3)*Z_(3/4).

R counts prime complements; E0 and H0 count squarefree semiprime and triple complements. The coefficient costs are7 and53/3 at these chosen nodes. Nonsquarefree rough complements number at most N/(z-1)=O(N^(1-alpha)), negligible compared with S(N)*N/log^2N. Prime reconstruction needs no correction because mu kills nonsquarefree terms; F0 requires adding nonsquarefree odd triples. At rho=1/2 the deweighting error is exactly H0/4, controlled by the earlier H bound. The selected-divisor expansion retains h=1, which contributes -R itself.

These weights have a nonzero rough-population bias. Simultaneous uniform zero-centered estimates at all three nodes would contradict the positive average prime-pair count. Correctly chosen centers with individual errors below (1/7)*S(N)*N/log^2N would suffice, but no such estimate was proved.

The parameter repair was actually attempted: increasing auxiliary list length to improve the displayed small-K dirty-edge bound worsens the polynomial-height factor at the published moment order. An enlarged order requires a new moment theorem. Independently, one polynomial label already exceeds the inspected root-averaging range exp(O_K(log(N)^0.98)). These are limitations of using the displayed available upper bounds, not lower bounds for actual operator norms or a general impossibility theorem. See the separately reviewed [parameter calculation](parameter-retuning.md).

For a squarefree product D of forced small labels, coprime to q and separated from its group divisors, W(Dq)=C_D and the padded correlation is mu(D)*C_D times the original. Any q-independent mixture remains a scalar multiple. A zero scalar cannot be normalized to recover the original. Shared-label collisions are exactly1/t for equal selections and sum pi_j^2>=1/t for arbitrary normalized probabilities. Padding also changes primitivity, ambient mass and roughness conditions. Its scalar identity supplies no analytic gain by itself.

The authoritative accepted formulation is [revision.md](revision.md); the frozen author input is [statement.md](statement.md), with the collision wording corrected only in the revision. [review.md](review.md) records the separate critic's hashes and assurance. Proof assurance is complete stated algebra and elementary bounds plus a distinct host-agent substantive review. No formal proof checker or external peer review was used.

## Computation and protocol

The independent exact checks passed2,874 support cases,930 capacity cases, all19 finite multiplicity types, the reconstruction/norm identities and the recorded coprimality, separated-label and zero-normalizer witnesses. [finite-results.json](finite-results.json) records domains and code hash. These are finite checks, not analytic source validation.

A preregistered supplemental numerical screen examined the original cubic T sign at49,998 even targets6 through100,000. It found no nonnegative candidates. Small cases had98 independent exact recounts; the full FFT screen was floating point and has no exact all-range convolution certificate. Its null result establishes no infinite theorem and was not used as proof. The search stopped at its declared boundary. See [sign-search-plan.md](sign-search-plan.md) and [sign-search-results.json](sign-search-results.json).

Actual six-stage host results were retained under `.runs/goldbach-labels-005-manual-20261029`. The nominal fleet cost was14 dispatch proxy units, with3 root units for retuning and2 for the supplemental falsifier screen, total19 within20. Actual inference usage and monetary cost are unknown. Replay validates response protocol only, with research_validated=false and no fresh inference. The manual preparation receipt remains awaiting_execution; [host-execution.json](host-execution.json) separately records completed host work.

Repository contract checks pass. The full116-test repository suite retains10 failures and3 errors in unrelated Windows, timing and frozen-evidence paths; it is not green. Exact Goldbach input hashes remain unchanged. [repository-tests.json](repository-tests.json) identifies the failures and saved log.

## Next mathematical attempt

The next bounded program is `GOLDBACH-SECTORS-006`, [moving-target determinant sectors](../moving-sectors-20261029/brief.md). It attempts an exact congruence-sector conjugacy and a genuine estimate on the resulting domains. Merely changing coordinates will not count as cancellation. The positive F margin, signed-operator lower bound and original Goldbach proof remain open.
