import euler

def oldhamming( n, m ):
    return max(euler.primeFactors(n)) <= m

import math
def generate( primes, c ):
    if primes == []:
        #yield [],1
        yield 1
    else:
        for i in xrange( 0, int(math.ceil(math.log(c, primes[0]))) ):
            #for lst, res in generate(primes[1:], c/(primes[0]**i)+1 ):
            for res in generate(primes[1:], c/(primes[0]**i)+1 ):
                final = primes[0]**i * res
                if final < c:
                    #yield [i]+lst, final
                    yield final

primes = [ x for x in range(2,100+1) if euler.isprime(x) ]
primes.reverse()
c = 0
for item in generate(primes, 10**9):
    if c % 10000 == 0:
        print item
    c+=1
print c+1

