# This is a good example of solving an integer partition problem
# The easiest way to do this is probably using Mathematica, which
# has elegant built-ins for doing this kind of work.
#
# PartitionsP[100] - 1 (where the -1 is to remove the partition with 1 element)
#
# http://en.wikipedia.org/wiki/Partition_(number_theory)
# http://stackoverflow.com/questions/10035752/elegant-python-code-for-integer-partitioning
import euler

# slow code, but this is very obviously correct for small n
# from the SO question. Much too slow for this task.
def slow_integer_partition(n):
     result = set()
     result.add((n, ))
     for x in range(1, n):
         for y in partition(n - x):
             result.add(tuple(sorted((x, ) + y)))
     return result

