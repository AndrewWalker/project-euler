import euler

def numberChainNext(n):
    seq = euler.intToSeq(n)
    seq = [ i*i for i in seq ]
    return sum(seq)

leadsToGoal = dict()

def buildChain(n):
    lst = []
    while n not in lst:
        lst.append(n)
        n = numberChainNext(n)
        if n == 89:
            return n,lst
    return n,lst

def solve(maxv):
    cnt = 0
    for i in range(maxv):
        n = buildChain(i)
        if n == 89:
            cnt += 1
        if i % 10000 == 0:
            print i,cnt
    return cnt

def getValue(s):
    d = {}
    d['ten']     = 10
    d['hundred'] = 100        
    d['1k']   = 1000
    d['10k']  = 10000
    d['100k'] = 100000
    d['1M']   = 1000000
    d['10M']  = 10000000
    return d[s]

#mv = -1
#for i in range():
#    v = numberChainNext(i)
#    mv = max(mv,v)
#    print mv

chains = [-1 for i in range(568) ]
for i in range(1,568):
    n,seq = buildChain(i)
    chains[i] = n
print chains

maxv = getValue('10M')
cnt  = 0
for i in range(1,maxv):
    if i < 568:
        if chains[i] == 89:
            cnt += 1
    else:
        if chains[ numberChainNext(i) ] == 89:
            cnt += 1
    if i % getValue('100k') == 0:
        print i, cnt

print 'soln',cnt
