import euler
import os

def primeGenerator(n):
    for i in xrange(2, n ):
        if euler.isprime(i):
            yield i

def rotations(n):
    res = []
    sn = str(n)
    for i in range(len(sn)):
        res.append( sn )
        snd = sn[1:] + sn[0]
        sn = snd
    res = [ int(r) for r in res ]
    return res

cnt = 0
for p in primeGenerator( 1000000 ):
    allprime = True
    for rot in rotations(p):
        if not euler.isprime(rot):
            allprime = False
            break
    if allprime:
        cnt += 1
        print p,cnt,rotations(p),allprime

print 'soln',cnt
