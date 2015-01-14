"""Project Euler 174.

https://projecteuler.net/problem=174
https://github.com/AndrewWalker/project-euler/blob/master/prob174.py

Q. What's hard?
A. Picking out all solutions in the form

x^2 - y^2 = n

For an arbitrary n

Q. Is the equation familiar?
A. Yep, it's a modified Pell equation 

x^2 - N y^2 = k

Q. Any good reading?
A. Yep,

http://en.m.wikipedia.org/wiki/Pell%27s_equation
http://www.ams.org/notices/200202/fea-lenstra.pdf

Looking at some stuff Euler links to in the forums 
    https://www.ocf.berkeley.edu/~wwu/cgi-bin/yabb/YaBB.cgi?board=riddles_medium
"""
from euler import *

def largest_outside_square(area):
    return area / 4 + 1

def base(n):
    if n%2 == 1:
        return 1
    else:
        return 2

import collections
tmax = 1000001
d = collections.defaultdict(int)
for t in xrange(8, tmax):
    cnt = 0
    n = largest_outside_square(t)
    low = int(math.ceil(math.sqrt(t)))
    for a in xrange(low, n+1):
        bsq = a**2 - t
        if bsq > 0 and is_square(bsq):
            b = isqrt(bsq)
            if (a - b) % 2 == 1:
                cnt += 1
    d[cnt] += 1
    if t % 1000 == 0:
        print t/float(tmax-1), d
        print low, n
        print
print d

