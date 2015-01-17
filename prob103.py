"""Code for solving problem 103 from project euler

Keywords: sets, bounds, special sum set

Notes
----------

This is a bit of a side track, but in looking for an equivalent of
ParitionsP in Mathematica in Python, which is (somewhat) similar to the
issue of enumerating subsets [4]. PartitionsP is well know [3], and there
is a generating function in [4] that is related to pentagonal numbers.

References
----------

[1] http://stackoverflow.com/questions/15649331/efficient-enumeration-of-subsets
[2] http://en.wikipedia.org/wiki/Combinatorial_number_system
[3] http://oeis.org/A000041
[4] http://en.wikipedia.org/wiki/Partition_(number_theory)
"""
import euler
from euler import *

def upper_bound(n):
    assert(n>0)
    if n == 1:
        return [1]
    else:
        As = upper_bound(n - 1)
        mid_idx = len(As)//2
        if n % 2 == 0:
            mid_idx
        b  = As[mid_idx]
        return [b] + [b+ a for a in As]

def set_string(lst):
    return ''.join('%d' % i for i in lst)

assert(upper_bound(1) == [1])
assert(upper_bound(2) == [1, 2])
assert(upper_bound(3) == [2, 3, 4])
assert(upper_bound(4) == [3, 5, 6, 7])
assert(upper_bound(5) == [6, 9, 11, 12, 13])
assert(upper_bound(6) == [11, 17, 20, 22, 23, 24])

# If the set is:
# {n, n+p, n+p+q}, s.t. {n,p,q} \in Integers and n>0, p>0, q>0
# then
#  2n+p > n+p+q
#  n > q
# If the set is:
#  {n, n+p, n+p+q, n+p+q+r}
# then
#  p > 0
#  n > q;     2n+p > n+p+q => n>q
#             2n+2p+q > n+p+q+r; n+p > r
#  n > q + r; 2n+p > n+p+q+r
#
# Generalizing:
# Union( n + a_i )

#7n + 6p + 5q + 4r + 3s + 2t + u = 271
#n+(n+p+q) != (n+p)+(n+p+q+r)
#2n+p+q    != 2n+2p+q+r
#p         != 2p+r

s = upper_bound(7)
#print s
#print sum(s)

def ruleGen(n, m, sigma):
    """
    Generates all interpart restricted compositions of n with first part
    >= m using restriction function sigma. See Kelleher 2006, 'Encoding
    partitions as ascending compositions' chapters 3 and 4 for details.

    http://www.homepages.ed.ac.uk/jkellehe/downloads/k06.pdf
    """
    a = [0 for i in range(n + 1)]
    k = 1
    a[0] = m - 1
    a[1] = n - m + 1
    while k != 0:
        x = a[k - 1] + 1
        y = a[k] - 1
        k -= 1
        while sigma(x) <= y:
            a[k] = x
            x = sigma(x)
            y -= x
            k += 1
        a[k] = x + y
        yield a[:k + 1]

def enumerate_special_subsets(x):
    items = list(power_sets_iter(x, min_size= 1))
    for i, u in enumerate(items):
        for j, v in enumerate(items):
            if j > i and u.isdisjoint(v):
                yield u, v

def is_special(x):
    for a, b in enumerate_special_subsets(x):
        la = len(a)
        lb = len(b)
        sa = sum(a)
        sb = sum(b)
        if la == lb and sa == sb:
            return False
        if la > lb and sa < sb:
            return False
        if la < lb and sa > sb:
            return False
    return True

minv = 18  # guessed by progressive reduction
for q in xrange(100, 118):
    print q
    for i in ruleGen(q, 11, lambda x : x):
        # hack to reduce the search space of permutations
        if len(i) == 6 and len(set(i)) == 6:
            k = [minv] + [minv+j for j in i]
            if is_special(k):
                print k, sum(k), q, ''.join(str(j) for j in k)
