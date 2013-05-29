S = range(1,21) + [25]
D = [2*i for i in S]
T = [3*i for i in range(1,21)]
cells = S+D+T

def f():
    for k in xrange(len(D)):
        yield D[k],

    for i in xrange(len(cells)):
        for k in xrange(len(D)):
            yield cells[i], D[k]


    for i in xrange(len(cells)):
        for j in xrange(i, len(cells)):
            for k in xrange(len(D)):
                yield cells[i], cells[j], D[k]

print sum([1 for t in f() if sum(t) < 100])
