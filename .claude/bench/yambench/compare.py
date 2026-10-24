"""Describe how two records of the same problem differ, axis by axis, without a blended score."""

from __future__ import annotations

from . import BenchError
from .spec import METRIC_IDS

GATE_ORDER = {"pass": 0, "unknown": 1, "review": 2, "fail": 3}


def same_runtime(a: dict, b: dict) -> bool:
    ta, tb = a["provenance"]["telemetry"], b["provenance"]["telemetry"]
    return ta.get("clients") == tb.get("clients") and ta.get("models") == tb.get("models")


def compare(baseline: dict, candidate: dict, allow_spec_drift: bool = False) -> dict:
    pb, pc = baseline["provenance"]["problem"]["id"], candidate["provenance"]["problem"]["id"]
    if pb != pc:
        raise BenchError(f"Records benchmark different problems: {pb} vs {pc}")
    drift = baseline["spec"]["hashes"].get("metrics.json") != candidate["spec"]["hashes"].get("metrics.json")
    if drift and not allow_spec_drift:
        raise BenchError("Records use different metric specifications; rescore both or pass --allow-spec-drift")
    axes, tally = {}, {"better": 0, "worse": 0, "equal": 0, "unknown": 0}
    runtime_match = same_runtime(baseline, candidate)
    for metric_id in METRIC_IDS:
        a, b = baseline["metrics"][metric_id], candidate["metrics"][metric_id]
        outcome, delta = "unknown", None
        if a["status"] == b["status"] == "scored" and not (metric_id == "B09" and not runtime_match):
            delta = round(b["score"] - a["score"], 1)
            outcome = "better" if delta > 0 else "worse" if delta < 0 else "equal"
        tally[outcome] += 1
        axes[metric_id] = {"baseline": a["score"], "candidate": b["score"], "baseline_status": a["status"],
                           "candidate_status": b["status"], "delta": delta, "outcome": outcome}
    gates = {g: {"baseline": baseline["gates"][g]["status"], "candidate": candidate["gates"][g]["status"]}
             for g in baseline["gates"]}
    regression = any(GATE_ORDER[v["candidate"]] > GATE_ORDER[v["baseline"]] for v in gates.values())
    eligible = (not baseline["retrospective"] and not candidate["retrospective"]
                and baseline["kind"] == candidate["kind"] == "final" and not drift)
    limitations = ["Unknown, pending and n/a axes are never counted as wins.",
                   "Observed dominance on one paired run is descriptive evidence, not significance."]
    if not runtime_match:
        limitations.append("Clients or models differ; B09 is not compared.")
    if not eligible:
        limitations.append("Retrospective, snapshot or spec-drifted records cannot support a dominance claim.")
    return {
        "problem": pb, "baseline": baseline["record_id"], "candidate": candidate["record_id"],
        "framework": {"baseline": baseline["provenance"]["framework"]["commit"],
                      "candidate": candidate["provenance"]["framework"]["commit"]},
        "axes": axes, "summary": tally, "gates": gates, "gate_regression": regression,
        "observed_dominance": tally["worse"] == 0 and tally["better"] > 0 and not regression,
        "dominance_claim_eligible": eligible, "promotion_authorized": False, "limitations": limitations,
    }
