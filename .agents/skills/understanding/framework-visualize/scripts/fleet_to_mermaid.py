"""Print Mermaid flowcharts of the fleet templates in fleets/registry.json.

Run from anywhere inside the repository:

    python3 .agents/skills/understanding/framework-visualize/scripts/fleet_to_mermaid.py
    python3 .agents/skills/understanding/framework-visualize/scripts/fleet_to_mermaid.py --fleet pair

The diagram is generated from the registry, so it matches the checked-out revision.
Solid arrows are depends_on edges (delivery order). Dotted links labeled "distinct role"
are independent_of constraints: the stage must be assigned a different role profile
than the linked stage. That is role separation, not statistical independence.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def find_root(start: Path) -> Path:
    for candidate in (start, *start.parents):
        if (candidate / "fleets" / "registry.json").is_file():
            return candidate
    raise SystemExit("fleets/registry.json not found; pass --root")


def node(fleet_id: str, stage_id: str) -> str:
    return f"{fleet_id}_{stage_id}".replace("-", "_")


def fleet_chart(fleet: dict) -> list[str]:
    fid = fleet["id"]
    lines = [f'  subgraph {node(fid, "fleet")}["fleet: {fid}"]', "    direction LR"]
    for stage in fleet["stages"]:
        requires = ", ".join(stage.get("requires", []))
        tags = stage.get("required_tags", [])
        tag_text = f"<br/>tags: {', '.join(tags)}" if tags else ""
        lines.append(f'    {node(fid, stage["id"])}["{stage["id"]}<br/>needs: {requires}{tag_text}"]')
    for stage in fleet["stages"]:
        for upstream in stage.get("depends_on", []):
            lines.append(f"    {node(fid, upstream)} --> {node(fid, stage['id'])}")
    for stage in fleet["stages"]:
        for other in stage.get("independent_of", []):
            lines.append(f"    {node(fid, stage['id'])} -.-|distinct role| {node(fid, other)}")
    lines.append("  end")
    return lines


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--root", type=Path, help="repository root (default: search upward)")
    parser.add_argument("--fleet", help="one fleet id (default: all fleets)")
    args = parser.parse_args()
    root = args.root or find_root(Path.cwd())
    registry = json.loads((root / "fleets" / "registry.json").read_text(encoding="utf-8"))
    fleets = registry["fleets"]
    if args.fleet:
        fleets = [f for f in fleets if f["id"] == args.fleet]
        if not fleets:
            known = ", ".join(f["id"] for f in registry["fleets"])
            raise SystemExit(f"unknown fleet {args.fleet!r}; known: {known}")
    out = ["```mermaid", "flowchart LR"]
    for fleet in fleets:
        out.extend(fleet_chart(fleet))
    out.append("```")
    print("\n".join(out))


if __name__ == "__main__":
    main()
