from euler import *

def row_naive(i):
    lst = []
    for j in xrange(i+1):
        res = ncr(i, j) % 7 == 0
        lst.append(not res)
    return lst

def to_string(lst):
    res = []
    for item in lst:
        if item:
            res.append('X')
        else:
            res.append('.')
    return ''.join(res)

def int2seq(x, base):
    res = []
    while x:
        res.append( x % base )
        x /= base
    res.reverse()
    return res

def padseq(seq, maxlen, padchar):
    return [padchar] * (maxlen-len(seq)) + list(seq)

def row_count(n):
    lst = [0] + int2seq(n, 7)
    lst = [ i+1 for i in lst ]
    return product(lst)

def solve(a, b):
    cnt = 0
    for j in xrange(a, b):
        cnt += row_count(j)
    return cnt

#print solve(10**6)
#print math.log(10**9 / 10**6, 7)
#print 7**5
#for i in xrange(1,10000):
    #a = solve(i)
    #b = sum(range(1,i+1))
    #print i,
    #print a,
    #print b,
    #print a / float(b)
#print sum(range(101))

#n = 100
#for i in xrange(n):
    #print row_count(i)


#j = -1
#for i in xrange(10):
    #j += 343
    #lst = [0] + int2seq(j, 7)
    #lst = [k+1 for k in lst]
    #print lst
import sys
step  = 7**5
start = -1 + step
while start + step < 10**9:
    print start
    lst = [0] + int2seq(start, 7)
    lst = [k+1 for k in lst]
    print product(lst[:-5])
    sys.stdout.flush()
    start += step
#print solve(0,i)
#print solve(i,i*2)/2.


