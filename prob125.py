from math import *
from euler import *

def consecutive(n):
    for i in itertools.count(start=1):
        yield [i+j for j in range(n)]

lst = []
for j in xrange(2, 5000):
    for grp in consecutive(j):
        sqr = [ i**2 for i in grp ]
        sos = sum(sqr)
        if sos > 10**8:
            break
        if palindrome(sos):
            lst.append(sos)

print lst
print sum(set(lst))
