# naive approach

def dot(v1, v2):
    return v1[0]*v2[0] + v1[1]*v2[1]

def is_right_angle(p0, p1, p2):
    delta01 = (p1[0]-p0[0], p1[1]-p0[1])
    delta12 = (p2[0]-p1[0], p2[1]-p1[1])
    return dot(delta01, delta12) == 0

def naive_points( xy_max ):
    for x1 in xrange(xy_max):
        for y1 in xrange(xy_max):
            yield (x1, y1)

def naive_triangle( xy_max ):
    p0 = (0, 0)
    for x1 in xrange(xy_max):
        for y1 in xrange(xy_max):
            for x2 in xrange(x1, xy_max):
                for y2 in xrange(y1, xy_max):
                    if x1 == 0 and y1 == 0:
                        continue
                    if x1 == x2 and y1 == y2:
                        continue
                    yield p0, (x1,y1), (x2,y2)

items = []
for p0, p1, p2 in naive_triangle(3):
    print p0, p1, p2
    #a = is_right_angle(p0, p1, p2)
    #b = is_right_angle(p1, p2, p0)
    #c = is_right_angle(p2, p0, p1)
    #if a or b or c:
        #items.append([p0, p1, p2])
#print len(items)
