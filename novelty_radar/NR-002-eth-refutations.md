# NR-002: The Exponential Time Hypothesis reported false, by two AI labs on the same day

| Field | Value |
| --- | --- |
| ID | NR-002 |
| Found | 2026-10-26, through the openai/math update of that date (family 378); followed up 2026-10-28 and 2026-10-29 |
| Kind | New result (claimed refutation of a central complexity conjecture); formalization milestone; AI-generated mathematics |
| State | `PROMOTED` to [problems/eth](../problems/eth/README.md) at the operator's request (2026-10-29), with `TRACKING` items below |
| Evidence here | **Unverified upstream claim.** The preprint was read at statement level and its overview, matrix construction and Appendices C and D in full (inspection level T, [R039](../references/reading-list.md#exponential-time-hypothesis-consequences)); the upstream Lean development was not rebuilt. The second report is known only from a secondary article (level A, R058). Method-level results proved here do not depend on the claim (see [problems/eth/subresults](../problems/eth/subresults/README.md)). |
| Receiving project | [problems/eth](../problems/eth/README.md); ranking for the next fleet iteration in [RANKING.md](../problems/eth/RANKING.md) |
| Next action | The bounded steps under [Tracking](#tracking) |

## The sources

1. **openai/math family 378**, "The Exponential Time Hypothesis is False" (manuscript revised
   2026-10-25, released 2026-10-26 at upstream commit `7ef5c0cc5`). The upstream `history.md`
   says that an independent working group led by Russell Impagliazzo, Ramamohan Paturi and
   Ryan Williams will examine and explain the proof.
2. **A reported independent refutation by Anthropic.** A secondary article (OfficeChai,
   2026-10-27) reports an Anthropic paper titled "A 2^o(n) Time Algorithm for 3-SAT", written
   by Claude, with a Lean formalization of about 1050 modules, and a crossover with brute force
   only beyond about $10^{10000}$ variables. The primary source was not located or inspected.
3. **Expositions.** R. O'Donnell, "Some exposition of 'The Exponential Time Hypothesis Is
   False'" (2026-10-28), and S. Kintali, "A simplified proof of ETH is false" (2026-10-26); a
   blog post by L. Fortnow (2026-10-28) reports a follow-up by Subercaseaux on nondeterministic
   time. All are recorded in the [reading list](../references/reading-list.md#exponential-time-hypothesis-consequences) (R041, R042, R057).

## What is new, as the primary source states it

* For every fixed $k\ge2$, a deterministic algorithm counts the satisfying assignments of a
  $k$-CNF with $n$ variables and $m$ clauses in $(n+m)^{O_k(1)}2^{O_k(n\log\log n/\sqrt{\log n})}$
  time and polynomial space; $2^{O(n/\sqrt{\log n})}$ at bounded density (Theorem 1.1).
* Consequences stated: ETH, #ETH, SETH, Gap-ETH and NSETH fail for fixed width; subexponential
  counting of independent sets, colourings and perfect matchings; approximate Max-$k$-SAT; a
  circuit lower bound $C_L(n)>c\,n\sqrt{\log n}$ for a language in $\mathrm E^{\mathrm{NP}}$.
* The upstream Lean development proves the weaker exponent $n(\log\log n)^2/\sqrt{\log n}$ for a
  multi-tape machine (scope note `lean/docs/378.md`, R040).

## Why it matters here

* **Verification budgets.** Exact model counting in subexponential time changes the
  asymptotic cost model of [E014](../explore/E014-value-of-computation.md), although
  [SR-06](../problems/eth/subresults/SR-06-galactic-thresholds.md) shows the analysed bound
  beats exhaustive search only for $n\gtrsim2^{160000}$; concrete budgets are unaffected.
* **A rich source of bounded problems.** The method's square root is not yet understood;
  [problems/eth](../problems/eth/README.md) turns it into the cube polynomial problem and proves
  first barriers and constructions, with Lean certificates.
* **Method transfer.** Two labs reportedly produced machine-checked refutations of a central
  conjecture within a day of each other; how such results are reviewed is evidence for the
  harness's own review rules (unvalidated workflow hypothesis, see
  [meta/protocol.md](../meta/protocol.md)).

## Tracking

1. **Working-group verdict.** Record the Impagliazzo, Paturi and Williams group's report when it
   appears, and update [SOURCE.md](../problems/eth/SOURCE.md). Stop condition: a published
   verdict or retraction.
2. **The second paper.** Locate the primary source of the reported Anthropic paper, add a
   reading-list entry with its inspection level, and compare its mechanism with the square-root
   analysis in [ETH-A01](../problems/eth/01-algorithmic-core/ETH-A01-break-the-sqrt-log-barrier.md).
   Stop condition: primary source read at level T, or two searches without a primary source.
3. **Follow-ups.** Check the reported nondeterministic-time follow-up (R057) against
   [ETH-D07](../problems/eth/04-fine-grained/ETH-D07-reduction-blowup-boundary.md).

Following, posting, submitting or contacting anyone about these results is the operator's
action.

## Dated source links

* openai/math, family 378, local copy at commit `7ef5c0cc5` (2026-10-26):
  [paper](https://github.com/openai/math/blob/main/preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026/paper.pdf),
  [Lean scope note](https://github.com/openai/math/blob/main/lean/docs/378.md).
* [O'Donnell exposition](https://www.cs.cmu.edu/~odonnell/some_eth_false_exposition.pdf) (2026-10-28).
* [Kintali, simplified proof](https://shivakintali.github.io/papers/ETH.pdf) (2026-10-26).
* [Fortnow, "The exponential-time refutation"](https://blog.computationalcomplexity.org/2026/10/the-exponential-time-refutation.html) (2026-10-28).
* [OfficeChai report on the Anthropic paper](https://officechai.com/ai/anthropic-says-claude-too-independently-disproved-exponential-time-hypothesis-on-the-same-day-as-openai/) (2026-10-27, secondary).
