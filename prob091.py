from euler import *

def naive_triangle2( xy_max ):
    p0 = (0, 0)
    for x1 in xrange(xy_max):
        for y1 in xrange(xy_max):
            if x1 == 0 and y1 == 0:
                continue
            d = gcd(x1, y1)
            if d == 0 and y1 == 0:
                dy = 1
                dx = 0
            else:
                dy = x1 / d
                dx = -y1 / d
            #print 'X', x1, y1, (dx, dy)
            for i in xrange(-(xy_max+1), xy_max+1):
                if i == 0:
                    continue
                x2 = x1 + i * dx
                y2 = y1 + i * dy
                if x2 < 0 or x2 >= xy_max:
                    continue
                if y2 < 0 or y2 >= xy_max:
                    continue
                if x2 == 0 and y2 == 0:
                    continue
                if ((x1 == x2) and (y1 == y2)):
                    continue
                yield p0, (x1,y1), (x2,y2)

def naive_triangle( xy_max ):
    p0 = (0, 0)
    for x1 in xrange(xy_max):
        for y1 in xrange(xy_max):
            for x2 in xrange(xy_max):
                for y2 in xrange(xy_max):
                    if x1 == 0 and y1 == 0:
                        continue
                    if x2 == 0 and y2 == 0:
                        continue
                    if x1 == x2 and y1 == y2:
                        continue
                    yield p0, (x1,y1), (x2,y2)

def dsq(x):
    return x[0]**2+x[1]**2

def check(u, v):
    x1, y1 = u
    x2, y2 = v
    assert(x1 < xy_max)
    assert(x2 < xy_max)
    assert(y1 < xy_max)
    assert(y2 < xy_max)

def valid(iterable):
    res = set()
    for x, y, z in iterable:
        #check(y,z)
        al = dsq(y)
        bl = dsq(z)
        cl = dsq((y[0]-z[0],y[1]-z[1]))
        al, bl, cl = sorted([al, bl, cl])
        if al + bl - cl == 0:
            res.add( tuple(sorted([x, y, z])) )
    return res

def solve(n):
    return len(valid(naive_triangle2(n+1))) + n**2

print solve(50)
