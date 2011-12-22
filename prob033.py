import euler

for i in range(10,100):
    for j in range(10,100):
        if i != j and ((i%10!=0) and (j%10!=0)):
            ifactors = euler.factors(i)
            jfactors = euler.factors(j)
            if ifactors.intersection(jfactors):
                print i,'/',j,' ',
