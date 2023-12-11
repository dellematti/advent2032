# come la parte 1, ma aggiungo una mappa per tenermi il path (coordinateToChar)

class day10:

    matrice = []
    coordinateToChar = {}     # tengo una mappa in cui salvo il path valido, e il simbolo in quella posizione


    def spostati (coordinate, direzione, passi):   # 0 sopra 1 destra 2 sotto 3 sinistra
        riga = coordinate[0]
        colonna = coordinate[1]
        if riga == -1 or colonna == -1:
            return -1

        day10.coordinateToChar[(riga,colonna)] = day10.matrice[riga][colonna]
        
        if direzione == 0 :
            if riga == 0:
                return -1
            prossimoCarattere = day10.matrice[riga-1][colonna]
            if prossimoCarattere != "|" and prossimoCarattere != "F" and prossimoCarattere != "7" and prossimoCarattere != "S":
                return -1
            if prossimoCarattere == "|":
                return day10.spostati((riga-1,colonna), 0, passi+1)
            if prossimoCarattere == "7":
                return day10.spostati((riga-1,colonna), 3, passi+1)
            if prossimoCarattere == "F":
                return day10.spostati((riga-1,colonna), 1, passi+1)
        if direzione == 1 :
            if colonna == len(day10.matrice[0]):
                return -1
            prossimoCarattere = day10.matrice[riga][colonna+1]
            if prossimoCarattere != "-" and prossimoCarattere != "J" and prossimoCarattere != "7" and prossimoCarattere != "S":
                return -1
            if prossimoCarattere == "-":
                return day10.spostati((riga,colonna+1), 1, passi+1)
            if prossimoCarattere == "J":
                return day10.spostati((riga,colonna+1), 0, passi+1)
            if prossimoCarattere == "7":
                return day10.spostati((riga,colonna+1), 2, passi+1)
        if direzione == 2 :
            if riga == len(day10.matrice):
                return -1
            prossimoCarattere = day10.matrice[riga+1][colonna]
            if prossimoCarattere != "|" and prossimoCarattere != "L" and prossimoCarattere != "J" and prossimoCarattere != "S":
                return -1
            if prossimoCarattere == "|":
                return day10.spostati((riga+1,colonna), 2, passi+1)
            if prossimoCarattere == "L":
                return day10.spostati((riga+1,colonna), 1, passi+1)
            if prossimoCarattere == "J":
                return day10.spostati((riga+1,colonna), 3, passi+1)
            
        if direzione == 3 :
            if colonna == 0:
                return -1
            prossimoCarattere = day10.matrice[riga][colonna-1]
            if prossimoCarattere != "-" and prossimoCarattere != "F" and prossimoCarattere != "L" and prossimoCarattere != "S":
                return -1
            if prossimoCarattere == "-":
                return day10.spostati((riga,colonna-1), 3, passi+1)
            if prossimoCarattere == "F":
                return day10.spostati((riga,colonna-1), 2, passi+1)
            if prossimoCarattere == "L":
                return day10.spostati((riga,colonna-1), 0, passi+1)
        return passi
        





fileName = "day10/input.txt"
with open(fileName, 'r+') as f:
    riga = 0
    for idxRiga, line in enumerate (f):
        day10.matrice.append(line)
        if (line.rfind("S") != -1):
            coordinateS = (idxRiga,line.rfind("S"))
        riga += 1
# print("coordinate partenza :", coordinateS, "\n")

import sys
sys.setrecursionlimit(40000)  # a caso
# print(sys.getrecursionlimit())

strada = -1
direzione = 0
while (strada == -1):
    day10.coordinateToChar.clear()
    strada = (day10.spostati( coordinateS ,direzione,0))
    direzione += 1

import math
print(math.ceil(strada/2))
# 6931



# --------------------- PARTE 2 ---------------------


# fileName = "day10/input.txt"
output = 0
with open(fileName, 'r+') as f:
    for idxRiga, line in enumerate (f):
        numeroVerticali = 0
        for idxColonna, ch in enumerate (line) :
            # ora vedo se è un "|" "J" "L" appartentente al path
            # in teoria implementandola diversa, dovrebbe funzionare anche con gli opposti ("7", "F") (?)
            # se passo ad esempio da F-J sono entrato/uscito per forza dal loop
            char = day10.coordinateToChar.get((idxRiga,idxColonna))
            if char == "|" or char == "J" or char == "L":
            # if char == "|" or char == "F" or char == "7":
                numeroVerticali += 1
            if char == None:     # se non era nella mappa allora potrebbe essere chiuso dal loop
                if (numeroVerticali % 2 != 0 ):   # sono dentro se ho trovato un numero pari di verticali
                    output += 1
print(output)
# 357