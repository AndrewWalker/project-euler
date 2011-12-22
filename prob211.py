import euler
import math

def factors(n):
    s = euler.factors(n)
    s.add(1)
    s.add(n)
    return list(s)

def sumSqDivisors(n):
    sqd = factors(n)
    sqd = [ i*i for i in sqd ]
    return sum(sqd)

def perfectSq(n):
    sqrtn = math.sqrt(n)
    sqrtn = int(sqrtn)
    return n - sqrtn*sqrtn == 0

maxv = 64000000
lst = []
for i in xrange( 1, maxv ):
    if perfectSq(sumSqDivisors(i)):
        lst.append(i)
    if i % 1000 == 0:
        print i/float(maxv)

print lst


