"""Build, scrub and validate benchmark records; apply independent judgments and audits."""

from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path

from . import BenchError, __version__
from .spec import (ANCHORS, BENCH_ROOT, GATE_IDS, KNOWN_METRIC_IDS, METRIC_COUNT, metric_defs, metric_ids, sha256_bytes,
                   sha256_file, spec_digest)
from .telemetry import public

SCHEMA = "yambench.record/1"
RECORDS_DIR = BENCH_ROOT / "records"
ANCHOR_METRICS = ("B03", "B05", "B13", "B14")
GATE_STATUSES = {"pass", "fail", "review", "unknown"}
# POSIX homes, and Windows homes with forward slashes or (possibly JSON-escaped) backslashes.
HOME_RE = re.compile(r"/(?:Users|home)/[^/\s\"]+|[A-Za-z]:(?:\\+|/)Users(?:\\+|/)[^\\/\s\"]+", re.I)


def now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def engine_sha256() -> str:
    files = sorted((BENCH_ROOT / "yambench").glob("*.py"))
    return sha256_bytes("".join(f"{p.name}\0{sha256_file(p)}\n" for p in files).encode())


def record_id(created_at: str, framework: str, problem_id: str, kind: str) -> str:
    stamp = created_at.replace("-", "").replace(":", "")
    return f"{stamp}-{framework[:7]}-{problem_id}-{kind}"


def scrub(value, replacements: list[tuple[str, str]]):
    """Replace local absolute prefixes so tracked records carry repo-relative paths only."""
    if isinstance(value, str):
        for old, new in replacements:
            value = value.replace(old, new)
        return HOME_RE.sub("~", value)
    if isinstance(value, list):
        return [scrub(item, replacements) for item in value]
    if isinstance(value, dict):
        return {key: scrub(item, replacements) for key, item in value.items()}
    return value


def family(model: str | None) -> str | None:
    if not model:
        return None
    lowered = model.lower()
    if "claude" in lowered or lowered in {"opus", "sonnet", "haiku", "fable", "inherit"}:
        return "claude"
    if "gpt" in lowered or "codex" in lowered or lowered.startswith(("o1", "o3", "o4")):
        return "openai"
    return lowered


def build(*, spec: dict, problem: dict, computed: dict, kind: str, created_at: str, framework: dict,
          output: dict | None, program: dict, run: dict, sessions: list[dict], telemetry: dict,
          replacements: list[tuple[str, str]], assessment: dict | None = None,
          trajectory: list | None = None, step: str | None = None, limitations: list[str] | None = None) -> dict:
    retrospective = bool(problem.get("registered_after_run"))
    notes = list(limitations or [])
    if retrospective:
        notes.append("Retrospective: the problem's ladder was registered after the run; excluded from dominance claims.")
    notes.append("Benchmarks describe this run on this problem; they never authorize promotion (meta/protocol.md).")
    summary = {k: v for k, v in telemetry.items() if k not in ("window",)}
    record = {
        "schema": SCHEMA,
        "record_id": record_id(created_at, framework["commit"], problem["id"], kind),
        "kind": kind,
        "step": step,
        "created_at": created_at,
        "spec": {"version": spec["metrics"]["spec_version"], "digest": spec_digest(spec), "hashes": spec["hashes"]},
        "engine": {"version": __version__, "sha256": engine_sha256()},
        "provenance": {
            "framework": framework,
            "output": output,
            "problem": {"id": problem["id"], "title": problem["title"], "statement_ref": problem["statement_ref"],
                        "registered_after_run": retrospective},
            "program": program,
            "run": {**run, "window": telemetry.get("window")},
            "sessions": [public(s) for s in sessions],
            "telemetry": summary,
        },
        "metrics": computed["metrics"],
        "gates": computed["gates"],
        "flags": computed["flags"],
        "assessment": assessment,
        "trajectory": trajectory or [],
        "retrospective": retrospective,
        "promotion_authorized": False,
        "limitations": notes,
    }
    return scrub(record, replacements)


def validate(record: dict, spec: dict) -> dict:
    if record.get("schema") != SCHEMA:
        raise BenchError(f"record.schema must be {SCHEMA}")
    if record.get("promotion_authorized") is not False:
        raise BenchError("promotion_authorized must be false")
    statuses = set(spec["metrics"]["statuses"])
    metrics = record.get("metrics") or {}
    if len(metrics) != METRIC_COUNT or not set(metrics) <= set(KNOWN_METRIC_IDS):
        raise BenchError(f"record must carry twelve known metric IDs, found {sorted(metrics)}")
    current = (record.get("spec") or {}).get("hashes", {}).get("metrics.json") == spec["hashes"].get("metrics.json")
    if current and set(metrics) != set(metric_ids(spec)):
        raise BenchError(f"record under the current spec must carry exactly {list(metric_ids(spec))}")
    for metric_id, entry in metrics.items():
        status, score = entry.get("status"), entry.get("score")
        if status not in statuses:
            raise BenchError(f"{metric_id}: status {status!r} not in {sorted(statuses)}")
        if (status == "scored") != (score is not None):
            raise BenchError(f"{metric_id}: score must be present exactly when status is scored")
        if score is not None and not 0 <= score <= 100:
            raise BenchError(f"{metric_id}: score {score} outside [0, 100]")
        judged_anchor = metric_id in ANCHOR_METRICS or (metric_id == "B04" and (entry.get("raw") or {}).get("source") == "judged")
        if score is not None and judged_anchor and score not in ANCHORS:
            raise BenchError(f"{metric_id}: judged score {score} is not an anchor {list(ANCHORS)}")
    gates = record.get("gates") or {}
    if tuple(sorted(gates)) != GATE_IDS or any(g.get("status") not in GATE_STATUSES for g in gates.values()):
        raise BenchError("record gates must be G1..G4 with pass/fail/review/unknown")
    if HOME_RE.search(json.dumps(record)):
        raise BenchError("record contains a local home path; scrub before writing")
    return record


