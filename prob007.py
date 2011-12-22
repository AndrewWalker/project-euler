import euler

def naturalNumbers():
    i = 1
    while 1:
        yield i
        i += 1

def nthprime(n):
    seen = 0
    for i in naturalNumbers():
        if euler.isprime(i):
            seen += 1
        if seen == (n+1):
            return i

#for i in range(1,10):
#    print i, nthprime(i)
print nthprime(10001)
