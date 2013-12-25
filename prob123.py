from euler import *

primes = sieve(2000000)

def f(n):
    v = primes[n-1]
    a = (v-1)**n
    b = (v+1)**n
    return (a+b) % v**2


tol = 10**10
for n in xrange(20001, 22000, 2):
    print n
    if f(n) > tol:
        break
print 'soln', n
