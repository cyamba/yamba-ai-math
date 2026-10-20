from __future__ import annotations

import itertools
import json
import sys
import tempfile
import unittest
from pathlib import Path

from harness.catalog import ContractError, load_catalog, local_file, positive_int, topological_order
from harness.evaluation import compare, metrics, validate_evaluation
from harness.planner import assemble
from harness.runtime import execute, validate_result


ROOT = Path(__file__).resolve().parents[1]


def agent(name, capabilities, cost=1, tags=None):
    return {"id": name, "name": name, "category": "test", "capabilities": capabilities,
            "cost_units": cost, "tags": tags or [], "prompt_file": "agents/scout.md"}


def program(**constraints):
    return {"id": "T001", "title": "Test program", "objective": "Exercise orchestration only",
            "fleet": "test", "briefs": [], "deliverables": ["test"],
            "success_criteria": ["valid protocol"], "stop_conditions": ["budget"],
            "constraints": {"max_agents": 4, "max_cost_units": 20, "max_workers": 2,
                            "max_rounds": 2, "timeout_seconds": 5, **constraints}}


def fleet(stages):
    return {"id": "test", "description": "Test only", "max_agents": 4,
            "required_capabilities": sorted({r for s in stages for r in s["requires"]}), "stages": stages}


def result(summary="test result"):
    return {"summary": summary, "claims": [], "artifacts": []}


