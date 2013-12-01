from euler import *

@in_mem_memoize
def f(x, y):
    #print 'f',x,y
    if x == y:
        return 2
    if x <= y:
        return 1
    return f(x-1, y) + f(x-y, y)

def solve(x, y):
    return f(x, y) - 1

print solve(50,4) + solve(50,3) + solve(50,2)
