"""Problem 118 - Pandigital prime sets

url: https://projecteuler.net/problem=118
status: complete
keywords: pandigital, prime, greedy

Q. What's hard?
A. Lots of things going on at once. Hard to see which will be fastest

Q. At most, how many 9 digit pandigitals could there be?
A. 9! =~ 360k

    actually, there are none
    you can prove it using the divisibility rule for 3

Q. Can you bound that any tighter?
A. The final digit can't be even or 5 {2, 4, 5, 6, 8} ~ 60k

Once this is done you don't need to repeat it

Q. Eight digits are special because you know the other thing must be prime

{2, 3, 5, 7} so only 3 of the four may appear

Q. How many power sets (subsets of a set) are there
A. 2^9 = 512

Q. Relevant reading?
A. Yep

http://en.m.wikipedia.org/wiki/Pandigital_number

Q. Primes < 10
4
Q. How many primes < 100
25
Q. Prime < 1000
168
Q. Primes < 10000
1229
Q. Primes < 100000
9552

How long? 40 minutes

Q. Max number of  subsets to consider?
A. 6 ish?

It's very hard to provide many small subsets

Q. Does this suggest some approaches?
A. Backtracking? Not really backtracking, more a greedy enumeration

Findsettypes(starting, subsetsizes)
    If subsetsizes is empty
        Yield []
    Else
    For s in range head(subsetsizes)
        For p in primesoflength s
            If p intersection starting is empty
                For below in findsettypes( p Union starting, rest subsetsizes )
                    Yield [p] + below

Q. How long
A. An hour


"""

from euler import *
from collections import defaultdict

def draw_table():
    """Draw a table to visualise how many pandigital primes there are

    This was an exploration activity

    >>> draw_table()
    1 4
    2 20
    3 83
    4 395
    5 1610
    6 5045
    7 12850
    8 23082
    """
    pps = pandigital_primes()
    for k, v in pps.iteritems():
        print k, len(v)

def pandigital_primes(allowed, size):
    for j in permutations(allowed, size):
        n = from_digits(j)
        if isprime(n):
            #print 'pan primes', allowed, size
            yield j

allitems = set(range(1,10))

def greedy(allowed, maxsize):
    #print 'greedy', allowed, maxsize
    if maxsize == 0:
        yield []
    else:
        for s in reversed(xrange(1, maxsize+1)):
            for p in pandigital_primes(allowed, s):
                rest = [ i for i in allowed if i not in p ]
                for below in greedy(rest, min(len(rest), len(p))):
                    yield [p] + below

s = set()
for item in greedy(allitems, 9):
    item = [ from_digits(d) for d in item ]
    item.sort()
    item = tuple(item)
    print item
    s.add(item)
print len(s)
