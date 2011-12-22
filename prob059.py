lowerCaseChars = range(97,123)
lcc = lowerCaseChars

def listPerms( lst ):
    if lst == []:
        yield []
    else:
        for i in lst[0]:
            for res in listPerms(lst[1:]):
                yield [i] + res


f = open('cipher1.txt','r')
line = f.read()
f.close()
del f
line = line.strip()
vals = line.split(',')
vals = [ int(i) for i in vals ]

def decrypt(vals,key):
    res = [ v ^ key[(i%len(key))] for i,v in enumerate(vals) ]
    return res

def keysearch():
    for key in listPerms([lcc,lcc,lcc]):  
        res =  decrypt(vals,key)
        res = [ chr(v) for v in res ]
        res = ''.join(res)
        if res.find('the') != -1 and res.find('and') != -1:
            print ''.join([chr(c) for c in key])        
            print res
        
# key is 'god'


def stringToKey(s):
    return [ ord(c) for c in s ]

res = decrypt(vals,stringToKey('god'))
sres = [ chr(v) for v in res ]
sres = ''.join(sres)
print sres,sum(res)
