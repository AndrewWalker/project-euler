def sumOfSquares(n):
    lst = range(1,n+1)
    lst = [ i**2 for i in lst ]
    return sum(lst)

def squareOfSum(n):
    lst = range(1,n+1)
    res = sum(lst)
    return res**2

def diff(n):
    return squareOfSum(n) - sumOfSquares(n)

# testcase
assert diff(10) == 2640 

# solution
print diff(100)
