"""Repository-local command line entrypoint. No provider credentials are required."""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

from .catalog import ContractError, load_catalog, load_program, read_json
from .evaluation import compare
from .planner import assemble
from .runtime import execute


ROOT = Path(__file__).resolve().parents[1]


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(description="Assemble bounded research fleets and retain their evidence trail.")
    result.add_argument("--root", type=Path, default=ROOT, help="repository containing the registries and instructions")
    commands = result.add_subparsers(dest="action", required=True)
    commands.add_parser("list", help="list agent roles and fleet templates")
    commands.add_parser("validate", help="validate registry and program contracts")
    for action in ("plan", "packet", "run"):
        command = commands.add_parser(action)
        command.add_argument("program", type=Path)
        if action in {"packet", "run"}:
            command.add_argument("--output", type=Path, help="fresh run directory; default .runs/<program>-<UTC timestamp>")
        if action == "run":
            command.add_argument("--backend", choices=("manual", "command", "replay"), default="manual")
            command.add_argument("--replay-dir", type=Path)
            command.add_argument("--command", nargs=argparse.REMAINDER, help="trusted worker executable and argv; put this option last")
    comparison = commands.add_parser("compare", help="compare paired heldout evaluation records")
    comparison.add_argument("champion", type=Path)
    comparison.add_argument("challenger", type=Path)
    return result


def main(argv: list[str] | None = None) -> int:
    args = parser().parse_args(argv)
    root = args.root.resolve()
    try:
        if args.action == "compare":
            output = compare(read_json(args.champion), read_json(args.challenger))
        else:
            agents, fleets = load_catalog(root)
            if args.action == "list":
                output = {
                    "agents": [{k: a[k] for k in ("id", "name", "category", "capabilities", "tags", "cost_units")} for a in agents.values()],
                    "fleets": [{"id": f["id"], "description": f["description"], "stages": len(f["stages"])} for f in fleets.values()],
                }
            elif args.action == "validate":
                programs = []
                for path in sorted((root / "programs").glob("*.json")):
                    program = load_program(path, root, fleets)
                    assemble(program, agents, fleets)
                    programs.append(program["id"])
                output = {"status": "valid", "agents": len(agents), "fleets": len(fleets), "programs": programs}
            else:
                program = load_program(args.program, root, fleets)
                plan = assemble(program, agents, fleets)
                if args.action == "plan":
                    output = plan
                else:
                    destination = args.output or root / ".runs" / f"{program['id']}-{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')}"
                    backend = "manual" if args.action == "packet" else args.backend
                    output = execute(root, program, plan, agents, destination, backend=backend,
                                     command=getattr(args, "command", None), replay_dir=getattr(args, "replay_dir", None))
        print(json.dumps(output, indent=2, ensure_ascii=False))
        return 1 if output.get("status", "").startswith("failed_") else 0
    except (ContractError, OSError) as exc:
        print(f"harness: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
