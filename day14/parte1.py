def column(matrix, i):
    s = ""
    for riga in matrix:
        s += riga[i]
    return s


#restituisce una lista di posizioni del ch in s ( len(s)-i e non i perchè la prima posizione è il max e non 0 )
def find(s, ch):
    return [len(s)-i for i, ltr in enumerate(s) if ltr == ch]


file = open("day14/input.txt", 'r')
matrice = file.readlines()
output = 0
for riga in range(len(matrice)):
    col = column(matrice,riga)
    for i in range (len(col)):
        col = col.replace(".O", "O.")
    posizioniSassi = find(col, "O")
    output += sum(posizioniSassi)
print(output)
# 109833