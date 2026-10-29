"""Read run and research artifacts without scoring them."""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path

from .spec import sha256_file

HEX64 = re.compile(r"^[0-9a-f]{64}$")
SHA_IN_TEXT = re.compile(r"\b[0-9a-f]{64}\b")
VERDICT_RE = re.compile(r"\*\*Verdict:\s*(.+?)\*\*", re.S)
REVIEWER_RE = re.compile(r"Reviewer:\s*([^.\n]+)")
VERDICT_TERMS = ("supported", "conditional", "incomplete", "refuted", "refutation")
LEVEL_RE = re.compile(r"\s*([ATP])\b")
PATH_PAIRS = (("path", "sha256"), ("log", "sha256"), ("saved_summary", "saved_summary_sha256"))


def load_json(path: Path | None):
    if path is None or not path.is_file():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError):
        return None


def json_values(value, segments: list) -> list:
    """Follow ``segments`` through ``value``; ``"*"`` fans out over lists and objects."""
    nodes = [value]
    for segment in segments:
        following = []
        for node in nodes:
            if segment == "*":
                following.extend(node if isinstance(node, list) else node.values() if isinstance(node, dict) else [])
            elif isinstance(node, dict) and segment in node:
                following.append(node[segment])
            elif isinstance(node, list) and isinstance(segment, int) and -len(node) <= segment < len(node):
                following.append(node[segment])
        nodes = following
    return nodes


def walk_key(value, key: str) -> list:
    found = []
    if isinstance(value, dict):
        for name, child in value.items():
            if name == key:
                found.append(child)
            found.extend(walk_key(child, key))
    elif isinstance(value, list):
        for child in value:
            found.extend(walk_key(child, key))
    return found


@dataclass
class Layout:
    """Where one benchmarked state lives: a commit tree, its framework tree and the ignored run dir."""

    tree: Path
    workspace: str
    run_dir: Path | None = None
    base: Path | None = None

    @property
    def runs_base(self) -> Path | None:
        if self.run_dir is None:
            return None
        for parent in [self.run_dir, *self.run_dir.parents]:
            if parent.name == ".runs":
                return parent.parent
        return self.run_dir.parent

    @property
    def run_label(self) -> str | None:
        if self.run_dir is None:
            return None
        base = self.runs_base
        try:
            return self.run_dir.relative_to(base).as_posix()
        except ValueError:
            return f".runs/{self.run_dir.name}"

    def expand(self, template: str, tmp: Path | None = None) -> tuple[str, Path | None, bool]:
        """Return (display path, absolute path or None, is_run_file) for a registry template."""
        if template.startswith("{run}"):
            rel = template[len("{run}"):].lstrip("/")
            label = f"{self.run_label}/{rel}" if self.run_label else f"{{run}}/{rel}"
            return label, (self.run_dir / rel if self.run_dir else None), True
        if template.startswith("{tmp}"):
            rel = template[len("{tmp}"):].lstrip("/")
            return template, (tmp / rel if tmp else None), False
        rel = template.replace("{ws}", self.workspace)
        return rel, self.tree / rel, False

    def recorded(self, path: str, doc_dir: str | None = None) -> list[Path]:
        """Candidate files for a path recorded inside an artifact (repo-relative or under .runs/)."""
        if path.startswith(".runs/"):
            return [self.runs_base / path] if self.runs_base else []
        candidates = [self.tree / path]
        if doc_dir:
            candidates.append(self.tree / doc_dir / path)
        if self.run_dir and self.run_dir.is_dir():
            candidates += [child / path for child in sorted(self.run_dir.iterdir())
                           if child.is_dir() and child.name.endswith("-source")]
        return candidates


