"""Project Euler 495 - 

Writing n as the product of k distinct positive integers

URL: https://projecteuler.net/problem=495
Status: thinking
Keywords: factorial, divisors, product

Q. What do you need to do?
A. Find a function

W(x, n) how many ways can you write x as a product on n distinct integers

Q. Anything that makes that easier?
A. x is a factorial

Q. Give an example for X
A. X = 6! = 720

Q. What?
A. 6 x 5 x 4 x 3 x 2 x 1 = X

Q. Can you write it another way?
A. As products of prime factors

X = (2x3) x 5 x (2x2) x 3 x 2 x 1
X = 5 x 3^2 x 2^4 x 1

Q. Divisors of x will be products of the prime factors?
A. Yep

1 x 2 x 3 x (5x3x2^3)
1 x 2 x 3 x 120

1 x (2^2) doesn't work, repeated 2 or 4

1 x 2 x 5 x (2^3 x 3^2)
1 x 2 x 5 x 72

1 x 2 x (3^2) x (5x2^3)
1 x 2 x 9 x 40

Q. Can you write factorial_prime_factors?
A. Yep

Q. Anything annoying about this?
A. One is annoying 

Q. Does this suggest a naive algorithm? 
A. Yep

def solve_factorial(x, n):
    pfs = factorial_prime_factors(n)
    for c in combinations(pfs, n):
        if len(c) == len(set(c)):
            yield c
""" 
