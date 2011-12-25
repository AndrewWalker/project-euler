import math

def factors(n):
    res = set([])
    for i in xrange(1,int(math.sqrt(n))+1):
        if n % i == 0:
            res.add(i)
            res.add(n/i)
    return res

def triangular(n):
    return sum(range(n+1))

best = 0
i = 1
while 1:
    t = triangular(i)
    n = len(factors(t))
    if n > best:
        best = n
    print i,t,n,best
    if n >= 500:
        break
    i += 1

