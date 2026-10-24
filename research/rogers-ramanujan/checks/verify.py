"""Bounded, source-bound finite checks. Never certifies the unresolved bridge."""

import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import resource
import signal
import subprocess
import sys
import time

import kr1


ROOT = Path(__file__).resolve().parents[3]
DIRECTORY = Path(__file__).resolve().parents[1]


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def source_hashes():
    files = [DIRECTORY / "checks" / name for name in ("kr1.py", "verify.py")]
    files += [DIRECTORY / "evidence" / name for name in
              ("construction-contract.md", "source-audit.md",
               "round-1-proposal.md", "round-2-proposal.md")]
    files += [ROOT / "programs/rogers-ramanujan-construction.json",
              ROOT / "tests/test_rogers_ramanujan.py"]
    return {str(path.relative_to(ROOT)): hashlib.sha256(path.read_bytes()).hexdigest()
            for path in sorted(files)}


def finite_checks(ceiling):
    product_counts = kr1.residue_counts(ceiling)
    sum_counts = kr1.cluster_counts(ceiling)
    column_counts = kr1.flat_column_counts(ceiling)
    rows = []
    checked_columns = 0
    normalization_checks = rewrites = max_rewrites = 0
    start = time.monotonic()
    # Independent W oracle: ordinary sizes <=N, since every row weight >=1.
    # This uses a different search space and the literal final predicate.
    brute_weighted = Counter()
    for ordinary_size in range(ceiling + 1):
        for asc in kr1.ordinary_partitions(ordinary_size):
            desc = asc[::-1]
            if kr1.is_weighted(desc):
                weight = kr1.weighted_size(desc)
                if weight <= ceiling:
                    brute_weighted[weight] += 1

    for n in range(ceiling + 1):
        gap = list(kr1.gap_partitions(n))
        residue = list(kr1.residue_partitions(n))
        weighted = list(kr1.weighted_partitions(n))
        cluster = list(kr1.cluster_data(n))
        literal_gap = {p for p in kr1.ordinary_partitions(n) if kr1.is_gap(p)}
        literal_residue = {p for p in kr1.ordinary_partitions(n) if kr1.is_residue(p)}
        require(len(set(gap)) == len(gap), f"A duplicates at {n}")
        require(set(gap) == literal_gap, f"A generator mismatch at {n}")
        require(len(set(residue)) == len(residue), f"B duplicates at {n}")
        require(set(residue) == literal_residue, f"B generator mismatch at {n}")
        require(len(set(weighted)) == len(weighted), f"W duplicates at {n}")
        require(len(set(cluster)) == len(cluster), f"C duplicates at {n}")
        require(all(kr1.is_gap(p) and sum(p) == n for p in gap), f"A validity at {n}")
        require(all(kr1.is_residue(p) and sum(p) == n for p in residue), f"B validity at {n}")
        require(all(kr1.is_weighted(p) and kr1.weighted_size(p) == n for p in weighted),
                f"W validity at {n}")
        require(all(c.weight == n for c in cluster), f"C validity at {n}")
        require(len(residue) == product_counts[n], f"B independent DP at {n}")
        require(len(cluster) == sum_counts[n], f"C independent DP at {n}")
        require(len(weighted) == column_counts[n] == brute_weighted[n],
                f"W independent oracles at {n}")
        require(len(gap) == len(residue) == len(weighted) == len(cluster),
                f"finite four-way count mismatch at {n}")
        require(Counter(map(len, gap)) == Counter(c.gap_length for c in cluster),
                f"known gap/cluster refined count mismatch at {n}")
        for partition in weighted:
            columns = kr1.weighted_columns(partition)
            require(sum(columns) == n, f"column weight at {partition}")
            require(kr1.decode_columns(columns) == partition, f"column inverse at {partition}")
            require(kr1.weighted_columns(kr1.decode_columns(columns)) == columns,
                    f"column reverse at {columns}")
            checked_columns += 1
            for profile in kr1.RULE_PROFILES:
                image, steps, trace = kr1.column_straighten(partition, profile=profile)
                require(kr1.is_gap(image) and sum(image) == n,
                        f"R2 validity: profile {profile.name}, input {partition}")
                require(2 * steps <= n * n, f"R2 energy bound at {partition}")
                require(not trace, "default normalization must retain no history")
                normalization_checks += 1
                rewrites += steps
                max_rewrites = max(max_rewrites, steps)
        rows.append({"weight": n, "A": len(gap), "B": len(residue),
                     "W": len(weighted), "C": len(cluster)})
        usage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        rss_bytes = usage if sys.platform == "darwin" else usage * 1024
        require(rss_bytes <= 2 * 1024 ** 3, "enumeration exceeded 2 GiB resident memory")
        require(time.monotonic() - start <= 600, "enumeration exceeded ten minutes")
    return rows, checked_columns, {"normalizations": normalization_checks,
                                  "rewrites": rewrites, "max_rewrites": max_rewrites,
                                  "claim_status": "empirical"}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ceiling", type=int, default=12)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--require-bijection", action="store_true",
                        help="fail until the actual full bridge and Lean certificate exist")
    args = parser.parse_args(argv)
    if not 0 <= args.ceiling <= 30:
        parser.error("ceiling must be between zero and thirty under RR002")
    started = time.monotonic()
    try:
        before = source_hashes()
    except OSError as error:
        print(json.dumps({"status": "failed", "error": f"required source unavailable: {error}"}))
        return 1
    report = {
        "schema": "kr1-finite-checks-v1",
        "started_utc": datetime.now(timezone.utc).isoformat(),
        "ceiling": args.ceiling,
        "status": "failed",
        "claim_status": "empirical",
        "bridge": {"status": "unresolved", "forward_map": None, "inverse_map": None,
                   "lean_certificate": None},
        "source_sha256": before,
        "base_revision": subprocess.run(
            ["git", "rev-parse", "HEAD"], cwd=ROOT, check=True,
            capture_output=True, text=True).stdout.strip(),
        "python": sys.version,
        "limits": {"seconds": 600, "rss_bytes": 2 * 1024 ** 3,
                   "scope": "this finite-check process; parent/critic usage is separate"},
    }

    def timed_out(_signal, _frame):
        raise TimeoutError("finite checks exceeded ten minutes")

    previous_handler = signal.signal(signal.SIGALRM, timed_out)
    signal.setitimer(signal.ITIMER_REAL, 600)
    code = 1
    try:
        (report["counts"], report["column_round_trips"],
         report["normalization_checks"]) = finite_checks(args.ceiling)
        report["falsifiers"] = kr1.first_projection_falsifiers(args.ceiling)
        report["local_rule_family"] = {
            profile.name: kr1.first_straightening_falsifier(args.ceiling, profile)
            for profile in kr1.RULE_PROFILES}
        report["refuted_profiles"] = sum(
            result["status"].startswith("refuted_")
            for result in report["local_rule_family"].values())
        require(before == source_hashes(), "sources changed while verification was running")
        report["status"] = "finite_checks_passed_bridge_unresolved"
        code = 2 if args.require_bijection else 0
        if args.require_bijection:
            report["required_completion_failure"] = "actual W<->C maps and Lean certificate are absent"
    except (AssertionError, TimeoutError, MemoryError, ValueError) as error:
        report["error"] = str(error)
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
        signal.signal(signal.SIGALRM, previous_handler)
    usage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    report["peak_rss_bytes"] = usage if sys.platform == "darwin" else usage * 1024
    report["elapsed_seconds"] = time.monotonic() - started
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps({key: report.get(key) for key in
                      ("status", "ceiling", "elapsed_seconds", "peak_rss_bytes",
                       "column_round_trips", "error")}, sort_keys=True))
    return code


if __name__ == "__main__":
    raise SystemExit(main())
