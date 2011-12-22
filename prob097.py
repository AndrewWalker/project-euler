limit = 10000000000

def pow2digits(p):
    v = 1
    for i in range(0,p):
        v = (v * 2)%limit
        if i % 100000 == 0:
            print i
    return v


print ((pow2digits(7830457)*28433)+1)%limit
#for i in range(100):
#    print pow2digits(i),2**i%limit
