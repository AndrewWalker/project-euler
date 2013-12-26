"""Project Euler 173

Keywords: square lamina, sums of squares

Notes
----------
A non-empty square of tiles with side length n with have $A = n^2$ tiles
A (symmetric) square lamina will have an area of
$$
    A = n^2 - (n-2m)^2
    A = n^2 - (n^2 -4nm + m^2)
    A = 4mn + m^2
$$
Where the hole is $n-2m$ units accross

Question. Can you reduce this to 1/4 of the "square"? No.
          Because n can be even or odd

Question. When do you have maximum tiles for a given n?
    when the "hole" is minimised
        n % 2 == 1 (n is odd),  n - 2m = 1
        n % 2 == 0 (n is even), n - 2m = 2

Question. When do you have minimum tiles for a given n?
    when the "hole" is maximised
        when m = 1

Question. What is the biggest value of $n$ you need to consider?
    from sympy import *
    from sympy.abc import a, n
    print solve(Eq(a, n**2 - (n-1)**2), n) # (because m == 1)
    > a/4 + 1

Question. Given a value of a and n what is the smallest values of m?

"""
import math
from numpy import sqrt

def square_lamina_area(n, m):
    return n**2 - (n - 2*m)**2

def largest_outside_square(area):
    return area / 4 + 1

assert(square_lamina_area(9, 1) == 32)
assert(square_lamina_area(6, 2) == 32)
assert(largest_outside_square(32) == 9)

def solve(area):
    cnt = 0
    for i in xrange(3, largest_outside_square(area)+1):
        # in the worst case this
        topval = i/2
        if i**2 > area:
            # more typically this which as i -> infinity topval -> 1
            topval = int(math.floor(i/2. - sqrt(-area + i**2)/2.))
        for j in xrange(1, topval+1):
            a = square_lamina_area(i, j)
            if i - j*2 == 0:
                continue
            if a <= area:
                cnt += 1
        if i % 1000 == 0:
            print i, cnt
    return cnt

print 'sol', solve(10**6)


