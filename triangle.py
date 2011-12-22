import collections
import sys

def load(fname):
    f = open(fname,'r')
    lines = f.readlines()
    f.close()
    del f
    lines = [ line.split() for line in lines ]
    lines = [ [ int(t) for t in line ] for line in lines ]
    nlines = len(lines)
    lines = reduce( lambda a,b:a+b, lines, [])
    return lines,nlines

def triangleNumber(n):
    return sum(range(0,n))

def indexValue(d):
    res = []
    for di in range(d):
        tn = triangleNumber(di+1)
        r = range(tn,tn+di+1)
        res.append(r)
    return res

if __name__ == "__main__":
    fname = sys.argv[1]
    lines,nlines = load(fname)

    E = []
    tri = indexValue(nlines)
    for rowid,row in enumerate(tri[:-1]):
        for colid,col in enumerate(row):
            E.append((col, tri[rowid+1][colid]))
            E.append((col, tri[rowid+1][colid+1]))
    succ = collections.defaultdict(list)
    for e0,e1 in E:
        succ[e0].append(e1)

    # init
    maxv = [ -1 for i in range(len(lines)) ]
    # seed
    for i in tri[-1]:
        maxv[i] = lines[i]
    for i in range(nlines-2,-1,-1):
        row = tri[i]
        for j in row:
            succ_vals = [ maxv[k] for k in succ[j] ]
            maxv[j] = lines[j] + max(succ_vals)

    print maxv[0]
