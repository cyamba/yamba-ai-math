"""Evaluate declarative evidence checks and a problem's milestone ladder."""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

from .collectors import Layout, load_json, json_values, md_heading, reviews
from .spec import sha256_file

PASS, FAIL, UNKNOWN, PENDING, NA = "pass", "fail", "unknown", "pending", "n/a"
EMPTY = (None, "", [], {}, False)


@dataclass
class CheckContext:
    layout: Layout
    problem: dict
    registry: dict
    snapshot: bool = False
    distinct_threads: bool | None = None
    judged: dict = field(default_factory=dict)
    milestone: str | None = None


def outcome(check: dict, result: str, detail: str, path: str | None = None) -> dict:
    found = {"kind": check["kind"], "result": result, "detail": detail}
    if path:
        found["path"] = path
    return found


def missing(check: dict, label: str, is_run: bool) -> dict:
    return outcome(check, UNKNOWN if is_run else FAIL, "run file unavailable" if is_run else "file absent", label)


def compare_values(op: str, values: list, expected) -> bool:
    if op == "eq" or op == "all_eq":
        return all(value == expected for value in values)
    if op == "any_eq":
        return any(value == expected for value in values)
    if op == "in":
        return all(value in expected for value in values)
    if op == "contains_all":
        return set(expected) <= {value for value in values if isinstance(value, (str, int, float, bool))}
    if op == "ge":
        return all(isinstance(value, (int, float)) and not isinstance(value, bool) and value >= expected for value in values)
    if op == "any_nonempty":
        return any(value not in EMPTY for value in values)
    raise ValueError(op)


def verification_status(target: str, ctx: CheckContext) -> tuple[bool, str]:
    allowed = set(ctx.registry.get("allowed_axioms", []))
    for rel in ctx.registry.get("verification_files", []):
        record = load_json(ctx.layout.tree / rel)
        if not isinstance(record, dict) or record.get("status") != "passed":
            continue
        axioms = (record.get("axioms") or {}).get(target)
        if axioms is None:
            continue
        if not set(axioms) <= allowed:
            return False, f"{target} depends on disallowed axioms in {rel}"
        stale = [name for name, digest in (record.get("sha256") or {}).items()
                 if not any(p.is_file() and sha256_file(p) == digest
                            for p in ctx.layout.recorded(name, str(Path(rel).parent)))]
        if stale:
            return False, f"{rel} source hashes are stale: {', '.join(stale[:3])}"
        return True, f"{target} checked in {rel}"
    return False, f"{target} is not in a passed verification record"


