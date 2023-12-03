import re

def allIndexs(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]


filne = "/home/delle/Scrivania/Programmi/advent2032/day3/input.txt"

coordinateSimboli = []
output = 0
indexToNum = {}
with open(filne, 'r+') as f:
    for idx, line in enumerate (f):
        tmp = []
        tmp += (allIndexs(line, "*"));

        for indice in tmp :
            coordinateSimboli.append((idx,indice))
    f.seek(0)
    for idx, line in enumerate (f):
        indexToNum.update(dict(((idx, m.start()), int(m.group())) for m in re.finditer(r'\d+', line)))

#   print(indexToNum)

for rc in coordinateSimboli :
    print("nuovo asterisco")
    daModificare = True
    numero1 = 0
    numero2 = 0
    # print("Coordinate:")
    # print(rc[0],rc[1])
    for riga in range (rc[0]-1, rc[0]+2):
        for colonna in range (rc[1]-1, rc[1]+2) :
            adiacenteAsterisco = (riga,colonna)
            # print("    ",adiacenteAsterisco)
            # ora se per un asterisco trovo due numeri adiacenti, li moltiplico
            for key in indexToNum:
                value = indexToNum.get(key)
                # print(" numero:",key, value)
                # ora devo vedere per tutte le coordinate, con key ho solo quella iniziale
                # faccio un altro for, dalla coordinata iniziale, a quella + len(value)
                for index in range (key[1], key[1]+len(str(value))):
                    if adiacenteAsterisco == (key[0], index) :
                        # print("dentro l if",adiacenteAsterisco, value)
                        # print("numero", numero1, numero2)
                        if numero2 == 0 and numero1 != 0 and value != numero1:
                            numero2 = value
                        if numero1 == 0:
                            numero1 = value;
                        # print(numero1, numero2)
                        if numero1 != numero2 :
                            if numero1 != 0 and numero2 != 0:
                                if daModificare:
                                    # print("outputtttt",numero1,numero2)
                                    output += (numero1 * numero2)
                                    daModificare = False


print(output)
# 78915902