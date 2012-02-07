import euler
import numpy
import matplotlib.pyplot as plt

def naive_transition_matrix( n ):
    states = [ tuple(state) for state in euler.permutations( range(1,n+1) ) ]
    m = len(states)
    mat = numpy.zeros( (m,m) )
    state2id = dict(zip(states, range(len(states))))
    id2state = dict(zip(range(len(states)), states))
    choices = list(euler.choose(range(n), 2))
    for u in states[1:]:
        for i, j in choices:
            v = list(u)
            v[i], v[j] = v[j], v[i]
            v = tuple(v)
            mat[ state2id[u], state2id[v] ] = 1.0/len(choices)
    return numpy.matrix(mat)

def markov_chain_fundamental_by_inverse( mat ):
    return (numpy.identity(mat.shape[0]) - numpy.matrix(mat)).I
    
def markov_chain_fundamental_iterative( mat, iters = 100 ):
    """
    Alternative when you can't simply invert the matrix
    """
    return sum( mat**i for i in xrange(iters) )

# this is a fudged up way of getting the fundamental matrix of
# the markov chain
mat = naive_transition_matrix(4)[1:,1:]
fund = markov_chain_fundamental_by_inverse(mat)

## mean time to reach absorbing states
print numpy.sum(fund/float(mat.shape[0]+1))
