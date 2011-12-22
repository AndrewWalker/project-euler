import fraction
import euler

maxv = 1000000  
minf = fraction.Fraction(3*maxv-10,7*maxv)
maxf = fraction.Fraction(3,7)

def fracs(maxv):
    lowestSeen = minf
    for d in range(maxv-50,maxv+1):
        for n in range(((lowestSeen.num*d)/lowestSeen.den)-1,d):
            f = fraction.Fraction(n,d)
            f = f.cancel()
            if f > lowestSeen and f < maxf:
                lowestSeen = f
                yield f,d 
            if f >= maxf:
                break
        if d % 1000 == 0:
            print d

minv = None
for f,d in fracs(maxv):
    print f,d,f.toFloat(),minf.toFloat(),maxf.toFloat()

