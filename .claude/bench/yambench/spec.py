"""Load and validate the frozen benchmark specification."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

from . import BenchError

BENCH_ROOT = Path(__file__).resolve().parents[1]
SPEC_DIR = BENCH_ROOT / "spec"
AGENTS_DIR = BENCH_ROOT.parent / "agents"
# Every axis the engine can compute. A spec version selects twelve of them; retired axes keep their
# IDs so records from older specs stay readable, and a new axis never reuses a retired ID.
KNOWN_METRIC_IDS = tuple(f"B{n:02d}" for n in range(1, 15))
METRIC_COUNT = 12
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
GATE_IDS = ("G1", "G2", "G3", "G4")
ANCHORS = (0, 25, 50, 75, 100)
MODES = {"C", "K", "C+J", "K/J"}
JUDGED_TYPES = {"anchor", "items"}
CHECK_KINDS = {"file_exists", "sha256_matches", "json_path", "run_json_equals_sha", "review_verdict",
               "verification_declaration", "md_heading", "judged"}
JSON_OPS = {"eq", "in", "all_eq", "any_eq", "contains_all", "ge", "any_nonempty"}
CANARY_RE = re.compile(r"yambench-canary-[0-9a-f]{16}")
METRIC_FIELDS = ("id", "family", "name", "mode", "question", "formula", "unknown_policy", "gaming_risk")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def read_json(path: Path):
    try:
        return json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise BenchError(f"Cannot read JSON {path}: {error}") from error


def load_spec(spec_dir: Path = SPEC_DIR) -> dict:
    spec_dir = Path(spec_dir)
    files = sorted(p for p in spec_dir.rglob("*") if p.is_file() and p.suffix in {".json", ".md"})
    spec = {
        "dir": spec_dir,
        "metrics": read_json(spec_dir / "metrics.json"),
        "gates": read_json(spec_dir / "gates.json"),
        "problems": read_json(spec_dir / "problems.json"),
        "rubrics": {p.name: p.read_text(encoding="utf-8") for p in sorted((spec_dir / "rubrics").glob("*.md"))},
        "hashes": {p.relative_to(spec_dir).as_posix(): sha256_file(p) for p in files},
    }
    validate_spec(spec)
    return spec


def spec_digest(spec: dict) -> str:
    return sha256_bytes(json.dumps(spec["hashes"], sort_keys=True).encode())


def metric_defs(spec: dict) -> dict:
    return {metric["id"]: metric for metric in spec["metrics"]["metrics"]}


def problem(spec: dict, problem_id: str) -> dict:
    for entry in spec["problems"]["problems"]:
        if entry["id"] == problem_id:
            return entry
    known = ", ".join(p["id"] for p in spec["problems"]["problems"])
    raise BenchError(f"Unknown problem {problem_id!r}; registered: {known}")


def canaries(spec: dict, agents_dir: Path = AGENTS_DIR) -> list[str]:
    texts = list(spec["rubrics"].values())
    if agents_dir.is_dir():
        texts += [p.read_text(encoding="utf-8") for p in sorted(agents_dir.glob("*.md"))]
    return sorted({token for text in texts for token in CANARY_RE.findall(text)})


def validate_bands(metric_id: str, bands: dict):
    for name, steps in bands.items():
        limits = [step[0] for step in steps]
        if not steps or limits != sorted(limits) or any(not 0 <= step[1] <= 100 for step in steps):
            raise BenchError(f"{metric_id}.bands.{name} must be increasing thresholds with scores in [0, 100]")


def validate_check(check: dict, where: str):
    kind = check.get("kind")
    if kind not in CHECK_KINDS:
        raise BenchError(f"{where}: unknown check kind {kind!r}")
    if kind == "json_path" and check.get("op") not in JSON_OPS:
        raise BenchError(f"{where}: unknown json_path op {check.get('op')!r}")
    if kind == "json_path" and not isinstance(check.get("path"), list):
        raise BenchError(f"{where}: json_path needs a list of path segments")


def validate_problem(entry: dict):
    where = f"problem {entry.get('id')!r}"
    for key in ("id", "title", "statement_ref", "workspace"):
        if not isinstance(entry.get(key), str) or not entry[key]:
            raise BenchError(f"{where}: {key} must be a nonempty string")
    if not entry.get("programs"):
        raise BenchError(f"{where}: programs must name at least one program file")
    ladder = entry.get("ladder") or {}
    milestones = ladder.get("milestones") or {}
    branches = ladder.get("branches") or {}
    if not branches:
        raise BenchError(f"{where}: ladder needs at least one branch")
    for name, steps in branches.items():
        for step in steps:
            if step not in milestones:
                raise BenchError(f"{where}: branch {name} references unknown milestone {step!r}")
    for name, milestone in milestones.items():
        checks = milestone.get("all")
        if not checks:
            raise BenchError(f"{where}: milestone {name} has no checks")
        for check in checks:
            validate_check(check, f"{where} milestone {name}")
    for finding in entry.get("findings", []):
        validate_check(finding["check"], f"{where} finding {finding.get('name')!r}")
    for key in ("next_step", "remaining_obligations", "status_record"):
        check = (entry.get("continuity") or {}).get(key)
        if check:
            validate_check(check, f"{where} continuity {key}")


def metric_ids(spec: dict) -> tuple:
    """The current spec's axes in radar order."""
    return tuple(metric["id"] for metric in spec["metrics"]["metrics"])


