"""Attributed RR003 KR1 residue<->column endpoint using Stockhofe's map.

Implementation of Andrews--Keith arXiv:2203.05202v2, section 2, with removal
weights normalized by m before conjugation. Author-only implementation audit;
this is an established endpoint, not the unresolved U<->C bridge.
"""
import kr1

M=5


def _flat(parts):
    return (all(type(x) is int and x>0 for x in parts)
            and all(0 <= x-y < M for x,y in zip(parts,parts[1:]+(0,))))


def _minimal_regular(residues):
    result=[]
    below=0
    for residue in reversed(residues):
        below += (residue-below)%M
        result.append(below)
    return tuple(reversed(result))


def flat_to_regular(heights):
    if not isinstance(heights,(tuple,list)) or not _flat(tuple(heights)):
        raise ValueError('expected literal descending five-flat heights including tail')
    work=list(heights)
    units=[]
    for i in range(len(work)-1,-1,-1):
        if work[i]%M==0:
            below=work[i+1] if i+1<len(work) else 0
            if i==0 or work[i-1]-below<M:
                units.append(work.pop(i)//M)
    while True:
        i=next((j for j,value in enumerate(work) if value%M==0),None)
        if i is None:
            break
        value=work.pop(i)
        units.append(value//M+i)
        for j in range(i):
            work[j]-=M
    displacement=kr1.conjugate(tuple(sorted(units,reverse=True)))
    if len(displacement)>len(work):
        raise AssertionError('Stockhofe removal unit exceeds nonzero-residue length')
    result=tuple(value+M*(displacement[i] if i<len(displacement) else 0)
                 for i,value in enumerate(work))
    if tuple(work)!=_minimal_regular(tuple(x%M for x in work)):
        raise AssertionError('Stockhofe residual is not the canonical minimal regular flat partition')
    return result


def regular_to_flat(regular):
    if (not isinstance(regular,(tuple,list)) or any(type(x) is not int or x<=0 or x%M==0 for x in regular)
            or any(x<y for x,y in zip(regular,regular[1:]))):
        raise ValueError('expected descending positive five-regular partition')
    regular=tuple(regular)
    minimal=_minimal_regular(tuple(x%M for x in regular))
    displacement=tuple((x-y)//M for x,y in zip(regular,minimal))
    if any(x<0 for x in displacement) or any(x<y for x,y in zip(displacement,displacement[1:])):
        raise AssertionError('regular displacement is not a partition')
    units=kr1.conjugate(tuple(x for x in displacement if x))
    work=list(minimal)
    for unit in units:  # Descending, hence reverse order of essential removals.
        if unit <= (work[0]+M-1)//M:
            work.append(M*unit)
            work.sort(reverse=True)
            continue
        # In the essential-insertion phase every existing multiple has
        # position+ceil(value/5)>unit. A monotone boundary identifies one slot.
        positions=[i for i,x in enumerate(work,1) if i+(x+M-1)//M<=unit]
        if not positions:
            raise AssertionError('missing essential Stockhofe insertion boundary')
        prefix=max(positions)
        value=M*(unit-prefix)
        work=[x+M for x in work[:prefix]]+[value]+work[prefix:]
        if not _flat(tuple(work)):
            raise AssertionError('essential Stockhofe insertion violated flatness')
    return tuple(work)


def columns_to_residue(columns):
    kr1.decode_columns(columns)
    heights=tuple(kr1.inverse_prefix(x) for x in columns)
    regular=flat_to_regular(heights)
    return tuple(reversed(tuple(kr1.prefix_weight(x) for x in regular)))


def residue_to_columns(parts):
    if not kr1.is_residue(parts):
        raise ValueError('expected actual ascending KR1 residue partition')
    regular=tuple(kr1.inverse_prefix(x) for x in reversed(parts))
    return tuple(kr1.prefix_weight(x) for x in regular_to_flat(regular))
