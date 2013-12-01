"""Code for solving problem 103 from project euler

Keywords: sets, bounds, special sum set

Notes
----------
This is a bit of a side track, but in looking for an equivalent of ParitionsP
in Mathematica in Python, which is (somewhat) similar to the issue of enumerating
subsets [4]. PartitionsP is well know [3], and there is a generating function
in [4] that is related to pentagonal numbers.

References
----------

[1] http://stackoverflow.com/questions/15649331/efficient-enumeration-of-subsets
[2] http://en.wikipedia.org/wiki/Combinatorial_number_system
[3] http://oeis.org/A000041
[4] http://en.wikipedia.org/wiki/Partition_(number_theory)
"""
import euler

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


