from __future__ import annotations

import copy
import hashlib
import io
import json
import subprocess
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from yambench import BenchError  # noqa: E402
from yambench import provenance  # noqa: E402
from yambench.cli import main  # noqa: E402
from yambench.collectors import Layout, hash_bindings, verify_bindings  # noqa: E402
from yambench.compare import compare  # noqa: E402
from yambench.dashboard import export_artifact, render  # noqa: E402
from yambench.ladder import CheckContext, evaluate, ladder  # noqa: E402
from yambench.metrics import Context, compute, gate_g4  # noqa: E402
from yambench.records import apply_audit, apply_judgments, validate  # noqa: E402
from yambench.spec import ANCHORS, canaries, load_spec, validate_spec  # noqa: E402
from yambench.telemetry import classify_turn, modifies_files, read_claude, select_codex, summarize  # noqa: E402

BENCH = Path(__file__).resolve().parents[1]
REPO = BENCH.parents[1]
MAIN_RUN = Path.home() / "YambaCode" / "yamba-ai-math" / ".runs" / "h3-unimodality"
WS = "research/ws"


def sha(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()


def write(root: Path, rel: str, content) -> Path:
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content if isinstance(content, str) else json.dumps(content), encoding="utf-8")
    return path


def problem(**overrides) -> dict:
    entry = {
        "id": "toy", "title": "Toy problem", "statement_ref": f"{WS}/README.md", "workspace": WS,
        "programs": ["programs/toy.json"], "formal_targets": [], "registered_after_run": False,
        "reference_budget": {"effective_tokens": 1000},
        "closest_work": [{"key": "A", "match": "1111.0001"}, {"key": "B", "match": "2222.0002"}],
        "novelty_label": {"file": "{ws}/evidence.json", "path": ["novelty_status"]},
        "findings": [{"name": "witness", "check": {"kind": "json_path", "file": "{ws}/evidence.json",
                                                    "path": ["witness"], "op": "any_nonempty"}}],
        "continuity": {"next_step": {"kind": "json_path", "file": "{ws}/evidence.json", "path": ["next_step"],
                                     "op": "any_nonempty"}},
        "ladder": {
            "branches": {"prove": ["frozen", "finite", "argument"], "refute": ["frozen", "counterexample"]},
            "milestones": {
                "frozen": {"all": [{"kind": "sha256_matches", "path": "{ws}/protocol.json",
                                    "recorded": {"file": "{ws}/evidence.json", "path": ["protocol_sha256"]}}]},
                "finite": {"all": [{"kind": "json_path", "file": "{ws}/evidence.json", "path": ["cases", "*", "status"],
                                    "op": "all_eq", "value": "complete"}]},
                "argument": {"all": [{"kind": "judged"}]},
                "counterexample": {"all": [{"kind": "file_exists", "path": "{run}/counterexample.json"}, {"kind": "judged"}]},
            },
        },
    }
    entry.update(overrides)
    return entry


def tree(root: Path, cases=("complete", "complete"), witness=None) -> Path:
    protocol = json.dumps({"frozen": True})
    write(root, f"{WS}/protocol.json", protocol)
    write(root, f"{WS}/evidence.json", {"protocol_sha256": sha(protocol), "cases": [{"status": s} for s in cases],
                                        "novelty_status": "unverified", "witness": witness, "next_step": "Prove L1.",
                                        "source_stable": True,
                                        "report": {"path": f"{WS}/protocol.json", "sha256": sha(protocol)}})
    write(root, f"{WS}/review-r1.md", "# Review\n\nReviewer: separate critic. Bound to " + "a" * 64 +
          ".\n\n**Verdict: supported finite evidence; universal theorem incomplete.**\n")
    write(root, f"{WS}/README.md", "Cites arXiv 1111.0001 and 2222.0002.\n")
    write(root, "references/reading-list.md",
          "| ID | Source | Inspection | Use |\n| --- | --- | --- | --- |\n"
          "| R001 | [A](https://arxiv.org/abs/1111.0001) | T; partial | x |\n"
          "| R002 | [B](https://arxiv.org/abs/2222.0002) | A | x |\n")
    write(root, "programs/toy.json", {"id": "T1", "rounds": 1, "constraints": {"max_agents": 2, "max_cost_units": 4},
                                      "deliverables": ["d"], "success_criteria": ["s"]})
    return root


