from euler import *

def in_mem_memoize(fun):
    def inner(*args):
        if not args in inner.d:
            v = fun(*args)
            inner.d[args] = v
            return v
        else:
            return inner.d[args]
    inner.d = {}
    return inner


@in_mem_memoize
def f(x):
    if x <= 1:
        return 1
    else:
        return sum(f(x - y) for y in [1, 2, 3, 4] if x-y>=0)

print f(50)


