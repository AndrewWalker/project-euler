"""Project Euler 134 Prime Pair Connection

Q. What is hard?
A. Not sure if there properties of consecutive primes

Don't think so

Q. Does concatenation have a good definition?
A. No
http://math.stackexchange.com/questions/748324/primality-of-the-number-of-obtained-by-concatenating-the-n-consecutive-digits#

Q. Can you Write a function to count digits
A. Yes. Call it D(n)

Q. Now write question using that definition
A.

    x === p_1 (mod 10^D(p_1))
    x ===   0 (mod p_2)

Q. Don't write math - write it so a computer scientist can understand it
A.

Find x such that:

    x % 10**D(p_1) == p_1
    x % 0          == p_2

Q. If you look at the math, does something look familiar?
A. yep, it look like the definition for the chinese remainder theorem

    http://en.wikipedia.org/wiki/Chinese_remainder_theorem#Theorem_statement
"""
# In mathematica:
# ChineseRemainder[{0, 19}, {23, 100}]
# 1219
