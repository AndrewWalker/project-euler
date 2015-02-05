"""Problem 500!!!


Q. How are divisors related to prime factors
A. http://mathschallenge.net/library/number/number_of_divisors

    If you know the prime factorization, you can get the number of divisors

Q. Is that helpful?
A. Yep,

    n = p^a . q^b . r^c ...
    d(n) = (a+1)(b+1)(c+1) ...

Q. What?
A. You don't need to count up, you just need to look at the prime factors

Q. Anything special about the sample?
A. 16 divisors == 2^4 divisors

    16's divisors are [1,2,4,8,16]
    2^n has n-1 divisors

    combinations of 16 are:

    2^0,  2^4 invalid
    2^1,  2^3 -> p1^(2-1) . p2^(8-1)
    2^2,  2^2 -> p1^(4-1) . p2^(4-1)

    this example is to easy to see it, but those are the partitions of
    n, such that the minimum value >= 2

Q. So if you know that, what do you do with it?
A. Something like this?

    def min_divisors(n):
        items = []
        for i in generate_integer_partitions(range(1,n+1),n):
            lst = [2**j for j in i]
            lst.reverse()
            out = [ (sympy.prime(j+1), lst[j]) for j in xrange(len(lst)) ]
            res = euler.product([ p**(a-1) for p, a in out ])
            items.append(res)
        return min(items)

Q. Still not fast enough. What next?
A. It is fast enough to produce sufficient terms to put into OEIS

OEIS A037992

(after much mucking around. solved)

Retrospective
-------------

This problem looked easy, the research turned up good results, and then took
forever to get out.

Pros:
 - Made a really really good start, dug deeply into the maths of primes and divisors
 - Did some really good rapid work exploring the problem space
    - with pencil and paper
    - with brute force
 - Realised how the problem looked like a product of integer partitions 
 - Coded that up (almost first time)
    - Excellent debugging by shortening the stack depth
 - used OEIS
     - identified sequence
     - coded up implementation / solver 
 - managed to pick why the initial implementation was slow (sorting)
     - picked a faster way to insert into a sorted collection


Cons:
 - Found http://www.primepuzzles.net/problems/prob_019.htm which has the answer
   / algorithm embedded in it at the bottom. Didn't read far enough to work
   that out.
 - Churn. 
    - Really struggled to find a good way to write out and describe ideas in a
      way that I can go back to
 - 

"""
import sys
import heapq
import sympy
import euler

# PriorityQueueSet is CC-SA-3.0 
# http://stackoverflow.com/a/407922/2246
class PriorityQueueSet(object):
    """ Combined priority queue and set data structure. Acts like
        a priority queue, except that its items are guaranteed to
        be unique.

        Provides O(1) membership test, O(log N) insertion and 
        O(log N) removal of the smallest item.

        Important: the items of this data structure must be both
        comparable and hashable (i.e. must implement __cmp__ and
        __hash__). This is true of Python's built-in objects, but
        you should implement those methods if you want to use
        the data structure for custom objects.
    """
    def __init__(self, items=[]):
        """ Create a new PriorityQueueSet.

            items:
                An initial item list - it can be unsorted and 
                non-unique. The data structure will be created in
                O(N).
        """
        self.set = dict((item, True) for item in items)
        self.heap = self.set.keys()
        heapq.heapify(self.heap)

    def __len__(self):
        return len(self.heap)

    def has_item(self, item):
        """ Check if *item* exists in the queue
        """
        return item in self.set

    def pop_smallest(self):
        """ Remove and return the smallest item from the queue
        """
        smallest = heapq.heappop(self.heap)
        del self.set[smallest]
        return smallest

    def add(self, item):
        """ Add *item* to the queue. The item will be added only
            if it doesn't already exist in the queue.
        """
        if not (item in self.set):
            self.set[item] = True
            heapq.heappush(self.heap, item)

def oeis_a037992(maxsize):
    cnt = 0
    todo = PriorityQueueSet([(2,2,0)])
    done = set([2])
    while maxsize != cnt:
        out, p, k = todo.pop_smallest()
        yield out
        cnt += 1
        np = sympy.nextprime(p)
        if np not in done:
            todo.add((np,np,0))
            done.add(np)
        todo.add((p**(2**(k+1)), p, k+1))

def prob500():
    cum = 1
    for i, v in enumerate(oeis_a037992(500500)):
        cum *= v
        cum %= 500500507
    return cum

print prob500()
