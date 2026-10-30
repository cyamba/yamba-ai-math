# Result of the joint unit-root count

29 October 2026. `GOLDBACH-ROOTS-008`. The actual theorem-fleet author, distinct critic and finite checker support the joint count below. This is a scoped classical-method arithmetic lemma. Novelty remains unverified; no Goldbach proof or substantive demonstrated breakthrough has been achieved.

## Accepted finite count and useful range

For H>=2, U,V>=2, primitive positions P=(u,v) with both coordinates coprime to H, let c_H be the canonical residue in [0,u) satisfying v*c_H=-H modulo u. Put d_H=(H+v*c_H)/u. The matrix [[u,c_H],[v,d_H]] has determinantH. For squarefree S coprime to H, prescribed first-row kernel lines at each p|S, and the specified half-open intervals I1,I2,I3 for u/U,v/V,c_H/u, the accepted count is

    N = UV*|I1|*|I2|*|I3|*kappa_b(H)/product_(p|S)(p+1)
        + O_eta(2^omega(H)*(U^(7/4+eta)+V)*log^2(2U)),
    kappa_b(H)=zeta(2)^(-1)*product_(ell|H)(ell-1)/(ell+1).

The absolute-error constant depends only on fixed eta>0. It covers all line types, prime powers in u, p dividing u, nonunit row entries, all squarefree H divisors and empty intervals. The proof splits S=QR: horizontal kernels impose Q|u, while the others impose (u,R)=1 and c_H=rho*u modR. Double completion retains both the exact zero-v-frequency mass and the zero-c/nonzero-v terms. The weighted-u count pays the R exclusion cost before its V/R prefactor absorbs 2^omega(R)/R. No positive H power or unrecorded S factor is suppressed.

For H<=X^A, subpolynomial S as in the brief, and U,V comparable to X^a,X^b with fixed positive exponents and b>3a/4, the error is UV*X^(-gamma+o(1)), gamma=min(a,b-3a/4)>0. Balanced square-root boxes give exponent1/8. Fixed positive interval lengths also give relative saving and eventual nonemptiness. Shrinking intervals need their actual main mass to dominate the absolute error; empty populations are not normalized.

The formula is an absolute estimate for all aspect ratios, but its displayed completion error does not give a power saving when b<=3a/4. That broader target is unproved, not refuted. No effective constants or numerical eventual threshold were extracted. The [revision](revision.md), [frozen proof](statement.md) and [separate review](review.md) are authoritative.

## Evidence and scope

Proof assurance is a complete elementary argument plus a distinct host-agent substantive review, without a proof assistant or external peer review. The separately reconstructed Kloosterman input comes from RATIOS-007. The full LWW theorem or its moving-H transport is not an accepted dependency. Later inspection of pinned Guo source locates already-present labelled enlargement, root-count and conditional transport framing; see the [source audit](../trace-extension-20261029/goal-bridge-source-audit.md). This strengthens the priority caution rather than turning a conditional source claim into a proved application.

The [exact finite checks](finite-results.json) passed859 canonical matrices,2,174 local kernels,11,352 complete residue matrices with166 prescription cases,40,418 Q/R reductions,2,335 canonical-c Mobius masses,1,740 interval aggregations and3,216 partitions. All288 double-Fourier identities and their exact zero-v terms passed;1,320 zero-c/nonzero-v terms and9,792 coefficient-gcd cases include18 empty intervals. A nonzero zero-c contribution is retained as a witness against dropping it. An H=6,S=3 horizontal-line obstruction tests why this unit-filtered theorem retains (S,H)=1. Numerical big-O scale ratios are diagnostics only.

All six actual host responses are retained in `.runs/goldbach-roots-008-manual-20261029`. Nominal dispatch cost14, checker preparation2, separate pre-mortem2 and next-operator source inspection2 total20 within20. Actual token use and monetary cost are unknown. The pre-mortem preceded the main author audit and is not an earlier execution of that dependent stage. Replay checks saved response protocol only, with research_validated=false and no fresh inference.

Repository and harness contracts pass. The full116-test suite retains10 failures and3 errors in existing unrelated Windows, timing and frozen-evidence paths; [repository-tests.json](repository-tests.json) records them. It is not a green suite. Imported Goldbach hashes remain unchanged, and the new finite script passed its declared executions. No provider billing, publication, push or external message occurred.

## Next actual proof task

The count does not bound growing-list/path moments or selected-endpoint operator norms. It supplies no changed denominatorH prime major-arc estimate or actual-prime lower margin. The original polynomial-rough nonzero-center and h=1 obligations remain.

[TRACE-009](../trace-extension-20261029/brief.md) is already executing: its author statement is frozen and dispatched for separate review and finite checks. It tests an exact trace/Gram comparison and an enlarged determinantH root population, so that root-dependent unit restrictions are not silently dropped. That candidate changes the population and is not yet an accepted dependency here. The overall Goldbach objective remains active and unachieved.
