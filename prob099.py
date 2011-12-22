import math

# Log identity 1:
#
# if x=b^y then y = log_b(x)
#
# Log identity 2:
#
# log_b(x) = log_k(x)/log_k(b)
#
#
# a^x > b^y
# log_a(a^x) > log_a(b^y)
# x > log_a(b^y)
# x > log_b(b^y)/log_b(a)
# x > y/log_b(a)

def readInput():
    f = open('data/base_exp.txt','r')
    lines = f.readlines()
    f.close()
    del f
    return [ [ int(t) for t in line.split(',') ] for line in lines ]

def gt(a,x,b,y):
    return x > (y/math.log(a,b))

def main():
    vals = readInput()
    a = 0
    aval = vals[a]
    for b,bval in enumerate(vals):
        if not gt(aval[0],aval[1],bval[0],bval[1]):
            a = b
            aval = bval
            print b,'>',a
        else:
            print a,'>',b

    # count lines from 1
    print a+1,aval


