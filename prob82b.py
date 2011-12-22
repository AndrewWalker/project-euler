import numpy

def loadMat(fname):
    f = open(fname,'r')
    lines = f.readlines()
    lines = [ [ int(t) for t in line.split(',') ] for line in lines ]
    f.close()
    return lines

def gridGraph( n, m, connList ):

    def conn( s ):
        x = s%n
        y = s/m
        lst = []
        for vx,vy in connList:
            dx = x + vx
            dy = y + vy
            if dx < n and dx >= 0 and dy < m and dy >= 0:
                lst.append((s,dy*n+dx))
        return lst

    s = range(n*m)
    v = [ (i%n,i/n) for i in s ]
    e = []
    for si in s:
        e += conn(si)
    return v,e

def toCombinatronica( v, e, w ):
    ea = [ (v0+1,v1+1) for v0,v1 in e ]
    def aw( s ):
        sd = s-1
        x = sd%w.shape[0]
        y = sd/w.shape[0]
        return w[x][y]
    print 'Graph['
    print '{',','.join(['{{%d,%d}}' % ev for ev in ea ]),'},'
    print '{',','.join(['{{%d,%d}}' % (vv[0],vv[1]) for vv in v ]),'},'
    print 'EdgeDirection -> True'
    print ']'

w = numpy.array(loadMat('data/matrix.txt'))
n,m = 80,80
w = w[0:n,0:m]
x = w.shape[0]
y = w.shape[1]
v,e = gridGraph(x,y,[ (1,0),(0,1),(0,-1) ])
toCombinatronica(v,e,w)

