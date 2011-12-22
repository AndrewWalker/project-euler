import euler

def nextAmicable(n):
    return sum(euler.properDivisors(n))

def buildAmicableChain(n):
    lst = []
    while lst == []  or n != lst[0]:
        lst.append(n)
        #print len(lst),lst[-1],euler.properDivisors(n)
        n = nextAmicable(n)
        if n > 1000000:
            return None
        if n in lst[1:]:
            return None
    lst.append(n)
    return lst

#print buildAmicableChain(12496)
for i in range(2,1000000):
    c = buildAmicableChain(i)
    if c != None:
        print i,len(c)
    
