def posizioneRiflesso(matrice):
    # faccio i controlli per ogni possibile colonna e riga di partenza (ipotetici centri) 
    for i in range(len(matrice[0])-1):
        if controlloColonna(i,i+1, matrice,False):
            return i+1
    for i in range(len(matrice)-1):    #e righe
        if controlloRiga(i,i+1, matrice, False):
            return (i+1)*100
    return 0


def controlloRiga (sopra, sotto, matrix, unaSolaRigaDiversa):
    caratteriDifferenti = 0
    for i in range(len(matrix[sopra])):
        if matrix[sopra][i] != matrix[sotto][i]:
            caratteriDifferenti += 1
    if caratteriDifferenti > 1 or (unaSolaRigaDiversa and caratteriDifferenti == 1):
        return False
    if caratteriDifferenti == 1:
        unaSolaRigaDiversa = True
    if matrix[sopra] == matrix[sotto] or caratteriDifferenti == 1:    
        if sopra == 0 or sotto == len(matrix)-1:
            return unaSolaRigaDiversa
        else:
            return controlloRiga(sopra-1,sotto+1, matrix, unaSolaRigaDiversa)


def controlloColonna (sinistra, destra, matrix,unaSolaColonnaDiversa):
    caratteriDifferenti = 0
    colonnaSinistra = column(matrix, sinistra)
    colonnaDestra = column(matrix, destra)
    for i in range(len(colonnaSinistra)):
        if colonnaSinistra[i] != colonnaDestra[i]:
            caratteriDifferenti += 1
    if caratteriDifferenti > 1 or (unaSolaColonnaDiversa and caratteriDifferenti == 1):
        return False
    if caratteriDifferenti == 1:
        unaSolaColonnaDiversa = True
    if colonnaSinistra == colonnaDestra or caratteriDifferenti == 1:    
        if sinistra == 0 or destra == len(matrix[0])-1 :
            return unaSolaColonnaDiversa
        else:
            return controlloColonna(sinistra-1,destra+1, matrix, unaSolaColonnaDiversa)


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
            output += posizioneRiflesso(matrice)
            matrice.clear()
        else:
            matrice.append(line.strip())
        riga += 1
output += posizioneRiflesso(matrice)
print(output)
# 38063