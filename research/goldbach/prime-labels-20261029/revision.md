# Revision of the bounded-label and padding attempts

29 October 2026. Registry role: Mathematician, `GOLDBACH-LABELS-005`. This revision uses the populated `revise` packet, the separate `review.md`, the independent finite-check result, and the separately reviewed root-authored `parameter-retuning.md`. The frozen statement, survey and reviewed supplement remain unchanged. No new source search or computation was performed here.

## Accepted bounded-label construction

The critic supports the exact support, reconstruction and deweighting arguments. Original subpolynomial source groups lie below z=N^alpha eventually and have zero divisor weight on the target rough population. Moving K disjoint required groups above z forces empty support whenever K*alpha>=1, including equality because every selected prime strictly exceeds z. This leaves bounded K as a possible construction; the support observation alone is not a general obstruction.

One group covering all primes in (z,N) repairs coverage. Let nu(q) count distinct prime factors and h_rho(q)=nu(q)*rho^(nu(q)-1). For admitted squarefree q, its factor count is 1, 2 or 3. With

\[
Z_\rho(N)=\sum_{p,\ q=N-p>1,\ P^-(q)>z}\mu(q)h_\rho(q),
\]

the exact cell identity is

\[
Z_\rho=-R+2\rho E_0-3\rho^2H_0.
\]

Here R counts prime complements, E0 squarefree semiprime complements, and H0 squarefree triples. The accepted three-node reconstructions are

\[
R=-3Z_{1/4}+3Z_{1/2}-Z_{3/4},
\]

\[
F_0=-\frac{17}{3}Z_{1/4}+\frac{25}{3}Z_{1/2}
                              -\frac{11}{3}Z_{3/4}.
\]

Their coefficient l1 costs are 7 and 53/3 for these nodes. The prime reconstruction is exact without repeated-factor corrections. The second counts only squarefree odd complements; adding nonsquarefree odd triples gives F. The bare unsigned distinct-factor interpolation has its separately recorded prime-square false positives and distinct r^2*s false negatives. No formula silently replaces nu by Omega.

The elementary exceptional-count estimate is

\[
Q_{\rm ns}(N)\le N/(z-1)=O(N^{1-\alpha})=o(A_N),
\qquad A_N=\mathfrak S(N)N/\log^2N.
\]

It also controls the difference of rough mu and lambda sums. The profile suprema 1, 1, 27/16 give the stated bare-interpolation bound 323/16. Dividing by the known group mass V_N~log(1/alpha) retains its normalization cost.

At rho=1/2 the exact deweighting formulas are Z_1/2=B_mu+H0/4 and Y_1/2=U0-H0/4. The previous H bound controls these approximation errors at O(epsilon^2*A_N) with epsilon fixed. Thus finite labels do repair algebraic coverage and weight approximation. They do not estimate the signed sums.

## Nonzero centers and the prime boundary remain essential

The source's unsifted zero-center conclusion cannot be copied to these adapted rough weights. Their centers must respect the three signed cells above. In particular, simultaneous uniform Z_rho=o(A_N) at the three interpolation nodes would force R=o(A_N), contradicting the positive average prime-pair count supplied by PNT. A formal averaged rough-type center is generally nonzero; it is not a pointwise estimate for the moving target.

For proposed centers whose prime reconstruction equals 1, individual errors at most eta*A_N with eta<1/7 would suffice for positivity. This is only an elementary propagation implication. The required correctly centered signed estimates have not been established.

The selected-divisor quotient expansion retains h=1 exactly. On squarefree q=r*h, mu(q)=-mu(h), and selecting each prime factor once reproduces its multiplicity nu(q). The h=1 component is -R itself. Long-quotient character-Mellin cancellation cannot omit that boundary, whose selected prime label is macroscopic when the prime complement is macroscopic. Dropping it would remove the original unknown prime-complement contribution rather than estimate it.

## An explicit parameter repair was attempted

The inspected source uses fixed K, J=floor(L^0.01), moment order R comparable to sqrt L, and a dirty-edge budget containing L^2*(J+1)^(-K), where L=log N. At K<=3 the resulting displayed L^(1-0.005*K) bound does not certify logarithmic decay. This describes the available bound; it does not lower-bound the actual operator norm.

The separately reviewed supplement tries increasing J to repair that bound. If its fixed Schur prefactor is L^C, using that positive budget term to certify an edge saving L^(-G) requires

\[
L^{C+1}(J+1)^{-K/2}\ll L^{-G},\qquad
J+1\gg L^{2(G+C+1)/K}.
\]

With genuine polynomial labels, the complete auxiliary product has log height at least K*(J+1)*alpha*L. At the published moment order the remaining dimension factor therefore is at least

