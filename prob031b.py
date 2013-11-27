#!/usr/bin/env python

#main :: IO ()
#main = print $ count [200,100,50,20,10,5,2,1] 200
#count :: [Integer] -> Integer -> Integer
#count _ 0      = 1
#count [c] _    = 1
#count (c:cs) s = sum $ map (count cs . (s-)) [0,c..s]


def count(cs, s):
    if s == 0:
        return 1
    elif len(cs) == 1:
        return 1
    else:
        partial = lambda x : count(cs[1:],s-x)
        ran = range(0, s+1, cs[0])
        return sum(map(partial, ran))

cs = [ 200,100,50,20,10,5,2,1]
print count(cs,200)
