"""
How many numbers below a googol (10^100) are not bouncy?

Question. How many increasing numbers are there < 10^n and > 10^(n-1)
    The solution can be described by a function f[n]

    For n = 1 (how many increasing numbers less than 10?)
        f[1] = 9
        f[1] = \sum_{i=1}^9 1
    For n = 2 (how many increasing numbers less than 100?)
        f[2] = f[1] + \sum_{i=1}^9 \sum_{j=i}^9 1
        f[2] = f[1] + \sum_{i=1}^9 i
    For n = 3 (how many increasing numbers less that 1000?)
        f[3] = f[2] + \sum_{i=1}^9 (\sum_{j'=1}^9 1 - \sum{j'=1}^i 1)


    This is a hopeless mess. Look for some literature on how to solve
    this in a logically consistnant manner.

    http://math.stackexchange.com/questions/177805/sums-of-sums-of-sums-of-of-numbers

    Which was totally awesome because I'd at least managed to write the
    formulas out even if I didn't actually know how to solve this

    In python:
        f = lambda n : ncr(9+n-1, n)

Question. How many decreasing numbers are there < 10^n and > 10^(n-1)

    In python:
        f = lambda n : ncr(10+n-1, n)

    (well that was easy)

Question. How many numbers are *both* increasing and decreasing less that

    numbers like:
        11, 22, 33, ...
        111, 222, 333, 444

"""

from euler import *

def increasing_numbers(m):
    return sum(ncr(9+n-1, n) for n in xrange(1, m+1))

def decreasing_numbers(m):
    return sum(ncr(10+n-1, n) for n in xrange(1, m+1)) - m

def naive_solve(limit):
    return sum(1 for i in xrange(1, 10**limit) if is_bouncy(i))

def dupsolve(limit):
    return -9*limit

def fastsolve(i):
    return (decreasing_numbers(i) + increasing_numbers(i) + dupsolve(i))

for i in xrange(1, 101):
    print fastsolve(i)





