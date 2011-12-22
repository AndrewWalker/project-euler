def divGenerator(divisor, dividend):
    a = divisor
    d = dividend
    while 1:
        q = a / d
        r = a % d
        yield (a,d,q,r)
        a = 10*r
        if r == 0:
            break

def longdiv(a,b):
    lst = []
    res = []
    for i,v in enumerate(divGenerator(a,b)):
        res.append(v[2])
        if v[0] in lst:
            lst.append(v[0])
            break
        else:
            lst.append(v[0])
    return res,lst

def longestCycle(n):
    a,b = longdiv(1,n)
    #print a
    #print b
    b_end      = b[-1]
    b_endidx   = len(b)-1
    b_startidx = b.index(b_end)
    #print b[b_startidx:b_endidx]
    #print a[b_startidx:b_endidx]
    return len(a[b_startidx:b_endidx])

#for i in range(1,1000):
#    print i,longestCycle(i)

lst = [ (i,longestCycle(i)) for i in range(1,1000) ]
print max(lst, key = lambda a : a[1] )

