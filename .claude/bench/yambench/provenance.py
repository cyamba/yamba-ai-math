"""Git provenance, frozen commit snapshots and framework fingerprints."""

from __future__ import annotations

import io
import subprocess
import tarfile
from pathlib import Path

from . import BenchError
from .spec import sha256_bytes, sha256_file

SKIP_PARTS = {"__pycache__", ".lake", ".git"}
MARKER = ".yambench-commit"


def git(repo: Path, *args: str, check: bool = True) -> str:
    proc = subprocess.run(["git", "-C", str(repo), *args], capture_output=True, text=True)
    if check and proc.returncode:
        raise BenchError(f"git {' '.join(args)} failed: {proc.stderr.strip()}")
    return proc.stdout.strip()


def toplevel(path: Path) -> Path:
    return Path(git(path, "rev-parse", "--show-toplevel"))


def resolve(repo: Path, rev: str) -> str:
    return git(repo, "rev-parse", "--verify", f"{rev}^{{commit}}")


def commit_info(repo: Path, rev: str) -> dict:
    sha, committed_at, subject = git(repo, "show", "-s", "--format=%H%x00%cI%x00%s", rev).split("\x00")
    points_at = git(repo, "branch", "--format=%(refname:short)", "--points-at", sha, check=False).splitlines()
    preferred = [name for name in ("main", "master") if name in points_at] + points_at
    return {"commit": sha, "committed_at": committed_at, "subject": subject,
            "branch": preferred[0] if preferred else None}


def working_state(repo: Path) -> dict:
    status = git(repo, "status", "--porcelain=v1", "--untracked-files=all")
    branch = git(repo, "rev-parse", "--abbrev-ref", "HEAD")
    return {"commit": resolve(repo, "HEAD"), "branch": None if branch == "HEAD" else branch,
            "dirty": bool(status), "status_sha256": sha256_bytes(status.encode()) if status else None}


def materialize(repo: Path, sha: str, dest: Path) -> Path:
    """Extract the tracked tree of ``sha`` into ``dest`` so scoring reads a frozen snapshot."""
    marker = dest / MARKER
    if marker.is_file() and marker.read_text().strip() == sha:
        return dest
    attributes = git(repo, "show", f"{sha}:.gitattributes", check=False)
    if "export-ignore" in attributes or "export-subst" in attributes:
        raise BenchError("git archive would alter the snapshot: .gitattributes uses export-ignore/export-subst")
    if not hasattr(tarfile, "data_filter"):
        raise BenchError("Python 3.11.4+ is required for safe snapshot extraction")
    proc = subprocess.run(["git", "-C", str(repo), "archive", "--format=tar", sha], capture_output=True)
    if proc.returncode:
        raise BenchError(f"git archive {sha} failed: {proc.stderr.decode(errors='replace').strip()}")
    dest.mkdir(parents=True, exist_ok=True)
    with tarfile.open(fileobj=io.BytesIO(proc.stdout)) as archive:
        archive.extractall(dest, filter="data")
    marker.write_text(sha + "\n")
    return dest


def fingerprint(root: Path, paths: list[str]) -> dict:
    """Hash the framework files that define a version; benchmark records never count."""
    entries = []
    for item in paths:
        target = root / item
        files = sorted(target.rglob("*")) if item.endswith("/") and target.is_dir() else [target]
        for path in files:
            rel = path.relative_to(root).as_posix()
            if not path.is_file() or SKIP_PARTS & set(path.parts) or rel.startswith(".claude/bench/records/"):
                continue
            entries.append(f"{rel}\0{sha256_file(path)}\n")
    return {"sha256": sha256_bytes("".join(sorted(entries)).encode()), "files": len(entries)}


def changed(repo: Path, base: str, head: str, filter_: str, *paths: str) -> list[str]:
    output = git(repo, "diff", "--name-only", f"--diff-filter={filter_}", base, head, "--", *paths, check=False)
    return [line for line in output.splitlines() if line]


def adding_commit(repo: Path, head: str, path: str) -> str | None:
    found = git(repo, "log", "--diff-filter=A", "--format=%H", head, "--", path, check=False).splitlines()
    return found[-1] if found else None


def is_ancestor(repo: Path, older: str, newer: str) -> bool:
    proc = subprocess.run(["git", "-C", str(repo), "merge-base", "--is-ancestor", older, newer], capture_output=True)
    return proc.returncode == 0
