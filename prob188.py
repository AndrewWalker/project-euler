"""Project Euler 188 Hyperexponentiation

Question. What does a naive implementaiton look like?

    def hyperexponentiation(a, b):
        if b == 1:
            return a
        else:
            return a**hyperexponentiation(a, b-1)

    print hyperexponentiation(3, 2)
    print hyperexponentiation(3, 3)
    print hyperexponentiation(3, 4) # too slow

Question. Where should I look for help?

    Wikipedia
    http://en.wikipedia.org/wiki/Tetration#Iterated_powers_vs._iterated_bases.2Fexponentiation

    "When a and 10 are coprime, we can compute the last m decimal digits of
     a^^n using Euler's Theorem"

Question. Does the case we care about fall into this category?

    print coprime(1777, 10)
    > True

    Yes. Guessing this is a good hint
    googling around, yep, looks like this is a well trodden path
"""
from euler import *

def fastpower(num, power):
    return num**power

def tetration(num, tetrate):
    product = 1
    if tetrate == 0:
        return product
    product = number
    while(tetrate > 1):
        product = fastpower(number, product)
        tetrate -= 1
    return product


#print totient(100000)
#print 222/4
#print 222%4


def fp(a, p, n):
    assert(coprime(a, n))
    phi_n = totient(n)
    q = p % phi_n
    return  (a**q) % n

lim = 10**9
print 3**3
print fp(3, fp(3, 3, lim), lim)
