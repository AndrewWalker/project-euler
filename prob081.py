import numpy
import collections
import pyplan.astar

def loadMatrix(fname):
    return numpy.loadtxt(fname,dtype=type(1),delimiter=',') 

class Grid:
    def __init__(self,w,h):
        self.width = w
        self.height = h

    def pt2idx(self,x,y):
        return y*self.width+x

    def idx2pt(self,idx):
        x = idx % self.width
        y = idx / self.width
        return (x,y)

    def inside(self,x,y):
        if x >= 0 and x < self.width:
            if y >= 0 and y < self.height:
                return True
        return False

def loadEdges(matrix):
    x,y = matrix.shape
    g = Grid(x,y)
    E = []
    for y in range(g.height):
        for x in range(g.width):
            xprime = x + 1
            yprime = y + 1
            if g.inside(xprime,y):
                s = g.pt2idx(x,y)
                d = g.pt2idx(xprime,y)
                c = matrix[xprime,y]
                E.append( (s,d,c) )
            if g.inside(x,yprime):
                s = g.pt2idx(x,y)
                d = g.pt2idx(x,yprime)
                c = matrix[x,yprime]
                E.append( (s,d,c) )
    return g,E

class Search81(pyplan.astar.AStarSearch):
    def __init__(self):
        self.matrix = loadMatrix('data/matrix.txt')
        shp = self.matrix.shape

        grid,E = loadEdges(self.matrix)
        edge = [ (a,b) for a,b,c in E ]
        cost = [ c for a,b,c in E ]

        self.adj = collections.defaultdict(list)
        for e in E:
            self.adj[e[0]].append(e[1])
        self.C   = dict(zip(edge,cost))
        self.grid      = grid
        self.numStates = shp[0]*shp[1]
        pyplan.astar.AStarSearch.__init__(self,self.numStates)

    def pt2idx(self,x,y):
        return self.grid.pt2idx(x,y)

    def idx2pt(self,idx):
        return self.grid.idx2pt(idx)

    def heuristic(self, s0, qg):
        x0,y0 = self.grid.idx2pt(s0)
        x1,y1 = self.grid.idx2pt(qg)
        return abs(x1-x0) + abs(y1-y0)

    def matrixCost(self,p):
        x,y = self.idx2pt(p)
        return self.matrix[x,y]

    def cost(self, s0, s1):
        return self.C[ (s0,s1) ]

    def successors(self, s):
        return self.adj[s]

s = Search81()
qi = s.pt2idx(0,0)
qg = s.pt2idx(79,79)

path = s.search(qi,qg)
#for p in path:
#    print s.idx2pt(p),s.matrixCost(p)

costs = [ s.matrixCost(p) for p in path ]
print 'soln',sum(costs)

