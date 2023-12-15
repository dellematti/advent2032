def adventHash(step) :
    currentValue = 0
    for ch in step:
        currentValue = ((currentValue + ord(ch)) * 17) % 256
    return currentValue


def posizioneLenteNelBox(the_list, substring):
    for i, s in enumerate(the_list):
        if substring == s[:len(s)-2]:
              return i
    return -1


matrice = []
with open("day15/input.txt", 'r') as file:
    data = file.read().replace('\n', '')
steps = data.split(',')
# print(steps)


adventMappa = {}
output = 0
for step in steps:
    if "=" in step:
        labelValore = step.split("=")
        label = labelValore[0]
        valore = labelValore[1]
        posizioneBox = adventHash(label)
        if posizioneBox in adventMappa.keys():
            lens = adventMappa[posizioneBox]
            index = posizioneLenteNelBox(lens, label)
            if index != -1:
                adventMappa[posizioneBox][index] = label + " " + valore
            else:
               adventMappa[posizioneBox].append(label + " " + valore) 
        else:
            adventMappa[posizioneBox] = [label + " " + valore]
    elif "-" in step:
        label = step[0: len(step)-1]
        posizioneBox = adventHash(label)
        if posizioneBox in adventMappa.keys():
            index = posizioneLenteNelBox(adventMappa[posizioneBox], label)
            if index != -1:
                adventMappa[posizioneBox].pop(index)
# print(adventMappa)

for box in range (256):
    if box in adventMappa.keys():
        for slotIdx, slot in enumerate(adventMappa[box]):
            output += (box + 1) * (int(slotIdx)+1) * int(slot[-1])

print(output)
# 263211   soluzione