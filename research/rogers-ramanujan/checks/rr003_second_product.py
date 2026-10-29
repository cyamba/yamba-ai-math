"""RR003 auxiliary (epsilon,P2) <-> P1 disjoint-union cut objects.

Attributed anti-telescoping / Garsia--Milne method. Universal author argument
in second-product-involution.md; novelty and separate semantic review outstanding.
This is one auxiliary source branch, NOT a complete KR1 bijection.
No partition enumeration, rank lookup or visited-state table defines a map.
"""
from dataclasses import dataclass,replace


@dataclass(frozen=True)
class Cut:
    j: int
    parts: tuple

    @property
    def weight(self):
        return 9*self.j+7+sum(self.parts)


@dataclass(frozen=True)
class State:
    layer: int
    kind: str
    j: int
    mask: int
    marks: frozenset
    parts: tuple


def _pair(kind,j):
    return (9*j+8,9*j+10) if kind=='Q' else (9*j+7,9*j+11)


def _bits(mask,pair):
    return frozenset(x for i,x in enumerate(pair) if mask & (1<<i))


def _frame(kind,j,marks,parts):
    pair=_pair(kind,j)
    mask=sum(1<<i for i,x in enumerate(pair) if x in marks)
    return State(1,kind,j,mask,frozenset(marks)-frozenset(pair),parts)


def _toggle(parts,marks,coin):
    values=list(parts)
    marks=set(marks)
    if coin in marks:
        marks.remove(coin)
        values.append(coin)
        values.sort()
    else:
        values.remove(coin)
        marks.add(coin)
    return tuple(values),frozenset(marks)


def alpha(state,length):
    """Telescope edges on layers 0/1; denominator cancellation on layer 2."""
    if state.layer==0:
        return _frame('Q',length-1,state.marks,state.parts) if state.kind=='A' else _frame('P',0,state.marks,state.parts)
    if state.layer==1:
        marks=state.marks | _bits(state.mask,_pair(state.kind,state.j))
        if state.kind=='Q':
            if state.j==length-1:
                return State(0,'A',0,0,marks,state.parts)
            return _frame('P',state.j+1,marks,state.parts)
        if state.j==0:
            return State(0,'B',0,0,marks,state.parts)
        return _frame('Q',state.j-1,marks,state.parts)
    coins={1,3}
    for i in range(state.j):
        coins.update(_pair('Q',i))
    for i in range(state.j+1,length):
        coins.update(_pair('P',i))
    marks=state.marks | _bits(state.mask,(1,3))
    eligible=coins & (set(state.parts)|marks)
    if not eligible:
        return state
    parts,marks=_toggle(state.parts,marks,min(eligible))
    mask=sum(1<<i for i,x in enumerate((1,3)) if x in marks)
    return replace(state,mask=mask,marks=marks-{1,3},parts=parts)


def beta(state,length):
    """Endpoint cancellation on layer 0; local polynomial edges on 1/2."""
    if state.layer==0:
        coins=set()
        for i in range(length):
            coins.update(_pair('Q' if state.kind=='A' else 'P',i))
        eligible=coins & (set(state.parts)|state.marks)
        if not eligible:
            return state
        parts,marks=_toggle(state.parts,state.marks,min(eligible))
        return replace(state,parts=parts,marks=marks)
    if state.layer==1:
        if state.mask in (0,3):
            return replace(state,kind='P' if state.kind=='Q' else 'Q')
        mask=state.mask if state.kind=='Q' else (0 if state.mask==1 else 3)
        return State(2,'',state.j,mask,state.marks,state.parts)
    kind,mask=(('P',1),('Q',1),('Q',2),('P',2))[state.mask]
    return State(1,kind,state.j,mask,state.marks,state.parts)


def state_weight(state):
    total=sum(state.parts)+sum(state.marks)
    if state.layer==1:
        total+=sum(_bits(state.mask,_pair(state.kind,state.j)))
    elif state.layer==2:
        total+=9*state.j+7+sum(_bits(state.mask,(1,3)))
    return total


