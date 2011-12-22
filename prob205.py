import collections
import fraction

def diceVals(n,maxv):
    if n == 0:
        yield []
    else:
        for i in range(1,maxv+1):
            for j in diceVals(n-1,maxv):
                yield [i]+j

def diceProb(n,maxv):
    cnt  = 0
    freq = collections.defaultdict(int)
    for vals in diceVals(n,maxv):
        s = sum(vals)
        freq[s] += 1
        cnt += 1
    return freq,cnt

afreq,acnt = diceProb(9,4)
bfreq,bcnt = diceProb(6,6)

def winners(afreq,bfreq):
    for ak in afreq.keys():
        for bk in bfreq.keys():
            if ak > bk:
                yield ak,bk

def winningFraction():
    res = fraction.Fraction(0,0)
    for ak,bk in winners(afreq,bfreq):
        af = fraction.Fraction(afreq[ak],acnt)
        bf = fraction.Fraction(bfreq[bk],bcnt)
        res += (af*bf)
    print res.toFloat()

winningFraction()
