import euler

d = [ sum(list(euler.factors(i)))+1 for i in range(10001) ]

s = set()
for a in range(10001):
    try:
        b = d[a]
        if d[b] == a and a != b:
            s.add( (min(a,b),max(a,b)) )
    except:
        pass

lst = []
for a,b in s:
    lst.append(a)
    lst.append(b)
print lst
print sum(lst)
