"""Bounded transcription checks for the written all-parameter a3,b0 theorem."""
from collections import Counter
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / 'research/rogers-ramanujan/checks'))
import rr004_multidim_cones as m


def closed(s, t, d):
    if min(s, t, d) < 0:
        raise ValueError('nonnegative coordinates required')
    if t == 0:
        u, v = divmod(s + 3, 2)
        core = (6,) * u + (3,) * v
    elif t in (1, 2):
        marker = 8 if t == 1 else 10
        core = ((marker,) + (3,) * (s + 1) if s <= 1
                else (marker, 6) + (3,) * (s - 1))
    elif t == 3:
        if s == 0:
            return (9, 6) if d == 0 else (10, 6) + (1,) * (d - 1)
        core = ((10, 8) + (3,) * (s - 1) if s <= 2
                else (10, 8, 6) + (3,) * (s - 3))
    else:
        q, r = divmod(t, 3)
        if r == 1:
            core = (9, 8) + (6,) * (q - 1) + (3,) * s
        elif r == 2:
            core = ((9, 9, 1) if (q, s) == (1, 0)
                    else (10, 9) + (6,) * (q - 1) + (3,) * s)
        elif q >= 4 and s >= 1:
            core = (10, 9, 9, 8) + (6,) * (q - 4) + (3,) * (s - 1)
        else:
            core = (9, 9) + (6,) * (q - 2) + (3,) * (s + 1)
    return core + (1,) * d


def explicit_inverse(u):
    c = Counter(u)
    head = tuple(v for v in u if v >= 8)
    d = c[1]
    if head == ():
        s, t = 2*c[6]+c[3]-3, 0
    elif head in ((8,), (10,)):
        if head == (10,) and c[3] == 0:
            s, t, d = 0, 3, d+1
        else:
            s = c[3]-1 if c[6] == 0 else c[3]+1
            t = 1 if head == (8,) else 2
    elif head == (9,):
        s, t, d = 0, 3, 0
    elif head == (10, 8):
        s = c[3]+1 if c[6] == 0 else c[3]+3
        t = 3
    elif head == (9, 8):
        s, t = c[3], 3*(c[6]+1)+1
    elif head == (9, 9) and c[3] == c[6] == 0:
        s, t, d = 0, 5, d-1
    elif head == (10, 9):
        s, t = c[3], 3*(c[6]+1)+2
    elif head == (9, 9):
        s, t = c[3]-1, 3*(c[6]+2)
    elif head == (10, 9, 9, 8):
        s, t = c[3]+1, 3*(c[6]+4)
    else:
        raise ValueError('not in the displayed image')
    if min(s, t, d) < 0 or closed(s, t, d) != u:
        raise ValueError('not in the displayed image')
    return s, t, d


def verify(s_max=12, t_max=36, d_max=8):
    seen = {}
    count = 0
    for s in range(s_max+1):
        for t in range(t_max+1):
            for d in range(d_max+1):
                c = m.kr1.ClusterData(3, 0, (s, s+t, s+t+d), ())
                u = closed(s, t, d)
                assert m.reconstruct_a3_b0(c) == u
                assert explicit_inverse(u) == (s, t, d)
                assert m.decompose_a3_b0(u) == c
                assert sum(u) == 9+3*s+2*t+d
                m.kr1.decode_columns(u)
                try:
                    m.rr003_a2.decompose_columns(u)
                except m.OutsideRestrictedDomain:
                    pass
                else:
                    raise AssertionError(('lower overlap', c, u))
                assert u not in seen
                seen[u] = c
                count += 1
    return {'status': 'passed_bounded_transcription_checks', 'checks': count,
            'coordinate_bounds': {'s': [0, s_max], 't': [0, t_max], 'd': [0, d_max]},
            'all_parameter_theorem_assurance': 'written proof, not established by this finite check',
            'max_weight_in_box': 9+3*s_max+2*t_max+d_max}


if __name__ == '__main__':
    if not __debug__:
        raise SystemExit('Run with assertions enabled; omit -O')
    report = verify()
    output = Path(__file__).with_name('sector_evidence.json')
    output.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report, indent=2))
