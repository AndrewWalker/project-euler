"""
Problem 147 rectangles in a cross hatched grid

https://projecteuler.net/problem=147

Q. What is hard?
A. Looks like lots of special cases. Especially for diagonals

Q. What do we do?
A. Look for a pattern

Q. That's hard!
A. Break it into smaller pieces. Can you find a pattern in the horizontal tiles?

By observation, a (straight) tiling of a p x q rectangle with an n x m tile gives

T = (p-n+1)(q-m+1)
For n<=p and m<=q

Q. There is going to be a lot of repeated enumeration?
A. Yes. Memoize

Q. What about diagonals?
A. Symmetry means we only need to worry about half the solutions

D(p,q,n,m) = D(p,q,m,n)

Q. Are there symmetry duplicates?
A. Yep, when m=n

So, only count them once 

Q. Any base cases?
A. Yep, if p =0 or q=0 then D=0
"""
