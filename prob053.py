import euler

f = { 0 : 1 }
for i in range(1,101):
    f[i] = i * f[i-1]

def ncr(n,r):
    return f[n] / (f[r]*f[n-r])

#print ncr(23,10)
cnt = 0
maxv = 100
for n in range(1,maxv+1):
    for r in range(1,n+1):
        if ncr(n,r) > 1000000:
            cnt += 1

print 'soln',cnt
