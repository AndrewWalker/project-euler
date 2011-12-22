
'''
Sieves?
'''

import euler

N = 10**6
totient = euler.phisieve(N+1)

def smartTotient(N):
    return sum([ totient[n] for n in range(1,N+1) ])-1

print smartTotient(N)


