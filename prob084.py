import itertools
import numpy

s = '''
GO A1 CC1 A2 T1 R1 B1 CH1 B2 B3 
JAIL C1 U1 C2 C3 R2 D1 CC2 D2 D3
FP E1 CH2 E2 E3 R3 F1 F2 U2 F3 
G2J G1 G2 CC3 G3 R4 CH3 H1 T2 H2
'''

id2name = dict([(i,v) for i,v in enumerate(s.split())])
name2id = dict([(v,i) for i,v in enumerate(s.split())])

def stationaryDistribution(p):
    """
    Parameters: 
    
        * p is a 2D NumPy array, assumed to be stationary

    Returns: A flat array giving the stationary distribution
    """
    N = len(p)                                      # p is N x N
    I = numpy.identity(N)                           # Identity matrix
    B, b = numpy.ones((N, N)), numpy.ones((N, 1))   # Matrix and vector of ones
    A = numpy.transpose(I - p + B) 
    solution = numpy.linalg.solve(A, b)
    return solution.flatten()                # Return a flat array


def nextr(s):
    if s <= name2id['R1']:
        return name2id['R1']
    elif s <= name2id['R2']:
        return name2id['R2']
    elif s <= name2id['R3']:
        return name2id['R3']
    elif s <= name2id['R4']:
        return name2id['R4']
    return name2id['R1']

def nextu(s):
    if s <= name2id['U1']:
        return name2id['U1']
    elif s <= name2id['U2']:
        return name2id['U2']
    return name2id['U1']

def back(sid, pos):
    return (sid - pos) % 40
    
def advance(sid, pos):
    return (sid + pos) % 40

def tally(x):
    res = []
    for k,g in itertools.groupby(sorted(x)):
        res.append( (k,len(list(g))) )
    return res

def dice(n):
    x = []
    for i in range(1,n+1):
        for j in range(1,n+1):
            x.append( i+j )
    return [ (k,v/float(n*n)) for k,v in tally(x) ]

def ttable():
    dicevals = dice(4)
    x = numpy.zeros((40,40))
    GO   = name2id['GO']
    JAIL = name2id['JAIL']
    for i in range(40):
        for pos,prob in dicevals:
            j = advance(i,pos)
            if id2name[j] in [ 'CC1','CC2','CC3' ]:
                x[i][GO]   += prob * 1/8.
                x[i][JAIL] += prob * 1/8.
                x[i][j]    += prob * 6/8.
            elif id2name[j] in [ 'CH1','CH2','CH3' ]:
                x[i][GO]            += prob * 1/16.
                x[i][JAIL]          += prob * 1/16.
                x[i][name2id['C1']] += prob * 1/16.
                x[i][name2id['E3']] += prob * 1/16.
                x[i][name2id['H2']] += prob * 1/16.
                x[i][name2id['R1']] += prob * 1/16.
                x[i][nextr(j)]      += prob * 2/16.
                x[i][nextu(j)]      += prob * 1/16.
                x[i][back(j,3)]     += prob * 1/16.
                x[i][j]             += prob * 6/16.
            elif id2name[j] == 'G2J':
                x[i][JAIL] += prob
            else:
                x[i][j] += prob
    return x

P=ttable()

def show(P):
    N = len(P)
    for i in range(N):
        for j in range(N):
            print '%.4f' % P[i][j],
        print 

show(P)
Q = stationaryDistribution(P)*100.0

lst = [ (i,id2name[i],Q[i]) for i in range(40) ]
lst.sort(cmp = lambda u,v : cmp(u[2],v[2]))

for t in lst:
    print '%02d %6s %.4f' % t
