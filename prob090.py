import euler

lst =[
((0,1),(1,0)),
((0,4),(4,0)),
((0,9),(9,0),(0,6),(6,0)),
((1,9),(9,1),(1,6),(6,1)),
((2,5),(5,2)),
((3,6),(6,3),(3,9),(9,3)),
((4,9),(9,4),(6,4),(4,6)),
((8,1),(1,8)),
]

def constr(a, b, v1, v2):
    if a in v1 and b in v2:
        return True

def row_or(row, v1, v2):
    for a, b in row:
        if constr(a, b, v1, v2):
            return True
    return False

def col_and(cols, v1, v2):
    for row in cols:
        if row_or(row, v1, v2) == False:
            return False
    return True

combs = set()
faces = list(euler.choose(range(10), 6))
for d1 in faces:
    for d2 in faces:
        if col_and(lst, d1, d2):
            a = tuple(d1)
            b = tuple(d2)
            ab = (a, b)
            if b < a:
                ab = (b, a)
            combs.add(ab)
print len(combs)
