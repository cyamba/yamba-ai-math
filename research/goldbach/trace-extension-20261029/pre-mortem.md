# Supplemental pre-mortem for trace enlargement

29 October 2026. Distinct critic's preparatory audit of `brief.md`, before reading any author statement. This is a separate supplemental dispatch. It does not execute the later main critic stage or accept an unseen trace or root-count proof.

## A valid trace comparison is available

For a finite weighted Hilbert space, orthogonal projection P and arbitrary operator B, the genuine statement is

    tr(((PBP)(PBP)*)^R) <= tr((BB*)^R),

for positive integer R. It follows from Schatten contraction under multiplication by orthogonal projections, or directly from singular-value domination. For the latter, a rank-j approximation C to B gives the rank-j approximation PCP to PBP with no larger operator-norm error; the singular-value variational characterization then gives s_j(PBP)<=s_j(B). Sum their 2R powers.

Weights belong in the Hilbert inner product and its adjoint. The trace is the trace in an orthonormal basis for that weighted space, not a sum of weighted-coordinate matrix entries chosen ad hoc. Sector copies must remain disjoint. If the exact compressed-operator equivalence is proved, the trace inequality can be applied to each enlarged sector and summed.

This does not license deleting arbitrary internal projections from a signed centered-kernel path expansion. One must identify the whole operator as a compression or invoke a separate justified ideal-norm inequality.

## A small counterexample to pointwise projection deletion

Take the ordinary three-dimensional Euclidean space,

    B = [[2,0,1], [2,0,-2], [0,0,0]],
    P = diag(1,1,0),    e = (1,0,0).

The endpoint e is already in the projected subspace. For R=2,

    <e, (((PBP)(PBP)*)^2)e> = 32,
    <e, ((BB*)^2)e> = 29.

Thus even this natural pointwise moment inequality is false. Its trace counterpart is true: the two traces are 64 and 97. This is a minimal-sized useful example with a two-dimensional projected subspace; no entrywise positive-kernel interpretation is available for the general centered operator.

## The enlarged good states need an actual definition

Outside the unit-first-coordinate compression, an image point may be primitive while its original preimage is not. For example, H=2, sector c=0 and image position (2,1) map back to (2,2), which has no determinant-one integral complement. An original complement ratio r_P is therefore undefined there.

A valid enlarged operator can instead define coefficient-one good-state conditions from the primitive image position and prove that their restriction agrees with the transported H*r_P condition on unit-first-coordinate states. It cannot use an original determinant-one complement on every enlarged preimage by assertion. No claim that this extension represents the original arithmetic sequence should be made.

## Endpoint vectors give a necessary factor

Let u_P be the indicator of all list states at position P. Distinct positions give orthogonal endpoint vectors. Their frame operator is

    B_end = sum_P |u_P><u_P| <= M*I,
    M = max_P ||u_P||^2.

For any positive T, the actual root moment is tr(T*B_end), hence at most M*tr(T). This is the correct direction. It does not identify the source's root moment with the full trace.

There is no automatic reverse comparison. In a single two-state list block, u=(1,1) and T equal to the projection onto (1,-1) have <u,Tu>=0 but tr(T)=1. A theorem controlling only the indicator endpoint vector need not control the trace on the remaining list directions. A new trace estimate, or a proved restriction to an appropriate endpoint span, is required.

For ordered distinct active lists, if n_i(P) is the number of available group-i divisors of the first coordinate, then

    ||u_P||^2 <= product_i (n_i(P))_(J+1) * V_i^(-(J+1)),

where the falling factorial counts ordered tuples. Replacing it by an unordered binomial count without a factorial correction would be wrong for the source state measure. With fixed K, source group primes at least exp(L^0.1), polynomial first-coordinate height and V_i bounded below, one has n_i(P)=O(L^0.9). Thus

    log M = O_K((J+1)*log L).

At J comparable to L^0.01 and R comparable to sqrt L, M^(1/(2R))=1+o(1). This factor can be harmless after the specified root, but cannot be discarded from the finite inequality. Its group-mass dependence and any changed normalization must remain explicit. The conclusion would need rechecking for growing K, a different J/R balance or masses tending rapidly to zero.

## The arithmetic trace issue remains

Even a correct compression and a harmless endpoint factor leave tr((B_c B_c*)^R) to be estimated for the enlarged arithmetic operator and then summed with the true sector and list weights. The source's indicator-endpoint moment statement is not already this trace theorem. The expansion has basis list states, endpoint closures, distinctness conditions, geometric projections and signed centered kernels; those must be treated at their actual normalization.

The proposed enlarged determinant-H root count can address the base arithmetic roots only after its bijection, multiplicities and local densities are proved. It does not by itself justify arbitrary high-moment accumulation. Path coordinate heights and boundary derivatives must retain the actual factor H/(UV) and list/moment costs before being called subpolynomial. A sector count or norm-one projection alone cannot establish their cancellation.

These observations leave a viable bounded task: prove the exact enlarged-operator compression, retain the endpoint factor, prove the proposed root count independently, and identify the remaining arithmetic trace estimate. They do not supply that estimate, validate the full source theorem, remove the denominator-H prime major term, resolve polynomial-label or prime-boundary issues, or establish a Goldbach breakthrough.
