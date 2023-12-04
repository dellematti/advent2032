def numeriInRiga ( riga):
        return [int(s) for s in riga.split() if s.isdigit()]


file = "/home/delle/Scrivania/Programmi/advent2032/day4/input.txt"
cards = [1]*214 # anche questo 6 (214) è da modificare, serve il numero di righe (o cards)
with open(file, 'r+') as f:
    for idx, line in enumerate (f):
        numeri = numeriInRiga(line)
        numeriVincenti = numeri[:10] # per ora il 5 (10) lo metto a mano, so che | è dopo 5 numeri
        numeriMiei = numeri[10:]
        quantitàNumeriVincenti = 0
        for numero in numeriMiei:
             if numero in numeriVincenti :
                  quantitàNumeriVincenti += 1
        for i in range (idx + 1, idx + 1 + quantitàNumeriVincenti):
            cards[i] += 1*cards[idx]
print(sum(cards))  
# 13261850         