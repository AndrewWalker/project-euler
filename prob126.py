"""Project Euler 126


0, [6]                          6
1, [6, 10, 6]                   22
2, [6, 10, 14, 10, 6]           46  [ w*h+4*i for i in range(2*layers) ]
4, [6, 10, 14, 18, 14, 10, 6]
5, [6, 10, 14, 18, 22, 18, 14, 10, 6]

    yyy
   yXXXy
  yXzzzXy
 yXz   zXy
yXz     zXy
yXz     zXy
 yXz   zXy
  yXzzzXy
   yXXXy
    yyy
"""
import unittest

def layer_size(w, h, l, layer = 0):
    if layer == 0:
        return l * w * h
    return 2*(w*h + h*l + w*l)
    # otherwise, a new layer (in the l direction) is like
    #
    #if layer == 1:
        #return
    #if layer == 2:
        #return layer(w, h, l, layer - 1) + 4*(l + w + h)
    #return 0
    #if layer == 3:
        #return 2*(w*h + h*l + w*l) + 8*(l + w + h)


class CuboidLayersTest(unittest.TestCase):
    def test_layer0(self):
        self.assertEquals(layer_size(3, 2, 1, layer = 0), 6)

    def test_layer1(self):
        self.assertEquals(layer_size(3, 2, 1, layer = 1), 22)

    def test_layer2(self):
        self.assertEquals(layer_size(3, 2, 1, layer = 2), 46)

    def test_layer3(self):
        self.assertEquals(layer_size(3, 2, 1, layer = 3), 78)

    def test_layer4(self):
        self.assertEquals(layer_size(3, 2, 1, layer = 3), 118)

    def test_layer4(self):
        self.assertEquals(layer_size(5, 1, 1, layer = 3), 22)


#def isum(n):
    #return n*(n+1)/2

#0, [6]                          6  6+0
#1, [6, 10, 6]                   22 18+4
#2, [6, 10, 14, 10, 6]           46 30+16
#4, [6, 10, 14, 18, 14, 10, 6]   78 42+36
#5, [6, 10, 14, 18, 22, 18, 14, 10, 6]

#print isum(0)*4
#print isum(1)*4
#print isum(2)*4 + 6

#def foo(n):
    #return (2*isum(n-1) + 1)*4+6*n

#for i in xrange(4):
    #print foo(i)
#lsts = [
    #[0],
    #[0,1,0],
    #[0,1,2,1,0],
    #[0,1,2,3,2,1,0],
    #[0,1,2,3,4,3,2,1,0]
#]
#for i, v in enumerate(lsts):
    #t = numpy.array(v)*4+6
    #print i, t, sum(v), numpy.sum(t)


