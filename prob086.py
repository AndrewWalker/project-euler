import euler
import math
import itertools


def naive(n):
    cnt = 0
    for i in xrange(1,n+1):
        for j in xrange(i,n+1):
            for k in xrange(j,n+1):
                a = (i+j)**2 + k**2
                b = (i+k)**2 + j**2
                c = (j+k)**2 + i**2
                x = min(a,b,c)
                if euler.isSquare(x):
                    cnt += 1
    return cnt

assert( naive(99) == 1975 )
assert( naive(100) == 2060 )
for i in xrange(1, 50):
    print i, naive(i)
        
def take(n, iterable):
    "Return first n items of the iterable as a list"
    return list(itertools.islice(iterable, n))

def squares():
    for i in itertools.count(1):
        yield i**2

for s in [7225]:
#for s in take(220, squares()):
    for u in itertools.takewhile(lambda x : x < s, squares()):
        v = s - u
        if euler.isSquare(v):
            print s, math.sqrt(u), math.sqrt(v)/2
