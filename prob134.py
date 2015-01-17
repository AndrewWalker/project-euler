"""Project Euler 134 Prime Pair Connection

url: https://projecteuler.net/problem=134
status: complete
keywords: chinese remainder theorem, primes, modulus

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

Q. Is python the easiest way to do this?
A. meh. mathematica is easier in this case.
"""
# In mathematica:
# ChineseRemainder[{0, 19}, {23, 100}]
# 1219

# F[p1_, p2_] := ChineseRemainder[{0, p1}, {p2, 10^IntegerLength[p1]}]
# Total[Map[F[Prime[#], Prime[# + 1]] &, Range[3, PrimePi[10^6]]]]


