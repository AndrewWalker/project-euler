import euler

def numbers_with_n_digits(n):
    return xrange(10**(n-1), 10**n)

def prob30():
    cnt = 0
    # picking the upper bound here was guess work, but it makes
    # sense that you could prove this given some extra work
    for i in xrange(2, 7):
        for n in numbers_with_n_digits(i):
            digits = euler.digits(n)
            fifth_power_sum = sum([ d**5 for d in digits])
            if fifth_power_sum == n:
                cnt += n
    return cnt

print 'soln', cnt


