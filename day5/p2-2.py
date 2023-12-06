from copy import deepcopy

def numeriInRiga ( riga):
        return [int(s) for s in riga.split() if s.isdigit()]


file = "/home/delle/Scrivania/Programmi/advent2032/day5/input.txt"
seedsRange = []
with open(file, 'r+') as f:
    for idx, line in enumerate (f):
        if  line.strip():
            if line.split()[0] == "seeds:":
                seedsRange = numeriInRiga(line) 
                break
seeds = []
for idx, seedRange in enumerate(seedsRange):
    if idx % 2 == 0 :
        valoreIniziale = seedRange
    else :
        seeds.append((valoreIniziale, valoreIniziale+seedRange-1))   # sono compresi sia il primo che il secondo
# ORA HO I SEED (range dei seed)




rangeFase = []
rangeTot = []
with open(file, 'r+') as f:
    for idx, line in enumerate (f):
        numeri = numeriInRiga(line) 
        if  line.strip() :   # se la riga non è vuota faccio. altrimenti fase è quella successiva
            if len(numeri) > 0 and idx > 2:       # è la frase non è senza numeri (titoli delle fasi)
                inputRange = (numeri[1], numeri[1]+numeri[2]-1)
                outputRange = (numeri[0], numeri[0]+numeri[2]-1)
                rangeFase.append((inputRange, outputRange))
        elif idx > 2 :
            rangeTot.append(rangeFase)
            rangeFase = []

# ora in rangeTot ho per ogni fase i vari range






nuovoSeeds = []
for  fase in rangeTot:
    for seed in seeds :  
        modifica = True
        for rang in fase :  
            if modifica :
                inputRange = (rang[0])
                outputRange = (rang[1])
                           
                if seed[0] >= inputRange[0] and seed[1] <= inputRange[1]:
                    nuovoSeeds.append((seed[0]+(outputRange[0]-inputRange[0]) ,seed[1]+(outputRange[0]-inputRange[0])  ))
                    modifica = False
                elif seed[0] >= inputRange[0] and seed[0] <= inputRange[1] and seed[1] > inputRange[1]:
                    nuovoSeeds.append((seed[0]+(outputRange[0]-inputRange[0]) ,inputRange[1]+(outputRange[0]-inputRange[0])  ))
                    seeds.append((inputRange[1]+1, seed[1]))
                    modifica = False
                elif seed[0] < inputRange[0] and seed[1] >= inputRange[0] and seed[1] <= inputRange[1]: #avanzano a sinistra
                    nuovoSeeds.append((inputRange[0]+(outputRange[0]-inputRange[0]) ,seed[1]+(outputRange[0]-inputRange[0])  ))
                    seeds.append((seed[0], inputRange[0]-1))
                    modifica = False
                elif seed[0] < inputRange[0] and seed[1] > inputRange[1]: #avanzano a sinistra e destra
                    nuovoSeeds.append((inputRange[0]+(outputRange[0]-inputRange[0]) ,inputRange[1]+(outputRange[0]-inputRange[0])  ))
                    seeds.append((seed[0], inputRange[0]-1))
                    seeds.append((inputRange[1]+1, seed[1]))
                    modifica = False
        if modifica:
            nuovoSeeds.append(seed)
    seeds = deepcopy(nuovoSeeds)
    nuovoSeeds = []



min = float("inf")
for val in seeds:
    primo = val[0]
    if primo != 0 and primo < min:
        min = primo
print(min)
#  100165128
