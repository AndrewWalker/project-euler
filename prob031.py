"""Project Euler 31 - Coin Sums

url: https://projecteuler.net/problem=31
status: complete
keywords: knapsack, change-making

Q. Anything else to read?
A. Yep,

    http://en.wikipedia.org/wiki/Change-making_problem
    http://en.wikipedia.org/wiki/Knapsack_problem

Q. Anything useful in the forum?
A. From the Haskell solution by mvz in https://projecteuler.net/thread=31
    
    main :: IO ()
    main = print $ count [200,100,50,20,10,5,2,1] 200
    
    count :: [Integer] -> Integer -> Integer
    count _ 0      = 1
    count [c] _    = 1
    count (c:cs) s = sum $ map (count cs . (s-)) [0,c..s]

Q. Was this hard?
A. Yep. found this one really hard
"""
import euler

coins = (1,2,5,10,20,50,100,200)
print euler.coin_change(coins, 200)

