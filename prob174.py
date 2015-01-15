"""Project Euler 174. Count the number of "hollow" square laminae

Status:   Finished
Url:      https://projecteuler.net/problem=174
Keywords: Difference of squares, Pell Equation, Diophantine

See Also
========

    https://projecteuler.net/problem=173

Process
=======

Q. What's hard?
A. Picking out all solutions in the form

    x^2 - y^2 = n, for an arbitrary n

Q. Is the equation familiar?
A. Yep, it's a modified Pell equation 

    x^2 - N y^2 = k

Q. Any good reading?
A. Yep,

    http://en.wikipedia.org/wiki/Pell%27s_equation
    http://en.wikipedia.org/wiki/Difference_of_two_squares
    http://www.ams.org/notices/200202/fea-lenstra.pdf

    Looking at some stuff Euler links to in the forums 

    https://www.ocf.berkeley.edu/~wwu/cgi-bin/yabb/YaBB.cgi?board=riddles_medium

Q. Is that helpful?
A. Not really in this case - it's easy enough if you do it right

Retrospective
=============

Q. What went wrong?

A. Didn't look to see if this problem was related to anything else

    It was, to 173

A. Didn't do a type analysis

    The problem would have been easier if L and N were more clearly
    defined to work out what they were (still not convinced what I did
    worked very well, or makes sense)

A. The original code wasn't clear at all

    It need to be thrown away, even though the algebra was right

A. I was a bit to obsessed with finding a general solution

    I should have just got on with it

Q. How long did it take?
A. 
    - About 20 Minute of thinking / research time
    - About 10 Minutes to disprove an idea
    - About 20 Minutes to implement
    - About 15 Minutes typing out notes / tidy up

Q. What went right?
A. 
    - Writing out pseudo code to say what you want (top down design)
    - Doing a Big Oh analysis

"""
import collections
from pprint import pprint
from euler import *

def laminae_area(inner, outer):
    return outer**2 - inner**2

def laminae(tmax):
    """Iterator over all the possible numbers of tiles used
    """

    # The actual peformance characteristics for this function
    # can be calculated by pencil and paper to make sure it will
    # converge (fast enough) for the one minute guideline
    #
    # The thinest laminae will be the inner radius + 2 units across
    #
    # basically the inner loop converges very quickly, and the
    # running time of the outer loop is sufficiently small.
    inner = 1 
    while laminae_area(inner, inner+2) < tmax:
        outer = inner + 2
        while laminae_area(inner, outer) < tmax:
            yield laminae_area(inner, outer) 
            outer += 2
        inner += 1

# d is mapping of #tiles : frequency
d = collections.defaultdict(int)
for j, t in enumerate(laminae(10**6)):
    d[t] += 1

# L is mapping of frequency : frequency-occurance
L = collections.defaultdict(int)
for k, v in d.iteritems():
    L[v] += 1

print sum(L[i] for i in xrange(1,11))



