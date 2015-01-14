"""Project Euler support code

This module includes (a few) doctests, you can run them
on the command-line like:

    $ python euler.py

You won't see any results if the tests passed
"""
import math
import os
import pickle
import collections
import random
import sympy
import itertools
from itertools import combinations, permutations, \
    combinations_with_replacement
from sympy import totient, isprime, divisors, factors

# we'll rename this to minimise regressions
fib = sympy.fibonacci

def repunit(n):
    """A base 10 repunit is a number with all digits 1

    For details see http://en.wikipedia.org/wiki/Repunit

    >>> repunit(1)
    1
    >>> repunit(4)
    1111
    >>> repunit(8)
    11111111
    """
    return (10**n-1)/9

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

    >>> triangle_area(3, 4, 5)
    6.0
    """
    s = (a+b+c)/2
    return math.sqrt(s * (s-a) * (s-b) * (s-c))

def digits(n):
    """Returns the digits that make up a number

    >>> digits(123)
    [1, 2, 3]
    >>> digits(4567)
    [4, 5, 6, 7]
    """
    if n == 0:
        return [0]
    else:
        lst = []
        while n != 0:
            lst.append(n % 10)
            n = n / 10
        lst.reverse()
        return lst

def from_digits( seq ):
    """Return a number from individual digits

    >>> from_digits([1, 2, 3])
    123
    """
    return int( ''.join( [ str(i) for i in seq ] ) )

def ndigits(n):
    """Count the number of base 10 digits in a number

    >>> ndigits(9)
    1
    >>> ndigits(99)
    2
    >>> ndigits(99999)
    5
    """
    return len(digits(n))

def increasing_digits(seq):
    """Are the values in a sequence increasing (or equal)

    >>> increasing_digits(digits(134468))
    True
    """
    for i in xrange(len(seq)-1):
        if seq[i+1] < seq[i]:
            return False
    return True

def decreasing_digits(seq):
    """Are the values in a sequence decreasing (or equal)

    >>> decreasing_digits(digits(66420))
    True
    """
    for i in xrange(len(seq)-1):
        if seq[i+1] > seq[i]:
            return False
    return True

def is_bouncy(n):
    """Checks if a number is bouncy

    >>> is_bouncy(66420)
    False
    >>> is_bouncy(134468)
    False
    >>> is_bouncy(155349)
    True
    """
    seq = digits(n)
    if increasing_digits(seq):
        return False
    elif decreasing_digits(seq):
        return False
    else:
        return True

def is_happy(n):
    """Check if a number is happy

    A happy number is a number defined by the following process: Starting
    with any positive integer, replace the number by the sum of the
    squares of its digits, and repeat the process until the number equals
    1 (where it will stay), or it loops endlessly in a cycle which does
    not include 1. Those numbers for which this process ends in 1 are
    happy numbers, while those that do not end in 1 are unhappy numbers
    (or sad numbers)

    http://en.wikipedia.org/wiki/Happy_number

    >>> is_happy(31)
    True
    >>> is_happy(32)
    True
    >>> is_happy(33)
    False
    """
    seen = set()
    while 1:
        if n == 1:
            return True
        if n in seen:
            return False
        seen.add(n)
        n = sum(digit**2 for digit in digits(n))

def take(n, iterable):
    "Return first n items of the iterable as a list"
    return list(itertools.islice(iterable, n))

def fib_iter():
    """Iterator over the Fibonacci sequence

    There are much better ways to do this, but this
    is an ok start if you're looking for something 
    trivial

    >>> [ i for i in take(6, fib_iter()) ]
    [0, 1, 1, 2, 3, 5]
    """
    fn2 = 0
    fn1 = 1
    yield fn2
    while 1:
        fn1, fn2 = fn1+fn2, fn1
        yield fn2

def is_perfect_square(n):
    """Check if a number is a perfect square

    >>> is_perfect_square(144)
    True
    >>> is_perfect_square(145)
    False
    """
    assert(type(n) == type(1) or type(n) == long), type(n)
    rt = int(math.floor(math.sqrt(n)))
    return rt*rt==n

def coprime(a,b):
    """Two integers a and b are co-prime if they have no common factors

    >>> coprime(5, 3)
    True
    >>> coprime(6, 3)
    False
    """
    return gcd(a,b) == 1

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

def primepi(n):
    """Number of primes less than a value

    http://mathworld.wolfram.com/PrimeCountingFunction.html

    This is here as a reminder of what is in sympy

    >>> primepi(10**5)
    9592
    """
    return sympy.primepi(n) 

def dice_vals(num_dice, maxv):
    """Give all possible combinations of dice

    >>> len(list(dice_vals(2, 6)))
    36
    """
    return itertools.product(*tuple([range(1, maxv+1)] * num_dice))

def dice_frequency(num_dice, maxv):
    """Get the frequency of occurance of a particular die value

    >>> dice_frequency(2, 6)[7]
    6
    >>> dice_frequency(2, 6)[2]
    1
    >>> dice_frequency(2, 6)[1]
    0
    """
    vals = [sum(i) for i in dice_vals(num_dice, maxv)]
    freq = collections.Counter(vals)
    return freq

def gcd(a,b):
    """Euclid's method for finding the GCD.

    If you need a caching version of this, use sympy.igcd

    >>> gcd(10, 2)
    2
    >>> gcd(10, 4)
    2
    >>> gcd(7, 3)
    1
    """
    while b != 0:
        t = b
        b = a % b
        a = t
    return a

def in_mem_memoize(fun):
    """Function decorator to cache values
    """
    def inner(*args):
        if args not in inner.d:
            v = fun(*args)
            inner.d[args] = v
        return inner.d[args]
    inner.d = {}
    return inner

@in_mem_memoize
def factorial(n):
    """Evaluate the factorial function n!

    See: http://docs.sympy.org/latest/modules/mpmath/functions/gamma.html

    >>> factorial(4)
    24
    """
    if n == 0:
        return 1
    return n * factorial(n-1)

def product(seq):
    """Cumulative product of all items in a sequence

    >>> product([2, 3, 4])
    24
    """
    return reduce( lambda a,b : a*b, seq, 1 )

def ncr(n, r):
    """Number of ways to choose r elements from n

    This is in as a reminder of how the sympy api works

    >>> ncr(10, 5)
    252
    """
    return sympy.binomial(n, r)

def choose( lst, n ):
    """Iterator over the way to choose n items from `lst`

    >>> take(3, choose(range(4), 2))
    [(0, 1), (0, 2), (0, 3)]
    """
    return combinations(lst, n)

def properDivisors(n):
    return divisors(n)-set([n])

def prime_factors(n):
    assert(n > 0)
    if n == 1:
        return [1]
    else:
        return [ i for i in divisors(n) if isprime(i) ]

def is_composite(n):
    """Is a number composite

    >>> is_composite(1)
    False
    >>> is_composite(4)
    True
    >>> is_composite(5)
    False
    """
    return (n>1) and not isprime(n)

def palindrome(n):
    """Check if a number is a palindrome

    >>> palindrome(123)
    False
    >>> palindrome(1234321)
    True
    >>> palindrome(12344321)
    True
    """
    s = str(n)
    for i in range(len(s)/2):
        if s[i] != s[-(i+1)]:
            return False
    return True

def word_sum(word):
    """Return the sum of the letter values of a word

    >>> word_sum('SKY')
    55
    """
    return sum([ ord(c)-ord('A')+1 for c in word ])

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
    """Count the number of ways a set can be partitioned

    http://en.wikipedia.org/wiki/Power_set

    >>> count_power_sets(set(range(4)))
    16
    """
    n = len(aset)
    return 2**n

def powmod(a, b, c):
    """Calculate $(a^b)%c$

    Running time is $O(log(b))$

    >>> powmod(10, 1, 7)
    3
    >>> powmod(10, 10, 7)
    4
    """
    x = 1
    y = a
    while b > 0:
        if b % 2 == 1:
            x = (x * y) % c
        y = (y * y) % c
        b /= 2
    return x % c


def is_mersenne_prime(p):
    """Detect if 2**p - 1 is prime

    Uses the `Lucas-Lehmer test <http://en.wikipedia.org/wiki/Lucas%E2%80%93Lehmer_primality_test>`_

    >>> is_mersenne_prime(3)
    True
    >>> is_mersenne_prime(7)
    True
    >>> is_mersenne_prime(31)
    True
    >>> is_mersenne_prime(127)
    True
    """
    s = 4
    M = 2**p - 1
    for _ in xrange(p-2):
        s = ((s * s) - 2) % M
    if s == 0:
        return True
    return False

if __name__ == "__main__":
    import doctest
    doctest.testmod()
