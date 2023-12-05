def numeriInRiga ( riga):
        return [int(s) for s in riga.split() if s.isdigit()]


file = "/home/delle/Scrivania/Programmi/advent2032/day5/input.txt"
cards = [1]*214 # anche questo 6 (214) è da modificare, serve il numero di righe (o cards)
seeds = []
with open(file, 'r+') as f:
    for idx, line in enumerate (f):
        if  line.strip():
            if line.split()[0] == "seeds:":
                seeds = numeriInRiga(line) 
                break
# print(seeds)

minimo = 10000000000000000    # cambiare
for seed in seeds :
    # seed = 0
    modifica = True
    with open(file, 'r+') as f:
        for idx, line in enumerate (f):
            if  line.strip():
                if modifica:
                    if line.split()[0] != "seeds:":   # la prima linea non mi interessa
                    #     seed = numeriInRiga(line)[0]  #ogni volta incremento il valore dello zero 
                    # else: 
                        numeri = numeriInRiga(line)
                        # se sono qua so già che modifica è true
                        #cerco nei numeri se c è il range corretto rispetto al seed
                        if len(numeri) > 0 and seed >= numeri[1] and seed < numeri[1]+numeri[2]:
                            seed = seed - numeri[1] + numeri[0]
                            modifica = False
                        # devo anche considerare il caso in cui non ci sia nessuno?
            else :
                modifica = True
        # print(seed)
        if seed < minimo :
            minimo = seed

print(minimo)
