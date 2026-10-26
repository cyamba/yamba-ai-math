"""Executable coordinates for the proved marked six-weight cone family.

The proof is in partitions/argon-2026-10-26/cone_proof.md. This module does
not define a full KR1 map or claim that a lower-sector-free target is unused
by other higher sectors. All coordinates are literal column multiplicities.
"""
from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
import kr1

BASIS = (10, 9, 8, 6, 3, 1)


def _natural(value):
    if type(value) is not int or value < 0:
        raise ValueError('Expected a nonnegative integer coordinate')


@dataclass(frozen=True)
class ConeCoordinates:
    z: int
    y: int
    x: int
    c6: int = 0
    c3: int = 0
    c1: int = 0

    def __post_init__(self):
        for v in (self.z, self.y, self.x, self.c6, self.c3, self.c1):
            _natural(v)
        if self.y < 1 or self.x + self.z < 1:
            raise ValueError('Marked cone requires y>=1 and x+z>=1')
        if self.x + self.c6 + self.c3 + self.c1 < 1:
            raise ValueError('A height below five must follow the 9-columns')

    @property
    def head(self):
        return self.z, self.y, self.x

    @property
    def tail(self):
        return self.c6, self.c3, self.c1

    @property
    def weight(self):
        return 10*self.z + 9*self.y + 8*self.x + 6*self.c6 + 3*self.c3 + self.c1

    def columns(self):
        return tuple(v for v, count in zip(BASIS, (*self.head, *self.tail))
                     for _ in range(count))

    @classmethod
    def from_columns(cls, columns):
        if type(columns) is not tuple or any(type(v) is not int for v in columns):
            raise ValueError('Expected a canonical tuple of integer column weights')
        if columns != tuple(sorted(columns, reverse=True)) or set(columns) - set(BASIS):
            raise ValueError('Expected descending columns in the six-weight basis')
        counts = Counter(columns)
        return cls(*(counts[v] for v in BASIS))

    def lower_preimage(self):
        """Exact preimage in the literal current a<=2 map, or None.

        This is a consequence of the exhaustive forward-family classification,
        not a definition of membership by a search or a call to the old inverse.
        """
        if self.z <= 3 and self.y >= 3 and self.c6 >= 2 and self.c3 >= 2:
            k = 4*self.x + 5*self.z - 2
            nu = (self.y-3, self.y+self.c6-5, self.y+self.c6+self.c3-7)
            return kr1.ClusterData(2, 3, (k, k+self.c1), nu)
        return None

    def entire_increment_octant_avoids_lower_image(self):
        """All nonnegative (+6,+3,+1) tail increments remain lower-sector-free."""
        return self.y <= 2 or self.z >= 4


@dataclass(frozen=True)
class ConeOctant:
    base: ConeCoordinates

    def at(self, q, d3, d1):
        for v in (q, d3, d1):
            _natural(v)
        b = self.base
        return ConeCoordinates(b.z, b.y, b.x, b.c6+q, b.c3+d3, b.c1+d1)

    def recover(self, columns):
        point = ConeCoordinates.from_columns(columns)
        if point.head != self.base.head:
            raise ValueError('The target has a different head')
        offsets = tuple(a-b for a, b in zip(point.tail, self.base.tail))
        if min(offsets) < 0:
            raise ValueError('The target lies below the octant base')
        return offsets

    def intersection_witness(self, other):
        """Two full tail octants intersect iff their fixed heads agree."""
        if self.base.head != other.base.head:
            return None
        tail = tuple(max(a, b) for a, b in zip(self.base.tail, other.base.tail))
        return ConeCoordinates(*self.base.head, *tail)
