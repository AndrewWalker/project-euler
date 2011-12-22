import euler
import sys

f = { 0 : 1 }
for i in range(1,10):
    f[i] = i * f[i-1]

def val(d=4):
    if d == 0:
        yield []
    else:
        for i in range(10):
            for rest in val(d-1):
                yield [i] + rest

def seqToInt( seq ):
    return int( ''.join( [ str(i) for i in seq ] ) )

def intToSeq(n):
    if n == 0:
        return [0]
    else:
        lst = []
        while n != 0:
            lst = [ n % 10 ] + lst
            n = n / 10
        return lst

for i in xrange(10**8):
    v0 = intToSeq(i)
    v1t = [ f[x] for x in v0 ]
    v1 = sum(v1t)
    if i == v1:
        print i, v1t
    if i % 100000 == 0:
        print i
