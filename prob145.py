import euler

def revno(n):
    seq = euler.intToSeq(n)
    seq.reverse()
    m = euler.seqToInt(seq)   
    return m

def reversible(n):
    assert(n%10!=0)
    m = revno(n)
    assert(m % 10 != 0)
    seq = euler.intToSeq(n+m)
    for i in seq:
        if i % 2 != 1:
            return False
    return True
    

#print len([i for i in xrange(2,1000,2) if reversible(i) ])

lst = ( i for i in xrange(1,1000000) if i % 10 != 0 and reversible(i) )
for i,v in enumerate(lst):
    print i,v,revno(v),revno(v)+v
#print i
#        print i,revno(i),i+revno(i),reversible(i)

