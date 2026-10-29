"""Independent RR004 exact-domain audit; does not import author check modules."""
from pathlib import Path
import hashlib
import json

ROOT = Path.cwd()
PREFIX = (0, 1, 3, 6, 8)

def F(h):
    return 9 * (h // 5) + PREFIX[h % 5]

def domain_u(n):
    answer = []
    max_h = 0
    while F(max_h + 1) <= n:
        max_h += 1
    def visit(rem, bound, path):
        if rem == 0:
            if not path or path[-1] < 5:
                answer.append(tuple(F(h) for h in path))
            return
        for h in range(1, bound + 1):
            if F(h) > rem:
                break
            if path and path[-1] - h >= 5:
                continue
            visit(rem - F(h), h, path + (h,))
    visit(n, max_h, ())
    return set(answer)

def ascending_vectors(length, total, floor=0):
    if length == 0:
        if total == 0:
            yield ()
        return
    for first in range(floor, total // length + 1):
        for tail in ascending_vectors(length - 1, total - first, first):
            yield (first,) + tail

def domain_c(n):
    answer = set()
    for a in range(n + 1):
        for b in range(n + 1):
            q = a*a + 3*a*b + 3*b*b
            if q > n:
                continue
            for nu_sum in range((n - q)//3 + 1):
                mu_sum = n - q - 3*nu_sum
                for mu in ascending_vectors(a, mu_sum):
                    for nu in ascending_vectors(b, nu_sum):
                        answer.add((a, b, mu, nu))
    return answer

freeze = json.loads((ROOT/'research/rogers-ramanujan/rr004/round-1-freeze.json').read_text())
for name, expected in freeze['source_sha256'].items():
    actual = hashlib.sha256((ROOT/name).read_bytes()).hexdigest()
    assert actual == expected, (name, actual, expected)

D = {n:(domain_u(n),domain_c(n)) for n in range(13)}
assert D[0] == ({()}, {(0,0,(),())})
assert D[1] == ({(1,)}, {(1,0,(0,),())})
assert D[3][0] == {(3,), (1,1,1)}
assert D[4][0] == {(3,1), (1,1,1,1)}
assert D[7][0] == {(1,)*7, (3,)+(1,)*4, (3,3,1), (6,1)}
expected_positive = {3:{(0,1,(),(0,))}, 4:set(), 7:{(1,1,(0,),(0,))}, 9:{(0,1,(),(2,)),(1,1,(2,),(0,))}}
for n, expected in expected_positive.items():
    assert {c for c in D[n][1] if c[1]>0} == expected
for u in ((3,3,3),(6,1,1,1),(6,3),(6,3,1)):
    assert u in D[sum(u)][0]
assert (3,0,(0,0,0),()) in D[9][1]
forced = {(1,0):0,(2,0):1,(2,1):0,(3,1):1,(3,2):-1}
def charge(u):
    inverse = {F(h):h for h in range(1,13)}
    heights = tuple(inverse[x] for x in u)
    return sum(0 if h==k else forced[(h,k)] for h,k in zip(heights,heights[1:]+(0,)))
assert [charge(u) for u in ((3,3,3),(6,1,1,1),(6,3),(6,3,1))] == [1,1,0,-1]
report = {'status':'independent_literal_checks_passed','script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'frozen_hashes':'matched','counts':[{'weight':n,'U':len(u),'C':len(c),'positive_b':sum(x[1]>0 for x in c)} for n,(u,c) in D.items()], 'U_fibers':{str(n):sorted(D[n][0]) for n in (1,3,4,7,9,10)},'C_fibers':{str(n):sorted(D[n][1]) for n in (1,3,4,7,9,10)},'caveat':'Finite transcription audit, not the universal diagonal proof or a KR1 bijection.'}
path = ROOT/'.runs/rr004/critic1-independent-result.json'
with path.open('x') as stream:
    stream.write(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
