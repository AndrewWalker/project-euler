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
from euler import isprime

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

def ring_adj(tup, adj):
    r, s, p = tup
    n = (s * r + p + adj)
    m = (n/r)%6
    return (r, m, n % r)

def neighbours(n):
    r, t_s, t_p = to_hex_coord(n)
    if n == 1:
        return set([2,3,4,5,6,7])
    elif t_p == 0:
        items = [
            (r+1, t_s, t_p),
            ring_adj((r+1, t_s, t_p), -1),
            ring_adj((r+1, t_s, t_p), +1),
            ring_adj((r, t_s, t_p), -1),
            ring_adj((r, t_s, t_p), +1),
            (r-1, t_s, t_p),
        ]
        items = [ from_hex_coord(item) for item in items ]
        return set(items)
    else:
        items = [
            ring_adj((r+1, t_s, t_p), 0),
            ring_adj((r+1, t_s, t_p), +1),
            ring_adj((r-1, t_s, t_p), 0),
            ring_adj((r-1, t_s, t_p), -1),
            ring_adj((r, t_s, t_p), -1),
            ring_adj((r, t_s, t_p), +1),
        ]
        items = [ from_hex_coord(item) for item in items ]
        return set(items)

def diffs(n):
    return list(sorted(abs(n-d) for d in neighbours(n)))

def PD(n):
    return sum([1 for d in diffs(n) if isprime(d) ])

if __name__ == "__main__":
    class HexagonTests(unittest.TestCase):
        def test_diff17(self):
            self.assertEquals(diffs(17), [1,1,10,11,16,17])
        def test_PD17(self):
            self.assertEquals(PD(17), 2)
        def test_n1(self):
            self.assertEquals(neighbours(1), set([2,3,4,5,6,7]))
        def test_n2(self):
            self.assertEquals(neighbours(2), set([1,3,7,8,9,19]))
        def test_n8(self):
            self.assertEquals(neighbours(8), set([2,9,19,20,21,37]))
        def test_n10(self):
            self.assertEquals(neighbours(10), set([3,9,11,22,23,24]))
        def test_n11(self):
            self.assertEquals(neighbours(11), set([3,4,10,12,24,25]))
        def test_n15(self):
            self.assertEquals(neighbours(15), set([5, 6, 14, 16, 30, 31]))
        def test_n21(self):
            self.assertEquals(neighbours(21), set([20,22,9,8,39,40]))

    #unittest.main()
    def slow_gen():
        cnt = 0
        i = 1
        while 1:
            if PD(i) == 3:
                cnt += 1
                yield i
            i+=1

    def fast_gen():
        yield 1
        i = 1
        while 1:
            a = from_hex_coord((i, 0, 0))
            b = from_hex_coord((i, 5, i-1))
            if PD(a) == 3:
                yield a
            if PD(b) == 3:
                yield b
            i += 1

    #import itertools
    #for a, b in itertools.izip(slow_gen(), fast_gen()):
        #print a, b
    for i, v in enumerate(fast_gen()):
        print i, v
        if i == 1999:
            break
