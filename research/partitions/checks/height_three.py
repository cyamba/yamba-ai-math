"""P012 exact signed tableaux and bounded, preregistered first-difference tests.

No new theorem or Lean certificate is inferred from these finite computations.
Run from the repository root with ``python3 -m research.partitions.checks.height_three``.
"""
from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
import hashlib
from itertools import permutations
import json
from pathlib import Path
import resource
import signal
import subprocess
import sys
import time

from . import coloring_oracle as oracle
from . import tableaux as tab


ROOT = Path(__file__).resolve().parents[3]
PHASE = ROOT / "research/partitions/height-three-unimodality"
PROTOCOL = PHASE / "protocol.json"
LIMITS = dict(round_seconds=600, case_seconds=120, extensions=5_000_000,
              candidates=5_000_000, memory_bytes=2 * 1024**3,
              artifact_bytes=250 * 1024**2)
HELDOUT = ((3, 3, 3, 6, 6, 6, 9, 9, 9),
           (3, 3, 4, 6, 6, 7, 9, 9, 9),
           (3, 3, 3, 6, 6, 6, 10, 10, 10, 10),
           (3, 3, 4, 7, 7, 7, 8, 10, 10, 10))
SELECTORS = tuple((order, end) for order in permutations(range(3)) for end in (0, 1))


def height(h):
    h = oracle._hessenberg(h)
    lengths = []
    for v in range(1, len(h) + 1):
        lengths.append(1 + max((lengths[u - 1] for u in range(1, v)
                                if tab.lt_p(h, u, v)), default=0))
    return max(lengths, default=0)


def target(n):
    if type(n) is not int or n < 7:
        raise ValueError("P012 requires n >= 7")
    return (n - 4, 3, 1)


def parity(sigma):
    return (-1) ** sum(a > b for i, a in enumerate(sigma) for b in sigma[i + 1:])


@dataclass(frozen=True, order=True)
class Sector:
    shape: tuple
    sigma: tuple
    indices: tuple

    @property
    def sign(self):
        return parity(self.sigma)


def determinant_terms(shape):
    """Raw determinant terms, including zero factors and negative-index zeros."""
    columns = tuple(sum(x > j for x in shape) for j in range(max(shape, default=0)))
    for sigma in permutations(range(len(columns))):
        yield Sector(tuple(shape), sigma,
                     tuple(x - i + sigma[i] for i, x in enumerate(columns)))


def contributes(sector, lam):
    return (all(x >= 0 for x in sector.indices)
            and tuple(sorted((x for x in sector.indices if x), reverse=True)) == tuple(lam))


def sectors(n, lam=None, max_width=3):
    lam = target(n) if lam is None else tuple(lam)
    return tuple(sorted(s for shape in tab.partitions(n, max_width)
                        for s in determinant_terms(shape) if contributes(s, lam)))


def wang_sectors(n):
    """Independent closed-form shape/sign list; invalid shapes are empty."""
    result = Counter()
    for a, b, sign in ((1, 2, 1), (2, 2, 1), (1, 3, -1), (2, 0, -1), (3, 0, -1)):
        rest = n - 3 * a - 2 * b
        if rest >= 0:
            result[(3,) * a + (2,) * b + (1,) * rest] += sign
    if n == 8:
        result[(3, 3, 2)] -= 1
    return dict(result)


def development():
    answer = []
    for n in (7, 8):
        ranked = sorted((h for h in tab.hessenberg_vectors(n) if height(h) == 3),
                        key=lambda h: hashlib.sha256(
                            ("h3-unimodality-v1:" + ",".join(map(str, h))).encode()).hexdigest())
        answer.extend(ranked[:4])
    return tuple(answer)


def protocol():
    return dict(schema_version=1, program="P012", target="(n-4,3,1), height exactly 3",
                development=development(), heldout=HELDOUT, limits=LIMITS,
                primitives=["same-word reblocking", "comparable-prefix insertion/all exact extractions",
                            "one adjacent incomparable swap then reblocking"],
                selectors=[dict(id=i, priority=order, endpoint=("first", "last")[end])
                           for i, (order, end) in enumerate(SELECTORS)],
                raw_order=["shape", "sigma", "rows", "epsilon"],
                selection="minimum development unpaired negatives; ties by selector id; capped development ineligible",
                round_two="after certified tableau obstruction compare complete forest triples; no new tableau grammar")


def encoded(value):
    return json.dumps(value, indent=2, sort_keys=True) + "\n"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify_protocol():
    if json.loads(PROTOCOL.read_text()) != json.loads(encoded(protocol())):
        raise ValueError("Frozen protocol differs from implemented experiment")


