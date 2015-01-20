"""Project Euler 231 - The prime factorisation of binomial coefficients

url: https://projecteuler.net/problem=231
Status: thinking
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

Q. How to deal with fraction?
A. It removes some terms
"""
from euler import *
from collections import defaultdict
import sympy
from sympy import factorial 

def factorial_factors(n):
    merge = defaultdict(int)
    for i in xrange(2, n+1):
        fs = sympy.factorint(i)
        for k,v in fs.iteritems():
            merge[k] += v
        if i % 10000 == 0:
            print 100.0 * (float(i)/n)
    return dict(merge)

def get_value(fs):
    return product(k**v for k, v in fs.iteritems())
        
#def slow(n):
    #return sympy.factorint(sympy.factorial(n))

#n = 20000000
#c = 15000000
#print factorial_factors(n)

a = factorial_factors(200)
b = factorial_factors(150)
c = factorial_factors( 50)
print a
print b

for k, v in b.iteritems():
    a[k] -= v
for k, v in c.iteritems():
    a[k] -= v

print get_value(a)
print factorial(200)/(factorial(150)*factorial(50))


