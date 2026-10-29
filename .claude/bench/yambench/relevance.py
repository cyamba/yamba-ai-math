"""Question the benchmark itself: which axes still separate versions, and whether a spec review is due.

Flags are questions for the operator, not verdicts. Changing an axis is a new spec version.
"""

from __future__ import annotations

from datetime import date

from .spec import metric_defs, metric_ids

SATURATED, FLOOR, HYGIENE_GAP = 95.0, 5.0, 40.0
CREATION_FAMILY = "discovery"


def current_finals(records: list[dict], spec: dict) -> list[dict]:
    digest = spec["hashes"].get("metrics.json")
    return [r for r in records if r.get("kind") == "final"
            and (r.get("spec") or {}).get("hashes", {}).get("metrics.json") == digest]


def axis(records: list[dict], metric_id: str) -> dict:
    entries = [r["metrics"][metric_id] for r in records if metric_id in r["metrics"]]
    scores = [e["score"] for e in entries if e["status"] == "scored"]
    unmeasured = sum(1 for e in entries if e["status"] in ("unknown", "n/a"))
    flags = []
    if entries and unmeasured * 2 >= len(entries):
        flags.append("unmeasured: unknown or n/a in at least half the records; fix the instrument or retire the axis")
    if len(scores) >= 2 and min(scores) >= SATURATED:
        flags.append("saturated: every score is at the ceiling; the axis no longer separates versions")
    if len(scores) >= 2 and max(scores) <= FLOOR:
        flags.append("floor: every score is at the floor; check the axis can be reached at all")
    if len(scores) >= 3 and max(scores) == min(scores):
        flags.append("flat: identical scores across records")
    return {"records": len(entries), "scored": len(scores), "unmeasured": unmeasured,
            "min": min(scores, default=None), "max": max(scores, default=None), "flags": flags}


def shape(record: dict, defs: dict) -> dict:
    """Whether the radar of one record is carried by process axes rather than mathematical ones."""
    creation, other = [], []
    for metric_id, entry in record["metrics"].items():
        if entry["status"] == "scored" and metric_id in defs:
            (creation if defs[metric_id]["family"] == CREATION_FAMILY else other).append(entry["score"])
    mean = lambda values: round(sum(values) / len(values), 1) if values else None
    found = {"record_id": record["record_id"], "creation_mean": mean(creation), "process_mean": mean(other)}
    if found["creation_mean"] is not None and found["process_mean"] is not None \
            and found["process_mean"] - found["creation_mean"] >= HYGIENE_GAP:
        found["flag"] = "hygiene-dominated: rigor and operations carry the radar while discovery axes stay low"
    return found


def relevance(records: list[dict], spec: dict, today: date | None = None) -> dict:
    today = today or date.today()
    defs, review = metric_defs(spec), spec["metrics"]["relevance_review"]
    finals = current_finals(records, spec)
    since = [r for r in finals if r.get("created_at", "")[:10] > review["reviewed"]]
    reasons = []
    if len(since) >= review["next_due"]["records"]:
        reasons.append(f"{len(since)} final record(s) since the last review")
    if today.isoformat() >= review["next_due"]["date"]:
        reasons.append(f"review date {review['next_due']['date']} reached")
    return {
        "spec_version": spec["metrics"]["spec_version"],
        "records": len(finals),
        "review": {"reviewed": review["reviewed"], "due": bool(reasons), "reasons": reasons},
        "axes": {metric_id: {"name": defs[metric_id]["name"], "family": defs[metric_id]["family"],
                             **axis(finals, metric_id)} for metric_id in metric_ids(spec)},
        "shapes": [shape(r, defs) for r in finals],
        "note": "Descriptive. A flag asks whether an axis still tracks new mathematics; it changes nothing by itself.",
    }


def text(report: dict) -> str:
    review = report["review"]
    lines = [f"spec {report['spec_version']}: {report['records']} final record(s); last review {review['reviewed']}; "
             + ("review DUE: " + "; ".join(review["reasons"]) if review["due"] else "review not yet due")]
    for metric_id, found in report["axes"].items():
        span = "" if found["min"] is None else f" {found['min']:g}..{found['max']:g}"
        lines.append(f"{metric_id} {found['name']:<22} scored {found['scored']}/{found['records']}{span}"
                     + "".join(f"\n    ? {flag}" for flag in found["flags"]))
    lines += [f"{s['record_id']}: discovery {s['creation_mean']} vs process {s['process_mean']}"
              + (f"\n    ? {s['flag']}" if s.get("flag") else "") for s in report["shapes"]]
    return "\n".join(lines)
