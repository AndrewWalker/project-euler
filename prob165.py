import mathextra
import euler
import numpy

s0 = 290797
sn = s0

def blumBlumShub():
    global sn
    sn = (sn*sn)%50515093
    return sn % 500
grads = []
lines = set([])
for i in xrange(5000):
    line = ( blumBlumShub() for j in xrange(4) )
    x1,y1,x2,y2 = line
    if x2 - x1 == 0:
        grads.append( float('inf') )
    else:
        grads.append( y2-y1/float(x2-x1) )
grads.sort()
print len(set(grads))
#for m in grads:
#    print m
    
    #arr = numpy.array
    #line = [ arr([a,b]), arr([c,d]) ]
    #lines.append(line)

#for line in lines:
#    print line

def intTests( lines ):
    for i in xrange(len(lines)):
        if i % 10 ==0: print i
        for j in xrange(i):
            if i == j:
                continue
            (x1,y1),(x2,y2) = tuple(lines[i])
            (u1,v1),(u2,v2) = tuple(lines[j])
            dx = x2 - x1
            dy = y2 - y1
            du = u2 - u1
            dv = v2 - v1
            if euler.gcd(dx,du) == euler.gcd(dy,dv):
                print 'parallel',dx,du
                continue                
            else:
                pass
#                l1 = [(x1,y1),(x2,y2)]
#                l1 = [ numpy.array(p) for p in l1 ]
#                l2 = [(u1,v1),(u2,v2)]
#                l2 = [ numpy.array(p) for p in l2 ]
#                pt = mathextra.intersectionSegmentSegment( l1, l2 )
#                if pt != None:
#                    pass
                    #print pt

#intTests(lines)
