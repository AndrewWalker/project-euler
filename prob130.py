import euler
import sympy

def fastA(p):
    # from http://mathlesstraveled.com/2011/11/17/fun-with-repunit-divisors-more-solutions/
    i = 1
    x = 1
    while 1:
        x = (10*x +1) % p
        i += 1
        if x == 0:
            break
    return i

import itertools

lst = []
for i in itertools.count(start = 6):
#for i in xrange(6, 10000):
    if sympy.isprime(i):
        continue
    if euler.gcd(i, 10) != 1:
        continue
    if (i-1)%fastA(i) == 0:
        lst.append(i)
    if len(lst) == 25:
        break
print sum(lst)
