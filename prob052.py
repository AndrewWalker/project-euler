def digits(n):
    lst = list(str(n))
    lst = [ int(i) for i in lst ]
    return set(lst)

def compareSetSeq( seq ):
    for i in range(len(seq)-1):
        if seq[i] != seq[i+1]:
            return False
    return True

#for x in range(1,4):
x = 1
while 1:
    if x % 10000 == 0:
        print x
    res = [ digits(x*mult) for mult in [2,3,4,5,6] ]
    if compareSetSeq(res):
        print res,x
        break
    x += 1
    
