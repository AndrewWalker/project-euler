import euler
import collections
import sys

lst = euler.sieve(10000)
lst = [ i for i in lst if i >= 1000 ]
print len(lst)

def isPerm( a, b ):
    return set( euler.intToSeq(a) ) == set( euler.intToSeq(b) )


def seqPoints(seq):
    for i in range(len(seq)):
        for j in range(i+1,len(seq)):
            for k in range(j+1,len(seq)):
                yield [ seq[idx] for idx in [i,j,k] ]

def isArithmeticSeq(seq):
    for i in seqPoints(seq):
        a,b,c = tuple(i)
        if c-b == b-a:
            return True,str(a)+str(b)+str(c)
    return False,''

d = collections.defaultdict(set)
seen = set()
for i in lst:
    if i not in seen:
        for j in lst:
            if j not in seen and i != j and isPerm(i,j):
                d[i].add(i)
                d[i].add(j)
                seen.add(i)
                seen.add(j)
    sys.stdout.write('.')
    sys.stdout.flush()
print
keys = d.keys()
keys.sort()
for k in keys:
    vals = list(d[k])
    vals.sort()
    isas,s = isArithmeticSeq(vals)
    if isas:
        print k,vals,s
            

