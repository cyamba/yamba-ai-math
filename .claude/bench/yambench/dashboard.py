"""Shape records into dashboard datasets; render them offline or export them for the published dashboard."""

from __future__ import annotations

import json

from .spec import BENCH_ROOT

PAGE = BENCH_ROOT / "dashboard" / "page.html"
TEMPLATE = BENCH_ROOT / "dashboard" / "index.html"
DATA_PLACEHOLDER = "/*YAMBENCH_DATA*/null"
PAGE_PLACEHOLDER = "<!--YAMBENCH_PAGE-->"
DATASETS = {
    "records": ("Benchmarked versions", "One row per benchmark record: framework and output commits, problem, program, client, model, effort, tokens and assessment. Exported from .claude/bench/records."),
    "scores": ("Benchmark axis scores", "Twelve rows per record: each axis's status, 0-100 score, coverage and a short detail. Exported from .claude/bench/records."),
    "gates": ("Hard gate outcomes", "Four rows per record: no fabrication, scope, budget and stop conditions, benchmark leakage. Exported from .claude/bench/records."),
    "notes": ("Flags and limitations", "Computed flags, auditor disputes, unanswered judgments and stated limitations per record. Exported from .claude/bench/records."),
    "metrics": ("Benchmark definitions", "The twelve benchmark definitions of the current spec. Exported from .claude/bench/spec/metrics.json."),
    "trajectory": ("Intermediate snapshots", "Axis scores at each intermediate snapshot embedded in a final record. Exported from .claude/bench/records."),
}


def short(sha):
    return sha[:7] if isinstance(sha, str) else None


def joined(values):
    return ", ".join(values) if values else None


def metric_detail(metric_id: str, entry: dict) -> str | None:
    raw = entry.get("raw") or {}
    parts = []
    if metric_id == "B01" and "depth_end" in raw:
        parts.append(f"{raw['branch']} branch: depth {raw['depth_start']} to {raw['depth_end']} of {raw['of']}")
    if raw.get("bindings"):
        b = raw["bindings"]
        parts.append(f"{b['pass']} recorded hashes verified, {b['mismatch']} mismatched, {b['unknown']} unavailable")
    if raw.get("not_in_reading_list_at_T"):
        parts.append("not in the reading list at T or higher: " + ", ".join(raw["not_in_reading_list_at_T"]))
    if metric_id == "B09" and raw.get("effective_tokens") is not None:
        parts.append(f"{raw['effective_tokens']:,} effective tokens")
    if metric_id == "B10" and raw.get("measures"):
        parts.append(", ".join(f"{k.replace('_', ' ')} {v}" for k, v in raw["measures"].items() if v is not None))
    if metric_id == "B11" and raw.get("items"):
        parts.append(f"{raw.get('post_hoc_summaries', 0)} post-hoc stage summaries; human turns {raw.get('human_turns')}")
    if raw.get("pending"):
        parts.append("awaiting judgment: " + ", ".join(raw["pending"]))
    if raw.get("flags"):
        parts.append("flags: " + ", ".join(f["id"] for f in raw["flags"]))
    if entry.get("notes"):
        parts.append(entry["notes"])
    return "; ".join(parts)[:400] or None


def record_row(record: dict) -> dict:
    p = record.get("provenance") or {}
    fw, out, prob = p.get("framework") or {}, p.get("output") or {}, p.get("problem") or {}
    prog, tel = p.get("program") or {}, p.get("telemetry") or {}
    tokens, turns = tel.get("tokens") or {}, tel.get("human_turns")
    assessment = record.get("assessment") or {}
    return {
        "record_id": record.get("record_id"), "kind": record.get("kind"), "step": record.get("step"),
        "created_at": record.get("created_at"),
        "problem_id": prob.get("id"), "problem_title": prob.get("title"),
        "framework_commit": fw.get("commit"), "framework_short": short(fw.get("commit")),
        "framework_branch": fw.get("branch"), "framework_subject": fw.get("subject"),
        "framework_committed_at": fw.get("committed_at"),
        "framework_fingerprint": short((fw.get("fingerprint") or {}).get("sha256")),
        "output_commit": out.get("commit"), "output_short": short(out.get("commit")), "output_branch": out.get("branch"),
        "program_id": prog.get("id"), "program_sha256": short(prog.get("sha256")), "program_frozen": prog.get("frozen_at_start"),
        "clients": joined(tel.get("clients")), "models": joined(tel.get("models")), "efforts": joined(tel.get("efforts")),
        "working_threads": tel.get("working"), "overhead_threads": tel.get("overhead"),
        "effective_tokens": tel.get("effective_tokens"), "uncached_input": tokens.get("uncached_input"),
        "cache_read": tokens.get("cache_read"), "output_tokens": tokens.get("output"),
        "reasoning_tokens": tokens.get("reasoning"), "compactions": tel.get("compactions"),
        "ctx_peak_fraction": tel.get("ctx_peak_fraction"),
        "steering_turns": (turns.get("steering", 0) + turns.get("correction", 0)) if turns is not None else None,
        "retrospective": record.get("retrospective"),
        "spec_version": record.get("spec_version") or (record.get("spec") or {}).get("version"),
        "engine_version": (record.get("engine") or {}).get("version"),
        "assessor_model": (assessment.get("assessor") or {}).get("model"),
        "auditor_model": (assessment.get("auditor") or {}).get("model"),
        "same_model_family": assessment.get("same_model_family"),
    }


