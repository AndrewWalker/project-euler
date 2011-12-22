def triangle(n):
    return n*(n+1)/2

def pentagon(n):
    return n*(3*n-1)/2

def hexagon(n):
    return n*(2*n-1)

maxv = 100000
t = set([ triangle(i) for i in range(maxv) ])
p = set([ pentagon(i) for i in range(maxv) ])
h = set([ hexagon(i) for i in range(maxv) ])

s = t.intersection(p).intersection(h)
s = list(s)
s.sort()
print s

#for i in range(500):
#    if  and pentagon(i) and hexagon(i):
#        print 

