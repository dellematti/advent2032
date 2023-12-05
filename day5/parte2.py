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
# print(seeds)
seeds = []
for idx, seedRange in enumerate(seedsRange):
    if idx % 2 == 0 :
        valoreIniziale = seedRange
    else :
            seeds.append((valoreIniziale, valoreIniziale+seedRange-1))   # sono compresi sia il primo che il secondo

print("seediniziali")
print(seeds)
nuovoSeeds = []



# minimo = 10000000000000000    # cambiare
# for seed in seeds :
for x in range (1) :
    seed = seeds[0]
    modifica = True
    with open(file, 'r+') as f:
        for idx, line in enumerate (f):
            # if modifica:
#                     if line.split()[0] != "seeds:":   # la prima linea non mi interessa
            if modifica and line.strip() and line.split()[0] != "seeds:":
                numeri = numeriInRiga(line)
                if len(numeri) > 0:
                    inputRange = (numeri[1], numeri[1]+numeri[2]-1)
                    outputRange = (numeri[0], numeri[0]+numeri[2]-1)
                    print("sto guardando il seed", seed)
                    print("range",inputRange, " -> ", outputRange)
                    print("\n")
                    print(seeds)
                    print("\n")
                    # VARI CASI DI RANGE
                    if seed[0] >= inputRange[0] and seed[1] <= inputRange[1]:
                        nuovoSeeds.append((seed[0]+(outputRange[0]-inputRange[0]) ,seed[1]+(outputRange[0]-inputRange[0])  ))
                        modifica = False
                    # quando li divido in range, le parti del seed che non ho ancora "filtrato", li rimetto in seed, perchè 
                    # possono ancora essere filtrati

                    elif seed[0] >= inputRange[0] and seed[0] <= inputRange[1] and seed[1] > inputRange[1]:
                        #quelli che "avanzano" a destra, li rimetto in seed
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
                    
                    #casi in cui solo un "pezzo" del seed entra nel range :   sono quelli sopra?
                    # else :
                    print("nuovi",nuovoSeeds)

                else:
                    print("\nNuovafase")
                    if modifica:
                        nuovoSeeds.append(seed)
                    modifica = True
                    # a nuovoSeeds ci aggiungo quelli rimasti in seed, che sono quelli che tanto restano costanti


# COSA FARE ORA: UNA VOLTA CHE UN RANGE È "PASSATO" DEVO SMETTERE DI GUARDARLO

print("\n")
print(seeds)
print("\n")
print(nuovoSeeds)





