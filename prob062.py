import euler
import math
import profile

@euler.in_mem_memoize
def max_perm(n):
    seq = euler.intToSeq(n)
    seq.sort()
    seq.reverse()
    return seq

def test(n):
    maxperm = euler.seqToInt(max_perm(n**3))
    y = int( math.ceil( maxperm**(1./3) ) )
    return y

def isperm( a, b ):
    return max_perm(a) == max_perm(b)

def equivPerms( n ):
    x = n**3
    cubes =[ i for i in xrange(n+1,test(n)+4) if isperm(x,i**3) ]
    return cubes

def main():
    for i in range(1000, 1500):
        ep = len(equivPerms(i))+1
        if ep >= 5:
            print i,ep
            return
        else:
            if i % 50 == 0:
                print i

main()


