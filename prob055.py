import euler

def lychrel(n):
    cnt = 0
    while 1:
        a = euler.intToSeq(n)
        b = list(reversed(a))
        a = euler.seqToInt(a)
        b = euler.seqToInt(b)
        n = a+b
        if euler.palindrome(n):
            return True
        if cnt >50:
            return False
        cnt += 1
    return True

cnt = 0
for i in xrange(10000):
    if not lychrel(i):
        cnt += 1
    print i
print 'soln',cnt


