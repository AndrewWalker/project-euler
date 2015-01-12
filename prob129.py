import euler 
import sympy
import numpy
import time

def R(k):
    return (10**k - 1)/9

def A(n):
    for k in xrange(2, n+2):
        if R(k) % n == 0:
            return k
    assert(1==0)

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

# this is a key to this - k > n (but probably not by much)
for i in xrange(10**6, 10**7):
    if euler.gcd(i, 10) == 1:
        if fastA(i) > 10**6:
            print i


