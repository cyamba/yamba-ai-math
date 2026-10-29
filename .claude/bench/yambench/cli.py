"""Command line: start, snapshot, stop, collect, finalize, validate, compare, relevance, dashboard, export-artifact, sessions."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from . import BenchError
from . import provenance as prov
from .collectors import Layout, load_json
from .compare import compare
from .dashboard import export_artifact, render
from .metrics import Context, compute
from .records import (RECORDS_DIR, apply_audit, apply_judgments, build, family, judge_packet, load_all, now,
                      validate, write)
from .relevance import relevance, text as relevance_text
from .spec import CANARY_RE, load_spec, problem as find_problem, sha256_file
from .telemetry import codex_candidates, codex_role, epoch, read_claude, select_codex, summarize

MATH_DOMAIN = ("AGENTS.md", "CLAUDE.md", "SKILLS.md", "explore/AGENTS.md")
MATH_GLOBS = ("agents/*.md", "skills/*/SKILL.md", "programs/*.json")


def work_root(repo: Path) -> Path:
    return repo / ".runs" / "bench"


def worktrees(repo: Path) -> list[Path]:
    lines = prov.git(repo, "worktree", "list", "--porcelain", check=False).splitlines()
    found = [Path(line.split(" ", 1)[1]) for line in lines if line.startswith("worktree ")]
    return found or [repo]


def program_info(tree: Path, problem: dict) -> dict:
    path = problem["programs"][0]
    doc = load_json(tree / path) or {}
    return {"id": doc.get("id"), "path": path, "doc": doc,
            "sha256": sha256_file(tree / path) if (tree / path).is_file() else None}


def resolve_run_dir(value: str | None, repo: Path, problem: dict) -> Path | None:
    candidates = [Path(value).expanduser()] if value else [w / problem["default_run_dir"] for w in worktrees(repo)]
    for candidate in candidates:
        if candidate.is_dir():
            return candidate.resolve()
    return None


def gather_sessions(repo: Path, pins: list[str], infer: bool, framework: str, window) -> list[dict]:
    bad = [p for p in pins if not p.startswith(("codex:", "claude-code:"))]
    if bad:
        raise BenchError(f"Sessions are pinned as codex:<id> or claude-code:<id>; got {bad}")
    codex = [p.split(":", 1)[1] for p in pins if p.startswith("codex:")]
    claude = [p.split(":", 1)[1] for p in pins if p.startswith("claude-code:")]
    sessions = select_codex(worktrees(repo), codex, framework, window) if codex or infer else []
    for sid in claude:
        found, error = read_claude(sid)
        if error:  # missing telemetry leaves cost and context items unknown; it does not void the record
            print(f"bench: warning: {error}; session telemetry stays unknown", file=sys.stderr)
            continue
        sessions += found
    return sessions


def context(spec, prob, layout, repo, framework, output, sessions, *, snapshot=False, deep=False, hook=False,
            judgments=None, ladder=None, cache=None) -> Context:
    return Context(spec=spec, problem=prob, layout=layout, repo=repo, framework_commit=framework,
                   output_commit=output, program=program_info(layout.tree, prob),
                   telemetry=summarize(sessions) if sessions else {"available": False},
                   session_files=[s["file"] for s in sessions if s.get("file")], snapshot=snapshot, deep=deep,
                   hook=hook, judgments=judgments or {}, ladder_judged=ladder or {}, cache=cache or {})


def replacements(repo: Path, layout: Layout, work: Path) -> list[tuple[str, str]]:
    roots = [layout.tree, work] + ([layout.runs_base] if layout.runs_base else []) + worktrees(repo)
    pairs = []
    for root in roots:  # native separators on Windows, POSIX form everywhere
        pairs += [(str(root) + "/", ""), (str(root) + "\\", ""), (Path(root).as_posix() + "/", "")]
    return pairs + [(str(Path.home()), "~"), (Path.home().as_posix(), "~")]


def make_record(spec, prob, ctx: Context, computed: dict, *, kind: str, repo: Path, work: Path,
                sessions: list[dict], output: dict | None, assessment=None, trajectory=None, step=None) -> dict:
    framework_tree = ctx.layout.base or ctx.layout.tree
    info = prov.commit_info(repo, ctx.framework_commit)
    started_on = [s["git"]["branch"] for s in sessions if s["role"] == "lead" and s["git"].get("branch")
                  and (s["git"].get("commit") or "").startswith(ctx.framework_commit[:12])]
    framework = {"commit": ctx.framework_commit, "branch": (started_on or [info["branch"]])[0],
                 "committed_at": info["committed_at"],
                 "subject": info["subject"], "fingerprint": prov.fingerprint(framework_tree, spec["problems"]["framework_paths"])}
    if ctx.layout.base is not None:
        changed = prov.fingerprint(ctx.layout.tree, spec["problems"]["framework_paths"])["sha256"] != framework["fingerprint"]["sha256"]
        framework["framework_paths_changed_during_run"] = changed
    program = {"id": ctx.program["id"], "path": ctx.program["path"], "sha256": ctx.program["sha256"],
               "frozen_at_start": computed.get("program_frozen") == "pass"}
    run = {"dir": ctx.layout.run_label, "available": bool(ctx.layout.run_dir and ctx.layout.run_dir.is_dir()),
           "harness_runs": [{"name": r["name"], "backend": r["receipt"].get("backend"), "status": r["receipt"].get("status"),
                             "planned_cost_units": r["receipt"].get("planned_cost_units"),
                             "attempted_cost_units": r["receipt"].get("attempted_cost_units")} for r in ctx.runs]}
    limitations = []
    if not sessions:
        limitations.append("No session telemetry selected; cost, context and human-turn items are unknown.")
    if any(s.get("selection") == "inferred" for s in sessions):
        limitations.append("Sessions were inferred from cwd, start commit and time window; verify the selection.")
    return build(spec=spec, problem=prob, computed=computed, kind=kind, created_at=now(), framework=framework,
                 output=output, program=program, run=run, sessions=sessions, telemetry=ctx.telemetry,
                 replacements=replacements(repo, ctx.layout, work), assessment=assessment,
                 trajectory=trajectory, step=step, limitations=limitations)


def summary(computed: dict) -> str:
    lines = []
    for metric_id, entry in computed["metrics"].items():
        score = "" if entry["score"] is None else f"{entry['score']:5.1f}"
        coverage = f"  coverage {entry['coverage']:.2f}" if entry.get("coverage") not in (None, 1.0) else ""
        lines.append(f"{metric_id} {entry['name']:<22} {entry['status']:<8} {score}{coverage}")
    lines += [f"{gate} {value['status']:<8} {'; '.join(value.get('notes', []))[:120]}" for gate, value in computed["gates"].items()]
    return "\n".join(lines)


def collected(work: Path) -> tuple[dict, list[dict]]:
    state = load_json(work / "collect.json")
    if not state:
        raise BenchError(f"No collection at {work}; run collect first")
    return state, load_json(work / "sessions.json") or []


def layout_for(state: dict, prob: dict, work: Path) -> Layout:
    return Layout(tree=work / "tree", workspace=prob["workspace"],
                  run_dir=Path(state["run_dir"]) if state.get("run_dir") else None,
                  base=work / "base" if (work / "base").is_dir() else None)


def trajectory(work: Path) -> list[dict]:
    points = []
    for path in sorted((work / "snapshots").glob("*.json")):
        snap = load_json(path) or {}
        points.append({"created_at": snap.get("created_at"), "step": snap.get("step"),
                       "output": (snap.get("provenance") or {}).get("output"),
                       "scores": {k: v.get("score") for k, v in (snap.get("metrics") or {}).items()},
                       "statuses": {k: v.get("status") for k, v in (snap.get("metrics") or {}).items()}})
    return points


# --- commands ------------------------------------------------------------------------------------

def cmd_collect(args) -> int:
    spec = load_spec()
    prob = find_problem(spec, args.problem)
    repo = prov.toplevel(Path(args.repo).resolve() if args.repo else Path.cwd())
    start = load_json(work_root(repo) / args.key / "start.json") if args.key else None
    output = prov.resolve(repo, args.commit)
    framework = prov.resolve(repo, args.framework_commit or (start or {}).get("framework_commit") or output)
    key = args.key or f"{prob['id']}-{framework[:7]}-{output[:7]}"
    work = work_root(repo) / key
    work.mkdir(parents=True, exist_ok=True)
    prov.materialize(repo, output, work / "tree")
    if framework != output:
        prov.materialize(repo, framework, work / "base")
    run_dir = resolve_run_dir(args.run_dir or (start or {}).get("run_dir"), repo, prob)
    out_info = prov.commit_info(repo, output)
    window = (epoch((start or {}).get("started_at")), epoch(out_info["committed_at"]))
    pins = args.session or (start or {}).get("sessions") or []
    sessions = gather_sessions(repo, pins, args.infer_sessions, framework, window)
    state = {"problem": prob["id"], "repo": str(repo), "framework": framework, "output": output,
             "run_dir": str(run_dir) if run_dir else None, "deep": args.deep, "key": key, "pins": pins,
             "infer": args.infer_sessions, "output_info": out_info}
    (work / "collect.json").write_text(json.dumps(state, indent=1))
    (work / "sessions.json").write_text(json.dumps(sessions, indent=1))
    ctx = context(spec, prob, layout_for(state, prob, work), repo, framework, output, sessions, deep=args.deep,
                  cache=load_json(work / "cache.json"))
    computed = compute(ctx)
    (work / "cache.json").write_text(json.dumps(ctx.cache, indent=1))
    packet = judge_packet(key=key, problem=prob, program=ctx.program, computed=computed, spec=spec,
                          tree=ctx.layout.tree, run_dir=run_dir, author_sessions=[s["id"] for s in sessions],
                          deep=args.deep, out=work / "judgments.json")
    (work / "judge-packet.json").write_text(json.dumps(packet, indent=1))
    audit = {"schema": "yambench.audit-packet/1", "key": key, "tree": str(ctx.layout.tree),
             "run_dir": packet["run_dir"], "gates": computed["gates"], "flags": computed["flags"],
             "judgments": str(work / "judgments.json"), "author_sessions": packet["author_sessions"],
             "write_to": str(work / "audit.json"),
             "answer_shape": {"auditor": {"agent": "bench-auditor", "session": "<id>", "model": "<model>"},
                              "gates": {"G1": {"status": "pass", "rationale": "...", "evidence": ["..."]}},
                              "disputes": [{"metric": "B05", "detail": "..."}]}}
    (work / "audit-packet.json").write_text(json.dumps(audit, indent=1))
    print(summary(computed))
    print(f"\nkey: {key}\njudge packet: {work / 'judge-packet.json'} ({len(packet['requests'])} metric request(s), "
          f"{len(packet['ladder'])} milestone(s))\naudit packet: {work / 'audit-packet.json'}")
    return 0


def cmd_finalize(args) -> int:
    spec = load_spec()
    repo = prov.toplevel(Path(args.repo).resolve() if args.repo else Path.cwd())
    work = work_root(repo) / args.key
    state, sessions = collected(work)
    prob = find_problem(spec, state["problem"])
    packet = load_json(work / "judge-packet.json")
    judgments = load_json(Path(args.judgments))
    if judgments is None:
        raise BenchError(f"Cannot read judgments {args.judgments}")
    metric_judgments, ladder_judgments, assessor = apply_judgments(judgments, packet, spec)
    ctx = context(spec, prob, layout_for(state, prob, work), repo, state["framework"], state["output"], sessions,
                  deep=state["deep"], judgments=metric_judgments, ladder=ladder_judgments,
                  cache=load_json(work / "cache.json"))
    computed = compute(ctx)
    audit = load_json(Path(args.audit)) if args.audit else None
    if args.audit and audit is None:
        raise BenchError(f"Cannot read audit {args.audit}")
    computed["gates"], auditor, disputes = apply_audit(computed["gates"], audit, packet["author_sessions"])
    authors = {family(s.get("model")) for s in sessions if s["role"] != "overhead"}
    assessment = {"packet_sha256": sha256_file(work / "judge-packet.json"), "assessor": assessor, "auditor": auditor,
                  "assessor_not_author": True, "same_model_family": family(assessor["model"]) in authors,
                  "disagreements": disputes,
                  "unanswered": [r["metric"] for r in packet["requests"] if r["metric"] not in metric_judgments]}
    info = state["output_info"]
    output = {"commit": state["output"], "branch": info["branch"], "committed_at": info["committed_at"],
              "subject": info["subject"]}
    record = make_record(spec, prob, ctx, computed, kind="final", repo=repo, work=work, sessions=sessions,
                         output=output, assessment=assessment, trajectory=trajectory(work))
    validate(record, spec)
    path = write(record, Path(args.out_dir) if args.out_dir else RECORDS_DIR)
    print(summary(computed))
    print(f"\nrecord: {path}")
    return 0


def cmd_start(args) -> int:
    spec = load_spec()
    prob = find_problem(spec, args.problem)
    repo = prov.toplevel(Path.cwd())
    state = prov.working_state(repo)
    stamp = now()
    key = f"{prob['id']}-{state['commit'][:7]}-{stamp.replace(':', '').replace('-', '')}"
    run_dir = resolve_run_dir(args.run_dir, repo, prob)
    start = {"key": key, "problem": prob["id"], "framework_commit": state["commit"], "framework_dirty": state["dirty"],
             "branch": state["branch"], "started_at": stamp, "run_dir": str(run_dir) if run_dir else args.run_dir,
             "sessions": args.session or [], "declared": {"client": args.client, "model": args.model, "effort": args.effort}}
    work = work_root(repo) / key
    work.mkdir(parents=True, exist_ok=True)
    (work / "start.json").write_text(json.dumps(start, indent=1))
    (work_root(repo) / "ARMED").write_text(json.dumps(start, indent=1))
    print(f"armed {key} at {state['commit'][:10]}{' (dirty)' if state['dirty'] else ''}")
    return 0


def cmd_stop(args) -> int:
    repo = prov.toplevel(Path.cwd())
    armed = work_root(repo) / "ARMED"
    if armed.is_file():
        key = (load_json(armed) or {}).get("key")
        armed.unlink()
        print(f"disarmed {key}; collect with: bench.py collect --key {key} --problem <id> --commit HEAD")
    return 0


def cmd_snapshot(args) -> int:
    repo = prov.toplevel(Path.cwd())
    armed = load_json(work_root(repo) / "ARMED")
    if not armed:
        if not args.quiet:
            print("no armed run; use start first")
        return 0
    if args.hook:
        try:
            event = json.loads(sys.stdin.read() or "{}")
        except json.JSONDecodeError:
            event = {}
        session, pinned = event.get("session_id") or "", [p.split(":", 1)[-1] for p in armed.get("sessions", [])]
        if pinned and not any(session.startswith(p) or p.startswith(session) for p in pinned if session):
            return 0
    work = work_root(repo) / armed["key"]
    state = prov.working_state(repo)
    marker = f"{state['commit']}:{state['status_sha256']}"
    last = work / "last-snapshot"
    if args.hook and last.is_file() and last.read_text() == marker:
        return 0
    spec = load_spec()
    prob = find_problem(spec, armed["problem"])
    base = prov.materialize(repo, armed["framework_commit"], work / "base")
    layout = Layout(tree=repo, workspace=prob["workspace"],
                    run_dir=Path(armed["run_dir"]) if armed.get("run_dir") else None, base=base)
    sessions = [] if args.hook else gather_sessions(repo, armed.get("sessions", []), False, armed["framework_commit"], (None, None))
    ctx = context(spec, prob, layout, repo, armed["framework_commit"], state["commit"], sessions,
                  snapshot=True, hook=args.hook)
    computed = compute(ctx)
    record = make_record(spec, prob, ctx, computed, kind="snapshot", repo=repo, work=work, sessions=sessions,
                         output={**state, "working_tree": True}, step=args.step)
    validate(record, spec)
    snaps = work / "snapshots"
    snaps.mkdir(exist_ok=True)
    path = snaps / f"{len(list(snaps.glob('*.json'))) + 1:03d}.json"
    path.write_text(json.dumps(record, indent=1) + "\n")
    last.write_text(marker)
    if not args.quiet:
        print(summary(computed))
        print(f"\nsnapshot: {path}")
    return 0


def math_domain_files(repo: Path) -> list[Path]:
    files = [repo / name for name in MATH_DOMAIN]
    for pattern in MATH_GLOBS:
        files += sorted(repo.glob(pattern))
    return [p for p in files if p.is_file()]


def cmd_validate(args) -> int:
    spec = load_spec()
    records = load_all()
    for record in records:
        validate(record, spec)
    repo = prov.toplevel(Path.cwd())
    leaks = [p.relative_to(repo).as_posix() for p in math_domain_files(repo) if CANARY_RE.search(p.read_text(encoding="utf-8"))]
    if leaks:
        raise BenchError(f"Benchmark canaries leaked into research files: {leaks}")
    print(f"valid: {len(spec['metrics']['metrics'])} metrics, {len(spec['gates']['gates'])} gates, "
          f"{len(spec['problems']['problems'])} problem(s), {len(records)} record(s); no canary in research files")
    return 0


def find_record(value: str) -> dict:
    path = Path(value)
    if not path.is_file():
        matches = sorted(RECORDS_DIR.glob(f"*{value}*.json"))
        if len(matches) != 1:
            raise BenchError(f"{value!r} matches {len(matches)} records")
        path = matches[0]
    return json.loads(path.read_text(encoding="utf-8"))


def cmd_compare(args) -> int:
    result = compare(find_record(args.baseline), find_record(args.candidate), args.allow_spec_drift)
    print(json.dumps(result, indent=2))
    return 0


def cmd_relevance(args) -> int:
    report = relevance(load_all(), load_spec())
    print(json.dumps(report, indent=2) if args.json else relevance_text(report))
    return 0


def all_records(include_snapshots: bool) -> list[dict]:
    records = load_all()
    if include_snapshots:
        repo = prov.toplevel(Path.cwd())
        records += [json.loads(p.read_text()) for p in sorted(work_root(repo).glob("*/snapshots/*.json"))]
    return records


def cmd_dashboard(args) -> int:
    spec = load_spec()
    repo = prov.toplevel(Path.cwd())
    out = Path(args.out) if args.out else work_root(repo) / "dashboard.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(render(all_records(args.snapshots), spec), encoding="utf-8")
    print(out)
    return 0


def cmd_export(args) -> int:
    """Write one JSON file per dataset plus the page, ready to upload to the published dashboard."""
    exported = export_artifact(all_records(args.snapshots), load_spec())
    repo = prov.toplevel(Path.cwd())
    out = Path(args.out_dir) if args.out_dir else work_root(repo) / "artifact-export"
    out.mkdir(parents=True, exist_ok=True)
    for name, rows in exported["datasets"].items():
        (out / f"{name}.json").write_text(json.dumps(rows, ensure_ascii=False) + "\n", encoding="utf-8")
    (out / "index.html").write_text(exported["page"], encoding="utf-8")
    (out / "index.doc.json").write_text(json.dumps({"text": exported["page"]}, ensure_ascii=False), encoding="utf-8")
    manifest = {name: {"title": title, "description": description, "file": f"{name}.json",
                       "rows": len(exported["datasets"][name])}
                for name, (title, description) in exported["descriptions"].items()}
    (out / "manifest.json").write_text(json.dumps(manifest, indent=1) + "\n", encoding="utf-8")
    print(out)
    return 0


def cmd_sessions(args) -> int:
    repo = prov.toplevel(Path.cwd())
    commit = prov.resolve(repo, args.framework_commit) if args.framework_commit else None
    for path, meta in codex_candidates(worktrees(repo)):
        role, name = codex_role(meta.get("source"))
        git = meta.get("git") or {}
        if commit and not (git.get("commit_hash") or "").startswith(commit[:12]):
            continue
        print(f"codex:{(meta.get('id') or '')[:13]}  {role:<8} {name or '':<24} {meta.get('timestamp', '')[:19]}  "
              f"{git.get('branch')}@{(git.get('commit_hash') or '')[:8]}")
    return 0


def parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(prog="bench.py", description=__doc__)
    sub = ap.add_subparsers(dest="command", required=True)
    p = sub.add_parser("collect", help="score a commit: computed metrics plus a judge packet")
    p.add_argument("--problem", required=True)
    p.add_argument("--commit", required=True, help="output commit holding the run's results")
    p.add_argument("--framework-commit", help="framework version under test (default: start record or --commit)")
    p.add_argument("--run-dir", help="ignored run directory (absolute path allowed)")
    p.add_argument("--repo")
    p.add_argument("--key")
    p.add_argument("--session", action="append", help="pin a session: codex:<id> or claude-code:<id>")
    p.add_argument("--infer-sessions", action="store_true", help="accept Codex sessions inferred by cwd, commit, window")
    p.add_argument("--deep", action="store_true", help="also rerun unit tests and declared reproduction commands")
    p.set_defaults(fn=cmd_collect)
    p = sub.add_parser("finalize", help="merge independent judgments and audit into a tracked record")
    p.add_argument("--key", required=True)
    p.add_argument("--judgments", required=True)
    p.add_argument("--audit")
    p.add_argument("--repo")
    p.add_argument("--out-dir")
    p.set_defaults(fn=cmd_finalize)
    p = sub.add_parser("start", help="arm a live run for snapshots")
    p.add_argument("--problem", required=True)
    p.add_argument("--run-dir")
    p.add_argument("--session", action="append")
    p.add_argument("--client")
    p.add_argument("--model")
    p.add_argument("--effort")
    p.set_defaults(fn=cmd_start)
    p = sub.add_parser("snapshot", help="computed metrics on the working tree of the armed run")
    p.add_argument("--step")
    p.add_argument("--hook", action="store_true")
    p.add_argument("--quiet", action="store_true")
    p.set_defaults(fn=cmd_snapshot)
    p = sub.add_parser("stop", help="disarm the live run")
    p.set_defaults(fn=cmd_stop)
    p = sub.add_parser("validate", help="validate spec, records and canary isolation")
    p.set_defaults(fn=cmd_validate)
    p = sub.add_parser("compare", help="axis-by-axis comparison of two records")
    p.add_argument("baseline")
    p.add_argument("candidate")
    p.add_argument("--allow-spec-drift", action="store_true")
    p.set_defaults(fn=cmd_compare)
    p = sub.add_parser("relevance", help="question the axes: saturation, unmeasured axes, hygiene-dominated radars, review due")
    p.add_argument("--json", action="store_true")
    p.set_defaults(fn=cmd_relevance)
    p = sub.add_parser("dashboard", help="render the radar dashboard locally")
    p.add_argument("--out")
    p.add_argument("--snapshots", action="store_true")
    p.set_defaults(fn=cmd_dashboard)
    p = sub.add_parser("export-artifact", help="dataset files and page for the published dashboard")
    p.add_argument("--out-dir")
    p.add_argument("--snapshots", action="store_true")
    p.set_defaults(fn=cmd_export)
    p = sub.add_parser("sessions", help="list Codex sessions recorded in this repository")
    p.add_argument("--framework-commit")
    p.set_defaults(fn=cmd_sessions)
    return ap


def main(argv: list[str] | None = None) -> int:
    args = parser().parse_args(argv)
    try:
        return args.fn(args)
    except BenchError as error:
        print(f"bench: {error}", file=sys.stderr)
        return 2
