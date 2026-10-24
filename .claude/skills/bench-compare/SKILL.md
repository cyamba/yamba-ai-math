---
name: bench-compare
description: Compare two yamba-ai-math benchmark records of the same problem axis by axis, as a descriptive paired report. Meta-harness only.
disable-model-invocation: true
argument-hint: <baseline record id or path> <candidate record id or path>
---

# Compare two versions

Run `python3 .claude/bench/bench.py compare <baseline> <candidate>`. It refuses different problems or
metric specifications and never counts an unknown, pending or n/a axis as a win.

Report, in the vocabulary of `meta/scorecard.md` ("Paired decision report"): the two framework commits,
problem, axis outcomes (better, worse, equal, unknown) with deltas, gate changes, observed dominance and
whether it is claim-eligible, and every limitation the command lists. One paired run is descriptive, not
significant. Recommend nothing stronger than `inconclusive` unless a preregistered trial in `meta/`
defines the criterion, and state that `promotion_authorized` is false.
