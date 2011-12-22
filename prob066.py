# pell's equation
import math
import euler
import fraction
import decimal
    
decimal.getcontext().prec = 100

def continuedFraction( value ):
    dig = value.to_integral( decimal.ROUND_FLOOR )
    #dig = int(math.floor( value ))
    rem = value - dig 
    rec = decimal.Decimal(1) / rem
    return rem,rec,int(dig)

def getCF( v0, n ):
    v = v0
    seq = []
    for i in xrange(n):
        a,v,d = continuedFraction( v )
        seq.append(d)
    return seq

def convergent( seq ):
    if len(seq) == 1:
#        print 'X'
        return fraction.Fraction(seq[0],1)
    else:
        a = fraction.Fraction(seq[0],1)
        b = fraction.Fraction(1,1)/convergent(seq[1:])
        c = a+b
        c = c.cancel()
#        print 'Y',a,b,c
        return c

def pell( v0 ):
    seq = []
    i = 0
    v = decimal.Decimal(v0).sqrt()#math.sqrt(v0)
    while 1:
        a,v,d = continuedFraction( v )
        seq.append(d)
        if len(seq) > 1:
            f = convergent(seq)
            f = f.cancel()
            h = f.num
            k = f.den
            #print seq,f
            if h*h - v0*k*k == 1:
                return h,k
        i += 1    
        assert(i < 100)

#print continuedFraction(decimal.Decimal(61).sqrt())
#print getCF( decimal.Decimal(61).sqrt(), 22 )

lst = []
for i in range(1001):
    if not euler.isSquare(i):
        x,y = pell(i)
        print i,'-',x,'/',y
        lst.append((x,i))

print lst[max( range(len(lst)), key = lambda i : lst[i][0] )][1]

#print pell(61)

#maxv = 24
#seq = getCF( decimal.Decimal(61).sqrt() , maxv )
#print seq
#for i in range(1,maxv):
#    f = convergent(seq[:i])
#    h = f.num
#    k = f.den
#    print h,k,h*h-61*k*k
