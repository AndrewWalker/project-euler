from euler import *

x = range(12)

def enumerate_special_subsets(x):
    items = list(power_sets_iter(x, min_size= 1))
    for i, u in enumerate(items):
        for j, v in enumerate(items):
            if j > i and u.isdisjoint(v):
                yield u, v

print len(list(enumerate_special_subsets(x)))
