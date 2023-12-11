def calcoloDistanza (primaCoordinata, secondaCoordinata) :
    return abs(secondaCoordinata[0]-primaCoordinata[0]) + abs(secondaCoordinata[1] - primaCoordinata[1])

def colonnaConSpazi (colonna, colonneVuote):
    tmp = 0
    for c in colonneVuote:
        if colonna > c:
            tmp += 1
        else :
            break
    return colonna + tmp


def rigaConSpazi (riga, righeVuote):
    tmp = 0
    for r in righeVuote:
        if riga > r:
            tmp += 1
        else :
            break
    return riga + tmp




fileName = "day11/input.txt"
output = 0
file = []
righeVuote = []

with open(fileName, 'r+') as f:
    riga = 0
    for line in f:
        elem = []
        if not "#" in line:
            righeVuote.append(riga)
        for colonna in range(0, len(line)):
            if line[colonna] != "\n":
                elem.append(line[colonna])
        file.append(elem)
        riga += 1

    

colonneVuote = []
for colonna in range(len(file[0])):
    presente = False
    for riga in range(len(file)):
        if file[riga][colonna] == "#":
            presente = True
    if not presente:
        colonneVuote.append(colonna) 
# print(colonneVuote)




coordinate = []
for riga in range(len(file)):
    for colonna in range(len(file[0])):
        if file[riga][colonna] == "#":
            coordinate.append((rigaConSpazi(riga,righeVuote), colonnaConSpazi(colonna,colonneVuote)))
# print(coordinate)

for idx in range(len(coordinate)-1):
    for idx2 in range(len(coordinate)-idx-1):
        output += calcoloDistanza(coordinate[idx], coordinate[idx+idx2+1])
print(output)