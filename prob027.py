import euler

maxcnt = 0
for a in range(-999,1000):
    for b in range(-999,1000):
        if a != 0 and b != 0:
            cnt = 0
            for n in range(80):
                v = n*n + a*n + b
                if v < 0:
                    break
                #print 'v',v
                if euler.isprime(v):
                    cnt += 1
                else:
                    break
            if cnt > maxcnt:
                print a,b,cnt
                maxcnt = cnt
