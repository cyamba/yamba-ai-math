<p align="center">
  <img src="assets/yamba-ai-math-banner.webp" alt="Yamba AI Math: intelligent mathematical solutions, agentic AI and mathematics" width="100%">
</p>

# Yamba AI Math Lab

**New mathematics for smaller, smarter, more cost-effective AI.**

This is an open research workspace for investigating neural architectures, attention, geometric deep learning, reliable reasoning, world models, and agent systems. The aim is to turn promising mathematical ideas into precise statements, real experiments, and eventually useful models and software.

The current phase is **explore**. Start with [the research angles](explore/README.md): each brief identifies a question, prior work, an unproved theorem target, an obstruction, and a small experiment capable of disproving the idea. No model superiority or new theorem is claimed by the initial collection.

## Two connected projects

1. **The mathematical AI universe:** which structures let a model preserve useful information, reason correctly, learn efficiently, or predict the consequences of actions?
2. **The research harness:** which agent roles, team compositions, communication patterns, and review methods help investigate those questions effectively?

The harness can study and improve itself through controlled trials. Its own success does not establish that an architecture under study works. Read the [research manifesto](docs/manifesto.md) and [evidence protocol](docs/research-protocol.md) for the standards connecting ideas to results.

## Start exploring

- [Evidence-preserving attention](explore/E001-certified-attention-compression.md): can compression retain the few distinctions that determine an answer?
- [Approximate symmetry](explore/E003-approximate-symmetry.md): when does structure save more estimation error than it introduces bias?
- [Action-identifiable world models](explore/E005-action-identifiable-jepa.md): what must predictive representations retain to support interventions and decisions?
- [Decision-sufficient world models](explore/E006-decision-sufficient-world-models.md): can a compact state preserve good actions without reconstructing everything?
- [All research briefs](explore/README.md), including reliability, multiscale models, agent topology, and value of computation.

Ideas are welcome even when speculative. Label the uncertainty, identify the closest existing work, and make the proposed advantage falsifiable.

The [integer-partition investigation](research/partitions/README.md) records the
user-authorized expansion into constructive combinatorics: an audit of the
supplied positivity proofs, a reproduced height-two theorem with an end-to-end
Lean proof for every finite alphabet, and an illustrated article. It does not claim a general open-problem
solution or an improvement to an AI architecture.

The [Parikh matrix research](research/parikh/README.md) continues Christopher Yamba's 2006
thesis on Parikh matrices and permutation statistics. It contains two articles with their
LaTeX sources, Lean 4 proofs and verification checks. That directory is **all rights
reserved** and excluded from the MIT License (see its
[NOTICE](research/parikh/NOTICE.md)).

## Run the harness

Clone the repository and work from its root. Python **3.11+** is the only dependency; no model account is required for planning, handoffs, replay, or tests.

```sh
python3 -m harness list
python3 -m harness validate
python3 -m harness plan programs/evidence-preserving-attention.json
python3 -m harness packet programs/evidence-preserving-attention.json
python3 -m unittest discover -s tests -v
python3 scripts/check_repository.py
```

`packet` creates a fresh ignored `.runs/` directory containing the plan and worker instructions. Its status is `awaiting_execution`. It has prepared work, not performed research. Dependent packets have empty upstream results until the orchestrator supplies their predecessors' outputs.

For automated execution, supply your own trusted worker command:

```sh
python3 -m harness run programs/evidence-preserving-attention.json \
  --backend command --command /absolute/path/to/your-worker --your-option
```

The adapter receives one JSON packet on standard input and returns structured JSON on standard output. Independent branches run concurrently; a failed stage blocks its dependents. The runner records packets, results, events, and a receipt. There are no automatic retries or bundled paid inference services. The adapter runs with your permissions; it is not sandboxed by this harness. See [the adapter contract](docs/adapter.md).

To exercise the orchestration locally without inference:

```sh
python3 -m harness run programs/evidence-preserving-attention.json \
  --backend command --command python3 examples/offline_worker.py
```

The example worker explicitly returns **synthetic protocol fixtures**. They demonstrate execution only. Saved real or synthetic responses can also be validated using `--backend replay --replay-dir PATH`, with files named `<step-id>.json` as listed by `plan`.

## Agents, tags, and fleets

[Agent cards](agents/registry.json) define contributions such as literature discovery, formal mathematics, geometry, world models, causal investigation, independent criticism, experiment design, and synthesis. Tags describe research styles and specialties; they are declared routing information, not credentials. Character tags include `first-principles`, `constructive-skeptic`, `counterfactual-thinker`, and `frugal`. A program's `preferred_tags` breaks cost ties; a fleet stage's `required_tags` filters assignments.

[Fleet templates](fleets/registry.json) define workflows for exploration, proofs, attention architectures, world models, pairs, agent topology, and harness evaluation. Programs supply the objective and resource limits. A coordinator frames the work; a deterministic planner assembles feasible role assignments.

The planner finds the exact minimum declared dispatch cost, then uses preferred tags and stable tie breaks. This is optimality for a small finite allocation problem, not a guarantee of the best research team. Reusing a role for another stage costs another dispatch. Different roles can still share the same model and the same errors.

See [program examples](programs/README.md), [the architecture](docs/architecture.md), [AGENTS.md](AGENTS.md), and the [skill catalog](SKILLS.md). A [continuation handoff](docs/handoff.md) is ready for the next investigation.

## Improve the harness through evidence

[The meta program](meta/README.md) compares a fixed champion with a challenger on frozen evaluations, including correctness, evidence quality, coverage, cost, and human review. Improvements have recorded assumptions and rollback conditions.

```sh
python3 -m harness compare examples/evaluations/champion.json examples/evaluations/challenger.json
```

Those records are synthetic fixtures. The comparison reports descriptive outcomes on matching cases and never authorizes promotion. There is no autonomous self-improvement result in this initial repository.

## Repository map

| Path | Purpose |
| --- | --- |
| `explore/` | Mathematical research angles and brief template |
| `references/` | Primary-source reading and inspection ledger |
| `research/partitions/` | Partition research, exact counterexamples, formal proofs, and article |
| `agents/`, `fleets/` | Role cards, categories, tags, and workflow registries |
| `skills/`, `SKILLS.md` | Reusable research workflows |
| `programs/` | Bounded investigations ready to plan or dispatch |
| `harness/` | Provider-neutral planner, runner, and evaluation comparison |
| `meta/` | Controlled improvement of the research harness |
| `docs/` | Research standards, architecture, and adapter contract |
| `tests/`, `examples/` | Behavioral checks and explicitly synthetic examples |

Contribute through [the contribution guide](CONTRIBUTING.md). Code and original repository material use the [MIT license](LICENSE); linked third-party research retains its own terms.
