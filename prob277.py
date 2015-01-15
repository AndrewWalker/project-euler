"""Project Euler 277. 

Status:   Started
Url:      https://projecteuler.net/problem=277
Keywords: Collatz

See Also
========

Collatz-conjecture
    https://projecteuler.net/problem=14

Process
=======

Q. What is hard?
A. Collatz sequences are unpredictable - not sure about patterns?
A. Guessing is out - sequence is 3^30

Q. What might make this easy?
A. You only need to run a small number of steps for each one
A. Opt out early

Q. Where to start?
A. Experiment

    Time taken to implement sequence, 10 minutes

    Time taken to implement the *dumb thing* 20 minutes (interrupted)

Q. What if you knew the sequence from the "other end"?
A. You could predict what the value was

Retrospective
=============

"""
from euler import *

def modified_collatz_step(a_n):
    if a_n % 3 == 0:
        return 'D', a_n/3
    elif a_n % 3 == 1:
        return 'U', (4 * a_n + 2) / 3
    else:
        return 'd', (2 * a_n - 1) / 3

def modified_collatz(a_n):
    out = ''
    lst = [a_n]
    while a_n != 1:
        s, a_n = modified_collatz_step(a_n)
        out += s
        lst.append(a_n)
    return out, lst

assert modified_collatz(231)[0] == 'DdDddUUdDD'
assert modified_collatz(231)[1] == [231,77,51,17,11,7,10,14,9,3,1]
assert modified_collatz(1004064)[0] == 'DdDddUUdDDDdUDUUUdDdUUDDDUdDD'

def maxlen_collatz(a_n, maxlen):
    out = ''
    while a_n != 1:
        s, a_n = modified_collatz_step(a_n)
        out += s
        if len(out) >= maxlen:
            break
    return out

pattern = 'UDDDUdddDDUDDddDdDddDDUDDdUUDd'

i = 10**15
while 1:
    res = maxlen_collatz(10**15 + i, len(pattern))
    i += 1
    if res == pattern:
        break
    if i % 10000 == 0:
        print res, i

