# The harness as a research subject

This directory studies whether a change in orchestration improves research outcomes at a stated cost. It is separate from proving a neural architecture better.

Permitted candidate changes include team composition, packet wording, role separation, dependency graphs, bounded communication, retrieval strategy, and review order. Candidate generation may be recursive: a meta fleet can suggest how to evaluate a later meta fleet. Each proposal still needs a fixed scope, an external evaluation boundary, and a finite budget. Recursion is a source of candidate ideas, not authority to run indefinitely.

Start with `protocol.md`, use `scorecard.md`, and record every evaluated candidate in `change-ledger.md`. `candidates/M0001-independent-first-pass.md` is an unexecuted example proposal. The initial ledger contains no completed trials, accepted improvements, or rejected experimental results.

The command-line `compare` facility compares supplied evaluation records. A computed comparison is only as meaningful as the task selection, scoring, independence, and cost measurements behind those records. No function in this repository establishes a globally optimal fleet or guarantees discovery.
