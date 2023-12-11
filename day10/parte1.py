class day10:

    matrice = []


    def spostati (coordinate, direzione, passi):   # 0 sopra 1 destra 2 sotto 3 sinistra
        riga = coordinate[0]
        colonna = coordinate[1]
        if riga == -1 or colonna == -1:
            return -1
        # print("entro nella funzione")
        # print(coordinate, direzione)
        # print(day10.matrice[riga][colonna])

        # if day10.matrice[riga][colonna] == "S":
        #     return passi
        
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
# print(day10.matrice)


import sys
sys.setrecursionlimit(40000)
# print(sys.getrecursionlimit())

strade = []
strade.append(day10.spostati( coordinateS ,0,0))
strade.append(day10.spostati( coordinateS ,1,0))
strade.append(day10.spostati( coordinateS ,2,0))
strade.append(day10.spostati( coordinateS ,3,0))


import math

for strada in strade:
    if strada != -1:
        print(math.ceil(strada/2))
        break
