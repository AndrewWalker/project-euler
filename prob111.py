"""Project Euler 111

Messy at this stage but it works

Question. Will a naive solution work?

    No. 10 digit numbers and prime testing. It is too big

Question. What do you really care about?

    S(n, d)
    M(n, d) - bounds problem size

    N(n, d) is only for debugging

Question. How big is the problem?

    Assuming you find solutions quickly
        when n - M(n, d) is small
    You shouldn't have too many problems
"""

from euler import *
from itertools import *

def digits_excluding(n, d):
    notd = [j for j in xrange(10) if j != d]
    ps = [notd for _ in xrange(n)]
    for rest in itertools.product(*ps):
        yield rest

def m(n, d):
    stop = False
    for i in xrange(1, n):
        ds = list(digits_excluding(i, d))
        cs = list(choose(range(0, n), i))
        for p, q in itertools.product(ds, cs):
            base = [d for _ in xrange(n)]
            for x, y in itertools.izip(p, q):
                base[y] = x
            if len(digits(seqToInt(base))) == n and isprime(seqToInt(base)):
                yield seqToInt(base)
                stop = True
        if stop:
            break

s = 0
for d in xrange(10):
    for n in m(10, d):
        s += n
print s