def judge_packet(*, key: str, problem: dict, program: dict, computed: dict, spec: dict, tree: Path,
                 run_dir: Path | None, author_sessions: list[str], deep: bool, out: Path) -> dict:
    defs = metric_defs(spec)
    requests = []
    for metric_id, entry in computed["metrics"].items():
        judged = defs[metric_id].get("judged")
        if not judged or (metric_id == "B12" and not deep):
            continue
        if entry["status"] == "pending" or (entry.get("raw") or {}).get("pending"):
            requests.append({"metric": metric_id, "name": defs[metric_id]["name"], "type": judged["type"],
                             "items": judged.get("items"), "rubric": f".claude/bench/spec/{judged['rubric']}",
                             "computed": entry.get("raw"), "evidence": entry["evidence"][:30]})
    milestones = problem["ladder"]["milestones"]
    return {
        "schema": "yambench.judge-packet/1", "key": key,
        "problem": {k: problem[k] for k in ("id", "title", "statement_ref", "workspace")},
        "tree": str(tree), "run_dir": str(run_dir) if run_dir else None,
        "program": {"path": program["path"], "rounds": program["doc"].get("rounds"),
                    "deliverables": program["doc"].get("deliverables"),
                    "success_criteria": program["doc"].get("success_criteria")},
        "reviews": computed["reviews"], "requests": requests,
        "ladder": [{"milestone": m, "title": milestones[m].get("title", m)} for m in computed["frontier_judgments"]],
        "ladder_rubric": ".claude/bench/spec/rubrics/ladder.md",
        "author_sessions": author_sessions,
        "write_to": str(out),
        "answer_shape": {
            "assessor": {"agent": "bench-assessor", "session": "<your agent or session id>", "model": "<model id>"},
            "metrics": {"B03": {"anchor": 50, "rationale": "...", "evidence": ["repo-relative path"]},
                        "B06": {"items": {"independent_check": [True, False]}, "rationale": "...", "evidence": ["..."]}},
            "ladder": {"<milestone>": {"met": False, "rationale": "...", "evidence": ["..."]}},
        },
    }


def apply_judgments(judgments: dict, packet: dict, spec: dict) -> tuple[dict, dict, dict]:
    assessor = judgments.get("assessor") or {}
    session = assessor.get("session")
    if not session or not assessor.get("model"):
        raise BenchError("judgments.assessor needs session and model")
    if any(session == author or session.startswith(author) or author.startswith(session)
           for author in packet["author_sessions"]):
        raise BenchError("The assessor session is an author session of the benchmarked run")
    requested = {r["metric"]: r for r in packet["requests"]}
    accepted = {}
    for metric_id, answer in (judgments.get("metrics") or {}).items():
        request = requested.get(metric_id)
        if request is None:
            raise BenchError(f"{metric_id} was not requested in the judge packet")
        if not answer.get("rationale") or not answer.get("evidence"):
            raise BenchError(f"{metric_id}: judgments need a rationale and cited evidence")
        if request["type"] == "anchor":
            if answer.get("anchor") not in ANCHORS:
                raise BenchError(f"{metric_id}: anchor must be one of {list(ANCHORS)}")
        else:
            items = answer.get("items") or {}
            unknown = set(items) - set(request["items"])
            if unknown:
                raise BenchError(f"{metric_id}: undeclared judged items {sorted(unknown)}")
            for name, value in items.items():
                values = value if isinstance(value, list) else [value]
                if not values or not all(isinstance(v, bool) for v in values):
                    raise BenchError(f"{metric_id}.{name} must be a boolean or list of booleans")
        accepted[metric_id] = answer
    frontier = {item["milestone"] for item in packet["ladder"]}
    ladder = {}
    for milestone, answer in (judgments.get("ladder") or {}).items():
        if milestone not in frontier:
            raise BenchError(f"Milestone {milestone!r} was not requested")
        if not isinstance(answer.get("met"), bool) or not answer.get("rationale"):
            raise BenchError(f"Milestone {milestone!r} needs met and a rationale")
        ladder[milestone] = answer["met"]
    return accepted, ladder, assessor


def apply_audit(gates: dict, audit: dict | None, author_sessions: list[str]) -> tuple[dict, dict | None, list]:
    if not audit:
        return gates, None, []
    auditor = audit.get("auditor") or {}
    session = auditor.get("session") or ""
    if not session or any(session.startswith(a) or a.startswith(session) for a in author_sessions):
        raise BenchError("The auditor needs a session id distinct from the run's authors")
    updated = {gate: dict(value) for gate, value in gates.items()}
    for gate, ruling in (audit.get("gates") or {}).items():
        if gate not in updated or ruling.get("status") not in GATE_STATUSES or not ruling.get("rationale"):
            raise BenchError(f"Audit ruling for {gate} needs a valid status and rationale")
        if gate == "G4" and updated["G4"]["status"] == "fail":
            continue  # a found canary cannot be overruled
        updated[gate].update(status=ruling["status"], ruling=ruling["rationale"], reviewer="bench-auditor")
    return updated, auditor, audit.get("disputes", [])


def write(record: dict, directory: Path = RECORDS_DIR) -> Path:
    directory.mkdir(parents=True, exist_ok=True)
    path = directory / f"{record['record_id']}.json"
    path.write_text(json.dumps(record, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return path


def load_all(directory: Path = RECORDS_DIR) -> list[dict]:
    return [json.loads(p.read_text(encoding="utf-8")) for p in sorted(directory.glob("*.json"))]
