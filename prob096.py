import sys

class Sudoku:
    constraints = None 
    w = 9
    h = 9

    def __init__(self, lst = [ 0 for i in range(81) ]):
        self.lst = lst

    def clone(self):
        return Sudoku( list(self.lst) )

    def getGaps( self ):
        return [ i for i,v in enumerate(self.lst) if v == 0 ]

    def numGaps( self ):
        return len( self.getGaps() )

    def valid( self, idx, val ):
        const = [ self.lst[i] for i in Sudoku.constraints[idx] ]
        return val not in const

    def render(self):
        for y in range(9):
            for x in range(9):
                v = self.lst[ self.pt2idx(x,y) ]
                if v == 0:
                    print '.',
                else:
                    print v,
            print

    @staticmethod
    def pt2idx( x,y ):
        return y*Sudoku.w + x

    @staticmethod
    def idx2pt( idx ):
        return idx%Sudoku.w, idx/Sudoku.w

    @staticmethod
    def getBlock( ax, ay ):
        x = (ax*3)/Sudoku.w
        y = (ay*3)/Sudoku.h
        lst = []
        for yi in range(3):
            for xj in range(3):
                lst.append( (3*x+xj, 3*y+yi) )
        return lst

    @staticmethod
    def buildConstraints():
        def unique( lst ):
            return set(lst)
        d = {}
        for y in range(Sudoku.h):
            for x in range(Sudoku.w):
                row = [ (i,y) for i in range(Sudoku.w) ]
                col = [ (x,i) for i in range(Sudoku.h) ]
                blk = Sudoku.getBlock(x,y)
                pts = list(unique( row+col+blk ) - set([ (x,y) ]))
                idx = [ Sudoku.pt2idx(i,j) for i,j in pts ]
                idx.sort()
                me  = Sudoku.pt2idx(x,y)
                d[me] = idx
        Sudoku.constraints = d

def solve(s,func = None):
    def impl(s,gaps):
        if gaps == []:
            return s
        else:
            if func != None:
                func(gaps)
            sc = s.clone()
            g  = gaps[0]
            for i in range(1,10):
                if sc.valid(g,i):
                    sc.lst[g] = i
                    soln = impl(sc, gaps[1:])
                    if soln != None:
                        return soln
            return None 
    gaps = [ i for i in range(81) if s.lst[i] == 0 ]
    return impl( s, gaps )

class status:
    def __init__(self):
        self.deepest = 82

    def __call__(self,gaps):
        lgaps = len(gaps)
        if lgaps < self.deepest:
            self.deepest = lgaps
            print lgaps,
            sys.stdout.flush()
import profile

def solveProblem(i):                
    Sudoku.buildConstraints()

    f = open('sudoku.txt','r')
    lines = f.readlines()
    f.close()

    s = lines[i*10+1:(i+1)*10]
    s = [ line[0:9] for line in s ]
    s = ''.join(s)
    s = [ int(j) for j in s ]
    img = Sudoku(s)
    res = solve(img,status())
    return res.lst[0:3]
    #print 
    #print 'problem',i
    #res.render()

try:
    vals = []
    for i in range(50):
        vals.append(tuple(solveProblem(i)))
        print '\n'
    
    tmp = [ int(''.join([ str(c) for c in v])) for v in vals ]
    for t,v in zip(tmp,vals):
        print t,v
    print 'soln',sum(tmp)
except KeyboardInterrupt:
    print 'keyboard stop'
