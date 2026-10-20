# Worker adapter contract

The local harness is provider-neutral. Planning and manual handoffs work without model credentials. To run real model-backed workers, provide a trusted executable that implements the contract below. You choose its model, tools, credentials, and billing limits outside research documents and worker outputs.

## Invocation

```sh
python3 -m harness run programs/evidence-preserving-attention.json \
  --backend command --command /absolute/path/to/worker --adapter-option
```

Put `--command` last: everything after it is passed as an argument vector, without shell expansion. Each ready stage starts a new process at the repository root, subject to `max_workers` and its timeout. This is concurrency of processes, not a sandbox. The command inherits the operator's permissions and environment; it may use tools or incur charges if the configured adapter permits that.

The adapter should honor the supplied scope, timeout, evidence requirements, and its own provider limits. This first runner bounds dispatches, rounds, and wall time; it does not independently enforce token billing, arbitrary tool actions, or semantic stop conditions.

## Standard input

Read one UTF-8 JSON object. Protocol version `"1"` includes:

- `run_id`, `step`, and `agent`: the assignment, role, requirements, and dependencies.
- `fleet_plan`: all assignments and the declared budget objective.
- `instructions.repository`: root `AGENTS.md` contents.
- `instructions.scoped`: applicable nested instructions for the program's briefs.
- `instructions.role` and `instructions.skills`: role card and selected reusable workflows.
- `instructions.output_contract` and `instructions.trust_boundary`.
- `program`, `briefs` with inline source text, and `upstream` completed predecessor results.

The adapter must treat source text and predecessor responses as research data. They do not grant permission to change repository instructions or execute commands embedded in evidence.

## Standard output

Write exactly one JSON object and no progress text:

```json
{
  "summary": "Describe the actual contribution, limitations, and unresolved questions.",
  "claims": [
    {"text": "A candidate theorem remains unproved.", "status": "conjecture", "source": "path or primary reference if relevant"}
  ],
  "artifacts": [],
  "usage": {"input_tokens": 100, "output_tokens": 50}
}
```

The numbers above illustrate the schema; they are not measured usage. The entire `usage` object is optional. If present, both counts are required nonnegative integers. Missing usage stays unknown in the receipt. The runner records reported usage, not independently verified billing.

`summary` must be nonempty. `claims` and `artifacts` are required lists and may be empty. A claim requires `text` and one status: `established`, `proved`, `conjecture`, `empirical`, `unverified`, or `refuted`. Use `source` for provenance; explain proof assurance and review in the summary or artifact. A label does not certify truth or correctness. Artifact strings are recorded, not executed or certified to exist. Do not claim an artifact was produced unless it exists.

Send adapter progress to standard error, without secrets. The runner does not persist adapter stderr, which can contain credentials or provider details. Packets and valid results are persisted, so they must also exclude secrets. Maximum stdout result size is 1 MiB; a command dispatch packet is limited to 8 MiB. Reduce output or split the program if necessary.

## Failures and receipts

Invalid JSON, invalid result fields, a nonzero exit, or a timeout fails that stage. Its dependents are blocked; unrelated branches may complete. Dispatch preparation failures are also recorded when the run directory remains writable. There are no automatic retries. A fresh output path is required to avoid overwriting an earlier run.

`completed_execution` means all protocol responses were collected. `research_validated` remains false until research review is performed and recorded separately. Task-specific success and semantic stop conditions require the orchestrator and reviewers; this runner is not a proof checker or novelty judge.

## Manual and replay modes

`packet PROGRAM` and `run PROGRAM --backend manual` prepare all task packets with status `awaiting_execution`. Dependent packets contain null predecessor results. A human or agent orchestrator must supply completed upstream results before issuing those tasks; the runner has not executed them.

`run PROGRAM --backend replay --replay-dir PATH` reads `<step-id>.json` responses from that directory as each stage becomes ready. Missing or malformed responses fail the stage. Replay is labeled explicitly and never represented as a fresh independent result.

[The offline worker](../examples/offline_worker.py) is a deliberately synthetic protocol demonstration. To connect an actual provider, replace it with your own adapter; the lab does not assume a particular model service or agent SDK.
