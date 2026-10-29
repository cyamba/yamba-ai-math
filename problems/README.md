# Problems

Curated problem sets derived from external results, organized for fleets of agents. Each set
lives in its own folder, splits its problems into category subfolders, and keeps one Markdown
file per problem with a precise statement, status labels, closest work, an obstruction, a
smallest falsifier and a score used for ranking.

| Set | Source | Entry point | Ranking | Programs for the next iteration |
| --- | --- | --- | --- | --- |
| `eth/` | openai/math result 378, "The Exponential Time Hypothesis is False" (2026-10-25) | [eth/README.md](eth/README.md) | [eth/RANKING.md](eth/RANKING.md) | [ETH001](../programs/eth-point-dependent-designs.json), [ETH002](../programs/eth-dense-graded-counting.json), [ETH003](../programs/eth-formal-audit.json) |

Conventions shared by all sets:

- Claims carry one of the repository labels: **established**, **proved**, **conjecture**,
  **empirical**, **unverified**, **refuted** (see [AGENTS.md](../AGENTS.md)).
- Novelty is **not verified** until the closest prior work is inspected and recorded.
- A ranked list for the next fleet iteration lives in each set's `RANKING.md`, with the rubric
  that produced it and a novelty ledger.
- Proved subresults live in the set's `subresults/`, formal proofs in its `lean/` project
  with a `verification.json` certificate, experiments in `experiments/`, and draft write-ups
  in `articles/`. Publishing or submitting an article is the operator's decision.
- Sources cited by a set are recorded in the [reading list](../references/reading-list.md)
  with inspection levels; external developments go to the [novelty radar](../novelty_radar/README.md).
