# Goldbach continuation: checked progress and the open lower bound

29 October 2026. **Goldbach is not solved, and no novel breakthrough on it is established.** This investigation closes a specific upper-bound gap in the suggested approach, checks the exact moving endpoints, and sharpens the local-factor margin in a conditional analytic route. The lower-bound investigation is specified in [its brief](lower-bound-brief.md).

## Strongest supported mathematical result

Let N be even, alpha=1/3-epsilon, 0<=epsilon<=1/30. Let H_alpha(N) count primes p such that N-p is a product of exactly three primes, counting repetitions, all strictly greater than N^alpha. Write S(N) for the conventional binary singular series. There are absolute effective, numerically unspecified constants C,N0 such that for every even N>=N0, simultaneously for all these epsilon,

\[
H_\alpha(N)\le 3+C\,\mathfrak S(N)\frac{N}{\log^2N}
                   \left(\varepsilon+\frac1{\log N}\right)^2.
\]

The term 3 can be replaced by the number of prime divisors of N greater than N^alpha. For fixed epsilon the normalized upper bound is O(epsilon^2), pointwise in N. This improves the programme's previous elementary estimate, which lost a logarithm. The [complete proof](statement.md) uses a classical coefficient-uniform two-linear-form upper sieve and Mertens' estimate. Its [separate critic](review.md) supports the derivation. It is a classical sieve consequence; novelty is unverified.

The [endpoint lemma](endpoint-lemma.md) also proves a sharp constant-one transfer from maximal partial-sum discrepancies to the moving weighted sums. It preserves the necessary restriction n<N-eta*k in the divisor switch. An exact counterexample at N=4, eta=2 shows that dropping this cutoff changes the expression by log(2)^2. This repairs a finite algebraic step; it proves no prime-distribution conjecture. Announced prior art directly overlaps this endpoint issue.

The second tranche derived an endpoint-corrected signed-operator reduction and established a sharper uniform local-factor margin:

\[
\mathfrak S(N)(1-\mathcal A(N))\gg\frac1{\log N},\qquad
\mathcal A(N)=\prod_{\substack{p\nmid N\\p>2}}
                  \left(1-\frac1{p(p-1)}\right).
\]

The [complete local-factor proof](local-gap.md) shows this order is sharp along primorial targets. The [separate lower-bound review](lower-review.md) supports it and the reduction, relative to its explicitly imported unconditional coefficient estimates. Retaining these local factors together reduces the sufficient fixed logarithmic saving in a maximal twisted discrepancy estimate from exponent 3+eta to 2+eta. That discrepancy estimate remains unproved. This is a refinement within a conditional reduction, not an established new Goldbach theorem.

**Proof assurance:** handwritten mathematical arguments, inspected primary theorem statements and a separate host-agent semantic review. No proof assistant or external human peer review was run. Agent separation does not imply independent model errors.

## Claim ledger

| ID | Status | Evidence and limit |
| --- | --- | --- |
| H-002 | Proved at the stated assurance level | Uniform pointwise contamination upper bound, [statement](statement.md), [review](review.md) |
| E-002 | Proved at the stated assurance level | Sharp finite endpoint transfer and exact divisor switch, [proof](endpoint-lemma.md), [review](review.md) |
| C-002 | Refuted | Removing the lower-scale term while allowing epsilon to depend on N fails for N=r^3+3, [argument](statement.md) |
| Q-002 | Refuted inherited statement | Strict quarter-root roughness permits at most three factors, not four; [dated erratum](revision.md) |
| LG-003 | Proved at the stated assurance level | Sharp uniform local-factor margin, [proof](local-gap.md), [review](lower-review.md) |
| P-open | Conjecture | Required pointwise parity-sensitive lower bound, [precise statement](revision.md) |
| O-open / T2-open | Conjecture | Sufficient signed-operator or maximal twisted discrepancy estimate, [lower proposal](lower-proposal.md), [sharper threshold](local-gap.md) |
| G | Unverified | No all-N binary Goldbach proof, effective connection or demonstrated novelty |

