# parto al contrario, se devo mettere 1 3 6 parto mettendo prima il 6 poi il 3 poi 1

# per ogni riga tengo conto delle sequenze di # attaccate, tengo una lista di
# tuple con il range

import re
class day12:

    output = 0


    def numeriInRiga ( riga):
        return (re.findall("\d+", riga))


    def controllaRiga(riga):
        # print(day12.numeriInRiga(riga))
        numeri = (day12.numeriInRiga(riga))
        # non so se è più efficiente o no guardare quanti canc ho
        quanti = riga.count('#')
        s = 0
        for n in numeri:
            s += int(n)
        if s != quanti:
            return

        # print("\n",riga)
        cancDiFila = 0
        controllo = 0
        for ch in riga:
            if ch == "#":
                cancDiFila += 1
            else:
                if cancDiFila != 0:
                    # print("canc di fila", cancDiFila)
                    # print(int(numeri[controllo]))
                    if cancDiFila == int(numeri[controllo]):
                        controllo += 1
                        if controllo > len(numeri)-1:     # se i numeri sono stati uguali ogni volta
                            day12.output += 1
                            # print(riga)
                            return
                    else:
                        return
                cancDiFila = 0
                




    def sost (riga, cancelletto):
        for idx, ch in enumerate (riga):
            if ch == " " and cancelletto:
                # print(riga)
                day12.controllaRiga(riga)
                return
            if ch == "?":
                if cancelletto :
                    riga2 = ( riga[:idx] + "#" + riga[idx+1:])
                    day12.sost(riga2, True)
                    day12.sost(riga2, False)
                    return
                else:
                    riga2 = ( riga[:idx] + "." + riga[idx+1:])
                    day12.sost(riga2, True)
                    day12.sost(riga2, False)
                    return
            

import sys
sys.setrecursionlimit(40000)
file = "day12/input.txt"
with open(file, 'r+') as f:
    for idx, riga in enumerate (f):
        day12.sost(riga, True)
        day12.sost(riga, False)
        print(idx)

# riga = ".??..??...?##. 1,1,3"
# riga = "?###???????? 3,2,1"
# day12.sost(riga, True)
# day12.sost(riga, False)
print(day12.output)