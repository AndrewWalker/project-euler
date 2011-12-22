
def rightAngleTriangles(p):
    cnt = 0
    for a in range(1,p):
        for b in range(a,p-a):
            c = p - a - b
            if a*a + b*b - c*c == 0:
                cnt += 1
    return cnt

big = 0
for i in range(1000):
    v = rightAngleTriangles(i)
    if v > big:
        big = v
        print i,v