def state_sign(state):
    parity=(len(state.marks)+state.mask.bit_count())%2
    base=(1 if state.kind=='A' else -1) if state.layer==0 else (-1 if state.kind=='Q' else 1) if state.layer==1 else 1
    return base*(-1 if parity else 1)


def _walk(state,first,weight,audit=False):
    length=weight//9+1
    next_edge=first
    steps=0
    while True:
        operation=alpha if next_edge=='alpha' else beta
        following=operation(state,length)
        if following==state:
            return state,steps
        if audit:
            if operation(following,length)!=state or state_weight(following)!=weight or state_sign(following)!=-state_sign(state):
                raise AssertionError(('edge invariant',next_edge,state,following))
        state=following
        next_edge='beta' if next_edge=='alpha' else 'alpha'
        steps+=1


def _partition(parts,residues):
    return (isinstance(parts,(tuple,list)) and all(type(x) is int and x>0 and x%9 in residues for x in parts)
            and all(x<=y for x,y in zip(parts,parts[1:])))


def _start(parts,kind):
    return State(0,kind,0,0,frozenset(),tuple(parts))


@dataclass(frozen=True)
class Packet:
    epsilon: int
    parts: tuple

    @property
    def weight(self):
        return self.epsilon+sum(self.parts)


def _packet_to_t(packet):
    if (not isinstance(packet,Packet) or type(packet.epsilon) is not int or packet.epsilon not in (0,1)
            or not _partition(packet.parts,{2,3,6,7})):
        raise ValueError('expected epsilon in {0,1} and an actual P2 partition')
    count=packet.parts.count(2)
    return tuple(sorted(tuple(x for x in packet.parts if x!=2)+(1,)*(2*count+packet.epsilon)))


def _t_to_packet(parts):
    count=parts.count(1)
    quotient,remainder=divmod(count,2)
    return Packet(remainder,tuple(sorted(tuple(x for x in parts if x!=1)+(2,)*quotient)))


def split_packet(packet,*,audit=False,with_steps=False):
    parts=_packet_to_t(packet)
    endpoint,steps=_walk(_start(parts,'A'),'alpha',packet.weight,audit)
    if endpoint.layer==0 and endpoint.kind=='B':
        result=('P1',endpoint.parts)
    elif endpoint.layer==2 and not endpoint.marks and not endpoint.mask:
        result=('L',Cut(endpoint.j,endpoint.parts))
    else:
        raise AssertionError(('unexpected packet endpoint',endpoint))
    return (result,steps) if with_steps else result


def join_p1(parts,*,audit=False,with_steps=False):
    if not _partition(parts,{1,3,6,8}):
        raise ValueError('expected actual KR1 P1 residue partition')
    endpoint,steps=_walk(_start(parts,'B'),'alpha',sum(parts),audit)
    if endpoint.layer!=0 or endpoint.kind!='A':
        raise AssertionError(('unexpected P1 endpoint',endpoint))
    result=_t_to_packet(endpoint.parts)
    return (result,steps) if with_steps else result


def is_cut(cut):
    if not isinstance(cut,Cut) or type(cut.j) is not int or cut.j<0:
        return False
    if not _partition(cut.parts,{1,2,3,6,7,8}):
        return False
    for x in cut.parts:
        residue=x%9
        if residue in (3,6):
            if x==3:
                return False
        elif residue==7:
            if x//9>cut.j:
                return False
        elif residue==2:
            if x<11 or (x-11)//9>cut.j:
                return False
        elif residue==8:
            if x//9<cut.j:
                return False
        elif x<10 or (x-10)//9<cut.j:
            return False
    return True


def join_cut(cut,*,audit=False,with_steps=False):
    if not is_cut(cut):
        raise ValueError('expected an actual auxiliary L cut object')
    start=State(2,'',cut.j,0,frozenset(),tuple(cut.parts))
    endpoint,steps=_walk(start,'beta',cut.weight,audit)
    if endpoint.layer!=0 or endpoint.kind!='A':
        raise AssertionError(('unexpected L cut endpoint',endpoint))
    result=_t_to_packet(endpoint.parts)
    return (result,steps) if with_steps else result
