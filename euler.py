import math
import os
import pickle
import collections
import itertools
import random

def pells_eqn(x1, y1, n):
    """Generator over solutions of pells equation

    x^2 - n y^2 = 1

    Examples - project euler 66, 94
    """
    xk = int(x1)
    yk = int(y1)
    while 1:
        assert(xk**2 - n * yk**2 == 1)
        yield (xk, yk)
        xkn = x1 * xk + n * y1 * yk
        ykn = x1 * yk +     y1 * xk
        xk = xkn
        yk = ykn

def triangle_area(a, b, c):
    """Area of a general triangle (without right angles)

    Notes
    -----
    Uses Heron's formula
    """
    s = (a+b+c)/2
    return math.sqrt(s * (s-a) * (s-b) * (s-c))

def digits(n):
    #assert isinstance(n, int)
    if n == 0:
        return [0]
    else:
        lst = []
        while n != 0:
            lst.append(n % 10)
            n = n / 10
        lst.reverse()
        return lst

def increasing_digits(seq):
    for i in xrange(len(seq)-1):
        if seq[i+1] < seq[i]:
            return False
    return True

def decreasing_digits(seq):
    for i in xrange(len(seq)-1):
        if seq[i+1] > seq[i]:
            return False
    return True

def is_bouncy(n):
    seq = digits(n)
    if increasing_digits(seq):
        return False
    elif decreasing_digits(seq):
        return False
    else:
        return True


def is_happy(n):
    seen = set()
    while 1:
        if n == 1:
            return True
        if n in seen:
            return False
        seen.add(n)
        n = sum(digit**2 for digit in digits(n))

def fib_iter():
    """Iterator over the Fibonacci sequence"""
    fn2 = 0
    fn1 = 1
    yield fn2
    while 1:
        fn1, fn2 = fn1+fn2, fn1
        yield fn2

def primeIter():
    return prime_iter()

def prime_iter():
    return itertools.ifilter( isprime, itertools.count(1) )

def primes_less_than(m):
    return itertools.takewhile(lambda n : n < m, primeIter())


def ndigits(n):
    '''
    Use a base 10 logarithm to calculate an equivalent
    to len(euler.intToSeq(n))
    '''
    # note: the small fudge factor here to overcome
    #       numerical stability issues of taking the
    #       floor of a logarithm
    eps = 10e-15
    return int(math.floor(math.log(n,10)+eps))

def isSquare(n):
    assert(type(n) == type(1) or type(n) == long), type(n)
    rt = math.floor(math.sqrt(n))
    return rt*rt==n

def coprime(a,b):
    """Two integers a and b are co-prime if they have no common factors
    """
    return gcd(a,b) == 1

def totient(n):
    """Totient or Euler's phi function for a value of `n`

    literally, the number of integers less than `n` that are coprime to `n`
    """
    assert(n>=1)
    if n == 1:
        return 1
    else:
        return sum([1 for i in range(1, n) if coprime(i, n)])

def phisieve(nmax):
    ts=range(nmax)
    for i in xrange(2,nmax):
        # Prime, as it hasn't been divided by anything lower.
        if ts[i]==i:
            # Primes are coprime to everything below them.
            ts[i]-=1
            # Factor i into the totients of its multiples.
            for j in xrange(i+i,nmax,i):
                ts[j] = (ts[j]*(i-1))//i
    return ts

def take(n, iterable):
    "Return first n items of the iterable as a list"
    return list(itertools.islice(iterable, n))

def diceVals(n,maxv):
    if n == 0:
        yield []
    else:
        for i in range(1,maxv+1):
            for j in diceVals(n-1,maxv):
                yield [i]+j

def diceProb(n,maxv):
    cnt  = 0
    freq = collections.defaultdict(int)
    for vals in diceVals(n,maxv):
        s = sum(vals)
        freq[s] += 1
        cnt += 1
    return freq,cnt



class in_file_cache:
    def __init__(self, fun):
        self.fun = fun

    def save(self, fname, obj):
        f = open(fname,'w')
        pickle.dump(obj, f)
        f.close()
        del f

    def load(self, fname):
        f = open(fname,'r')
        ret = pickle.load(f)
        f.close()
        del f
        return ret

    def __call__(self,*args,**kwargs):
        ret = None
        fname = '.' + self.fun.func_name
        if not os.path.exists(fname):
            ret = self.fun(*args,**kwargs)
            self.save(fname,ret)
        else:
            ret = self.load(fname)
        return ret

def gcd(a,b):
    '''
    Euclid's method for finding the GCD.
    This is a significant improvement on other approaches
    '''
    while b != 0:
        t = b
        b = a % b
        a = t
    return a

def in_mem_memoize(fun):
    def inner(*args):
        if args not in inner.d:
            v = fun(*args)
            inner.d[args] = v
        return inner.d[args]
    inner.d = {}
    return inner

@in_mem_memoize
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def cond_memoize(cond):
    def memoize_wrap(fun):
        def inner(n):
            if cond(n):
                return fun(n)
            else:
                if not n in inner.d:
                    v = fun(n)
                    inner.d[n] = v
                    return v
                else:
                    return inner.d[n]
        inner.d = {}
        return inner
    return memoize_wrap



