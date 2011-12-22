def coinpiles( x ):
    def impl( x, maxval,stack ):
        vals = range(maxval+1)
        cnt = 0
        for p in vals:
            if x - p == 0:
                cnt += 1
                print stack + [p]
            elif x - p > 0:
                cnt += impl(x-p,p,stack+[p]) 
        return cnt
    return impl(x,x,[])

print coinpiles(5)
'''
oooooo
ooooo o
oooo oo
oooo o o
ooo ooo
ooo oo o
ooo o o o
oo oo oo
oo oo o o
oo o o o o
'''
