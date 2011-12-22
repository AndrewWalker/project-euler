import euler

q1 = lambda x : (2*x+1)**2
q2 = lambda x : q1(x) - 2*x
q3 = lambda x : q1(x) - 4*x
q4 = lambda x : q1(x) - 6*x

q = [ q2, q3, q4 ]

maxprime = 14000
lowPrimes = euler.sieve(maxprime)
lowPrimes = set(lowPrimes)
def isprime(n):
    if n < maxprime:
        return n in lowPrimes
    else:
#        return euler.isprime_slow(n)
        return euler.isprime(n)

@euler.in_mem_memoize
def nprimes(x):
    cnt = 0
    for qi in q:
        if isprime(qi(x)):
            cnt += 1
    return cnt

def primesInLayer(n):
    cnt = 0
    for i in range(n):
        cnt += nprimes(i)
        if i % 200 == 0:
            print i
    return cnt,4*(n-1)+1

print primesInLayer(1)

#c,l = primesInLayer(4000)
#print (100*c)/float(l)
import sys

cnt = 0
tot = 1
for i in range(1,14000):
    for qi in q:
        cnt += isprime(qi(i))
    tot += 4
    v = float(cnt*100)/tot
    if v < 10:
        break
    if i % 100 == 0:
        print i,v

print 'soln',2*i+1
