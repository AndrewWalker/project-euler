import math

def factors(n):
    sr = math.sqrt(n)
    for i in xrange(2,int(sr)+1):
        if n % i == 0:
            yield i

src = range(2,21)
maxval = reduce( lambda a,b : a*b, src, 1)
##src = set(src)
##print maxval
##print math.sqrt(maxval)
##for i in factors(maxval):
##    val = len(src.intersection(set(factors(i))))
##    if val == len(src):
##        print 'soln',i
##        break
##    elif val > 17:
##        print i,val,src - src.intersection(set(factors(i)))
###print lst

x = 3*5*7*11*13*17*19
for i in range(100):
    print x,set(factors(x)).intersection(src)
    x *= 2
