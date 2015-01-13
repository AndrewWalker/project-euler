"""Project Euler 191. Prize Strings

https://projecteuler.net/problem=191

Question. For a day, how many outcomes are there?

    3 (O, L, A)

    L = Late
    A = Absent
    O = On Time


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

    Maybe. I couldn't work out how to do it
"""
import timeit
from euler import *
from collections import defaultdict

"""
    No prize if 3 consecutive A's
    No prize if more than 1 L

"""

A = 0
L = 1
E = 2
O = 2

INITIAL = (0,0,False)
ERROR = (0,0,True)

def transition(state, day):
    if state == ERROR:
        return ERROR
    if day == L:
        if state[L] == 0:
            return (0, 1, False)
        elif state[L] == 1:
            return ERROR
    elif day == A:
        if state[A] == 0:
            return (1, state[L], False)
        elif state[A] == 1:
            return (2, state[L], False)
        elif state[A] == 2:
            return ERROR
    elif day == O:
        return (0, state[L], False)
    assert(1 == 0)

assert transition((0,0,False), A) == (1,0,False)
assert transition((1,0,False), A) == (2,0,False)
assert transition((2,0,False), A) == ERROR 
assert transition((0,1,False), A) == (1,1,False)
assert transition((1,1,False), A) == (2,1,False)
assert transition((2,1,False), A) == ERROR

assert transition((0,0,False), L) == (0,1,False)
assert transition((1,0,False), L) == (0,1,False)
assert transition((2,0,False), L) == (0,1,False)
assert transition((0,1,False), L) == ERROR
assert transition((1,1,False), L) == ERROR
assert transition((2,1,False), L) == ERROR

assert transition((0,0,False), O) == (0,0,False)
assert transition((1,0,False), O) == (0,0,False)
assert transition((2,0,False), O) == (0,0,False)
assert transition((0,1,False), O) == (0,1,False)
assert transition((1,1,False), O) == (0,1,False)
assert transition((2,1,False), O) == (0,1,False)

def step(states):
    out = defaultdict(int)
    for day in [A, L, O]:
        for s0, k0 in states.iteritems():
            s = transition(s0, day)
            out[s] += k0
    return out

def fast(n):
    states = defaultdict(int)
    states[INITIAL] = 1
    for i in xrange(n):
        states = step(states)
    if ERROR in states:
        del states[ERROR]
    assert ERROR not in states.keys()
    return states

def last(seq):
    d = {'O' : O, 'A' : A, 'L' : L}
    s = INITIAL
    for i in seq:
        s = transition(s, d[i])
    return s

def naive(n):
    lst = 'OAL'
    cnt = 0
    out = defaultdict(int)
    for i in itertools.product(*tuple([lst]*n)):
        s = ''.join(i)
        if s.count('L') > 1:
            continue
        if s.find('AAA') != -1:
            continue
        cnt += 1
        out[last(s)] += 1
    return out

i = 30
d = fast(i)
print sum(d.values())

