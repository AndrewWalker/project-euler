"""Project Euler 131

There are some prime values, p, for which there exists a positive integer, n,
such that the expression n^3 + p n^2 is a perfect cube.

For example, when p = 19, 8^3 + 8^2x19 = 12^3.

What is perhaps most surprising is that for each prime with this property the
value of n is unique, and there are only four such primes below one-hundred.

How many primes below one million have this remarkable property?

Question. Are there any interesting properties?

 n^3 + p n^2 = k^3
 n^2 (n + p) = k^3
 p is prime
 p > 0
 n > 0
 k^3 is divisible by n^2
 k^3 is greater than n^3
 (k^3 - n^3) is divisible by n^2

 k^3 = c n^2 + n^3

 by observation n is a perfect cube

 the difference between two perfect cubes is a perfect square
"""

import euler
import math

def perfect_cube(n):
    cbrt = int(math.ceil(n**(1/3.)))
    return cbrt**3 == n

def f(p):
    lst = range(1, int((300*p)**(1./3)))
    for nprime in lst:
        n = nprime**3
        v = n**3 + n**2 * p
        if perfect_cube(v):
            print n, p, n/float(p)
            return True
    return False

cnt = 0
for i in euler.primes_less_than(10**6):
    if f(i):
        cnt += 1
        print i, cnt


