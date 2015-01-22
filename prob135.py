"""
Problem 135 same differences

https://projecteuler.net/problem=135

See also: 136

Q. What is hard?
A. Looks ugly - best to start with the algebra

    z = a 
    y = a + b
    x = a + 2b

    x^2 = a^2 + 4ab + 4b^2
    Y^2 = a^2 + 2ab + b^2
    z^2 = a^2

    n = x^2 - y^2 - z^2
    n = 4b^2 - (a-b)^2

Q. A different way?
A. Ok

    (x+a)^2-x^2-(x-a)^2=n solve n

    n = x(4a-x)

Q. Example

    x = 27
    a = 7

    x = 9
    a = 3


Q. Constraints?
A. Yep. 

    a, x and a are positive integers 
    4a-x > 0, and so, a > x/4

    (n/x + x) % 4 = 0
    n = 0 (mod x)

Q. What is interesting about this?
A. For n to have m solutions, it must have 2m divisors

Retrospective
-------------

Looking back, this was a bit of a gimme question. 

But. it did take doing the algebra twice, and I'm not really sure I
understand why it worked when I chose the middle value and didn't when I
chose the low value.

"""
from sympy import *

def solutions(n):
    """Find a solution to the equation described in problem 135

    >>> solutions(27)
    2
    >>> solutions(1155)
    10
    """
    cnt = 0
    for x in divisors(n):
        q = n / x
        a = (q+x)/4
        if x-a <= 0:
            continue
        if (x+a)**2-x**2-(x-a)**2 == n:
            cnt += 1
    return cnt

if __name__ == "__main__":
    cnt = 0
    for i in xrange(1, 10**6):
        if solutions(i) == 10:
            cnt += 1
    print cnt

