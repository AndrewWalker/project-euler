import euler
import pickle
import os

maxv = 28123

def divisors(n):
    lst = [1] + list(euler.factors(n))
    lst.sort()
    return lst

def abundant(n):
    return sum(divisors(n)) > n

def abundantNumbers():
    abundNums = [ i for i in range(1,maxv+1) if abundant(i) ]
    s = set()
    for a in abundNums:
        for b in abundNums:
            s.add(a+b)
    s = list(s)
    s.sort()
    return s

def abundantMem():
    fname = '.abundant'
    if not os.path.exists(fname):
        print 'making'
        lst = abundantNumbers()
        pickle.dump(lst,open(fname,'w'))
        return lst
    else:
        print 'loaded'
        return pickle.load(open(fname,'r'))

if __name__ == "__main__":
    abund = abundantMem()
    abund = set(abund)
    abundSum = [ i for i in xrange(1,maxv) if i not in abund]
    print list(abund)[:15]
    print abundSum
    print sum(abundSum)
