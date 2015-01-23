"""Problem 158 lexicographical strings

Url: 
Status: complete
Keywords: dynamic programming

Q. How many possiblities if we didn't care about order for a three Char string?
A.

26 . 25 . 24 = 15600

Q. Why is that important?
A. It's an Upper bound

Q. If you tried the all lengths of string in this way?
A. Factorials still give an upper bound

n! / (26-n)!

Q. Comments?
A.

If L = 3 (three choices from the alphabet) if you choose y or z you cannot
finish. You only have 24 choices at step 1.

If you choose x in step 0, then in step 1 you have 26 -1 - x choices

Q. Given that way of choosing, write a type definition 
A. 

Int, Int -> Int
Choice minv, todo

Q. Now write the body
A.

    _, 0 = 1
    26, _ = 0
    minv, todo = sum map (/x Choice x+1 Todo-1) [minv..26]

Q. What looks icky?
A. Validating the induction steps 

Does it really count as 1 regardless of minv? Maybe this is just baked
into this way of doing things

That x+1 looks icky, but it basically says if I picked x this time, next
time it

Q. Looks slow
A. Memoize

Q. Was that hard? 
A. Nope

Q. Think you're done?
A. Nope

Q. Guess the value of minimum n?
A. About 13 ~ 18

Q. What code should you write first?
A. Tests

Generate and check each one

Brute force upto 5 or 6


Make sure you get the presented results

Q. Ok, what did you do wrong?
A. Didn't read the question.

    Sigh.

    Exactly one character comes lexicographically after it's neighbour to
    the left

Q. Is what you've got useless?
A. No.

    homeomorphisms

    what we've done is enumerate all the ways you can pick a sorted 
    set of letters.

    *all* we need to do now is find out how many ways, for n letters,
    you can have one letter out of place

    for all permutations of 0..n, how many have one item out of order

Q. Given that you've worked that out, visualise it
A. ok.

    permutation, delta
    (0, 2, 1) [0, 1]    1,1
    (1, 0, 2) [1, 0]    0,1
    (1, 2, 0) [0, 1]    0,2
    (2, 0, 1) [1, 0]    


    permutation, delta
    (0, 1, 3, 2) [0, 0, 1]  2,1
    (0, 2, 1, 3) [0, 1, 0]  
    (0, 2, 3, 1) [0, 0, 1]
    (0, 3, 1, 2) [0, 1, 0]
    (1, 0, 2, 3) [1, 0, 0]
    (1, 2, 0, 3) [0, 1, 0]
    (1, 2, 3, 0) [0, 0, 1]
    (1, 3, 0, 2) [0, 1, 0]
    (2, 0, 1, 3) [1, 0, 0]
    (2, 3, 0, 1) [0, 1, 0]
    (3, 0, 1, 2) [1, 0, 0]

    permutations, delta
    (0, 1, 2, 4, 3) [0, 0, 0, 1]
    (0, 1, 3, 2, 4) [0, 0, 1, 0]
    (0, 1, 3, 4, 2) [0, 0, 0, 1]
    (0, 1, 4, 2, 3) [0, 0, 1, 0]
    (0, 2, 1, 3, 4) [0, 1, 0, 0]
    (0, 2, 3, 1, 4) [0, 0, 1, 0]
    (0, 2, 3, 4, 1) [0, 0, 0, 1]
    (0, 2, 4, 1, 3) [0, 0, 1, 0]
    (0, 3, 1, 2, 4) [0, 1, 0, 0]
    (0, 3, 4, 1, 2) [0, 0, 1, 0]
    (0, 4, 1, 2, 3) [0, 1, 0, 0]
    (1, 0, 2, 3, 4) [1, 0, 0, 0]
    (1, 2, 0, 3, 4) [0, 1, 0, 0]
    (1, 2, 3, 0, 4) [0, 0, 1, 0]
    (1, 2, 3, 4, 0) [0, 0, 0, 1]
    (1, 2, 4, 0, 3) [0, 0, 1, 0]
    (1, 3, 0, 2, 4) [0, 1, 0, 0]
    (1, 3, 4, 0, 2) [0, 0, 1, 0]
    (1, 4, 0, 2, 3) [0, 1, 0, 0]
    (2, 0, 1, 3, 4) [1, 0, 0, 0]
    (2, 3, 0, 1, 4) [0, 1, 0, 0]
    (2, 3, 4, 0, 1) [0, 0, 1, 0]
    (2, 4, 0, 1, 3) [0, 1, 0, 0]
    (3, 0, 1, 2, 4) [1, 0, 0, 0]
    (3, 4, 0, 1, 2) [0, 1, 0, 0]
    (4, 0, 1, 2, 3) [1, 0, 0, 0]

    1, 4, 11, 26, 57, 120, ...

Q. Comments?
A. Bleh. 

    That pattern is horrible

Q. What do you do if you've got a sequence of numbers (that you don't know
   what to do with)?
A. Stick it in OEIS

    Finds A000295, Eulerian numbers (Euler's triangle, column k=2)

    Heh. That looks like the right thing

Retrospective
-------------

What went wrong
 - didn't read the question
     - in this case it didn't matter too much
     - went from one hard problem to two easier problems
 - took a long time to get it out 1 hour to think, 3 hours to code
 - partially recognised oeisA000295, but not enough to reproduce it

What went right
 - recongising homeomorphisms
     - letters to numbers
     - arbitrary ordered sequences to ranges
 - Did pretty well to estimate upper bounds?
 - Visualisation / counting helped
     - Using OEIS was genius where it happened
 - Getting an induction out was huge 
     - recognised optimal substructre
     - writing the pseudocode in haskell helped heaps
     - recognised memoization would be necessary

"""
from euler import *

def sorted_choice(n, k):
    """How many are there to choose k things from n, where the choices are in sorted order

    n is the number of things to choose from
    k is how many to choose
    """

    @in_mem_memoize
    def sorted_choice_impl(n, k, minv):
        """
        minv is the lowest value permissable
        """
        if k == 0:
            return 1
        if minv == n:
            return 0
        return sum([ sorted_choice_impl(n, k-1, i+1) for i in xrange(minv, n) ]) 

    return sorted_choice_impl(n, k, 0)

def prob158():
    items = []
    for i in xrange(1, 26):
        items.append(sorted_choice(26, i)*oeisA000295(i))
    print max(items)

prob158()

