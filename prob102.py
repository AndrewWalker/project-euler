import numpy

def extend(v):
    r = numpy.array([ v[0], v[1], 0.] )
    return r

def cross(a,b):
    ea = extend(a)
    eb = extend(b)
    return numpy.cross(ea,eb)

def sameSide(p1,p2, a,b):
    cp1 = cross(b-a, p1-a)
    cp2 = cross(b-a, p2-a)
    if numpy.dot(cp1,cp2) >= 0:
        return True
    return False

def pointInTriangle(p, a, b, c):
    if sameSide(p,a, b,c) and sameSide(p,b, a,c) and sameSide(p,c, a,b):
        return True
    return False

#a = numpy.array([-340.,495.])
#b = numpy.array([-153.,-910.])
#c = numpy.array([835.,-947.])

o = numpy.array([0.,0.])
f = open('data/triangles.txt','r')
cnt = 0
for line in f:
    toks = line.split(',')
    toks = [ int(t) for t in toks ]
    a,b,c,d,e,f = tuple(toks)
    va = numpy.array([a,b])
    vb = numpy.array([c,d])
    vc = numpy.array([e,f])
    if pointInTriangle(o, va,vb,vc):
        cnt += 1
print 'soln',cnt
