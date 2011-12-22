import math

def factors(n):
    res = set([])
    for i in xrange(2,int(math.sqrt(n))+1):
        if n % i == 0:
            res.add(i)
            res.add(n/i)
    return res

def isprime(n):
    return len(factors(n)) == 0

lst = factors(600851475143)
lst = list(lst)
lst.sort()
print lst
lst = [ n for n in lst if isprime(n)]
print lst
print lst[-1]
