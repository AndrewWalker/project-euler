def collatz(n):
    assert(n >= 0)
    if n % 2 == 0:
        return n / 2
    else:
        return 3 * n + 1

def collatzSequence(n):
    s = n
    yield s
    while s != 1:
        s = collatz(s)
        yield s

maxv = 1000000

def part2():
    besti = 0
    best  = 0
    for i in range(1,maxv):
        cs = len(list(collatzSequence(i)))
        if cs > best:
            best  = cs
            besti = i
            print best,besti
        if i % 10000 == 0:
            print i/float(maxv)
    print best,besti

part2()

def part1():
    d = {}
    d[1] = 1
    for i in range(1,maxv):
        if i not in d:
            lst = [ n for n in collatzSequence(i) if n not in d ]
            lst.reverse()
            depth = 0
            if len(lst) > 0:
                depth = d[collatz(lst[0])]
            for idx,v in enumerate(lst):
                if v < maxv:
                    d[v] = depth + idx + 1
        if i % 10000 == 0:
            print i/float(maxv)
    print d

