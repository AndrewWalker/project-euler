from euler import *

@in_mem_memoize
def f(x):
    if x <= 1:
        return 1
    else:
        return sum(f(x - y) for y in [1, 2, 3, 4] if x-y>=0)

print f(50)


