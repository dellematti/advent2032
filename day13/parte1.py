def posizioneRiflesso(matrice):
    # faccio i controlli per ogni possibile colonna di partenza (ipotetico centro) 
    for i in range(len(matrice[0])-1):
        if controlloColonna(i,i+1, matrice):
            return i+1
    for i in range(len(matrice)-1):    #e righe
        if controlloRiga(i,i+1, matrice):
            return (i+1)*100
    return 0


def controlloRiga (sopra, sotto, matrix):
    if matrix[sopra] == matrix[sotto]:    
        if sopra == 0 or sotto == len(matrix)-1:
            return True
        else:
            return controlloRiga(sopra-1,sotto+1, matrix)
    return False


def controlloColonna (sinistra, destra, matrix):
    if column(matrix, sinistra) == column(matrix,destra):    
        if sinistra == 0 or destra == len(matrix[0])-1:
            return True
        else:
            return controlloColonna(sinistra-1,destra+1, matrix)
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
# 33735