# ETH-A07. Close the gap between the Lean exponent and the manuscript's

| Field | Value |
| --- | --- |
| Category | Algorithmic core (formal) |
| Source items | "YMB-ETH-02: closing the $(\log\log n)^2/\log n\to\log\log n/\log n$ gap in Lean" (exponents corrected) |
| Status | **Open** |
| Depends on the upstream theorem | Yes (formalizes it) |
| Score (I/B/T/L/Lean) | 2 / 1 / 2 / 2 / 5, composite **2.0** |
| Subresults | none |

## Task

The openai/math Lean development proves time $(L+1)^{O_k(1)}2^{O_k(n(\log\log n)^2/\sqrt{\log n})}$
([378.md](https://github.com/openai/math/blob/main/lean/docs/378.md)); the manuscript proves
$n\log\log n/\sqrt{\log n}$ in general and $n/\sqrt{\log n}$ at bounded density via Appendix C.
Formalize the sharper bounds.

## Correction

The source summary attributes the extra $\log\log n$ to IPZ branching and proposes "buffered
clause-width compression". In the preprint the difference is between the rational-interpolation
route (Sections 3 to 5) and the tensor-contraction route (Appendix C); see
[SR-08](../subresults/SR-08-corrections-to-gemini-summaries.md), row 4.

## Plan

1. Formalize Theorem C.1 abstractly over $(\mathbb Z/2^P)[V]/(V^\ell)$ (contraction identity,
   tapered Hermite recovery Lemma C.4, mode expansion), separate from Turing-machine accounting.
2. Reuse `HermiteUniqueness.lean` and add a 2-adic valuation version.

## Closest work

openai/math `lean/OAI/Algorithms/SubexponentialSAT/` (level T); our
[`lean/`](../lean/) modules.

## Obstruction

Appendix C is long and arithmetic-heavy; the 2-adic precision bookkeeping is the risk.

## Resource boundary

A multi-iteration Lean project; first iteration: statement of Theorem C.1 and Lemma C.4 with
proofs of the algebraic identities only.
