import euler

print 'init'
N = 10**7#2*10**7
phi = euler.phisieve(N)
print 'init.'

def relevant(i):
    a = euler.intToSeq(i)
    a.sort()
    b = euler.intToSeq(phi[i])
    b.sort()
    return a==b

vbest = None
nbest = None
for n in xrange(2,N):
    if relevant(n):
        v = n/float(phi[n])
        if vbest == None or v < vbest:
            vbest = v
            nbest = n
            print vbest,nbest,phi[n]

print 'soln',nbest
    