def freeze():
    expected = encoded(protocol())
    if PROTOCOL.exists() and PROTOCOL.read_text() != expected:
        raise ValueError("Refusing to replace a different frozen protocol")
    PHASE.mkdir(parents=True, exist_ok=True)
    PROTOCOL.write_text(expected)
    return dict(protocol=str(PROTOCOL.relative_to(ROOT)), sha256=digest(PROTOCOL),
                development=development(), heldout=HELDOUT)


class Capped(RuntimeError):
    pass


def peak_rss():
    value = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return value if sys.platform == "darwin" else value * 1024


class Budget:
    def __init__(self, **overrides):
        self.limits = LIMITS | overrides
        self.start = time.monotonic()
        self.cpu = time.process_time()
        self.case_start = self.start
        self.extensions = self.candidates = 0

    def check(self):
        now = time.monotonic()
        if now - self.start >= self.limits["round_seconds"]:
            raise Capped("round wall time")
        if now - self.case_start >= self.limits["case_seconds"]:
            raise Capped("case wall time")
        if peak_rss() >= self.limits["memory_bytes"]:
            raise Capped("peak RSS")

    def tick(self, kind="extensions"):
        value = getattr(self, kind)
        if value >= self.limits[kind]:
            raise Capped("round " + kind)
        setattr(self, kind, value + 1)
        if value % 128 == 0:
            self.check()

    def begin_case(self):
        self.case_start = time.monotonic()
        self.check()

    def receipt(self):
        return dict(extensions=self.extensions, candidates=self.candidates,
                    wall_seconds=time.monotonic() - self.start,
                    process_seconds=time.process_time() - self.cpu,
                    peak_rss_bytes=peak_rss(), limits=self.limits)


@dataclass(frozen=True, order=True)
class State:
    shape: tuple
    sigma: tuple
    rows: tuple
    epsilon: int
    inversion: int = field(compare=False)

    @property
    def sign(self):
        return parity(self.sigma) * (-1) ** self.epsilon

    @property
    def degree(self):
        return self.inversion + self.epsilon

    def record(self):
        return asdict(self) | dict(sign=self.sign, degree=self.degree)


def filling_generator(h, shape, budget):
    """Complete prefix-pruned enumeration; no row/column constraint is postponed."""
    cells = [(r, c) for r, length in enumerate(shape) for c in range(length)]
    rows = [[] for _ in shape]

    def visit(k, unused):
        if k == len(cells):
            value = tuple(map(tuple, rows))
            if not tab.validates(h, value, shape):
                raise AssertionError("prefix pruning admitted an invalid tableau")
            yield value
            return
        r, c = cells[k]
        for u in unused:
            budget.tick()
            if c and not tab.lt_p(h, rows[r][-1], u):
                continue
            if r and tab.lt_p(h, u, rows[r - 1][c]):
                continue
            rows[r].append(u)
            yield from visit(k + 1, tuple(v for v in unused if v != u))
            rows[r].pop()
    yield from visit(0, tuple(range(1, len(h) + 1)))


def reblock(word, shape):
    offset = 0
    rows = []
    for length in shape:
        rows.append(tuple(word[offset:offset + length]))
        offset += length
    return tuple(rows)


def bubble_neighbors(h, rows, budget=None):
    """Forward insertion and every exact inverse, rather than height-two recovery."""
    answer = set()
    for k, row in enumerate(rows):
        if len(row) == 2 and all(len(x) == 1 for x in rows[k + 1:]):
            if budget:
                budget.tick("candidates")
            answer.add(tab.bubble_demote(h, rows, k))
        if len(row) == 1 and all(len(x) == 1 for x in rows[k:]):
            for i in range(k + 1, len(rows)):
                if budget:
                    budget.tick("candidates")
                candidate = rows[:k] + ((row[0], rows[i][0]),) + rows[k + 1:i] + rows[i + 1:]
                if tab.validates(h, candidate) and tab.bubble_demote(h, candidate, k) == rows:
                    answer.add(candidate)
    return answer


def legal_targets(h, state, all_sectors, budget):
    """Complete neighbors in each frozen primitive, with raw determinant tags."""
    word = tuple(u for row in state.rows for u in row)
    answer = [set(), set(), set()]

    def consider(kind, sec, rows, epsilon):
        budget.tick("candidates")
        if not tab.validates(h, rows, sec.shape):
            return
        inv = tab.inv_g(h, rows)
        dest = State(sec.shape, sec.sigma, rows, epsilon, inv)
        if dest.sign == -state.sign and dest.degree == state.degree:
            answer[kind].add(dest)

    for sec in all_sectors:
        if sec.sign == -parity(state.sigma):
            consider(0, sec, reblock(word, sec.shape), state.epsilon)
    for rows in bubble_neighbors(h, state.rows, budget):
        for sec in all_sectors:
            if sec.shape == tuple(map(len, rows)) and sec.sign == -parity(state.sigma):
                consider(1, sec, rows, state.epsilon)
    edges = set(tab.graph_edges(h))
    for i in range(len(word) - 1):
        if tuple(sorted(word[i:i + 2])) not in edges:
            continue
        swapped = word[:i] + (word[i + 1], word[i]) + word[i + 2:]
        for sec in all_sectors:
            if sec.sign == parity(state.sigma):
                consider(2, sec, reblock(swapped, sec.shape), 1 - state.epsilon)
    return tuple(tuple(sorted(group)) for group in answer)


