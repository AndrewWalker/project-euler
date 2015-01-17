import euler
import itertools
from euler import digits

def ndigits(x):
    return len(euler.intToSeq(x))

def is_reversible(n):
    if n % 10 == 0:
        return False
    m  = n + reverse_number(n)
    dm = digits(m)
    return all([ d % 2 == 1 for d in dm ])

def reverse_number(n):
    """Reverse the order of the digits in a number

    for abc, gives cba
        123, gives 321
    """
    res = 0
    while 1:
        res += n % 10
        n /= 10
        if n == 0:
            break
        res *= 10
    return res

def all_odd_digits(digits):
    """Generator over numbers that have only odd digits
    """
    if digits == 0:
        yield []
    else:
        for i in [1,3,5,7,9]:
            for res in all_odd_digits(digits-1):
                yield [i] + res

def generate_reversible_pairs(x):
    """Given a number, returns all the ways that a number
    and it's reverse can sum to it
    """
    lower_bound = min(1, ndigits(x)-1)
    for i in xrange(lower_bound, x/2+1):
        if i % 10 == 0:
            continue
        if i + reverse_number(i) == x:
            yield i, reverse_number(i)

def odd_digits(d):
    digits = euler.digits(d)
    return [d%2==1 for d in digits]

#vals = []
#for i in xrange(1, 10**6):
    ## trailing zero, skip this one
    #if i % 10 == 0:
        #continue
    #n = i + reverse_number(i)
    #if all(odd_digits(n)):
        #vals.append(i)
        #if len(digits(n)) != len(digits(i)):
            #print i, n#, odd_digits(i)


#import itertools
#def all_odd_digits(max_digits):
    #for j in xrange(2,max_digits+1):
        #res = [(1,3,5,7,9) for _ in xrange(j)]
        #res = tuple(res)
        #for tup in itertools.product(*res):
            #yield tup

#for i, v in enumerate(all_odd_digits(9)):
    #if i % 1000 == 0:
        #print v

#d3 = [o, e, e], [o, o, e]
#d4 = [o, o, e, e], [o, e, o, e]

#for v in itertools.product(*d2):
    #vi = euler.seqToInt(v)
    #if is_reversible(vi):
        #print vi
#print '---'
#for i in xrange(11,100):
    #if is_reversible(i):
        #print

#def bit_generator(n):
    #m = n/2
    #if n % 2 == 1:
        #m += 1
    #bits = [(0, 1) for _ in xrange(m)]
    #for v in itertools.product(*bits):
        #v = list(v)
        #ext = [ 1-v[i] for i in xrange(n-m) ]
        #ext.reverse()
        #v += ext
        #yield v

#def oe_generator(n):
    #p = {
       #1 : (1,3,5,7,9),
       #0 : (2,4,6,8,0),
    #}
    #patterns = list(bit_generator(n))
    #patterns = patterns[:len(patterns)/2]
    #for pattern in patterns:
        #yield [ p[i] for i in pattern ]

#def candidates(n):
    #for i in xrange(1, n+1):
        #for oe in oe_generator(i):
            #for v in itertools.product(*oe):
                #if v[0] != 0 and v[-1] != 0:
                    #yield euler.seqToInt(v)

#cnt = 0
#for i in candidates(9):
    #if is_reversible(i):
        #cnt += 1
        ###print i
#print 'res=', cnt*2


#print 2**5 * 5**10
#1 0 implies 0 1

def is_reversible2(v):
    n = v + reverse_number(v)
    if v % 10 == 0:
        return False
    while n > 0:
        m = (n % 10)
        n /= 10
        if m % 2 == 0:
            return False
    return True

#print is_reversible(36)
cnt = 0
for i in xrange(10, 10**9):
    if i % 10**7 == 0:
        print i, cnt
    if is_reversible2(i):
        cnt += 1
print cnt
