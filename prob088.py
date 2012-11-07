import euler

def divisor_permutations(n, largest):
    if n == 1:
        yield []
    divisors = euler.divisors(n)
    divisors = [ d for d in divisors if d > 1 and d <= largest]
    for d in divisors:
        for rest in divisor_permutations(n/d, d):
            yield [d] + rest

solns = {}
for i in xrange(15000):
    for divs in divisor_permutations(i, i):
        # pad the sequence to the correct length
        act = divs + ([1] * (euler.product(divs) - sum(divs)))
        if len(divs) > 1:
            if len(act) not in solns or solns[len(act)] > i:
                solns[len(act)] = i
vals = set()
for k in xrange(2,12000):
    vals.add(solns[k])
print vals
print 'total', sum(vals)

