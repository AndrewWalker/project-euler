from euler import *


for i,v in enumerate(fib_iter()):
    l = len(str(v))
    if l == 1000:
        print i,v
        break

