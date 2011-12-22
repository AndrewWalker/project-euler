
def factorial(n):
    if n == 0:
        return 1
    else:
        l = range(1,n+1)
        return reduce(lambda a,b: a*b, l, 1)

def choose(n,k):
    assert(n > k)
    return factorial(n) / (factorial(k) * factorial(n-k))

def gridn(dim):
    return factorial(2*dim) / (factorial(dim)**2)

print gridn(2)
print gridn(3)
print gridn(20)

