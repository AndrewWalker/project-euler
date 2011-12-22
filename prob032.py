import euler

lst = []
for a in range(1,8):
    for b in range(a+1,9):
        lst.append( (range(0,a),range(a,b),range(b,9)) )

#for i in lst:
#    print i

def seqToInt( seq ):
    return int( ''.join( [ str(i) for i in seq ] ) )

res = set()
for i in euler.permutations(range(1,10)):
    for a,b,c in lst:
        a = seqToInt([ i[j] for j in a ])
        b = seqToInt([ i[j] for j in b ])
        c = seqToInt([ i[j] for j in c ])
        if a*b == c:
            res.add(c)
            print a,b,c, '-', list(res)

print res

