import euler

def ndigits(x):
    return len(euler.intToSeq(x))

def reverse_number(n):
    """Reverse the order of the digits in a number

    for abc, gives cba
        123, gives 321
    """
    seq = euler.intToSeq(n)
    seq.reverse()
    m = euler.seqToInt(seq)
    return m

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

vals = []
for i in xrange(1, 10000000):
    if i % 10000 == 0:
        print i, len(vals)
    if i % 10 == 0:
        continue
    digits = euler.digits(i + reverse_number(i))
    odd = [d%2==1 for d in digits]
    if all(odd):
        vals.append(i)
print len(vals)
