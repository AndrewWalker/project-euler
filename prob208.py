"""Project Euler 208 - Robot Walks

http://projecteuler.net/problem=208

Question. At any step how many actions can you take?

    Two.
        clockwise (forward)
        anticlockwise (forward)

Question. After `n` steps, how many possiblities are there?

    2^n

Question. How can you represent endpoint state (naively?)

    (x, y, theta)

Question. What are the basic constraints on a path?

    sum( change in x ) = 0
    sum( change in y ) = 0
    sum( change in theta) = 0

Question. Any significant implications?

    sum(change in theta) = 0
    implies
        (ACW - CW) mod 5 == 0

    This implies that given a number of CW and a length, you can tell how
    many ways there are to make a valid solution (which will be very much
    less than 2^n)

Question. Any significant challenges?

    Perhaps rounding errors?  Working out that you're exactly
    back at (0,0,0) is potentially tricky

    cos((2*pi*i)/5) is not rational

    Given there are only 5 possible changes in x and y, could
    count these?

Question. How can you implement transitions

    x_{i+1} = x_i + xtable[theta_i][direction]
    y_{i+1} = y_i + ytable[theta_i][direction]

Question. Anything significant about transitions

    In mathematica (ie/ being lazy):

        x = Simplify[Cos[(2 \[Pi] (i + 1))/5] - Cos[2 \[Pi] i /5]]
        Simplify[Map[x /. i -> # &, Range[-5, 4]]] // TableForm
        y = Simplify[Sin[(2 \[Pi] (i + 1))/5] - Sin[2 \[Pi] i /5]]
        Simplify[Map[y /. i -> # &, Range[-5, 4]]] // TableForm

    x : 0 -> 1,  A = (-5+sqrt(5))/4
        1 -> 2,  B = -sqrt(5)/2
        2 -> 3,  0 = 0
        3 -> 4, -B = sqrt(5)/2
        4 -> 0, -A = (5-sqrt(5))/4
        0 -> 4,  A
        4 -> 3,  B
        3 -> 2,  0
        2 -> 1, -B
        1 -> 0, -A

#def transition(t, c, res):
    #d = {
        #(0, 1) : (0, 1)
        #(1, 1) : (1, 1)
        #(3, 1) : (1,-1)
        #(4, 1) : (0,-1)
        #(0,-1) : (0, 1)
        #(4,-1) :


    so as ugly as they are, there are still symmetries

Question. Does this help?

    change in x = n A + m B = 0
    change in y = p C + q D + r E = 0

Question. Can this be used to form a new state space?

    Yes

        (n, m, p, q, r, theta)

    Where n,m,p,q,r,theta are integers
"""
import math

def test_angle_sum(s):
    t = 0
    for c in s:
        if c == 'l':
            t -= 1
        else:
            t += 1
        t = t % 5
    return t % 5 == 0

assert test_angle_sum('lrlllrrrrlrrlrllllrllrlll')
assert test_angle_sum('rrrrrrrrrrrrlrllllrllrlll')
assert test_angle_sum('llllllllllrrlrllllrllrlll')
assert test_angle_sum('lllll')
assert test_angle_sum('llllrll')

#for i in xrange(1,6):
    #a = i*72%360
    #y = math.cos(math.radians(a))
    #x = math.sin(math.radians(a))
    #print a, x, y

#CW  = 0
#CCW = 1
#transitions = {
    #(0, CCW) : (-1, 0, 1),
    #(1, CCW) : ( 0,-1, 1),
    #(2, CCW) : ( 0, 0, 1),
    #(3, CCW) : ( 0, 1, 1),
    #(4, CCW) : ( 1, 0, 1),

    #(0,  CW) : (-1, 0,-1),
    #(1,  CW) : ( 0,-1,-1),
    #(2,  CW) : ( 0, 0,-1),
    #(3,  CW) : ( 0, 1,-1),
    #(4,  CW) : ( 1, 0,-1),
#}

#def get_dir(c):
    #if c == 'l':
        #return CCW
    #return CW

#def trace(src):
    #s = {
        #'n' : 0,
        #'m' : 0,
        #'t' : 0,
    #}
    #for c in src:
        #tr = transitions[(s['t'], get_dir(c))]
        #s['n'] += tr[0]
        #s['m'] += tr[1]
        #s['t'] = (s['t'] + tr[2]) % 5
        #yield c, s

#for c, s in trace('lrrl'):
    #print c, s['n'], s['m'], s['t']

def step(x, u):
    xx, yy, tt = x

