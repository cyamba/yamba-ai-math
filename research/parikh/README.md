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
| 3 | *Four diagonals suffice: completeness of Parikh matrices when letters occur at most twice* (23 Oct 2026, 9 pp) | [PDF](article3/parikh-four-diagonals.pdf) · [LaTeX source](article3/source/) · [Lean proofs](article3/lean/) · [checks](article3/checks/) · [verification package](article3/parikh-four-diagonals-verification.zip) · [article page](https://www.christopheryamba.com/math/parikh-four-diagonals/) |

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
  times. Exhaustive tests support it for n = 3 and n = 4.
- **Lean 4.** Theorem A and its lemmas are formalised at the level of words (core Lean 4.34,
  no `sorry`); build with `lake build` in [article3/lean/](article3/lean/).

## Checking the results

Every computational statement has a standard-library Python check, and each exits with a
non-zero status on any failure.

- **Article 2:** unzip the verification package and run the checks from inside it, e.g.
  `python3 checks/check_r7_golden.py`.
- **Article 3:** run `python3 article3/checks/check_article3.py` (about 4 minutes; add `--full`
  for the larger ranges).

## How this work was made

Generative AI tools assisted with the exploration, the drafting of proofs and of the Lean
formalisation, the computational checks, the literature search and the drafting of the
articles. The tools were Anthropic's Claude (through Claude Code) and OpenAI's Codex.
Mathematical responsibility and authorship rest with Christopher Yamba. Each result went
through independent skeptic and referee passes before release. Those passes are not a human
peer review.