\[
\exp(cK\alpha(J+1)\sqrt L),
\]

which exceeds every fixed power of L already for constant J. Raising J worsens this displayed loss. Raising R as well would require

\[
R\gg K\alpha(J+1)L/\log L
\]

to contain this particular factor within a fixed logarithmic power. No cited moment statement supplies that enlarged order with the needed uniformity. Changing a memory truncation would likewise require re-proving its discarded-path error; the published memory budget cannot be independently suppressed while retaining its moment conclusion.

There is an earlier range obstruction independent of J and R. The inspected source's root-averaging input prescribes squarefree moduli only through

\[
S\le\exp(O_K(L^{0.98})).
\]

A single polynomial label r>N^alpha already lies outside that range eventually: alpha*L exceeds C_K*L^0.98 for every fixed K and constant C_K. Retuning J or R cannot reverse that inequality. The source appendix's S-dependent error does not become a larger-range theorem by substitution. A new root-averaging proof, or a genuinely different small-K contraction argument, is needed.

These are checked failures of attempts to use the displayed source estimates. They do not rule out a better weighted Schur bound, normalization, moment argument, or root-averaging theorem. None has been proved here. The source also uses small auxiliary primes below its sift threshold for coprimality and primitive-position claims. Polynomial labels violate that arrangement, and the reflected determinant is bmn-ars=N(b-a), rather than the fixed-shift determinant. Its moving-target treatment remains a separate obligation.

## Accepted padding identities and corrected collision wording

Let D be squarefree and built from t_i>=1 small primes in each source group, all below z. Then gcd(D,q)=1 for every admitted q, and

\[
W(Dq)=C_D=\prod_i t_i\rho^{t_i-1}/V_i>0,\qquad
\mu(Dq)=\mu(D)\mu(q),\qquad
\lambda(Dq)=\lambda(D)\lambda(q).
\]

Thus the padded signed sum is mu(D)*C_D times the original rough mu sum, and the analogous Liouville identity holds. Any q-independent finite average remains one scalar M times that same original sum. When M is nonzero, normalization recovers the original correlation. When M=0, the padded average is identically zero and cannot be normalized to recover information. Its center transforms by the same scalar. Coprimality is essential for mu, and label separation is needed to make W(Dq) constant; neither may be omitted from its hypotheses.

With one forced divisor in each group, all label selections give a=b=D. Discarding shared-label terms would discard the entire construction. The collision statement is now precise: with t forced labels and equal independent selections the probability of equality is exactly 1/t. For arbitrary normalized probabilities pi_j it is

\[
\sum_{j=1}^t\pi_j^2\ge1/t,
\]

with equality for equal probabilities. For example probabilities 3/4 and 1/4 give 5/8 rather than 1/2. This corrects the unqualified exact-probability wording while preserving the collision diagnosis under nonuniform source measures.

Taking t_i=J+1 at fixed rho introduces the recorded inverse-normalizer growth of order exp(cKJ). Allowing rho to vary with J would leave the inspected fixed-rho regime and require a new uniform estimate. The padded form -D*p+D*N is nonprimitive; removing its common divisor returns q=N-p. As a sequence at ambient size D*N it is restricted to multiples of D, retains the original prime mass, and imposes roughness on n/D rather than n. These changes prevent an automatic application of a fixed-shift, unconditioned prime theorem. The padding identities are not an impossibility theorem for every auxiliary-list construction.

## Independent checks, assurance, and next obligation

The finite worker reports exact Fraction-based checks of 2,874 rough-support weight cases, 930 capacity cases including equality, all 19 multiplicity types on its finite alphabet, the stated reconstruction and norm formulas, and the recorded padding and signed-mixture cases. All passed. Its explicit counterexamples show why mu padding needs coprimality, constant group weight needs label separation, and zero padded normalization need not mean zero original correlation.

Those checks verify finite algebra and boundary handling, not the source's analytic estimates. The assurance here is complete stated algebra and elementary bounds, selected primary-source parameter inspection, a separate host-agent substantive review, and finite reproduction. No proof assistant or external human peer review was used. The full LWW theorem and analytic source chain remain unverified as dependencies. Novelty, effective numerical constants and actual inference usage are unmeasured or unverified.

No correctly centered target-uniform correlation estimate, positive original F margin, Goldbach proof or demonstrated breakthrough has been established. The active goal remains open. The next substantive proof obligation is an actual arithmetic estimate in the missing polynomial-label/moving-target range, with the h=1 prime boundary and nonzero center retained, or a new parity-sensitive actual-prime mechanism that supplies it. Another interpolation, beta optimization, padding average with zero normalizer, or unproved enlargement of the source's range would not meet that obligation.
