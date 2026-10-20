"""Read and validate research programs, agent cards, and fleet DAGs."""

from __future__ import annotations

import json
import re
from pathlib import Path


class ContractError(ValueError):
    """An input violates the repository's orchestration contract."""


IDENTIFIER = re.compile(r"^[a-zA-Z0-9][a-zA-Z0-9_-]*$")


def read_json(path: Path) -> dict:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        raise ContractError(f"Cannot read {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise ContractError(f"{path}: expected a JSON object")
    return value


def positive_int(value, label: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < 1:
        raise ContractError(f"{label} must be a positive integer")
    return value


def strings(value, label: str, *, empty: bool = False) -> list[str]:
    if not isinstance(value, list) or (not empty and not value):
        raise ContractError(f"{label} must be {'a' if empty else 'a nonempty'} list")
    if any(not isinstance(item, str) or not item.strip() for item in value):
        raise ContractError(f"{label} must contain nonempty strings")
    if len(value) != len(set(value)):
        raise ContractError(f"{label} contains duplicates")
    return value


def text_field(value, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ContractError(f"{label} must be a nonempty string")
    return value


def local_file(root: Path, relative: str) -> Path:
    text_field(relative, "file path")
    path = (root / relative).resolve()
    if not path.is_relative_to(root.resolve()) or not path.is_file():
        raise ContractError(f"Expected an existing file inside the repository: {relative}")
    return path


def index_records(records, label: str) -> dict[str, dict]:
    if not isinstance(records, list) or not records:
        raise ContractError(f"{label} must be a nonempty list")
    result = {}
    for record in records:
        if not isinstance(record, dict):
            raise ContractError(f"{label}: expected objects")
        key = record.get("id")
        if not isinstance(key, str) or not IDENTIFIER.fullmatch(key):
            raise ContractError(f"{label}: invalid id {key!r}")
        if key in result:
            raise ContractError(f"{label}: duplicate id {key}")
        result[key] = record
    return result


def topological_order(stages: list[dict]) -> list[dict]:
    remaining = index_records(stages, "stages")
    known = set(remaining)
    for stage in stages:
        for field in ("depends_on", "independent_of"):
            refs = strings(stage.get(field, []), f"{stage['id']}.{field}", empty=True)
            if set(refs) - known or stage["id"] in refs:
                raise ContractError(f"{stage['id']}.{field}: unknown or self reference")
        strings(stage.get("requires"), f"{stage['id']}.requires")
        strings(stage.get("required_tags", []), f"{stage['id']}.required_tags", empty=True)
    ordered = []
    while remaining:
        ready = [s for s in remaining.values() if not set(s.get("depends_on", [])) & remaining.keys()]
        if not ready:
            raise ContractError("Fleet dependencies contain a cycle; unroll bounded rounds instead")
        for stage in ready:
            ordered.append(stage)
            del remaining[stage["id"]]
    return ordered


def load_catalog(root: Path) -> tuple[dict[str, dict], dict[str, dict]]:
    agents = index_records(read_json(root / "agents/registry.json").get("agents"), "agents")
    fleets = index_records(read_json(root / "fleets/registry.json").get("fleets"), "fleets")
    for agent in agents.values():
        for field in ("name", "category"):
            text_field(agent.get(field), f"{agent['id']}.{field}")
        strings(agent.get("capabilities"), f"{agent['id']}.capabilities")
        strings(agent.get("tags"), f"{agent['id']}.tags", empty=True)
        positive_int(agent.get("cost_units"), f"{agent['id']}.cost_units")
        local_file(root, agent.get("prompt_file"))
    for fleet in fleets.values():
        text_field(fleet.get("description"), f"{fleet['id']}.description")
        positive_int(fleet.get("max_agents"), f"{fleet['id']}.max_agents")
        required = set(strings(fleet.get("required_capabilities"), f"{fleet['id']}.required_capabilities"))
        stages = topological_order(fleet.get("stages"))
        stage_requirements = set().union(*(set(s["requires"]) for s in stages))
        if required != stage_requirements:
            raise ContractError(f"{fleet['id']}: required_capabilities must equal the union of stage requirements")
        for stage in stages:
            if not any(set(stage["requires"]) <= set(a["capabilities"]) and set(stage.get("required_tags", [])) <= set(a["tags"]) for a in agents.values()):
                raise ContractError(f"{fleet['id']}.{stage['id']}: no agent covers all requirements")
    return agents, fleets


def load_program(path: Path, root: Path, fleets: dict[str, dict]) -> dict:
    program = read_json(path)
    for field in ("id", "title", "objective", "fleet"):
        text_field(program.get(field), f"program.{field}")
    if not IDENTIFIER.fullmatch(program["id"]):
        raise ContractError("program.id must be a simple identifier")
    if program["fleet"] not in fleets:
        raise ContractError(f"Unknown fleet: {program['fleet']}")
    for field in ("deliverables", "success_criteria", "stop_conditions"):
        strings(program.get(field), f"program.{field}")
    for brief in strings(program.get("briefs", []), "program.briefs", empty=True):
        local_file(root, brief)
    strings(program.get("preferred_tags", []), "program.preferred_tags", empty=True)
    constraints = program.get("constraints")
    if not isinstance(constraints, dict):
        raise ContractError("program.constraints must be an object")
    for field in ("max_agents", "max_cost_units", "max_workers", "max_rounds"):
        positive_int(constraints.get(field), f"constraints.{field}")
    rounds = positive_int(program.get("rounds", 1), "program.rounds")
    if rounds > constraints["max_rounds"]:
        raise ContractError("program.rounds exceeds max_rounds")
    timeout = positive_int(constraints.get("timeout_seconds", 120), "constraints.timeout_seconds")
    if timeout > 3600:
        raise ContractError("Per-call timeout_seconds must not exceed 3600")
    return program
