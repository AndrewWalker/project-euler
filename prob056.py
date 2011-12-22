import euler

res = []
for a in range(2,100):
    for b in range(2,100):
        v = sum(euler.intToSeq(a**b))
        res.append(v)
print max(res)
#    res.append([ sum(euler.intToSeq(2**b)) for b in range(100) ]))
#print max(res)
