"""Project Euler 127

Status: started
Url: https://projecteuler.net/problem=127
Keywords: radical, gcd, prime factor
GitHub: https://github.com/AndrewWalker/project-euler/blob/master/prob127.py

Q. What is easy ?
A. Checking if a number is an abc hit

    We already have gcd and radical is trivial

    Is_abc_hit(a,b) -> bool

Q. Can we enumerate?
A. Yep

    Find_hits(b)
    For a in range b
        If coprime a b and is Is_abc_hit
                Yield a, b

Q. Does that look slow?
A. Yep

~ 120000^2

The naive approach is too slow

Q. Alternatives?
A. Maybe radicals are rare?

Radicals are Product P_i^a_i
Radicals are composite

a, b, c
b = a + b'
b' = b- a
b'>0
c = 2a + b'

abc = a(a+b')(2a+b')

= (a^2 + ab')(2a + b')
= 2a^3 + 4a^2 b' + a b'^2

abc = ab(a+b) = a^2 b + b^2 a

Q. C is valid iff sum P_i < c How many sums of primes less than c?
A. Does it then become a dynamic programming question

While P < C
    Recurse C - P
        P = Pnext
"""

from euler import gcd, radical

print radical(504)

#def abchit(a, b, c):
    #if gcd(a, b) != 1 or gcd(b, c) != 1 or gcd(a, c) != 1:
        #return False
    #if a >= b:
        #return False
    #if a+b-c != 0:
        #return False
    #if radical(a*b*c) >= c:
        #return False
    #return True

##print abchit(5, 27, 32)

#for c in xrange(3, 1000):
    #for b in xrange(2, c-1):
        #a = c - b
        #print a, b, c


