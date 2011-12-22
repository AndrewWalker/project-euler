import collections

def loadKeylog():
    f = open('keylog.txt','r')
    res = [ line[:-1] for line in f ]
    f.close()
    del f
    return res

def predGraph(tups):
    res = collections.defaultdict(list)
    for src,dst in tups:
        res[dst].append(src)
        res[src] += []
    return res

lines = loadKeylog()
res = []
for line in lines:
    res.append( (line[0],line[1]) )
    res.append( (line[1],line[2]) )

res = list(set(res))
res.sort()
print 'digraph G {'
for a,b in res:
    print a,'->',b,';'
print '}'

# I did the rest by hand

