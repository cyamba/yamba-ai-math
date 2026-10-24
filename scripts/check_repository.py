"""Offline integrity checks for the research catalog and local document links."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from harness.catalog import ContractError, load_catalog, load_program
from harness.planner import assemble

LOCAL_DIRS = {".git", ".runs", ".venv", "venv", "__pycache__", ".pytest_cache", "dist", "build"}


def top_level_directories() -> set[str]:
    """Tracked top-level directories; the filesystem stands in when git is unavailable."""
    try:
        listed = subprocess.run(["git", "-C", str(ROOT), "ls-files", "-z"], capture_output=True, check=True).stdout
        names = {path.split("/", 1)[0] for path in listed.decode().split("\0") if "/" in path}
    except (OSError, subprocess.CalledProcessError):
        names = {p.name for p in ROOT.iterdir() if p.is_dir()}
    return {name for name in names if name not in LOCAL_DIRS and not name.endswith(".egg-info")}


def check() -> list[str]:
    failures = []
    try:
        agents, fleets = load_catalog(ROOT)
        program_ids = set()
        for path in sorted((ROOT / "programs").glob("*.json")):
            program = load_program(path, ROOT, fleets)
            if program["id"] in program_ids:
                failures.append(f"Duplicate program id: {program['id']}")
            program_ids.add(program["id"])
            assemble(program, agents, fleets)
    except ContractError as exc:
        failures.append(str(exc))

    briefs = sorted((ROOT / "explore").glob("E*.md"))
    seen_ids = set()
    for path in briefs:
        text = path.read_text(encoding="utf-8")
        frontmatter = re.match(r"\A---\n(.*?)\n---(?:\n|$)", text, re.S)
        if not frontmatter:
            failures.append(f"{path.relative_to(ROOT)}: missing brief frontmatter")
            continue
        fields = dict(re.findall(r"^([a-z_]+):\s*(.+)$", frontmatter[1], re.M))
        for field in ("id", "title", "status", "category", "tags"):
            if not fields.get(field):
                failures.append(f"{path.relative_to(ROOT)}: missing {field}")
        identifier = fields.get("id", "").strip("\"'")
        if identifier in seen_ids or not path.name.startswith(identifier + "-"):
            failures.append(f"{path.relative_to(ROOT)}: duplicate or filename-mismatched id")
        seen_ids.add(identifier)

    for path in sorted((ROOT / "skills").glob("*/SKILL.md")):
        text = path.read_text(encoding="utf-8")
        header = re.match(r"\A---\n(.*?)\n---(?:\n|$)", text, re.S)
        if not header:
            failures.append(f"{path.relative_to(ROOT)}: missing skill frontmatter")
        elif not re.search(r"^description:\s*\S", header[1], re.M) or not re.search(rf"^name:\s*{re.escape(path.parent.name)}\s*$", header[1], re.M):
            failures.append(f"{path.relative_to(ROOT)}: invalid skill name or description")

    repository_map = re.search(r"^## Repository map\n(.*?)(?=^## |\Z)", (ROOT / "AGENTS.md").read_text(encoding="utf-8"),
                               re.S | re.M)
    if not repository_map:
        failures.append("AGENTS.md: missing Repository map section")
    else:
        for name in sorted(top_level_directories()):
            if f"`{name}/" not in repository_map[1]:
                failures.append(f"AGENTS.md: Repository map omits top-level directory {name}/")

    documents =[path for path in ROOT.rglob("*.md")
                 if not any(part.startswith(".") for part in path.relative_to(ROOT).parts)]
    for path in documents:
        text = re.sub(r"```.*?```", "", path.read_text(encoding="utf-8"), flags=re.S)
        for target in re.findall(r"\[[^\]\n]*\]\(([^)\n]+)\)", text):
            target = target.strip().strip("<>")
            if urlparse(target).scheme or target.startswith("#"):
                continue
            relative = unquote(target.split("#", 1)[0])
            if relative and not (path.parent / relative).exists():
                failures.append(f"{path.relative_to(ROOT)}: broken local link {target}")
    return failures


if __name__ == "__main__":
    errors = check()
    if errors:
        print("\n".join(errors), file=sys.stderr)
        raise SystemExit(1)
    print("Repository checks passed: registries, feasible programs, brief/skill metadata, repository map, and local file links.")
    print("These checks do not establish citation accuracy, novelty, mathematical validity, or model performance.")