def hash_bindings(document, origin: str) -> list[dict]:
    """Every (path, sha256) pair an artifact records about other files."""
    found = []
    doc_dir = str(Path(origin).parent)

    def visit(node, trail):
        if isinstance(node, dict):
            for path_key, sha_key in PATH_PAIRS:
                path, digest = node.get(path_key), node.get(sha_key)
                if isinstance(path, str) and isinstance(digest, str) and HEX64.match(digest):
                    found.append({"path": path, "sha256": digest, "origin": origin, "at": "/".join(trail), "doc_dir": doc_dir})
            for key, child in node.items():
                is_map = (isinstance(child, dict) and child
                          and (key in ("sources", "sha256") or key.endswith("sources_sha256"))
                          and all(isinstance(v, str) and HEX64.match(v) for v in child.values()))
                if is_map:
                    for path, digest in child.items():
                        found.append({"path": path, "sha256": digest, "origin": origin,
                                      "at": "/".join([*trail, key]), "doc_dir": doc_dir})
                else:
                    visit(child, [*trail, str(key)])
        elif isinstance(node, list):
            for index, child in enumerate(node):
                visit(child, [*trail, str(index)])

    visit(document, [])
    return found


def verify_bindings(bindings: list[dict], layout: Layout) -> list[dict]:
    checked, seen, cache = [], set(), {}
    for binding in bindings:
        key = (binding["path"], binding["sha256"])
        if key in seen:
            continue
        seen.add(key)
        existing = [path for path in layout.recorded(binding["path"], binding.get("doc_dir")) if path.is_file()]
        result = "unknown"
        if existing:
            digests = [cache.setdefault(path, sha256_file(path)) for path in existing]
            result = "pass" if binding["sha256"] in digests else "mismatch"
        checked.append({"path": binding["path"], "origin": binding["origin"], "at": binding["at"],
                        "sha256": binding["sha256"], "result": result})
    return checked


def reviews(tree: Path, pattern: str) -> list[dict]:
    found = []
    for path in sorted(tree.glob(pattern)):
        text = path.read_text(encoding="utf-8", errors="replace")
        verdict = VERDICT_RE.search(text)
        reviewer = REVIEWER_RE.search(text)
        verdict_text = " ".join(verdict.group(1).split()) if verdict else None
        found.append({
            "path": path.relative_to(tree).as_posix(),
            "verdict": verdict_text,
            "terms": [term for term in VERDICT_TERMS if verdict_text and term in verdict_text.lower()],
            "sha256_mentions": len(set(SHA_IN_TEXT.findall(text))),
            "reviewer": reviewer.group(1).strip() if reviewer else None,
        })
    return found


def md_heading(path: Path | None, pattern: str) -> bool | None:
    if path is None or not path.is_file():
        return None
    return re.search(pattern, path.read_text(encoding="utf-8", errors="replace"), re.M) is not None


def reading_list(tree: Path) -> list[dict]:
    path = tree / "references" / "reading-list.md"
    if not path.is_file():
        return []
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) >= 3 and re.fullmatch(r"R\d+", cells[0]):
            level = LEVEL_RE.match(cells[2])
            rows.append({"id": cells[0], "text": cells[1], "level": level.group(1) if level else None})
    return rows


def read_events(path: Path) -> list[dict]:
    events = []
    if path.is_file():
        for line in path.read_text(encoding="utf-8").splitlines():
            try:
                events.append(json.loads(line))
            except json.JSONDecodeError:
                continue
    return events


def harness_runs(run_dir: Path | None) -> list[dict]:
    """Every harness output directory (one holding receipt.json) at or one level below run_dir."""
    if run_dir is None or not run_dir.is_dir():
        return []
    runs = []
    for directory in [run_dir, *sorted(p for p in run_dir.iterdir() if p.is_dir())]:
        receipt = load_json(directory / "receipt.json")
        if not isinstance(receipt, dict):
            continue
        results_dir = directory / "results"
        results = {p.stem: load_json(p) for p in sorted(results_dir.glob("*.json"))} if results_dir.is_dir() else {}
        runs.append({
            "name": directory.relative_to(run_dir).as_posix() or ".",
            "dir": directory,
            "receipt": receipt,
            "plan": load_json(directory / "plan.json"),
            "program": load_json(directory / "program.json"),
            "events": read_events(directory / "events.jsonl"),
            "results": results,
            "packets": sorted((directory / "packets").glob("*.json")) if (directory / "packets").is_dir() else [],
        })
    return runs


def workspace_files(tree: Path, workspace: str, suffixes=(".md", ".json")) -> list[Path]:
    root = tree / workspace
    return sorted(p for p in root.rglob("*") if p.is_file() and p.suffix in suffixes) if root.is_dir() else []