def spec_with(entry: dict) -> dict:
    spec = copy.deepcopy(load_spec())
    spec["problems"]["problems"] = [entry]
    return spec


def context(root: Path, entry=None, telemetry=None, **kwargs) -> Context:
    entry = entry or problem()
    spec = spec_with(entry)
    return Context(spec=spec, problem=entry, layout=Layout(tree=root, workspace=WS, run_dir=kwargs.pop("run_dir", None)),
                   repo=root, framework_commit="f" * 40, output_commit=None,
                   program={"id": "T1", "path": "programs/toy.json", "sha256": None,
                            "doc": json.loads((root / "programs/toy.json").read_text())},
                   telemetry=telemetry or {"available": False}, **kwargs)


def codex_rollout(root: Path, name: str, meta: dict, records: list[dict]) -> Path:
    lines = [{"timestamp": meta.get("timestamp", "2026-10-23T21:00:00Z"), "type": "session_meta", "payload": meta}]
    lines += records
    return write(root, f"2026/10/23/rollout-{name}.jsonl", "\n".join(json.dumps(line) for line in lines) + "\n")


def token_count(input_tokens, cached, output, window=1000):
    return {"timestamp": "2026-10-23T21:05:00Z", "type": "event_msg", "payload": {"type": "token_count", "info": {
        "model_context_window": window, "last_token_usage": {"input_tokens": input_tokens // 4},
        "total_token_usage": {"input_tokens": input_tokens, "cached_input_tokens": cached,
                              "cache_write_input_tokens": 0, "output_tokens": output, "reasoning_output_tokens": 1}}}}


def user(text):
    return {"timestamp": "2026-10-23T21:01:00Z", "type": "response_item",
            "payload": {"type": "message", "role": "user", "content": [{"type": "input_text", "text": text}]}}


class SpecTests(unittest.TestCase):
    def test_repository_spec_has_twelve_metrics_and_canaried_rubrics(self):
        spec = load_spec()
        self.assertEqual(len(spec["metrics"]["metrics"]), 12)
        self.assertGreaterEqual(len(canaries(spec)), 7)

    def test_rubric_without_canary_is_rejected(self):
        spec = copy.deepcopy(load_spec())
        spec["rubrics"]["B03.md"] = "# B03 without a canary\n"
        with self.assertRaises(BenchError):
            validate_spec(spec)

    def test_missing_metric_is_rejected(self):
        spec = copy.deepcopy(load_spec())
        spec["metrics"]["metrics"].pop()
        with self.assertRaises(BenchError):
            validate_spec(spec)

    def test_spec_selects_twelve_distinct_known_axes_and_schedules_its_own_review(self):
        ids = [m["id"] for m in load_spec()["metrics"]["metrics"]]
        self.assertTrue({"B13", "B14"} <= set(ids) and not {"B04", "B10"} & set(ids))
        unknown, duplicate, unreviewed = (copy.deepcopy(load_spec()) for _ in range(3))
        unknown["metrics"]["metrics"][0]["id"] = "B99"
        duplicate["metrics"]["metrics"][1]["id"] = duplicate["metrics"]["metrics"][0]["id"]
        del unreviewed["metrics"]["relevance_review"]
        for spec in (unknown, duplicate, unreviewed):
            with self.assertRaises(BenchError):
                validate_spec(spec)


class LadderTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def check_context(self, run_dir=None, snapshot=False, judged=None):
        return CheckContext(layout=Layout(tree=self.root, workspace=WS, run_dir=run_dir), problem=problem(),
                            registry={"verification_files": [], "allowed_axioms": []}, snapshot=snapshot,
                            judged=judged or {})

    def test_depth_is_contiguous_and_stops_at_pending_judgment(self):
        tree(self.root)
        result = ladder(self.check_context())
        self.assertEqual(result["branches"]["prove"]["depth"], 2)
        self.assertEqual(result["branches"]["prove"]["stopped_result"], "pending")
        self.assertEqual(result["frontier_judgments"], ["argument"])

    def test_skipped_milestone_does_not_count(self):
        tree(self.root, cases=("complete", "capped"))
        result = ladder(self.check_context(judged={"argument": True}))
        self.assertEqual(result["branches"]["prove"]["depth"], 1)

    def test_unregistered_formal_rung_is_not_applicable(self):
        tree(self.root)
        entry = problem()
        entry["ladder"]["branches"]["prove"] = ["frozen", "finite", "lean"]
        entry["ladder"]["milestones"]["lean"] = {"all": [{"kind": "verification_declaration"}]}
        ctx = CheckContext(layout=Layout(tree=self.root, workspace=WS, run_dir=None), problem=entry,
                           registry={"verification_files": [], "allowed_axioms": []})
        prove = ladder(ctx)["branches"]["prove"]
        self.assertEqual((prove["depth"], prove["of"], prove["not_applicable"]), (2, 2, ["lean"]))

    def test_refute_branch_can_win(self):
        tree(self.root, cases=("capped",))
        run = self.root / "run"
        write(run, "counterexample.json", {"n": 7})
        result = ladder(self.check_context(run_dir=run, judged={"counterexample": True}))
        self.assertEqual(result["best"], "refute")
        self.assertEqual(result["branches"]["refute"]["depth"], 2)

    def test_hash_mismatch_fails_and_missing_run_file_is_unknown(self):
        tree(self.root)
        (self.root / WS / "protocol.json").write_text("{\"edited\": true}")
        ctx = self.check_context(run_dir=self.root / "absent-run")
        frozen = evaluate(problem()["ladder"]["milestones"]["frozen"]["all"][0], ctx)
        self.assertEqual(frozen["result"], "fail")
        missing = evaluate({"kind": "file_exists", "path": "{run}/counterexample.json"}, ctx)
        self.assertEqual(missing["result"], "unknown")


class BindingTests(unittest.TestCase):
    def test_bindings_resolve_tree_and_run_snapshot_copies(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            write(root, "tree/a.py", "new")
            write(root, ".runs/r/r1-source/a.py", "old")
            write(root, ".runs/r/log.txt", "ok")
            doc = {"sources": {"a.py": sha("old")}, "checks": [{"log": ".runs/r/log.txt", "sha256": sha("ok")}],
                   "other": {"path": "missing.txt", "sha256": sha("x")}}
            layout = Layout(tree=root / "tree", workspace=WS, run_dir=root / ".runs" / "r")
            results = {b["path"]: b["result"] for b in verify_bindings(hash_bindings(doc, "ws/e.json"), layout)}
            self.assertEqual(results, {"a.py": "pass", ".runs/r/log.txt": "pass", "missing.txt": "unknown"})


class MetricTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = tree(Path(self.temp.name))

    def test_snapshot_leaves_judged_metrics_pending_and_scores_computed_ones(self):
        computed = compute(context(self.root, snapshot=True))
        metrics = computed["metrics"]
        self.assertEqual(metrics["B01"]["score"], 66.7)
        self.assertEqual(metrics["B02"]["status"], "n/a")
        self.assertEqual(metrics["B03"]["status"], "scored")  # empty inventory is an objective zero
        self.assertEqual(metrics["B03"]["score"], 0.0)
        self.assertEqual(metrics["B05"]["status"], "pending")
        self.assertIn("novelty_label_honest", metrics["B08"]["raw"]["pending"])

    def test_resource_efficiency_unknown_without_tokens_and_na_without_progress(self):
        computed = compute(context(self.root))
        self.assertEqual(computed["metrics"]["B09"]["status"], "unknown")
        telemetry = {"available": True, "effective_tokens": 500, "tokens": {}, "working": 1}
        ctx = context(self.root, telemetry=telemetry)
        ctx.layout.base = self.root  # same tree: no new depth, and B03 scores zero
        self.assertEqual(compute(ctx)["metrics"]["B09"]["status"], "n/a")

    def test_found_witness_needs_judgment_then_takes_the_anchor(self):
        write(self.root, f"{WS}/evidence.json", {**json.loads((self.root / WS / "evidence.json").read_text()),
                                                  "witness": {"n": 7}})
        self.assertEqual(compute(context(self.root))["metrics"]["B03"]["status"], "pending")
        judged = compute(context(self.root, judgments={"B03": {"anchor": 50, "rationale": "r", "evidence": ["e"]}}))
        self.assertEqual(judged["metrics"]["B03"]["score"], 50.0)

    def test_discovery_axes_need_an_inventory_and_novelty_needs_inspected_closest_work(self):
        snapshot = compute(context(self.root, snapshot=True))["metrics"]
        self.assertEqual((snapshot["B13"]["score"], snapshot["B14"]["score"]), (0.0, 0.0))  # nothing to judge
        probe = [{"name": "witness", "check": {"kind": "json_path", "file": "{ws}/evidence.json",
                                               "path": ["next_step"], "op": "any_nonempty"}}]
        entry = problem(contribution_probes=probe, idea_probes=probe)
        self.assertEqual(compute(context(self.root, entry))["metrics"]["B13"]["status"], "pending")
        anchor = {"anchor": 75, "rationale": "r", "evidence": ["e"]}
        judged = compute(context(self.root, entry, judgments={"B13": anchor, "B14": anchor}))["metrics"]
        self.assertEqual(judged["B13"]["score"], 50.0)  # closest work B is inspected only at level A
        self.assertTrue(judged["B13"]["raw"]["capped_at_50"])
        self.assertEqual(judged["B14"]["score"], 75.0)

    def test_unverifiable_program_freeze_does_not_cap_contract_fulfilment(self):
        from yambench.metrics import b04
        judgments = {"B04": {"anchor": 100, "rationale": "r", "evidence": ["e"]}}
        found = b04({"mode": "K/J"}, context(self.root, judgments=judgments), {})
        self.assertEqual((found["score"], found["raw"]["capped_at_50"]), (100.0, False))

    def test_canary_in_worker_packet_fails_g4(self):
        token = canaries(load_spec())[0]
        ctx = context(self.root)
        ctx.runs = [{"packets": [write(self.root, "run/packets/s.json", {"text": token})]}]
        self.assertEqual(gate_g4(ctx)["status"], "fail")
        ctx.runs = []
        self.assertEqual(gate_g4(ctx)["status"], "pass")

    def test_g3_reviews_more_working_threads_than_max_agents(self):
        telemetry = {"available": True, "working": 3, "child_names": ["/root/a", "/root/b"]}
        self.assertEqual(compute(context(self.root, telemetry=telemetry))["gates"]["G3"]["status"], "review")


class TelemetryTests(unittest.TestCase):
    def test_codex_selection_counts_children_overhead_and_uncached_input(self):
        with tempfile.TemporaryDirectory() as temp:
            root, repo = Path(temp) / "sessions", Path(temp) / "repo"
            repo.mkdir()
            git = {"commit_hash": "c" * 40, "branch": "main"}
            lead = {"id": "lead-1", "cwd": str(repo), "source": "vscode", "git": git, "timestamp": "2026-10-23T21:00:00Z"}
            codex_rollout(root, "lead", lead, [
                {"type": "turn_context", "payload": {"model": "gpt-x", "effort": "high"}},
                user("# AGENTS.md instructions for repo"), user("Begin the investigation."),
                user("PLEASE IMPLEMENT THIS PLAN: ..."), user("Are you using the harness?"),
                token_count(1000, 600, 50)])
            codex_rollout(root, "child", {**lead, "id": "child-1", "parent_thread_id": "lead-1",
                                          "source": {"subagent": {"thread_spawn": {"agent_path": "/root/critic"}}}},
                          [token_count(200, 100, 10)])
            codex_rollout(root, "guardian", {**lead, "id": "g-1", "parent_thread_id": "lead-1",
                                             "source": {"subagent": {"other": "guardian"}}}, [token_count(30, 0, 1)])
            codex_rollout(root, "elsewhere", {**lead, "id": "other-1", "cwd": "/elsewhere"}, [token_count(9, 0, 9)])
            sessions = select_codex([repo], ["lead"], None, (None, None), root)
            self.assertEqual(sorted(s["id"] for s in sessions), ["child-1", "g-1", "lead-1"])
            summary = summarize(sessions)
            self.assertEqual(summary["tokens"]["uncached_input"], 400 + 100)
            self.assertEqual(summary["effective_tokens"], 500 + 60)
            self.assertEqual(summary["overhead"], 1)
            self.assertEqual(summary["human_turns"], {"approval": 1, "steering": 1})
            self.assertEqual(summary["child_names"], ["/root/critic"])

    def test_inference_requires_the_framework_commit(self):
        with tempfile.TemporaryDirectory() as temp:
            root, repo = Path(temp) / "sessions", Path(temp) / "repo"
            repo.mkdir()
            meta = {"id": "lead-2", "cwd": str(repo), "source": "vscode", "timestamp": "2026-10-23T21:00:00Z",
                    "git": {"commit_hash": "d" * 40}}
            codex_rollout(root, "lead", meta, [token_count(10, 0, 1)])
            self.assertEqual(select_codex([repo], [], "e" * 40, (None, None), root), [])
            self.assertEqual(len(select_codex([repo], [], "d" * 40, (None, None), root)), 1)

    def test_orientation_heuristic_ignores_arrow_functions(self):
        self.assertFalse(modifies_files("exec", 'tools.exec_command({cmd:"cat a.md"}).then(r => r)'))
        self.assertFalse(modifies_files("exec", 'tools.exec_command({cmd:"ls 2>/dev/null > /dev/null"})'))
        self.assertTrue(modifies_files("exec", 'tools.apply_patch("*** Begin Patch")'))
        self.assertTrue(modifies_files("exec", 'tools.exec_command({cmd:"python3 x.py > out/r.json"})'))

    def test_turn_classification(self):
        self.assertEqual(classify_turn("excellent continue! you can do it"), "approval")
        self.assertEqual(classify_turn("Hoe are things going?"), "status")
        self.assertEqual(classify_turn("No, that is the wrong file"), "correction")
        self.assertEqual(classify_turn("Are you utilising the harness?"), "steering")

    def test_claude_sessions_come_from_the_recorder(self):
        with tempfile.TemporaryDirectory() as temp:
            recorder = write(Path(temp), "recorder.py", "import json\nprint(json.dumps(" + repr({
                "session": "s1", "cwd": "/r", "agents": [
                    {"id": "main", "type": "orchestrator", "model": "claude-x", "effort": "high",
                     "tokens": {"input": 5, "cache_write": 10, "cache_read": 100, "output": 7, "thinking": 2},
                     "tools": 3, "tool_errors": 0, "ctx_peak_pct": 40.0, "compactions": 0, "window": 1000}],
                "events": [{"agent": "main", "kind": "prompt", "source": "human", "text": "start"},
                           {"agent": "main", "kind": "tool.call", "tool": "Read", "detail": "a"},
                           {"agent": "main", "kind": "tool.call", "tool": "Read", "detail": "a"},
                           {"agent": "main", "kind": "tool.call", "tool": "Edit", "detail": "a"},
                           {"agent": "main", "kind": "prompt", "source": "human", "text": "stop, that is wrong"}]}) + "))\n")
            sessions, error = read_claude("s1", recorder)
            self.assertIsNone(error)
            summary = summarize(sessions)
            self.assertEqual(summary["effective_tokens"], 22)
            self.assertEqual(summary["orientation_tool_calls"], 2)
            self.assertEqual(summary["redundant_read_ratio"], 0.5)
            self.assertEqual(summary["human_turns"], {"correction": 1})


class RecordTests(unittest.TestCase):
    def setUp(self):
        self.spec = load_spec()
        self.packet = {"author_sessions": ["lead-1"], "ladder": [{"milestone": "argument"}],
                       "requests": [{"metric": "B03", "type": "anchor"},
                                    {"metric": "B06", "type": "items", "items": ["independent_check"]}]}

    def judgments(self, **metrics):
        return {"assessor": {"session": "assessor-9", "model": "claude-x"},
                "metrics": metrics or {"B03": {"anchor": 50, "rationale": "r", "evidence": ["e"]}}}

    def test_author_cannot_assess_its_own_run(self):
        answer = self.judgments()
        answer["assessor"]["session"] = "lead-1"
        with self.assertRaises(BenchError):
            apply_judgments(answer, self.packet, self.spec)

    def test_off_anchor_scores_and_missing_evidence_are_rejected(self):
        with self.assertRaises(BenchError):
            apply_judgments(self.judgments(B03={"anchor": 60, "rationale": "r", "evidence": ["e"]}), self.packet, self.spec)
        with self.assertRaises(BenchError):
            apply_judgments(self.judgments(B03={"anchor": 50, "rationale": "r", "evidence": []}), self.packet, self.spec)
        with self.assertRaises(BenchError):
            apply_judgments(self.judgments(B06={"items": {"invented": True}, "rationale": "r", "evidence": ["e"]}),
                            self.packet, self.spec)

    def test_accepted_judgments_and_ladder(self):
        answer = self.judgments(B06={"items": {"independent_check": [True, False]}, "rationale": "r", "evidence": ["e"]})
        answer["ladder"] = {"argument": {"met": False, "rationale": "finite only"}}
        metrics, ladder_judged, _ = apply_judgments(answer, self.packet, self.spec)
        self.assertEqual(ladder_judged, {"argument": False})
        self.assertIn("B06", metrics)

    def test_found_canary_cannot_be_overruled_by_the_auditor(self):
        gates = {g: {"status": "unknown"} for g in ("G1", "G2", "G3")} | {"G4": {"status": "fail"}}
        audit = {"auditor": {"session": "auditor-1"}, "gates": {"G4": {"status": "pass", "rationale": "fine"},
                                                                "G1": {"status": "pass", "rationale": "checked"}}}
        updated, _, _ = apply_audit(gates, audit, ["lead-1"])
        self.assertEqual(updated["G4"]["status"], "fail")
        self.assertEqual(updated["G1"]["status"], "pass")

    def test_unmetered_budget_gate_cannot_be_passed_on_self_reports(self):
        gates = {g: {"status": "unknown"} for g in ("G1", "G2", "G4")}
        gates["G3"] = {"status": "unknown", "evidence_missing": True, "notes": []}
        audit = {"auditor": {"session": "auditor-1"}, "gates": {"G3": {"status": "pass", "rationale": "records fit"}}}
        self.assertEqual(apply_audit(gates, audit, ["lead-1"])[0]["G3"]["status"], "unknown")
        audit["gates"]["G3"]["status"] = "review"
        self.assertEqual(apply_audit(gates, audit, ["lead-1"])[0]["G3"]["status"], "review")

    def test_record_validation_rules(self):
        record = minimal_record()
        validate(record, self.spec)
        broken = copy.deepcopy(record)
        broken["metrics"]["B01"].update(status="scored", score=None)
        with self.assertRaises(BenchError):
            validate(broken, self.spec)
        broken = copy.deepcopy(record)
        broken["metrics"]["B05"].update(status="scored", score=60.0)
        with self.assertRaises(BenchError):
            validate(broken, self.spec)
        broken = copy.deepcopy(record)
        broken["limitations"] = ["/Users/someone/private/path"]
        with self.assertRaises(BenchError):
            validate(broken, self.spec)
        broken = copy.deepcopy(record)
        broken["promotion_authorized"] = True
        with self.assertRaises(BenchError):
            validate(broken, self.spec)
        for leaked in ["C:\\Users\\someone\\dev", json.dumps("C:\\Users\\someone\\dev"), "c:/Users/someone/dev"]:
            broken = copy.deepcopy(record)
            broken["limitations"] = [leaked]
            with self.assertRaises(BenchError):
                validate(broken, self.spec)

    def test_record_under_the_current_spec_carries_its_axes(self):
        record = minimal_record()  # retired B04 and B10 are fine under an older spec
        validate(record, self.spec)
        record["spec"]["hashes"]["metrics.json"] = self.spec["hashes"]["metrics.json"]
        with self.assertRaises(BenchError):
            validate(record, self.spec)
        validate(current_record(self.spec), self.spec)


def minimal_record(problem_id="toy", scores=None, retrospective=False, gates=None) -> dict:
    scores = scores or {}
    metrics = {}
    for n in range(1, 13):
        metric_id = f"B{n:02d}"
        value = scores.get(metric_id)
        metrics[metric_id] = {"status": "scored" if value is not None else "unknown", "score": value, "evidence": []}
    return {"schema": "yambench.record/1", "record_id": f"r-{problem_id}-{sorted(scores.items())}", "kind": "final",
            "spec": {"version": "v", "hashes": {"metrics.json": "m"}},
            "provenance": {"problem": {"id": problem_id}, "framework": {"commit": "c"},
                           "telemetry": {"clients": ["codex"], "models": ["m"]}},
            "metrics": metrics, "gates": {g: {"status": (gates or {}).get(g, "pass")} for g in ("G1", "G2", "G3", "G4")},
            "retrospective": retrospective, "promotion_authorized": False, "limitations": []}


def current_record(spec: dict, scores=None, created_at="2026-11-01T00:00:00Z", **fields) -> dict:
    record = minimal_record(scores={}, **fields)
    record["metrics"] = {m["id"]: {"status": "scored" if (scores or {}).get(m["id"]) is not None else "unknown",
                                   "score": (scores or {}).get(m["id"]), "evidence": []}
                         for m in spec["metrics"]["metrics"]}
    record["spec"]["hashes"]["metrics.json"] = spec["hashes"]["metrics.json"]
    record.update(created_at=created_at, record_id=f"r-{created_at}")
    return record


class RelevanceTests(unittest.TestCase):
    def test_flags_saturated_unmeasured_and_hygiene_dominated_axes_and_a_due_review(self):
        from datetime import date
        from yambench.relevance import relevance
        spec = load_spec()
        scores = {"B01": 10.0, "B03": 0.0, "B13": 0.0, "B14": 25.0, "B05": 100.0, "B06": 100.0, "B07": 100.0,
                  "B08": 100.0, "B11": 90.0, "B12": 100.0}
        records = [current_record(spec, scores, f"2026-11-0{day}T00:00:00Z") for day in (1, 2, 3)]
        records.append(minimal_record())  # an older spec never enters the report
        report = relevance(records, spec, today=date(2026, 11, 4))
        self.assertEqual(report["records"], 3)
        self.assertTrue(report["review"]["due"])
        self.assertTrue(any(f.startswith("saturated") for f in report["axes"]["B07"]["flags"]))
        self.assertTrue(any(f.startswith("unmeasured") for f in report["axes"]["B09"]["flags"]))
        self.assertIn("flag", report["shapes"][0])
        quiet = relevance(records[:1], spec, today=date(2026, 11, 4))
        self.assertFalse(quiet["review"]["due"])
        self.assertEqual(quiet["axes"]["B07"]["flags"], [])


class CompareTests(unittest.TestCase):
    def test_axes_measured_by_only_one_spec_are_unknown(self):
        spec = load_spec()
        result = compare(minimal_record(scores={"B01": 25.0}), current_record(spec, {"B01": 50.0, "B13": 75.0}),
                         allow_spec_drift=True)
        self.assertEqual(result["axes"]["B01"]["outcome"], "better")
        self.assertEqual(result["axes"]["B13"]["outcome"], "unknown")
        self.assertEqual(result["axes"]["B04"]["candidate_status"], "absent")
        self.assertFalse(result["dominance_claim_eligible"])

    def test_unknown_axes_never_count_as_wins(self):
        result = compare(minimal_record(scores={"B01": 25.0}), minimal_record(scores={"B01": 50.0, "B02": 100.0}))
        self.assertEqual(result["summary"]["better"], 1)
        self.assertEqual(result["axes"]["B02"]["outcome"], "unknown")
        self.assertTrue(result["observed_dominance"])
        self.assertFalse(result["promotion_authorized"])

    def test_gate_regression_blocks_dominance(self):
        result = compare(minimal_record(scores={"B01": 25.0}),
                         minimal_record(scores={"B01": 50.0}, gates={"G1": "fail"}))
        self.assertFalse(result["observed_dominance"])

    def test_different_problems_or_specs_are_refused(self):
        with self.assertRaises(BenchError):
            compare(minimal_record("a"), minimal_record("b"))
        drifted = minimal_record()
        drifted["spec"]["hashes"]["metrics.json"] = "other"
        with self.assertRaises(BenchError):
            compare(minimal_record(), drifted)

    def test_retrospective_records_cannot_support_a_claim(self):
        result = compare(minimal_record(scores={"B01": 25.0}, retrospective=True), minimal_record(scores={"B01": 50.0}))
        self.assertFalse(result["dominance_claim_eligible"])


class ProvenanceTests(unittest.TestCase):
    def test_materialized_snapshot_and_fingerprint_ignore_records(self):
        with tempfile.TemporaryDirectory() as temp:
            repo = Path(temp) / "repo"
            write(repo, "AGENTS.md", "rules")
            write(repo, ".claude/skills/x/SKILL.md", "skill")
            subprocess.run(["git", "init", "-q", str(repo)], check=True)
            subprocess.run(["git", "-C", str(repo), "add", "."], check=True)
            subprocess.run(["git", "-C", str(repo), "-c", "user.name=t", "-c", "user.email=t@t", "commit", "-qm", "c"], check=True)
            head = provenance.resolve(repo, "HEAD")
            snap = provenance.materialize(repo, head, Path(temp) / "snap")
            self.assertEqual((snap / "AGENTS.md").read_text(), "rules")
            before = provenance.fingerprint(snap, ["AGENTS.md", ".claude/"])
            write(snap, ".claude/bench/records/r.json", "{}")
            self.assertEqual(provenance.fingerprint(snap, ["AGENTS.md", ".claude/"]), before)


class CommandTests(unittest.TestCase):
    def test_unarmed_hook_exits_zero_silently(self):
        with tempfile.TemporaryDirectory() as temp:
            subprocess.run(["git", "init", "-q", temp], check=True)
            out = subprocess.run([sys.executable, str(BENCH / "bench.py"), "snapshot", "--hook", "--quiet"], cwd=temp,
                                 input="{}", capture_output=True, text=True)
            self.assertEqual((out.returncode, out.stdout, out.stderr), (0, "", ""))

    def test_dashboard_escapes_script_terminators(self):
        record = minimal_record()
        record["limitations"] = ["</script><script>alert(1)</script>"]
        record["spec"] = {"version": "v"}
        html = render([record], load_spec())
        self.assertNotIn("</script><script>alert", html)

    def test_dashboard_datasets_have_twelve_scores_and_four_gates_per_record(self):
        exported = export_artifact([minimal_record(scores={"B01": 25.0})], load_spec())
        rows = exported["datasets"]
        self.assertEqual(set(rows), {"records", "scores", "gates", "notes", "metrics", "trajectory"})
        self.assertEqual((len(rows["scores"]), len(rows["gates"]), len(rows["metrics"])), (12, 4, 12))
        self.assertIn("dash.onData", exported["page"])

    def test_validate_command_passes_on_repository(self):
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            self.assertEqual(main(["validate"]), 0)
        self.assertIn("12 metrics", buffer.getvalue())


@unittest.skipUnless(MAIN_RUN.is_dir() and subprocess.run(["git", "-C", str(REPO), "cat-file", "-e", "a0c897f^{commit}"],
                                                          capture_output=True).returncode == 0,
                     "P012 run directory or output commit unavailable")
class RealRunTests(unittest.TestCase):
    def test_p012_backfill_reproduces_the_dry_run(self):
        with tempfile.TemporaryDirectory() as temp:
            work = Path(temp)
            spec = load_spec()
            entry = spec["problems"]["problems"][0]
            provenance.materialize(REPO, provenance.resolve(REPO, "a0c897f"), work / "tree")
            provenance.materialize(REPO, provenance.resolve(REPO, "dce6026"), work / "base")
            ctx = Context(spec=spec, problem=entry,
                          layout=Layout(tree=work / "tree", workspace=entry["workspace"], run_dir=MAIN_RUN, base=work / "base"),
                          repo=REPO, framework_commit=provenance.resolve(REPO, "dce6026"),
                          output_commit=provenance.resolve(REPO, "a0c897f"),
                          program={"id": "P012", "path": entry["programs"][0], "sha256": None,
                                   "doc": json.loads((work / "tree" / entry["programs"][0]).read_text())},
                          telemetry={"available": False})
            metrics = compute(ctx)["metrics"]
            self.assertEqual(metrics["B01"]["raw"]["depth_start"], 0)
            self.assertEqual(metrics["B01"]["raw"]["depth_end"], 2)
            self.assertEqual(metrics["B02"]["status"], "n/a")
            self.assertEqual(metrics["B04"]["raw"]["program_frozen"], "pass")
            self.assertEqual(metrics["B07"]["raw"]["bindings"]["mismatch"], 0)
            self.assertIn(metrics["B03"]["status"], {"pending"})
            self.assertTrue(all(v in ANCHORS or v is None for v in [metrics["B03"]["score"]]))


if __name__ == "__main__":
    unittest.main()
