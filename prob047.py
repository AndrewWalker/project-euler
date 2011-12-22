import math
import euler

maxv = 1000000
primes = euler.sieve(maxv)

def primeFactors(n):
    factors = []
    for p in primes:
        if p > n:
            break
        if n % p == 0:
            factors.append(p)
    return factors

def sieve(n):
    nfactors = [ 0 for i in xrange(n) ]
    for p in primes:
        if p > n:
            break
        for v in xrange(p,n,p):
            nfactors[v] += 1
    return nfactors

pick = -1
nfactors = sieve(maxv)
rest = [ i for n,i in zip(nfactors,xrange(maxv)) if n == 4 ]
for i in range(len(rest)-4):
    a = rest[i] 
    b = rest[i+1]
    c = rest[i+2]
    d = rest[i+3]
    if (b-a == 1) and (c-b == 1) and (d-c == 1):
        pick = rest[i]
        break

for i in range(4):
    v = pick+i
    print v,nfactors[v],primeFactors(v)
print 'soln',pick

