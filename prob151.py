"""Project Euler 151 - Paper sheets of standard sizes: an expected-value problem


Url: https://projecteuler.net/problem=151
Status: thinking
Keywords: expected value

Q. Anything hard here?  
A. No hints in the question (off by one errors are a real possibility here)


Q. Can we get a good approximation?
A. Yep. Naive Monte Carlo is perfect for this

Basically. simulate the a batch n times, randomly drawing at each step.
Count the number of times per batch that one envelope is left, take the
mean over all batches. Error decrease in sqrt of n, but you should see the
process converge very quickly

Q. What do we need for that?
A. A transition rule. 

Given a piece of size x you add the pieces of the following sizes:

{ 1: { 2:1, 3:1, 4:1, 5:2},
  2: { 3:1, 4:1, 5:2},
  3: { 4:1, 5:2},
  4: { 5:2}}

And remove the one you cut. 

def transition(state, choice):
    newstate = dict(state)
    for k, v in transition[choice]:
        newstate[k] =+ v
    newstate[choice] -= 1
    return newstate 

def batch(x0):
    cnt = 0
    x = dict(x0)
    for i in xrange(16):
        c = uniform_from_state(x0)
        x = transition(x, c)
        if count_slices(x) ==1:
            cnt += 1
    return cnt

x0 = {1:1}
n = 10^7
print mean( batch(x0) for i in xrange(n) )

Q. How long?
A. 30 minutes

Q. Can you do better?
A. Yep

Q. What kind of process is this?
A. It's a Markov chain

    State to state transitions weighted by probability

Q. What is a state?
A. The number of each type of paper

Q. How many states are there?
A. 32? 

Q. How big is the transition matrix?
A. 32 x 32

Q. What values go into each cell?
A. Easy

0 if no transition can occur
P(x_i, x_j) if one does

Q. How do you work out P?
A. It's 1/n if there are n slices in your state x

Q. What is the one step probability?
A. Easy

P

Q. What is the transition matrix like after n steps?
A. Still easy.

P^n

Q. How do I get out what I want?
A. Break this into smaller steps!

Get the probability of being in a state after n days

Build a column vector, x0, with 1 in your initial state and 0 everywhere
else

Yn = P^n x0 gives the probability of being in a state after n steps if
your initial distribution was x0

Q. And the last bit?
A. 

Build a second vector V which is 1 if there is one sheet and 0 otherwise 

Yn . V gives the expected number of times you had one sheet on day n

Sum over all days of interest 
"""


