import euler
import types

class Fraction:
    def __init__(self, num, den):
        self.num = num
        self.den = den

    def __hash__(self):
        c = self.cancel()
        return hash((c.num,c.den))

    def __add__(self, other):
        other = self.toFraction(other)
        return Fraction(self.num*other.den+other.num*self.den,self.den*other.den).cancel()

    def __sub__(self, other):
        other = self.toFraction(other)
        return Fraction(self.num*other.den-other.num*self.den,self.den*other.den).cancel()

    def __mul__(self, other):
        other = self.toFraction(other)
        return Fraction(self.num*other.num, self.den*other.den).cancel()

    def __div__(self, other):
        other = self.toFraction(other)
        return Fraction(self.num*other.den, self.den*other.num).cancel()

    def __eq__(self,other):
        if isinstance(other, Fraction):
            a = Fraction(self.num  * other.den, self.den*other.den )
            b = Fraction(other.num * self.den,  self.den*other.den )
            return a.num == b.num
        return NotImplemented

    def __ne__(self,other):
        result = self.__eq__(other)
        if result == NotImplemented:
            return NotImplemented
        return not result

    def __lt__(self,other):
        if isinstance(other, Fraction):
            a = self.innerMul( other.den ) 
            b = other.innerMul( self.den )
            return a.num < b.num
        return NotImplemented
       
    def __gt__(self,other):
        if isinstance(other, Fraction):
            a = self.innerMul( other.den ) 
            b = other.innerMul( self.den )
            return a.num > b.num
        return NotImplemented

    def __le__(self,other):
        if isinstance(other, Fraction):
            a = self.innerMul( other.den ) 
            b = other.innerMul( self.den )
            return a.num <= b.num
        return NotImplemented
       
    def __ge__(self,other):
        if isinstance(other, Fraction):
            a = self.innerMul( other.den ) 
            b = other.innerMul( self.den )
            return a.num >= b.num
        return NotImplemented
 
    def toFraction(self, other):
        if type(other) == types.IntType:
            return self.__add__( Fraction(other,1) )
        elif isinstance(other,Fraction):
            return Fraction(other.num,other.den)

    def innerMul(self, other):
        return Fraction(self.num*other, self.den*other)

    def toFloat(self):
        return self.num/float(self.den)

    def __str__(self):
        return 'Fraction(%d,%d)' % (self.num,self.den)

    def cancel(self):
        if self.num == 0:
            return Fraction(0,1)
        gcd = euler.gcd(self.num,self.den)
        return Fraction(self.num / gcd, self.den / gcd)

    def canCancel(self):
        if self.num == 0:
            return Fraction(0,1)
        gcd = euler.gcd(self.num,self.den)
        return gcd != 1
        

def test2():
    lst = []
    for a in range(10,100):
        for b in range(10,100):
            f = Fraction(a,b)
            if f.canCancel() and f < Fraction(1,1):
                lst.append(f)

    def commonPartialVal(f):
        a,b = tuple(euler.intToSeq(f.num))
        c,d = tuple(euler.intToSeq(f.den))
        return a==d or b==c

    def manipFrac(f):
        a,b = tuple(euler.intToSeq(f.num))
        c,d = tuple(euler.intToSeq(f.den))
        return Fraction(a,d), Fraction(b,c)
        


    lst = [item for item in lst if commonPartialVal(item)]
    res = []
    for item in lst:
        a,b = tuple(manipFrac(item))
        if item==a or item==b:
            res.append(item)
            print item

    print [ str(f) for f in res ]
    f = reduce( lambda a,b:a*b, res, Fraction(1,1) )
    print 'soln p1',f
    f.cancel()
    print 'soln p2',f
    print res[0]*res[1]*res[2]*res[3]

import unittest

class FractionTests(unittest.TestCase):

    def testMult(self):
        a = Fraction(1,2)
        b = Fraction(1,3)
        c = Fraction(1,6)
        self.assert_( a*b == c )

    def testMultAssoc(self):
        a = Fraction(1,2)
        b = Fraction(1,3)
        self.assert_( a*b == b*a )

    def testAddition(self):
        a = Fraction(1,2)
        b = Fraction(1,3)
        c = Fraction(5,6)
        self.assert_( a+b == c )

    def testAdditionAssoc(self):
        a = Fraction(1,2)
        b = Fraction(1,3)
        self.assert_( a+b == b+a )

    def testGT(self):
        a = Fraction(1,2)
        b = Fraction(1,3)
        self.assert_( (a > b) == True )
        self.assert_( (b > a) == False )
        self.assert_( (a > a) == False )

    def testGTEq(self):
        a = Fraction(1,2)
        b = Fraction(1,3)
        self.assert_( (a >= b) == True )
        self.assert_( (b >= a) == False )
        self.assert_( (a >= a) == True )

    def testLT(self):
        a = Fraction(1,2)
        b = Fraction(1,3)
        self.assert_( (b < a) == True )
        self.assert_( (a < b) == False )
        self.assert_( (a < a) == False )

    def testLTEq(self):
        a = Fraction(1,2)
        b = Fraction(1,3)
        self.assert_( (b <= a) == True )
        self.assert_( (a <= b) == False )
        self.assert_( (a <= a) == True )


if __name__ == "__main__":
    unittest.main()
    

