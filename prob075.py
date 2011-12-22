import sys
import euler
import collections
import math
import itertools

L  = 1500000
ks = euler.divisors(L)
ks = list(ks)
ks.sort()

def tri(n, m, k = 1):
    nsq = n*n
    msq = m*m
    a = k * (msq - nsq)
    b = k * 2 * m * n
    c = k * (msq + nsq)
    return (a,b,c)
def perim(n, m, k = 1):
    return 2*k*m*(m+n)
def odd(n):
    return not even(n)
def even(n):
    return n%2==0

def solve(L, k = 1):
    for n in xrange(1,L):
        for m in xrange(n+1,L):
            #t = tri(n,m,k)
            p = perim(n,m,k)
            if p > L:
                break
            yield p, (n,m,k)#t

#d = collections.defaultdict(list)
#ks = list(euler.divisors(L))
#ks.sort()
#for k in ks:
#    print k
#    for p,(n,m,k) in solve(L,k):
#        d[p].append(1)
#
#for k in sorted(d.keys()):
#    print k,'=',d[k]

def relativelyprime(m):
    return ( n for n in xrange(1,m) if euler.coprime(n,m) )

# assuming n === 1
Ms = ( 2*m*m+2*m for m in xrange(1,L) )
Ms = itertools.takewhile(lambda m : m < L, Ms)
Ms = list(Ms)
for m in Ms:
    print m, len(list(relativelyprime(m)))
#print list(Ms)
