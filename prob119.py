import euler
import math
from euler import digits

def is_interesting(i):
    digits  = euler.digits(i)
    sdigits = sum(digits)
    if sdigits == 1:
        return False
    p = math.log(i, sdigits)
    return i == (sdigits**math.ceil(p)) or i == (sdigits**math.floor(p))

# Ok, this is silly brute force, but it worked
lst = []
for i in xrange(2, 2000):
    for j in xrange(2,10):
        x = i**j
        if is_interesting(x):
            lst.append(x)
lst.sort()
lst = [ i for i in lst if i > 10 ]
lst = list(sorted(set(lst)))
for i, v in enumerate(lst):
    print i+1, v
