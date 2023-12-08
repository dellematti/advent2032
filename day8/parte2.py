file = "/home/delle/Scrivania/Programmi/advent2032/day8/input.txt"
grafo = {}
stati = []
with open(file, 'r+') as f:
    istruzioni = f.readline()       
    istruzioni = istruzioni[0: len(istruzioni)-1]   # mi salvo le istruzioni
    for idx, line in enumerate (f):
        if  line.strip():
            parole = line.split()
            grafo[parole[0]] = (parole[2][1:4],parole[3][0:3]) 
            if parole[0][2] == "A":                 # e gli stati iniziali
                stati.append(parole[0])

numeroIstruzione = 0
output = 0


# for stato in stati:
#     volteCheZ = 0
#     print("\n\nnuovo stato di partenza")
#     while(volteCheZ < 5):   # metto un numero a caso per vedere su 5 volte ogni quanto torno a z
#         numeroIstruzione = numeroIstruzione % len(istruzioni)
#         istruzione = istruzioni[numeroIstruzione]
#         if istruzione == "L":
#             stato = grafo[stato][0]
#         else:
#             stato = grafo[stato][1]
#         output += 1
#         numeroIstruzione += 1
#         if stato[2] == "Z":
#             volteCheZ += 1  
#             print(output)
#             # break


# è ciclico, ogni stato ci mette n passaggi ad arrivare a z. Una volta arrivato, se va avanti per tornare a z ci metterà
# ancora n passaggi (anche se il successivo di z è diverso dallo stato iniziale)
# in pratica una volta arrivato allo stato finale, se proseguo è come se ricominciassi.
# Es :parto da AAA arrivo a ZZZ in 17873 passaggi, se non mi fermo e vado avanti , per tornare a una Z ci metto
# di nuovo 17873 passaggi, anche se non sono gli stessi che ho fatto prima


passaggiPerStato = []
for stato in stati:
    output = 0
    while(stato[2] != "Z"):
        numeroIstruzione = numeroIstruzione % len(istruzioni)
        istruzione = istruzioni[numeroIstruzione]
        if istruzione == "L":
            stato = grafo[stato][0]
        else:
            stato = grafo[stato][1]
        output += 1
        numeroIstruzione += 1
    passaggiPerStato.append(output)

# print(passaggiPerStato)


from math import gcd
lcm = 1
for i in passaggiPerStato:
    lcm = lcm*i//gcd(lcm, i)

print(lcm)
# 15746133679061