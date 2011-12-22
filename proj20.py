num = reduce(lambda a,b : a*b, range(1,101), 1)
print num
num = [ int(i) for i in list(str(num)) ]
print num
print sum(num)
