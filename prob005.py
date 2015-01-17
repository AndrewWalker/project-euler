"""Project Euler 5

url: https://projecteuler.net/problem=5
status: complete
Keywords: divisors, guess

"""
import math

def main():
    # guess that these primes occur occur in power 1
    x = 11*13*17*19

    # count upwards
    i = 1
    while 1:
        y = x * i
        # check divisibility 
        res = [y%j==0 for j in xrange(2,21)]
        if all(res):
            break
        i += 1

    print x * i

main()
