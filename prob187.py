'''Project Euler 187

Question. How to start?
Answer. Research
    Semiprimes less than 10^n
        http://oeis.org/A066265

    http://mathworld.wolfram.com/Semiprime.html
        SemiprimesLT[x_] := Total[Map[PrimePi[x/Prime[#]] - # + 1 &, Range[1, PrimePi[Sqrt[x]]]]]
        SemiprimesLT[10^8]

    Meh.
        http://mathworld.wolfram.com/notebooks/PrimeNumbers/Semiprime.nb
'''
