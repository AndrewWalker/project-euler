from euler import *

#_prime = [ i for i in  xrange(1000, 10000) if euler.isprime(i) ]

n = 4
d = 1
#for i in xrange(1, n+1):
    #cnt = 0
    #for j in choose(range(n), i):
        #print j

def digits_excluding(n, d):
    notd = [j for j in xrange(10) if j != d]
    ps = [notd for _ in xrange(n)]
    for rest in itertools.product(*ps):
        yield rest
from itertools import *
def m(n, d):
    stop = False
    for i in xrange(1, n):
        ds = list(digits_excluding(i, d))
        cs = list(choose(range(0, n), i))
        for p, q in itertools.product(ds, cs):
            base = [d for _ in xrange(n)]
            for x, y in itertools.izip(p, q):
                base[y] = x
            if isprime(seqToInt(base)):
                yield seqToInt(base)
                stop = True
        if stop:
            break

for d in xrange(10):
    s = 0
    for n in m(4, d):
        s += n
    print s
