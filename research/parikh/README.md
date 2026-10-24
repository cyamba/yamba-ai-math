# Parikh matrices and permutation statistics

Research by Christopher Yamba, continuing his 2006 degree thesis *Parikh Matrices and
Permutation Statistics* (Stockholm University, Examensarbeten i matematik 2006:8).

> **All rights reserved.** This directory is excluded from the repository's MIT License. See
> [NOTICE.md](NOTICE.md).

The Parikh matrix of a word records the counts of its scattered subwords made of consecutive
letters (pairs on the third diagonal, triples on the fourth, and so on). The thesis proved that
for permutations the third diagonal determines the whole matrix, and that the number of
permutations with a given second-order Parikh vector equals a descent-set count. These articles
take the same questions to words with repeated letters.

## Articles

| | Article | Files |
|---|---|---|
| 1 | *Partition stabilization and semigroup gaps for ternary Parikh matrices* (19 Oct 2026) | [article page](https://www.christopheryamba.com/math/ternary-parikh/) |
| 2 | *From Euler numbers to the golden ratio: rigidity, ranges and the most ambiguous Parikh matrices for words with repeated letters* (23 Oct 2026, 55 pp) | [PDF](article2/parikh-golden-ratio.pdf) · [LaTeX source](article2/parikh-golden-ratio-source.zip) · [verification package](article2/parikh-golden-ratio-verification.zip) · [article page](https://www.christopheryamba.com/math/parikh-golden-ratio/) |
| 3 | *Four diagonals for doubled letters, five for tripled: completeness of Parikh matrices* (version 2, 24 Oct 2026, 16 pp; version 1, 23 Oct 2026) | [PDF](article3/parikh-four-diagonals.pdf) · [LaTeX source](article3/source/) · [Lean proofs](article3/lean/) · [checks](article3/checks/) · [verification package](article3/parikh-four-diagonals-verification.zip) · [article page](https://www.christopheryamba.com/math/parikh-four-diagonals/) · [version 1](article3/v1/) |

### Article 2 in brief

- **Rigidity.** For every content, the pair-count vectors that determine the whole matrix are
  characterised by a local rule on every three consecutive letters.
- **Ranges.** For three letters, the least and greatest triple counts are given for every pair
  of pair counts. This includes the least remainder in the Cauchy inequality of Mateescu,
  Salomaa and Yu.
- **The most ambiguous matrices.** For content (a,2,c) with a ≤ c, the largest Parikh class
  has C(a+c, a) words iff c(c−1) ≤ a(a+c−1), a threshold asymptotic to the golden ratio.
- **Doubled letters.** A conjecture that the two alternating classes are the unique largest
  classes for content (2^k) once k ≥ 6, verified for k ≤ 12.

### Article 3 in brief

- **Theorem A.** If every letter other than the first and the last letter of the alphabet
  occurs at most twice, the first four diagonals determine the Parikh matrix. The proof gives
  explicit formulas: a *rectangle rule* and a *crossing chain*.
- **Theorem B.** For every n ≥ 2, two words of content (1, n, …, n) whose Parikh matrices
  differ only in the corner entry. Their window counts are ballot numbers, with the Catalan
  number C_n among them. So counts of length ≤ n do not suffice when inner letters occur n
  times.
- **Conjecture C.** Counts of length ≤ n+1 suffice when the inner letters occur at most n
  times. It holds for n ≤ 3; exhaustive tests support it for n = 4.
- **Theorem D (new in version 2).** A local pivot theorem: a long count is determined by the
  shorter counts as soon as one letter at distance at least 2 from both ends occurs at most
  twice, or it and its two neighbours occur at most three times. Hence (Corollary 1.2) the
  first five diagonals determine the Parikh matrix when the letters other than the first and
  the last occur at most three times. Explicit words (Proposition 7.1) show that the hypotheses
  cannot be relaxed, except possibly at a pivot that occurs four times.
- **Lean 4.** Theorems A and D and their corollaries are formalised at the level of words (core
  Lean 4.34, no `sorry`); build with `lake build` in [article3/lean/](article3/lean/).

### What is new in Article 3, version 2 (24 October 2026)

- New title (version 1: *Four diagonals suffice: completeness of Parikh matrices when letters
  occur at most twice*).
- New results: Theorem D and its explicit form (Theorem 6.8), Corollaries 1.2 and 1.3, and
  Proposition 7.1 (sharpness examples); a new Section 6 with the proofs and the chain lemma
  (Lemma 6.6, Table 1).
- Renumbering: Sections 6 and 7 of version 1 are now Sections 7 and 8, and its Table 1 is now
  Table 2; all earlier numbers are unchanged.
- Corrections and additions: Remark 3.2 (the equality case of the Cauchy inequality is known in
  full for single letters x, y, z); Salomaa's words in Example 4.5; the planar-network picture
  of total positivity (Remark 6.5); the Lean file `ParikhCompletenessThree.lean` and the check
  `check_c3.py`.
- Version 1 (PDF, source and verification package) is kept in [article3/v1/](article3/v1/).

Corrections, comments, questions and feedback are welcome at christopher.yamba@yambacode.com,
and so is access to two papers of Salomaa (2008 and 2015) that could not be consulted.

## Checking the results

Every computational statement has a standard-library Python check, and each exits with a
non-zero status on any failure.

- **Article 2:** unzip the verification package and run the checks from inside it, e.g.
  `python3 checks/check_r7_golden.py`.
- **Article 3:** run `python3 article3/checks/check_article3.py` (about 4 minutes) and
  `python3 article3/checks/check_c3.py` (about 40 seconds); add `--full` for the larger ranges.

## How this work was made

These results were developed with the assistance of an agentic AI harness. Anthropic's Claude
(through Claude Code, with several coordinated agents) and OpenAI's Codex assisted with the
exploration, the drafting of proofs and of the Lean formalisation, the computational checks,
the literature search and the drafting of the articles. Mathematical responsibility and
authorship rest with Christopher Yamba. Each result went through independent skeptic and
referee passes by AI agents before release. Those passes are not a human peer review.
