from euler import factorial, digits
import sys

def digit_factorial_sum(n):
    ds = digits(n)
    return sum([ factorial(d) for d in ds ])

def prob34():
    cnt = 0
    # upper bound is an educated guess
    for i in xrange(3, 10**5):
        if i == digit_factorial_sum(i):
            cnt += i
    return cnt

print prob34()
