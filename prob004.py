import euler

lst = []
for i in range(999,99,-1):
    for j in range(999,99,-1):
        if euler.palindrome(i*j):
            lst.append( i*j )
print max(lst)
