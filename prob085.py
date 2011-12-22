
def boxes( w, h ):
    lst = []
    for w in range(1,w+1):
        for h in range(1,h+1):
            lst.append( (w,h) )
    return lst

def fits(bw,bh,w,h):
    return ((w-bw+1)*(h-bh+1))

def boxCount(w,h):
    cnt = 0
    for bw,bh in boxes(w,h):
        v = fits(bw,bh,w,h)
        #print bw,bh,v
        cnt += v
    return cnt

def boxCountIter(maxv):
    for i in range(1,maxv):
        for j in range(i,maxv):
            v = boxCount(i,j)
            if v < 2000000:
                yield (i,j,v,i*j)
            else:
                break

bestv = -1
for i,j,v,a in boxCountIter(1000):
    if v>bestv:
        bestv = v
        print i,j,v,a

# + manual intervention for a likely solution
