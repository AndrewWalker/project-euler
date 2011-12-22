import unittest
import euler
import sys

def isIncreasing(seq):
    for i in xrange(len(seq)-1):
        if seq[i+1] < seq[i]:
            return False
    return True

def isDecreasing(seq):
    for i in xrange(len(seq)-1):
        if seq[i+1] > seq[i]:
            return False
    return True

def isBouncy(n):
    seq = euler.intToSeq(n)
    return (not isIncreasing(seq)) and (not isDecreasing(seq))

class Tests112(unittest.TestCase):
    def test_increasing(self):
        self.assert_( isIncreasing(euler.intToSeq(134468))==True )
        self.assert_( isIncreasing(euler.intToSeq(66420))==False )
        self.assert_( isIncreasing(euler.intToSeq(155349))==False )

    def test_decreasing(self):
        self.assert_( isDecreasing(euler.intToSeq(134468))==False )
        self.assert_( isDecreasing(euler.intToSeq(66420))==True )
        self.assert_( isDecreasing(euler.intToSeq(155349))==False )

    def test_bouncy(self):
        self.assert_( isBouncy(134468)==False )
        self.assert_( isBouncy(66420)==False )
        self.assert_( isBouncy(155349)==True )

def bouncyGenerator():
    i = 0
    b = 0
    while 1:
        i += 1
        if isBouncy(i):
            b += 1
        yield (i,b)

if __name__ == "__main__":
    #unittest.main()

    for idx,v in enumerate(bouncyGenerator()):
        i,b = v
        r = (b*100/float(i))
        if r >= 99:
            print 'soln',idx,i,b,r
            break
        if idx % 50000 == 0:
            print idx,i,b,r


