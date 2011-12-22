import euler


def tern( c, v0, v1 ):
    if c:
        return v0
    else:
        return v1

def reverse(s):
    lst = list(s)
    lst.reverse()
    return ''.join(lst)

def binaryString(n):
    lst = [ (1<<i) for i in range(20) ]
    res = [ tern(n&i == 0,0,1) for i in lst ]
    res = [ str(r) for r in res ]
    res = ''.join(res)
    res = res.rstrip('0')
    return reverse(res)   

lst = [ i for i in range(1000000) if euler.palindrome(i) ]
lst = [ i for i in lst if euler.palindrome(binaryString(i)) ]
for i in lst:
    print i,binaryString(i)

print sum(lst)