## What remains necessary

Define F_alpha(N)=(U_alpha(N)-L_alpha(N))/2 with the original rough-complement and Liouville counts, and A_N=S(N)N/log(N)^2. Exactly R_z=F_alpha-H_alpha. A sufficient missing input, for at least one fixed epsilon>0, is

\[
\liminf_{\substack{N\to\infty\\2\mid N}}
   \frac{F_{1/3-\varepsilon}(N)}{A_N}>C\varepsilon^2.
\]

This is a target-uniform lower bound with a positive prime-pair-scale margin. The upper sieve does not establish it. A negative mean, unsigned Chen count, full-endpoint estimate, or statement of a twisted distribution conjecture does not establish it either. Even a sufficiently-large theorem would require an effective threshold and a justified finite connection for an all-N proof.

The alternative ordinary Goldbach route uses the explicit signed operator in [the lower proposal](lower-proposal.md). Its corrected decomposition is G(N)=S(N)(N-B_N)+O_N(N^theta)+an arbitrarily logarithmically small error, for one fixed theta<1/2, where B_N is the reflected Mobius-weighted Mangoldt sum. A sufficient but unproved estimate keeps that signed operator above -(1-kappa)S(N)(1-A(N))N, for fixed kappa>0. The sharper margin also makes an O(N/log(N)^(2+eta)) maximal twisted discrepancy bound sufficient. No such bound has been obtained here. The two actual attempts fail at explicit logarithmic, distribution-level and bilinear-input gaps, as detailed in the review. This route need not prove the stronger original rough-count criterion.

The [external-source parameter audit](source-addendum.md) records why the located subpolynomial roughness results and conditional follow-ups do not supply these inputs. Their full proofs and upstream formalizations were not audited here, and they are not used as established analytic dependencies.

## Computation and execution

The independent [preregistered experiment](experiment-plan.md) and [script](finite_checks.py) produced [finite-results.json](finite-results.json): 29,994 exact rough-complement identity cases through N=20,000, 294 trial-division cross-checks, 628 exact symbolic-log divisor swaps, and 4,792 numerical Abel checks with the recorded tolerance. There were zero failures. These checks do not prove an infinite bound or certify its unspecified constant.

The existing Yamba theorem fleet assigned survey, statement, separate critic and experimenter, revision and integration. The plan costs 14 declared proxy units; the supplemental endpoint author adds 3. The subsequent author-critic-revision pair costs 8, with 3 supplemental units declared for the root-authored local-factor lemma: 28 host proxy units in total. These are dispatch proxies, not money or inference tokens. Actual host agents supplied the results; saved-result replay checks the protocol and is not new inference. See [first-tranche provenance](host-execution.json) and [lower-bound provenance](lower-host-execution.json). The original manual receipts intentionally remain `awaiting_execution`; they record packet preparation rather than falsely claiming command-backed model execution. Both validation replays completed their protocols with `research_validated: false`.

Repository and harness-contract checks pass. All six imported Goldbach unit tests pass. The complete 116-test suite has unrelated Windows portability, timing and existing frozen-source failures, detailed in [repository-tests.json](repository-tests.json); it is not reported as green. No tracked pre-existing source file was changed. Inference token usage and monetary cost are unknown.

The [original input manifest](input-provenance.json) preserves byte-identical copies from source revision b69b270947c053d20134431b172b49a7c51286e8. The original brief remains intact; use the dated erratum in the revision for its quarter-root claim. No publication, push, external message or separately billed provider execution occurred.

The [final lower-bound revision](lower-revision.md) incorporates the separate review and proposes a genuinely different next attempt: a nonnegative Buchstab switching minorant, with either a proved positive coefficient or a checked failure certificate. That next attempt has not yet been executed. See [the continuation checkpoint](NEXT_SESSION.md). Completion of these bounded tranches does not complete the active user goal.
