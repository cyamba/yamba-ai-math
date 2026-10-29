"""Session telemetry from Codex rollouts and Claude Code transcripts (via recorder.py)."""

from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path

from .spec import sha256_file

CODEX_ROOT = Path.home() / ".codex" / "sessions"
RECORDER = Path(os.environ.get("YAMBENCH_RECORDER",
                               Path.home() / "YambaCode" / "agentic-workbench-recorder" / "recorder.py"))
INJECTED = ("# AGENTS.md instructions", "<environment_context", "<external_", "<user_instructions",
            "<INSTRUCTIONS>", "<turn_aborted", "<user_shell_command", "<task-notification",
            "[SYSTEM NOTIFICATION", "<system-reminder")
WRITE_TOOLS = {"Edit", "Write", "NotebookEdit", "MultiEdit", "apply_patch"}
SHELL_TOOLS = {"exec", "exec_command", "shell", "Bash"}
SHELL_WRITE = re.compile(r"\btee\s+[\w~./-]|\bsed\s+-i\b|(?<![<>=&\d-])>>?\s*(?!/dev/null)(?!\d)[\w~$/-][\w~$./-]*[/.][\w./-]*")
JS_CMD = re.compile(r"""cmd\s*:\s*("(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|`[^`]*`)""")
APPROVAL = re.compile(r"^\W*(please implement this plan|yes\b|ok\b|okay\b|approved?\b|go ahead|continue|proceed"
                      r"|excellent|great|good job|looks good|lgtm|thanks?\b)", re.I)
STATUS = re.compile(r"(are|is) (things|it|this) going|\bstatus\b|\bprogress\b|how far|are you done|any update", re.I)
CORRECTION = re.compile(r"^\W*(no\b|wrong|incorrect|stop\b|revert|undo)|\b(that's not|not what i|don't do|do not do)\b", re.I)
TOKEN_FIELDS = ("uncached_input", "cache_read", "cache_write", "output", "reasoning")


def classify_turn(text: str) -> str:
    """Heuristic intent of a human turn after the initial prompt; recorded as approximate."""
    if APPROVAL.search(text):
        return "approval"
    if STATUS.search(text):
        return "status"
    if CORRECTION.search(text):
        return "correction"
    return "steering"


def injected(text: str) -> bool:
    stripped = text.strip()
    return not stripped or stripped.startswith(INJECTED) or bool(re.fullmatch(r"(<[\w-]+[^>]*>.*?</[\w-]+>\s*)+", stripped, re.S))


def epoch(stamp: str | None) -> float | None:
    if not stamp:
        return None
    try:
        return datetime.fromisoformat(stamp.replace("Z", "+00:00")).timestamp()
    except ValueError:
        return None


def codex_role(source) -> tuple[str, str | None]:
    if isinstance(source, dict) and "subagent" in source:
        sub = source["subagent"]
        if isinstance(sub, dict) and "thread_spawn" in sub:
            return "child", (sub["thread_spawn"] or {}).get("agent_path")
        return "overhead", sub.get("other") if isinstance(sub, dict) else str(sub)
    return "lead", None


def codex_meta(path: Path) -> dict | None:
    try:
        with open(path, encoding="utf-8") as handle:
            for _ in range(5):
                line = handle.readline()
                if not line:
                    break
                record = json.loads(line)
                if record.get("type") == "session_meta":
                    return record.get("payload") or {}
    except (OSError, json.JSONDecodeError, UnicodeDecodeError):
        return None
    return None


def call_name_and_text(payload: dict) -> tuple[str, str]:
    name = payload.get("name") or ""
    text = payload.get("input") if isinstance(payload.get("input"), str) else payload.get("arguments") or ""
    return name, text if isinstance(text, str) else json.dumps(text)


def shell_commands(name: str, text: str) -> list[str]:
    """Shell command strings inside a Codex call: JS code-mode ``cmd:`` literals or JSON ``cmd`` arguments."""
    if name == "exec":
        return [literal[1:-1].replace("\\n", "\n").replace('\\"', '"') for literal in JS_CMD.findall(text)]
    try:
        cmd = json.loads(text).get("cmd")
    except (json.JSONDecodeError, AttributeError):
        return [text]
    return [" ".join(cmd) if isinstance(cmd, list) else str(cmd or "")]


