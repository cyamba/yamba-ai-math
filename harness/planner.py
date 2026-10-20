"""Exact assignment of declared roles; this is not an optimizer of research quality."""

from __future__ import annotations

from .catalog import ContractError, topological_order


def assemble(program: dict, agents: dict[str, dict], fleets: dict[str, dict]) -> dict:
    fleet = fleets[program["fleet"]]
    stages = topological_order(fleet["stages"])
    rounds = program.get("rounds", 1)
    constraints = program["constraints"]
    maximum_agents = min(fleet["max_agents"], constraints["max_agents"])
    preferred_tags = set(program.get("preferred_tags", []))
    candidates = {
        stage["id"]: sorted(
            (a for a in agents.values() if set(stage["requires"]) <= set(a["capabilities"]) and set(stage.get("required_tags", [])) <= set(a["tags"])),
            key=lambda a: (a["cost_units"], a["id"]),
        )
        for stage in stages
    }
    exclusions = {s["id"]: set(s.get("independent_of", [])) for s in stages}
    for stage in stages:
        for other in stage.get("independent_of", []):
            exclusions[other].add(stage["id"])
    best_key = None
    best_assignment = None
    minimum_suffix = [0] * (len(stages) + 1)
    for i in range(len(stages) - 1, -1, -1):
        options = candidates[stages[i]["id"]]
        if not options:
            raise ContractError(f"No agent covers stage {stages[i]['id']}")
        minimum_suffix[i] = minimum_suffix[i + 1] + options[0]["cost_units"]

    def search(i: int, assignment: dict[str, str], cost: int):
        nonlocal best_key, best_assignment
        lower_bound = (cost + minimum_suffix[i]) * rounds
        if lower_bound > constraints["max_cost_units"]:
            return
        if best_key is not None and lower_bound > best_key[0]:
            return
        if i == len(stages):
            affinity = sum(len(preferred_tags & set(agents[a]["tags"])) for a in assignment.values())
            key = (cost * rounds, -affinity, len(set(assignment.values())), tuple(assignment[s["id"]] for s in stages))
            if best_key is None or key < best_key:
                best_key, best_assignment = key, dict(assignment)
            return
        stage = stages[i]
        for agent in candidates[stage["id"]]:
            if any(assignment.get(other) == agent["id"] for other in exclusions[stage["id"]]):
                continue
            assignment[stage["id"]] = agent["id"]
            if len(set(assignment.values())) <= maximum_agents:
                search(i + 1, assignment, cost + agent["cost_units"])
            del assignment[stage["id"]]

    search(0, {}, 0)
    if best_assignment is None:
        raise ContractError("No fleet assignment satisfies the capability, independence, agent, and dispatch budgets")

    sinks = {s["id"] for s in stages} - {d for s in stages for d in s.get("depends_on", [])}
    steps = []
    for round_number in range(1, rounds + 1):
        def step_id(name: str, r: int = round_number) -> str:
            return name if rounds == 1 else f"r{r}--{name}"

        for stage in stages:
            dependencies = [step_id(d) for d in stage.get("depends_on", [])]
            if round_number > 1 and not dependencies:
                dependencies = [step_id(d, round_number - 1) for d in sorted(sinks)]
            steps.append({
                "id": step_id(stage["id"]),
                "stage_id": stage["id"],
                "round": round_number,
                "requires": stage["requires"],
                "depends_on": dependencies,
                "agent_id": best_assignment[stage["id"]],
                "cost_units": agents[best_assignment[stage["id"]]]["cost_units"],
            })
    return {
        "protocol_version": "1",
        "program_id": program["id"],
        "fleet_id": fleet["id"],
        "objective": "minimum declared dispatch cost; then maximum declared preferred-tag matches; then distinct role count; then stable agent IDs",
        "optimality_scope": "exact for this finite registry and constraints; capability tags and costs are declared proxies, not measured quality or money",
        "cost_units": best_key[0],
        "distinct_agents": sorted(set(best_assignment.values())),
        "rounds": rounds,
        "max_workers": constraints["max_workers"],
        "steps": steps,
    }
