import numpy
import collections
import pyplan.astar

def loadMatrix(fname):
    return numpy.loadtxt(fname,dtype=type(1),delimiter=',') 

class Search81(pyplan.astar.AStarSearch):
    def __init__(self):
        self.matrix = loadMatrix('data/matrix.txt')
        shp = self.matrix.shape
        self.width  = shp[0]
        self.height = shp[1]

        self.numStates = shp[0]*shp[1]
        pyplan.astar.AStarSearch.__init__(self,self.numStates)

    def pt2idx(self,x,y):
        return y*self.width+x

    def idx2pt(self,idx):
        return (idx%self.width,idx/self.width)

    def heuristic(self, s0, qg):
        x0,y0 = self.idx2pt(s0)
        x1,y1 = self.idx2pt(qg)
        return abs(x1-x0) + abs(y1-y0)

    def matrixCost(self,p):
        x,y = self.idx2pt(p)
        return self.matrix[x,y]

    def cost(self, s0, s1):
        x0,y0 = self.idx2pt(s0)
        x1,y1 = self.idx2pt(s1)
        if s0 == 0:
            return self.matrix[x0,y0] + self.matrix[x1,y1]
        else:
            return self.matrix[x1,y1]

    def inside(self,x,y):
        if x >= 0 and x < self.width:
            if y >= 0 and y < self.height:
                return True
        return False

    def successors(self, s):
        x0,y0 = self.idx2pt(s)
        lst = []
        for dx,dy in [(-1,0),(1,0),(0,1),(0,-1)]:
            x = x0 + dx
            y = y0 + dy
            if self.inside(x,y):
                lst.append( (x,y) )
        return [ self.pt2idx(x,y) for x,y in lst ]

    def solvePathCost(self,qi,qg):
        path = s.search(qi,qg)
        print path
        path = [ self.idx2pt(i) for i in path ]
        cost = [ self.matrix[x,y] for x,y in path ]
        return sum(cost)
        

s = Search81()
qi = s.pt2idx(0,0)
qg = s.pt2idx(79,79)

print s.solvePathCost(qi,qg)



