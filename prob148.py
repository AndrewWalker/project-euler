"""Problem 148 - Exploring Pascal's triangle

url: https://projecteuler.net/problem=148
progress: started
keywords: pascals triangle, binomial, factorial

Q. What is hard?
A. 10^9 rows isn't reachable using brute force

Q. Can you explore the problem
A. Visually:

00 _
01 __
02 ___
03 ____
04 _____
05 ______
06 _______
07 _xxxxxx_
08 __xxxxx__
09 ___xxxx___
10 ____xxx____
11 _____xx_____
12 ______x______
13 ______________
14 _xxxxxx_xxxxxx_

Q. Is that it?
A. The pattern is more complex after about 100 rows (you get bigger blocks)

Q. Do the row sums appear in OEIS?
A. No

Q. Does the cummulative sum appear in OEIS?
A. No

Q. Any other research that helps?
A. Yep.

    TWO BINOMIAL COEFFICIENT CONJECTURES by Rowland 

    From section 2 "One basic question we can ask about Pascal's triangle modulo k
    is how many nonzero entries there are on row n" it goes on to explain that the
    question is answered for cases when k is prime

    That paper references work by Hexel and Sachs.
"""
import euler

def pascals_triangle(rows):
    for i in xrange(rows):
        yield [euler.ncr(i, j) for j in xrange(i+1)]

def triangle_mod(rows, n=7, f = '.', t = 'O'):
    for row in pascals_triangle(rows):
        yield [ t if i%n==0 else f for i in row ]

def naive_solution(rows):
    """
    >>> naive_solution(100)
    2361
    """
    cumsum = 0
    for row in triangle_mod(rows, 7, 1, 0):
        cumsum += sum(row)
    return cumsum


#cum = 0
#for row in triangle_mod(15, 7, 1, 0):
    #print sum(row),',',
    #cum += sum(row)
    #print cum, ',',
