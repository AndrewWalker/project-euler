import numpy
import collections
import pyplan.astar
import pyplan.dijkstra

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
    vecs = [ (1,0),(0,1),(0,-1) ]
    x,y = matrix.shape
    g = Grid(x,y)
    E = []
    for y in range(g.height):
        for x in range(g.width):
            for vx,vy in vecs:
                if g.inside(x+vx,y+vy):
                    s = g.pt2idx(x,y)
                    d = g.pt2idx(x+vx,y+vy)
                    c = matrix[x+vx,y+vy]
                    E.append( (s,d,c) )
    return g,E

class Search82(pyplan.dijkstra.DijkstraSearch):
#class Search82(pyplan.astar.AStarSearch):
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
        pyplan.dijkstra.DijkstraSearch.__init__(self,self.numStates)
#        pyplan.astar.AStarSearch.__init__(self,self.numStates)

    def pt2idx(self,x,y):
        return self.grid.pt2idx(x,y)

    def idx2pt(self,idx):
        return self.grid.idx2pt(idx)

    def matrixCost(self,p):
        x,y = self.idx2pt(p)
        return self.matrix[x,y]

    def cost(self, s0, s1):
        return self.C[ (s0,s1) ]

    def successors(self, s):
        return self.adj[s]

#def solve():
#    s = Search82()
#    lst = []
#    for src in range(3):
#        for dst in range(3):
#            qi = s.pt2idx(0,src)
#            qg = s.pt2idx(79,dst)
#            path = s.search(qi,qg)
#            costs = [ s.matrixCost(p) for p in path ]
#            costs = sum(costs)
#            lst.append(costs)
#            print src,dst
#        print '.'
#
#import profile
#
#profile.run('solve()')
#

s = Search82()
s.solve(80)
#print [ n.g for n in s.nodes ]
