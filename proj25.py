def fib():
    a = 0
    b = 1
    c = a+b
    yield b
    while 1:
        a = b
        b = c
        c = a+b
        yield b

def take( iter, n ):
    res = []
    for i,v in enumerate(iter):
        res.append(v)
        if i > n:
            return res
    return None

#print take( fib(), 50 )

for j,v in enumerate(fib()):
    i = j +1
    l = len(str(v))
    if l == 1000:
        print i,v
        break

