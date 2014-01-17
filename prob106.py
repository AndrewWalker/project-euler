from euler import *

x = range(12)

def enumerate_special_subsets(x):
    items = list(power_sets_iter(x, min_size= 1))
    for i, u in enumerate(items):
        for j, v in enumerate(items):
            if j > i and u.isdisjoint(v):
                yield u, v

cnt = 0
for u, v in enumerate_special_subsets(range(12)):
    if len(u) == len(v):
        if not all(b>a for a, b in zip(sorted(u), sorted(v))):
            cnt += 1
print cnt
