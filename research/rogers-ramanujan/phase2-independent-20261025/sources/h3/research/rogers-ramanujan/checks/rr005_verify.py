"""Frozen RR005 chain implementation checks; complete KR1 stays unresolved."""
import argparse
from dataclasses import asdict
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import kr1
import rr005_chains as ch

ROOT = Path(__file__).resolve().parents[3]
PHASE = ROOT / 'research/rogers-ramanujan/rr005'


def require(value, message):
    if not value:
        raise AssertionError(message)


def check_freeze(name='round-1-freeze.json'):
    data = json.loads((PHASE/name).read_text())
    for path, sha in data['source_sha256'].items():
        require(hashlib.sha256((ROOT/path).read_bytes()).hexdigest() == sha,
                'frozen source changed: '+path)
    return data


def verify(ceiling):
    if type(ceiling) is not int or not 12 <= ceiling <= 30:
        raise ValueError('ceiling must be from 12 through 30')
    freeze = check_freeze()
    report = {'program':'RR005','ceiling':ceiling,'full_KR1':'unresolved',
              'started_utc':datetime.now(timezone.utc).isoformat(),
              'assurance':'exposed finite implementation checks; universal claims require written proof and review',
              'source_sha256':freeze['source_sha256'],'weights':[],
              'checks':{'U_normal_forms':0,'C_normal_forms':0,'partial_pairs':0,'raising_round_trips':0}}
    for n in range(ceiling+1):
        # Ordinary-size literal search and the W path are different algorithms.
        us = {tuple(reversed(p)) for p in kr1.ordinary_partitions(n)
              if ch.literal_u(tuple(reversed(p)))}
        from_w = {kr1.weighted_columns(w) for w in kr1.weighted_partitions(n)}
        require(us == from_w, 'literal U mismatch')
        cs = tuple(kr1.cluster_data(n))
        eu = []; ec = []; partial = []
        for u in sorted(us):
            f = ch.split_u(u)
            require(ch.e_u(f.root) and ch.join_u(f) == u and ch.split_u(ch.join_u(f)) == f,
                    'U normal-form round trip')
            require(sum(f.root)+f.n1+3*f.n3 == n, 'U split weight')
            require(ch.l1_u(ch.r1_u(u)) == u, 'U unit inverse')
            require(sum(ch.r1_u(u)) == n+1, 'U unit weight')
            report['checks']['U_normal_forms'] += 1
            report['checks']['raising_round_trips'] += 1
            if ch.d_u(u):
                v=ch.r3_u(u)
                require(ch.d_u(v) and ch.l3_u(v) == u and sum(v) == n+3, 'U triple inverse')
                report['checks']['raising_round_trips'] += 1
            expected = set(u) <= {1,3,6} and u.count(6) <= 1
            try:
                c=ch.partial_u_to_c(u)
            except ValueError:
                require(not expected, 'missed restricted source')
            else:
                require(expected and c.weight == n and ch.partial_c_to_u(c) == u,
                        'restricted U round trip')
                partial.append(c)
                report['checks']['partial_pairs'] += 1
            if ch.e_u(u): eu.append(u)
        require(len(set(partial)) == len(partial), 'partial collision')
        seen_c = set()
        for c in cs:
            f=ch.split_c(c)
            require(ch.e_c(f.root) and ch.join_c(f) == c and ch.split_c(ch.join_c(f)) == f,
                    'C normal-form round trip')
            require(f.root.weight+f.n1+3*f.n3 == n, 'C split weight')
            require(ch.l1_c(ch.r1_c(c)) == c and ch.r1_c(c).weight == n+1, 'C unit inverse')
            report['checks']['C_normal_forms'] += 1
            report['checks']['raising_round_trips'] += 1
            if ch.d_c(c):
                v=ch.r3_c(c)
                require(ch.d_c(v) and ch.l3_c(v) == c and v.weight == n+3, 'C triple inverse')
                report['checks']['raising_round_trips'] += 1
            try: u=ch.partial_c_to_u(c)
            except ValueError: pass
            else:
                require(u in us and ch.partial_u_to_c(u) == c, 'restricted C round trip')
                seen_c.add(c)
            if ch.e_c(c): ec.append(asdict(c))
        require(seen_c == set(partial), 'partial missing image')
        report['weights'].append({'N':n,'U':len(us),'C':len(cs),'partial':len(partial),
                                  'E_U':eu,'E_C':ec})
    # Direct boundary controls, not an enumeration above the declared ceiling.
    boundary=(9,1)
    require(ch.r3_u(boundary) == (10,3) and ch.l3_u((10,3)) == boundary,
            'terminal replacement boundary')
    require(ch.e_u((18,10,3)), 'higher bridge must block the tempting inverse')
    require(ch.partial_u_to_c((6,3)) == kr1.ClusterData(3,0,(0,0,0),()), 'weight-nine core')
    require(ch.partial_u_to_c((6,3,1)) == kr1.ClusterData(3,0,(0,0,1),()), 'weight-ten context')
    for bad in ((9,), (10,), (10,1), (11,), (3,6), (True,), [1]):
        require(not ch.literal_u(bad), 'malformed U accepted')
    check_freeze()
    report.update(status='chain_checks_passed_full_KR1_unresolved',
                  high_weight_direct_controls=[{'U':[18,10,3],'weight':31,'purpose':'terminal inverse rejection; not a sweep'}])
    return report


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--ceiling',type=int,default=12)
    parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--require-bijection',action='store_true')
    args=parser.parse_args()
    if args.output.exists(): parser.error('refusing to overwrite evidence')
    try:
        result=verify(args.ceiling)
        code=2 if args.require_bijection else 0
        if code: result['completion_failure']='Residual root map and complete KR1 proof absent'
    except (AssertionError, ValueError, OSError, KeyError) as exc:
        result={'program':'RR005','status':'failed','error':str(exc)}
        code=1
    args.output.parent.mkdir(parents=True,exist_ok=True)
    with args.output.open('x') as stream: stream.write(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ('status',)}) )
    return code


if __name__ == '__main__':
    raise SystemExit(main())
