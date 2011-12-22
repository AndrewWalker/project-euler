#important. digits not required to be unique
#recursive descent backtracking? try each digit in turn

import math
import euler

tt = '1_2_3_4_5_6_7_8_9_0'

def valid(i):
    lst = [(-3,9),(-5,8),(-7,7),(-9,6),(-11,5),(-13,4)]
    #lst = [(-3,9),(-5,8),,(-11,5),(-13,4)]
    seq = euler.intToSeq(i)
    for a,b in lst:
        if seq[a] != b:
            return False
    return True

j = 1020304050607080900
k = 1929394959697989900
a = (int(math.sqrt(j))-1)
b = (int(math.sqrt(k))+2)
for x in xrange(b/100,a/100,-1):
    for y in [30,70]:
        t = x*100 + y
        if valid(t*t):
            print t*t,'*',t
            print tt
            print j
            print k
            print
#x = ( (i*10)**2 for i in xrange(a/10,b/10) if valid((i*10)**2) )

#for i in xrange(b,a,-1):
#    tmp = (i*10)**2
#    if valid(tmp):
#        print i,tmp,valid(tmp),'(',a,',',b,')'
    #print i,'\t',math.sqrt(i)

#
##def issqr(n):
##    return int(math.sqrt(n))**2 - n == 0
##
##for i in range(10):
##    j = i
##    print j,j*j*10
#
#for i in xrange(a,b):
#    #v = [ v for i,v in enumerate(euler.intToSeq(i*i)) if i % 2 == 1]
#    #if v == range(1,10) + [0]:
#    #    print 'soln',v
#    #    break
#    print i*i*100
#    if i % 100000 == 0:
#        print i
#

