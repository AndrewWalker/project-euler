"""Project Euler 162 - Hex numbers

url: https://projecteuler.net/problem=162
status: started


Q. what is the shortest sequence?

    3 digits.
        10A, 1A0, A01, A10

Q. What does it look like for four?

    where t is 1,0,A and x is anything, it kind of like this
        tttx
        ttxt
        txtt
        xttt

        really this is 4 choose 1

    but, this doesn't take duplications into account

    for 5?
        tttxx
        ttxtx
        txttx
        xtttx
        ttxxt
        txtxt
        xttxt
        txxtt
        xtxtt
        xxttt

        really, this is 5 choose 2

Q. For `n` digits (n>=3), what is an approximate upper bound?

        6 * 16^(n-3) * ncr(n, n-3)

        6 possible arrangements of a01
        16^(n-3) values of the `x`'s
        ncr(n, n-3) ways to mix the `x`'s in

Q. Any hints
A.

        - "At most"
        - 001 === 1 (don't count dups)

Q. Any helpful past experience?
A. State machine trick?

        (1-placed, 0-placed, a-placed, non-zero)
        Transitions are, ( Any 1 0 A )


Q. Prety close, but still wrong
A. Missing the case where 0 is the first valid digit

01A  (doesn't make sense)
001A (doesn't include zero)

maybe need to add another state item to work out if the prefix
is all zeros, and none of the rest is zeros

"""

digits = [0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F']
digits = [str(c) for c in digits]

def generate_valid_numbers(n):
    assert n>=0
    if n == 0:
        yield []
    else:
        for c in digits:
            if c != 0:
                for rest in generate_valid_numbers(n-1):
                    yield [c] + rest

def is_match(lst):
    return 'A' in lst and '0' in lst and '1' in lst

def count_matches(n):
    cnt = 0
    for s in generate_valid_numbers(n):
        if is_match(s):
            print s, len(s)
            cnt += 1
    return cnt

#0,_,_  ->1   1,_,_
#_,0,_  ->A   _,1,_
#_,_,0  ->0   _,_,1

def transition(c, state):
    if c == '0':
        if state[0] == 0:
            return (1, state[1], state[2])
        else:
            return state
    elif c == '1':
        if state[1] == 0:
            return (state[0], 1, state[2])
        else:
            return state
    elif c == 'A':
        if state[2] == 0:
            return (state[0], state[1], 1)
        else:
            return state
    return state
import collections
from pprint import pprint
INITIAL = (0,0,0)
chars = '0123456789ABCDEF'


def step(states):
    out = collections.defaultdict(int)
    for s, cnt in states.iteritems():
        for c in chars:
            sprime = transition(c, s)
            out[sprime] += cnt
    return dict(out)

def multistep(steps):
    states = { INITIAL : 1 }
    for i in xrange(steps):
        states = step(states)
    return states

n = 16
steps = multistep(n)
#count_matches(n)
print hex(steps[(1,1,1)]).upper()[2:]
#print hex(count_matches(n)).upper()[2:]
