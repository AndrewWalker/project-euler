import euler

data  = open('words.txt','r').read()
words = data.split(',')
words = [ w[1:-1] for w in words ]
vals  = [ euler.alphaValue(w) for w in words ]
tnums = [ n*(n+1)/2 for n in range(25) ]
lst = [w for w,v in zip(words,vals) if v in tnums ]
print len(lst)
