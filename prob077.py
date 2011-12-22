import itertools
import euler

'''
This is apparently pretty far off the money wrt the 'right' way to do this
'''

primes = [ x for x in xrange(1000) if euler.isprime(x) ]

def numPrimeSums( x ):
    def impl( x, maxval,stack ):
        primesLessThanMax = [ y for y in primes if y<=maxval ]
        cnt = 0
        for p in primesLessThanMax:
            if x - p == 0:
                cnt += 1
            elif x - p > 0:
                cnt += impl(x-p,p,stack+[p]) 
        return cnt
    return impl(x,x,[])

# by guesswork            
print numPrimeSums(70)   
print numPrimeSums(71)   


