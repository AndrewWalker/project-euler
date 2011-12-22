import euler
import math

def sieve(n):
    lst   = range(0,n)
    prime = [ True for i in lst ]
    for i in range(2,int(math.sqrt(n))+1):
        for j in range(2*i,n,i):
            prime[j] = False
    lst = lst[2:]
    prime = prime[2:]
    
    return [ i for i,j in zip(lst,prime) if j ]


print sum(sieve(2000000))
