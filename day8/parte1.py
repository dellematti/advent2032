file = "/home/delle/Scrivania/Programmi/advent2032/day8/input.txt"
grafo = {}
with open(file, 'r+') as f:
    istruzioni = f.readline()       
    istruzioni = istruzioni[0: len(istruzioni)-1]
    for idx, line in enumerate (f):
        if  line.strip():
            parole = line.split()
            grafo[parole[0]] = (parole[2][1:4],parole[3][0:3]) 

numeroIstruzione = 0
output = 0
stato = "AAA"     
while(stato != "ZZZ"):
    numeroIstruzione = numeroIstruzione % len(istruzioni)
    istruzione = istruzioni[numeroIstruzione]
    if istruzione == "L":
        stato = grafo[stato][0]
    else:
        stato = grafo[stato][1]
    output += 1
    numeroIstruzione += 1

print(output)

