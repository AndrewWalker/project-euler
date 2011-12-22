import euler

#print euler.ncr(1,0),euler.ncr(1,1)
#print euler.ncr(2,0),euler.ncr(2,1)

def pascal(rows):
    return [ euler.ncr(rows,i) for i in range(rows+1) ]

def pascalUnique(nrows):
    lst = []
    for i in range(nrows):
        lst += pascal(i) 
    lst = set(lst)
    lst = list(lst)
    return lst

lst = pascalUnique(50)
lst.sort()
for i,item in enumerate(lst):
    print i,len(lst),item,euler.primeFactors(item)
