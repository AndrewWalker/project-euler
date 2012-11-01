import euler

def search(m):
    def solve(tlen, slen, minv=1):
        if slen == 0:
            yield []
        else:
            for i in xrange(minv, tlen):
                for soln in solve(tlen, slen-1, i):
                    yield [i] + soln

    items = [ item for item in solve(m+1, m) ]
    xitems = [ (sum(i),i) for i in items ]
    xitems.sort()
    for c, i in xitems:
        if sum(i) == euler.product(i):
            return i

#search(5)
for i in xrange(2,13):
    res = search(i)
    try:
        print i, res, sum(res)
    except:
        pass
