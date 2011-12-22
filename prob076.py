
def g( left, maxv ):
    #print 'g(%d,%d)' % (left,maxv)
    if left == 0:
        yield []
    else:
        for i in range(maxv,0,-1):
            if left-i >= 0:
                for rest in g(left-i,i):
                    yield [ i ] + rest

def glen(n):
    return len(list(g(n,n-1)))

for i in range(2,10):
    print i,glen(i)