class CatalogTests(unittest.TestCase):
    def test_real_catalog_has_feasible_role_prompts(self):
        agents, fleets = load_catalog(ROOT)
        self.assertGreaterEqual(len(agents), 10)
        self.assertIn("explore", fleets)

    def test_cycle_is_rejected(self):
        with self.assertRaises(ContractError):
            topological_order([{"id": "a", "requires": ["x"], "depends_on": ["b"]},
                               {"id": "b", "requires": ["x"], "depends_on": ["a"]}])

    def test_unknown_independence_target_is_rejected(self):
        with self.assertRaises(ContractError):
            topological_order([{"id": "a", "requires": ["x"], "independent_of": ["missing"]}])

    def test_boolean_is_not_a_budget(self):
        with self.assertRaises(ContractError):
            positive_int(True, "budget")

    def test_prompt_path_cannot_escape_repository(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "root"
            root.mkdir()
            (Path(tmp) / "outside.md").write_text("outside")
            with self.assertRaises(ContractError):
                local_file(root, "../outside.md")
            (root / "link.md").symlink_to(Path(tmp) / "outside.md")
            with self.assertRaises(ContractError):
                local_file(root, "link.md")


class PlannerTests(unittest.TestCase):
    def setUp(self):
        self.agents = {a["id"]: a for a in [agent("cheap", ["write", "review"], 1),
                                            agent("reviewer", ["review"], 2),
                                            agent("writer", ["write"], 2, ["proof"]) ]}
        self.fleet = fleet([{"id": "write", "requires": ["write"]},
                            {"id": "review", "requires": ["review"], "depends_on": ["write"], "independent_of": ["write"]}])

    def test_exact_cost_matches_exhaustive_assignments(self):
        plan = assemble(program(), self.agents, {"test": self.fleet})
        feasible = [a["cost_units"] + b["cost_units"] for a, b in itertools.product(self.agents.values(), repeat=2)
                    if "write" in a["capabilities"] and "review" in b["capabilities"] and a["id"] != b["id"]]
        self.assertEqual(plan["cost_units"], min(feasible))
        self.assertNotEqual(plan["steps"][0]["agent_id"], plan["steps"][1]["agent_id"])

    def test_budget_and_role_count_are_hard_constraints(self):
        for p in [program(max_cost_units=2), program(max_agents=1)]:
            with self.assertRaises(ContractError):
                assemble(p, self.agents, {"test": self.fleet})

    def test_tag_preference_breaks_cost_ties(self):
        p = program()
        p["preferred_tags"] = ["proof"]
        plan = assemble(p, self.agents, {"test": self.fleet})
        self.assertEqual(plan["cost_units"], 3)
        self.assertEqual(plan["steps"][0]["agent_id"], "writer")

    def test_required_tags_filter_candidates(self):
        self.fleet["stages"][0]["required_tags"] = ["proof"]
        plan = assemble(program(), self.agents, {"test": self.fleet})
        self.assertEqual(plan["steps"][0]["agent_id"], "writer")

    def test_repeated_role_dispatches_are_counted(self):
        f = fleet([{"id": "first", "requires": ["write"]},
                   {"id": "again", "requires": ["write"], "depends_on": ["first"]}])
        p = program()
        p["rounds"] = 2
        plan = assemble(p, self.agents, {"test": f})
        self.assertEqual(plan["cost_units"], 4)
        self.assertEqual(len(plan["steps"]), 4)
        self.assertEqual(plan["steps"][2]["depends_on"], ["r1--again"])
        self.assertEqual(plan["distinct_agents"], ["cheap"])

    def test_multiround_budget_applies_to_whole_run(self):
        p = program(max_cost_units=5)
        p["rounds"] = 2
        with self.assertRaises(ContractError):
            assemble(p, self.agents, {"test": self.fleet})


class RuntimeTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.directory = Path(self.temp.name)
        self.agents = {"worker": agent("worker", ["literature"])}
        self.fleet = fleet([{"id": "first", "requires": ["literature"]},
                            {"id": "dependent", "requires": ["literature"], "depends_on": ["first"]},
                            {"id": "parallel", "requires": ["literature"]}])
        self.program = program()
        self.plan = assemble(self.program, self.agents, {"test": self.fleet})

    def run_backend(self, **kwargs):
        return execute(ROOT, self.program, self.plan, self.agents, self.directory / "run", **kwargs)

    def test_manual_packets_are_unexecuted(self):
        receipt = self.run_backend()
        self.assertEqual(receipt["status"], "awaiting_execution")
        self.assertEqual(receipt["attempted_cost_units"], 0)
        request = json.loads((self.directory / "run/packets/dependent.json").read_text())
        self.assertIsNone(request["upstream"][0]["result"])
        self.assertIn("Research standards", request["instructions"]["repository"])
        self.assertTrue(request["instructions"]["skills"])
        self.assertIn("fleet_plan", request)

    def test_preparation_failure_is_recorded_and_blocks_dependents(self):
        self.agents["worker"]["prompt_file"] = "agents/missing-role.md"
        receipt = self.run_backend()
        self.assertEqual(receipt["status"], "failed_preparation")
        self.assertEqual(receipt["states"]["first"], "failed")
        self.assertEqual(receipt["states"]["dependent"], "blocked")
        self.assertTrue((self.directory / "run/receipt.json").is_file())

    def test_scoped_rules_are_delivered_with_briefs(self):
        self.program["briefs"] = ["explore/E001-certified-attention-compression.md"]
        self.run_backend()
        saved = json.loads((self.directory / "run/packets/first.json").read_text())
        self.assertIn("explore/AGENTS.md", [r["path"] for r in saved["instructions"]["scoped"]])

    def test_command_passes_completed_upstream_results(self):
        source = "import json,sys; p=json.load(sys.stdin); print(json.dumps({'summary':json.dumps(p['upstream']),'claims':[],'artifacts':[]}))"
        receipt = self.run_backend(backend="command", command=[sys.executable, "-c", source])
        self.assertEqual(receipt["status"], "completed_execution")
        self.assertFalse(receipt["research_validated"])
        self.assertIsNone(receipt["reported_usage"])
        saved = json.loads((self.directory / "run/results/dependent.json").read_text())
        self.assertEqual(json.loads(saved["summary"])[0]["result"]["summary"], "[]")

    def test_bad_output_blocks_only_dependents(self):
        source = "import json,sys; p=json.load(sys.stdin); print('bad' if p['step']['id']=='first' else json.dumps({'summary':'ok','claims':[],'artifacts':[]}))"
        receipt = self.run_backend(backend="command", command=[sys.executable, "-c", source])
        self.assertEqual(receipt["states"], {"first": "failed", "dependent": "blocked", "parallel": "completed"})
        self.assertEqual(receipt["attempted_cost_units"], 2)

    def test_nonzero_adapter_stderr_is_not_persisted(self):
        source = "import sys; print('SECRET_SENTINEL',file=sys.stderr); sys.exit(7)"
        receipt = self.run_backend(backend="command", command=[sys.executable, "-c", source])
        self.assertEqual(receipt["status"], "failed_execution")
        persisted = (self.directory / "run/events.jsonl").read_text() + json.dumps(receipt)
        self.assertNotIn("SECRET_SENTINEL", persisted)

    def test_timeout_is_failure_without_retry(self):
        self.program["constraints"]["timeout_seconds"] = 1
        receipt = self.run_backend(backend="command", command=[sys.executable, "-c", "import time; time.sleep(5)"])
        self.assertEqual(receipt["states"]["first"], "failed")
        self.assertEqual(receipt["states"]["dependent"], "blocked")
        self.assertLess(receipt["elapsed_seconds"], 4)

    def test_replay_requires_every_dispatched_result(self):
        replay = self.directory / "replay"
        replay.mkdir()
        (replay / "first.json").write_text(json.dumps(result()))
        (replay / "dependent.json").write_text(json.dumps(result()))
        receipt = self.run_backend(backend="replay", replay_dir=replay)
        self.assertEqual(receipt["backend"], "replay")
        self.assertEqual(receipt["states"]["parallel"], "failed")
        self.assertEqual(receipt["states"]["dependent"], "completed")

    def test_existing_run_directory_is_not_overwritten(self):
        self.run_backend()
        with self.assertRaises(ContractError):
            self.run_backend()

    def test_unknown_claim_status_is_rejected(self):
        value = result()
        value["claims"] = [{"text": "claim", "status": "definitely-genius"}]
        with self.assertRaises(ContractError):
            validate_result(value)

    def test_reported_usage_cannot_be_negative_or_boolean(self):
        for number in [-1, True]:
            value = {**result(), "usage": {"input_tokens": number, "output_tokens": 0}}
            with self.assertRaises(ContractError):
                validate_result(value)


def evaluation(name, cases=None, **fields):
    return {"evaluation_id": name, "candidate_id": name, "suite_id": "test-suite", "suite_revision": "v1",
            "split": "heldout", "synthetic": True,
            "cases": cases or [{"case_id": "one", "answered": True, "complete_correct": True,
                                "false_claims": 0, "unsupported_claims": 0, "cost_units": 2}], **fields}


class EvaluationTests(unittest.TestCase):
    def test_synthetic_gain_never_qualifies_for_promotion(self):
        left, right = evaluation("left"), evaluation("right")
        right["cases"][0]["cost_units"] = 1
        report = compare(left, right)
        self.assertTrue(report["challenger_dominates_observed_cases"])
        self.assertFalse(report["promotion_eligible_for_review"])
        self.assertFalse(report["promotion_authorized"])

    def test_all_abstain_has_undefined_risk_and_no_dominance(self):
        right = evaluation("right")
        right["cases"][0].update(answered=False, complete_correct=False, cost_units=0)
        self.assertIsNone(metrics(right)["false_response_risk"])
        self.assertFalse(compare(evaluation("left"), right)["challenger_dominates_observed_cases"])

    def test_mismatched_suite_or_cases_are_rejected(self):
        for field, value in [("suite_revision", "v2"), ("synthetic", False)]:
            with self.assertRaises(ContractError):
                compare(evaluation("a"), evaluation("b", **{field: value}))
        right = evaluation("b")
        right["cases"][0]["case_id"] = "other"
        with self.assertRaises(ContractError):
            compare(evaluation("a"), right)

    def test_duplicate_cases_are_rejected(self):
        value = evaluation("x")
        value["cases"] *= 2
        with self.assertRaises(ContractError):
            validate_evaluation(value)

    def test_nan_cost_is_rejected(self):
        value = evaluation("x")
        value["cases"][0]["cost_units"] = float("nan")
        with self.assertRaises(ContractError):
            validate_evaluation(value)

    def test_huge_and_overflowing_aggregate_costs_are_rejected(self):
        value = evaluation("x")
        value["cases"][0]["cost_units"] = 10 ** 1000
        with self.assertRaises(ContractError):
            validate_evaluation(value)
        value = evaluation("x")
        value["cases"][0]["cost_units"] = 1e308
        value["cases"].append({**value["cases"][0], "case_id": "second"})
        with self.assertRaises(ContractError):
            validate_evaluation(value)

    def test_false_claim_cannot_be_scored_complete_correct(self):
        value = evaluation("x")
        value["cases"][0]["false_claims"] = 1
        with self.assertRaises(ContractError):
            validate_evaluation(value)


if __name__ == "__main__":
    unittest.main()
