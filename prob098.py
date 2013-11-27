import collections
from pprint import pprint
from euler import *
import math

def load_words():
    words = []
    with open("words.txt","r") as fh:
        words = fh.read().split(',')
        words = [ item[1:-1] for item in words ]
    return words

def anagramic_words(words):
    tmp = collections.defaultdict(list)
    for word in words:
        tmp[''.join(sorted(word))].append(word)
    res = {}
    for k,v in tmp.iteritems():
        if len(v) > 1:
            res[k] = v
    return res

def is_square_anagram(u, v):
    return False

def perfect_squares():
    res = []
    for i in xrange(10**5):
        if i**2 > 10**9:
            break
        res.append(i**2)
    return res

squares = set(perfect_squares())
words = load_words()
words = anagramic_words(words)

def is_square(n):
    return n in squares

def word_to_value(word, mapping):
    nums = [ mapping[c] for c in word ]
    return seqToInt(nums)

def check_match( u, v ):
    chars = ''.join(sorted(set(u)))
    for nums in permutations(range(0,10), len(chars)):
        d = dict(zip(chars, nums))
        if d[u[0]] == 0 or d[v[0]] == 0:
            continue
        uval = seqToInt([ d[c] for c in u ])
        vval = seqToInt([ d[c] for c in v ])
        if is_square(uval) and is_square(vval):
            yield max(uval, vval)

def biggest_match( u, v ):
    matches = [m for m in check_match(u, v)]
    if not matches:
        return 0
    return max(matches)

for k, vals in words.iteritems():
    print vals
    if len(vals) == 2:
        print biggest_match(vals[0], vals[1])
#print biggest_match('care', 'race')
#for nums in permutations(range(0,10),3):
    #print is_square(seqToInt(nums))



