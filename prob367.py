import euler
import numpy

def naive( n ):
    mat = numpy.zeros( (n,n) )
    states = [ tuple(state) for state in euler.permutations( range(1,n+1) ) ]
    state2id = dict(zip(states, range(len(states))))
    id2state = dict(zip(range(len(states)), states))
    choices = list(euler.choose(range(n), 2))
    for u in states:
        for i, j in choices:
            v = list(u)
            v[i], v[j] = v[j], v[i]
            v = tuple(v)
            mat[ state2id[u], state2id[v] ] = 1.0/n
    print mat

naive(4)

