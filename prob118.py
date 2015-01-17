import euler

def pandigital_prime(n):
    for c in euler.permutations(range(1, 10), n):
        m = euler.from_digits(c)
        if euler.isprime(m):
            yield m


