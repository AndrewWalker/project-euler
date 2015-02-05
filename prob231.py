"""Project Euler 231 - The prime factorisation of binomial coefficients

url: https://projecteuler.net/problem=231
Status: complete
Keywords: binomial, factors, prime, factorial

See also:

    http://blog.janmr.com/2010/10/prime-factors-of-factorial-numbers.html

Q. What is the definition of a term in the binomial coefficients 
A. This: 

    http://en.m.wikipedia.org/wiki/Binomial_coefficient

But not this:

    http://en.m.wikipedia.org/wiki/Binomial

Q. Give the equation
A. 

    n! / (k!(n-k)!)

Q. Is there a fast way to get the prime factors of a factorial?
A. Yep,

    Split the factorial into a product of terms
    Factor each term individually

Q. Is that fast enough?
A. Gets you within an order of magnitude in the minute, but still too slow

Q. Is there a better way?
A. Research!

    See Prime Factors of Binomial Coefficients (Riasat)

    Which describes the technique used here (first suggested by Legendre)

Retrospective
-------------

Pros:
    - code was easy to write
    - had a genuinely good idea about how to speed it up without research

Cons:
    - this wasn't the first go at this one. Not sure what the problem was previously
    - it was pretty easy.
    - this one got forgotten for a while, mainly because it was mostly solved
      by research. 

"""
from euler import *
from collections import defaultdict
import sympy
from sympy import factorial 

       
def prime_exponent(factorial_n, p):
    i = 1
    cumsum = 0
    while 1:
        ki = int(math.floor(factorial_n / float(p**i)))
        cumsum += ki
        if ki == 0:
            break
        i += 1
    return cumsum

def opt_factorial_factors(factorial_n):
    prime_factors = {}
    for i in xrange(1, sympy.primepi(factorial_n)+1):
        p = sympy.prime(i)
        k = prime_exponent(factorial_n, p)
        prime_factors[p] = k
    return prime_factors

def sum_of_prime_factors(pfs):
    return sum(p*exponent for p, exponent in pfs.iteritems())

n = 20000000
k = 15000000
nf  = opt_factorial_factors(n)
kf  = opt_factorial_factors(k)
nkf = opt_factorial_factors(n-k)

for k, v in kf.iteritems():
    nf[k] -= v
for k, v in nkf.iteritems():
    nf[k] -= v
#print nf
print sum_of_prime_factors(nf)

