def cumsum(lst):
    cnt = 0
    for item in lst:
        cnt += item
        yield cnt+1

def pairs(seq):
    for i in xrange(len(seq)-1):
        yield seq[i], seq[i+1]

lst = [6*i for i in xrange(7)]
#print list(cumsum(lst))
for i, j in pairs(list(cumsum(lst))):
    print i+1, j

