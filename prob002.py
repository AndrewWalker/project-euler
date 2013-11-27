import itertools

def fibonacci_iter():
    a = 0
    b = 1
    while 1:
        yield a
        b, a = a, b
        a = a+b

vals = itertools.takewhile(lambda val : val < 4*10**6, fibonacci_iter())
vals = ( val for val in vals if val % 2 == 0 )
print sum(vals)
