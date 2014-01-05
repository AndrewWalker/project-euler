"""Efficient exponentiation

Question. Where to for research?

    Wikipedia
    http://en.wikipedia.org/wiki/Addition-chain_exponentiation

    Comment
    "Note that the problem of finding the shortest addition chain
    cannot be solved by dynamic programming, because it does not
    satisfy the assumption of optimal substructure"


    Stackoverflow
    http://stackoverflow.com/q/7330752/2246

    Comment
    References TAOCP vol 2 by Knuth (and so does wikipedia)


    Math stackexchange
    http://math.stackexchange.com/q/127685/703

    Comment
    References OEIS

    https://oeis.org/A003313/b003313.txt
"""
from pprint import pprint

def addition_chain():
    d = {}
    with open('b003313.txt','r') as fh:
        for line in fh:
            line = line.strip()
            if line:
                k, v = line.split()
                d[int(k)] = int(v)
    return d

m = addition_chain()
print sum(m[k] for k in xrange(1,201))
