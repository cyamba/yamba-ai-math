# ETH-D08. Replacement hypotheses: polylog-ETH and the lower bounds that survive

| Field | Value |
| --- | --- |
| Category | Fine-grained complexity |
| Source items | New (synthesis of the "consequences" items) |
| Status | **Open** (definitional and survey work) |
| Depends on the upstream theorem | Yes |
| Score (I/B/T/L/Lean) | 4 / 3 / 3 / 4 / 1, composite **3.2** |
| Subresults | [SR-09](../subresults/SR-09-coverage-map.md) |

## Task

Formulate and study the weakest natural hypotheses consistent with the preprint, e.g.

* **polylog-ETH($c$)**: 3-SAT on $n$ variables needs $2^{n/(\log n)^{c}}$ deterministic time;
  consistent with the preprint for $c>\frac12$ (and with any future improvement to exponent
  $n/(\log n)^{\alpha}$ only if $c\ge\alpha$);
* **#polylog-ETH** for counting;
* **barrier-relative hypotheses**: "no algorithm of the deformation type beats $\sqrt{\log}$"
  (meaningful only once [ETH-A01](../01-algorithmic-core/ETH-A01-break-the-sqrt-log-barrier.md)
  has a barrier theorem).

Then list which ETH-based lower bounds survive with polylog losses: every linear reduction
(SERF) turns $2^{\Omega(n)}$ into $2^{\Omega(n/(\log n)^c)}$; polynomial-size reductions
($N=n^a$) turn it into $2^{\Omega(n^{1/a}/(\log n)^{c})}$.

## Why it matters

Hundreds of conditional lower bounds rested on ETH; the literature search of the independent
Anthropic paper reportedly counts over 800 papers depending on ETH or SETH (secondary source,
OfficeChai, 2026-10-27, not inspected). A clean replacement hypothesis preserves most of them up to polylog
factors and makes the true remaining question, the exponent of 3-SAT, explicit.

## Resource boundary

One agent for definitions and a survey table; no theorems claimed.
