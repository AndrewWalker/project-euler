"""Project Euler 126 - Cuboid Layers

url: https://projecteuler.net/problem=126
keywords: TBD
status: started

Q. What does the pattern look like?
A. 

2 x 3 x 1

0: [6]                          6
1: [6, 10, 6]                   22
2: [6, 10, 14, 10, 6]           46  [ w*h+4*i for i in range(2*layers) ]

2 x 2 x 2

0:        [8]
1:    [4, 16, 4]
2: [4, 8, 24, 8, 4]

Q. If there is a pattern, can write a function to get it
A. Yes. It is annoying to do so however


"""

def cuboid_layer(L,W,H, layers):
    """How many cuboids in each layer

    >>> cuboid_layer(3, 2, 1, 1)
    22
    >>> cuboid_layer(3, 2, 1, 2)
    46
    >>> cuboid_layer(3, 2, 1, 3)
    78
    >>> cuboid_layer(2, 2, 2, 1)
    24
    >>> cuboid_layer(2, 2, 2, 2)
    48
    >>> cuboid_layer(5, 1, 1, 1)
    22
    >>> cuboid_layer(5, 3, 1, 1)
    46
    >>> cuboid_layer(7, 2, 1, 1)
    46
    """
    # top and bottom
    c = 2*L*W 

    # middle 2sides of each type + 4H spacers per layer
    c += 2*L*H + 2*W*H + 4*H*(layers-1)

    # layers that aren't the top, bottom or middle
    for i in xrange(1, layers):
        c += 4*(L+W+2*(i-1))
    return c

def find_target(target = 154, N = 1000):
    """plays the role of C(target)

    >>> find_target( 22 ) 
    2
    >>> find_target( 46 ) 
    4
    >>> find_target( 78 ) 
    5
    >>> find_target( 118 ) 
    8
    """
    cnt = 0
    for i in xrange(1, N):
        for j in xrange(i, N):
            for k in xrange(j, N):
                if cuboid_layer(i, j, k, 1) > target:
                    break
                l = 1
                while 1:
                    size = cuboid_layer(i,j,k,l) 
                    if size == target:
                        cnt += 1
                    if size >= target:
                        break
                    l += 1
    return cnt

for i in xrange(1000):
    print i, find_target(i)



#if __name__ == "__main__":
    #import doctest
    #doctest.testmod()
