import fraction
import euler

def contFraction(base):
    num = fraction.Fraction(1,1)
    den = fraction.Fraction(2,1) + base
    #print 'CF',num ,'/',den,'=',num/den
    return num / den

def main():
    v = fraction.Fraction(1,2)
    cnt = 0
    for i in range(1,1000):
        v = contFraction(v)
        v = v.cancel()
        r = v+fraction.Fraction(1,1)
        numseq = euler.intToSeq(r.num)
        denseq = euler.intToSeq(r.den)
        if len(numseq) > len(denseq):
            print i+1
            cnt += 1
    print 'soln',cnt

main()
