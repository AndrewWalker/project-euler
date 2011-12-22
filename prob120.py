def f(a,n):
    return ((a-1)**n + (a+1)**n) % a**2

lst = []

amin = 2
amax = 20
nmin = 2
nmax = 50

def g(a):
    if a % 2 == 1:
        return a**2-a
    else:
        return a**2-2*a

print sum([ g(a) for a in range(3,1001) ])

#for a in range(amin,amax):
#    print '%4s' % str(a),
#print
#for a in range(amin,amax):
#    print '%4s' % str(a*a),
#print
#for a in range(amin,amax):
#    print '%4s' % str(g(a)),
#print
#print '--------------------------'
#for n in range(nmin,nmax):
#    for a in range(amin,amax):
#        print '%4s' % str(f(a,n)),
#    print
#
