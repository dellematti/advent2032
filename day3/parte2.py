import re

def allIndexs(riga, ch):
    return [i for i, ltr in enumerate(riga) if ltr == ch]


filne = "/home/delle/Scrivania/Programmi/advent2032/day3/input.txt"
coordinateAsterischi = []
indexToNum = {}
output = 0
with open(filne, 'r+') as f:
    for idx, line in enumerate (f):
        indexToNum.update(dict(((idx, m.start()), int(m.group())) for m in re.finditer(r'\d+', line)))
        tmp = []
        tmp += (allIndexs(line, "*"));
        for indice in tmp :
            coordinateAsterischi.append((idx,indice))

for rigaColonna in coordinateAsterischi :
    daModificare = True
    gear1 = 0
    gear2 = 0
    for riga in range (rigaColonna[0]-1, rigaColonna[0]+2):
        for colonna in range (rigaColonna[1]-1, rigaColonna[1]+2) :
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
                        if gear2 != 0 and daModificare :
                            output += (gear1 * gear2)
                            daModificare = False

print(output)
# 78915902

# 3 for sono costanti, quindi comunque dovrebbe andare O(asterischi*numeri)    
# (e si potrebbe contare anche il numero di cifre dei numeri...)