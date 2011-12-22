import euler

dirs = [ (0,1), (1,0), (0,-1), (-1,0) ]

def nextState(instr, x,y,d):
    if instr == 'F':
        dx,dy = dirs[d]
        return (x+dx,y+dy,d)
    elif instr == 'R':
        return (x,y,(d+1)%4)
    elif instr == 'L':
        return (x,y,(d-1)%4)
    else:
        return (x,y,d)

def recdragon(dmax,smax):
    strinit = 'Fa'
    sinit = (0,0,0)
    rules = {}
    rules['a'] = 'aRbFR'
    rules['b'] = 'LFaLb'
    numfs = 0

    def impl( s, state, depth ):
        for c in s:
            #print s,c,state,depth
            if c == 'a' or c == 'b':
                if depth < dmax:
                    for c,ns in impl( rules[c], state, depth+1 ):
                        state = ns
                        yield c,ns
            else:
                state = nextState(c, *state)
                yield c,state

    steps = 0
    for i,(c,s) in enumerate(impl(strinit, sinit, 0 )):
        if c == 'F':
            steps += 1
        if steps == smax:
            return s
        if steps % 1000 == 0:
            print '%.8f' % (steps/float(10**12))

#print recdragon(50,10**12)
    
            
def itdragon(s,dmax):

    def dragonstr(s):
        res = ''
        for c in s:
            if c == 'a':
                res +=  'aRbFR' 
            elif c == 'b':
                res +=  'LFaLb'
            else:
                res += c
        return res

    for i in range(dmax):
        s = dragonstr(s)
    return s

def walkSoln(s):
    state = (0,0,0)
    for c in s:
        state = nextState(c,*state)
        if c in 'LRF':
            print c,state
    return state

#s = itdragon('Fa',4)
#print s
#print walkSoln(s)

def itsolve():
    D0  = 'Fa'
    D10 = itdragon(D0,10)
    s = (0,0,0)
    steps = 0
    for c in D10:
        if c == 'F':
            steps += 1
        s = nextState(c,*s)
        if steps == 500:
            break
    print 'soln',s

def ass(n):
    if n == 0:
        return 'RFR'
    else:
        return ass(n-1) + 'R' + bss(n-1) + 'FR'

def bss(n):
    if n == 0:
        return 'LFL'
    else:
        return 'LF' + ass(n-1) + 'L' + bss(n-1)
        
def ste( c, x ):
    x,y,d,s = x
    if c == 'F':
        return (x+dirs[d][0],y+dirs[d][1],d,s+1)
    elif c == 'R':
        return (x,y,(d+1)%4,s)
    elif c == 'L':
        return (x,y,(d+1)%4,s)
    else:
        print 'c',c
        print 'x',x
        assert(1 == 0)

def add( s0, s1 ):
    x0,y0,d0,s0 = s0
    x1,y1,d1,s1 = rotate(s1,d0)
    return (x0+x1,y0+y1,d1,s0+s1)

def rotate( x, dd ):
    dd = dd % 4
    x,y,d,s = x
    if dd == 0:
        return (x,y,d,s)
    elif dd == 1:
        return (y,-x,(d+1)%4,s)
    elif dd == 2:
        return (-x,-y,(d+2)%4,s)
    elif dd == 3:
        return (-y,x,(d+3)%4,s)

def iterste( string, x=(0,0,0,0) ):
    for c in string:
        x = ste(c,x)
    return x

@euler.in_mem_memoize
def a(n):
    if n == 0:
        return iterste('RFR')
    else:
        x0 = a(n-1)
        x1 = iterste('R')
        x2 = b(n-1)
        x3 = iterste('FR')
        y0 = add(x0,x1)
        y1 = add(y0,x2)
        y2 = add(y1,x3)
        return y2

@euler.in_mem_memoize
def b(n):
    if n == 0:
        return iterste('LFL')
    else:
        x0 = iterste('LF')
        x1 = a(n-1)
        x2 = iterste('L')
        x3 = b(n-1)
        y0 = add( x0, x1 )
        y1 = add( y0, x2 )
        y2 = add( y1, x3 )
        return y2

def countSteps(c,d):
    if c == 'F':
        return 1
    elif c == 'a':
        return a(d)[3]
    elif c == 'b':
        return b(d)[3]
    else:
        return 0

def dragon(maxl,maxn):

    def impl(s,x,d):
        for c in s:
            y = None
            if c in 'FRL':
                y = iterste(c)
            elif c == 'a' and d < maxl:
                y = a(maxl-d)#('aRbFR',d+1,maxl)
            elif c == 'b' and d < maxl:
                y = b(maxl-d)#dragon('LFaLb',d+1,maxl)
            else:
                pass
            if y != None:
                if y[3] + x[3] < maxn:
                    x = add(x,y)
                else:
                    if c == 'a' and d < maxl:
                        y = impl('aRbFR',x,d+1)
                    if c == 'b' and d < maxl:
                        y = impl('LFaLb',x,d+1)
                    x = add(x,y)
        return x

    return impl('Fa',(0,0,0,0),0)

for i in range(10):
    print dragon(i,500),add(iterste('F'),a(i))
