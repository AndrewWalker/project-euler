"""Project Euler 174.

Question. Given t tiles, how many square lamina exist?

Given that maximum value of

    #a^2 - b^2 = t
    #(a - b)(a + b) = t
    #a^2 + ba -ba -b^2  = t
    #sqrt(a^2 - t) = b

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

