"""Reserved refinement: local common demotion fibers, no family enumeration.

The forward map is partial. Its domain is characterized by a bounded scan of
the four singleton slots of its proposed image. This does not claim that all
remaining negative sources belong to that domain.
"""
from structural import (tb, forward as old_forward, inverse as old_inverse,
                        triangle_source)


def merge_forward(h, source):
    """First eligible inverse bubble, from (3,1,1,1) to (3,2,1).

    The inverse on this image is ordinary bubble_demote at row1, so two
    different negative sources cannot collide at a merged positive tableau.
    """
    if tuple(map(len,source)) != (3,1,1,1):
        return None
    target = tb.recover(h,source,1)
    if target is not None and old_inverse(h,'321',target) is None:
        return ('321',target)
    return None


def demote(h, source):
    shape = tuple(map(len, source))
    if shape == (3,1,1,1):
        arm, label = source[0][:-1], source[0][-1]
        prefix, tail = (), tuple(r[0] for r in source[1:])
    elif shape == (2,2,1,1):
        arm = source[0]
        a, label = source[1]
        prefix, tail = (a,), tuple(r[0] for r in source[2:])
    else:
        raise ValueError('not a remaining source shape')
    split = 0
    while split < len(tail) and tb.lt_p(h, tail[split], label):
        split += 1
    leg = prefix + tail[:split] + (label,) + tail[split:]
    return (arm,) + tuple((x,) for x in leg)


def local_preimages(h, target):
    """At most seven entry extractions; not an enumeration of tableaux.

    Priority is hooks before two-column sources, then leftmost extracted
    singleton slot. A first eligible scan has a direct intrinsic inverse.
    """
    if tuple(map(len,target)) != (2,1,1,1,1):
        return ()
    if old_inverse(h, '21111', target) is not None:
        return ()
    arm, leg = target[0], tuple(r[0] for r in target[1:])
    result = []
    for i, label in enumerate(leg):
        if not tb.lt_p(h, arm[-1], label):
            continue
        source = (arm + (label,),) + tuple((x,) for x in leg[:i]+leg[i+1:])
        if (tb.validates(h,source,(3,1,1,1)) and demote(h,source) == target
                and merge_forward(h,source) is None):
            result.append(source)
    a, tail = leg[0], leg[1:]
    for i, label in enumerate(tail):
        if not tb.lt_p(h,a,label):
            continue
        source = (arm,(a,label)) + tuple((x,) for x in tail[:i]+tail[i+1:])
        if (tb.validates(h,source,(2,2,1,1)) and triangle_source(h,source) is None
                and demote(h,source) == target):
            result.append(source)
    return tuple(result)


def forward(h, source):
    shape = tuple(map(len,source))
    if shape == (5,1):
        return old_forward(h,'hook',source)
    if shape == (4,2):
        return old_forward(h,'two',source)
    if shape == (2,2,1,1):
        branch = triangle_source(h,source)
        if branch is not None:
            return old_forward(h,branch,source)
    if shape not in ((3,1,1,1),(2,2,1,1)):
        return None
    merged = merge_forward(h,source)
    if merged is not None:
        return merged
    target = demote(h,source)
    candidates = local_preimages(h,target)
    if candidates and candidates[0] == source:
        return ('21111',target)
    return None


def inverse(h,tag,target):
    old = old_inverse(h,tag,target)
    if old is not None:
        return old[1]
    if tag == '321':
        source = tb.bubble_demote(h,target,1)
        if merge_forward(h,source) == ('321',target):
            return source
    if tag == '21111':
        candidates = local_preimages(h,target)
        return candidates[0] if candidates else None
    return None
