basic = [ 'zero','one','two','three','four','five','six','seven','eight','nine']
teens = [ 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['---','---','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
hundred = 'hundred'

def towords(n):
    if n < 10:
        return basic[n]
    elif n < 20:
        return teens[n-10]
    elif n < 100:
        a = n / 10
        b = n % 10
        if b == 0:
            return tens[a]
        else:
            return tens[a] + '-' + towords(b)
    elif n < 1000:
        a = n / 100
        b = n % 100
        if b == 0:
            return towords(a) + ' hundred'
        else:
            return towords(a) + ' hundred and ' + towords(b)
    elif n == 1000:
        return 'one thousand'
    else:
        return '???'

words = [ towords(i) for i in range(1,1001) ]
words = [ w.replace(' ','') for w in words ]
words = [ w.replace('-','') for w in words ]
lens  = [ len(w) for w in words ]

#for w in words:
#    print w
print sum(lens)
