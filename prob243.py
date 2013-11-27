# primary task
#
# make reslient number test much faster
#  how many numbers less than `d` have no factors in common with `d` (except 1 or d)

# if d is prime then resilence = 1/1
#    d will be minimised when it has lots of factors
# if d is even then all even vals less then d have a common factor
# if d is odd  then all even vals

# sieving?
# memoization?
# for n factors
#  a valid composite is: product factor_n ^ power_n
# how do you avoid duplicates
# how do you reuse work

import euler
import fractions


def resiliance(d):
    return sum(euler.gcd(i, d)==1 for i in xrange(1,d))

def resiliance_frac(d):
    return fractions.Fraction(resiliance(d), d-1)

def solve(limit):
    best = None
    i = 94744
    while 1:
        i += 1
        r = resiliance_frac(i)
        if r == 0:
            continue
        if not best or r <= best:
            best = r
            print i,  best, float(best), euler.primeFactors(i)
        if r < limit:
            break


limit = fractions.Fraction(15499, 94744)
print float(limit)