def modifies_files(name: str, text: str) -> bool:
    if name in WRITE_TOOLS or "apply_patch" in text:
        return True
    return name in SHELL_TOOLS and any(SHELL_WRITE.search(cmd) for cmd in shell_commands(name, text))


def read_codex(path: Path) -> dict:
    meta, models, efforts, turns = {}, {}, {}, []
    tokens, window, ctx_peak = None, None, None
    compacted = context_compacted = tool_calls = 0
    orientation, first, last = None, None, None
    with open(path, encoding="utf-8") as handle:
        for line in handle:
            try:
                record = json.loads(line)
            except json.JSONDecodeError:
                continue
            kind, payload, stamp = record.get("type"), record.get("payload") or {}, record.get("timestamp")
            first = first or stamp
            last = stamp or last
            sub = payload.get("type") if isinstance(payload, dict) else None
            if kind == "session_meta":
                meta = payload
            elif kind == "turn_context":
                model, effort = payload.get("model"), payload.get("effort")
                if model:
                    models[model] = models.get(model, 0) + 1
                if effort:
                    efforts[effort] = efforts.get(effort, 0) + 1
            elif kind == "compacted":
                compacted += 1
            elif kind == "event_msg" and sub == "context_compacted":
                context_compacted += 1
            elif kind == "event_msg" and sub == "token_count" and payload.get("info"):
                info = payload["info"]
                window = info.get("model_context_window") or window
                total = info.get("total_token_usage")
                if total:
                    tokens = total
                used = (info.get("last_token_usage") or {}).get("input_tokens")
                if used and window:
                    ctx_peak = max(ctx_peak or 0.0, used / window)
            elif kind == "response_item" and sub in ("function_call", "custom_tool_call"):
                name, text = call_name_and_text(payload)
                if orientation is None and modifies_files(name, text):
                    orientation = tool_calls
                tool_calls += 1
            elif kind == "response_item" and sub == "message" and payload.get("role") == "user":
                text = " ".join(item.get("text", "") for item in payload.get("content", []) if isinstance(item, dict))
                if not injected(text):
                    turns.append({"at": stamp, "text": text})
    role, name = codex_role(meta.get("source"))
    usage = None
    if tokens:
        usage = {"uncached_input": max(0, tokens.get("input_tokens", 0) - tokens.get("cached_input_tokens", 0)),
                 "cache_read": tokens.get("cached_input_tokens", 0),
                 "cache_write": tokens.get("cache_write_input_tokens", 0),
                 "output": tokens.get("output_tokens", 0),
                 "reasoning": tokens.get("reasoning_output_tokens", 0)}
    return {
        "client": "codex", "id": meta.get("id"), "parent": meta.get("parent_thread_id"), "role": role, "name": name,
        "file": str(path), "file_sha256": sha256_file(path),
        "model": max(models, key=models.get) if models else None, "models": models,
        "effort": max(efforts, key=efforts.get) if efforts else None, "efforts": efforts,
        "cwd": meta.get("cwd"), "git": {"branch": (meta.get("git") or {}).get("branch"),
                                        "commit": (meta.get("git") or {}).get("commit_hash")},
        "started_at": meta.get("timestamp") or first, "ended_at": last,
        "tokens": usage, "context_window": window, "ctx_peak_fraction": round(ctx_peak, 4) if ctx_peak else None,
        "compactions": max(compacted, context_compacted), "tool_calls": tool_calls, "tool_errors": None,
        "orientation_tool_calls": orientation, "orientation_method": "codex heuristic",
        "redundant_read_ratio": None, "turns": turns,
    }


