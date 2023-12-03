import re

def allIndexs(s, ch):
    # return [i for i, ltr in enumerate(s) if bool(re.search([!£$%&/?*^+], s))]
    return [i for i, ltr in enumerate(s) if ltr == ch]


filne = "/home/delle/Scrivania/Programmi/advent2032/day3/input.txt"

coordinateSimboli = []
output = 0
with open(filne, 'r+') as f:
    for idx, line in enumerate (f):
        tmp = []
        # tmp += (allIndexs(line, "*")) + (allIndexs(line, "+")) +(allIndexs(line, "#")) + (allIndexs(line, "$")) ;
        # usare una regex in all index
        simboli =["!","£","$", "%","&","/","(",")","=","?","^","*","+","@","-","#"]
        for simbolo in simboli:
            tmp += allIndexs(line,simbolo)

        for indice in tmp :
            coordinateSimboli.append((idx,indice))
    f.seek(0)
    for idx, line in enumerate (f):
        indexToNum = dict((m.start(), int(m.group())) for m in re.finditer(r'\d+', line))
        for key in indexToNum:
            indiceInizio = key
            numero = (indexToNum.get(indiceInizio))
            # ora ho ad esempio 0 e 467, devo controllare se negli adiacenti cè un simbolo
            for riga in range (idx-1, idx+2):
                for colonna in range (indiceInizio - 1, indiceInizio + len(str(numero)) + 1) :
                    puntoAdiacente = (riga,colonna)
                    if puntoAdiacente in coordinateSimboli:
                        output += numero
                        # print(numero)
                        break




# print(coordinateSimboli)
print(output)
# 514969


