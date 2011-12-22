import math

def prob( b, r ):
    n = (-1+b) * b
    d = (-1 + b + r) * (b + r)
    return float(n) / float(d), n*2 == d

def solve( b ):
    r  = b
    dr = b
    while dr > 0:
        dr = dr / 2 
        p,e = prob(b,r)
        if e:
            return r
        if p > 0.5:
            r += dr
        else:
            r -= dr
    return None

#for b in xrange(10,10000000):
#    r = solve(b)
#    if r:
#        print b,r
from euler import *
b = 10
lastb = None
while 1:
    r = solve(b)
    if r:
        if lastb != None:
            print 'ratio', float(b)/lastb
        lastb = b
        print b, r
        print primeFactors(b)
        print primeFactors(r)
        print gcd(b,r)
        b = int(b*5.8)
    else:
        b+=1

 
