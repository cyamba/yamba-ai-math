---
id: ETH-B08
source: new (this program)
category: exponent-frontier
status: open question (no conjecture asserted)
---

# ETH-B08: Is `2^{n / (log n)^{1/2 + o(1)}}` the truth for #3-SAT?

Both of OpenAI's routes stop at `n / sqrt(log n)` up to `log log` factors, and [ETH-B01](ETH-B01-sqrt-log-barrier.md)
shows that the replacement-form template with `M_0`-type rows cannot do better. Natural questions:

1. **Weaker hypotheses that may still hold.** Formulate a "`sqrt(log)`-ETH": #3-SAT (or 3-SAT) has no
   `2^{n / (log n)^{1/2 + delta}}` algorithm for some `delta > 0`. What would it imply under the standard
   linear-size reductions (SERF class, [ETH-D02](../D-complexity-consequences/ETH-D02-serf-collapse.md))?
   This is only a framework for organising lower bounds, not a conjecture of this program.
2. **Restricted-model lower bounds.** Prove that a natural algebraic model containing both routes
   ("sums of products of low-degree forms with separable measurement structure, recovered by Hermite
   interpolation") needs `2^{n / (log n)^{1/2 + o(1)}}` operations for #3-SAT. ETH-B01 is a first step.
3. **Decision vs counting.** Does deciding 3-SAT admit a faster route than exact counting? Every known step
   here counts. Combining with Schoening/PPSZ-style local search on the subexponential leaves is unexplored.
