# Articles of the `eth` set

| Article | Status | Files |
| --- | --- | --- |
| **Point-dependent measurement designs and the square root in the subexponential #SAT algorithm** (10 pages) | Draft for operator review, 2026-10-29. Not submitted or posted. Novelty **not verified**. | [LaTeX source](point-dependent-designs/main.tex), [PDF](point-dependent-designs/main.pdf) |

The article writes up [SR-01](../subresults/SR-01-isoperimetric-rank-barrier.md) to
[SR-05](../subresults/SR-05-stress-duality-and-products.md), the top of the
[subresult ranking](../RANKING.md#subresults-ranked), with the small exact cases of SR-02 and
the open problems of [ETH-A03](../01-algorithmic-core/ETH-A03-point-dependent-designs.md). Every
statement in it is stated with the same status as in the subresult files, and the Lean
declarations it cites are in the certificate [`verification.json`](../lean/verification.json).

Before any submission or posting (the operator's decision):

1. resolve every finding of the separate critic's review (recorded in the subresult files);
2. complete the closest-work checks listed in the [novelty ledger](../RANKING.md#novelty-ledger),
   including the working group's report and the reported second refutation;
3. decide authorship and the AI-assistance statement (the draft says it was prepared with
   Claude under the direction of Christopher Yamba);
4. re-run `python3 ../lean/verify.py` and rebuild the PDF with `latexmk -pdf main.tex`.

The PDF built on 2026-10-29 has SHA-256 `52e993363f4a29f04df1302dd835a01d6a12a2d66294c2c3573a6921fb28b5c9`.
