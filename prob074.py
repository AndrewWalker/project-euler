import euler

f = [ euler.factorial(i) for i in range(10) ]

def factorialChainNext(n):
    seq = euler.intToSeq(n)
    seq = [ f[i] for i in seq ]
    return sum(seq)

def factorialChain(n):
    lst = []
    while n not in lst:
        lst.append(n)
        n = factorialChainNext(n)
        assert(len(lst)<=60)
    lst.append(n)    
    return lst

def factorialChainLength(n):
    return len(factorialChain(n))-1

def main():
    cnt = 0
    for i in range(3000):
        fc  = factorialChain(i)
        fcl = len(fc)-1
        if fcl==60:
            cnt +=1
            print i,fcl,cnt
        if i % 10000 == 0:
            print '#',i

#import profile
#profile.run('main()')
#main()

def increasingIter(minv,digits):
    def impl(minv,digits):
        if digits == 0:
            yield []
        else:
            for i in [0] + range(minv,10):
                for j in impl(i,digits-1):
                    yield [i] + j
    for i in impl(minv,digits):
        yield euler.seqToInt(i)

res = []
for i in set(increasingIter(0,6)):
    fc  = factorialChain(i)
    fcl = len(fc)-1
    if fcl == 60:
        res.append( i )

final = []
for r in res:
    s = set()
    for p in euler.permutations(euler.intToSeq(r)):
        v = euler.seqToInt(p)
        if factorialChainLength(v) == 60:
            s.add(v)
    for item in s:
        final.append(item)

cnt = 0
final = list(set(final))
final.sort()
for item in final:
    cnt += 1
    print cnt,item,factorialChainLength(item)

print 'soln',cnt


