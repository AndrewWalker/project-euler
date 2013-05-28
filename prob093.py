import fractions

def _exprs(expr, stack_depth, vals, ops):
    """ Generate postfix expressions recursively.
        `expr` is the expression so far, a list of values and operators.
        `stack_depth` is the depth of the stack created by expr.
        `vals` is a list of values remaining to add to the expression.
        `ops` is a list of possible operators to choose from.
    """
    if stack_depth == 1 and not vals:
        # This is a valid expression.
        yield expr
    if stack_depth > 1:
        # Try using an operator
        for o in ops:
            for e in _exprs(expr+[o], stack_depth-1, vals, ops):
                yield e
    if vals:
        # Vals are available, push one on the stack
        for e in _exprs(expr+[vals[0]], stack_depth+1, vals[1:], ops):
            yield e

def exprs(vals, ops):
    """ Generate postfix expressions created from `vals`, the list of values
        to use, and `ops`, the possible operators to combine them with.
    """
    return _exprs([], 0, vals, ops)

from euler import *

def f(lst):
    for p in permutations(lst):
        d = dict(zip('ABCD',p))
        for o in '+-*/':
            d[o] = o
        for e in exprs('ABCD','+-*/'):
            enew = [ d[ei] for ei in e ]
            yield enew

def evalpf(lst):
    nums = []
    for i in lst:
        if type(i) == str:
            a, b = nums[-2], nums[-1]
            nums = nums[:-2]
            if i == '+':
                nums.append(a + b)
            if i == '-':
                nums.append(a - b)
            if i == '*':
                nums.append(a * b)
            if i == '/':
                if b > 0:
                    nums.append(fractions.Fraction(a, b))
                else:
                    raise ValueError('bad')
        else:
            nums.append(i)
    return nums[0]

def evaled(lst):
    for e in f(lst):
        try:
            n = evalpf(e)
            if n > 0:
                if type(n) == fractions.Fraction:
                    if n.denominator == 1:
                        yield n.numerator
                else:
                    yield n
        except ValueError:
            pass

def longest_consecutive(lst):
    for i in xrange(1,len(lst)):
        if i not in set(lst):
            return i
    return len(lst)

def make_digits():
    for a in range(1,10):
        for b in range(a+1,10):
            for c in range(b+1,10):
                for d in range(c+1,10):
                    yield [a,b,c,d]

digits = list(make_digits())
for vals in digits:
    s = set(evaled(vals))
    s = list(sorted(s))
    c = longest_consecutive(s)
    if c > 41:
        print c, vals
        print s

