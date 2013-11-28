import math

def factors(n):
    sr = math.sqrt(n)
    for i in xrange(2,int(sr)+1):
        if n % i == 0:
            yield i

src = range(2,21)
maxval = reduce( lambda a,b : a*b, src, 1)

x = 3*5*7*11*13*17*19
for i in range(100):
    print x,set(factors(x)).intersection(src)
    x *= 2
