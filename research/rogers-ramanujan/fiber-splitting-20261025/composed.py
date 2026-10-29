"""Coherent restricted extension of the exact reviewed H3 checkpoint.

The caller supplies that checkpoint's loaded module. Raw alternate encodings
in candidates.py are frozen discovery artifacts; this wrapper admits the
funded encoding only when 3 <= y <= 17, in BOTH directions.
"""
import candidates


def y2_domain(c):
    return c.a == 4 and c.b == 0 and c.mu[2] - c.mu[1] == 2


def funded_domain(c):
    try:
        _, _, y, _, _, _, _ = candidates.middle_parameters(c)
    except ValueError:
        return False
    return 3 <= y <= 17


class Extension:
    def __init__(self, h3):
        self.h3 = h3

    def domain(self, c):
        return self.h3.domain(c) or y2_domain(c) or funded_domain(c)

    def forward(self, c):
        if self.h3.domain(c):
            return self.h3.forward(c)
        if y2_domain(c):
            return candidates.y2_forward(c)
        if funded_domain(c):
            return candidates.middle_forward(c)
        raise self.h3.m.Outside('outside the explicitly proved restricted domain')

    def inverse(self, u):
        try:
            return candidates.y2_inverse(u)
        except ValueError:
            pass
        try:
            source = candidates.middle_inverse(u)
            if not funded_domain(source):
                raise ValueError('alternate y2 encoding is not in the composed image')
            return source
        except ValueError:
            return self.h3.inverse(u)
