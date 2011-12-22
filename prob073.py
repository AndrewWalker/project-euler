import fraction

def fracs(maxv):
    lb = fraction.Fraction(1,3)
    ub = fraction.Fraction(1,2)
    for d in range(maxv+1):
        for n in range((d/3)-1,(d/2)+1):
            f = fraction.Fraction(n,d)
            if f.canCancel() == False:
                if f > lb and f < ub:
                    yield f,n,d

cnt = 0
for f,n,d in fracs(10000):
    cnt+=1
    if cnt % 10000 == 0:
        print cnt,n,d

print cnt
