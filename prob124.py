import euler

def rad(n):
    return euler.product(euler.primeFactors(n))

assert(rad(504) == 42)

lst = []
for i in xrange(1,100001):
    lst.append((i,rad(i)))
    #if i % 1000 == 0:
    #    print i
lst.sort( cmp = lambda a,b : cmp(a[1],b[1]) )
for i,v in enumerate(lst):
    a,b = v
    print a,b,i+1
