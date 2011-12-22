import euler

def digits(n):
    return [ i for i in range(10**(n-1), (10**n)) ]

def replaceLocations(n,m):
    assert(m < n)
    for p in euler.combinations(range(n+1),m):
        yield p

def combine( dig, reploc, repval ):
    digseq = euler.intToSeq(dig)
    seqn = len(digseq) + len(reploc)
    j = 0
    res = [ None for i in range(seqn) ]
    for i in range(seqn):
        if i in reploc:
            res[i] = repval
        else:
            res[i] = digseq[j]
            j += 1
    if res[0] == 0:
        return None
    return res

def getPrimes( dig, reploc ):
    vals = [ combine(dig,reploc,repval) for repval in range(10) ]
    # filter leading zeros
    vals = [ v for v in vals if v != None ]
    vals = [ euler.seqToInt(v) for v in vals ] 
    vals = [ v for v in vals if euler.isprime(v) ]
    return vals

for dig in digits(3):
    for c in euler.combinations(range(6),3):
        n = getPrimes( dig, c )
        if len(n) >= 8:
            print len(n),n
