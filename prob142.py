"""Project Euler 142 - Perfect Square Collection

Brute forces. About 5 minutes.
"""
import collections
from itertools import count
from euler import *

def squares():
    for i in count(1):
        yield i**2

def squares_less_than(n):
    lst = itertools.takewhile(lambda x : x < n, squares())
    lst = list(lst)
    lst.reverse()
    return lst

def f():
    for x in count(4):
        for yprime in squares_less_than(x):
            y = x - yprime
            if isSquare(x + y):
                yield x, y

def f2():
    for x in count(4):
        for y in xrange(1, x):
            if not isSquare(x+y):
                continue
            if not isSquare(x-y):
                continue
            yield x, y

def g():
    d = collections.defaultdict(list)
    for x, y in f():
        d[x].append(y)
        for z in d[y]:
            yield x, y, z, len(d)

#print 434657 + 420968 + 150568

for x,y,z,c in g():
    print x, y, z, c
    if not isSquare(x+z):
        continue
    if not isSquare(x-z):
        continue
    if not isSquare(y+z):
        continue
    if not isSquare(y-z):
        continue
    break


