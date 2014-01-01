"""Project Euler 128 - Hexagonal Tile Differences

Question. What are the neighbours of a tile?

    Question. How many tiles are there in each "ring"
    Answer.
        def f(n):
            if n == 0:
                return 1
            return 6*n

    Assumption. Tiles directly `up` from the tile number 1

    Question. What is the tile number of the tile in ring n that is up
    Answer.
        def c(n):
            return sum([f(i) for i in xrange(n)])+1

    Question. Which tiles are on an edge?
        n.b. edge tiles are neighboured by:
            2 tiles in the same ring
            2 tiles in the next ring
            2 tiles in the previous ring

    Question. Which tiles are on a corner?
        n.b. corner tiles a neighboured by:
            2 tiles in the same ring
            3 tiles in the next ring
            1 tile in the previous ring

"""

def cumsum(lst):
    cnt = 0
    for item in lst:
        cnt += item
        yield cnt

#def pairs(seq):
    #for i in xrange(len(seq)-1):
        #yield seq[i], seq[i+1]

#lst = [6*i for i in xrange(7)]
##print list(cumsum(lst))
#for i, j in pairs(list(cumsum(lst))):
    #print i+1, j

#lst = [1, 6, 12, 18]
#print list(cumsum(lst))

def f(n):
    if n == 0:
        return 1
    return 6*n

def c(n):
    return sum([f(i) for i in xrange(n)])+1

def ringno(n):
    i = 0
    while 1:
        if c(i+1)-1 >= n:
            return i
        i+=1

#print [c(i) for i in xrange(5)]
for i in xrange(1, 50):
    print ringno(i), i,


