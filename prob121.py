"""Project Euler 121 - Disc Game Prize Fund

Question. What does this look like in terms of actual results?

turn    bag         P(b)
1       r b         1/2
2       r r b       1/3
3       r r r b     1/4
4       r r r r b   1/5

turn 1234
     rrrr    1/2, 2/3, 3/4, 4/5
     rrrb    1/2, 2/3, 1/4, 4/5
     rrbr
     rrbb
     rbrr
     rbrb
     rbbr
     rbbb

     brrr
     brrb
     brbr
     brbb
     bbrr
     bbrb
     bbbr
     bbbb

Question. How many outcomes are possible in each turn?

    In any turn there are exactly two outcomes, blue or not blue

Question. After n turns, how many possible outcomes are there?

    2 outcomes at each turn = 2^n

Question. How do you enumerate all possible outcomes?

    power sets?
    count from 0 to 2^n and use bitmasks?

Question. In the n-th turn how many disks will there be?

    there will be n+1 disks in the bag

Question. In the n-th turn, what is the probability of a blue?

    1/(n+1)

Question. In the n-th turn, what is the probability of a red?

    1 - P(b) = n/(n+1)

Question. Do you literally have to enumerate possiblities?
          Or is there as shortcut?
"""
import fractions
from euler import *

def enumerate_outcomes(n):
    for p in xrange(0, 2**n):
        yield [int((p & 2**b)!=0) for b in xrange(n)]

def p_blue(n):
    return fractions.Fraction(1, n+1)

def p_not_blue(n):
    return 1 - p_blue(n)

def enumerate_winners(n):
    for bm in enumerate_outcomes(n):
        blues = 0
        ps = []
        for t, b in enumerate(bm):
            if b:
                ps.append(p_blue(t+1))
                blues += 1
            else:
                ps.append(p_not_blue(t+1))
        if blues > (n/2.):
            yield product(ps)
        else:
            pass

print sum(w for w in enumerate_winners(15))

# floor(1/soln)



