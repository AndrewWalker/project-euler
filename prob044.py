import math
import itertools

def take(n, iterable):
    "Return first n items of the iterable as a list"
    return list(itertools.islice(iterable, n))

def pentagonal(n):
    return (n*((3*n)-1))/2

def quadratic(a,b,c):
    discr = (b*b)-(4*a*c)
    if discr == 0:
        return (-b/(2*a))
    if discr >= 0:
        s1 = (-b - math.sqrt(discr))/(2*a)
        s2 = (-b + math.sqrt(discr))/(2*a)
        return (s1,s2)

def isSquare(n):
    sqrt = int(math.sqrt(n))
    return n - sqrt*sqrt == 0

def isPentagonal(D):
    a = 3
    b = -1
    c = -2*D
    discr = (b*b)-(4*a*c)
    if isSquare(discr) and ((-b+int(math.sqrt(discr))) % 6 == 0):
        return int(max(quadratic(a,b,c)))
    return None

def pentIter():
    k = 2
    while 1:
        for j in range(k-1,0,-1):
            yield j,k
        k += 1
        if k % 100 == 0:
            print k

for j,k in pentIter():
    s = pentagonal(j) + pentagonal(k)
    d = pentagonal(k) - pentagonal(j)
    if isPentagonal(d) and isPentagonal(s):
        print 'soln',d


