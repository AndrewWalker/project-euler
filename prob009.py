"""Project Euler 9 - Special Pythagorean Triplet

url: https://projecteuler.net/problem=9
status: complete
keywords: pythogrean-triplet
"""
import math

def square(n):
    return n - int(math.sqrt(n))**2 == 0


lst = []
for a in range(1,1000):
    for b in range(a,1000):
        if 1000-a-b > b:
            lst.append((a,b,1000-a-b))

sqs = [ i*i for i in range(1000) ]
l1 = [ (a,b,c) for a,b,c in lst if a*a+b*b-c*c == 0]
print reduce(lambda a,b : a*b, l1[0], 1)

