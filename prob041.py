import euler

for i in range(9):
    print '----'
    lst = range(1,i+2)
    lst.reverse()
    for perm in euler.permutations(lst):
        v = euler.seqToInt(perm)
        if euler.isprime(v):
            print v
            break
