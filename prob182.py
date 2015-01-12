import euler
import time
import numpy as np

def find_es(phi):
    return (e for e in xrange(2, phi) if euler.gcd(e, phi) == 1)

def unconcealed(p, q, e):
    """Naive solution (too slow)
    """
    n   = p * q
    phi = (p-1)*(q-1)
    assert euler.gcd(e, phi) == 1
    assert e > 1
    assert e < phi

    cnt = 0
    for m in xrange(n):
        c = (m**e) % n
        if c == m:
            cnt += 1
    return cnt

def fast_unconcealed(p, q, e):
    # From the "Handbook of applied cryptography", which is on google
    # books p. 290
    a = (1+euler.gcd(e-1, p-1))
    b = (1+euler.gcd(e-1, q-1))
    return a*b

def trivial_testcase():
    p = 19
    q = 37
    n = p * q
    phi = (p-1)*(q-1)
    for e in find_es(phi):
        u = unconcealed(p,q,e)
        print e, unconcealed(p,q,e), fast_unconcealed(p,q,e)

def prob182():
    p = 1009
    q = 3643
    phi = (p-1)*(q-1)
    cnt = 0
    for e in find_es(phi):
        print e
        u = unc3(p,q,e)
        if u == 9:
            cnt += e
    print 'res=', cnt

prob182()
