coins = [1,2,5,10,20,50,100,200]
count = [ range((200/i)+1) for i in coins ]

def tally(c):
    return sum([c*v for c,v in zip(c,coins)])

def coinGen(counts,vals,val):
    if counts == []:
        yield []
    else:
        for i in counts[0]:
            curval = val + i*vals[0]
            if curval <= 200:
                for rest in coinGen(counts[1:],vals[1:],curval):
                    comb = [i] + rest
                    yield comb

cnt = 0
for i in coinGen(count,coins,0):
    change = False
    t = tally(i)
    if t == 200:
        cnt += 1
        change = True
    if change and cnt % 1000 == 0:
        print cnt,i

print 'soln = ',cnt
