import euler
import math
import fraction

def primeFactors(n):
    s = set()
    for f in euler.factors(n):
        if euler.isprime(f):
            s.add(f)
    return s

def totient2(n):
    if euler.isprime(n):
        return n-1
    else:
        factors = primeFactors(n)
        factors = [ fraction.Fraction(p-1,p) for p in factors ]
        factors = [ fraction.Fraction(n,1) ] + factors
        return reduce( lambda a,b:a*b, factors, fraction.Fraction(1,1) ).cancel().num


def totient(n):
    factors = euler.factors(n)
    coprime = [ 1 for i in range(n) ]
    coprime[0] = 0
    for f in factors:
        for i in range(f,n,f):
            coprime[i] = 0
    return sum(coprime)

@euler.in_mem_memoize
def f(n):
#    return n/float(totient(n))
    return n/float(totient2(n))

def main(maxv):
    best   = 2
    f_best = 0

    for n in range(390390,maxv):
        if euler.isprime(n) == False:
            f_n = f(n)
            if f_n > f_best: 
                print 'possible',n,f_n
                best = n
                f_best = f_n
            if n % 1000 == 0:
                print '.'#n,f(n),'best',best,f_best
            
#main(1000000)
        
    
for i in range(2,1000000):
    if euler.isprime(i) == False:
        if len(euler.factors(i)) > 50:
            if f(i) > 5.1:
                print i,len(euler.factors(i)),f(i)
    #v = totient2(i)
    #if i % 1000 == 0:
    #    print i,v,totient(i),i/float(v),len(euler.factors(i))


