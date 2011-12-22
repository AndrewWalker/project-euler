import euler

def generate(n):
    res = []
    c = 1
    while len(res) < 9:
        res += euler.intToSeq(n*c)
        c+=1
    if len(res) == 9:
        return res
    return None

def isPandigital(seq):
    return len(seq) == len(set(seq)) and (0 not in seq)

res = []
for i in range(1,10000):
    x = generate(i)
    if x != None:
        if isPandigital(x):
            res.append(euler.seqToInt(x))
            print i,x
res.sort()
print res
