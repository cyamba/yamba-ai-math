"""Frozen six-strip implementation verification; never declares full KR1."""
import argparse
from dataclasses import asdict
import json
from pathlib import Path
import kr1
import rr005_chains as ch
import rr005_six as six
import rr005_verify as first


def require(condition,message):
    if not condition:
        raise AssertionError(message)


def verify(ceiling=12):
    if type(ceiling) is not int or not 12 <= ceiling <= 30:
        raise ValueError('ceiling must be from 12 through 30')
    freeze=first.check_freeze('round-2-freeze.json')
    report={'program':'RR005','round':2,'full_KR1':'unresolved','ceiling':ceiling,
            'source_sha256':freeze['source_sha256'],
            'assurance':'finite exposed implementation checks; not a universal proof',
            'checks':{'U_normal_forms':0,'C_normal_forms':0,'partial_pairs':0,
                      'U_six_edges':0,'C_six_edges':0},'weights':[]}
    for n in range(ceiling+1):
        us={tuple(reversed(p)) for p in kr1.ordinary_partitions(n)
            if ch.literal_u(tuple(reversed(p)))}
        require(us == {kr1.weighted_columns(w) for w in kr1.weighted_partitions(n)},
                'literal source mismatch')
        cs=tuple(kr1.cluster_data(n)); partial=set(); fs=[]; fc=[]
        for u in sorted(us):
            form=six.split_u(u)
            require(six.f_u(form.root) and six.join_u(form) == u and
                    six.split_u(six.join_u(form)) == form,'U six normal form')
            require(sum(form.root)+form.n1+3*form.n3+6*form.n6 == n,'U weight')
            report['checks']['U_normal_forms']+=1
            if ch.e_u(u) and n+6 <= ceiling:
                raised=six.r6_u(u)
                require(ch.e_u(raised) and six.l6_u(raised)==u and sum(raised)==n+6,
                        'U six edge')
                report['checks']['U_six_edges']+=1
            expected=set(u) <= {1,3,6}
            try: c=six.partial_u_to_c(u)
            except ValueError: require(not expected,'missed low-height source')
            else:
                require(expected and c.weight==n and six.partial_c_to_u(c)==u,'partial U')
                require(c not in partial,'partial collision')
                partial.add(c); report['checks']['partial_pairs']+=1
            if six.f_u(u): fs.append(u)
        reverse=set()
        for c in cs:
            form=six.split_c(c)
            require(six.f_c(form.root) and six.join_c(form)==c and
                    six.split_c(six.join_c(form))==form,'C six normal form')
            require(form.root.weight+form.n1+3*form.n3+6*form.n6==n,'C weight')
            report['checks']['C_normal_forms']+=1
            if ch.e_c(c) and n+6 <= ceiling:
                raised=six.r6_c(c)
                require(ch.e_c(raised) and six.l6_c(raised)==c and raised.weight==n+6,
                        'C six edge')
                report['checks']['C_six_edges']+=1
            try: u=six.partial_c_to_u(c)
            except ValueError: pass
            else:
                require(u in us and six.partial_u_to_c(u)==c,'partial C')
                reverse.add(c)
            if six.f_c(c): fc.append(asdict(c))
        require(partial==reverse,'partial missing image')
        report['weights'].append({'N':n,'U':len(us),'C':len(cs),'partial':len(partial),
                                  'F_U':fs,'F_C':fc})
    # The C1 branch starts at weight 31; retain it as written proof only under
    # this round's <=30 input policy, rather than executing a larger control.
    report['C1_six_branch']='universal written argument; no finite input <=30 enables this branch'
    first.check_freeze('round-2-freeze.json')
    report['status']='six_strip_checks_passed_full_KR1_unresolved'
    return report


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--ceiling',type=int,default=12)
    parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--require-bijection',action='store_true')
    args=parser.parse_args()
    if args.output.exists(): parser.error('refusing to overwrite evidence')
    try:
        result=verify(args.ceiling); code=2 if args.require_bijection else 0
        if code: result['completion_failure']='Universal F_U/F_C root map and complete KR1 proof absent'
    except (AssertionError,ValueError,OSError,KeyError) as exc:
        result={'program':'RR005','status':'failed','error':str(exc)}; code=1
    args.output.parent.mkdir(parents=True,exist_ok=True)
    with args.output.open('x') as stream: stream.write(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':result['status']}))
    return code


if __name__ == '__main__':
    raise SystemExit(main())
