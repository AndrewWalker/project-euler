import unittest
import euler

class TestFactors(unittest.TestCase):
    def testFactors(self):
        self.assert_(euler.factors(24) == set([2,3,4,6,8,12]))

    def testDivisors(self):
        self.assert_(euler.divisors(24) == set([1,2,3,4,6,8,12,24]))

    def testGCD1(self):
        self.assert_( euler.gcd(12,24) == 12 )

    def testGCD2(self):
        self.assert_( euler.gcd(18,12) == 6 )

    def testGCD3(self):
        self.assert_( euler.gcd(3,7) == 1 )

class Factorial(unittest.TestCase):
    def testFactorial(self):
        for i in range(1,20):
            a = euler.naive_factorial(i)
            b = euler.factorial(i)
            print a,b
            self.assert_( a == b)

if __name__ == "__main__":
    unittest.main()
        
