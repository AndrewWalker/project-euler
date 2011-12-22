import euler

def tleft(n):
    seq = euler.intToSeq(n)
    return [ seq[:i] for i in range(1,len(seq)+1) ]

def tright(n):
    seq = euler.intToSeq(n)
    return [ seq[i:] for i in range(0,len(seq)) ]

def tall(n):
    return tleft(n) + tright(n)

res = []        
for n in euler.sieve(4000):
    if n > 7:
        seq = tall(n)
        seq = [ euler.seqToInt(x) for x in seq ]
        seq = [ euler.isprime(x) for x in seq ]
        val = reduce( lambda a,b : a and b, seq, True )
        if val:
            res.append(n)
            print n,seq

print 'soln',sum(res) + 739397
    #if sum([ 1 for x in seq if not euler.isprime(x) ]) == 0:
    #    print n
