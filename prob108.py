# http://projecteuler.net/problem=108
#
# see also: http://projecteuler.net/problem=110 for a good test case

# the key point with this problem relates to the number of prime factors of
# `n`. Unique (non-repeated) prime factors make it grow very fast, repeated
# factors make it grow more slowly.
#
# interestingly, it doesn't matter *what* the prime factors of `n` are - the
# number of unique solutions for
#  fn( 2 x 3 x 5 ) === fn( 3 x 5 x 7 )
#
# this lets you very rapidly put an upper bound on the value of `n` that you
# need to consider. Keep multiplying by increasing unique prime factors until
# you exceed the required number of prime factors.

import fractions
import euler

#def f(n):
    #for i in xrange(n, 2*n+1):
        #b = fractions.Fraction(1, n)
        #a = fractions.Fraction(1, i)
        #c = b - a
        #if c.numerator == 1:
            #yield a, c

def ffast(n):
    for i in xrange(n+1, 2*n+1):
        if i*n % (i - n) == 0:
            yield i*n/(i-n)

def fn(n):
    #return len(list(f(n)))
    return len(list(ffast(n)))

from euler import *
primes = [ p for p in xrange(100) if isprime(p) ]

def g(n):
    def impl(n):
        if n == 0:
            yield []
        else:
            for i in reversed(xrange(1, n+1)):
                for rest in impl(n-i):
                    if not rest or rest[0] <= i:
                        yield [i] + rest
    return impl(n)

def primepow(ps, qs):
    ns = [ p**q for p,q in zip(ps,qs) ]
    return product(ns)

#targ = 4000000
#best = None
#for j in xrange(2, 20):
    #print j
    #for i in g(j):
        #qs = i
        #ps = primes[:len(i)]
        #ns = [ p**q for p,q in zip(ps,qs) ]
        #n = product(ns)
        #if not best or n < best:
            #m = fn(n)
            #if m > targ:
                #print n, m, qs
                #best = n

#for i in xrange(10):
    #print fn(primepow(primes[:i], [1]*i))

def fastfn(n):
    # http://projecteuler.net/thread=108
    return (len(divisors(i**2))+1)/2



print primes[:7]
print primepow(primes[:7],[1]*7)
print primeFactors(
