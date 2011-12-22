import euler
import math
import sys

def primeFactors(n):
    if euler.isprime(n):
        return []
    v = n
    i = 2
    res = []
    while i < int(math.sqrt(v))+1:
        while (v % i) == 0:
            v = v/i
            res.append(i)
            if len(res) > 2:
                return []
        i += 1
    assert(v == 1 or euler.isprime(v))
    if v != 1:
        res.append(v)
    return res


def testpf():
    c = 0
    for i in xrange(2,10**5):
        pf = primeFactors(i)
        if len(pf) == 2:
            c+=1
        if i % 1000 == 0:
            print i,c
        

def foo(maxv):
    p = euler.sieve(maxv/2)
    print p
    c = 0
    for i in xrange(len(p)):
        for j in xrange(i,len(p)):
            if p[i]*p[j] < maxv:
                print i,j,p[i]*p[j]
                c+=1
    return c

print foo(30)
