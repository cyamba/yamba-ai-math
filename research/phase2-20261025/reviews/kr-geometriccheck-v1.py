"""Independent bounded falsification of the three frozen U cuts."""
import argparse
from collections import Counter
import json
from pathlib import Path

from importlib.util import module_from_spec, spec_from_file_location
HERE = Path(__file__).resolve().parent
spec = spec_from_file_location('critic_base',HERE / 'kr-independentcheck.py')
base = module_from_spec(spec)
spec.loader.exec_module(base)


def height(v):
    q,r = divmod(v,9)
    return 5*q+(0,1,3,6,8).index(r)


def sheets(h):
    q,r = divmod(h,5)
    return tuple(3*q+max(0,min(3,r-t)) for t in range(3))


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('bound',type=int,choices=(12,30,40))
    n=ap.parse_args().bound
    us=base.u_census(n)
    rows=sorted(us,key=lambda u:(sum(u),u))
    bad=[[],[],[]]
    qimages=set()
    for u in rows:
        hs=tuple(map(height,u))
        solid=tuple(map(sheets,hs))
        assert sum(map(sum,solid)) == sum(u)
        assert all(p[0]>=p[1]>=p[2]>=0 for p in solid)
        assert all(all(x>=y for x,y in zip(p,q)) for p,q in zip(solid,solid[1:]))
        children=(tuple(p[2] for p in solid if p[2]),u[2::3],
                  tuple(base.f(h//3) for h in hs if h//3))
        for i,c in enumerate(children):
            assert sum(c) <= n
            if c not in us:
                bad[i].append((u,c))
        qchild=children[2]
        qimages.add(qchild)
        qs=tuple(map(height,qchild))+(0,)*(len(hs)-len(qchild))
        rem=tuple(h%3 for h in hs)
        restored=tuple(3*q+r for q,r in zip(qs,rem))
        assert restored == hs
        assert sum(u)-3*sum(qchild)>=0 # finite claim only
    # Exact observed counts are reported rather than used to define a claim.
    assert not bad[2]
    assert (3,) not in qimages
    if n >= 8:
        assert bad[0][0] == ((8,),(2,))
    if n >= 28:
        assert bad[1][0] == ((9,9,9,1),(9,))
    obstruction=None
    if n >= 15:
        hs0=(3,2,2,1)
        obstruction=sorted(u for u in us if sum(u)==15
                           and len(u)>=len(hs0)
                           and all(x>=y for x,y in zip(map(height,u),hs0)))
        assert set(obstruction)=={(8,3,3,1),(6,3,3,3),(6,3,3,1,1,1)}
        assert all(base.m.old.utags(u) for u in obstruction)
    out={'bound':n,'independent_U_count':len(us),'invalid_children':[len(x) for x in bad],
         'first_failures':[x[0] if x else None for x in bad],
         'ternary_quotient_both_arithmetic_identities':True,
         'ternary_child_3_absent':True,'inclusion_obstruction_targets':obstruction,
         'residual_nonnegative':'finite observation only'}
    dest=HERE/f'kr-geometric-result-{n}.json'
    if dest.exists():
        raise FileExistsError(dest)
    dest.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out))


if __name__=='__main__':
    main()
