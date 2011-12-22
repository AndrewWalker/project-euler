import euler
import collections
from itertools import *

def concatPrimes(a,b):
    astr = euler.intToSeq(a)
    bstr = euler.intToSeq(b)
    return euler.seqToInt(astr+bstr)

def validPair(a,b):
    i = concatPrimes( a,b )
    j = concatPrimes( b,a )
    if euler.isprime(i) and euler.isprime(j):
        return True
    return False

def primesLessThan(n):
    return list(takewhile( lambda x : x < n, euler.primeIter() ))

def listConcatPrimes( n, restrict = None ):
    if restrict == None:
        restrict = primesLessThan(n)
    return list(ifilter(lambda x : validPair(x,n), restrict ))

def solve(y,ys):
    xs = listConcatPrimes(y,ys)
    for xi in range(len(xs)):
        for lst in solve(xs[xi], xs[:xi]):
            yield [y] + lst
    yield [y] 
        
def solveBase(n,tlen):
    for x in solve(n,primesLessThan(n)):
        if len(x) == tlen:
            return x
    return None

for i in euler.primeIter():#primesLessThan(1000):
    res = solveBase(i,5)
    print i,res
    if res != None:
        break


