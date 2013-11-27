from itertools import *
from math import sqrt

def pells_eqn(x1, y1, n):
    """Generator over solutions of pells equation

    x^2 - n y^2 = 1
    """
    xk = int(x1)
    yk = int(y1)
    while 1:
        assert(xk**2 - n * yk**2 == 1)
        yield (xk, yk)
        xkn = x1 * xk + n * y1 * yk
        ykn = x1 * yk +     y1 * xk
        xk = xkn
        yk = ykn

def almost_equalaterial_triangles():
    iter = pells_eqn(2, 1, 3)
    while 1:
        x, y = iter.next()
        aTimes3 = 2 * x - 1
        areaTimes3 = y * (x - 2)
        if aTimes3 % 3 == 0 and areaTimes3 % 3 == 0:
            a = aTimes3 / 3
            tri = (a, a, int(2*sqrt(a**2 - y**2)))
            yield areaTimes3 / 3, sum(tri)

        aTimes3 = 2 * x + 1
        areaTimes3 = y * (x + 2)
        if aTimes3 % 3 == 0 and areaTimes3 % 3 == 0:
            a = aTimes3 / 3
            tri = (a, a, int(2*sqrt(a**2 - y**2)))
            yield areaTimes3 / 3, sum(tri)



lst = []
for a, p in almost_equalaterial_triangles():
    if p == 0 or a == 0:
        continue
    if p > 1000000000:
        break
    lst.append(p)
print lst
print sum(lst)