def evaluate(check: dict, ctx: CheckContext) -> dict:
    kind = check["kind"]
    layout = ctx.layout
    if kind == "judged":
        if ctx.snapshot or ctx.milestone not in ctx.judged:
            return outcome(check, PENDING, "awaiting independent judgment")
        verdict = ctx.judged[ctx.milestone]
        return outcome(check, PASS if verdict else FAIL, "judged met" if verdict else "judged not met")
    if kind == "file_exists":
        label, path, is_run = layout.expand(check["path"])
        return outcome(check, PASS, "present", label) if path and path.is_file() else missing(check, label, is_run)
    if kind == "sha256_matches":
        label, path, is_run = layout.expand(check["path"])
        rec_label, rec_path, rec_run = layout.expand(check["recorded"]["file"])
        if not (path and path.is_file()):
            return missing(check, label, is_run)
        recorded = json_values(load_json(rec_path), check["recorded"]["path"])
        if not recorded:
            return missing(check, rec_label, rec_run) if not (rec_path and rec_path.is_file()) else \
                outcome(check, FAIL, "recorded hash absent", rec_label)
        good = sha256_file(path) == recorded[0]
        return outcome(check, PASS if good else FAIL, "hash matches record" if good else "hash differs from record", label)
    if kind == "json_path":
        label, path, is_run = layout.expand(check["file"])
        document = load_json(path)
        if document is None:
            return missing(check, label, is_run)
        values = json_values(document, check["path"])
        if not values:
            return outcome(check, FAIL, f"path {'/'.join(map(str, check['path']))} absent", label)
        good = compare_values(check["op"], values, check.get("value"))
        return outcome(check, PASS if good else FAIL, f"{check['op']} {'holds' if good else 'fails'} over {len(values)} value(s)", label)
    if kind == "run_json_equals_sha":
        label, path, is_run = layout.expand(check["file"])
        of_label, of_path, _ = layout.expand(check["of"])
        recorded = json_values(load_json(path), check["path"])
        if not recorded:
            return missing(check, label, is_run)
        if not (of_path and of_path.is_file()):
            return outcome(check, FAIL, "hashed file absent", of_label)
        good = sha256_file(of_path) == recorded[0]
        return outcome(check, PASS if good else FAIL, "recorded at run time" if good else "changed since the run recorded it", of_label)
    if kind == "md_heading":
        label, path, is_run = layout.expand(check["file"])
        found = md_heading(path, check["regex"])
        if found is None:
            return missing(check, label, is_run)
        return outcome(check, PASS if found else FAIL, "heading present" if found else "heading absent", label)
    if kind == "review_verdict":
        pattern = check["glob"].replace("{ws}", layout.workspace)
        matched = [r for r in reviews(layout.tree, pattern)
                   if r["verdict"] and re.search(check["regex"], r["verdict"], re.I)]
        if not matched:
            return outcome(check, FAIL, "no review verdict matches", pattern)
        if check.get("distinct_thread"):
            if ctx.distinct_threads is None:
                return outcome(check, UNKNOWN, "reviewer thread unknown without telemetry", matched[0]["path"])
            if not ctx.distinct_threads:
                return outcome(check, FAIL, "review not written in a distinct thread", matched[0]["path"])
        return outcome(check, PASS, matched[0]["verdict"][:160], matched[0]["path"])
    if kind == "verification_declaration":
        targets = check.get("targets") or ctx.problem.get("formal_targets") or []
        if not targets:  # a rung nobody registered must not cap the ladder below 100
            return outcome(check, NA, "no formal target registered")
        statuses = [verification_status(target, ctx) for target in targets]
        good = all(ok for ok, _ in statuses)
        return outcome(check, PASS if good else FAIL, "; ".join(detail for _, detail in statuses))
    raise ValueError(kind)


def combine(results: list[str]) -> str:
    for state in (FAIL, PENDING, UNKNOWN):
        if state in results:
            return state
    return NA if results and all(result == NA for result in results) else PASS


def milestone(name: str, ctx: CheckContext) -> dict:
    spec = ctx.problem["ladder"]["milestones"][name]
    ctx.milestone = name
    computed = [evaluate(check, ctx) for check in spec["all"] if check["kind"] != "judged"]
    judged = [check for check in spec["all"] if check["kind"] == "judged"]
    settled = all(c["result"] in (PASS, NA) for c in computed)
    if judged and settled:  # a judgment cannot rescue a failed or unknown computed check
        computed += [evaluate(check, ctx) for check in judged]
    result = combine([c["result"] for c in computed])
    return {"id": name, "title": spec.get("title", name), "result": result, "checks": computed,
            "needs_judgment": bool(judged) and settled and result == PENDING}


def ladder(ctx: CheckContext) -> dict:
    spec = ctx.problem["ladder"]
    states = {name: milestone(name, ctx) for name in spec["milestones"]}
    branches = {}
    for name, all_steps in spec["branches"].items():
        steps = [step for step in all_steps if states[step]["result"] != NA]
        depth = 0
        for step in steps:
            if states[step]["result"] != PASS:
                break
            depth += 1
        stop = steps[depth] if depth < len(steps) else None
        branches[name] = {"depth": depth, "of": len(steps), "stopped_at": stop,
                          "stopped_result": states[stop]["result"] if stop else None,
                          "not_applicable": [step for step in all_steps if step not in steps]}
    best = max(branches, key=lambda b: (branches[b]["depth"] / max(branches[b]["of"], 1), b == "prove"))
    frontier = [b["stopped_at"] for b in branches.values()
                if b["stopped_at"] and states[b["stopped_at"]]["needs_judgment"]]
    return {"best": best, "branches": branches, "milestones": states, "frontier_judgments": sorted(set(frontier))}