def choose(endpoints, selector):
    order, end = SELECTORS[selector]
    for primitive in order:
        if endpoints[primitive]:
            return endpoints[primitive][end]
    return None


def analyze_moves(h, states, all_sectors, budget, selector_ids=range(12)):
    lookup = set(states)
    endpoints = {}
    isolated = None
    for state in sorted(states, key=lambda s: (s.degree, s)):
        groups = legal_targets(h, state, all_sectors, budget)
        if any(dest not in lookup for group in groups for dest in group):
            raise AssertionError("legal move escaped complete same-degree universe")
        endpoints[state] = tuple((group[0], group[-1]) if group else () for group in groups)
        if state.sign < 0 and not any(groups) and isolated is None:
            isolated = state.record()
    negative = sorted((s for s in states if s.sign < 0), key=lambda s: (s.degree, s))
    reports = []
    for selector in selector_ids:
        matched = 0
        collisions = 0
        seen = {}
        first_failure = first_collision = None
        for state in negative:
            dest = choose(endpoints[state], selector)
            back = choose(endpoints[dest], selector) if dest else None
            if dest in seen:
                collisions += 1
                if first_collision is None:
                    first_collision = dict(source=state.record(), other=seen[dest].record(), target=dest.record())
            elif dest:
                seen[dest] = state
            if back == state:
                matched += 1
            elif first_failure is None:
                first_failure = dict(source=state.record(),
                                     target=dest.record() if dest else None,
                                     reverse=back.record() if back else None,
                                     reason="no legal neighbor" if dest is None else "nonreciprocal selection")
        reports.append(dict(id=selector, negative=len(negative), paired=matched,
                            unpaired=len(negative) - matched, directed_collisions=collisions,
                            first_failure=first_failure, first_collision=first_collision))
    return dict(status="complete", selectors=reports, isolated_negative=isolated,
                state_count=len(states), negative_count=len(negative))


