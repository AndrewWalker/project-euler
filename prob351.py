import euler

def orcharditer( n ):
    for y in xrange(n):
        for x in xrange(n-y):
            yield (2*(x+1)+y,y)

def valid( pt, n ):
    return  pt[0]+pt[1] <= 2*n

def solve( n ):
    found = set()
    for item in orcharditer(n):
        if item not in found:
            for k in xrange(2,n):
                newpt = (k*item[0], k*item[1])
                if not valid(newpt, n):
                    break
                found.add(newpt)
    #for item in found:
    #    print item
    return len(found)*6+6

def solveb( n ):
    cnt = 0
    for item in orcharditer(n):
        div = euler.gcd(item[0],item[1])
        if div > 1 and max(item[0],item[1])>0:
            #print item, div
            sumitem = (item[0]/div + item[1]/div) 
            if sumitem%2 == 0:
                cnt += 1
    return cnt*6 + 6*n
             

#for i in xrange(5,12):
#    print solve(i)# - solve(i-1)
#    print solveb(i)
solveb(100000)

