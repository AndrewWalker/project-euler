import prob112
import euler
import numpy

def increasingGen(ndigits,lb):
    if ndigits == 0:
        yield []
    else:
        for i in range(lb,9):
            for rest in increasingGen(ndigits-1,i):
                yield [i] + rest

def increasingCnt(ndigits):
    cnt = 0
    for i in increasingGen(ndigits,1):
        cnt += 1
    return cnt

def increasingCnt2(ndigits,src):
    lst = [ i*src for i in range(1,10)]
    print lst
    return sum(lst)

print increasingCnt2(1,1),increasingCnt(3)

#x = range(2,10)
#y = [ increasingCnt(i) for i in x ]
#for xi,yi in zip(x,y):
#    print xi,yi

#import matplotlib
#matplotlib.use('Cairo')
#import pylab
#pylab.plot(x,y)
#pylab.savefig('out.png')

#print numpy.polyfit(x,y,2)
