import pokereval

eval = pokereval.PokerEval()

def load():
    f = open('data/poker.txt','r')
    lines = f.readlines()
    f.close()
    del f
    return lines


def getHands(line):
    line = line.split(' ')
    line = [ t.strip() for t in line ]
    return line[:5],line[5:]

def convertHand(cards):
    return [ eval.string2card(c) for c in cards ]

cnt = 0
lines = load()
for line in lines:
    a,b = getHands(line)
    a = convertHand(a)
    b = convertHand(b)
    if eval.evaln(a) > eval.evaln(b):
        cnt += 1

print 'soln',cnt
