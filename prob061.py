import euler
import collections

def triangle(n):
    return n*(n+1)/2

def square(n):
    return n*n

def pentagonal(n):
    return n*(3*n-1)/2

def hexagonal(n):
    return n*(2*n-1)

def heptagonal(n):
    return n*(5*n-3)/2

def octagonal(n):
    return n*(3*n-2)

def front(n):
    return n/100

def back(n):
    return n%100

def getVals( func ):
    lst = []
    for i in xrange(200):
        val = func(i)
        if val >= 1000 and val < 10000:
            lst.append(val)
    return lst

def makeTable():
    d = {}
    d[3] = getVals(triangle)
    d[4] = getVals(square)
    d[5] = getVals(pentagonal)
    d[6] = getVals(hexagonal)
    d[7] = getVals(heptagonal)
    d[8] = getVals(octagonal)
    return d

table = makeTable()

def succ( seq ):
    dt,t  = seq[-1]
    used  = set([ s[0] for s in seq ])
    avail = set(range(3,9)).symmetric_difference(used)
    res   = []
    for a in avail:
        for val in table[a]:
            if back(t) == front(val):
                res.append( (a,val) )    
    return res

def dfs( seq ):
    if len(seq) == 6:
        fv = seq[0][1]
        bv = seq[-1][1]
        if back(bv) == front(fv):
            return seq
    else:
        for s in succ(seq):
            res = dfs( seq + [s] )
            if res != None:
                return res

for v in table[8]:
    lst = [(8,v)]
    res = dfs(lst)
    if res != None:
        vals = [ v[1] for v in res ]
        print sum(vals)

#for a in table[8]:
#    print a, [ i for i in table[4] if back(a) == front(i) ]

#def search( src ):
#    def impl(s,used):
#        print used
#        if len(used) == 6:
#            if back(s) == front(src):
#                return []
#            else:
#                return None
#        else:
#            notused = [ j for j in range(3,9) if j not in used ]
#            for i in notused:
#                for v in getValLst()[i]:
#                    if back(s) == front(v):
#                        res = impl(v,used.union([i]))
#                        if res != None:
#                            return [v]+res
#    return impl( src, set([8]) )
#                
#for i,v in enumerate(getValLst()[8]):
#    print i,v
#    print search(v)
#       
