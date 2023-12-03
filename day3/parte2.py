import re

def allIndexs(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]


filne = "/home/delle/Scrivania/Programmi/advent2032/day3/input.txt"

coordinateAsterischi = []
indexToNum = {}
output = 0
with open(filne, 'r+') as f:
    for idx, line in enumerate (f):
        tmp = []
        tmp += (allIndexs(line, "*"));
        for indice in tmp :
            coordinateAsterischi.append((idx,indice))
    f.seek(0)
    for idx, line in enumerate (f):
        indexToNum.update(dict(((idx, m.start()), int(m.group())) for m in re.finditer(r'\d+', line)))
#   print(indexToNum)



for rc in coordinateAsterischi :
    daModificare = True
    gear1 = 0
    gear2 = 0
    for riga in range (rc[0]-1, rc[0]+2):
        for colonna in range (rc[1]-1, rc[1]+2) :
            coordinateAdiacentiAsterisco = (riga,colonna)
            # per ogni coordinata adiacente all asterisco, controllo se cè un numero in quel punto
            for coordinateInizialiNumero in indexToNum:
                value = indexToNum.get(coordinateInizialiNumero)
                # ora devo vedere per tutte le coordinate del numero, con key ho solo quella iniziale
                colonnaInizialeNumero = coordinateInizialiNumero[1]
                for colonnaNumero in range (colonnaInizialeNumero, colonnaInizialeNumero+len(str(value))):
                    coordinateNumero = (coordinateInizialiNumero[0], colonnaNumero)
                    if coordinateAdiacentiAsterisco == coordinateNumero :
                        if gear2 == 0 and gear1 != 0 and value != gear1:
                            gear2 = value
                        if gear1 == 0:
                            gear1 = value;
                        if gear1 != gear2 and gear1 != 0 and gear2 != 0 and daModificare :
                            output += (gear1 * gear2)
                            daModificare = False

print(output)
# 78915902