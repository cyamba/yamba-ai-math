# ETH-D02. SETH, NSETH and Gap-ETH: what is refuted and what survives

| Field | Value |
| --- | --- |
| Category | Fine-grained complexity |
| Source items | "Refutation of fixed-width SETH vs re-anchoring to UW-SETH"; "Decoupling of SETH from ETH and collapse of ETH-hard approximation barriers" |
| Status | **Conditional consequence; survivors partly mapped** |
| Depends on the upstream theorem | Yes |
| Score (I/B/T/L/Lean) | 3 / 2 / 4 / 3 / 1, composite **2.7** |
| Subresults | [SR-09](../subresults/SR-09-coverage-map.md#the-clause-width-frontier) |

## Statement

If Theorem 1.1 holds, ETH, SETH, Gap-ETH (Dinur 2016; Manurangsi and Raghavendra 2017, "ETHA")
and NSETH (Carmosino et al., ITCS 2016) are false as stated, since each concerns fixed $k$
(preprint Section 1.1.1). Hypotheses that survive include:

* the **Orthogonal Vectors Conjecture** (implied by SETH, Williams 2005, not equivalent to it):
  LCS and dynamic time warping lower bounds (Abboud, Backurs, Vassilevska Williams, FOCS 2015)
  and regular-expression matching keep their basis; edit distance (Backurs and Indyk, STOC
  2015) as well where it reduces from OV;
* **unbounded-width CNF-SAT** hardness ("no $2^{(1-\delta)n}$ for CNF-SAT with $\mathrm{poly}(n)$
  clauses"): Fréchet distance, diameter approximation, treewidth-parameterized IS and DS;
* the 3SUM and APSP conjectures (not ETH-based).

## Open parts

1. A precise list of published lower bounds that used SETH only through fixed $k$ and have **no**
   OV or unbounded-width route: these lose all justification.
2. Does the algorithm refute the **Merlin–Arthur** or **AM** versions that were not already
   refuted (Williams refuted MA-SETH in 2016)? It decides, so all "deterministic, randomized and
   nondeterministic" fixed-width versions fall.
3. Gap-ETH consequences: parameterized inapproximability of Clique and Dominating Set
   (Chalermsook et al.) lose their basis; quasi-polynomial lower bounds proved from ETH via
   birthday repetition survive under polylog-ETH with small losses ([ETH-D08](ETH-D08-polylog-eth-and-surviving-lower-bounds.md)).

## Resource boundary

One literature agent; a table, no theorems.
