
f = open('data/network.txt','r')
lines = f.readlines()
for line in lines:
    print '{',
    toks = line[:-2].split(',')
    for i,tok in enumerate(toks):
        if i != 0:
            print ',',
        if tok == '-':
            print 'Infinity',
        else:
            print tok,
        
    print '},'
f.close()

