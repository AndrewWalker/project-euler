"""Project Euler 164  - Numbers for which no three consecutive digits have
a sum greater than a given value

url: https://projecteuler.net/problem=164
status: finished
keywords: memoization

Q. What is hard?
A. 10^20 means naive is way too big to enumerate 

Q. Alternatives?
A. Walk the tree

Need a function that takes the last digit and the sum of the last two
digits and lazily generates all valid possible digits

def depth_first( s, d, s0, reducer, children ):
    def impl(s, d):
        if d == 0:
            yield s
        else:
            for c in children(s):
                for rest in impl(c, d-1)
                    yield reducer(s, rest)
    return impl(s, d)

Q. How to deal with numbers with leading zeroes
A. Can't you just ignore the problem

0091 == 91 and because 0 doesn't add value it doesn't invalidate

Q. Is getting started tricky? Ie/ bootstrapping the tree
A. can you cheat and pass zeroes?

Q. How long
A. 10 minutes 

Q. To write p code?
A. About another ten 

Q. Did that work?
A. Yep, for small runs, but its slow.

Q. What really matters?
A. State

Q. What is state (in this case)?
A. (value n-1, value n-2)

Q. Can you write a state -> state transition function?
A. Well, yes, but its kind of icky 

    You have 100 states x 100 states, but its very sparse

Q. If you can write it like that can you make if faster by
   writing it as a series of matrix multiplies?
A. Yes. Did that, fast enough, wrong answer.

    use numpy,
    build a transition matrix A
    raise A^20
    multiply by your original state vector
    sum over all states A^20 . v

Q. Why didn't it work?
A. Because the "without leading zeros" literally means 
   between 10^20 and 10^21-1

Q. Can you go back to the original naive version and tweak it
A. Yep, need extra clause to stop 0 being the last digit

    That's enough to debug the counts

Q. Does that give you the right answer with numpy
A. It does when you get your matrices right

Q. Did you need to do the numpy stuff?
A. Nope. Could have just memoized
"""
from euler import *

@in_mem_memoize
def g( last1, last2, depth ):
    if depth == 0:
        return 1
    else:
        cnt = 0
        low = 0 if depth > 1 else 1
        for i in xrange(low, 10):
            if i + last2 <= 9:
                cnt += g(i, last1 + i, depth - 1)
        return cnt

print g(0, 0, 20)


