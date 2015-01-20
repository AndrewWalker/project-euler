"""Project Euler 162 - Hex numbers

url: https://projecteuler.net/problem=162
status: started, inclusion-exclusion principle


Q. what is the shortest sequence?

    3 digits.
        10A, 1A0, A01, A10

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

Retrospective
-------------

This was horrible to write in Python, I don't know if I could have written
this without writing out the pattern matching out before trying to write
the actual table.

After looking round for a library and not finding much, I can't think of a
better way to do this.

This was a big miss:

    http://en.wikipedia.org/wiki/Inclusion%E2%80%93exclusion_principle

"""
import collections
from pprint import pprint

VAL0 = 0
VAL1 = 1
VALA = 2
LEAD = 3

def transition(c, x):
    """
    (0,_,_,0) 0 (0,_,_,0)
    (0,_,_,1) 0 (1,_,_,1)
    (_,0,_,_) 1 (_,1,_,1)
    (_,_,0,_) A (_,_,1,1)
    (_,_,_,_) - (_,_,_,1)
    """
    if c == '0' and x[VAL0] == 0:
        if x[LEAD] == 0:
            return (0, x[VAL1], x[VALA], 0)
        elif x[LEAD] == 1:
            return (1, x[VAL1], x[VALA], 1)
    elif c == '1' and x[VAL1] == 0:
        return (x[VAL0], 1, x[VALA], 1)
    elif c == 'A' and x[VALA] == 0:
        return (x[VAL0], x[VAL1], 1, 1)
    else:
        return (x[VAL0], x[VAL1], x[VALA], 1)

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

INITIAL = (0,0,0,0)
chars = '0123456789ABCDEF'
s = multistep(16)[(1,1,1,1)]
print hex(s).upper()[2:]

