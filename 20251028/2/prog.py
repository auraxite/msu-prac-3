from math import acos, sqrt

class Triangle:
    def __init__(self, a, b, c):
        self.a_x, self.a_y = a
        self.b_x, self.b_y = b
        self.c_x, self.c_y = c

    def dist(self, x1, y1, x2, y2):
        return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    def __abs__(self):
        ab = self.dist(self.a_x, self.a_y, self.b_x, self.b_y)
        bc = self.dist(self.b_x, self.b_y, self.c_x, self.c_y)
        ca = self.dist(self.c_x, self.c_y, self.a_x, self.a_y)
        p = (ab + bc + ca) / 2
        s2 = p * (p - ab) * (p - bc) * (p - ca)
        return sqrt(s2) if s2 >= 1e-6 else 0

    def __bool__(self):
        return abs(self) > 0

    def __lt__(self, other):
        return abs(self) < abs(other)

    def has_point(self, px, py):
        s = 0

        def angle(ax, ay, ox, oy, bx, by):
            cross = (ax - ox) * (by - oy) - (ay - oy) * (bx - ox)
            sign = 1 if cross > 0 else -1 if cross < 0 else 0

            ao = self.dist(ax, ay, ox, oy)
            bo = self.dist(bx, by, ox, oy)
            ab = self.dist(ax, ay, bx, by)
            if ao * bo == 0:
                return 0
            cosv = (ao ** 2 + bo ** 2 - ab ** 2) / (2 * ao * bo)
            cosv = max(-1, min(1, cosv))

            return sign * acos(cosv)

        s += angle(self.a_x, self.a_y, px, py, self.b_x, self.b_y)
        s += angle(self.b_x, self.b_y, px, py, self.c_x, self.c_y)
        s += angle(self.c_x, self.c_y, px, py, self.a_x, self.a_y)

        return abs(s) > 1

    def __contains__(self, other):
        if not other:
            return True
        elif not self:
            return False
        return (
            self.has_point(other.a_x, other.a_y)
            and self.has_point(other.b_x, other.b_y)
            and self.has_point(other.c_x, other.c_y)
        )

    def __and__(self, other):
        if not self or not other:
            return False

        if any(self.has_point(px, py) for px, py in
               [(other.a_x, other.a_y), (other.b_x, other.b_y), (other.c_x, other.c_y)]):
            return True
        if any(other.has_point(px, py) for px, py in
               [(self.a_x, self.a_y), (self.b_x, self.b_y), (self.c_x, self.c_y)]):
            return True

        edges1 = [
            ((self.a_x, self.a_y), (self.b_x, self.b_y)),
            ((self.b_x, self.b_y), (self.c_x, self.c_y)),
            ((self.c_x, self.c_y), (self.a_x, self.a_y))
        ]
        edges2 = [
            ((other.a_x, other.a_y), (other.b_x, other.b_y)),
            ((other.b_x, other.b_y), (other.c_x, other.c_y)),
            ((other.c_x, other.c_y), (other.a_x, other.a_y))
        ]

        def does_intersect(a1, a2, b1, b2):
            def orient(p, q, r):
                return (q[0]-p[0])*(r[1]-p[1]) - (q[1]-p[1])*(r[0]-p[0])

            o1 = orient(a1, a2, b1)
            o2 = orient(a1, a2, b2)
            o3 = orient(b1, b2, a1)
            o4 = orient(b1, b2, a2)

            if o1 * o2 < 0 and o3 * o4 < 0:
                return True

            def on_segment(p, q, r):
                return (
                    min(p[0], r[0]) <= q[0] <= max(p[0], r[0]) and
                    min(p[1], r[1]) <= q[1] <= max(p[1], r[1])
                )

            return (
                (o1 == 0 and on_segment(a1, b1, a2))
                or (o2 == 0 and on_segment(a1, b2, a2))
                or (o3 == 0 and on_segment(b1, a1, b2))
                or (o4 == 0 and on_segment(b1, a2, b2))
            )

        return any(does_intersect(e1[0], e1[1], e2[0], e2[1]) for e1 in edges1 for e2 in edges2)

import sys
exec(sys.stdin.read())