import euler
import math

#N    = 50000000
#pmax = int(math.floor(N**(1/2.)))
#primes = euler.sieve(pmax+1)
#
#def ipow(n,p):
#    return int(math.ceil(N**(1/float(p))))
#
#def solve(nmax):
#    lst = []
#    for i in range(2,ipow(nmax,4)):
#        for j in range(2,ipow(nmax,3)):
#            for k in range(2,ipow(nmax,2)):
#                v = i**4 + j**3 + k**2
#                if v >= nmax:
#                    break
#                else:
#                    lst.append((v,(i,j,k)))
#                    #print v,i,j,k
#            v = i**4 + j**3
#            if v > nmax:
#                break
#    return lst
#
##lst = solve(1000)
##lst.sort()
##for i in lst:
##    print i
#
#v0 = 50000000
#v1 = 50
#
#print 4**10
#print v0
#print math.sqrt(v0)
#primes = euler.sieve( int(math.sqrt(v0)) +1 )
#print primes
#print len(primes)
#print len(primes)**3

v0 = 50000000
#v0 = 50
primes = euler.sieve( int(math.sqrt(v0)) +1 )

d = set()
tot = v0
for i in primes:
    itot = i**2
    for j in [ p for p in primes if p**3 < v0-itot ]:
        jtot = itot + j**3
        for k in [ p for p in primes if p**4 < v0-jtot ]:
            ktot = jtot + k**4
            print i,j,k,ktot
            d.add(ktot)
print len(d)
