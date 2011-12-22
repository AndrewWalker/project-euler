import numpy

def grid(n):
    S   = [ (i,j) for i in range(n) for j in range(n) ]
    Sid = range(n*n)
    fwd = dict(zip(S,Sid))
    bak = dict(zip(Sid,S))

    N   = numpy.zeros( (n*n,n*n) )
    for i in range(n):
        for j in range(n):
            for x,y in [(-1,0),(1,0),(0,-1),(0,1)]:
                a = i + x
                b = j + y
                if a >= 0 and a < n and b >= 0 and b < n:
                    p = fwd[(i,j)]
                    q = fwd[(a,b)]
                    N[p][q] += 1
    print N
    for j in range(n*n):
        t = sum(N[:,j])
        print N[:,j],t
        N[:,j] /= t
        #for i in range(n*n):
        #    N[i][j] = N[i][j]/t
    print N

grid(4)
