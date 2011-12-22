import euler


def phisieve(nmax):
    ts=range(nmax)
    for i in xrange(2,nmax):
        if ts[i]==i: #Prime, as it hasn't been divided by anything lower.
            ts[i]-=1 #Primes are coprime to everything below them.
            #Factor i into the totients of its multiples.
            for j in xrange(i+i,nmax,i):
                ts[j] = (ts[j]*(i-1))//i
    return ts


nmax = 10**7
phi = phisieve(nmax)
sys.exit(0)

def relevant(i):
    a = euler.intToSeq(i)
    a.sort()
    b = euler.intToSeq(phi[i])
    b.sort()
    return a==b

for i in range(2,nmax):
    pass
    #if relevant(i):
    #    print i

#s = makesieve(10000)
#for i in range(2,10):
#    print i,s[i],i/float(euler.totient(i))
    #if euler.isprime(i):
    #    print i,euler.totient(i)