def enumerate_signed(h, budget):
    h = oracle._hessenberg(h)
    if height(h) != 3:
        raise ValueError("P012 requires height exactly three")
    all_sectors = sectors(len(h))
    grouped = {}
    for sec in all_sectors:
        grouped.setdefault(sec.shape, []).append(sec)
    M = len(tab.graph_edges(h))
    polynomial = [0] * (M + 1)
    doubled = [0] * (M // 2 + 1)
    states = []
    census = []
    for shape, shape_sectors in sorted(grouped.items()):
        weights = Counter()
        for rows in filling_generator(h, shape, budget):
            inv = tab.inv_g(h, rows)
            weights[inv] += 1
            for sec in shape_sectors:
                polynomial[inv] += sec.sign
                for epsilon in (0, 1):
                    if inv + epsilon <= M // 2:
                        state = State(shape, sec.sigma, rows, epsilon, inv)
                        states.append(state)
                        doubled[state.degree] += state.sign
        for sec in shape_sectors:
            census.append(asdict(sec) | dict(sign=sec.sign, tableaux=sum(weights.values()),
                                             degrees=dict(sorted(weights.items()))))
    differences = [value - (polynomial[d - 1] if d else 0)
                   for d, value in enumerate(polynomial[:M // 2 + 1])]
    if doubled != differences:
        raise AssertionError("doubled signed space does not equal first differences")
    if polynomial != polynomial[::-1]:
        raise AssertionError("signed coefficient violates established palindromicity")
    return states, dict(status="complete", edges=M, coefficient=polynomial,
                        first_differences=differences, sectors=census,
                        nonnegative_lower_differences=all(x >= 0 for x in differences))


def coloring_coefficient(h, budget):
    """Reuse independent coloring/subset oracle, accounting for recursive visits."""
    previous = sys.getprofile()
    def profile(frame, event, arg):
        if event == "call" and frame.f_code.co_filename == oracle.__file__:
            if frame.f_code.co_name == "visit":
                budget.tick()
            else:
                budget.check()
    try:
        sys.setprofile(profile)
        value = oracle.elementary_expansion(h).get(target(len(h)), ())
        return list(value) + [0] * (len(tab.graph_edges(h)) + 1 - len(value))
    finally:
        sys.setprofile(previous)


def _alarm(signum, frame):
    raise Capped("case or round wall timer")


def run_case(h, budget, *, heldout=False, selector=0):
    receipt = dict(h=h, split="heldout" if heldout else "development", status="incomplete")
    before = budget.receipt()
    try:
        budget.begin_case()
        remaining = min(budget.limits["case_seconds"],
                        budget.limits["round_seconds"] - (time.monotonic() - budget.start))
        signal.setitimer(signal.ITIMER_REAL, max(0.001, remaining))
        states, receipt["signed_space"] = enumerate_signed(h, budget)
        receipt["moves"] = analyze_moves(h, states, sectors(len(h)), budget,
                                         (selector,) if heldout else range(12))
        del states
        if not heldout:
            receipt["oracle"] = dict(status="running")
            computed = coloring_coefficient(h, budget)
            if computed != receipt["signed_space"]["coefficient"]:
                raise AssertionError("independent coloring oracle disagrees")
            receipt["oracle"] = dict(status="agrees", coefficient=computed)
        else:
            receipt["oracle"] = dict(status="not scheduled for held-out sizes")
        receipt["status"] = "complete"
    except (Capped, MemoryError) as exc:
        receipt["status"] = "capped"
        receipt["cap_reason"] = str(exc) or "memory allocation"
        if receipt.get("oracle", {}).get("status") == "running":
            receipt["oracle"] = dict(status="capped", reason=receipt["cap_reason"])
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
    after = budget.receipt()
    receipt["resources"] = {key: after[key] - before[key]
                             for key in ("extensions", "candidates", "wall_seconds", "process_seconds")}
    receipt["resources"]["peak_rss_bytes"] = after["peak_rss_bytes"]
    return receipt


def provenance():
    paths = [Path(__file__), Path(tab.__file__), Path(oracle.__file__), PROTOCOL,
             ROOT / "programs/partition-h3-unimodality.json"]
    forest = Path(__file__).with_name("forest_triples.py")
    if forest.exists():
        paths.append(forest)
    return dict(base_revision=subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip(),
                branch=subprocess.check_output(["git", "branch", "--show-current"], cwd=ROOT, text=True).strip(),
                sources={str(p.relative_to(ROOT)): digest(p) for p in paths},
                python=sys.version, execution="manual orchestration; exact local computation")


def write_report(path, value):
    data = encoded(value)
    if path.exists():
        raise ValueError("Refusing to overwrite a run artifact")
    existing = sum(p.stat().st_size for p in path.parent.rglob("*") if p.is_file())
    if existing + len(data.encode()) > LIMITS["artifact_bytes"]:
        raise Capped("aggregate artifact bytes in output directory")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(data)


def run_round(output):
    verify_protocol()
    signal.signal(signal.SIGALRM, _alarm)
    budget = Budget()
    report = dict(program="P012", round=1, status="finite-exact-evidence", research_validated=False,
                  started_utc=datetime.now(timezone.utc).isoformat(), provenance=provenance(), cases=[])
    for h in development():
        report["cases"].append(run_case(h, budget))
        print(encoded({"h": h, "status": report["cases"][-1]["status"]}).strip(), flush=True)
    dev = report["cases"]
    scores = [sum(next(s["unpaired"] for s in c["moves"]["selectors"] if s["id"] == i)
                  for c in dev if c.get("moves", {}).get("status") == "complete") for i in range(12)]
    selected = min(range(12), key=lambda i: (scores[i], i))
    lock = dict(selector=selected, development_scores=scores,
                eligible=all(c["status"] == "complete" for c in dev) and scores[selected] == 0,
                development_sha256=hashlib.sha256(encoded(dev).encode()).hexdigest(),
                note="locked before held-out execution; no capped case counts as success")
    write_report(output.with_name(output.stem + "-selection-lock.json"), lock)
    report["selection_lock"] = lock
    for h in HELDOUT:
        report["cases"].append(run_case(h, budget, heldout=True, selector=selected))
        print(encoded({"h": h, "status": report["cases"][-1]["status"]}).strip(), flush=True)
    report["resources"] = budget.receipt()
    report["source_stable"] = report["provenance"]["sources"] == provenance()["sources"]
    if not report["source_stable"]:
        raise ValueError("Experiment sources changed during execution")
    write_report(output, report)
    return dict(output=str(output), resources=report["resources"], selection_lock=lock)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("freeze")
    run = commands.add_parser("run")
    run.add_argument("--round", type=int, choices=(1,), required=True)
    run.add_argument("--output", type=Path, required=True)
    forest = commands.add_parser("forest")
    forest.add_argument("--input", type=Path, required=True)
    forest.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.command == "freeze":
        answer = freeze()
    elif args.command == "run":
        answer = run_round(args.output)
    else:
        from .forest_triples import run_comparison
        answer = run_comparison(args.input, args.output)
    print(encoded(answer), end="")


if __name__ == "__main__":
    main()
