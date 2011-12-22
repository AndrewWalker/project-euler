
class Polynomial:
    def __init__(self, terms):
        self.terms = terms

    def eval(self,x):
        return sum( [ t*(x**i) for i,t in enumerate(self.terms) ] )

    def show(self):
        return ' + '.join( [ '%dx^%d' % (t,i) for i,t in enumerate(self.terms) ] )

#def f(n):
#    return (1,-1,1,-1,1,-1,1,-1,1,-1,1)

p = Polynomial( (1,-1,1,-1,1,-1,1,-1,1,-1,1) )
#p = Polynomial( (3,2,2) )
#print p.show()
#p = Polynomial( (0,0,0,1) )
for i in range(1,11):
    print p.eval(i)