def codex_candidates(repo_paths: list[Path], root: Path = CODEX_ROOT) -> list[tuple[Path, dict]]:
    wanted = {str(p.resolve()) for p in repo_paths}
    found = []
    for path in sorted(root.rglob("rollout-*.jsonl")) if root.is_dir() else []:
        meta = codex_meta(path)
        if meta and meta.get("cwd") and str(Path(meta["cwd"]).resolve()) in wanted:
            found.append((path, meta))
    return found


def select_codex(repo_paths: list[Path], pinned: list[str], framework_commit: str | None,
                 window: tuple[float | None, float | None], root: Path = CODEX_ROOT) -> list[dict]:
    """Pinned lead threads (or inferred ones) plus their child and overhead threads."""
    candidates = codex_candidates(repo_paths, root)
    start, end = window
    leads = set()
    for path, meta in candidates:
        role, _ = codex_role(meta.get("source"))
        sid = meta.get("id") or ""
        if role != "lead":
            continue
        if pinned:
            if any(sid.startswith(p) for p in pinned):
                leads.add(sid)
            continue
        began = epoch(meta.get("timestamp"))
        commit = (meta.get("git") or {}).get("commit_hash") or ""
        if framework_commit and commit.startswith(framework_commit[:12]) and began is not None \
                and (start is None or began >= start - 3600) and (end is None or began <= end):
            leads.add(sid)
    chosen = [path for path, meta in candidates if meta.get("id") in leads or meta.get("parent_thread_id") in leads]
    sessions = [read_codex(path) for path in chosen]
    for session in sessions:
        session["selection"] = "pinned" if pinned else "inferred"
    return dedupe(sessions)


def dedupe(sessions: list[dict]) -> list[dict]:
    """Rollout files that fork or resume a thread repeat its history; keep the fullest per thread id."""
    best = {}
    for session in sessions:
        total = sum((session["tokens"] or {}).get(f, 0) for f in TOKEN_FIELDS)
        key = (session["client"], session["id"])
        if key not in best or total > best[key][0]:
            best[key] = (total, session)
    return [session for _, session in sorted(best.values(), key=lambda item: item[1]["started_at"] or "")]


def read_claude(session_id: str, recorder: Path = RECORDER, timeout: int = 180) -> tuple[list[dict], str | None]:
    if not recorder.is_file():
        return [], f"recorder not found at {recorder}"
    proc = subprocess.run([sys.executable, str(recorder), session_id, "--json"], capture_output=True, text=True,
                          timeout=timeout)
    if proc.returncode:
        return [], f"recorder failed: {proc.stderr.strip()[:200]}"
    data = json.loads(proc.stdout)
    events = data.get("events", [])
    sessions = []
    for agent in data.get("agents", []):
        aid = agent.get("id")
        own = [e for e in events if e.get("agent") == aid]
        calls = [e for e in own if e.get("kind") == "tool.call"]
        writes = [i for i, e in enumerate(calls) if e.get("tool") in WRITE_TOOLS]
        reads = [e.get("detail") for e in calls if e.get("tool") == "Read" and e.get("detail")]
        turns = [{"at": e.get("ts"), "text": e.get("text", "")} for e in own
                 if e.get("kind") == "prompt" and e.get("source") == "human" and not injected(e.get("text", ""))]
        tok = agent.get("tokens") or {}
        is_lead = agent.get("type") == "orchestrator"
        sessions.append({
            "client": "claude-code", "id": data.get("session") if is_lead else f"{data.get('session')}:{aid}",
            "parent": None if is_lead else data.get("session"), "role": "lead" if is_lead else "child",
            "name": agent.get("label"), "file": agent.get("transcript"), "file_sha256": None,
            "model": agent.get("model"), "models": agent.get("models") or {},
            "effort": agent.get("effort"), "efforts": agent.get("efforts") or {},
            "cwd": data.get("cwd"), "git": {"branch": None, "commit": None},
            "started_at": iso(agent.get("started_at")), "ended_at": iso(agent.get("ended_at")),
            "tokens": {"uncached_input": tok.get("input", 0), "cache_read": tok.get("cache_read", 0),
                       "cache_write": tok.get("cache_write", 0), "output": tok.get("output", 0),
                       "reasoning": tok.get("thinking", 0)},
            "context_window": agent.get("window"),
            "ctx_peak_fraction": round(agent["ctx_peak_pct"] / 100, 4) if agent.get("ctx_peak_pct") is not None else None,
            "compactions": agent.get("compactions", 0), "tool_calls": agent.get("tools", 0),
            "tool_errors": agent.get("tool_errors"),
            "orientation_tool_calls": writes[0] if writes else None, "orientation_method": "first Edit/Write call",
            "redundant_read_ratio": round(1 - len(set(reads)) / len(reads), 4) if reads else None,
            "turns": turns, "selection": "pinned",
        })
    return sessions, None


