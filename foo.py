from numpy import *


maxv = 4

def func(maxv):
    a = [ i for i in range(0,maxv) ]
    w = [ i*2+1 for i in a ]

    q1 = [ x*x for x in w ]
    q2 = [ x-(wx-1) for x,wx in zip(q1,w) ]
    q3 = [ x-(wx-1)*2 for x,wx in zip(q1,w) ]
    q4 = [ x-(wx-1)*3 for x,wx in zip(q1,w) ]
    print q1
    print q2
    d = {}
    d[0] = q4
    d[1] = q3
    d[2] = q1
    d[3] = q2

    x = zeros((2*maxv-1,2*maxv-1))
    for i in a:
        b = [(i,i),(i,-i),(-i,i),(-i,-i)]
        for vi,v in enumerate(b):
            qi = array(v)+array((maxv-1,maxv-1))
            x[qi[0]][qi[1]] = d[vi][i]
    return x

def show(x):
    for r in x:
        for c in r:
            if c == 0:
                print '   ',
            else:
                print '%03d' % c,
        print

def cnt(x):
    return int(sum(x))

#print func(501).shape
#show(func(501))

print cnt(func(501))
print sum([ 16*x*x + 4*x + 4 for x in range(501) ]) - 3

