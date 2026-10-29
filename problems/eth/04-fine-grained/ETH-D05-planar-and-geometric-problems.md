# ETH-D05. Planar and geometric problems: can the algebra beat $2^{O(\sqrt n)}$?

| Field | Value |
| --- | --- |
| Category | Fine-grained complexity |
| Source items | "Vacation of conditional fine-grained and planar lower bounds" (overstated) |
| Status | **Open**; the source's claimed consequence is wrong |
| Depends on the upstream theorem | No for the question; yes for motivation |
| Score (I/B/T/L/Lean) | 4 / 4 / 2 / 3 / 1, composite **3.2** |
| Subresults | [SR-08](../subresults/SR-08-corrections-to-gemini-summaries.md), row 12 |

## Correction

Planar 3-SAT, planar Independent Set and similar problems have $2^{O(\sqrt n)}$ algorithms
(separators, treewidth), and ETH implied $2^{\Omega(\sqrt n)}$ lower bounds through quadratic
crossover gadgets. If ETH falls, those lower bounds lose their basis, but the new algorithm on
planar inputs costs $2^{O(n/\sqrt{\log n})}$, which is **worse** than $2^{O(\sqrt n)}$. Nothing
like $2^{O(\sqrt n/\log n)}$ follows.

## Task

Combine separator structure with the deformation: is planar #3-SAT solvable in
$2^{O(\sqrt n/(\log n)^{\alpha})}$ for some $\alpha>0$? Natural plan: a separator of size
$O(\sqrt n)$ splits the instance; the boundary assignments are the bottleneck
($2^{O(\sqrt n)}$ of them). Treat the boundary variables as the "measurements" of a design: at
each node the two sides interact through the boundary only, and a deformation might let them
interact through fewer effective bits.

## Obstruction

Treewidth-based dynamic programming is optimal for many problems relative to SETH-type
hypotheses on path decompositions (Lokshtanov, Marx, Saurabh 2011); those hypotheses now need
re-examination, but the separator bottleneck is information-theoretic for exact table methods.

## Smallest falsifier

A planar family where every design at every node needs $\Omega(\sqrt n)$ measurements (rank
lower bound in the style of SR-03) would show the method cannot help.

## Resource boundary

Two agents (separator-design construction; rank lower bound), one critic.
