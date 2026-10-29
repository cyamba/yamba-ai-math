# openai/math watch

Tracks [openai/math](https://github.com/openai/math) and its maintainer account
[dr-openai](https://github.com/dr-openai) for results that touch Christopher's interests
and open problems worth taking on here. The procedure is the
[watch-openai-math skill](../.agents/skills/watch-openai-math/SKILL.md); the machine-readable
baseline, interest profile and watched families are in
[openai-math-watch.json](openai-math-watch.json).

**Status of upstream material: unverified.** The collection is model-produced. Its README
warns that unformalized results may contain errors, and three manuscripts were withdrawn on
2026-10-07 after a sign error. A family listed here is a lead, not an established result.
Citing one in research files still requires a [reading-list](reading-list.md) entry with an
inspection level, and any use as a dependency needs the `audit-theorem` workflow.

## Sources

| Source | What to watch | Checked |
| --- | --- | --- |
| `openai/math` `history.md` | Dated update notes: new results, withdrawals, fixes, formalizations | 2026-10-27 |
| `openai/math` `CONTENTS.md` | Family list (number, title, Lean link); diffed by `scripts/openai_math_watch.py` | 2026-10-27 |
| `openai/math` commits and merged PRs | Update PRs merged by `dr-openai`; commits authored by Dan Roberts | 2026-10-27 |
| `dr-openai` public repositories | New public repositories or activity outside openai/math | 2026-10-27: none public |

## Baseline

- Commit `7ef5c0cc5` (2026-10-26, merge of PR #3 by dr-openai): 721 manuscripts, 373 families,
  245 families with a Lean documentation link.
- Upstream log so far: initial release 2026-10-06; update and three withdrawals 2026-10-07;
  PR-locking change 2026-10-12; 2026-10-26 update adding local smoothing for the wave
  equation and family 378 (disproof of the Exponential Time Hypothesis, under review by an
  independent working group).

## Watched families

| Family | Why it matters here | Hook into this repository |
| --- | --- | --- |
| 169 Shareshian–Wachs elementary positivity | Already a dependency of the partition H3 work | [R038](reading-list.md), [gap-closure plan](../research/partitions/gap-closure-plan.md); watch for revisions and the remaining Schur/h-positivity questions |
| 168 Combinatorial invariance of Kazhdan–Lusztig polynomials | Positivity and Bruhat-interval combinatorics beside H3 | Candidate `explore-angle` source; check its Lean coverage first |
| 122 Trace-reconstruction bounds | Deletion-channel decoding, relevant to sequencing and DNA storage | Bioinformatics lead; no project yet |
| 107 Matrix multiplication, omega at most 9/4 | Compute cost of dense linear algebra | [E001](../explore/E001-certified-attention-compression.md), [E014](../explore/E014-value-of-computation.md) |
| 378 Disproof of the Exponential Time Hypothesis | Exact model counting in subexponential time | [E014](../explore/E014-value-of-computation.md); promoted to [problems/eth](../problems/eth/README.md) on 2026-10-29 ([NR-002](../novelty_radar/NR-002-eth-refutations.md)); record external review state before any use |
| 133 Complexity of Weisfeiler–Leman refinement | Limits of graph-isomorphism refinement, graph-network expressivity | [E003](../explore/E003-approximate-symmetry.md), [E004](../explore/E004-multiscale-evidence-graphs.md) |
| 139 Log-concave sampling query complexity | Cost of sampling under oracle access | [E011](../explore/E011-sequential-risk-control.md), [E014](../explore/E014-value-of-computation.md) |
| 186 Uniform influence and sharp thresholds | Phase transitions in monotone properties | [E013](../explore/E013-agent-topology-and-correlation.md) |

Other keyword matches at baseline worth a first look: 099 and 121 (edit distance, for
sequence alignment), 113 (entropy of perfect matchings), 235 (random SAT thresholds).
Keyword hits on "chromatic" also catch chromatic homotopy theory (314, 318, 319) and
"partition" catches the set-theoretic Partition Principle (244); those are false friends.

## Problem candidates

Each row is a question to triage, not a commitment. Promote one only by writing an
`explore/` brief or a program contract within Christopher's authorization.

| ID | Source | Candidate question | State |
| --- | --- | --- | --- |
| OW001 | 169 | Does the permutation model behind elementary positivity give a bijective or sign-reversing explanation for the height-two and higher H3 coefficients already studied in `research/partitions`? | PENDING triage |
| OW002 | 169, 168 | Which neighbouring positivity statements (Schur and h-positivity cases, KL-type invariance) remain open after these releases, and does either family's Lean coverage supply reusable definitions for our mathlib bridge? | PENDING triage |
| OW003 | 122, 121 | Is there a tractable deletion or edit channel model close to real sequencing error profiles where the quasipolynomial decoder or the edit-distance approximation gives a usable algorithm? | PENDING triage |
| OW004 | 378 | If the ETH disproof survives review, what does subexponential #k-SAT imply for verification cost budgets in E014? | WAITING on external review |
| OW005 | 378 | Where does the method's $\sqrt{\log n}$ come from, and which consequences follow? | PROMOTED to [problems/eth](../problems/eth/README.md) at the operator's request, 2026-10-29 |

## Update log

Newest first. One entry per check: date, upstream commit seen, what changed, triage result.

- **2026-10-27** - Baseline recorded at `7ef5c0cc5`. Watch set, interest profile and four
  problem candidates created. No triage performed yet.
