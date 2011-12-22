import math
import euler

def bounds(n):
    a = 10**(n-1)
    b = 10**n
    lb = int(math.floor(a**(1/float(n))))
    ub = int(math.ceil(b**(1/float(n))))
    return lb,ub

def nDigitGen(n):
    lb,ub = bounds(n)
    res = []
    for i in range(lb,ub+1):
        if len(euler.intToSeq(i**n)) == n:
            res.append( (i,i**n) )
    return res

lst = []
for i in range(1,50):
    lst += nDigitGen(i)

print 'soln',len(lst)
