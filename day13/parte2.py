def posizioneRiflesso(matrice):
    # faccio i controlli per ogni possibile colonna di partenza (ipotetico centro) 
    for i in range(len(matrice[0])-1):
        if controlloColonna(i,i+1, matrice,False):
            return i+1
    for i in range(len(matrice)-1):    #e righe
        if controlloRiga(i,i+1, matrice, False):
            return (i+1)*100
    return 0


def controlloRiga (sopra, sotto, matrix, flag):
    numeroDifferenze = 0
    for i in range(len(matrix[sopra])):
        if matrix[sopra][i] != matrix[sotto][i]:
            numeroDifferenze += 1
    if numeroDifferenze > 1 or (flag and numeroDifferenze == 1):
        return False
    if numeroDifferenze == 1:
        flag = True

    if matrix[sopra] == matrix[sotto] or numeroDifferenze == 1:    
        if sopra == 0 or sotto == len(matrix)-1:
            if flag:
                return True
            else:
                return False
        else:
            return controlloRiga(sopra-1,sotto+1, matrix, flag)
    return False


def controlloColonna (sinistra, destra, matrix,flag):
    numeroDifferenze = 0
    colonnaSinistra = column(matrix, sinistra)
    colonnaDestra = column(matrix, destra)
    for i in range(len(colonnaSinistra)):
        if colonnaSinistra[i] != colonnaDestra[i]:
            numeroDifferenze += 1

    if numeroDifferenze > 1 or (flag and numeroDifferenze == 1):
        return False
    if numeroDifferenze == 1:
        flag = True

    if colonnaSinistra == colonnaDestra or numeroDifferenze == 1:    
        if sinistra == 0 or destra == len(matrix[0])-1 :
            if flag:
                return True
            else:
                return False
        else:
            return controlloColonna(sinistra-1,destra+1, matrix, flag)
    return False


def column(matrix, i):
    s = ""
    for riga in matrix:
        s += riga[i]
    return s



fileName = "day13/input.txt"
matrice = []
output = 0
with open(fileName, 'r+') as f:
    riga = 0
    for line in f:
        if line == "\n" :    # se la riga è vuota
            output += (posizioneRiflesso(matrice))
            matrice.clear()
        else:
            matrice.append(line.strip())
        riga += 1
output += (posizioneRiflesso(matrice))
print(output)
# 38063