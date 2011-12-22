def foo(d=4):
    if d == 0:
        yield []
    else:
        for i in range(10):
            for rest in foo(d-1):
                yield [i] + rest

mul = [ 10**i for i in range(6) ]
mul.reverse()

for cidx,c in enumerate(foo(6)):
    a = sum([ mm*cc for mm,cc in zip(mul,c) ])
    b = sum([ cc**5 for cc in c ])
    if a == b:
        print c,''.join([str(ci) for ci in c]),a

