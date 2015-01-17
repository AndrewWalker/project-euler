"""Project Euler 351 - 

url: https://projecteuler.net/problem=351
status: started
keywords: symmetry
"""

import euler

def orcharditer( n ):
    for y in xrange(n):
        for x in xrange(n-y):
            yield (2*(x+1)+y,y)

#def alt_iter(n):
    #for row_num in xrange(n+1):
        #for row_item in xrange(1, row_num):
            #x = row_num * 2 - row_item
            #y = row_item
            #yield (x, y)

def h(n):
    cnt = 0
    for x, y in orcharditer(n):#alt_iter(n):
        gcd = euler.gcd(x, y)
        if gcd > 1:
            xd = x / gcd
            yd = y / gcd
            if (xd + yd) % 2 == 0:
                cnt += 1
    return (cnt + n -1) * 6

#print h(10)
def valid( pt, n ):
    return  pt[0]+pt[1] <= 2*n

def solve( n ):
    found = set()
    for item in orcharditer(n):
        if item not in found:
            for k in xrange(2,n):
                newpt = (k*item[0], k*item[1])
                if not valid(newpt, n):
                    break
                found.add(newpt)
    #for item in found:
    #    print item
    return len(found)*6+6

def solveb( n ):
    cnt = 0
    for item in orcharditer(n):
        div = euler.gcd(item[0],item[1])
        if div > 1 and max(item[0],item[1])>0:
            #print item, div
            sumitem = (item[0]/div + item[1]/div)
            if sumitem%2 == 0:
                cnt += 1
    return cnt*6 + 6*n


#assert solve(5) == 30
#assert solve(10) == 138
##print solve(1000)
#for i in xrange(1,10):
    #print '%d,' % solveb(i),
##solveb(100000)
lst = []
for i in xrange(5, 400):
    print i
    lst.append(solve(i)/6)
import numpy
import matplotlib.pyplot as plt
lst = numpy.array(lst)
plt.plot(lst[1:]-lst[:-1],'.')
plt.show()
