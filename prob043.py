import euler
import itertools

def foo(n):
    res = []
    for i in range(100,1000):
        if i % n == 0:
            s = euler.digits(i)
            if len(set(s)) == 3:
                res.append(s)
    return res

def validPandigital():
    for a in foo(2):
        for b in foo(7):
            for c in foo(17):
                s = set(a+b+c)
                if len(s) == 9:
                    last = list(set(range(10)) - s)[0]
                    x = [last] + a + b + c
                    yield x

def substringProps( seq ):
    lst = [ (i,i+3) for i in range(1,8) ]
    div = [2,3,5,7,11,13,17]
    for divisor,pair in zip(div,lst):
        sub = seq[pair[0]:pair[1]]
        val = euler.seqToInt( sub )
        if val % divisor != 0:
            return False
    return True

res = []
for x in validPandigital():
    if substringProps(x):
        print x
        res.append( euler.seqToInt(x) )

print 'soln',sum(res)
