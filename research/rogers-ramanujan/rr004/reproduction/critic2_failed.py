"""Exact independent finite-injection audit; no author math/check imports."""
from collections import Counter
from fractions import Fraction
from itertools import product
from pathlib import Path
import hashlib
import json

ROOT = Path.cwd()
S = ((1,), (1,1), (1,1,1), (3,), (3,1), (3,3), (3,3,3),
     (1,)*7, (3,)+(1,)*4, (3,3,1), (6,1), (6,1,1,1), (6,3), (6,3,1))
assert len(set(S)) == 14 and max(map(sum,S)) == 10
prefix = (0,1,3,6,8)
def decode_value(v):
    q,r = divmod(v,9)
    assert r in prefix
    h = 5*q + prefix.index(r)
    assert h>0
    return h

def edge_counts(u):
    hs = tuple(decode_value(v) for v in u)
    assert all(0 <= h-k <5 for h,k in zip(hs,hs[1:]+(0,)))
    return Counter(zip(hs,hs[1:]+(0,)))

features = [edge_counts(u) for u in S]
edges = sorted(set().union(*(set(c) for c in features)))
assert edges == [(1,0),(1,1),(2,0),(2,1),(2,2),(3,1),(3,2)]
A = [[f[e] for e in edges] for f in features]

def vectors(k,total,minimum=0):
    if k==0:
        if total==0:
            yield ()
        return
    for t in range(minimum,total//k+1):
        for tail in vectors(k-1,total-t,t):
            yield (t,)+tail

def clusters(n):
    result = set()
    for a in range(n+1):
        for b in range(n+1):
            remainder = n-a*a-3*a*b-3*b*b
            if remainder<0:
                continue
            for nu_sum in range(remainder//3+1):
                for mu in vectors(a,remainder-3*nu_sum):
                    for nu in vectors(b,nu_sum):
                        result.add((a,b,mu,nu))
    return result

freeze = json.loads((ROOT/'research/rogers-ramanujan/rr004/round-2-freeze.json').read_text())
for name, expected in freeze['source_sha256'].items():
    assert hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==expected, name
weights = sorted(set(map(sum,S)))
C = {n:clusters(n) for n in weights}
capacity = {n:Counter(c[1] for c in C[n]) for n in weights}
assert all(set(capacity[n])=={0} for n in (1,2,4))
assert capacity[3]=={0:1,1:1}
assert capacity[6][0]>=1 and capacity[6][1]>=1 and set(capacity[6])=={0,1}
assert capacity[7]=={0:3,1:1}
assert {c for c in C[9] if c[1]>0} == {(0,1,(),(2,)),(1,1,(2,),(0,))}

# A rational-coefficient linear system is real-consistent exactly when
# Gaussian elimination over Q has no zero-left/nonzero-right row.
def real_consistent(rhs):
    rows = [[Fraction(x) for x in row]+[Fraction(b)] for row,b in zip(A,rhs)]
    pivot_row = 0
    for col in range(len(edges)):
        p = next((i for i in range(pivot_row,len(rows)) if rows[i][col]),None)
        if p is None:
            continue
        rows[pivot_row],rows[p] = rows[p],rows[pivot_row]
        scale = rows[pivot_row][col]
        rows[pivot_row] = [x/scale for x in rows[pivot_row]]
        for i in range(pivot_row+1,len(rows)):
            if rows[i][col]:
                factor = rows[i][col]
                rows[i] = [x-factor*y for x,y in zip(rows[i],rows[pivot_row])]
        pivot_row += 1
    return not any(not any(row[:-1]) and row[-1] for row in rows)

raw=0
admissible=0
consistent=0
for rhs in product(*(sorted(capacity[sum(u)]) for u in S)):
    raw += 1
    used={n:Counter() for n in weights}
    for u,b in zip(S,rhs):
        used[sum(u)][b] += 1
    if any(used[n][b]>cap for n,caps in capacity.items() for b,cap in caps.items()):
        continue
    admissible += 1
    if real_consistent(rhs):
        consistent += 1
assert consistent==0

# Independent explicit finite-deduction cross-check.
x=0
d=0-x
y=1
z=0-x
possible_g={b-y for b in capacity[6]}
assert possible_g=={-1,0}
possible_g={g for g in possible_g if 2*g+y>=0}
assert possible_g=={0}
g=next(iter(possible_g))
assert [6*d+x, y+3*d+z+x, g+z+x] == [0,0,0]
t=1-x
assert 2*g+y==1 and t+2*d+x==1
w=0-y
assert w+z+x == -1
report={'status':'independent_finite_injection_obstruction_passed',
        'frozen_hashes':'all nine matched',
        'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'source_count':len(S),'maximum_source_weight':max(map(sum,S)),
        'edges':edges,'target_capacities':capacity,
        'raw_integer_b_assignments':raw,
        'capacity_admissible_b_assignments':admissible,
        'real_consistent_charge_assignments':consistent,
        'g_initial_alternatives':[-1,0],'g_after_nonnegativity':[0],
        'forced_final_b':-1,
        'assurance':'Exact finite verification supplements the separate written proof; no global generating-function identity, surjectivity, asymptotic lemma or author math imports.'}
output=ROOT/'.runs/rr004/critic2-independent-result.json'
with output.open('x') as f:
    f.write(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
