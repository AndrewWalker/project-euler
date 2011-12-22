def product(seq):
    return reduce(lambda a,b : a*b, seq, 1)

n = 1000000
s = ''
i = 1
while len(s) < n:
    s += str(i)
    i += 1
lst = [1,10,100,1000,10000,100000,1000000]
res = [ int(s[i-1]) for i in lst ]
print s[:100]
print res
print product(res)
