# yambench: benchmarking versions of the framework

`yambench` scores one **version** of the research framework (a git commit) on one **registered open
problem**, after a run and at intermediate steps. It records what was benchmarked: framework and
output commits, branch, framework fingerprint, problem and program hashes, client, model, effort,
tokens, compactions and human turns. Records feed a radar dashboard. Python 3.11 standard library only.

## The twelve benchmarks

Each axis is 0–100, or `pending` (awaiting judgment), `unknown` (not measured) or `n/a` (does not apply).
Unknown and n/a are gaps on the radar, never zero. Modes: **C** computed, **K** checklist, **J** judged
by an independent `bench-assessor` against an anchored rubric (0/25/50/75/100).

| ID | Family | Benchmark | Question | Mode |
| --- | --- | --- | --- | --- |
| B01 | Progress | Frontier depth | How far up the problem's preregistered milestone ladder (prove or refute branch) does the output stand? | K |
| B02 | Progress | Formal assurance | Which maintainer-registered formal targets are machine-checked, with allowed axioms and current hashes? | C |
| B03 | Progress | Decisive finding | What is the single most decisive off-ladder finding: counterexample, refutation, obstruction, bound? | C+J |
| B04 | Progress | Contract fulfilment | Were the program's deliverables and success criteria met? Capped at 50 unless the program was hash-frozen at start. | K/J |
| B05 | Rigor | Claim integrity | Are material claims labeled, scoped and supported? Computed flags plus an audit sample. | C+J |
| B06 | Rigor | Adversarial review | Did an independent challenge, in a distinct thread, run checks and resolve objections every round? | K/J |
| B07 | Rigor | Reproducibility | Do recorded hashes, checks and declared reproduction commands re-verify? Coverage shown. | K |
| B08 | Rigor | Literature grounding | Was the closest prior work inspected (level T+) and is the novelty label honest? | C+J |
| B09 | Operations | Resource efficiency | Measured effective tokens against the problem's reference budget; n/a without progress. | C |
| B10 | Operations | Context economy | Tool calls before the first file write, peak context, compactions, redundant reads. | C |
| B11 | Operations | Operational autonomy | Harness-executed stages, agent-executed stages, failures, steering and correction turns. | C |
| B12 | Operations | Continuity | Next step, remaining obligations, preserved evidence, updated status, cold-start resume. | K/J |

Hard gates, shown beside the radar: **G1** no fabrication, **G2** scope and permissions, **G3** budget
and stop conditions, **G4** no benchmark leakage (rubric canaries). Full definitions, formulas, unknown
policies and gaming risks live in [spec/metrics.json](spec/metrics.json) and [spec/gates.json](spec/gates.json).

There is deliberately **no blended score** (`meta/protocol.md` §4). Versions are compared axis by axis on
the same problem; `compare` reports observed dominance and never counts an unknown axis as a win.

## Workflow

```sh
B=".claude/bench/bench.py"
python3 $B validate                                   # spec, records, canary isolation
python3 $B start --problem <id> --session codex:<id>  # arm a live run (optional)
python3 $B snapshot --step "after r1 propose"         # intermediate computed snapshot
python3 $B stop
python3 $B sessions --framework-commit <sha>          # find Codex threads to pin
python3 $B collect --problem <id> --commit <output> --framework-commit <version> \
    --run-dir <abs .runs dir> --session codex:<lead id> [--deep]
python3 $B finalize --key <key> --judgments <file> --audit <file>
python3 $B compare <baseline record> <candidate record>
python3 $B dashboard                                  # offline HTML with embedded records
python3 $B export-artifact [--out-dir DIR]            # dataset files and page for the published dashboard
```

`collect` materializes both commits with `git archive` under ignored `.runs/bench/<key>/`, so scoring
reads frozen snapshots and never checks anything out. It writes a judge packet for `bench-assessor` and
an audit packet for `bench-auditor`; `finalize` rejects an assessor or auditor whose session authored
the run, off-anchor scores and judgments without evidence. In Claude Code, `/bench-run` drives the
whole sequence.

Telemetry: Codex rollouts are read natively from `~/.codex/sessions` (lead, child and overhead threads).
Claude Code sessions are read through `recorder.py` from the agentic-workbench recorder
(`YAMBENCH_RECORDER` overrides its path). Without telemetry, cost, context and human-turn items stay
unknown.

## Dashboard

A private claude.ai dashboard (URL in [dashboard.json](dashboard.json)) shows the radar, gates,
provenance, comparison against another version, per-axis trends across versions and within a run, flags
and definitions. Its page is [dashboard/page.html](dashboard/page.html); `/bench-dashboard` uploads fresh
datasets after each benchmark. `bench.py dashboard` writes the same page offline with embedded data.

## Records

Final records are tracked in [records/](records/), one JSON file each, scrubbed of local paths and
message text. Schema `yambench.record/1`: `provenance` (framework, output, problem, program, run,
sessions, telemetry), `metrics`, `gates`, `flags`, `assessment`, `trajectory` (snapshots), and
`promotion_authorized: false`. A record whose problem ladder was registered after the run is
`retrospective` and cannot support a dominance claim.

## Adding a problem

Add an entry to [spec/problems.json](spec/problems.json) **before** the run it will measure: workspace,
programs, closest work, formal targets (maintainer only), reference budget, findings probes,
continuity probes, reproduction commands, and a ladder of milestones built from the check kinds
`file_exists`, `sha256_matches`, `json_path`, `run_json_equals_sha`, `review_verdict`,
`verification_declaration`, `md_heading` and `judged`. Changing a metric definition or rubric is a new
spec version; records from different specs are not compared.

## Tests

```sh
python3 -m unittest discover -s .claude/bench/tests -v
```
