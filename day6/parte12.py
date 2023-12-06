def metodiVittoria(tempo, spazio) :
    sum =0
    for velocità in range (tempo):
        distanza = velocità*(tempo-velocità)
        if distanza > spazio:
            sum += 1
            if sum>0 and distanza <= spazio:
                return sum
    return sum


def numeriInRiga ( riga):
        return [int(s) for s in riga.split() if s.isdigit()]


file = "/home/delle/Scrivania/Programmi/advent2032/day6/input.txt"
time = []
space = []
with open(file, 'r+') as f:
    for idx, line in enumerate (f):
        if idx == 0:
            time = numeriInRiga(line)
        if idx == 1:
             space = numeriInRiga(line)
output = 1
for i in range (len(time)):
    output *= metodiVittoria(time[i], space[i])
print(output)