def iso(milliseconds) -> str | None:
    if milliseconds is None:
        return None
    return datetime.fromtimestamp(milliseconds / 1000).astimezone().isoformat()


def summarize(sessions: list[dict]) -> dict:
    working = [s for s in sessions if s["role"] in ("lead", "child")]
    overhead = [s for s in sessions if s["role"] == "overhead"]
    leads = [s for s in working if s["role"] == "lead"]

    def total(group):
        if not group or any(s["tokens"] is None for s in group):
            return None
        return {f: sum(s["tokens"][f] for s in group) for f in TOKEN_FIELDS}

    tokens = total(working)
    turns = [t for s in leads for t in s["turns"][1:]]
    classified = {}
    for turn in turns:
        turn["kind"] = classify_turn(turn["text"])
        classified[turn["kind"]] = classified.get(turn["kind"], 0) + 1
    peaks = [s["ctx_peak_fraction"] for s in working if s["ctx_peak_fraction"] is not None]
    orient = [s["orientation_tool_calls"] for s in leads if s["orientation_tool_calls"] is not None]
    redundant = [s["redundant_read_ratio"] for s in leads if s["redundant_read_ratio"] is not None]
    errors = [s["tool_errors"] for s in working if s["tool_errors"] is not None]
    return {
        "available": bool(working),
        "sessions": len(sessions), "working": len(working), "overhead": len(overhead),
        "clients": sorted({s["client"] for s in sessions}),
        "models": sorted({m for s in working for m in s["models"]}),
        "efforts": sorted({e for s in working for e in s["efforts"]}),
        "tokens": tokens, "overhead_tokens": total(overhead),
        "effective_tokens": tokens["uncached_input"] + tokens["cache_write"] + tokens["output"] if tokens else None,
        "human_turns": classified if leads else None, "initial_prompts": len(leads),
        "compactions": sum(s["compactions"] for s in working) if working else None,
        "ctx_peak_fraction": max(peaks) if peaks else None,
        "orientation_tool_calls": min(orient) if orient else None,
        "redundant_read_ratio": max(redundant) if redundant else None,
        "tool_calls": sum(s["tool_calls"] for s in working) if working else None,
        "tool_errors": sum(errors) if errors else None,
        "distinct_threads": len(working) >= 2 if working else None,
        "window": [min((s["started_at"] for s in sessions if s["started_at"]), default=None),
                   max((s["ended_at"] for s in sessions if s["ended_at"]), default=None)],
        "child_names": sorted({s["name"] for s in working if s["role"] == "child" and s["name"]}),
    }


def public(session: dict) -> dict:
    """The sanitized form stored in a tracked record: no file paths, no message text."""
    turns = {}
    for turn in session["turns"][1:] if session["role"] == "lead" else []:
        kind = turn.get("kind") or classify_turn(turn["text"])
        turns[kind] = turns.get(kind, 0) + 1
    keep = ("client", "id", "parent", "role", "name", "model", "effort", "efforts", "git", "started_at", "ended_at",
            "tokens", "context_window", "ctx_peak_fraction", "compactions", "tool_calls", "tool_errors",
            "orientation_tool_calls", "orientation_method", "redundant_read_ratio", "selection", "file_sha256")
    return {**{key: session.get(key) for key in keep}, "human_turns": turns if session["role"] == "lead" else None}
