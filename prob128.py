"""Project Euler 128 - Hexagonal Tile Differences

Question. What are the neighbours of a tile?

    Assumption. Tiles directly `up` from the tile number 1 are the `first` tile
                in each `ring`

    Question. How many tiles are there in each "ring"
    Answer.
        def f(ring_no):
            if n == 0:
                return 1
            return 6*ring_no

    Question. What is the tile number of the first tile in ring n that is up
    Answer.
        def c(n):
            return sum([f(i) for i in xrange(n)])+1

        # which you can use like this:
        def ring_slow(n):
            assert(n >= 1)
            if n == 1:
                return 0
            else:
                m = 1
                cnt = 2
                while 1:
                    cnt += 6*m
                    if n < cnt:
                        return m
                    m += 1

    Question. That isn't very nice. Can you do better?
    Answer.
        yep. the key recognition here that youve got something like a summation
            6 * sum(i for in in xrange(n)) = n*(n+1)/2

        which simplifies to:
            3 * n*(n+1) + 1

    Question. Is there a smart way to work out which ring a tile is in?
    Answer.
        yep. solve the quadratic equation from the last step
            a = 3
            b = 3
            c = 1 - tile_number

        the roots give you a fractional `ring`, which you can floor/ceil to get
        current / next ring (with some testing)

    Question. Which tiles are on a corner / side?
    Answer.
        for a tile `n`, the ring is
            r = ring(n)
        the first tile on ring `r` is:
            t_r0 = ring_first(r)
        the tile `n` is how many tiles from the first tile on the ring:
            t_r  = n - t_r0
        the tile `n` is on which side?
            t_s  = t_r / 6
        the tile `n` is on which position on the side?
            t_p  = t_r % 6
"""
import unittest
from math import *


def quadratic(a, b, c):
    y1 = (-b + sqrt(b**2 - 4*a*c ))/(2*a)
    y2 = (-b - sqrt(b**2 - 4*a*c ))/(2*a)
    return y1, y2

def ring(n):
    v = max(quadratic(3.0, 3.0, 1.0 - n))
    return int(ceil(v))

def ring_first(n):
    if n == 0:
        return 1
    else:
        r  = n-1
        return 3*r**2 + 3*r + 2

def to_hex_coord(n):
    if n == 1:
        return (0,0,0)
    r = ring(n)
    t_r0 = ring_first(r)
    t_r  = n - t_r0
    t_s  = t_r / r
    t_p  = t_r % r
    return (r, t_s, t_p)

def from_hex_coord(tup):
    r, t_s, t_p = tup
    return ring_first(r) + t_s * r + t_p

def neighbours(n):
    r, t_s, t_p = to_hex_coord(n)
    if n == 1:
        return set([2,3,4,5,6,7])
    elif t_p == 0:
        items = [
            (r+1, t_s, t_p),
        ]
        items = [ from_hex_coord(item) for item in items ]
        #print 'items=',items
        return set(items)

#for i in xrange(1, 100):
    #print i, to_hex_coord(i), from_hex_coord(to_hex_coord(i))


if __name__ == "__main__":
    class HexagonTests(unittest.TestCase):
        def test_nop(self):
            pass
        def test_n1(self):
            self.assertEquals(neighbours(1), set([2,3,4,5,6,7]))
        def test_n2(self):
            self.assert_(8 in neighbours(2))
            self.assert_(10 in neighbours(3))
            self.assert_(16 in neighbours(6))

    unittest.main()



