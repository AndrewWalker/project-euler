def palindrome(n):
	s = str(n)
	for i in range(len(s)/2):
		if s[i] != s[-(i+1)]:
			return False
	return True

lst = []
for i in range(999,99,-1):
    for j in range(999,99,-1):
        if palindrome(i*j):
            lst.append( i*j )
    print '.',
print lst
lst.sort()
print lst[-1]
