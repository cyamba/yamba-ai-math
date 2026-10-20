"""Compare paired, externally assessed outcomes without inventing research scores."""

from __future__ import annotations

import math

from .catalog import ContractError, text_field


def validate_evaluation(record: dict) -> dict:
    for key in ("evaluation_id", "candidate_id", "suite_id", "suite_revision"):
        text_field(record.get(key), f"evaluation.{key}")
    if record.get("split") != "heldout":
        raise ContractError("Comparison requires records declared as heldout; declaration is not a leakage audit")
    if not isinstance(record.get("synthetic"), bool):
        raise ContractError("evaluation.synthetic must explicitly identify fixture data")
    cases = record.get("cases")
    if not isinstance(cases, list) or not cases:
        raise ContractError("evaluation.cases must be nonempty")
    seen = set()
    for case in cases:
        if not isinstance(case, dict):
            raise ContractError("Each evaluation case must be an object")
        name = text_field(case.get("case_id"), "case.case_id")
        if name in seen:
            raise ContractError(f"Duplicate evaluation case: {name}")
        seen.add(name)
        for key in ("answered", "complete_correct"):
            if not isinstance(case.get(key), bool):
                raise ContractError(f"case.{key} must be boolean")
        for key in ("false_claims", "unsupported_claims"):
            value = case.get(key)
            if isinstance(value, bool) or not isinstance(value, int) or value < 0:
                raise ContractError(f"case.{key} must be a nonnegative integer")
        cost = case.get("cost_units")
        try:
            valid_cost = not isinstance(cost, bool) and isinstance(cost, (int, float)) and math.isfinite(cost) and cost >= 0
        except OverflowError:
            valid_cost = False
        if not valid_cost:
            raise ContractError("case.cost_units must be a finite nonnegative number")
        if not case["answered"] and (case["complete_correct"] or case["false_claims"] or case["unsupported_claims"]):
            raise ContractError("An abstention cannot contain answered claims or count as a correct completed answer")
        if case["complete_correct"] and case["false_claims"]:
            raise ContractError("A correct complete answer cannot contain a false claim")
    try:
        finite_total = math.isfinite(sum(case["cost_units"] for case in cases))
    except OverflowError:
        finite_total = False
    if not finite_total:
        raise ContractError("The aggregate evaluation cost must also be finite")
    return record


def metrics(record: dict) -> dict:
    cases = record["cases"]
    answered = sum(c["answered"] for c in cases)
    correct = sum(c["complete_correct"] for c in cases)
    return {
        "cases": len(cases), "answered": answered,
        "coverage": answered / len(cases),
        "correct_complete": correct, "success_rate": correct / len(cases),
        "false_response_risk": sum(c["false_claims"] > 0 for c in cases) / answered if answered else None,
        "unsupported_response_risk": sum(c["unsupported_claims"] > 0 for c in cases) / answered if answered else None,
        "cost_units": sum(c["cost_units"] for c in cases),
    }


def compare(champion: dict, challenger: dict) -> dict:
    validate_evaluation(champion)
    validate_evaluation(challenger)
    for key in ("suite_id", "suite_revision", "split", "synthetic"):
        if champion[key] != challenger[key]:
            raise ContractError(f"Cannot compare different {key} values")
    if {c["case_id"] for c in champion["cases"]} != {c["case_id"] for c in challenger["cases"]}:
        raise ContractError("Comparison requires identical paired case IDs")
    left, right = metrics(champion), metrics(challenger)
    comparable = left["answered"] > 0 and right["answered"] > 0
    weak, strict = [], []
    if comparable:
        for key, direction in (("success_rate", 1), ("coverage", 1), ("false_response_risk", -1), ("unsupported_response_risk", -1), ("cost_units", -1)):
            difference = direction * (right[key] - left[key])
            weak.append(difference >= 0)
            strict.append(difference > 0)
    return {
        "champion": champion["candidate_id"], "challenger": challenger["candidate_id"],
        "suite_id": champion["suite_id"], "suite_revision": champion["suite_revision"],
        "synthetic": champion["synthetic"],
        "champion_metrics": left, "challenger_metrics": right,
        "challenger_dominates_observed_cases": comparable and all(weak) and any(strict),
        "promotion_eligible_for_review": comparable and not champion["synthetic"] and all(weak) and any(strict),
        "promotion_authorized": False,
        "limitations": "Descriptive comparison only. No statistical significance, proof validity, novelty, actual monetary cost, leakage freedom, or future superiority is established. Zero observed failures is not zero population risk. Human review and the meta protocol govern promotion.",
    }
