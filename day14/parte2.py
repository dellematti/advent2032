import copy

def column(matrix, i):
    s = ""
    for riga in matrix:
        s += riga[i]
    return s


#restituisce una lista di posizioni del ch in s ( len(s)-i e non i perchè la prima posizione è il max e non 0 )
def find(s, ch):
    return [len(s)-i for i, ltr in enumerate(s) if ltr == ch]


def tiltNord(matrice):
    for numeroColonna in range(len(matrice[0])):     # -1 per lo \n alla fine
        col = column(matrice,numeroColonna)
        for i in range (len(col)):           # faccio n volte il replace anche se servono meno iterazioni
            col = col.replace(".O", "O.")
        for idx in range (len(matrice)):    # ora in ogni riga sostituisco il carattere con quello della colonna ottenuta
            matrice[idx] = matrice[idx][:numeroColonna] + col[idx] + matrice[idx][numeroColonna + 1:]
    return matrice


def tiltEst(matrice):
    for numeroRiga in range(len(matrice)):
        for i in range (len(matrice[0])):           
            matrice[numeroRiga] = matrice[numeroRiga].replace("O.", ".O")
    return matrice


def tiltSud(matrice):
    for numeroColonna in range(len(matrice[0])):    
        col = column(matrice,numeroColonna)
        for i in range (len(col)):           
            col = col.replace("O.", ".O")
        for idx in range (len(matrice)):    
            matrice[idx] = matrice[idx][:numeroColonna] + col[idx] + matrice[idx][numeroColonna + 1:]
    return matrice


def tiltOvest(matrice):
    for numeroRiga in range(len(matrice)):
        for i in range (len(matrice[0])):           
            matrice[numeroRiga] = matrice[numeroRiga].replace(".O", "O.")
    return matrice


def doCycle(matrice):
    matrice = tiltNord(matrice)
    matrice = tiltOvest(matrice)
    matrice = tiltSud(matrice)
    matrice = tiltEst(matrice)
    return matrice




matrice = []
matricePartenza = []
with open("day14/input.txt", 'r+') as f:
    for line in f:
        matrice.append(line.strip())
        matricePartenza.append(line.strip())

stati = []
numeroCicli = 0
while(True):
    stati.append(copy.deepcopy(matrice))
    matrice = doCycle(matrice)
    numeroCicli += 1
    if matrice in stati:
        primaComparsa = stati.index(matrice)
        # print("la matrice era già presente all index", primaComparsa,"mentre ora siamo a ", numeroCicli)
        break
# da 3(primaComparsa) in poi si ripete ogni 7(numeroCicli-primaComparsa).Cioè la 3 la 10 la 17 la 24 etc sono uguali
cicliPerRipetizione = numeroCicli - primaComparsa
cicliUgualiAlMiliardo = (primaComparsa +((1000000000 - primaComparsa)% cicliPerRipetizione))
  
for i in range (cicliUgualiAlMiliardo):
    matricePartenza = doCycle(matricePartenza)

output = 0
for riga in range(len(matricePartenza)):
    col = column(matricePartenza,riga)
    posizioniSassi = find(col, "O")
    output += sum(posizioniSassi)

print(output)
# 99875