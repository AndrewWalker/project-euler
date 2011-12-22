import euler

def alleq(seq):
    o = seq[0]
    for x in seq[1:]:
        if x != o:
            return False
    return True

def solset(x):
    lst = [(0,1,2),(3,2,4),(5,4,6),(7,6,8),(9,8,1)]
    #lst = [(0,1,2),(3,2,4),(5,4,1)]
    seq = [ [ x[i] for i in y ] for y in lst ]
    return seq

def clockwise(seq):
    for i in range(1,5):
        if seq[0][0] >= seq[i][0]:
            return False
    return True

def flatten(seq):
    lst = ''
    for i in seq:
        for j in i:
            lst += str(j)
    return lst

ran = range(10)
ran.reverse()
ran = [ i+1 for i in ran ]
for i,v in enumerate(euler.permutations( ran )):
    ss   = solset(v)
    sums = [ sum(i) for i in ss]
    if alleq(sums) and clockwise(ss):
        print v, ss, sums, clockwise(ss)
        gon = flatten(ss)
        if len(gon) == 16:
            print gon