def binet_fib(n):
    '''
    a closed form approach to solving fib problems
    '''
    #assert(1 == 0) # not tested for big n
    phi = (1. + math.sqrt(5))/2
    return int(((phi**n)-((1/phi)**n))/math.sqrt(5))

@in_mem_memoize
def naive_factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

@in_mem_memoize
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

def intToSeq(n):
    if n == 0:
        return [0]
    else:
        lst = []
        while n != 0:
            lst = [ n % 10 ] + lst
            n = n / 10
        return lst

def seqToInt( seq ):
    return int( ''.join( [ str(i) for i in seq ] ) )

def sieve(n):
    lst   = range(0,n)
    prime = [ True for i in lst ]
    for i in range(2,int(math.sqrt(n))+1):
        for j in range(2*i,n,i):
            prime[j] = False
    lst = lst[2:]
    prime = prime[2:]
    return [ i for i,j in zip(lst,prime) if j ]

def product(seq):
    return reduce( lambda a,b : a*b, seq, 1 )

def ncr(n,r):
    """
    algebraic choosing or r elements from n
    """
    assert(r <= n)
    return factorial(n) / (factorial(r) * factorial(n-r))

def choose( lst, num ):
    """
    generator over the choices of all possible tuples of num elements of seq
    """
    if num == 0:
        yield []
    else:
        for i in xrange(len(lst)):
            for rst in choose(lst[i+1:],num-1):
                yield [lst[i]] + rst

def divisors(n):
    res = set()
    for i in range(1,int(math.sqrt(n))+1):
        if n % i == 0:
            res.add(i)
            res.add(n/i)
    return res

def properDivisors(n):
    return divisors(n)-set([n])

def factors(n):
    return divisors(n) - set([1,n])

def prime_factors(n):
    assert(n > 0)
    if n == 1:
        return [1]
    else:
        return [ i for i in divisors(n) if isprime(i) ]

def iscomposite(n):
    return (n>1) and not isprime(n)

import MillerRabin
uint32max = 2**32

def isprime(n):
    #assert(n < uint32max)
    if n > uint32max:
        return isprime_slow(n)
    if n == 0 or n == 1:
        return False
    return MillerRabin.miller_rabin(n)

def isprime_slow(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n))+1, 2):
        if n % i == 0:
            return False
    return True

def palindrome(n):
	s = str(n)
	for i in range(len(s)/2):
		if s[i] != s[-(i+1)]:
			return False
	return True

def combinations(iterable, r):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = range(r)
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)

def permutations(iterable, r=None):
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = range(n)
    cycles = range(n, n-r, -1)
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return

def alphaValue(name):
    return sum([ ord(c)-ord('A')+1 for c in name ])

def randBigPrime():
    '''
    Return a large prime number
    '''
    x = random.randint(0xA0000000,0xFFFFFFFF)
    while isprime(x) == False:
        x = random.randint(0xA0000000,0xFFFFFFFF)
    return x

def fastfib(n):
    def powLF(n):
        if n == 1:     return (1, 1)
        L, F = powLF(n//2)
        L, F = (L**2 + 5*F**2) >> 1, L*F
        if n & 1:
            return ((L + 5*F)>>1, (L + F) >>1)
        else:
            return (L, F)
    if n & 1:
        return powLF(n)[1]
    else:
        L, F = powLF(n // 2)
        return L * F

def fastfibFrontNine(n):
    return seqToInt(intToSeq(fastfib(8000))[0:9])


def int2base(x, base):
    """Convert a
    """
    import string
    digs = string.digits + string.lowercase
    # Alex Martelli
    # http://stackoverflow.com/a/2267446/2246
    if x < 0: sign = -1
    elif x==0: return '0'
    else: sign = 1
    x *= sign
    digits = []
    while x:
        digits.append(digs[x % base])
        x /= base
    if sign < 0:
        digits.append('-')
    digits.reverse()
    return ''.join(digits)

def count_partitions(m):
    # from http://stackoverflow.com/questions/7802160/number-of-ways-to-partition-a-number-in-python
    @in_mem_memoize
    def partition(k, n):
        assert(k > 0)
        assert(n > 0)
        if k > n: return 0
        if k == n: return 1
        return partition(k+1, n) + partition(k, n-k)
    return partition(1, m)

# You can think of this as a form of restricted partitioning
# In which there are a restricted number of classes (coins).
@in_mem_memoize
def coin_change(coins, value):
    # http://en.wikipedia.org/wiki/Change-making_problem
    if value <  0: return 0
    if value == 0: return 1
    if not coins:  return 0
    return coin_change(coins, value-coins[0]) + coin_change(coins[1:], value)



def power_sets_iter(aset, min_size=0):
    """All the possible subsets of a set
    """
    n = len(aset)
    alst = list(aset)
    bits = [ 2**i for i in xrange(n) ]
    for i in xrange(2**n):
        js = [j for j in xrange(n) if i & bits[j] != 0 ]
        if len(js) >= min_size:
            yield set([ alst[j] for j in js])

def count_power_sets(aset):
    """
    """
    n = len(aset)
    return 2**n

def powmod(a, b, c):
    """Calculate $(a^b)%c$

    Running time is $O(log(b))$
    """
    x = 1
    y = a
    while b > 0:
        if b % 2 == 1:
            x = (x * y) % c
        y = (y * y) % c
        b /= 2
    return x % c



