"""The benchmark axes (a spec selects twelve) and the computed parts of the hard gates."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from dataclasses import dataclass, field
from pathlib import Path

from . import provenance
from .collectors import (Layout, hash_bindings, harness_runs, json_values, load_json, reading_list, reviews,
                         verify_bindings, walk_key, workspace_files)
from .ladder import FAIL, PASS, PENDING, UNKNOWN, CheckContext, evaluate, ladder
from .spec import canaries, metric_defs


@dataclass
class Context:
    spec: dict
    problem: dict
    layout: Layout
    repo: Path
    framework_commit: str
    output_commit: str | None
    program: dict
    telemetry: dict
    session_files: list[str] = field(default_factory=list)
    snapshot: bool = False
    deep: bool = False
    hook: bool = False
    judgments: dict = field(default_factory=dict)
    ladder_judged: dict = field(default_factory=dict)
    cache: dict = field(default_factory=dict)
    runs: list = field(default_factory=list)

    def checks(self, layout: Layout | None = None) -> CheckContext:
        return CheckContext(layout=layout or self.layout, problem=self.problem, registry=self.spec["problems"],
                            snapshot=self.snapshot, distinct_threads=self.telemetry.get("distinct_threads"),
                            judged=self.ladder_judged)


def metric(definition: dict, status: str, score=None, raw=None, coverage=None, evidence=None, notes=None) -> dict:
    found = {"mode": definition["mode"], "status": status,
             "score": round(float(score), 1) if status == "scored" and score is not None else None}
    if raw is not None:
        found["raw"] = raw
    if coverage is not None:
        found["coverage"] = round(coverage, 3)
    found["evidence"] = evidence or []
    if notes:
        found["notes"] = notes
    return found


def band(value, steps) -> int:
    for limit, score in steps:
        if value <= limit:
            return score
    return 0


def itemize(items: dict, weights: dict | None = None) -> tuple[float | None, float, list[str]]:
    """Weighted mean of item values in [0, 1]; None is unknown, 'pending' awaits judgment."""
    weights = weights or {}
    known = {name: value for name, value in items.items() if isinstance(value, (int, float)) and not isinstance(value, bool)}
    total = sum(weights.get(name, 1) for name in items)
    covered = sum(weights.get(name, 1) for name in known)
    pending = [name for name, value in items.items() if value == PENDING]
    if not known:
        return None, 0.0, pending
    score = 100 * sum(value * weights.get(name, 1) for name, value in known.items()) / covered
    return score, covered / total if total else 0.0, pending


def as_item(result: str):
    return {PASS: 1.0, FAIL: 0.0, PENDING: PENDING}.get(result)


def judged_items(ctx: Context, metric_id: str, names: list[str]) -> dict:
    found = (ctx.judgments.get(metric_id) or {}).get("items", {})
    values = {}
    for name in names:
        if ctx.snapshot or name not in found:
            values[name] = PENDING
        else:
            value = found[name]
            values[name] = sum(map(bool, value)) / len(value) if isinstance(value, list) and value else float(bool(value))
    return values


def anchor(ctx: Context, metric_id: str):
    found = ctx.judgments.get(metric_id)
    return None if ctx.snapshot or not found else found.get("anchor")


def run_command(argv: list[str], cwd: Path, timeout: int) -> tuple[bool, str]:
    try:
        proc = subprocess.run(argv, cwd=cwd, capture_output=True, text=True, timeout=timeout)
    except (OSError, subprocess.TimeoutExpired) as error:
        return False, type(error).__name__
    tail = (proc.stdout + proc.stderr).strip().splitlines()[-1:] or [""]
    return proc.returncode == 0, f"exit {proc.returncode}: {tail[0][:160]}"


def cached(ctx: Context, key: str, compute):
    if key not in ctx.cache:
        ctx.cache[key] = compute()
    return ctx.cache[key]


def workspace_documents(ctx: Context) -> list[tuple[str, object]]:
    tree = ctx.layout.tree
    return [(p.relative_to(tree).as_posix(), load_json(p)) for p in workspace_files(tree, ctx.layout.workspace, (".json",))]


# --- progress --------------------------------------------------------------------------------

def b01(d, ctx, state):
    current = state["ladder"]
    best = current["best"]
    branch = current["branches"][best]
    start = 0
    if ctx.layout.base is not None:
        base_layout = Layout(tree=ctx.layout.base, workspace=ctx.layout.workspace, run_dir=None)
        before = ladder(ctx.checks(base_layout))
        start = before["branches"][best]["depth"]
    raw = {"branch": best, "depth_start": start, "depth_end": branch["depth"], "of": branch["of"],
           "provisional": branch["stopped_result"] in (PENDING, UNKNOWN),
           "branches": current["branches"],
           "milestones": {name: m["result"] for name, m in current["milestones"].items()}}
    evidence = [dict(check, milestone=name) for name, m in current["milestones"].items() for check in m["checks"]]
    if not branch["of"]:
        return metric(d, "n/a", raw=raw, evidence=evidence, notes="Every milestone of the best branch is n/a.")
    return metric(d, "scored", 100 * branch["depth"] / branch["of"], raw, 1.0, evidence)


def b02(d, ctx, state):
    targets = ctx.problem.get("formal_targets") or []
    if not targets:
        return metric(d, "n/a", notes="No formal target is registered for this problem.")
    excluded = set((ctx.judgments.get("B02") or {}).get("exclude_targets", []))
    rows = [dict(evaluate({"kind": "verification_declaration", "targets": [t]}, ctx.checks()), target=t) for t in targets]
    met = sum(1 for row in rows if row["result"] == PASS and row["target"] not in excluded)
    return metric(d, "scored", 100 * met / len(targets), {"targets": len(targets), "met": met}, 1.0, rows)


def b03(d, ctx, state):
    inventory = [dict(evaluate(f["check"], ctx.checks()), name=f["name"]) for f in ctx.problem.get("findings", [])]
    for run in ctx.runs:
        for step, result in run["results"].items():
            for claim in (result or {}).get("claims", []):
                if claim.get("status") == "refuted":
                    inventory.append({"kind": "claim", "result": PASS, "name": claim["text"][:160],
                                      "path": f"{ctx.layout.run_label}/{run['name']}/results/{step}.json"})
    for review in state["reviews"]:
        if {"refuted", "refutation"} & set(review["terms"]):
            inventory.append({"kind": "review", "result": PASS, "name": review["verdict"][:160], "path": review["path"]})
    found = [item for item in inventory if item["result"] == PASS]
    if not found:
        if any(item["result"] == UNKNOWN for item in inventory):
            return metric(d, "unknown", evidence=inventory, notes="Inventory incomplete without the run directory.")
        return metric(d, "scored", 0, {"inventory": 0}, 1.0, inventory, "No decisive finding in the inventory.")
    judged = anchor(ctx, "B03")
    raw = {"inventory": len(found)}
    if judged is None:
        return metric(d, "pending", raw=raw, evidence=inventory)
    return metric(d, "scored", judged, raw, 1.0, inventory, ctx.judgments["B03"].get("rationale"))


def program_frozen(ctx: Context) -> dict:
    frozen = ctx.problem.get("program_frozen")
    return evaluate(frozen, ctx.checks()) if frozen else {"kind": "none", "result": UNKNOWN, "detail": "no check"}


def changed_documents(ctx: Context) -> list[str]:
    """Workspace documents the run added or modified, as candidates for the judged discovery axes."""
    if not ctx.output_commit or ctx.output_commit == ctx.framework_commit:
        return []
    return cached(ctx, "changed_documents", lambda: [
        path for path in provenance.changed(ctx.repo, ctx.framework_commit, ctx.output_commit, "AM", ctx.layout.workspace + "/")
        if path.endswith((".md", ".tex", ".lean"))])


def idea_inventory(ctx: Context, probes: str, statuses: set[str]) -> list[dict]:
    inventory = [dict(evaluate(p["check"], ctx.checks()), name=p["name"]) for p in ctx.problem.get(probes, [])]
    for run in ctx.runs:
        for step, result in run["results"].items():
            for claim in (result or {}).get("claims", []):
                if claim.get("status") in statuses:
                    inventory.append({"kind": "claim", "result": PASS, "name": f"[{claim['status']}] {claim['text'][:150]}",
                                      "path": f"{ctx.layout.run_label}/{run['name']}/results/{step}.json"})
    inventory += [{"kind": "document", "result": PASS, "name": path, "path": path} for path in changed_documents(ctx)]
    return inventory


def judged_inventory(d, ctx, metric_id: str, inventory: list[dict], raw: dict, cap: bool = False):
    """Shared shape of the judged discovery axes: empty inventory scores 0, otherwise an anchor judgment."""
    found = [item for item in inventory if item["result"] == PASS]
    raw = {"inventory": len(found), **raw}
    if not found:
        if any(item["result"] == UNKNOWN for item in inventory):
            return metric(d, "unknown", raw=raw, evidence=inventory, notes="Inventory incomplete without the run directory.")
        return metric(d, "scored", 0, raw, 1.0, inventory, "Nothing in the inventory.")
    judged = anchor(ctx, metric_id)
    if judged is None:
        return metric(d, "pending", raw=raw, evidence=inventory[:40])
    return metric(d, "scored", min(judged, 50) if cap else judged, raw, 1.0, inventory[:40],
                  ctx.judgments[metric_id].get("rationale"))


def b13(d, ctx, state):
    inspected = ((state["metrics"].get("B08") or {}).get("raw") or {}).get("items", {}).get("inspected_at_T")
    cap = inspected != 1.0  # novelty cannot be judged against closest work nobody inspected
    inventory = idea_inventory(ctx, "contribution_probes", {"proved", "conjecture", "empirical"})
    return judged_inventory(d, ctx, "B13", inventory, {"closest_work_inspected": inspected, "capped_at_50": cap}, cap)


def b14(d, ctx, state):
    inventory = idea_inventory(ctx, "idea_probes", {"conjecture", "empirical", "refuted"})
    return judged_inventory(d, ctx, "B14", inventory, {})


def b04(d, ctx, state):
    frozen_result = program_frozen(ctx)
    cap = frozen_result["result"] == FAIL  # an unverifiable freeze is unknown, not a failure
    raw = {"program_frozen": frozen_result["result"], "capped_at_50": cap}
    record_template = ctx.problem.get("completion_record")
    if record_template:
        label, path, _ = ctx.layout.expand(record_template)
        record = load_json(path) or {}
        outcomes = [c.get("outcome") for c in record.get("success_criteria", [])]
        if outcomes:
            score = 100 * outcomes.count("met") / len(outcomes)
            raw.update(source="completion record", met=outcomes.count("met"), of=len(outcomes))
            return metric(d, "scored", min(score, 50) if cap else score, raw, 1.0, [frozen_result, {"path": label}])
    judged = anchor(ctx, "B04")
    if judged is None:
        return metric(d, "pending", raw=raw, evidence=[frozen_result])
    raw["source"] = "judged"
    return metric(d, "scored", min(judged, 50) if cap else judged, raw, 1.0, [frozen_result],
                  ctx.judgments["B04"].get("rationale"))


# --- rigor -----------------------------------------------------------------------------------

def b05(d, ctx, state):
    flags = []
    for group in ctx.problem.get("consistency", []):
        values = {}
        for ref in group["values"]:
            label, path, _ = ctx.layout.expand(ref["file"])
            found = json_values(load_json(path), ref["path"])
            if found:
                values[label] = found[0]
        if len({json.dumps(v, sort_keys=True) for v in values.values()}) > 1:
            flags.append({"id": "label_disagreement", "detail": f"{group['name']}: {values}"})
    if any(value is True for _, doc in workspace_documents(ctx) for value in walk_key(doc, "research_validated")):
        flags.append({"id": "research_validated_true", "detail": "A workspace record claims research validation."})
    claims = [c for run in ctx.runs for r in run["results"].values() for c in (r or {}).get("claims", [])]
    labels = {}
    for claim in claims:
        labels[claim.get("status")] = labels.get(claim.get("status"), 0) + 1
    if labels.get("proved"):
        flags.append({"id": "proved_claims", "detail": f"{labels['proved']} stage claim(s) labeled proved need certificate or review."})
    mismatched = [b for b in state["bindings"] if b["result"] == "mismatch"]
    if mismatched:
        flags.append({"id": "hash_mismatch", "detail": ", ".join(sorted({b["path"] for b in mismatched})[:5])})
    team = ctx.problem.get("team_record")
    if team and ctx.telemetry.get("child_names"):
        label, path, _ = ctx.layout.expand(team["file"])
        declared = json.dumps(json_values(load_json(path), team["path"]))
        hidden = [n for n in ctx.telemetry["child_names"] if n.rsplit("/", 1)[-1] not in declared]
        if hidden:
            flags.append({"id": "undisclosed_agent", "detail": f"{', '.join(hidden)} not in {label}"})
    raw = {"flags": flags, "stage_claim_labels": labels,
           "stage_claims_without_source": sum(1 for c in claims if not c.get("source"))}
    state["flags"].extend(flags)
    judged = anchor(ctx, "B05")
    if judged is None:
        return metric(d, "pending", raw=raw)
    return metric(d, "scored", judged, raw, 1.0, notes=ctx.judgments["B05"].get("rationale"))


def b06(d, ctx, state):
    found = state["reviews"]
    rounds = ctx.program["doc"].get("rounds", 1)
    items = {
        "review_per_round": float(len(found) >= rounds),
        "verdict_recorded": float(bool(found) and all(r["verdict"] for r in found)),
        "sha_bound": float(bool(found) and all(r["sha256_mentions"] for r in found)),
        "distinct_role": None, "distinct_thread": None,
    }
    plans = [run["plan"] for run in ctx.runs if run.get("plan")]
    if plans:
        steps = {s["id"]: s for s in plans[0]["steps"]}
        challenges = [s for s in steps.values() if "challenge" in s["stage_id"] or "critique" in s["stage_id"]]
        if challenges:
            items["distinct_role"] = float(all(steps[dep]["agent_id"] != s["agent_id"]
                                               for s in challenges for dep in s["depends_on"] if dep in steps))
    if ctx.telemetry.get("distinct_threads") is not None:
        items["distinct_thread"] = float(ctx.telemetry["distinct_threads"])
    names = d["judged"]["items"]
    items.update(judged_items(ctx, "B06", names))
    score, coverage, pending = itemize(items)
    if score is None:
        return metric(d, "unknown", raw={"items": items})
    evidence = [{"path": r["path"], "detail": r["verdict"] or "no verdict line"} for r in found]
    return metric(d, "scored", score, {"items": items, "pending": pending, "reviews": len(found), "rounds": rounds},
                  coverage, evidence)


def b07(d, ctx, state):
    tree, layout = ctx.layout.tree, ctx.layout
    bindings = state["bindings"]
    passed = sum(1 for b in bindings if b["result"] == "pass")
    mismatched = sum(1 for b in bindings if b["result"] == "mismatch")
    docs = [doc for _, doc in workspace_documents(ctx)]
    stable = [v for doc in docs for v in walk_key(doc, "source_stable")]
    exits = [c.get("exit_code") for doc in docs for checks in walk_key(doc, "checks") if isinstance(checks, list)
             for c in checks if isinstance(c, dict) and "exit_code" in c]
    items = {
        "hashes_verify": passed / (passed + mismatched) if passed + mismatched else None,
        "source_stable": float(all(v is True for v in stable)) if stable else None,
        "recorded_checks_exit_0": float(all(code == 0 for code in exits)) if exits else None,
        "repository_checker": None, "run_complete": None, "preregistration": None,
        "unit_tests": None, "reproduction": None,
    }
    evidence = []
    if not ctx.hook and (tree / "scripts" / "check_repository.py").is_file():
        ok, detail = cached(ctx, f"checker:{ctx.output_commit}", lambda: run_command(
            [sys.executable, "scripts/check_repository.py"], tree, 120))
        items["repository_checker"] = float(ok)
        evidence.append({"check": "scripts/check_repository.py", "result": PASS if ok else FAIL, "detail": detail})
    if layout.run_dir is not None:
        executed = [r for r in ctx.runs if r["receipt"].get("status") == "completed_execution"]
        complete = any(r["plan"] and r["program"] and set(s["id"] for s in r["plan"]["steps"]) <= set(r["results"])
                       for r in executed)
        items["run_complete"] = float(complete) if layout.run_dir.is_dir() else None
    prereg = ctx.problem.get("preregistration")
    if prereg and ctx.output_commit:
        items["preregistration"], detail = preregistered(ctx, prereg)
        evidence.append({"check": "preregistration", "detail": detail})
    if ctx.deep and not ctx.hook:
        ok, detail = cached(ctx, f"tests:{ctx.output_commit}", lambda: run_command(
            [sys.executable, "-m", "unittest", "discover", "-s", "tests"], tree, 900))
        items["unit_tests"] = float(ok)
        evidence.append({"check": "unit tests", "result": PASS if ok else FAIL, "detail": detail})
        repro = [cached(ctx, f"repro:{ctx.output_commit}:{r['name']}", lambda r=r: reproduce(r, ctx))
                 for r in ctx.problem.get("repro", [])]
        if repro:
            settled = [r for r in repro if r["result"] in (PASS, FAIL)]  # unknown is not a failure
            items["reproduction"] = sum(1 for r in settled if r["result"] == PASS) / len(settled) if settled else None
            evidence += repro
    score, coverage, _ = itemize(items)
    evidence += [b for b in bindings if b["result"] != "pass"][:20]
    raw = {"items": items, "bindings": {"pass": passed, "mismatch": mismatched,
                                        "unknown": sum(1 for b in bindings if b["result"] == "unknown")}}
    if score is None:
        return metric(d, "unknown", raw=raw, evidence=evidence)
    return metric(d, "scored", score, raw, coverage, evidence)


def preregistered(ctx: Context, prereg: dict):
    protocol, _, _ = ctx.layout.expand(prereg["protocol"])
    results, _, _ = ctx.layout.expand(prereg["results"])
    first = provenance.adding_commit(ctx.repo, ctx.output_commit, protocol)
    second = provenance.adding_commit(ctx.repo, ctx.output_commit, results)
    if not first or not second:
        return None, "protocol or results not committed"
    if first == second:
        return None, f"protocol and results added in the same commit {first[:10]}; order unverifiable"
    good = provenance.is_ancestor(ctx.repo, first, second)
    return float(good), f"protocol {first[:10]} {'precedes' if good else 'does not precede'} results {second[:10]}"


def reproduce(spec: dict, ctx: Context) -> dict:
    with tempfile.TemporaryDirectory() as tmp:
        argv = [a.replace("{tmp}", tmp) for a in spec["argv"]]
        argv = [sys.executable if a == "python3" else a for a in argv]
        ok, detail = run_command(argv, ctx.layout.tree, spec.get("timeout_seconds", 300))
        if not ok:
            return {"check": spec["name"], "result": FAIL, "detail": detail}
        produced = load_json(Path(argv[argv.index("--output") + 1])) if "--output" in argv else None
        label, against_path, _ = ctx.layout.expand(spec["against"])
        expected = load_json(against_path)
        if produced is None or expected is None:
            return {"check": spec["name"], "result": UNKNOWN, "detail": "comparison file unavailable"}
        same = all(json_values(produced, p) == json_values(expected, p) for p in spec["paths"])
        return {"check": spec["name"], "result": PASS if same else FAIL,
                "detail": f"{'matches' if same else 'differs from'} {label}"}


def b08(d, ctx, state):
    works = ctx.problem.get("closest_work", [])
    rows = reading_list(ctx.layout.tree)
    texts = "\n".join(p.read_text(encoding="utf-8", errors="replace")
                      for p in workspace_files(ctx.layout.tree, ctx.layout.workspace, (".md",)))
    inspected = [w["key"] for w in works if any(w["match"] in r["text"] and r["level"] in ("T", "P") for r in rows)]
    cited = [w["key"] for w in works if w["match"] in texts]
    label_check = ctx.problem.get("novelty_label")
    label = evaluate({"kind": "json_path", "op": "any_nonempty", **label_check}, ctx.checks()) if label_check else None
    items = {"inspected_at_T": len(inspected) / len(works) if works else None,
             "cited_in_workspace": len(cited) / len(works) if works else None,
             "novelty_label_present": as_item(label["result"]) if label else None}
    items.update(judged_items(ctx, "B08", d["judged"]["items"]))
    score, coverage, pending = itemize(items)
    missing = [w["key"] for w in works if w["key"] not in inspected]
    raw = {"items": items, "pending": pending, "not_in_reading_list_at_T": missing}
    if score is None:
        return metric(d, "unknown", raw=raw)
    return metric(d, "scored", score, raw, coverage, [label] if label else [])


# --- operations -------------------------------------------------------------------------------

def b09(d, ctx, state):
    depth = state["metrics"]["B01"]["raw"]
    finding = state["metrics"]["B03"]
    progressed = depth["depth_end"] > depth["depth_start"] or (finding["status"] == "scored" and finding["score"] >= 50)
    if not progressed and finding["status"] == "scored":
        return metric(d, "n/a", notes="No new ladder depth and no decisive finding: cost is not credited.")
    tokens = ctx.telemetry.get("effective_tokens")
    reference = (ctx.problem.get("reference_budget") or {}).get("effective_tokens")
    raw = {"effective_tokens": tokens, "reference_effective_tokens": reference,
           "tokens": ctx.telemetry.get("tokens"), "overhead_tokens": ctx.telemetry.get("overhead_tokens"),
           "progress_known": progressed or finding["status"] == "scored"}
    if tokens is None:
        return metric(d, "unknown", raw=raw, notes="No measured token telemetry.")
    if reference is None:
        return metric(d, "unknown", raw=raw, notes="No reference budget registered for this problem.")
    return metric(d, "scored", 100 * min(1.0, reference / tokens) if tokens else 100, raw, 1.0)


def b10(d, ctx, state):
    t = ctx.telemetry
    bands = d["bands"]
    parts = {
        "orientation_tool_calls": t.get("orientation_tool_calls"),
        "peak_context_fraction": t.get("ctx_peak_fraction"),
        "compactions": t.get("compactions"),
        "redundant_read_ratio": t.get("redundant_read_ratio"),
    }
    items = {name: (band(value, bands[name]) / 100 if value is not None else None) for name, value in parts.items()}
    score, coverage, _ = itemize(items)
    if score is None:
        return metric(d, "unknown", raw={"measures": parts}, notes="No session telemetry.")
    return metric(d, "scored", score, {"measures": parts, "items": items}, coverage)


def b11(d, ctx, state):
    plans = [run["plan"] for run in ctx.runs if run.get("plan")]
    planned = {s["id"] for s in plans[0]["steps"]} if plans else set()
    harness = {step for run in ctx.runs if run["receipt"].get("backend") == "command"
               for step, value in (run["receipt"].get("states") or {}).items() if value == "completed"}
    agent = {step for run in ctx.runs for step in run["results"]}
    failed = {step for run in ctx.runs for step, value in (run["receipt"].get("states") or {}).items()
              if value in ("failed", "blocked")}
    post_hoc = sum(1 for run in ctx.runs for r in run["results"].values()
                   if "post-hoc" in json.dumps(r).lower() or "after the fact" in json.dumps(r).lower())
    turns = ctx.telemetry.get("human_turns")
    steering = (turns or {}).get("steering", 0) + (turns or {}).get("correction", 0) if turns is not None else None
    items = {
        "harness_executed": len(harness & planned) / len(planned) if planned else None,
        "agent_executed": len(agent & planned) / len(planned) if planned else None,
        "failure_free": 1 - len(failed & planned) / len(planned) if planned else None,
        "human_steering": band(steering, d["bands"]["steering_turns"]) / 100 if steering is not None else None,
    }
    score, coverage, _ = itemize(items, d.get("weights"))
    raw = {"items": items, "planned_steps": len(planned), "post_hoc_summaries": post_hoc,
           "human_turns": turns, "classification": "heuristic"}
    if score is None:
        return metric(d, "unknown", raw=raw)
    return metric(d, "scored", score, raw, coverage)


def b12(d, ctx, state):
    continuity = ctx.problem.get("continuity") or {}
    items, evidence = {}, []
    for key in ("next_step", "remaining_obligations", "status_record"):
        if continuity.get(key):
            found = evaluate(continuity[key], ctx.checks())
            items[key] = as_item(found["result"])
            evidence.append(dict(found, item=key))
    deleted = status_touched = None
    if ctx.output_commit and ctx.output_commit != ctx.framework_commit:
        deleted = provenance.changed(ctx.repo, ctx.framework_commit, ctx.output_commit, "D", "research/")
        page = ctx.layout.expand(continuity["status_page"])[0] if continuity.get("status_page") else None
        status_touched = bool(page and provenance.changed(ctx.repo, ctx.framework_commit, ctx.output_commit, "AM", page))
    items["evidence_preserved"] = float(not deleted) if deleted is not None else None
    items["status_page_updated"] = float(status_touched) if status_touched is not None else None
    if deleted:
        evidence.append({"item": "evidence_preserved", "result": FAIL, "detail": ", ".join(deleted[:5])})
    if ctx.deep:
        items.update(judged_items(ctx, "B12", d["judged"]["items"]))
    else:
        items["cold_start"] = None
    score, coverage, pending = itemize(items)
    if score is None:
        return metric(d, "unknown", raw={"items": items})
    return metric(d, "scored", score, {"items": items, "pending": pending}, coverage, evidence)


# Retired axes (B04, B10) stay computable so records of older specs can still be reproduced.
COMPUTE = {"B01": b01, "B02": b02, "B03": b03, "B04": b04, "B05": b05, "B06": b06, "B07": b07,
           "B08": b08, "B09": b09, "B10": b10, "B11": b11, "B12": b12, "B13": b13, "B14": b14}


# --- gates -------------------------------------------------------------------------------------

def gate_g3(ctx: Context) -> dict:
    constraints = ctx.program["doc"].get("constraints", {})
    notes, status = [], PASS
    attempted = [r["receipt"].get("attempted_cost_units") for r in ctx.runs
                 if isinstance(r["receipt"].get("attempted_cost_units"), (int, float))]
    if attempted and max(attempted) > constraints.get("max_cost_units", float("inf")):
        status = "review"
        notes.append(f"attempted {max(attempted)} > max_cost_units {constraints['max_cost_units']}")
    working = ctx.telemetry.get("working")
    if working and working > constraints.get("max_agents", float("inf")):
        status = "review"
        notes.append(f"telemetry shows {working} working threads > max_agents {constraints['max_agents']}"
                     f" ({', '.join(ctx.telemetry.get('child_names', []))} besides the lead)")
    if not attempted and not working:
        notes.append("no receipts or telemetry to compare with the program constraints")
        return {"status": UNKNOWN, "computed": True, "notes": notes, "evidence_missing": True}
    return {"status": status, "computed": True, "notes": notes}


def gate_g4(ctx: Context) -> dict:
    tokens = canaries(ctx.spec)
    tree = ctx.layout.tree
    targets = [tree / name for name in ("AGENTS.md", "CLAUDE.md", "explore/AGENTS.md")]
    targets += sorted((tree / "programs").glob("*.json")) + workspace_files(tree, ctx.layout.workspace)
    targets += [packet for run in ctx.runs for packet in run["packets"]]
    if not ctx.hook:
        targets += [Path(f) for f in ctx.session_files]
    hits, scanned = [], 0
    for path in targets:
        if not path.is_file():
            continue
        scanned += 1
        text = path.read_text(encoding="utf-8", errors="replace")
        hits += [path.name for token in tokens if token in text]
    return {"status": FAIL if hits else PASS, "computed": True, "scanned": scanned,
            "notes": [f"canary found in {name}" for name in sorted(set(hits))]}


def compute(ctx: Context) -> dict:
    defs = metric_defs(ctx.spec)
    ctx.runs = harness_runs(ctx.layout.run_dir)
    documents = workspace_documents(ctx)
    bindings = [b for origin, doc in documents if doc is not None for b in hash_bindings(doc, origin)]
    state = {
        "ladder": ladder(ctx.checks()),
        "reviews": reviews(ctx.layout.tree, ctx.problem.get("review_glob", "{ws}/review*.md").replace("{ws}", ctx.layout.workspace)),
        "bindings": verify_bindings(bindings, ctx.layout),
        "flags": [], "metrics": {},
    }
    # ID order computes every axis after the ones it reads (B09 reads B01 and B03, B13 reads B08).
    for metric_id in sorted(defs):
        state["metrics"][metric_id] = {"id": metric_id, "name": defs[metric_id]["name"],
                                       "family": defs[metric_id]["family"], **COMPUTE[metric_id](defs[metric_id], ctx, state)}
    gates = {
        "G1": {"status": UNKNOWN, "computed": False,
               "notes": [f["detail"] for f in state["flags"] if f["id"] == "hash_mismatch"]},
        "G2": {"status": UNKNOWN, "computed": False, "notes": []},
        "G3": gate_g3(ctx),
        "G4": gate_g4(ctx),
    }
    return {"metrics": state["metrics"], "gates": gates, "flags": state["flags"],
            "frontier_judgments": state["ladder"]["frontier_judgments"],
            "reviews": state["reviews"], "program_frozen": program_frozen(ctx)["result"]}
