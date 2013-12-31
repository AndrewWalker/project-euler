"""Project Euler 191. Prize Strings

Question. For a day, how many outcomes are there?

    3 (O, L, A)

Question. For n days, how many outcomes are there?

    3^n
    For 4 days,  3^4 = 81
    For 30 days, 3^30 = 205891132094649 ~= 3 * 10^14

    From past experience, that is too many to iterate through

Question. How can you speed this up?

    Tree pruning? Much closer to 2^30 than 3^30
    Still Too slow for more than ~ 22 days.

Question. Can you convert recursion to iteration?

    Remove the cost of stack frame setup
    Still *way* too slow

Question. Can you use combinatorial tricks?

    Consider a simple case breakdown

    a) 1 late day        n . 2^(n-1)
       in which case, the late day takes up one of the n days
       and you have two choices for each of the other days

    or

    b) 0 late day(s)     2^n
       in which case, there are only two choices for each of n days

    n = 30
    m = (n*2**(n-1) + 2**n)
    d = (3**n)
    print m
    print d
    print m/float(d)
"""
import timeit
from euler import *

def f(duration):
    cnt = 0
    stack = ['']
    i = 0
    while stack:
        i += 1
        if i % 10000000 == 0:
            print (i / 3.**30)
        cs = ['O']
        top = stack.pop()
        if top[-2:] != 'AA':
            cs.append('A')
        if 'L' not in top:
            cs.append('L')
        for c in cs:
            new = str(top)
            new += c
            if len(new) == duration:
                cnt += 1
            else:
                stack.append(new)
    return cnt

#print timeit.timeit('f(4)', setup='from __main__ import f', number=1)
#print timeit.timeit('f(30)', setup='from __main__ import f', number=1)

#for i in xrange(1,22):
    #print f(i)

ps = [ 2**i for i in xrange(10) ]
for i in xrange(256):
    print [ i&p for p in ps]


