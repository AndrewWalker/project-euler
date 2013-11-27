import euler
import fractions

best = None
for i, t in enumerate(euler.phisieve(20000000)):
    if i < 2:
        continue
    v = float(fractions.Fraction(t , i -1))
    if not best or v < best:
        best = v
        print v
