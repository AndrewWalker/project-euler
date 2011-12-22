from euler import in_file_cache
import euler

@in_file_cache
def millionPrimes():
    lst = euler.sieve(1000000)
    return lst

primes = millionPrimes()
mill = 1000000


def pickPrimes():
    biggest = 0
    bigs = -1
    for i in range(len(primes)):
        print '#',i
        for j in range(i+bigs-2,len(primes)):
            lst = primes[i:j]
            s = sum(lst)
            if s < mill:
                if s in primes:
                    if len(lst) > biggest:
                        biggest = len(lst)
                        bigs = s
                        print bigs,biggest
            else:
                break
                

pickPrimes()
