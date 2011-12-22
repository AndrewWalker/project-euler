import euler
import profile

def perfTest(maxv):
    try:
        for i in range(1,maxv):
            a = euler.isprime(i)
            b = euler.isprime_slow(i)
            assert( a==b )
            if i % 10000 == 0:
                print i
    except:
        print 'break'

perfTest(10000000)
