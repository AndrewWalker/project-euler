import euler
import itertools
import math

def take(n, iterable):
    "Return first n items of the iterable as a list"
    return list(itertools.islice(iterable, n))

def oddComposite():
    i = 3
    while 1:
        if not euler.isprime(i):
            yield i
        i += 2

def squares(n):
    lst = [ i*i*2 for i in range(1,int(math.sqrt(n/2))+1) if i*i*2 < n ]
    lst.reverse()
    return lst

def goldbach(n):
    for sq in squares(n):
        if euler.isprime(n - sq):
            #print n,int(math.sqrt(sq/2)),n-sq
            return True
    return False
#print dir(itertools)
#print take(20,oddComposite())
#print squares(85)
#print goldbach(9)
#print goldbach(15)
for i in oddComposite():
    if not goldbach(i):
        print 'soln',i
        break
    if i % 1000 == 0:
        print i

print goldbach(5777)
