import collections
import matplotlib.pyplot as plt

colors = collections.defaultdict(int)

def next( x, y, d, colors ):
    dd = {
        0 : -1,
        1 :  1
    }
    d = (d-dd[colors[(x,y)]])%4
    stp = {
        0 : ( 1, 0),
        1 : ( 0,-1),
        2 : (-1, 0),
        3 : ( 0, 1),
    }
    colors[(x,y)] = 1 - colors[(x,y)]
    return x+stp[d][0], y+stp[d][1], d        

def cnt():
    return sum(colors.values())

lst = []
x,y,d = (0,0,0)
for i in xrange(1000):
    x,y,d = next(x,y,d,colors)
    lst.append( cnt() )
print lst
#plt.plot(lst)
#plt.show()