def validate_relevance(review):
    """The spec must say when its own axes are next questioned; see `bench.py relevance`."""
    if not isinstance(review, dict):
        raise BenchError("metrics.json needs a relevance_review block (reviewed, next_due, decisions)")
    due = review.get("next_due") or {}
    if not DATE_RE.match(str(review.get("reviewed"))) or not DATE_RE.match(str(due.get("date"))):
        raise BenchError("relevance_review.reviewed and next_due.date must be YYYY-MM-DD")
    if isinstance(due.get("records"), bool) or not isinstance(due.get("records"), int) or due["records"] < 1:
        raise BenchError("relevance_review.next_due.records must be a positive integer")
    decisions = review.get("decisions")
    if not isinstance(decisions, dict) or not set(decisions) <= set(KNOWN_METRIC_IDS):
        raise BenchError("relevance_review.decisions must map known metric IDs to one-line reasons")


def validate_spec(spec: dict):
    metrics = spec["metrics"]
    if tuple(metrics.get("anchors", ())) != ANCHORS:
        raise BenchError(f"anchors must be {list(ANCHORS)}")
    ids = tuple(metric.get("id") for metric in metrics.get("metrics", []))
    if len(ids) != METRIC_COUNT or len(set(ids)) != METRIC_COUNT or not set(ids) <= set(KNOWN_METRIC_IDS):
        raise BenchError(f"Exactly twelve distinct metrics from {KNOWN_METRIC_IDS[0]}..{KNOWN_METRIC_IDS[-1]} are required, found {list(ids)}")
    validate_relevance(metrics.get("relevance_review"))
    families = {family["id"] for family in metrics.get("families", [])}
    for metric in metrics["metrics"]:
        for field in METRIC_FIELDS:
            if not isinstance(metric.get(field), str) or not metric[field]:
                raise BenchError(f"{metric.get('id')}.{field} must be a nonempty string")
        if metric["family"] not in families:
            raise BenchError(f"{metric['id']}: unknown family {metric['family']!r}")
        if metric["mode"] not in MODES:
            raise BenchError(f"{metric['id']}: unknown mode {metric['mode']!r}")
        judged = metric.get("judged")
        if ("J" in metric["mode"]) != bool(judged):
            raise BenchError(f"{metric['id']}: judged modes need a judged block and only they may have one")
        if judged:
            if judged.get("type") not in JUDGED_TYPES:
                raise BenchError(f"{metric['id']}: judged.type must be anchor or items")
            rubric = Path(judged.get("rubric", "")).name
            if rubric not in spec["rubrics"] or not CANARY_RE.search(spec["rubrics"][rubric]):
                raise BenchError(f"{metric['id']}: rubric {rubric!r} missing or without canary")
            if judged["type"] == "items" and not judged.get("items"):
                raise BenchError(f"{metric['id']}: judged items must be listed")
        validate_bands(metric["id"], metric.get("bands", {}))
    gate_ids = tuple(gate.get("id") for gate in spec["gates"].get("gates", []))
    if gate_ids != GATE_IDS:
        raise BenchError(f"Gates must be {list(GATE_IDS)}, found {list(gate_ids)}")
    found = [token for text in spec["rubrics"].values() for token in CANARY_RE.findall(text)]
    if len(found) != len(set(found)):
        raise BenchError("Rubric canaries must be unique")
    seen = set()
    for entry in spec["problems"].get("problems", []):
        validate_problem(entry)
        if entry["id"] in seen:
            raise BenchError(f"Duplicate problem id {entry['id']!r}")
        seen.add(entry["id"])
