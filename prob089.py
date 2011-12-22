romanVal = {}
romanVal['I'] = 1
romanVal['V'] = 5
romanVal['X'] = 10
romanVal['L'] = 50
romanVal['C'] = 100
romanVal['D'] = 500
romanVal['M'] = 1000

def fromRomanNumeral( s ):
    v = 0
    i = 0
    while i < len(s):
        if i >= len(s)-1:
            v += romanVal[s[i]]
            i += 1
        else:
            # subtractive pair?
            a = romanVal[s[i]]
            b = romanVal[s[i+1]]
            if b > a:
                v += (b - a)
                i += 2
            else:
                v += a
                i += 1
    return v

def toRomanNumeral( v ):
    if v == 0:
        return ''
    if v < 4:
        return 'I' + toRomanNumeral(v-1)
    elif v == 4:
        return 'IV'
    elif v == 5:
        return 'V'
    elif v > 5 and v < 9:
        return 'V' + toRomanNumeral(v-5)
    elif v == 9:
        return 'IX'
    elif v >= 10 and v < 40:
        return 'X' + toRomanNumeral(v-10)
    elif v >= 40 and v < 50:
        return 'XL' + toRomanNumeral(v-40)
    elif v >= 50 and v < 90:
        return 'L' + toRomanNumeral(v-50)
    elif v >= 90 and v < 100:
        return 'XC' + toRomanNumeral(v-90)
    elif v >= 100 and v < 400:
        return 'C' + toRomanNumeral(v-100)
    elif v >= 400 and v < 500:
        return 'CD' + toRomanNumeral(v-400)
    elif v >= 500 and v < 900:
        return 'D' + toRomanNumeral(v-500)
    elif v >= 900 and v < 1000:
        return 'CM' + toRomanNumeral(v-900)
    elif v >= 1000:
        return 'M' + toRomanNumeral(v-1000)

def testToRoman():
    for i in range(1,1001):
        s = toRomanNumeral(i)
        assert(s!=None)
        print i,s

def testFromRoman():
    assert( 16 == fromRomanNumeral('XVI') )
    assert( 16 == fromRomanNumeral('XIIIIII') )
    assert( 16 == fromRomanNumeral('VVVI') )
    assert( 14 == fromRomanNumeral('VVIV') )
    assert( 1606 == fromRomanNumeral('MDCVI') )

saves = 0
f = open('data/roman.txt','r')
for line in f:
    line = line.strip()
    val  = fromRomanNumeral(line)
    new  = toRomanNumeral(val)
    print line,val,new
    lineSaving = len(line) - len(new)
    saves += lineSaving
    assert(lineSaving >= 0)
f.close()
del f
print 'soln',saves
