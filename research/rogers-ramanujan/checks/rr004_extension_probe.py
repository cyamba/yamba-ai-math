"""Bounded research probe preserving the first failure beyond the N40 certificate."""
from dataclasses import asdict
import json
from pathlib import Path
import argparse
import rr004_multidim_cones as m


def probe():
    high = m.kr1.ClusterData(5, 0, (0, 1, 2, 6, 7), ())
    low = m.kr1.ClusterData(2, 2, (5, 5), (0, 1))
    u = (19, 12, 6, 3, 1)
    assert m.reconstruct_full(high) == m.reconstruct_full(low) == u
    assert m.decompose_full(u) == low != high
    failures = []
    for c in m.kr1.cluster_data(41):
        try:
            image = m.reconstruct_full(c)
            if m.decompose_full(image) != c:
                failures.append({"cluster": asdict(c), "kind": "roundtrip_collision", "image": image})
        except m.OutsideRestrictedDomain as e:
            failures.append({"cluster": asdict(c), "kind": "missing_apex", "detail": str(e)})
    assert len(failures) == 10
    return {
        "assurance": "finite exact counterexample search, not a new general theorem",
        "full_candidate_extension": "refuted_at_N41",
        "first_weight_beyond_verified_bound": 41,
        "failures_at_41": failures,
        "collision": {"higher": asdict(high), "lower": asdict(low), "common_U": u},
        "a3_b0_states_verified_through_60": m.verify_a3_b0_sector(60),
        "next_target": "Repair +6,+3,+1 orbit of (19,12,6); establish invariant excluding lower-sector images and unique inverse, before extending apex table."
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    if not __debug__:
        raise SystemExit("Verification requires assertions enabled; omit -O")
    data = json.dumps(probe(), indent=2) + '\n'
    if args.output:
        args.output.write_text(data)
    else:
        print(data, end='')
