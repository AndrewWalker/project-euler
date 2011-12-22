import euler

r = xrange(1,1000001)
s = None
for i,v in zip(r,euler.permutations(range(10))):
    if i == 1000000:
        s = v
        break

s = [ str(i) for i in s ]
s = ''.join(s)
print s
