import euler

def pandigital_prime(n):
    for c in euler.permutations(range(1, 10), 9):
        m = euler.from_digits(c)
        if c[0] == 2:
            break
        print m
        if euler.isprime(m):
            yield m

#for p in pandigital_prime(9):
    #print p

# http://www.mathblog.dk/project-euler-41-pandigital-prime/
print euler.isprime(192384576)
