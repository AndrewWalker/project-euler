import euler
import math

def isPandigital(seq):
    a = set(seq).intersection(set(range(1,10)))
    return len(a) == 9

def fibiter():
    a = 0
    b = 1
    yield a
    while 1:
        yield b
        a, b = b, a+b

for i,v in enumerate(fibiter()):#xrange(2,100000):
    if isPandigital(euler.intToSeq(v % 10**9)):
        v2 = v / 10**(int(math.ceil(math.log10(v)))-11)
        v2 = euler.intToSeq(v2)[:9]
        print i
        if isPandigital(v2):
            break
