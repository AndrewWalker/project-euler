import math

#top = 10**9
#num = 1
#for iprime in xrange(top):
    #i = iprime + 1
    #num *= i
    #while num % 10 == 0:
        #num /= 10
    #num %= 10**5
    #if i % 1000000 == 0:
        #print i, num, math.log10(i)

#nums = []
#num = 1
#for i in xrange(1, 10**5+5):
    #num *= i
    #while num % 10 == 0:
        #num /= 10
    #num %= 10**5
    #if i < 20 or i > 10**5-20:
        #print i, num
    #nums.append(num)

#print nums
digits = 4
num = 1
for i in xrange(1, 10**6+1):
    num *= i
    while num % 10 == 0:
        num /= 10
    num %= 10**digits

print num
