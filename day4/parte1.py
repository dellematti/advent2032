def numeriInRiga ( riga):
        return [int(s) for s in riga.split() if s.isdigit()]


file = "/home/delle/Scrivania/Programmi/advent2032/day4/input.txt"
output = 0
with open(file, 'r+') as f:
    for idx, line in enumerate (f):
        numeri = numeriInRiga(line)
        numeriVincenti = numeri[:10] # per ora il 5 lo metto a mano, so che | è dopo 5 numeri
        numeriMiei = numeri[10:]
        quantitàNumeriVincenti = 0
        for numero in numeriMiei:
             if numero in numeriVincenti :
                  quantitàNumeriVincenti += 1
        if quantitàNumeriVincenti > 0:
             output += 2**(quantitàNumeriVincenti-1)

print(output)           