def datasets(records: list[dict], spec: dict) -> dict:
    defs = {m["id"]: m for m in spec["metrics"]["metrics"]}
    families = {f["id"]: f["name"] for f in spec["metrics"]["families"]}
    gates = {g["id"]: g["name"] for g in spec["gates"]["gates"]}
    rows = {name: [] for name in DATASETS}
    for record in records:
        rid = record.get("record_id")
        rows["records"].append(record_row(record))
        for metric_id, entry in sorted((record.get("metrics") or {}).items()):
            definition = defs.get(metric_id, {})
            rows["scores"].append({
                "record_id": rid, "metric_id": metric_id, "metric_name": definition.get("name", entry.get("name")),
                "family": families.get(definition.get("family"), definition.get("family")),
                "status": entry.get("status"), "score": entry.get("score"), "coverage": entry.get("coverage"),
                "mode": entry.get("mode"), "detail": metric_detail(metric_id, entry)})
        for gate_id, gate in sorted((record.get("gates") or {}).items()):
            notes = list(gate.get("notes") or [])
            if gate.get("ruling"):
                notes.append(f"Auditor: {gate['ruling']}")
            rows["gates"].append({"record_id": rid, "gate_id": gate_id, "gate_name": gates.get(gate_id, gate_id),
                                  "status": gate.get("status"), "notes": " ".join(notes) or None})
        assessment = record.get("assessment") or {}
        notes = [("Flag", f"{f['id'].replace('_', ' ')}: {f['detail']}") for f in record.get("flags") or []]
        notes += [("Dispute", f"{d.get('metric')}: {d.get('detail')}") for d in assessment.get("disagreements") or []]
        notes += [("Unanswered", f"{m} was not judged and stays pending") for m in assessment.get("unanswered") or []]
        notes += [("Limitation", text) for text in record.get("limitations") or []]
        rows["notes"] += [{"record_id": rid, "note_id": f"{rid}#{i}", "kind": kind, "text": text}
                          for i, (kind, text) in enumerate(notes)]
        for index, point in enumerate(record.get("trajectory") or []):
            for metric_id, score in sorted((point.get("scores") or {}).items()):
                rows["trajectory"].append({"record_id": rid, "step_index": index, "step": point.get("step"),
                                           "created_at": point.get("created_at"), "metric_id": metric_id,
                                           "score": score, "status": (point.get("statuses") or {}).get(metric_id)})
    rows["metrics"] = [{"metric_id": m["id"], "name": m["name"], "family": families[m["family"]], "mode": m["mode"],
                        "question": m["question"], "formula": m["formula"], "unknown_policy": m["unknown_policy"]}
                       for m in spec["metrics"]["metrics"]]
    return rows


def render(records: list[dict], spec: dict, template=TEMPLATE, page=PAGE) -> str:
    """A self-contained offline copy: the published page plus a small stand-in for the dashboard runtime."""
    data = json.dumps(datasets(records, spec), ensure_ascii=False).replace("</", "<\\/")
    shell = template.read_text(encoding="utf-8")
    if DATA_PLACEHOLDER not in shell or PAGE_PLACEHOLDER not in shell:
        raise ValueError("Dashboard template lacks its data or page placeholder")
    return shell.replace(PAGE_PLACEHOLDER, page.read_text(encoding="utf-8")).replace(DATA_PLACEHOLDER, data)


def export_artifact(records: list[dict], spec: dict) -> dict:
    return {"datasets": datasets(records, spec), "descriptions": DATASETS, "page": PAGE.read_text(encoding="utf-8")}
