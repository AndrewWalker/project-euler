"""Project Euler 137 - Fibonacci golden nuggets

url : https://projecteuler.net/problem=137
status: started

Q. Why does this problem appear hard?
A. Because it has an infinite series in it - can't do much with that.

Q. Does the question have any hints?
A. Golden is a bit of a hint, but just go read wikipedia.

    http://en.wikipedia.org/wiki/Fibonacci_number

Q. What do you learn from that page?
A. The series in the question is convergent (for some values of x)

A_f(x) = x/(1-x-x^2)

Solving you get:

n           = x/(1-x-x^2)
n(1-x-x^2)  = x
n-nx-nx^2   = x
n-nx-x-nx^2 = 0
n-(1+n)x-nx^2 = 0
nx^2+(1+n)x-n = 0

co-efficients

a = n
b = 1+n
c = -n

Give the terms of the quadratic solution. Or you could just plug it into Mathematica

x(n) = (-1 -n + sqrt(1+2*n+5*n^2))/(2*n)

Q. So what is a golden nugget?
A. Solutions in the form

    1 + 2n + 5n^2
    that are perfect squares

Q. Can you enumerate the solutions?
A. No, it's too slow

Q. So how do you enumerate them quickly?
A. Possibly use complete the square / pells equation?



"""
import euler
import math

def is_square(x):
    return math.ceil(math.sqrt(x))**2 == x

def is_nugget(x):
    return is_square(1+2*x+5*x**2)

def show(x):
    return x/(1.0 - x - x**2)

def inv(x):
    return (-1-x+math.sqrt(1 + 2.0*x + 5*x**2))/(2*x)

def tests():
    assert (math.sqrt(13)-2)/3.0, inv(3.0)
    assert (math.sqrt(89)-5)/8.0, inv(4.0)

# enumeration
for n in xrange(1, 20):
    print inv(n)
#for n in xrange(1, 10**7):
#    if is_nugget(n):
#        print n


