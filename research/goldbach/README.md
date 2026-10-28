# Goldbach parity bridge

This directory contains the first bounded program for investigating a signed rough-pair approach to binary Goldbach. Goldbach remains open. The first focus is the precise pointwise inequality in [orchestrated-prompt.md](orchestrated-prompt.md); neither the finite checks nor the saved run supply a proof.

The machine-readable [program](../../programs/goldbach-parity-bridge.json) assigns a six-stage theorem fleet, separates declared author and critic profiles, and caps the planned dispatch at 14 proxy units for one round. The units are not a count of tokens, money or evidence quality.

## Recorded command-backed finite run

A real harness command DAG was executed using a deterministic Python adapter, not an LLM model. It checked the finite reflection identity for 998 even N from 6 through 2,000, the shared-summand obstruction for 66 targets in the indicated progression, and quarter-root ties at N=8 and 12 using a separate trial-division method. Both prior failed attempts and the completed attempt are retained in [the run record](evidence/deterministic-run.json).

The successful receipt records `completed_execution` and `research_validated: false`. The generated role profiles are not independent semantic reviewers, because all stages were carried out by the same scripted program. In particular, this is not a model-backed proof search, a mathematical review or a proof of Goldbach. Token usage and provider costs were not measured.

Reproduce the bounded checks, with Python 3.11 or newer and the repository's standard-library harness:

```sh
python3 -m harness plan programs/goldbach-parity-bridge.json
python3 -m harness run programs/goldbach-parity-bridge.json --backend command --command /usr/bin/python3 research/goldbach/checks/deterministic_worker.py
```

Use the local Python path on systems without `/usr/bin/python3`. The actual model-backed research run requires a trusted provider adapter implementing [the adapter contract](../../docs/adapter.md), an explicit budget and independent substantive critique. Do not replace it with a synthetic demonstration and present that as research.
