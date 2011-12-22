import numpy

def loadMat(fname):
    f = open(fname,'r')
    lines = f.readlines()
    lines = [ [ int(t) for t in line.split(',') ] for line in lines ]
    f.close()
    return lines


A = numpy.array(loadMat('data/matrix.txt'))
#A = A[:5,:5]
A = A.transpose()
print A
#A = numpy.array([[131,673,234,103,18],
#[201,96,342,965,150],
#[630,803,746,422,111],
#[537,699,497,121,956],
#[805,732,524,37,331]])
#A = A.transpose()
#print A
S = numpy.zeros(A.shape)
N = A.shape[0]
for y in range(N):
    S[0][y] = A[0][y]
    for x in range(1,N):
        S[x][y] = 10**12
for x in range(1,N):
    for s in range(N):
        for t in range(N):
            p = min(s,t)
            q = max(s,t)
            v = S[x-1][s] + sum([ A[x][i] for i in range(p,q+1) ])
            S[x][t] = min(S[x][t],v)
    print x
S = S.transpose()
print S
print S[:,N-1]
print min(S[:,N-1])
