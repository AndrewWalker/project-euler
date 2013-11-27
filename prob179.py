L = 10**7

n = [0]*L
for i in xrange(2, int(L/2)):
    for j in xrange(i*2, L, i):
        n[j] += 1

cnt = 0
# 0 and 1 are wonky, got this wrong the first time because they got taken
# into account when they aren't important
for i in xrange(2, L-1):
    if n[i] == n[i + 1]:
        cnt += 1

print cnt
