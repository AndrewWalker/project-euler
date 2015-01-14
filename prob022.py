import euler

line = open('names.txt','r').read()
line = line.split(',')
names = [ name[1:-1] for name in line ]
names.sort()
vals = [ euler.word_sum(name) for name in names ]

acc = 0 
for i,name,val in zip(range(1,len(names)+1),names,vals):
    acc += i*val
    if i == 938:
        print i,name,val
print acc
