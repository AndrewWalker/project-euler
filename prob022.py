def alphaValue(name):
    return sum([ ord(c)-ord('A')+1 for c in name ])

line = open('names.txt','r').read()
line = line.split(',')
names = [ name[1:-1] for name in line ]
names.sort()
vals = [ alphaValue(name) for name in names ]

acc = 0 
for i,name,val in zip(range(1,len(names)+1),names,vals):
    acc += i*val
    if i == 938:
        print i,name,val
print acc
